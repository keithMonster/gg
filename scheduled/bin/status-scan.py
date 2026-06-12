#!/usr/bin/env python3
"""确定性 status-scan：巡检 monster/gg 定时任务与 NW/gg 健康状态。

替代原先的 claude -p prompt 版本。默认静默；发现异常时走全局 notify。
"""
from __future__ import annotations

import argparse
import json
import os
import re
import signal
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

HOME = Path.home()
MONSTER = HOME / "githubProject" / "monster"
GG = HOME / "githubProject" / "gg"
NOTIFY = HOME / ".agents" / "skills" / "notify" / "bin" / "notify.sh"
DEDUP_DIR = HOME / ".agents" / "skills" / "notify" / "dedup"
LABEL = "com.gg.status-scan"
SOURCE = "status-scan"
RUN_START = time.time()
MONTH = datetime.now().strftime("%Y-%m")
LOG_DIR = GG / "scheduled" / "logs"
LOG_FILE = LOG_DIR / f"{LABEL}.{MONTH}.log"
STALE_FAILURE_SECONDS = 6 * 60 * 60
DEDUP_SECONDS = 60 * 60
HARD_TIMEOUT_SECONDS = 600

TERMINAL_EXIT_RE = re.compile(r"(tick|L2 回炉|nw daily|inbox|auto_gg|候选池|prepped).*(完成|done|绿)|^完成", re.I)
LOG_TS_RE = re.compile(r"===== ([^ ]+) \[[^\]]+\] (start|end)(?: \(exit=(-?\d+)\))?")


@dataclass
class Alert:
    severity: str
    dimension: str
    message: str
    context: list[Path]
    task_id: str


def setup_timeout() -> None:
    def _handle_timeout(_signum: int, _frame: object) -> None:
        log(f"===== {datetime.now().isoformat(timespec='seconds')} [{LABEL}] end (exit=142) =====")
        sys.exit(142)

    signal.signal(signal.SIGALRM, _handle_timeout)
    signal.alarm(HARD_TIMEOUT_SECONDS)


def log(message: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    print(message)
    with LOG_FILE.open("a", encoding="utf-8") as f:
        f.write(message + "\n")


def run(cmd: list[str], cwd: Path | None = None, timeout: int = 30) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=str(cwd) if cwd else None, text=True, capture_output=True, timeout=timeout)


def latest_log_for(label: str) -> Path:
    root = MONSTER if label.startswith("com.monster.") else GG
    log_dir = root / "scheduled" / "logs"
    candidates = sorted(log_dir.glob(f"{label}.*.log"), key=lambda p: p.stat().st_mtime, reverse=True)
    if candidates:
        return candidates[0]
    return log_dir / f"{label}.{MONTH}.log"


def path_mtime(path: Path) -> float | None:
    try:
        return path.stat().st_mtime
    except FileNotFoundError:
        return None


def parse_iso_ts(value: str) -> float | None:
    try:
        return datetime.fromisoformat(value).timestamp()
    except ValueError:
        return None


def latest_completed_window(path: Path, before_ts: float | None = None) -> tuple[float | None, float | None, int | None]:
    if not path.exists():
        return None, None, None
    starts: list[float] = []
    latest: tuple[float | None, float | None, int | None] = (None, None, None)
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return latest
    for line in lines:
        match = LOG_TS_RE.search(line)
        if not match:
            continue
        ts = parse_iso_ts(match.group(1))
        if ts is None:
            continue
        if before_ts is not None and ts >= before_ts:
            continue
        kind = match.group(2)
        if kind == "start":
            starts.append(ts)
        else:
            start = starts[-1] if starts else None
            exit_code = int(match.group(3)) if match.group(3) is not None else None
            latest = (start, ts, exit_code)
    return latest


def launchd_labels() -> list[str]:
    result = run(["launchctl", "list"])
    labels: list[str] = []
    for line in result.stdout.splitlines():
        parts = line.split()
        if len(parts) >= 3:
            label = parts[-1]
            if re.fullmatch(r"com\.(monster|gg)\..+", label):
                labels.append(label)
    return sorted(set(labels))


def launchd_state(label: str) -> tuple[str | None, int | None]:
    result = run(["launchctl", "print", f"gui/{os.getuid()}/{label}"], timeout=15)
    state = None
    exit_code = None
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.startswith("state ="):
            state = line.split("=", 1)[1].strip()
        match = re.search(r"last exit code = (-?\d+)", line)
        if match:
            exit_code = int(match.group(1))
    return state, exit_code


def task_root(label: str) -> Path:
    return MONSTER if label.startswith("com.monster.") else GG


def recent_session_files(root: Path, start: float | None, end: float | None) -> Iterable[Path]:
    proj = HOME / ".claude" / "projects" / ("-Users-xuke-githubProject-monster" if root == MONSTER else "-Users-xuke-githubProject-gg")
    if not proj.exists():
        return []
    files = []
    for path in proj.glob("*.jsonl"):
        ts = path_mtime(path)
        if ts is None:
            continue
        if start is not None and ts < start - 60:
            continue
        if end is not None and ts > end + 60:
            continue
        files.append(path)
    return sorted(files, key=lambda p: p.stat().st_mtime, reverse=True)


def last_assistant_text(path: Path) -> str:
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError:
        return ""
    for line in reversed(lines):
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        if item.get("type") != "assistant":
            continue
        message = item.get("message") or {}
        parts = message.get("content") or []
        if not isinstance(parts, list):
            continue
        texts = [p.get("text", "") for p in parts if isinstance(p, dict) and p.get("type") == "text"]
        text = "\n".join(t for t in texts if t)
        if text:
            return text
    return ""


def business_ok_after_hang(label: str, log_path: Path) -> tuple[bool, Path | None]:
    start, end, _exit_code = latest_completed_window(log_path)
    for session in recent_session_files(task_root(label), start, end):
        text = last_assistant_text(session)
        if TERMINAL_EXIT_RE.search(text):
            return True, session
    return False, None


def effective_exit_for_self(exit_code: int | None, log_path: Path) -> tuple[int | None, float | None]:
    if exit_code in (None, 0):
        return exit_code, None
    _start, end, logged_exit = latest_completed_window(log_path, before_ts=RUN_START)
    if logged_exit is None:
        return exit_code, end
    return logged_exit, end


def scan_launchd() -> list[Alert]:
    alerts: list[Alert] = []
    for label in launchd_labels():
        state, raw_exit_code = launchd_state(label)
        log_path = latest_log_for(label)
        exit_code = raw_exit_code
        freshness_ts = path_mtime(log_path)

        if label == LABEL:
            exit_code, completed_end = effective_exit_for_self(raw_exit_code, log_path)
            freshness_ts = completed_end or freshness_ts

        if exit_code in (None, 0):
            continue

        if freshness_ts is not None and time.time() - freshness_ts > STALE_FAILURE_SECONDS:
            continue

        severity = "warning"
        task_id = label
        context = [log_path] if log_path.exists() else []
        meaning = {
            -9: "被 kill",
            124: "超时",
            137: "watchdog 升级 SIGKILL",
            142: "perl alarm 超时",
            143: "watchdog SIGTERM",
            127: "claude binary 找不到",
        }.get(exit_code, f"非零退出 {exit_code}")

        if exit_code in {142, 143, 137}:
            ok, session = business_ok_after_hang(label, log_path)
            if ok:
                severity = "info"
                task_id = f"{label}_hung_business_ok"
                if session:
                    context.append(session)
                message = f"{label} 进程退出 {exit_code}（{meaning}），但 session 终态显示业务已完成，按 hang 降级记录。"
            else:
                message = f"{label} 可能异常中断：exit={exit_code}（{meaning}），state={state or 'unknown'}。"
        else:
            message = f"{label} 任务失败：exit={exit_code}（{meaning}），state={state or 'unknown'}。"
            if exit_code == 127:
                severity = "critical"

        alerts.append(Alert(severity, f"launchd-fail-{label}", message, context, task_id))
    return alerts


def scan_morning_brief() -> list[Alert]:
    path = MONSTER / "harness-engineering" / "analysis" / "morning-brief.md"
    now = datetime.now()
    if not path.exists():
        if now.hour >= 9:
            return [Alert("warning", "morning-brief-missing", "NW morning-brief 09:00 后仍不存在。", [path], "morning-brief")]
        return []

    alerts: list[Alert] = []
    try:
        first = path.read_text(encoding="utf-8", errors="ignore").splitlines()[0] if path.stat().st_size else ""
    except OSError:
        first = ""
    age = time.time() - path.stat().st_mtime
    if "⚠️ NW 未产出" in first:
        alerts.append(Alert("warning", "morning-brief-warning-title", f"NW morning-brief 标题异常：{first}", [path], "morning-brief"))
    if age > 30 * 60 * 60:
        alerts.append(Alert("critical", "morning-brief-stale", "NW morning-brief 已超过 30 小时未更新。", [path], "morning-brief"))
    return alerts


def scan_nw_ledger() -> list[Alert]:
    path = MONSTER / "harness-engineering" / "analysis" / "proposals.jsonl"
    if not path.exists():
        return []
    items = []
    bad_lines = 0
    try:
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            if not line.strip():
                continue
            try:
                items.append(json.loads(line))
            except json.JSONDecodeError:
                bad_lines += 1
    except OSError as exc:
        return [Alert("warning", "nw-ledger-read", f"NW proposals.jsonl 读取失败：{exc}", [path], "nw-ledger")]

    unresolved = [item for item in items if item.get("status") == "pending"]
    l4 = sum(1 for item in items if item.get("status") == "L4_blocked" or (item.get("status") == "pending" and item.get("level") == "L4"))
    l5 = sum(1 for item in items if item.get("status") == "L5_pending" or (item.get("status") == "pending" and item.get("level") == "L5"))
    alerts: list[Alert] = []
    if bad_lines:
        alerts.append(Alert("warning", "nw-ledger-parse", f"NW proposals.jsonl 有 {bad_lines} 行解析失败。", [path], "nw-ledger"))
    if len(unresolved) > 30:
        alerts.append(Alert("warning", "nw-ledger-unresolved", f"NW 账本 pending 积压：unresolved={len(unresolved)}。", [path], "nw-ledger"))
    if l5 > 5:
        alerts.append(Alert("warning", "nw-ledger-l5", f"NW 账本 L5 待拍板过多：L5={l5}。", [path], "nw-ledger"))
    return alerts


def scan_gg_audit() -> list[Alert]:
    result = run(["python3", "scripts/audit.py", "--json"], cwd=GG, timeout=120)
    combined = result.stdout + "\n" + result.stderr
    if result.returncode == 0 and "[P0]" not in combined:
        return []
    severity = "critical" if "[P0]" in combined else "warning"
    message = f"gg audit 异常：exit={result.returncode}。"
    return [Alert(severity, "gg-audit", message, [GG / "scripts" / "audit.py"], "gg-audit")]


def should_notify(alert: Alert, dry_run: bool) -> bool:
    if dry_run:
        return False
    DEDUP_DIR.mkdir(parents=True, exist_ok=True)
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "_", f"{alert.severity}_{alert.dimension}")
    last = DEDUP_DIR / f"{safe}.last"
    last_ts = path_mtime(last)
    if last_ts is not None and time.time() - last_ts < DEDUP_SECONDS:
        last.touch()
        log(f"[dedup] skip {safe}")
        return False
    last.touch()
    return True


def notify(alert: Alert, dry_run: bool) -> None:
    context = ",".join(str(p) for p in alert.context)
    if dry_run:
        log(f"[dry-run] {alert.severity} {alert.task_id}: {alert.message} context={context}")
        return
    if not should_notify(alert, dry_run):
        return
    cmd = [str(NOTIFY), alert.severity, SOURCE, alert.message, "--task-id", alert.task_id, "--project", "gg"]
    if context:
        cmd.extend(["--context", context])
    result = run(cmd, cwd=GG, timeout=60)
    if result.returncode != 0:
        log(f"[notify] failed rc={result.returncode}: {result.stderr.strip() or result.stdout.strip()}")
    else:
        log(f"[notify] sent {alert.severity} {alert.task_id}: {result.stdout.strip()}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="只打印告警，不调用 notify / 不写 dedup")
    args = parser.parse_args()

    setup_timeout()
    log(f"===== {datetime.now().isoformat(timespec='seconds')} [{LABEL}] start (timeout={HARD_TIMEOUT_SECONDS}s, mode=script) =====")
    exit_code = 0
    try:
        alerts: list[Alert] = []
        for scanner in (scan_launchd, scan_morning_brief, scan_nw_ledger, scan_gg_audit):
            try:
                alerts.extend(scanner())
            except Exception as exc:  # noqa: BLE001 - 巡检失败不能阻断其他维度
                alerts.append(Alert("warning", scanner.__name__, f"{scanner.__name__} 扫描失败：{exc}", [], scanner.__name__))

        if not alerts:
            log("OK")
        else:
            log(f"WARN alerts={len(alerts)}")
            for alert in alerts:
                notify(alert, args.dry_run)
    except Exception as exc:  # noqa: BLE001
        exit_code = 1
        log(f"CRIT status-scan crashed: {exc}")
    finally:
        signal.alarm(0)
        log(f"===== {datetime.now().isoformat(timespec='seconds')} [{LABEL}] end (exit={exit_code}) =====")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())

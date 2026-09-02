#!/usr/bin/env python3
"""夜巡机械哨聚合：SCAN 段的机械判定从会话下沉到脚本。

**下沉的是判定手段，不是观察范围**（auto_gg.md §2 SCAN「拆焊」条款）。
脚本每项都跑全、不采样、不早退；省下的会话注意力留给 FOUND 三项语义判断
（跨夜模式 / 跨 track 反哺 / 辐射死链定性）——那三项是缺席型判断，
事件型传感器对它们结构性失明（essence `omission-failures-evade-event-driven-sensors` 07-28），
**全绿绝不等于无事可做**。

不在本脚本内的一项：**工具表 / model_id 两轴自核**。只有会话看得见自己的工具表，
脚本拿不到（`memory/substrate.md` 工具表节亲述：「本轴与 model_id 轴都不被
substrate_probe.py 机械核对——脚本只比 cli_version」）。该项永远留会话侧。

## 设计铁律：零匹配不是结论，是判据死亡与真无异常的同像点

`re.findall` / `re.split` 在判据失配时返回的是**语法合法的空集**，而空集有两个原像：
真的没有 ∪ 判据已经死了。传感器必须把这两者分开，否则它会用「我看过，都好」
的语气报告「我其实什么都没看见」。

**计数型输出不构成防线**——这是本脚本前身用血换来的：它的 `bets_due` 已经是计数型，
漂移下老老实实打出「Active 段 **0** 条在跟踪」，然后判 OK 全绿过关。N 就在报告里、
就是 0，照样没拦住。真正起效的只有两样：**零匹配走显式故障分支**（`if tracked == 0: ERROR`）
**+ selftest 反向注入**。判定量买的是次夜可比对性，不是防线本身——把它当防线
就是指望读者替脚本做核验（`trace-presence-substitutes-for-the-check-it-invites` 08-09）。

2026-08-13 设计会话实测，前身版本有 4 处静默报绿：

| 处 | 触发 | 前身行为 |
|---|---|---|
| `bets_due` | `bets.md` 的 `**到期**：` 格式漂移 | ok「无到期注（Active 段 **0** 条在跟踪）」 |
| `bets_due` | 注条目标题 `###`→`####` | 同上 |
| `broken_tail` | 日志 frontmatter `status:` 改名 | ok「近 7 夜 **status 全 done**」（7 夜实际全 in-progress） |
| `audit` | 字段名与 audit.py 输出对不上 | essence 违反 / 结构违规恒计 0 |

前三处是解析失败被当成「无异常」，第四处是字段契约漂移。共同形态 =
`fallback-detectability`(05-06)：失败被误判为成功时 fallback 永不触发。
**这不是脚本特有的病**——LLM 逐行读一份被改名成 `state:` 的 frontmatter，同样会报
「7 夜全 done」。所以别把它记成「机械化的代价」，它是解析型判定器的通病，
跟判定者是谁无关。

故本脚本所有传感器遵守：**解析不到 = ERROR（哨失灵），永不降级为 OK**；
每个 OK 分支写下来时必须先回答一句「零匹配时我走哪支」。

用法：
  python3 scripts/nightly_scan.py           # 人类可读报告
  python3 scripts/nightly_scan.py --json    # 机器可读

退出码：0 = 全绿 / 1 = 有 alert（需进 FOUND）/ 2 = 传感器自身故障（哨失灵，比 alert 更严重）

测试注入：`GG_ROOT` 环境变量覆盖仓根（selftest 造假仓用）；正常运行不设该变量。
"""
from __future__ import annotations

import datetime
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _common import ROOT as _REPO_ROOT

ROOT = Path(os.environ["GG_ROOT"]) if os.environ.get("GG_ROOT") else _REPO_ROOT
AUTO_GG_DIR = ROOT / "memory" / "auto_gg"
BETS = ROOT / "memory" / "bets.md"
EVAL_RUNS = ROOT / "eval" / "runs"
MONSTER = Path.home() / "githubProject" / "monster"

DARK_NIGHT_DAYS = 7      # 暗夜哨 / 断裂哨回看窗口（日历日）
EVAL_STALE_DAYS = 90     # eval 新鲜度门槛，来自 eval/README.md §3

OK, ALERT, ERROR = "ok", "alert", "error"


def sensor(name, status, summary, detail=None):
    return {"name": name, "status": status, "summary": summary, "detail": detail or []}


def _run(cmd, cwd=None, timeout=120):
    """跑子进程，返回 (returncode, stdout, stderr)；异常按 returncode=None 上报"""
    try:
        p = subprocess.run(cmd, cwd=cwd or ROOT, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout, p.stderr
    except Exception as e:
        return None, "", str(e)


def today():
    return datetime.date.today()


# ── 传感器 1：结构性健康（复用 audit.py） ────────────────────────────────
#
# 字段契约与 audit.py --json 输出绑死。**缺字段 = ERROR 不是 0**——
# 2026-08-13 实测前身把 `essence.append_only_violations`（不存在）当 0 读，
# 于是 KERNEL §3 append-only 硬约束的违反在报告里永远显示 0。

AUDIT_LIST_FIELDS = {
    "deadlinks": ["active_broken"],
    "orphans": ["orphans"],
    "essence": ["violations"],
    "structure": ["naming_violations", "state_missing_fields", "kernel_missing_sections",
                  "wc_sentinel_violations", "kernel_fuse_violations", "scan_coverage_violations"],
}


def scan_audit():
    rc, out, err = _run([sys.executable, "scripts/audit.py", "--json"])
    if rc is None:
        return sensor("audit", ERROR, f"audit.py 跑不起来：{err[:120]}")
    try:
        data = json.loads(out)
    except ValueError:
        return sensor("audit", ERROR, f"audit.py --json 输出不可解析（rc={rc}）")

    counts, missing = {}, []
    for section, fields in AUDIT_LIST_FIELDS.items():
        block = data.get(section)
        if not isinstance(block, dict):
            missing.append(f"{section}（整节缺失）")
            continue
        for f in fields:
            v = block.get(f)
            if not isinstance(v, list):
                missing.append(f"{section}.{f}")
                continue
            counts[f"{section}.{f}"] = v
    if missing:
        return sensor("audit", ERROR,
                      f"audit.py --json 字段契约漂移，{len(missing)} 项读不到（判定量不可信）",
                      [f"缺失/类型不符：{', '.join(missing)}",
                       "字段名以 audit.py run_all() 为准，改那边须同步本脚本 AUDIT_LIST_FIELDS"])

    total = sum(len(v) for v in counts.values())
    if total == 0:
        if rc != 0:
            return sensor("audit", ERROR,
                          f"audit 各项计数为 0 但 rc={rc}（计数口径与退出码不一致，哨不可信）")
        return sensor("audit", OK,
                      f"结构健康 0 违规（{len(counts)} 项判据全过，扫 {data['orphans']['total_files']} 份 .md）")

    detail = []
    for key, items in counts.items():
        if items:
            detail.append(f"{key} × {len(items)}：" + "; ".join(str(i)[:80] for i in items[:5]))
    return sensor("audit", ALERT, f"结构违规合计 {total}（audit rc={rc}）", detail)


# ── 传感器 2：基底 CLI 版本（复用 substrate_probe.py） ───────────────────

def scan_substrate():
    rc, out, err = _run([sys.executable, "scripts/substrate_probe.py"], timeout=60)
    line = (out or err).strip().splitlines()[-1] if (out or err).strip() else ""
    if rc is None:
        return sensor("substrate", ERROR, f"substrate_probe.py 跑不起来：{err[:120]}")
    if rc == 0:
        return sensor("substrate", OK, line or "CLI 版本与快照一致")
    if rc == 1:
        return sensor("substrate", ALERT, line or "CLI 版本 DIFF", ["四相分诊进 FOUND + 更新快照"])
    return sensor("substrate", ERROR, line or f"substrate_probe 异常 rc={rc}")


# ── 传感器 3：暗夜哨——近 7 日历日缺哪天日志 ──────────────────────────────

def scan_dark_night():
    """判据纯物理：文件在 / 不在。

    缺 ≠ 一定是调度 non-fire：日志由 auto_gg 会话自己在 SCAN 之后写，会话起了但在
    写日志前塌缩（collapse-before-log）同样缺文件。归因看该夜有无 `auto_gg(YYYY-MM-DD)`
    前缀 commit——有 commit 无日志 = 塌缩 / 收尾断裂；两者皆无 = 调度 non-fire
    （2026-09-02 体检订正：此前注解把"缺"单一归因为 non-fire，排查会漏掉塌缩形态）。

    不含今日——本夜日志由 auto_gg 自己在 SCAN 之后创建。
    """
    if not AUTO_GG_DIR.is_dir():
        return sensor("dark_night", ERROR, f"日志目录不存在：{AUTO_GG_DIR}")
    missing = []
    for i in range(1, DARK_NIGHT_DAYS + 1):
        d = today() - datetime.timedelta(days=i)
        if not (AUTO_GG_DIR / f"{d.isoformat()}.md").exists():
            missing.append(d.isoformat())
    present = DARK_NIGHT_DAYS - len(missing)
    if not missing:
        return sensor("dark_night", OK, f"近 {DARK_NIGHT_DAYS} 日历日日志 {present}/{DARK_NIGHT_DAYS} 在")
    return sensor("dark_night", ALERT,
                  f"近 {DARK_NIGHT_DAYS} 日日志 {present}/{DARK_NIGHT_DAYS} 在，缺 {len(missing)} 夜",
                  [f"缺席：{', '.join(sorted(missing))}（看该夜有无 auto_gg commit 分诊 non-fire / 塌缩，上报 FOUND + 进 parked）"])


# ── 传感器 4：收尾断裂哨——status 停在 in-progress ────────────────────────

def _frontmatter_field(text, field):
    m = re.search(rf"^{field}:\s*(.+)$", text, re.M)
    return m.group(1).strip().strip('"').strip("'") if m else None


def scan_broken_tail():
    """近 7 夜日志里 status 非 done 且非本夜文件 → 上一夜 §4 收尾断裂。

    **status 字段读不到 = ERROR**：2026-08-13 实测前身在字段改名后输出
    「近 7 夜 status 全 done」，而那 7 夜实际全部停在 in-progress——
    不是漏报，是报了一句假话。
    """
    if not AUTO_GG_DIR.is_dir():
        return sensor("broken_tail", ERROR, f"日志目录不存在：{AUTO_GG_DIR}")
    today_stem = today().isoformat()
    broken, unreadable, checked = [], [], 0
    for i in range(0, DARK_NIGHT_DAYS + 1):
        d = (today() - datetime.timedelta(days=i)).isoformat()
        f = AUTO_GG_DIR / f"{d}.md"
        if not f.exists() or d == today_stem:
            continue
        checked += 1
        status = _frontmatter_field(f.read_text(encoding="utf-8", errors="ignore"), "status")
        if status is None:
            unreadable.append(d)
        elif status != "done":
            broken.append(f"{d}: status={status}")
    if unreadable:
        return sensor("broken_tail", ERROR,
                      f"{len(unreadable)}/{checked} 夜日志读不到 status 字段（判据失配，非「无异常」）",
                      [f"读不到：{', '.join(unreadable)}",
                       "frontmatter 格式变了 → 先修判据再谈结论（日志格式 SSOT 在 auto_gg.md §3）"])
    if checked == 0:
        return sensor("broken_tail", ERROR, f"近 {DARK_NIGHT_DAYS} 夜无任何日志可检（与 dark_night 交叉核对）")
    if not broken:
        return sensor("broken_tail", OK, f"近 {DARK_NIGHT_DAYS} 夜 {checked} 份日志 status 全 done")
    return sensor("broken_tail", ALERT, f"{len(broken)}/{checked} 夜收尾断裂", broken +
                  ["修为 interrupted 留痕（不伪造 done——当夜实况已不可考）"])


# ── 传感器 5：押注到期 ────────────────────────────────────────────────────

def _active_section(text):
    """截 `## Active` 到下一个 `## ` 之间的正文"""
    m = re.search(r"^## Active\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def scan_bets_due():
    """到期日 ≤ 今日 且尚无 verdict 的 active 注 → 本夜必须物理核对结算。

    坑一（monster 侧首发现）：已结算的注仍留在 `## Active` 段（append-only，verdict 追加写回），
    所以「待结算」判据是「在 Active 段内 + 无 verdict 行」，不能只按段落切。

    坑二（2026-08-13 实测）：`**到期**：` 格式漂移或标题层级变化时，前身报
    「无到期注（Active 段 0 条在跟踪）」并判 OK——**tracked 掉到 0 是判据已死的物理信号**，
    不是「今天很平静」。故 tracked == 0 一律 ERROR。
    """
    if not BETS.exists():
        return sensor("bets_due", ERROR, f"账本不存在：{BETS}")
    text = BETS.read_text(encoding="utf-8", errors="ignore")
    body = _active_section(text)
    if not body.strip():
        return sensor("bets_due", ERROR, "bets.md 未找到 `## Active` 段（段落判据失配）")

    blocks = re.split(r"^### ", body, flags=re.M)[1:]
    due, tracked, settled, undated = [], 0, 0, []
    for block in blocks:
        head = block.splitlines()[0].strip()
        m = re.search(r"\*\*到期\*\*[：:]\s*(\d{4}-\d{2}-\d{2})", block)
        if not m:
            undated.append(head[:40])
            continue
        tracked += 1
        if re.search(r"^\s*-\s*\*\*verdict", block, re.M):
            settled += 1
            continue                      # 已结算，append-only 留在原位
        if datetime.date.fromisoformat(m.group(1)) <= today():
            due.append(f"{head}（到期 {m.group(1)}）")

    if tracked == 0:
        return sensor("bets_due", ERROR,
                      f"Active 段解析出 {len(blocks)} 个条目但 0 条读到到期日（判据已死，非「无到期注」）",
                      [f"无到期日的条目：{', '.join(undated[:6]) or '（一个条目都没切出来）'}",
                       "bets.md 格式 SSOT 在该文件头部协议；改格式须同步本传感器正则"])
    open_notes = tracked - settled
    if not due:
        return sensor("bets_due", OK,
                      f"无到期注（Active 段 {tracked} 条：{open_notes} 未结算 / {settled} 已结算留位）")
    return sensor("bets_due", ALERT, f"{len(due)}/{open_notes} 注到期待结算", due +
                  ["按判定条件物理核对，verdict 追加写回；结算帧 = 找茬不是复核"])


# ── 传感器 6：eval 新鲜度 ────────────────────────────────────────────────

def scan_eval_freshness():
    """最新 run 距今 >90 天 → FOUND（eval/README.md §3 的机械挂载）"""
    if not EVAL_RUNS.is_dir():
        return sensor("eval_freshness", ERROR, f"eval/runs 不存在：{EVAL_RUNS}")
    dates = []
    for f in EVAL_RUNS.glob("*.md"):
        m = re.match(r"(\d{4}-\d{2}-\d{2})", f.name)
        if m:
            dates.append((datetime.date.fromisoformat(m.group(1)), f.name))
    if not dates:
        return sensor("eval_freshness", ERROR, "eval/runs 无带日期的 run 文件（命名判据失配或从未跑过）")
    latest, name = max(dates)
    age = (today() - latest).days
    # 承重文件改动触发（2026-09-02 体检加）：最新 run 之后 KERNEL / CORE / constitution /
    # cc_agent 任一有 commit → eval 的被测对象已变、结论失效，不等 90 天线。
    # ROOT 不是 git 仓（selftest 夹具）或 git 失败 → 跳过本判据，不升 ERROR。
    changed = _bearing_changes_since(latest)
    if changed:
        return sensor("eval_freshness", ALERT,
                      f"最新 run {latest} 之后承重文件有 {len(changed)} 次 commit，eval 结论已失效",
                      [f"最新：{name}；承重改动：{' / '.join(changed[:6])}",
                       "跑一轮 eval（eval/README.md §3），或新建 eval/runs/<日期>_waived.md 写免跑理由（日期即新基线）"])
    if age <= EVAL_STALE_DAYS:
        return sensor("eval_freshness", OK,
                      f"最新 run {latest} 距今 {age} 天（共 {len(dates)} 份，线 {EVAL_STALE_DAYS} 天；承重文件无改动）")
    return sensor("eval_freshness", ALERT, f"最新 run {latest} 距今 {age} 天，已过 {EVAL_STALE_DAYS} 天线",
                  [f"最新：{name}；substrate 报 model_id 变更后无新 run 亦触发"])


EVAL_BEARING_FILES = ["KERNEL.md", "CORE.md", "constitution.md", "cc_agent.md"]


def _bearing_changes_since(since_date):
    """返回 since_date 之后（不含当日）触碰承重文件的 commit 简述列表；非 git 仓 / git 失败 → []"""
    after = (since_date + datetime.timedelta(days=1)).isoformat()
    rc, out, _ = _run(["git", "log", f"--since={after}", "--format=%h %ad %s", "--date=short",
                       "--", *EVAL_BEARING_FILES])
    if rc != 0:
        return []
    return [ln.strip()[:80] for ln in out.splitlines() if ln.strip()]


# ── 传感器 7：24h 变化面（gg + monster 双仓） ────────────────────────────

def _repo_24h(repo: Path, label: str):
    if not (repo / ".git").is_dir():
        return None, [f"{label}: 仓不存在或非 git 仓（{repo}）"]
    rc1, log, _ = _run(["git", "log", "--since=24 hours ago",
                        "--pretty=format:%h %ad %s", "--date=format:%m-%d %H:%M"],
                       cwd=repo, timeout=30)
    rc2, status, _ = _run(["git", "status", "--short"], cwd=repo, timeout=30)
    if rc1 is None or rc2 is None:
        return None, [f"{label}: git 命令跑不起来"]
    commits = [l for l in log.splitlines() if l.strip()]
    dirty = [l for l in status.splitlines() if l.strip()]
    lines = [f"{label}: {len(commits)} commit / {len(dirty)} 项工作区改动"]
    lines += [f"    {c}" for c in commits]
    lines += [f"    ~ {d}" for d in dirty]
    return (len(commits), len(dirty)), lines


def scan_git_24h():
    """不是告警项——把 24h 变化面摆出来供 FOUND 判断。

    双仓：gg 自身 + monster。跨仓辐射（gg 改动打断 monster 侧锚点）在 106 夜里
    至少出现两次（05-20 `CROSS_PROJECT_PREFIXES` 改名、08-03 分卷致 seam#4 失配），
    只看 gg 一侧的 git log 物理上看不见这类事。
    """
    detail, broke = [], []
    counts = {}
    for repo, label in ((ROOT, "gg"), (MONSTER, "monster")):
        c, lines = _repo_24h(repo, label)
        detail += lines
        if c is None:
            broke.append(label)
        else:
            counts[label] = c
    if "gg" in broke:
        return sensor("git_24h", ERROR, "gg 仓 git 读不到", detail)
    summary = " / ".join(f"{k} {v[0]}c+{v[1]}d" for k, v in counts.items())
    if broke:
        summary += f"（{', '.join(broke)} 未读到，跨仓辐射面不全）"
    return sensor("git_24h", OK, f"24h 变化面：{summary}", detail)


SENSORS = [scan_audit, scan_substrate, scan_dark_night, scan_broken_tail,
           scan_bets_due, scan_eval_freshness, scan_git_24h]

SENSOR_NAMES = ["audit", "substrate", "dark_night", "broken_tail",
                "bets_due", "eval_freshness", "git_24h"]

TAIL_NOTE = "工具表 + model_id 两轴不在脚本内，会话自核照旧；" \
            "全绿 ≠ 无事可做（缺席型判断无事件，见 FOUND 三项）"


def render(results):
    """每项都打印判定量——包括全绿项。

    只打 `name✓` 是内容无关的信任放大器（`trace-presence-substitutes-for-the-check-it-invites`
    08-09）；判定量（几条在跟踪 / 几份日志 / 几天）才是次夜识别计数漂移的物理指针。
    """
    alerts = [r for r in results if r["status"] == ALERT]
    errors = [r for r in results if r["status"] == ERROR]
    lines = []

    if errors:
        lines.append(f"⚠️ 哨失灵 {len(errors)} 项（比 alert 更严重——检验者本身坏了，先修判据再谈结论）")
        for r in errors:
            lines.append(f"  [{r['name']}] {r['summary']}")
            for d in r["detail"]:
                lines.append(f"      {d}")
        lines.append("")
    if alerts:
        lines.append(f"🔺 需进 FOUND {len(alerts)} 项")
        for r in alerts:
            lines.append(f"  [{r['name']}] {r['summary']}")
            for d in r["detail"]:
                lines.append(f"      {d}")
        lines.append("")

    green = [r for r in results if r["status"] == OK]
    if green:
        head = "全绿" if not alerts and not errors else "绿项"
        lines.append(f"{head}（{len(green)}/{len(results)} 项，判定量如下）：")
        for r in green:
            lines.append(f"  [{r['name']}] {r['summary']}")
    lines.append(TAIL_NOTE)
    return "\n".join(lines)


def main():
    results = [s() for s in SENSORS]
    if "--json" in sys.argv:
        print(json.dumps({"date": today().isoformat(), "sensors": results},
                         ensure_ascii=False, indent=2))
    else:
        print(render(results))
    if any(r["status"] == ERROR for r in results):
        return 2
    return 1 if any(r["status"] == ALERT for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())

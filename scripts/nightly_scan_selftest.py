#!/usr/bin/env python3
"""nightly_scan 反向验证：给每个传感器人为造故障，确认它真会报。

为什么必须有：没被人为造过一次阳性的报警器，与哑火在账本上同形。

**两类 case，缺一不可**：

1. **阳性（ALERT）**——真实故障发生时报不报。这是 monster 侧首版就有的。
2. **判据漂移（ERROR）**——被观察对象的**格式**变了、判据不再匹配时，
   传感器必须喊「我看不见」，而不是喊「我看过，都好」。
   2026-08-13 设计会话实测首版在三处格式漂移下静默报绿，其中
   `broken_tail` 在 7 夜全部 in-progress 时输出「近 7 夜 status 全 done」——
   不是漏报，是主动说了一句假话。

第 2 类是本 selftest 的重点：**bets.md 和 auto_gg 日志都是 auto_gg 自己每夜在写的通道**，
写入方不消费本 selftest 的一次性宣告（essence `one-shot-invariant-decays-under-live-append` 08-11），
所以格式漂移不是假想威胁，是这条通道的常态风险。

同理由，本 selftest 挂在 `scripts/hooks/pre-commit`：改 nightly_scan.py 必须先跑过它。
一次性验证会衰减，事件层触发才是飞轮（`rule-layer-flywheel` 04-24）。

阴性对照 = 一切正常时这些传感器必须全部静默。

用法：python3 scripts/nightly_scan_selftest.py    # 全过 exit 0，任一失败 exit 1
"""
from __future__ import annotations

import datetime
import importlib
import os
import sys
import tempfile
from pathlib import Path

TODAY = datetime.date.today()

# 假仓里的 audit.py 替身：输出与真 audit.py 同构的 --json，供 scan_audit 消费
FAKE_AUDIT_OK = '''#!/usr/bin/env python3
import json, sys
print(json.dumps({
    "deadlinks": {"active_broken": [], "archive_broken": 0},
    "orphans": {"orphans": [], "total_files": 42},
    "essence": {"commits": [], "violations": []},
    "structure": {"naming_violations": [], "state_missing_fields": [],
                  "kernel_missing_sections": [], "wc_sentinel_violations": [],
                  "kernel_fuse_violations": [], "scan_coverage_violations": []},
}))
sys.exit(0)
'''

# 字段契约漂移版：essence.violations 改名、structure 少一个字段
FAKE_AUDIT_DRIFTED = '''#!/usr/bin/env python3
import json, sys
print(json.dumps({
    "deadlinks": {"active_broken": [], "archive_broken": 0},
    "orphans": {"orphans": [], "total_files": 42},
    "essence": {"commits": [], "append_only_violations": 0},
    "structure": {"naming_violations": [], "state_missing_fields": [],
                  "kernel_missing_sections": []},
}))
sys.exit(0)
'''


def build_fake_repo(root: Path, audit_src: str = FAKE_AUDIT_OK):
    """造一个「一切正常」的最小 gg 仓：近 9 天日志齐全 + 无到期注 + 新鲜 eval"""
    (root / "memory" / "auto_gg").mkdir(parents=True)
    (root / "eval" / "runs").mkdir(parents=True)
    (root / "scripts").mkdir(parents=True)

    (root / "scripts" / "audit.py").write_text(audit_src, encoding="utf-8")

    for i in range(0, 9):
        d = (TODAY - datetime.timedelta(days=i)).isoformat()
        (root / "memory" / "auto_gg" / f"{d}.md").write_text(
            f"---\ndate: {d}\nstatus: done\nverdict: active\n---\n\n## SCAN\n\n略\n",
            encoding="utf-8")

    (root / "memory" / "bets.md").write_text(
        "# bets\n\n## Active\n\n"
        "### B1 / 2026-07-02 / far-future-bet\n\n"
        "- **置信**：0.6 · **到期**：2099-01-01 · **下注模式**：设计\n\n"
        "### B2 / 2026-07-02 / already-settled\n\n"
        "- **置信**：0.8 · **到期**：2026-01-01 · **下注模式**：设计\n"
        "- **verdict（2026-01-02 结算）**：✅ 命中\n\n"
        "## Settled\n\n略\n", encoding="utf-8")

    fresh = (TODAY - datetime.timedelta(days=10)).isoformat()
    (root / "eval" / "runs" / f"{fresh}_smoke.md").write_text("run\n", encoding="utf-8")


def load_module(root: Path):
    """按 GG_ROOT 重新加载模块——ROOT 是模块级常量，必须 reload 才生效"""
    os.environ["GG_ROOT"] = str(root)
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import nightly_scan
    return importlib.reload(nightly_scan)


CASES = []


def case(name, expect, audit_src=FAKE_AUDIT_OK):
    """expect ∈ {'alert', 'error'}——真实故障报 alert，判据漂移报 error"""
    def deco(fn):
        CASES.append((name, expect, audit_src, fn))
        return fn
    return deco


# ── 第 1 类：真实故障 → ALERT ────────────────────────────────────────────

@case("dark_night：删掉昨夜日志应报缺席", "alert")
def _dark_night(root, m):
    yesterday = (TODAY - datetime.timedelta(days=1)).isoformat()
    (root / "memory" / "auto_gg" / f"{yesterday}.md").unlink()
    return load_module(root).scan_dark_night(), yesterday


@case("broken_tail：status 停 in-progress 应报断裂", "alert")
def _broken_tail(root, m):
    d = (TODAY - datetime.timedelta(days=2)).isoformat()
    (root / "memory" / "auto_gg" / f"{d}.md").write_text(
        f"---\ndate: {d}\nstatus: in-progress\n---\n\n略\n", encoding="utf-8")
    return load_module(root).scan_broken_tail(), d


@case("bets_due：到期且无 verdict 应报待结算", "alert")
def _bets_due(root, m):
    p = root / "memory" / "bets.md"
    p.write_text(p.read_text(encoding="utf-8").replace("2099-01-01", "2026-01-01"),
                 encoding="utf-8")
    return load_module(root).scan_bets_due(), "B1"


@case("eval_freshness：run 超 90 天应报过线", "alert")
def _eval_freshness(root, m):
    runs = root / "eval" / "runs"
    for f in runs.glob("*.md"):
        f.unlink()
    stale = (TODAY - datetime.timedelta(days=120)).isoformat()
    (runs / f"{stale}_old.md").write_text("run\n", encoding="utf-8")
    return load_module(root).scan_eval_freshness(), stale


# ── 第 2 类：判据漂移 → ERROR（首版在这四处静默报绿） ────────────────────

@case("[漂移] bets 到期字段改名 → 必须喊看不见，不许报「无到期注」", "error")
def _bets_field_drift(root, m):
    p = root / "memory" / "bets.md"
    p.write_text(p.read_text(encoding="utf-8").replace("**到期**：", "到期日："),
                 encoding="utf-8")
    return load_module(root).scan_bets_due(), "判据已死"


@case("[漂移] bets 注条目标题 ###→#### → 必须喊看不见", "error")
def _bets_heading_drift(root, m):
    p = root / "memory" / "bets.md"
    p.write_text(p.read_text(encoding="utf-8").replace("\n### ", "\n#### "),
                 encoding="utf-8")
    return load_module(root).scan_bets_due(), "判据已死"


@case("[漂移] 日志 status 字段改名 + 全部 in-progress → 不许报「全 done」", "error")
def _status_field_drift(root, m):
    for i in range(1, 8):
        d = (TODAY - datetime.timedelta(days=i)).isoformat()
        (root / "memory" / "auto_gg" / f"{d}.md").write_text(
            f"---\ndate: {d}\nstate: in-progress\n---\n\n略\n", encoding="utf-8")
    return load_module(root).scan_broken_tail(), "读不到 status"


@case("[漂移] audit.py --json 字段契约变了 → 不许把缺字段当 0",
      "error", audit_src=FAKE_AUDIT_DRIFTED)
def _audit_contract_drift(root, m):
    return load_module(root).scan_audit(), "字段契约漂移"


def main():
    failures = []
    NEGATIVE = ["scan_audit", "scan_dark_night", "scan_broken_tail",
                "scan_bets_due", "scan_eval_freshness"]

    # ── 阴性对照：一切正常时全部传感器应静默 ──
    with tempfile.TemporaryDirectory() as td:
        root = Path(td) / "gg"
        build_fake_repo(root)
        m = load_module(root)
        baseline = [getattr(m, n)() for n in NEGATIVE]
        noisy = [r for r in baseline if r["status"] != m.OK]
        if noisy:
            failures.append("阴性对照失败——正常状态下这些传感器仍报警："
                            + ", ".join(f"{r['name']}({r['status']}:{r['summary']})" for r in noisy))
            print("❌ 阴性对照：正常仓被误报", flush=True)
        else:
            print(f"✅ 阴性对照：正常仓 {len(NEGATIVE)} 项传感器全静默", flush=True)

    # ── 逐个造故障 ──
    for name, expect, audit_src, fn in CASES:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "gg"
            build_fake_repo(root, audit_src)
            m = load_module(root)
            result, marker = fn(root, m)
            want = m.ALERT if expect == "alert" else m.ERROR
            hit = result["status"] == want
            evidence = result["summary"] + " | " + " ".join(result["detail"])
            traced = str(marker) in evidence
            if hit and traced:
                print(f"✅ {name}\n     → {result['summary']}", flush=True)
            else:
                why = (f"期望 {want} 实得 {result['status']}" if not hit
                       else f"状态对但证据里找不到「{marker}」")
                failures.append(f"{name}：{why}（summary={result['summary']}）")
                print(f"❌ {name} — {why}", flush=True)

    print()
    if failures:
        print(f"selftest 失败 {len(failures)} 项：")
        for f in failures:
            print("  - " + f)
        return 1
    n_alert = sum(1 for c in CASES if c[1] == "alert")
    n_error = sum(1 for c in CASES if c[1] == "error")
    print(f"selftest 全过：阴性对照 1 + 真实故障 {n_alert} + 判据漂移 {n_error}")
    print("  判据漂移那组保证的是：格式变了传感器会喊「我看不见」，不会喊「我看过，都好」")
    return 0


if __name__ == "__main__":
    sys.exit(main())

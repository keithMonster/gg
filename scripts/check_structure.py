#!/usr/bin/env python3
r"""memory/ 结构规范 + KERNEL 骨架 + state 字段完整性。

三个静态检查：
1. memory/{archival,design_sessions,reflections,audit,auto_gg}/*.md 命名规范
   规则：^\d{4}-\d{2}-\d{2}(_[a-z0-9._-]+)?\.md$
   例外：README.md / 归档子目录下的原文件（如 v0.3.0_levels_deprecated/）
2. memory/state.md 必填 yaml 字段齐全
3. KERNEL.md 三节骨架存在

退出码：违规总数（0 = 健康）。
"""
from __future__ import annotations
import datetime
import os
import re
import sys
import json
from pathlib import Path
from _common import ROOT

DATE_DIRS = (
    "memory/archival",
    "memory/design_sessions",
    "memory/reflections",
    "memory/audit",
    "memory/auto_gg",
)
DATE_FILE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}(_[a-z0-9._-]+)?\.md$")

STATE_REQUIRED = [
    "first_contact_done", "first_contact_date",
    "first_real_decision_done", "first_real_decision_date",
    "current_version", "created",
    "last_summoned_at", "last_decision_slug",
    "last_reflection_slug", "last_design_session_slug",
]

KERNEL_SECTIONS = [
    "## 1. 身份原点",
    "## 2. 铁律",
    "## 3. 最小生存循环",
]

# working_context.md 硬约束节的 6 条承重不变量哨兵（2026-06-10 围栏 L2 升级）。
# 任一消失 = 疑似被夜间瘦身静默洗白（KERNEL §2 / CORE §7 派生承重，见该文件 ⛔ 标记）。
# 连续多夜微删、单夜 diff 合理、N 夜后铁律消失——这个检查就是那道机械哨兵。
WC_SCAN_WINDOW_DAYS = 7   # SCAN 观察面哨的回看窗口，与 nightly_scan.DARK_NIGHT_DAYS 同宽

WC_SENTINELS = [
    "可逆性权力分层",
    "不执行决策",
    "连续两次明示",
    "不主动追问 git 层",
    "不用 json 承载规则",
    "不硬猜 context",
]


def check_naming():
    bad = []
    for d in DATE_DIRS:
        base = ROOT / d
        if not base.exists():
            continue
        # 只扫一级——子目录是归档的归档，不参与规则
        for fn in os.listdir(base):
            full = base / fn
            if full.is_dir():
                continue
            if not fn.endswith(".md"):
                continue
            if fn == "README.md" or fn == ".template.md":
                continue
            if not DATE_FILE_RE.match(fn):
                bad.append(f"{d}/{fn}")
    return bad


def check_state():
    path = ROOT / "memory/state.md"
    if not path.exists():
        return ["memory/state.md 不存在"]
    text = path.read_text(encoding="utf-8")
    return [f for f in STATE_REQUIRED if f not in text]


def check_kernel():
    path = ROOT / "KERNEL.md"
    if not path.exists():
        return ["KERNEL.md 不存在"]
    text = path.read_text(encoding="utf-8")
    return [s for s in KERNEL_SECTIONS if s not in text]


def check_working_context_sentinels():
    path = ROOT / "memory/working_context.md"
    if not path.exists():
        return ["memory/working_context.md 不存在"]
    text = path.read_text(encoding="utf-8")
    return [f"承重哨兵消失: {s}" for s in WC_SENTINELS if s not in text]


def check_kernel_fuse():
    """物理保险丝存在性（2026-07-02 建立，2026-08-13 扩到夜巡哨）。

    两个 hook 都是「规则从 prompt 层落到事件层」的物理落点，被移除/失活 = 保险丝被静默拆除：
    - `pre-commit`：KERNEL 铁律 3（连续两次确认）+ nightly_scan selftest 强制
    - `commit-msg`：auto_gg.md §1.1「夜间不得改夜巡哨源码」

    字段名保持 kernel_fuse_violations 不变——它有下游消费者（audit.py / nightly_scan.py /
    gg-audit skill），改名的辐射面大于命名精确性的收益。
    """
    import subprocess
    bad = []
    for name, what in (("pre-commit", "KERNEL 保险丝 + selftest 强制"),
                       ("commit-msg", "夜巡哨夜间写权保险丝")):
        hook = ROOT / "scripts/hooks" / name
        if not hook.exists():
            bad.append(f"scripts/hooks/{name} 不存在（{what}被移除）")
        elif not os.access(hook, os.X_OK):
            bad.append(f"scripts/hooks/{name} 失去可执行权限（{what}失活）")
    try:
        r = subprocess.run(
            ["git", "config", "core.hooksPath"],
            cwd=ROOT, capture_output=True, text=True, timeout=5,
        )
        if r.stdout.strip() != "scripts/hooks":
            bad.append(f"core.hooksPath != scripts/hooks（当前: {r.stdout.strip() or '未设置'}，保险丝未接入）")
    except Exception as e:
        bad.append(f"core.hooksPath 检查失败: {e}")
    return bad


def check_scan_coverage():
    """SCAN 观察面完整性哨（2026-08-13 设计会话建立）。

    `auto_gg.md §2` 的「SCAN 不允许简化」被拆焊后：**意图留硬**（观察面不许缩小，
    每项必须有物理判定结果落进日志）+ **形态降默认**（判定手段不限，机械项走脚本）。
    拆焊后意图必须仍机械可检，否则退化成豁免开洞
    （essence `hard-rule-welds-intent-to-form-breaks-at-first-legal-deviant` 08-05）。

    本检查就是那个「仍机械可检」：夜巡日志正文里 7 个传感器名必须齐全，
    缺任一 = 该夜观察面缩小。判据纯物理（字符串在不在），不判断内容对错。
    """
    since = datetime.date(2026, 8, 14)   # 脚本化生效日；此前的日志不适用本判据
    today = datetime.date.today()
    if not (ROOT / "memory/auto_gg").is_dir():
        return ["memory/auto_gg 目录不存在"]
    try:
        from nightly_scan import SENSOR_NAMES
    except Exception as e:
        return [f"nightly_scan.py 导入失败，SCAN 覆盖面无法核对（哨失灵）: {e}"]

    bad = []
    for i in range(0, WC_SCAN_WINDOW_DAYS):
        d = today - datetime.timedelta(days=i)
        if d < since or d == today:      # 本夜日志由 auto_gg 在 SCAN 之后才写完
            continue
        f = ROOT / "memory/auto_gg" / f"{d.isoformat()}.md"
        if not f.exists():
            continue                     # 缺席由 nightly_scan 的 dark_night 哨负责，不在此重复报
        text = f.read_text(encoding="utf-8", errors="ignore")
        miss = [n for n in SENSOR_NAMES if n not in text]
        if miss:
            bad.append(f"{d.isoformat()} SCAN 观察面缺 {len(miss)}/{len(SENSOR_NAMES)} 项: {', '.join(miss)}")
    return bad


def run():
    return {
        "naming_violations": check_naming(),
        "state_missing_fields": check_state(),
        "kernel_missing_sections": check_kernel(),
        "wc_sentinel_violations": check_working_context_sentinels(),
        "kernel_fuse_violations": check_kernel_fuse(),
        "scan_coverage_violations": check_scan_coverage(),
    }


def main():
    result = run()
    if "--json" in sys.argv:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        bad = result["naming_violations"]
        print(f"memory/ 日期命名: {len(bad)} 个违规")
        for b in bad:
            print(f"  {b}")
        miss = result["state_missing_fields"]
        print(f"\nstate.md 字段: {len(miss)} 个缺失")
        for m in miss:
            print(f"  {m}")
        ks = result["kernel_missing_sections"]
        print(f"\nKERNEL.md 骨架: {len(ks)} 节缺失")
        for k in ks:
            print(f"  {k}")
        wc = result["wc_sentinel_violations"]
        print(f"\nworking_context.md 承重哨兵: {len(wc)} 条消失")
        for w in wc:
            print(f"  ⛔ {w}")
        kf = result["kernel_fuse_violations"]
        print(f"\nKERNEL 物理保险丝: {len(kf)} 个问题")
        for k in kf:
            print(f"  ⛔ {k}")
        sc = result["scan_coverage_violations"]
        print(f"\nSCAN 观察面完整性: {len(sc)} 夜缺项")
        for s in sc:
            print(f"  ⛔ {s}")
    total = (len(result["naming_violations"])
             + len(result["state_missing_fields"])
             + len(result["kernel_missing_sections"])
             + len(result["wc_sentinel_violations"])
             + len(result["kernel_fuse_violations"])
             + len(result["scan_coverage_violations"]))
    sys.exit(total)


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))
    main()

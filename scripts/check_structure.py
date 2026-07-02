#!/usr/bin/env python3
"""memory/ 结构规范 + KERNEL 骨架 + state 字段完整性。

三个静态检查：
1. memory/{archival,design_sessions,reflections,audit,auto_gg}/*.md 命名规范
   规则：^\d{4}-\d{2}-\d{2}(_[a-z0-9._-]+)?\.md$
   例外：README.md / 归档子目录下的原文件（如 v0.3.0_levels_deprecated/）
2. memory/state.md 必填 yaml 字段齐全
3. KERNEL.md 三节骨架存在

退出码：违规总数（0 = 健康）。
"""
from __future__ import annotations
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
    """KERNEL 物理保险丝存在性（2026-07-02 建立）。
    pre-commit hook 是铁律 3 的事件层执行；hook 被移除/失活 = 保险丝被静默拆除。
    """
    import subprocess
    bad = []
    hook = ROOT / "scripts/hooks/pre-commit"
    if not hook.exists():
        bad.append("scripts/hooks/pre-commit 不存在（KERNEL 保险丝被移除）")
    elif not os.access(hook, os.X_OK):
        bad.append("scripts/hooks/pre-commit 失去可执行权限")
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


def run():
    return {
        "naming_violations": check_naming(),
        "state_missing_fields": check_state(),
        "kernel_missing_sections": check_kernel(),
        "wc_sentinel_violations": check_working_context_sentinels(),
        "kernel_fuse_violations": check_kernel_fuse(),
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
    total = (len(result["naming_violations"])
             + len(result["state_missing_fields"])
             + len(result["kernel_missing_sections"])
             + len(result["wc_sentinel_violations"])
             + len(result["kernel_fuse_violations"]))
    sys.exit(total)


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))
    main()

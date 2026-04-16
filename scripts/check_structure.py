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
            if fn == "README.md":
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


def run():
    return {
        "naming_violations": check_naming(),
        "state_missing_fields": check_state(),
        "kernel_missing_sections": check_kernel(),
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
    total = (len(result["naming_violations"])
             + len(result["state_missing_fields"])
             + len(result["kernel_missing_sections"]))
    sys.exit(total)


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))
    main()

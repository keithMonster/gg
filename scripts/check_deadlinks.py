#!/usr/bin/env python3
"""死链扫描。只输出数据，不做观点。

分类规则：
- 归档文件（memory/{archival,design_sessions,...}/）里的死链记为 archive，不属于活跃问题
- 噪音目标（glob / 占位符 / 模板 / 正则）完全跳过，不验证也不记数
- 跨项目目标（cc-space/ 等）记为 cross_project，不属于死链
- 其余验证存在性——有一条路径存在即通过

退出码：活跃死链数（0 = 健康）。
"""
from __future__ import annotations
import os
import sys
import json
from pathlib import Path
from _common import (
    ROOT, walk_md_files, extract_refs, is_archive,
    is_noise_target, is_cross_project,
)


def run():
    active_broken = []
    archive_broken = 0
    cross_project_refs = 0
    noise_refs = 0
    total_refs = 0

    for rel in walk_md_files():
        src_is_archive = is_archive(rel)
        full = ROOT / rel
        with open(full, encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                for kind, target in extract_refs(rel, line):
                    total_refs += 1
                    if is_noise_target(target):
                        noise_refs += 1
                        continue
                    if is_cross_project(target):
                        cross_project_refs += 1
                        continue
                    src_dir = full.parent
                    from_src = (src_dir / target).resolve()
                    from_root = (ROOT / target).resolve()
                    if from_src.exists() or from_root.exists():
                        continue
                    if src_is_archive:
                        archive_broken += 1
                    else:
                        active_broken.append({
                            "src": rel,
                            "line": lineno,
                            "target": target,
                            "kind": kind,
                        })
    return {
        "total_refs": total_refs,
        "noise_refs": noise_refs,
        "cross_project_refs": cross_project_refs,
        "archive_broken": archive_broken,
        "active_broken": active_broken,
    }


def main():
    result = run()
    as_json = "--json" in sys.argv
    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"扫描引用总数: {result['total_refs']}")
        print(f"  噪音（glob/占位符/模板）跳过: {result['noise_refs']}")
        print(f"  跨项目引用: {result['cross_project_refs']}")
        print(f"  归档死链（不修）: {result['archive_broken']}")
        print(f"  活跃死链: {len(result['active_broken'])}")
        if result["active_broken"]:
            print()
            by_file: dict[str, list] = {}
            for b in result["active_broken"]:
                by_file.setdefault(b["src"], []).append(b)
            for src in sorted(by_file):
                print(f"● {src}")
                for b in by_file[src]:
                    print(f"    L{b['line']}: {b['target']}  [{b['kind']}]")
    sys.exit(len(result["active_broken"]))


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))
    main()

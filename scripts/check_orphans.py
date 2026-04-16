#!/usr/bin/env python3
"""孤儿文件检查 + 体积 Top 报告。

孤儿定义：活跃（非归档）的 .md 文件，没有被其他任何 .md 通过路径或反引号引用。
入口文件（README / KERNEL / CLAUDE / 三种模式入口等）排除——它们是被外部 Read 的。

严格匹配策略：
- 完整相对路径（如 `memory/state.md` 或 `memory/state.md` 出现在正文）
- 反引号包裹的路径/文件名（如 `state.md`）
- markdown 链接的 target 能解析到本文件
不做子串模糊匹配——避免误判"有提到 state.md 的文档都算引用了 memory/state.md"。

退出码：孤儿数（0 = 健康）。
"""
from __future__ import annotations
import os
import sys
import json
from pathlib import Path
from _common import (
    ROOT, walk_md_files, extract_refs, is_archive, ENTRY_FILES,
    is_noise_target, is_cross_project,
)


def build_ref_index():
    """扫一遍所有文件，产出 {resolved_abs_path: [(src, line)]}"""
    index: dict[str, list] = {}
    for rel in walk_md_files():
        full = ROOT / rel
        with open(full, encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                for kind, target in extract_refs(rel, line):
                    if is_noise_target(target) or is_cross_project(target):
                        continue
                    src_dir = full.parent
                    for candidate in [(src_dir / target).resolve(),
                                      (ROOT / target).resolve()]:
                        key = str(candidate)
                        index.setdefault(key, []).append((rel, lineno))
    return index


def run():
    index = build_ref_index()
    orphans = []
    sizes = []
    for rel in walk_md_files():
        full = ROOT / rel
        sz = full.stat().st_size
        sizes.append((sz, rel))
        if is_archive(rel):
            continue
        basename = os.path.basename(rel)
        if basename in ENTRY_FILES:
            continue
        abs_key = str(full.resolve())
        if abs_key not in index:
            orphans.append({"path": rel, "size": sz})
    sizes.sort(reverse=True)
    return {
        "orphans": orphans,
        "size_top10": [{"path": p, "size": s} for s, p in sizes[:10]],
        "total_files": len(sizes),
        "total_bytes": sum(s for s, _ in sizes),
    }


def main():
    result = run()
    if "--json" in sys.argv:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"gg 项目: {result['total_files']} 个 .md / "
              f"{result['total_bytes']} bytes ({result['total_bytes']/1024:.1f} KiB)")
        print()
        print("Top 10 体积:")
        for e in result["size_top10"]:
            print(f"  {e['size']:>7} B  {e['path']}")
        print()
        print(f"孤儿文件: {len(result['orphans'])}")
        for o in result["orphans"]:
            print(f"  {o['size']:>7} B  {o['path']}")
    sys.exit(len(result["orphans"]))


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))
    main()

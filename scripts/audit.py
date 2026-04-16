#!/usr/bin/env python3
"""Phase 1 聚合入口。一键跑全部 4 个检查，输出总报告。

用法：
  python3 scripts/audit.py            # 人类可读报告
  python3 scripts/audit.py --json     # 机器可读 JSON（给 gg-audit skill 用）

退出码：所有子检查退出码之和（0 = 全绿）。
"""
from __future__ import annotations
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import check_deadlinks
import check_orphans
import check_essence
import check_structure


def run_all():
    return {
        "deadlinks": check_deadlinks.run(),
        "orphans": check_orphans.run(),
        "essence": check_essence.run(),
        "structure": check_structure.run(),
    }


def main():
    report = run_all()
    as_json = "--json" in sys.argv
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
        exit_code = (
            len(report["deadlinks"]["active_broken"])
            + len(report["orphans"]["orphans"])
            + len(report["essence"].get("violations", []))
            + len(report["structure"]["naming_violations"])
            + len(report["structure"]["state_missing_fields"])
            + len(report["structure"]["kernel_missing_sections"])
        )
        sys.exit(exit_code)

    print("=" * 70)
    print("gg 项目健康快照  (scripts/audit.py)")
    print("=" * 70)

    d = report["deadlinks"]
    print(f"\n[死链]  活跃 {len(d['active_broken'])} / 归档 {d['archive_broken']} "
          f"/ 跨项目 {d['cross_project_refs']} / 噪音过滤 {d['noise_refs']}")
    if d["active_broken"]:
        by_file: dict[str, list] = {}
        for b in d["active_broken"]:
            by_file.setdefault(b["src"], []).append(b)
        for src in sorted(by_file):
            print(f"  ● {src}")
            for b in by_file[src]:
                print(f"      L{b['line']}: {b['target']}")

    o = report["orphans"]
    print(f"\n[孤儿]  {len(o['orphans'])} / 总 {o['total_files']} 个活跃 .md "
          f"({o['total_bytes']/1024:.1f} KiB)")
    for item in o["orphans"]:
        print(f"  {item['size']:>7} B  {item['path']}")

    e = report["essence"]
    n_commits = len(e.get("commits", []))
    n_viol = len(e.get("violations", []))
    print(f"\n[essence]  {n_commits} 次 commit / append-only 违反 {n_viol}")
    if n_viol:
        for c in e["violations"]:
            print(f"  !! {c['hash']} {c['date']}  -{c['del']}  {c['subject'][:50]}")

    s = report["structure"]
    print(f"\n[结构]  命名违规 {len(s['naming_violations'])} / "
          f"state 缺字段 {len(s['state_missing_fields'])} / "
          f"KERNEL 缺节 {len(s['kernel_missing_sections'])}")
    for b in s["naming_violations"]:
        print(f"  命名: {b}")
    for b in s["state_missing_fields"]:
        print(f"  state: {b}")
    for b in s["kernel_missing_sections"]:
        print(f"  kernel: {b}")

    exit_code = (
        len(d["active_broken"])
        + len(o["orphans"])
        + n_viol
        + len(s["naming_violations"])
        + len(s["state_missing_fields"])
        + len(s["kernel_missing_sections"])
    )
    print()
    print("=" * 70)
    print(f"总违规: {exit_code}")
    print("=" * 70)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

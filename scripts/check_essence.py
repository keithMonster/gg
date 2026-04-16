#!/usr/bin/env python3
"""essence.md append-only 验证。

规则：memory/essence.md 的 git 历史里，首次 commit 之外任何一次 commit 有删除行即违反。
使用 git log --numstat --follow。

退出码：违反次数（0 = 健康）。
"""
from __future__ import annotations
import sys
import json
import subprocess
from pathlib import Path
from _common import ROOT

ESSENCE_PATH = "memory/essence.md"


def run():
    try:
        proc = subprocess.run(
            ["git", "log", "--follow", "--numstat",
             "--pretty=format:%H|%ai|%s", "--", ESSENCE_PATH],
            capture_output=True, text=True, cwd=ROOT, check=True,
        )
    except subprocess.CalledProcessError as e:
        return {"error": f"git log 失败: {e}", "commits": [], "violations": []}

    commits = []
    cur = None
    for raw in proc.stdout.splitlines():
        line = raw.strip()
        if "|" in line and line.count("|") >= 2:
            parts = line.split("|", 2)
            # heuristic: 第一段是 40 位 hash
            if len(parts[0]) == 40 and all(c in "0123456789abcdef" for c in parts[0]):
                if cur is not None:
                    commits.append(cur)
                cur = {
                    "hash": parts[0][:8],
                    "date": parts[1][:10],
                    "subject": parts[2],
                    "add": 0,
                    "del": 0,
                }
                continue
        if cur is not None and line:
            nums = line.split()
            if len(nums) >= 2 and nums[0].isdigit() and nums[1].isdigit():
                cur["add"] = int(nums[0])
                cur["del"] = int(nums[1])
    if cur is not None:
        commits.append(cur)

    # 首次 commit 是 commits[-1]（git log 时间倒序）
    violations = []
    if len(commits) >= 2:
        for c in commits[:-1]:
            if c["del"] > 0:
                violations.append(c)
    return {"commits": commits, "violations": violations}


def main():
    result = run()
    if "--json" in sys.argv:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if "error" in result:
            print(result["error"])
            sys.exit(2)
        commits = result["commits"]
        print(f"{ESSENCE_PATH} 历史: {len(commits)} 次 commit")
        for c in commits:
            mark = "!!" if c["del"] > 0 else "  "
            print(f"  {mark} {c['hash']} {c['date']}  +{c['add']}/-{c['del']}  {c['subject'][:60]}")
        if result["violations"]:
            print(f"\n⚠️ append-only 违反: {len(result['violations'])} 次")
        elif len(commits) < 2:
            print("\n(历史太短，append-only 尚未被真正考验)")
        else:
            print("\n✅ append-only 未违反")
    sys.exit(len(result["violations"]))


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))
    main()

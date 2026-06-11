#!/usr/bin/env python3
"""essence.md append-only 验证。

规则：memory/essence.md 的历史条目 append-only；格式约定区可演化。
检测只统计既有 essence 条目区里的删除行，避免把格式说明更新误报为历史篡改。

退出码：违反次数（0 = 健康）。
"""
from __future__ import annotations
import sys
import json
import re
import subprocess
from pathlib import Path
from _common import ROOT

ESSENCE_PATH = "memory/essence.md"
ENTRY_RE = re.compile(r"^## \d{4}-\d{2}-\d{2} /")
HUNK_RE = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=check,
    )


def first_entry_line_at(rev: str) -> int | None:
    proc = git("show", f"{rev}:{ESSENCE_PATH}", check=False)
    if proc.returncode != 0:
        return None
    for idx, line in enumerate(proc.stdout.splitlines(), 1):
        if ENTRY_RE.match(line):
            return idx
    return None


def entry_deletions_in_commit(commit_hash: str) -> int:
    first_entry = first_entry_line_at(f"{commit_hash}^")
    if first_entry is None:
        return 0

    proc = git("diff", "--unified=0", f"{commit_hash}^", commit_hash, "--", ESSENCE_PATH)
    deleted = 0
    old_line: int | None = None

    for line in proc.stdout.splitlines():
        hunk = HUNK_RE.match(line)
        if hunk:
            old_line = int(hunk.group(1))
            continue
        if old_line is None:
            continue
        if line.startswith("---") or line.startswith("+++"):
            continue
        if line.startswith("-"):
            if old_line >= first_entry:
                deleted += 1
            old_line += 1
        elif line.startswith("+"):
            continue
        else:
            old_line += 1
    return deleted


def run():
    try:
        proc = git(
            "log", "--follow", "--numstat",
            "--pretty=format:%H|%ai|%s", "--", ESSENCE_PATH,
        )
    except subprocess.CalledProcessError as e:
        return {"error": f"git log 失败: {e}", "commits": [], "violations": []}

    commits = []
    cur = None
    for raw in proc.stdout.splitlines():
        line = raw.strip()
        if "|" in line and line.count("|") >= 2:
            parts = line.split("|", 2)
            if len(parts[0]) == 40 and all(c in "0123456789abcdef" for c in parts[0]):
                if cur is not None:
                    commits.append(cur)
                cur = {
                    "hash": parts[0][:8],
                    "full_hash": parts[0],
                    "date": parts[1][:10],
                    "subject": parts[2],
                    "add": 0,
                    "del": 0,
                    "entry_del": 0,
                }
                continue
        if cur is not None and line:
            nums = line.split()
            if len(nums) >= 2 and nums[0].isdigit() and nums[1].isdigit():
                cur["add"] = int(nums[0])
                cur["del"] = int(nums[1])
    if cur is not None:
        commits.append(cur)

    violations = []
    if len(commits) >= 2:
        for c in commits[:-1]:
            if c["del"] > 0:
                c["entry_del"] = entry_deletions_in_commit(c["full_hash"])
            if c["entry_del"] > 0:
                violations.append(c)

    for c in commits:
        c.pop("full_hash", None)
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
            mark = "!!" if c.get("entry_del", 0) > 0 else "  "
            print(
                f"  {mark} {c['hash']} {c['date']}  "
                f"+{c['add']}/-{c['del']}  entry-del={c.get('entry_del', 0)}  "
                f"{c['subject'][:60]}"
            )
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

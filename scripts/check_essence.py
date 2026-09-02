#!/usr/bin/env python3
"""essence 卷 append-only 验证。

规则（KERNEL §3）：essence 历史条目 append-only；格式约定区可演化。
射程（2026-09-02 体检扩）：
  - 当前卷 memory/essence.md ——历史条目区不许删行（格式约定区更新不算）；
    分卷那一跳（R100 纯改名进 memory/essence/）豁免。
  - 归档卷 memory/essence/*.md ——创建 commit 之后**任何**增删都算违反：
    归档卷是冻结件，连 append 也不该有（新滴只进当前卷）。

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

CURRENT_PATH = "memory/essence.md"
ARCHIVE_GLOB = "memory/essence/*.md"
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


def archive_paths() -> list[str]:
    proc = git("ls-files", "--", ARCHIVE_GLOB, check=False)
    if proc.returncode != 0:
        return []
    return [p for p in proc.stdout.splitlines() if p.strip()]


def first_entry_line_at(rev: str, path: str) -> int | None:
    proc = git("show", f"{rev}:{path}", check=False)
    if proc.returncode != 0:
        return None
    for idx, line in enumerate(proc.stdout.splitlines(), 1):
        if ENTRY_RE.match(line):
            return idx
    return None


def entry_deletions_in_commit(commit_hash: str, path: str) -> int:
    # 分卷豁免：当前卷 100% 纯改名归档进 memory/essence/（KERNEL §3"重命名不违背
    # append-only"）不计条目删除；内容有任何改动（非 R100）不豁免（2026-08-01 分卷随动）
    ns = git("diff", "--name-status", "-M100%", f"{commit_hash}^", commit_hash, check=False).stdout
    for line in ns.splitlines():
        parts = line.split("\t")
        if (
            parts[0] == "R100"
            and len(parts) >= 3
            and parts[1] == path
            and parts[2].startswith("memory/essence/")
        ):
            return 0

    first_entry = first_entry_line_at(f"{commit_hash}^", path)
    if first_entry is None:
        return 0

    proc = git("diff", "--unified=0", f"{commit_hash}^", commit_hash, "--", path)
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


def commits_for(path: str, follow: bool) -> list[dict]:
    args = ["log", "--numstat", "--pretty=format:%H|%ai|%s"]
    if follow:
        args.insert(1, "--follow")
    proc = git(*args, "--", path)
    commits: list[dict] = []
    cur = None
    for raw in proc.stdout.splitlines():
        line = raw.strip()
        if "|" in line and line.count("|") >= 2:
            parts = line.split("|", 2)
            if len(parts[0]) == 40 and all(c in "0123456789abcdef" for c in parts[0]):
                if cur is not None:
                    commits.append(cur)
                cur = {
                    "path": path,
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
    return commits


def check_current(path: str) -> tuple[list[dict], list[dict]]:
    """当前卷：--follow 跨分卷改名追历史；最早一条（创建）豁免；条目区删行 = 违反"""
    commits = commits_for(path, follow=True)
    violations = []
    if len(commits) >= 2:
        for c in commits[:-1]:
            if c["del"] > 0:
                c["entry_del"] = entry_deletions_in_commit(c["full_hash"], path)
            if c["entry_del"] > 0:
                violations.append(c)
    return commits, violations


def check_archive(path: str) -> tuple[list[dict], list[dict]]:
    """归档卷：不 --follow（它的前身历史归当前卷那条线）；创建 commit 之后任何增删 = 违反"""
    commits = commits_for(path, follow=False)
    violations = []
    for c in commits[:-1]:
        if c["add"] > 0 or c["del"] > 0:
            c["entry_del"] = c["del"]
            c["frozen_violation"] = True
            violations.append(c)
    return commits, violations


def run():
    try:
        commits, violations = check_current(CURRENT_PATH)
        archives = {}
        for p in archive_paths():
            ac, av = check_archive(p)
            archives[p] = {"commits": len(ac), "violations": len(av)}
            commits += ac
            violations += av
    except subprocess.CalledProcessError as e:
        return {"error": f"git log 失败: {e}", "commits": [], "violations": []}

    for c in commits:
        c.pop("full_hash", None)
    return {"commits": commits, "violations": violations, "archives": archives}


def main():
    result = run()
    if "--json" in sys.argv:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if "error" in result:
            print(result["error"])
            sys.exit(2)
        commits = result["commits"]
        cur = [c for c in commits if c["path"] == CURRENT_PATH]
        print(f"{CURRENT_PATH} 历史: {len(cur)} 次 commit（当前卷，--follow）")
        for p, info in result.get("archives", {}).items():
            print(f"{p} 历史: {info['commits']} 次 commit（归档卷，冻结）")
        for c in commits:
            mark = "!!" if c.get("entry_del", 0) > 0 or c.get("frozen_violation") else "  "
            tag = " [归档卷增删]" if c.get("frozen_violation") else ""
            print(
                f"  {mark} {c['hash']} {c['date']}  "
                f"+{c['add']}/-{c['del']}  entry-del={c.get('entry_del', 0)}  "
                f"{c['subject'][:60]}{tag}"
            )
        if result["violations"]:
            print(f"\n⚠️ append-only 违反: {len(result['violations'])} 次")
        elif len(cur) < 2:
            print("\n(历史太短，append-only 尚未被真正考验)")
        else:
            print("\n✅ append-only 未违反（当前卷 + 归档卷）")
    sys.exit(len(result["violations"]))


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))
    main()

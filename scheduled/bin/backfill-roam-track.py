#!/usr/bin/env python3
"""一次性回填：给历史 exploration session 补 track frontmatter 字段。

区间 [2026-05-14, 2026-06-04] 经 gg 设计模式逐条语义核验，全部为 meta
（关于 gg 自己「能不能信自己」的自指探索）。幂等：已有 track 行则跳过。
跑完即可删；保留为回填工具备查。
"""
import os
import re
import glob

EXPLORE_DIR = "/Users/xuke/githubProject/gg/memory/explorations"
LO, HI = "2026-05-14", "2026-06-04"
TRACK = "meta"


def main():
    changed = []
    for p in sorted(glob.glob(os.path.join(EXPLORE_DIR, "*.md"))):
        base = os.path.basename(p)
        m = re.match(r"(\d{4}-\d{2}-\d{2})", base)
        if not m or not (LO <= m.group(1) <= HI):
            continue
        with open(p, encoding="utf-8") as f:
            text = f.read()
        if re.search(r"^track:\s*\S+", text, re.M):
            continue  # 已有，幂等跳过
        lines = text.split("\n")
        if lines[0].strip() == "---":
            # 有 frontmatter：闭合 --- 前插 track 行
            close = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
            if close is None:
                continue
            lines.insert(close, f"track: {TRACK}")
        else:
            # 无 frontmatter（漫游格式自由的产物）：顶部补最小 block，不动正文
            block = ["---", f"date: {m.group(1)}", f"track: {TRACK}", "---", ""]
            lines = block + lines
        with open(p, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        changed.append(base)
    print(f"回填 {len(changed)} 个 session → track: {TRACK}")
    for c in changed:
        print(f"  {c}")


if __name__ == "__main__":
    main()

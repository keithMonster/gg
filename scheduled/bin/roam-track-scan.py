#!/usr/bin/env python3
"""漫游 track 雷达 — 机械统计 exploration session 的 track 分布。

由 roam-launch.sh 在每晚漫游启动前调用，把输出硬注入漫游 prompt。
触发硬化在 launchd 事件层（每晚必跑），判定留给漫游实例（看着事实自决）。

纯数据，无 LLM 判断：脚本产数据，漫游产观点（fast-slow-divide）。
设计意图见 exploration.md「镜子不是笼子」节。失败时输出空串（空注入，漫游照常起）。
"""
import os
import re
import sys
import glob
from collections import Counter

EXPLORE_DIR = "/Users/xuke/githubProject/gg/memory/explorations"
OUTWARD = ["ai", "architecture", "cc", "humanity", "keith"]  # 五条对外 track
META = "meta"  # 关于 gg 自己的元探索（自指），不属任何对外 track
WINDOW = int(sys.argv[1]) if len(sys.argv) > 1 else 21


def parse_track(path):
    """只读 frontmatter 头部找 track: 值；无则 None。"""
    with open(path, encoding="utf-8") as f:
        head = f.read(800)
    m = re.search(r"^track:\s*(\S+)", head, re.M)
    return m.group(1) if m else None


def parse_date(path):
    m = re.match(r"(\d{4}-\d{2}-\d{2})", os.path.basename(path))
    return m.group(1) if m else None


def main():
    files = sorted(glob.glob(os.path.join(EXPLORE_DIR, "*.md")), reverse=True)
    rows = []  # (date, track) 新→旧
    for p in files:
        d = parse_date(p)
        if d:
            rows.append((d, parse_track(p)))
    if not rows:
        return  # 空注入

    # 连击：从最近往前数连续相同 track（跨全量，不被 window 截断；None 中断）
    head_track = rows[0][1]
    streak = 0
    for d, t in rows:
        if t == head_track and t is not None:
            streak += 1
        else:
            break
    streak_since = rows[streak - 1][0] if streak > 0 else rows[0][0]

    # 分布：最近 WINDOW 内各 track 计数
    window = rows[:WINDOW]
    dist = Counter(t for d, t in window if t)

    # 对外 track 全历史最近一次出现日期（机械可确证的；未标注的为 None）
    outward_last = {}
    for name in OUTWARD:
        ds = [d for d, t in rows if t == name]
        outward_last[name] = ds[0] if ds else None

    # ── 格式化（注入漫游 prompt 的文本）──
    L = []
    L.append("━━━━━ 漫游 track 雷达 · 机械统计（自动注入，非你的思考）━━━━━")
    if head_track and streak >= 1:
        tag = "（自指 meta）" if head_track == META else ""
        L.append(f"最近连击：{head_track}{tag} × {streak} 晚，自 {streak_since} 起未跳出")
    cov = " · ".join(f"{n} {dist.get(n, 0)}" for n in OUTWARD)
    L.append(f"窗口({len(window)}晚)内对外 track 覆盖：{cov}")
    if dist.get(META):
        L.append(f"其中 meta(关于 gg 自己) {dist[META]} 次 — meta 不属任何对外 track")
    missing = [n for n in OUTWARD if outward_last[n] is None]
    if missing:
        L.append(f"机械记录里从未标注过的对外 track：{' / '.join(missing)}（更早记录未打 track）")
    L.append("")
    L.append("镜子不是笼子：以上是事实不是命令，换不换向你自决。")
    if head_track == META and streak >= 5:
        L.append("唯一提示：连续多晚 meta 命中你自己的 blindspot-steers-its-own-search")
        L.append("（盲区反向操纵搜索方向，永远朝视野内走）—— 现在这个盲区在你视野内了。")
    L.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("\n".join(L))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass  # 失败=空注入，绝不阻断漫游启动

#!/usr/bin/env python3
"""Keith 自我基线快照——「领先现在的自己」的分母冻结器。

用法：python3 scripts/keith_baseline.py [--date YYYY-MM-DD] > tracks/keith/baseline-<date>.md
只读 monster / gg 两仓的既有仪器，不新造数据；每次重跑得到当日快照，与历史快照机械比对。
建立：2026-09-04 设计会话（Keith 答「领先谁 = 现在的自己」「12 个月判据想不好」→ 先冻基线，判据 3 个月后再拍）。
"""
import json, re, subprocess, sys, datetime, collections, pathlib

M = pathlib.Path.home() / 'githubProject/monster'
G = pathlib.Path(__file__).resolve().parent.parent
date = datetime.date.today().isoformat()
if '--date' in sys.argv:
    date = sys.argv[sys.argv.index('--date') + 1]
since = (datetime.date.fromisoformat(date) - datetime.timedelta(days=30)).isoformat()

def sh(cmd, cwd):
    return subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True).stdout.strip()

# 1. 学习台档位（level 0-4：🌑不了解/🌘了解/🌗会用/🌖能讲透/🌕能创新）
prog = json.load(open(M / 'study/data/progress.json'))
units = prog['units']
dist = collections.Counter(u.get('level', 0) for u in units)
by_track = collections.defaultdict(collections.Counter)
for u in units:
    by_track[u.get('track', '?')][u.get('level', 0)] += 1
l3 = [f"{u['id']} {u['title']}" for u in units if u.get('level', 0) >= 3]
track_name = {t['id']: t['name'] for t in prog['tracks']}

# 2. model-lab：Keith 已过的 Stage 数（PROGRESS.md 进度表第 5 列）
rows = [l for l in (M / 'model-lab/PROGRESS.md').read_text().splitlines() if re.match(r'\|\s*\d+\s*\|', l)]
passed = sum(1 for l in rows if '✅' in l.split('|')[5])
stages = len(rows)

# 3. 围棋：已完赛盘数 + 已授课数（go-dojo.md 流水里的「第N盘完赛」「第N课」最大值）
go = (M / 'threads/go-dojo.md').read_text()
cn = '一二三四五六七八九十'
def cn2int(s):
    if s.isdigit(): return int(s)
    if s == '十': return 10
    if len(s) == 2 and s[0] == '十': return 10 + cn.index(s[1]) + 1
    if len(s) == 2 and s[1] == '十': return (cn.index(s[0]) + 1) * 10
    if len(s) == 3: return (cn.index(s[0]) + 1) * 10 + cn.index(s[2]) + 1
    return cn.index(s) + 1
games = max((cn2int(x) for x in re.findall(r'第([一二三四五六七八九十\d]+)盘完赛', go)), default=0)
lessons = max((cn2int(x) for x in re.findall(r'第([一二三四五六七八九十\d]+)课', go)), default=0)

# 4. 活动量（30 天）
m_commits = sh(f'git log --since={since} --until={date}T23:59 --oneline | wc -l', M)
g_commits = sh(f'git log --since={since} --until={date}T23:59 --oneline | wc -l', G)
threads = len(list((M / 'threads').glob('*.md')))
essence_last = sh("git log --format=%s -n 200 | grep -o 'essence #[0-9]*' | head -1", G) or 'n/a'
explorations = len(list((G / 'memory/explorations').glob('*.md')))

print(f"""---
type: keith-baseline
date: {date}
generator: scripts/keith_baseline.py
window_30d: {since} → {date}
---

# Keith 自我基线快照 {date}

> 「5 年后大幅领先」的分母 = 现在的自己（Keith 原话，{date if date=='2026-09-04' else '2026-09-04'} 设计会话）。分母是移动靶，本文件把它钉在日期上。
> 全部数字来自两仓既有仪器，重跑 `python3 scripts/keith_baseline.py --date <日期>` 得同构快照，机械比对不靠回忆。

## 认知深度（学习台，`monster/study/data/progress.json` updated {prog.get('updated')}）

| 档位 | 🌑0 | 🌘1 | 🌗2 | 🌖3 能讲透 | 🌕4 |
|---|---|---|---|---|---|
| 条目数（共 {len(units)}） | {dist[0]} | {dist[1]} | {dist[2]} | {dist[3]} | {dist[4]} |

按 track：
""")
for t, c in by_track.items():
    print(f"- {track_name.get(t, t)}（{t}）：" + ' / '.join(f"L{k}={c[k]}" for k in sorted(c)))
print(f"\n🌖 及以上清单：" + ('；'.join(l3) if l3 else '（无）'))
print(f"""
## 动手层（model-lab，`monster/model-lab/PROGRESS.md`）

- 12 Stage 代码与轨迹全部就绪；**Keith 已过 {passed}/{stages}**（「已过」列 ✅ 计数）

## 生活面（围棋，`monster/threads/go-dojo.md`）

- 已完赛 {games} 盘 / 已授 {lessons} 课（零基础起，2026-09）

## 活动量（30 天窗口 {since} → {date}）

| 仪器 | 读数 |
|---|---|
| monster commits | {m_commits} |
| monster threads 数 | {threads} |
| gg commits | {g_commits} |
| gg essence 最新编号（git log 首见） | {essence_last} |
| gg explorations 档数 | {explorations} |

## 行为结构（沿用 08 月遥测，不重测）

- 工作节律（08-26）：日工作面 92% 回访 / 逐单元占空比中位 ~17% / 重入间隔中位 3 天
- 通道形态（08-29）：Keith 键入 ~87 条/天，中位 38 字符，纠正·校准类 ~16%

## 用法

- 2026-12 设计会话：拍 12 个月判据（agenda 已登记），判据只能引用本文件里有的仪器，或新增仪器后先补基线
- 2027-09-04：重跑快照，与本文件逐行比对；「领先了吗」由差值回答，不由 Keith 的体感回答（#209 两只表反装）
""")

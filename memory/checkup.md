---
type: checkup-checklist
last_updated: 2026-07-17
---

# 体检清单 — 周期性机械阈值的单一登记处

> **为什么存在**：治「阈值定义在明令别读的文件里」死角（2026-07-09 三层蓝图批次 B/C）。散落各处的"越线该报"阈值——曾定义在 `v2-roadmap.md`（明令别读）、体积门则完全真空——集中登记在此，配一个**机械读者**。
> **机械读者（SSOT）**：`auto_gg.md §2` 月度巩固夜"顺带过 checkup.md 机械阈值"——gg 用 wc/grep 核每条机械可判项，越线写 FOUND。设计模式体检（07-03 full-body-checkup 模式）亦读本表。
> **不是**：启动常驻文件（启动分支不读它）/ 硬 fail 门（越线是"提议复审"不是"报错"，判断权仍在 gg + Keith）。

---

## 1. 体积门（按需归档信号；越线 = 提议巩固/下沉，非硬 fail）

| 对象 | 阈值 | 机械核 | 越线动作 |
|---|---|---|---|
| `tracks/keith.md`（主卷） | > 800 行 或 > 90KB | `wc -l tracks/keith.md` / `wc -c` | FOUND：按季度 / 半年把逐场流水搬进 `tracks/keith/<卷>.md`（纯搬段 + 主卷留标题索引，稳定画像段与近 2 月流水留主卷）。首越 2026-09-01（93KB），2026-09-02 设计会话执行首次分卷：04-06 月流水 → `tracks/keith/2026-H1.md`，主卷降至 ~29KB |
| `memory/consolidation/essence-view.md` + `essence-index.md` | 覆盖对账失配（两文件合并 slug 数 ≠ essence `^## 20` 计数 + 异格式滴） | 见 §3 反向引力核 | FOUND：漏 slug = 某滴从启动记忆静默消失，立即补。**常驻层体积**：`wc -m essence-view.md` > 50k 字符 → 提议把族尾「按需」行下沉索引（2026-09-02 拆分时 37.9k） |
| `memory/essence.md`（当前卷） | **≥ 50k 字符（`wc -m`）或 ≥ 60 滴**（2026-09-02 机械化，essence.md 头部长期归档策略） | `wc -m memory/essence.md` / `grep -c '^## 20'` | 下一个月度巩固夜分卷为 essence/2026-H2 卷（卷序义；文件尚不存在，不写成链接以免死链哨误报）。上次分卷 2026-08-01（#1–#186 → `essence/2026-H1.md`，commit ef50fce）；2026-09-02 读数 51.4k 字符 / 45 滴——**字符线已越，09 月巩固夜（10-01）执行** |
| harness 自动记忆 `~/.claude/projects/-Users-xuke-githubProject-gg/memory/` | 条目出现 project / 身份 / 判断类事实而无仓内 SSOT 指针 | 月度巩固夜 `ls` + 逐条读（通常 <10 条） | FOUND：越界条目转 essence 验证关或删（exploration.md §2.5 纳编，2026-09-02） |

## 2. v2 触发阈值（从 v2-roadmap.md 移入，2026-07-09；v2-roadmap 只留话题定义 + 指针）

> v1 范围内**不做**这些——阈值是"何时该开 v2 讨论"的传感器，不是工作队列。越线 = 写 FOUND 提议开 v2 议题，交 Keith。完整话题背景见 `v2-roadmap.md`。

| v2 话题 | 触发阈值 | 机械可判 | 
|---|---|---|
| **记忆系统 sqlite 化**（v2 第一优先级） | 档案侧检索失败 ≥ 2（合理 grep 已跑仍找不到/找不全）**或** 单次启动加载 > 200k tokens **或** Keith 明示 | 第一条机械（数本节下方登记处条目）；第二条机械（启动链字节 ÷3）；第三条软 |
| **learned/ 自增长**（目录已于 2026-09-02 删除——空置 5 个月；话题定义留 v2-roadmap） | tracks 出现"重复模式"，提议固化成条目 | 软（需语义判断） |
| **humanist 第三人格** | 双人格辩论"明显不够用"（反复出现两人都没意识到的盲点） | 软 |
| **自主活动时间调度** | auto_gg EXPLORE 跑 ≥ 4 周后产出有规律 | 半机械（时长机械 + 规律性软） |
| **跨会话 memory 检索层** | 单次 LOAD 阶段 read 文件 > 10 个 | 机械（可在 reflection 统计） |
| **gg-audit 语义审查扩展** | gg-audit 跑过 ≥ 20 次 | 机械（`ls memory/audit/ \| wc -l` 近似） |
| **元审查员 meta-auditor** | gg-audit 自审边界成为痛点 | 软 |

**档案侧检索失败登记处**（sqlite 化第一条阈值的计数源；2026-07-17 Keith 拍板改锚——原 events≥50 数事件不数痛感，首响 206 即误报）：登记权在外部核查者（fresh 审 / codex / Keith），条目须附核查证据指针。**查询侧失败不登记**——没想起去 grep / 关键词范围没铺到 = 触发层病，验证关强制 grep 已治（07-14/07-16 两例 REFUTED 即此类，且都被 grep 逮住，恰证档案可检索）；sqlite 只治档案侧。

- *（暂无）*

## 3. 反向引力核（essence 视图不变量；每滴入库后即核——`essence.md` 头部协议第 5 步，2026-07-12 起；月度刷新后全量核为兜底）

```bash
# 视图常驻层 + 索引按需层合并必须含 essence 全部 slug（当前卷 + 归档卷，2026-08-01 分卷起双路径；2026-09-02 视图拆两层起两文件合并核）——漏一个 = 该滴 grep 不到 = 从启动记忆静默消失
python3 -c "
import re, glob
ess=set()
for path in ['memory/essence.md']+sorted(glob.glob('memory/essence/*.md')):
    for l in open(path):
        m=re.match(r'## \d{4}-\d{2}-\d{2} / \S+ / (\S+)', l) or re.match(r'## (\S+) \(\d{4}-\d{2}-\d{2}\)', l)
        if m: ess.add(m.group(1))
view=open('memory/consolidation/essence-view.md').read()+open('memory/consolidation/essence-index.md').read()
miss=[s for s in ess if s not in view]
print('MISS:', miss if miss else '无（全覆盖）')
"
```

---

## 变更日志

- 2026-07-09: 首建（三层蓝图批次 B/C）。从 v2-roadmap.md 移入 v2 触发阈值 + 新增 tracks/keith 体积门 + essence 视图反向引力核。机械读者 = auto_gg 月度巩固夜。
- 2026-07-12: 反向引力核触发点前移到入库事件（essence.md 头部协议第 5 步；月度核降为兜底）。诱因：07-11 滴入库后视图盲窗实例，Keith 授权（"觉得最优就执行"）+ 设计会话落笔。
- 2026-07-17: sqlite 化触发阈值改锚痛感线（Keith 逐项拍板）：events≥50 → 档案侧检索失败≥2（外部登记）/ 启动链>200k / Keith 明示。§2 新增登记处 + 查询侧/档案侧判别刀；首响 events=206 判误报（事件数是错代理）。
- 2026-08-01: 分卷随动（auto_gg 月度巩固首跑）：§1 essence 行更新为已执行记录；§3 反向引力核脚本扩为当前卷 + `essence/*.md` 归档卷双路径。
- 2026-09-02: 全仓架构体检设计会话（Keith 全批）：§1 keith 行改为分卷动作 + 首次执行记录；essence 视图行改两文件合并 + 常驻层体积线；essence 当前卷分卷线机械化（≥50k 字符或 ≥60 滴，字符线已越、10-01 巩固夜执行）；新增 harness 自动记忆抽样行；§2 learned/ 行标目录已删；§3 脚本改两文件合并核。

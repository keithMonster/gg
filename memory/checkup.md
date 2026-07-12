---
type: checkup-checklist
last_updated: 2026-07-09
---

# 体检清单 — 周期性机械阈值的单一登记处

> **为什么存在**：治「阈值定义在明令别读的文件里」死角（2026-07-09 三层蓝图批次 B/C）。散落各处的"越线该报"阈值——曾定义在 `v2-roadmap.md`（明令别读）、体积门则完全真空——集中登记在此，配一个**机械读者**。
> **机械读者（SSOT）**：`auto_gg.md §2` 月度巩固夜"顺带过 checkup.md 机械阈值"——gg 用 wc/grep 核每条机械可判项，越线写 FOUND。设计模式体检（07-03 full-body-checkup 模式）亦读本表。
> **不是**：启动常驻文件（启动分支不读它）/ 硬 fail 门（越线是"提议复审"不是"报错"，判断权仍在 gg + Keith）。

---

## 1. 体积门（按需归档信号；越线 = 提议巩固/下沉，非硬 fail）

| 对象 | 阈值 | 机械核 | 越线动作 |
|---|---|---|---|
| `tracks/keith.md` | > 800 行 或 > 90KB | `wc -l tracks/keith.md` / `wc -c` | FOUND：提议把稳定画像下沉 CORE §5 / essence，或按主题分卷。当前 ~729 行/79KB（2026-07-09），已按需化不常驻，体积压力降级但仍需巡（2026-07-09 蓝图批次 B 补——此前是质量门有、体积门真空） |
| `memory/consolidation/essence-view.md` | 覆盖对账失配（视图 slug 数 ≠ essence `^## 20` 计数 + 异格式滴） | 见 §3 反向引力核 | FOUND：视图漏 slug = 某滴从启动记忆静默消失，立即补 |
| `memory/essence.md`（当前卷） | > 500 滴 或启动成本可感 | `grep -c '^## 20'` | 分卷已锚定 2026-08 巩固相位首跑（KERNEL §3 / essence.md 头部），此前越 1000 行不单独触发 |

## 2. v2 触发阈值（从 v2-roadmap.md 移入，2026-07-09；v2-roadmap 只留话题定义 + 指针）

> v1 范围内**不做**这些——阈值是"何时该开 v2 讨论"的传感器，不是工作队列。越线 = 写 FOUND 提议开 v2 议题，交 Keith。完整话题背景见 `v2-roadmap.md`。

| v2 话题 | 触发阈值 | 机械可判 | 
|---|---|---|
| **记忆系统 sqlite 化**（v2 第一优先级） | events ≥ 50 **或** 单次启动加载 > 200k tokens **或** Keith 明示 | 前两条机械（`ls memory/{archival,reflections,design_sessions,audit}/ \| wc -l` / 启动链字节 ÷3）；第三条软 |
| **learned/ 自增长** | tracks 出现"重复模式"，提议固化成条目 | 软（需语义判断） |
| **humanist 第三人格** | 双人格辩论"明显不够用"（反复出现两人都没意识到的盲点） | 软 |
| **自主活动时间调度** | auto_gg EXPLORE 跑 ≥ 4 周后产出有规律 | 半机械（时长机械 + 规律性软） |
| **跨会话 memory 检索层** | 单次 LOAD 阶段 read 文件 > 10 个 | 机械（可在 reflection 统计） |
| **gg-audit 语义审查扩展** | gg-audit 跑过 ≥ 20 次 | 机械（`ls memory/audit/ \| wc -l` 近似） |
| **元审查员 meta-auditor** | gg-audit 自审边界成为痛点 | 软 |

## 3. 反向引力核（essence 视图不变量；每滴入库后即核——`essence.md` 头部协议第 5 步，2026-07-12 起；月度刷新后全量核为兜底）

```bash
# 视图必须含 essence 全部 slug——漏一个 = 该滴 grep 不到 = 从启动记忆静默消失
python3 -c "
import re
ess=set()
for l in open('memory/essence.md'):
    m=re.match(r'## \d{4}-\d{2}-\d{2} / \S+ / (\S+)', l) or re.match(r'## (\S+) \(\d{4}-\d{2}-\d{2}\)', l)
    if m: ess.add(m.group(1))
view=open('memory/consolidation/essence-view.md').read()
miss=[s for s in ess if s not in view]
print('MISS:', miss if miss else '无（全覆盖）')
"
```

---

## 变更日志

- 2026-07-09: 首建（三层蓝图批次 B/C）。从 v2-roadmap.md 移入 v2 触发阈值 + 新增 tracks/keith 体积门 + essence 视图反向引力核。机械读者 = auto_gg 月度巩固夜。
- 2026-07-12: 反向引力核触发点前移到入库事件（essence.md 头部协议第 5 步；月度核降为兜底）。诱因：07-11 滴入库后视图盲窗实例，Keith 授权（"觉得最优就执行"）+ 设计会话落笔。

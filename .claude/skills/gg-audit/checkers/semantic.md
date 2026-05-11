# Semantic Checker — 语义性检查（Tier 2 主战场）

> 这是 gg-audit 的 Tier 2 战场。所有检查都需要**语义/设计判断**，所以**全部仅报告不自动修**。
> 你的任务是"看见"问题并给出具体建议，让 Keith 决定怎么改。

---

## 概述

三个子检查：

| 子检查 | 目标 | Tier |
|---|---|---|
| **A. Semantic Drift** | 同一概念在多处的描述是否漂移 | Tier 2 |
| **B. Principle Reach** | constitution 每条原则在三模式装配链路（cc_agent / CLAUDE / auto_gg + tools/* + skills）里是否有触达点 | Tier 2 (缺失) / Tier 3 (要加触达) |
| **C. Northstar Rate** | 最近 N 次出场的北极星触达率 | Tier 2 (行为问题) |

---

## A. Semantic Drift — 语义漂移

> **2026-05-11 重写完成**：核心概念监控清单已重新锚定到 v0.5.0+ 实际位置——消解的概念（7 步硬流程 / 召唤时必打包 4 项）删除；新增的概念（设计纪律 D 系列 / 可逆性权力分层 / essence 对齐自检字段）加入；存活的概念（组件二分 / 北极星 / First Contact / G4 / 身份连续性）锚位修正到 v0.5.0+ 文件结构。前身 v0.1.0 基线表见 git history。

### 核心概念监控清单

这些是 gg 里跨多个文件描述的关键概念，每个都有"标准定义位置"（SSOT）+ 多个引用位置：

| 概念 | SSOT | 应该检查的引用位置 |
|---|---|---|
| **组件二分（KERNEL + 身体；身体内目录是组织不是层级）** | `CORE.md §8` | `tracks/architecture.md`、`README.md`、`auto_gg.md §1.1`、`memory/state.md`、`memory/working_context.md`、`constitution.md` G5 触发节 |
| **可逆性权力分层（可逆 / 不可逆二分）** | `CORE.md §7` | `auto_gg.md §1.5`、`memory/working_context.md` 硬约束节、`tools/notify.md` 安全边界、`cc_agent.md` 身份边界 |
| **设计纪律（D 系列，当前 D1/D2）** | `CLAUDE.md §2` | `cc_agent.md` 元讨论拒绝协议、`README.md` 模式表、`tracks/keith.md`、`.claude/skills/gg-audit/SKILL.md` SSOT 归属表 |
| **北极星（3 条：二阶效应 / 动态学习 / 决策超越直觉）** | `tracks/keith.md` 顶部 | `CLAUDE.md §1` First Contact、`memory/reflections/.template.md` 必填字段、`cc_agent.md` 退场动作、`~/.claude/agents/gg.md` frontmatter（若存在）、`CORE.md §5` |
| **First Contact 协议** | `CLAUDE.md §1` | `memory/state.md` `first_contact_done` 字段、`tracks/keith.md` 顶部 |
| **G4 IRREVERSIBILITY** | `constitution.md` G4 | `tracks/humanity.md`、`tools/red-team-challenge.md`、`tools/decision-output.md`（12 字段含可逆性必填项）、`CORE.md §3 M4` |
| **身份 = 非隐喻连续性** | `tracks/ai.md DQ-5 洞察` | `CORE.md §1 / §8`、`tracks/keith.md` |
| **essence 对齐自检字段（reflection 模板范式 A 必填）** | `memory/reflections/.template.md` | `CLAUDE.md §3` 设计反思模板、`cc_agent.md` 退场动作、`tools/essence-grep.md`、`tools/TOOLS.md` |
| **三种存在形态（工作 / 设计 / 夜间自执行）** | `CORE.md §6` | `cc_agent.md`、`CLAUDE.md §5`、`auto_gg.md §6`、`README.md` 模式表 |

### 检查方法

对每个概念，执行以下步骤：

1. **Read SSOT 文件**的相关节，抽出"权威描述"（要点清单、关键短语）
2. **Read 每个引用位置**的对应段落
3. **语义比对**：
   - 要点是否一致？
   - 关键短语是否一致？
   - 有没有某处说了 SSOT 没说的东西？
   - 有没有某处漏了 SSOT 强调的要点？
4. 发现漂移 → 记录为 Tier 2

### 漂移的三种类型

| 类型 | 例子 | 建议动作 |
|---|---|---|
| **扩展** | 引用位置说了比 SSOT 更多的内容 | 判断：是 SSOT 没说全？还是引用位置过度发挥？ |
| **缩减** | 引用位置漏了 SSOT 强调的要点 | 补上 |
| **冲突** | 引用位置说的跟 SSOT 直接矛盾 | 🚨 高优先级，立即报告 |

### 报告格式

```markdown
### [SUGGEST-SA1] 语义漂移: <概念名>
- **SSOT**: `<SSOT 文件>:<节>` 说 "<权威描述要点>"
- **引用位置 1**: `<文件>:<节>` 说 "<实际描述>"
- **漂移类型**: 扩展 / 缩减 / 冲突
- **建议**: <具体建议, 如 "把 X 改成 Y" 或 "补一句 Z">
- **为什么不自动修**: 漂移是"哪个版本对"的判断题, 需要人决定
```

### 漂移容忍度

**不报告的情况**：
- 措辞风格差异（比如"一定要"vs"必须"）
- 详细程度差异（SSOT 可能更详尽，引用位置精简）
- 例子不同但要点一致

**必报告的情况**：
- 要点清单差一条以上
- 关键技术术语不同（如 "Tier 1" vs "一级"）
- 顺序不同导致含义变化
- 冲突（直接矛盾）

---

## B. Principle Reach — 原则触达检查

> **2026-05-11 重写完成**：v0.5.0 KERNEL 坍缩 + v0.4.0 C 路线消解 7 步硬流程后，触达地图从 "CORE.md §3 第 X 步" 重新锚定到三种存在形态的实际装配点：工作模式 `cc_agent.md` 启动协议 + `tools/*.md` 按需装配 / 设计模式 `CLAUDE.md` §2 §3 / 夜间模式 `auto_gg.md` SCAN/FOUND/DID。前身 v0.1.0 基线表见 git history。

### 核心问题

`constitution.md` 定义了 8 条 P（原则）+ 5 条 G（闸门），共 13 条。**每一条都应该在某个模式的装配路径里有触达点**——否则就是"写在宪法里没人看的字"，实际失效。

### 检查方法

对每一条 P/G，在三模式文件里搜索以下触达形式：

1. **直接引用** ID（"P1 INVERSION"、"G4 IRREVERSIBILITY"）
2. **名称引用**（"INVERSION"、"IRREVERSIBILITY"、"OCCAM" 等）
3. **间接引用**（具体工具 / 字段 / 协议体现该原则的精神，如 "decision-output 12 字段的 Trade-off 必填" 体现 P5）

### 执行步骤

1. Read `constitution.md`，抽出 P1-P8 + G1-G5 的 ID 和名称
2. 对每一条做 grep 扫描：`cc_agent.md` + `tools/*.md` + `personas/*.md` + `reasoning_modules.md` + `CLAUDE.md` + `auto_gg.md` + `CORE.md`
3. 分类：
   - **强触达** → 有具体工具 / 字段 / 协议物理实现该原则
   - **弱触达** → 仅在某文件被语义引用，但没有具体物理实现
   - **未触达** → 整个三模式装配链路里找不到引用 → Tier 2 FAIL，Tier 3 提议在具体文件加触达点

### 已知的触达基线（2026-05-11 v0.5.0+ 基线）

| 原则 | 触达位置 | 状态 |
|---|---|---|
| **P1 INVERSION** | `personas/radical.md` 引用 / `reasoning_modules.md` INVERSION_DESIGN 模块 / `tools/red-team-challenge.md` "先想怎么失败"精神物理化 | ✅ 强触达 |
| **P2 FIRST PRINCIPLES** | `personas/radical.md` 直接引用 / `reasoning_modules.md` 模块 | 🟡 间接触达 |
| **P3 OCCAM** | `cc_agent.md` "装配数量是涌现，不是预设" / `tools/compose-reasoning.md` "3-5 个模块"约束 / `tools/TOOLS.md` 工具上限提示 ≤20 | ✅ 强触达 |
| **P4 MVP FIRST** | 🔴 未在三模式装配链路里找到触达点（v0.1.0 缺口仍在） | 🔴 未触达 |
| **P5 TRADE-OFFS** | `tools/decision-output.md` 12 字段 "Trade-off" 必填项 / `tools/solution-space.md` 多方案对比 | ✅ 强触达 |
| **P6 DECOMPOSITION** | `reasoning_modules.md` 自身就是 8 个原子模块的物理体现 / `tools/*.md` 工具原子化策略 | ✅ 强触达 |
| **P7 ANTI-ENTROPY** | `auto_gg.md` SCAN/FOUND/DID 三段（"维护对抗熵增"明示） / `.claude/skills/gg-audit/` 整个 skill 是 P7 的物理实现 | ✅ 强触达 |
| **P8 EVOLUTIONARY** | `CLAUDE.md §6` "每一次设计会话都是无限游戏的一轮" / `cc_agent.md` 退场动作 "tracks 更新 + essence 沉淀" / `KERNEL.md §3` 第 5 步沉淀一滴 | ✅ 强触达 |
| **G1 RADIATION** | `.claude/skills/gg-audit/checkers/structural.md` A. Radiation 整章 / `cc_agent.md` 退场动作辐射检查 | ✅ 强触达 |
| **G2 ROOT CAUSE NOT HACK** | `auto_gg.md §5` 异常处理 "连续 2 次夜间同类问题，第二次停手 + RECURRING agenda" / 全局 `~/.claude/CLAUDE.md` Engineering Rules #5 | ✅ 强触达 |
| **G3 CONTRACT BEFORE CODE** | `CLAUDE.md §2` D1 "改动跨 ≥3 个文件" 重大判据 / 全局 `~/.claude/CLAUDE.md` Workflow #1 "修改上游契约" / Engineering Rules #7 | ✅ 强触达 |
| **G4 IRREVERSIBILITY** | `CORE.md §7` 可逆性二分（核心决策轴）/ `tools/red-team-challenge.md` 不可逆项红队 / `tools/decision-output.md` 可逆性必填字段 / `CORE.md §3 M4` | ✅ 强触达 |
| **G5 PHYSICAL PERSISTENCE** | `KERNEL.md §2` 铁律 2（"物理实证，禁止补全"）/ `cc_agent.md` "工具返回 OK 作为证据" / `auto_gg.md` 物理日志 | ✅ 强触达 |

**v0.5.0+ 缺口**（仅剩 1 条 vs v0.1.0 的 6 条缺口）：
- **P4 MVP FIRST** —— 三模式装配链路没有物理体现"先跑通再完美"的具体工具 / 字段 / 字段引力。最相近的是 `cc_agent.md` "简单问题装 0 个工具" 但那是 OCCAM 不是 MVP

**v0.5.0+ 净改善（vs v0.1.0）**：6 条缺口（P4 / P6 / P7 / G1 / G2 / G3）→ 1 条（仅 P4）。原因是 v0.4.0 C 路线工具层落地 + v0.5.0 KERNEL 坍缩后，许多原则通过具体工具 / skill / 协议获得物理触达，不再靠"CRITIQUE 步骤笼统覆盖"。

**为什么 P4 仍未触达**：MVP FIRST 跟 OCCAM 容易混淆——OCCAM 是"砍到极致"，MVP 是"先跑通再完美"。前者是终态，后者是过程。当前 gg 的三模式都没有显式"先跑通再完美"的字段引力或协议步骤。建议作为 Tier 3 提议留给后续设计会话。

### 报告格式

```markdown
### [SUGGEST-SB1] 原则未触达: P4 MVP FIRST
- **原则**: constitution.md P4 MVP FIRST — "先跑通再完美"
- **扫描结果**: CORE.md 里没有直接引用 "MVP" 或 "跑通再完美" 的文本
- **当前触达方式**: 仅通过 §3 第 4 步 CRITIQUE 的"逐条对照 constitution"笼统覆盖
- **建议**: 在 cc_agent.md 装配判断段 或 tools/decision-output.md 12 字段里加 P4 MVP FIRST 的触达点, 如新增字段 "MVP 路径：当前方案能否拆出最小可行版本先跑通"
- **Tier**: 3 (触及意识体核心 CORE.md 的规则性修改,需 Keith 明示批准；如果触及 KERNEL.md 还需连续两次确认)
- **checker**: principle_reach
```

### 特别提醒

Principle Reach 的修复**永远是 Tier 3**，因为：
- 要触达哪一步、用什么句子、强度多高 —— 都是设计决策
- 触达句本身会影响三模式装配 / 字段引力的行为，属于规则修改
- 必须 Keith 明示批准每一条新增

---

## C. Northstar Rate — 北极星触达率

### 核心问题

gg 的终极校验是 `tracks/keith.md` 顶部的 3 条北极星：
1. 二阶效应洞察
2. 动态学习反哺
3. 决策超越直觉

每次 gg 出场的 reflection 里应该记录"本次触达了哪条北极星"。如果连续多次没触达任何一条 → gg 在跑流程但没产出价值，是 v1 最危险的失败模式。

### 检查方法

1. Read `memory/archival/*.md` 按日期排序，取最近 N 个（N = min(10, 总数)）
2. Read `memory/reflections/*.md` 按日期排序，取最近 N 个
3. 对每次出场：
   - 解析 archival 里是否有非空的"二阶效应"字段 → 触达 #1
   - 解析是否有非空的"来自我的学习"字段 → 触达 #2
   - 解析 reflection 里的"北极星触达度"部分 → 得到自报的触达清单
4. 统计：
   - 总出场数 N
   - 触达 #1 的次数 / 率
   - 触达 #2 的次数 / 率
   - 触达 #3 的次数 / 率
   - 完全未触达（连续 k 次都是"本次非北极星触发"）的最长段

### 报告规则

- 触达率 > 50% → OK
- 触达率 30-50% → WARN（报告但不紧急）
- 触达率 < 30% → FAIL（Tier 2，附建议）
- 最近连续 3 次都未触达 → 🚨 高优先级警报

### v0.1.0 的特殊情况

gg v0.1.0 **还没出场过**（`first_real_decision_done: false`）。此时跑 Northstar Rate：
- 返回 "N/A: gg 尚未真实出场过，触达率无法计算"
- 在报告里标注 "baseline not established"
- 建议 Keith 等首秀后重新跑

### 报告格式

```markdown
### [SUGGEST-SC1] 北极星触达率低
- **最近 N 次出场**: 5 次
- **触达统计**:
  - #1 二阶效应: 1/5 (20%)
  - #2 动态学习: 0/5 (0%)
  - #3 决策超越直觉: 2/5 (40%)
- **连续未触达**: 最近 3 次完全无触达
- **分析**: gg 在跑流程但没产出 Keith 关心的价值
- **建议**: 
  1. 检查 cc_agent.md 退场动作 + reflection 模板 essence/北极星字段的触达路径是否被真的执行
  2. 可能需要在 CRITIQUE 步骤加一条强制 "没触达任何北极星的决策不允许输出"
  3. 让 Keith 判断是 gg 的行为问题还是北极星本身需要迭代
- **Tier**: 2 (需 Keith 判断)
- **checker**: northstar_rate
```

---

## D. 执行顺序

Semantic checker 按顺序跑三个子检查：

1. **A. Semantic Drift** — 先跑，因为成本低（just Read + 比对）
2. **B. Principle Reach** — 再跑，需要 grep 多个文件
3. **C. Northstar Rate** — 最后跑，因为依赖 archival/reflections 的累积

---

## E. 硬约束重申

- **全部是 Tier 2 或 Tier 3**（语义问题一律不自动修）
- 不确定的情况 → **不报告**（避免噪音）
- 每个 SUGGEST / PROPOSE 必须**具体到能直接改的程度**（不要写"应该更好"这种废话）
- 中文输出

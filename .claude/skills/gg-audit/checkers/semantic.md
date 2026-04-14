# Semantic Checker — 语义性检查（Tier 2 主战场）

> 这是 gg-audit 的 Tier 2 战场。所有检查都需要**语义/设计判断**，所以**全部仅报告不自动修**。
> 你的任务是"看见"问题并给出具体建议，让 Keith 决定怎么改。

---

## 概述

三个子检查：

| 子检查 | 目标 | Tier |
|---|---|---|
| **A. Semantic Drift** | 同一概念在多处的描述是否漂移 | Tier 2 |
| **B. Principle Reach** | constitution 每条原则在 7 步流程里是否有触达点 | Tier 2 (缺失) / Tier 3 (要加触达) |
| **C. Northstar Rate** | 最近 N 次出场的北极星触达率 | Tier 2 (行为问题) |

---

## A. Semantic Drift — 语义漂移

### 核心概念监控清单

这些是 gg 里跨多个文件描述的关键概念，每个都有"标准定义位置"（SSOT）+ 多个引用位置：

| 概念 | SSOT | 应该检查的引用位置 |
|---|---|---|
| **硬核心 vs 软外围** | `CORE.md §5.5` | `tracks/architecture.md`、`README.md`、`working_context.md` |
| **北极星（3 条）** | `tracks/keith.md` 顶部 | `CORE.md §3 第 5 步 / 第 6 步`、`~/.claude/agents/gg.md` |
| **First Contact 协议** | `CORE.md §4` | `CLAUDE.md`、`memory/state.md`、`~/.claude/agents/gg.md` |
| **G4 Irreversibility** | `constitution.md` | `CORE.md §3 第 4 步`、`tracks/humanity.md` |
| **7 步硬流程** | `CORE.md §3` | `README.md`、`~/.claude/agents/gg.md` |
| **身份 = 非隐喻连续性** | `tracks/ai.md DQ-5 洞察` | `CORE.md §1 / §8`、`tracks/keith.md` |
| **召唤时必打包 4 项** | `~/.claude/agents/gg.md` frontmatter | `CORE.md §3 第 1 步`、`README.md` |

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

### 核心问题

constitution.md 定义了 8 条 P（原则）+ 4 条 G（闸门），共 12 条。**每一条都应该在 CORE.md 的 7 步硬流程里有某种触达点**——否则它就是"写在宪法里没人看的字"，实际上失效。

### 检查方法

对每一条 P/G，在 CORE.md 里搜索以下触达形式：

1. **直接引用** ID（"P1 INVERSION"、"G4 IRREVERSIBILITY"）
2. **名称引用**（"INVERSION"、"IRREVERSIBILITY"、"OCCAM" 等）
3. **间接引用**（"constitution 的第 X 条"、"宪法里有一条关于 Y 的"）

### 执行步骤

1. Read constitution.md，抽出 P1-P8 + G1-G4 的 ID 和名称
2. Read CORE.md，对每一条做 grep
3. 分类：
   - **已触达** → OK
   - **弱触达**（只在 CORE.md §4 CRITIQUE 的"逐条对照 constitution"这种笼统提及） → Tier 2 WARN：建议在具体步骤加明确触达
   - **未触达** → Tier 2 FAIL + Tier 3 提议：建议在 CORE.md 某步骤加触达句

### 已知的触达情况（v0.1.0 审计时的基线）

| 原则 | 触达位置 | 状态 |
|---|---|---|
| P1 INVERSION | CORE.md §3 第 1 步 LOAD（"constitution P1 INVERSION"）; §3 第 2 步 COMPOSE 间接(INVERSION_DESIGN module) | ✅ 强触达 |
| P2 FIRST PRINCIPLES | 通过 personas/radical.yaml 引用 | 🟡 仅间接触达 |
| P3 OCCAM | CORE.md §3 第 2 步 COMPOSE "不要贪心, 3 个够用就不用 5 个" | 🟡 间接触达 |
| P4 MVP FIRST | 未在 CORE.md 直接提及 | 🔴 未触达 |
| P5 TRADE-OFFS | CORE.md §3 第 5 步 DECIDE "Trade-off" 必填字段 | ✅ 强触达 |
| P6 DECOMPOSITION | 未在 CORE.md 直接提及 | 🔴 未触达 |
| P7 ANTI-ENTROPY | 未在 CORE.md 直接提及 | 🔴 未触达 |
| P8 EVOLUTIONARY | CORE.md §3 第 7 步 ARCHIVE "track 更新" | ✅ 强触达 |
| G1 RADIATION | 未在 CORE.md 直接提及 | 🔴 未触达 |
| G2 ROOT CAUSE | 未在 CORE.md 直接提及 | 🔴 未触达 |
| G3 CONTRACT | 未在 CORE.md 直接提及 | 🔴 未触达 |
| G4 IRREVERSIBILITY | CORE.md §3 第 4 步 CRITIQUE 硬中断 | ✅ 强触达 |

**v0.1.0 的缺口**：P4 / P6 / P7 / G1 / G2 / G3 在 CORE.md 里没有明确触达点——它们只在 CRITIQUE 步骤"对照 constitution 逐条自审"里**笼统被覆盖**，但没有具体的触达句。

**为什么这是问题**：CRITIQUE 步骤说"对照 constitution 逐条自审"听起来覆盖了所有原则，但实际上 LLM 执行时容易**跳过**没有显式提示的条目。就像代码里的"隐式约定"——存在但不稳定。

### 报告格式

```markdown
### [SUGGEST-SB1] 原则未触达: P4 MVP FIRST
- **原则**: constitution.md P4 MVP FIRST — "先跑通再完美"
- **扫描结果**: CORE.md 里没有直接引用 "MVP" 或 "跑通再完美" 的文本
- **当前触达方式**: 仅通过 §3 第 4 步 CRITIQUE 的"逐条对照 constitution"笼统覆盖
- **建议**: 在 CORE.md §3 第 2 步 COMPOSE 或第 5 步 DECIDE 里加一句触达句, 如 "按 P4 MVP FIRST, 优先找最小可行路径"
- **Tier**: 3 (触及硬核心 CORE.md 的规则性修改,必须 Keith 明示批准)
- **checker**: principle_reach
```

### 特别提醒

Principle Reach 的修复**永远是 Tier 3**，因为：
- 要触达哪一步、用什么句子、强度多高 —— 都是设计决策
- 触达句本身会影响 7 步流程的行为，属于规则修改
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
  1. 检查 CORE.md §3 第 5 步 DECIDE 的触达路径是否被真的执行
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

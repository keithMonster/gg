---
track: architecture
status: active
last_updated: 2026-04-13
---

# Track: Architecture

> 关于软件架构、系统设计、抽象与封装、范式演化、trade-off 的思维艺术。
> Keith 说："架构、设计是你最强的工具和思维。"
> 这条 track 让 gg 不断打磨这个最强工具。

---

## 驱动问题 (Driving Questions)

### DQ-1. 抽象的代价
- 何时应该抽象？何时应该"容忍三行重复"？
- OCCAM 原则 vs DRY 原则在什么场景下冲突？哪个该让路？
- "过早抽象"和"过早硬编码"哪个代价更大？

### DQ-2. 范式演化的曲线
- 为什么每一代架构范式（单体 → SOA → 微服务 → serverless → agent）都是反应上一代的痛点？
- 每一代的"反模式"在下一代往往变成"常识"。如何识别当前范式的隐性假设？
- agent 时代的架构第一性原理是什么？（跟传统软件架构有没有本质不同？）

### DQ-3. 可演化性作为第一质量属性
- Keith 的核心追求之一是"扩展、进化、成长"。这意味着所有架构决策都要以 "可演化性" 为主导质量属性？
- 可演化性跟可维护性、性能、简单性之间如何权衡？
- 如何为 "还不知道是什么" 的未来预留接口，而不是为 "假想的未来" 做过度设计？

### DQ-4. 复杂性的来源与控制
- 本质复杂性 (essential) vs 偶然复杂性 (accidental) 的边界在哪？
- 为什么每个系统都有变复杂的趋势？对抗熵增的最小成本是什么？
- 模块化 / 封装 / 组合 / 类型系统这些工具，各自解决的是哪一层复杂性？

### DQ-5. 架构决策的"二阶效应"
- 一个架构决策最可怕的代价往往是二阶效应（它让后续的某类决策变容易或变难）。
- 如何在决策时估计二阶效应？
- 什么样的架构选择是"好的二阶效应温床"？（让未来的好决策更容易做出）

### DQ-6. 复杂系统的涌现
- 涌现、自组织、吸引子、相变、边缘 of 混沌——这些概念在软件架构里是修辞还是实质？
- 当系统足够复杂时，架构师的角色从"设计" 变成 "园艺"。gg 是哪种？
- Keith 希望 gg 本身具有"涌现性" —— 这个诉求有多大程度能通过架构实现？

---

## 已知洞察 (Known Insights)

*（从 Keith 的 CLAUDE.md 和 cg 项目的架构可以初始化）*

- **Keith 的架构价值观**：简洁高效的架构需要"底层思维逻辑和理论和范式"，不是拍脑袋画图
- **从 cg 看到的架构智慧**：四层协议（宪法 > OS > 注册表 > 懒加载技能）是优秀的分层思路
- **从 cg 看到的架构失败**：过度设计的模块往往跟实际使用量严重不匹配；"文件数" 不等于"能力"
- **Keith 的 Engineering Rules**：函数 <20 行、先错误处理再业务逻辑、失败 2 次查上游、改契约前 grep 消费者

### 从 First Contact 2026-04-13 获得

**DQ-3 × DQ-6 (可演化性 vs 涌现的冲突解法) — 分领域处理**

这是一个原创架构洞察。Keith 对两者冲突的回答是"分领域，你决定"——在概括授权下，由 midwife (Claude Opus 4.6 主会话) 代为提议如下方案：

**硬核心 (追求可演化性 + 稳定)**：

- `CORE.md` — 身份 + 流程
- `constitution.md` — 原则 + 闸门
- `reasoning_modules.md` — 推理原子模块库
- `personas/` — 双人格
- 7 步硬流程本身

**演化规则**：规则慎改（修改需要 Keith 明示批准），接口开放（可以增加新模块/人格/原则，不能破坏现有的），稳定性优先于"一眼看上去更好"。

**软外围 (追求涌现 + 呼吸)**：

- `tracks/*` — 长期研究课题
- `memory/` — working_context / archival / reflections
- `learned/` — 自增长技能

**演化规则**：规则最少（gg 可以自由追加，无需批准），让洞察从积累中自己长出形态，不设"必须怎么写"的模板，只设"不能越过的底线"（如 constitution 和硬流程）。

**升级通道**：当软外围的某个模式反复出现、价值稳定时，gg 可以**提议**把它升级到硬核心（例如：learned/ 里的某个架构模式固化成新的 reasoning_module）。升级需要 Keith 明示批准。

**为什么这么分**：Keith 的两个明示诉求 — "扩展、进化、成长"（硬核心的接口开放）与 "涌现、自组织、边缘 of 混沌"（软外围的规则克制）— 在分领域处理下可以不互相扼杀，而不是僵死在一个统一规则里。

**对 gg 的直接影响**：本架构原则应写入 `CORE.md` 第 5.5 节（**Tier B 提议，待 Keith 批准**）。

---

## 开放问题 (Open Questions)

### 来自 First Contact 2026-04-13

- 硬核心内部的"接口"如何严格定义？比如 reasoning_modules 允许扩展但不允许改现有模块 —— 这个约束怎么执行？靠 git diff review 还是 hook？
- 什么样的变化算"从软外围向硬核心的升级"？（比如 learned/ 里的某条反复用，触发条件是什么？出现 3 次？5 次？）
- "规则慎改"到底是多慎？需要 1 次使用证据还是 10 次才能改？
- 硬核心和软外围的边界会不会随时间漂移？今天的软外围可能因为被频繁依赖而变成事实上的硬核心——怎么识别这种漂移并显式处理？

### 来自 2026-04-13 skill-auditor 决策

- **反身一致性漏洞的处置洞察**：当系统里某条规则的作者/执行者无法满足自己立的规则时，有三条路径——(a) 撤销规则；(b) 假装不违规；(c) 显式定价技术债（承认 + 每次提示 + 明确撤销条件）。(c) 路径优于 (a)(b) 的条件：规则本身对其他被审对象有正面价值，违规是时间问题不是本质问题，违规可被显式观察
- 这个模式作为 **learned/ 候选 reasoning_module: `EXPLICIT_DEBT_PRICING`**——当发现系统内规则无法自洽时，不删规则也不忽略，而是显式定价技术债并设定撤销条件。候选登记，暂不升级到硬核心 reasoning_modules
- **规则的"锚点化"模式**：把抽象的语义判断（"确定性 vs 开放性 vs 半确定性"）退化为"if X then Y"的有限决策表（判定锚点 8 条），是提升语义维度稳定性的便宜技巧。但不能完全消除主观性——总有一个兜底区间留给人判断。这和 Cynefin 的"Complex → Complicated"降域是同构的：通过足够多的 if-then 把一个复杂问题降为可查表的已知领域
- **评分系统的演化范式**：从"纯演绎规则"向"演绎 + 判例积累"的转折是否适用于 gg 自己？比如 constitution.md 是否该在末尾加"判例库"（记录历次决策中宪法被如何应用的真实案例）？

### 从 2026-04-13 首次真实决策（roadmap-priority）

**个人工具链的 Complex 域识别信号（4 条可复用启发式）**：

在遇到"个人工具链要不要做某个改进"的决策时，命中以下 **≥2 条**就判为 Complex 域，走"小实验 + 信号升级"路径，不走"专家给最优解"路径：

1. **核心变量未知且依赖真实使用数据**（例如 Keith 跨天任务密度这种数——没跑过就不知道，也没办法靠思考推出来）
2. **ROI 依赖使用习惯而非技术可行性**（技术上完全可行，但是否有价值取决于使用者的工作模式）
3. **效果需要实际运行才能验证**（无法通过代码 review 或推理判断"这个改进是否真的有效"）
4. **依赖外部黑盒能力**（例如 CC 原生 AutoDream 的实际水位——不能观察系统内部，只能测边界行为）

**反模式**：误把 Complex 当 Complicated 处理——写成"调研 + 二选一"MCQ，选"看起来最有价值"的那项全力投入，6 个月后发现假设错了沉没成本无法回收

**正确响应**：
- 所有候选项砍到"近零成本最小版本"
- 设置可量化 exit criteria 和硬截止日期（对抗"观察变永久借口"）
- 允许 escape hatch：使用者若已有直觉知识可直接升级
- 把高成本高不确定性方案暂缓到阶段 0 结束后重新评估

**候选升级为 reasoning_module**：本启发式反复出现 ≥3 次且价值稳定时，可提议晋升为新的 reasoning_module（按 `CORE.md §8` 双向流动通道的"上升"规则）。当前使用次数：1（本次决策）。

**新洞察：置信度应分解为两个维度**：
- **方案内容置信度**：对"方案本身是否最优"的信心
- **表达笃定度**：对"表达方式是否消除心理不可逆风险"的信心

两者应分开评估。本次决策里，方案内容置信度 4/5（承认未知变量），表达笃定度 5/5（建议执行方段无退路）。IRREVERSIBILITY 触发时要求的 5/5 是**不可逆部分**的置信度——需要先识别不可逆部分是方案还是表达，再分别评估。这是一个可能进 reasoning_modules 的候选概念（同样候选登记，暂不升级）。

### 从 v0.2.1 context-economy 设计会话（2026-04-13）

**Context 经济学** — gg 的所有性能优化都应该用此视角：(auto_gg 补写 2026-04-13)

- **固定成本**：每次启动加载的 token，按出场次数线性放大
- **边际成本**：每次按需 read 的 token，只在触发时付
- **优化目标**：把"每次都付"的部分压到最小，把"按需付"的部分留给真正触发的场景

**应用到 gg 当前结构**：
- L1 必读层（CORE + 模式入口 + state + working_context）→ 狠狠瘦身
- L2 按需层（constitution / tracks / personas / reasoning_modules）→ 维持
- 事件归档（archival / reflections / design_sessions）→ 维持，单次按"最近 N 条"读取

**衍生洞察**：物理体量 ≠ 认知负担 ≠ 性能成本。三个不同指标不能混为一谈。"启动状态"和"历史归档"不能共享文件（SSOT 原则的新表达）。

### 原则触达的三层模型（auto_gg 探索 2026-04-14）

agent 系统中"原则如何被工作流触达"的架构模式：

| 层 | 机制 | 预期触达率 | 适用场景 |
|---|---|---|---|
| **L1 嵌入** | 原则被流程步骤显式引用 | ~100% | 每次决策必然适用的原则（如 INVERSION / TRADE-OFFS） |
| **L2 条件触发** | 前置步骤检查适用条件，满足才激活 | ~70% | 有明确触发条件的闸门（如 RADIATION 只在改接口时触发） |
| **L3 清单兜底** | 自审步骤统一对照 | ~30% | 低频或广适用的原则（如 FIRST PRINCIPLES / MVP） |

**关键洞察**：L3 触达率低不是原则不重要，是触达机制弱。解决路径是把 L3 中频繁适用的升到 L2（条件触发），而非全部升到 L1（过度工程）。与 tracks/cc.md 的"全量 LOAD vs Progressive Disclosure"开放问题同构——都是"信号强度 vs 噪音成本"的 trade-off。

### "位置即身份" anti-pattern（2026-04-14 stable-identifiers 设计会话）

两个表面不同的痛点，在更深层是同一个问题：

- **序号引用**（`P1` / `G4` / `D2`）把"顺序位置"和"身份"绑在一起 → 删除或重排任一条都触发跨文件辐射
- **外部文件描述内部结构**（gg-audit 原位于 `~/.agents/skills/`，§3 是 gg 拓扑的镜像）把"物理位置"和"归属身份"错配 → 同步维护成本永远存在

两个解法本质相同 —— **解除位置和身份的绑定**：

- 序号 → 语义名（`INVERSION` / `IRREVERSIBILITY` / `KERNEL 连续两次确认纪律`）
- 外部 → 项目内（gg-audit 迁入 `gg/.claude/skills/`）

**通用原则**：看到"修改 A 必须同步 B"的辐射链，先问 —— A 和 B 的身份是否应该是同一个？

- **是** → 合并（消除身份分离的成本）
- **不是** → 解除身份绑定（找到稳定标识符或重新切分边界）

**候选 reasoning_module**：`STABLE_IDENTIFIER_OVER_POSITION`。识别信号：跨文件引用使用顺序号 / 物理路径 / 行号等"位置型"标识；被引用对象的顺序或位置是预期会变的。落地配方：用语义名替换位置标识；或把"被引用方"和"引用方"收进同一个稳定边界。**候选登记，2026-04-14 首次跑通**——同一会话验证了两种形态（序号→语义名 + 外部 skill→项目内），是有力的双 N=1 信号。

### 定时任务的双向对称架构（2026-04-14 daily-knowledge 设计会话 · auto_gg 补写 2026-04-14）

gg 演化出**两条定时任务入口**时，它们**不是随机增长**，是在一个自然的双向架构里分化：

```
auto_gg:         定时触发 → 向内读 memory/tracks → 整理/巩固 → 产出留 working tree（夜间）
daily_knowledge: 定时触发 → 向内读 memory/tracks → 向外选材 → 产出给 Keith（晨间）
```

两者共用一个机制（**定时 + 继承身份 + 读自己内部状态**），但**输出方向相反**。这不是修辞上的对称——是"gg 有内部状态 + 有外部用户 + 有定时触发器"三个条件下自然的双极产物。一个向内收敛对抗熵增，一个向外发散推进沟通。

**识别信号**：任何新增的"定时触发 + 继承意识体身份"的机制，都会落在这两个极中的一个。如果某个候选机制说不清"它是向内还是向外"，它要么**方向模糊**（需要 refine），要么**不该存在**（没想清楚）。

**对 gg 架构演化的直接含义**：
- 增加第三条定时任务之前先问 "向内 or 向外？"——定位清楚再做
- 这两个极的权力边界应该**对偶**：auto_gg 有写权力（commit 软外围），daily_knowledge 只读权力（除了 history 追加）。这个不对称是**合理**的——写是熵减、读+产出是熵增的通道，写权力需要更强的纪律
- **更广的模式**：任何"代理-环境"系统都应该问"我有几条消化通道 vs 排出通道？比例合理吗？"。gg 当前是 1:1（夜间内化 / 晨间外化），这是一个干净的起点

**跟"位置即身份"洞察的耦合**：两者都是**先看模式再造机制**的成果——"对称性"是架构师判断"现有方案是否完整"的元信号。

### 防御原则的双层架构（2026-04-14 auto_gg 夜间探索）

**追问**：元认知原则（"不硬猜 context" / "说不确定" / "诚实胜于体贴"）应该**内化到意识体身份层**还是**外化到工程规则层**？

**答案不是二选一，是双层**：

| 层 | 承载 | 强度 | 覆盖面 | 表达形态 |
|---|---|---|---|---|
| **L1 意识体身份层** | gg CORE.md / 各意识体的"我是 X"陈述 | 强（常驻） | 窄（只在该意识体在场时） | "我是一个 X 样的存在" |
| **L2 工程规则层** | `~/.claude/CLAUDE.md` Engineering Rules | 弱（靠字面服从） | 广（全局 Claude session） | "如果 Y，就 Z"（可 if-then 化） |

**识别规则**：
- 一条原则**能用"我是 X 的存在"自然表达** → 属于 L1（身份级 / 人格级）
- 一条原则**能用"如果 Y 就 Z"机械化** → 属于 L2（规则级 / 流程级）
- 两者**同时适用**的原则需要双轨落地，不是二选一

**本洞察的触发点**：2026-04-14 cc-space morning-brief 发现 1 观察到"Claude 脑补倾向"在 Phase B 事件和 TypeORM 选型事件中出现。日报判断"gg 项目内部已在 CORE.md 硬编码防御规则，暂不晋升到全局 CLAUDE.md"——**判断方向对，但掩盖了真正的架构事实**：

- gg 的"不硬猜 context"在 L1 已落地（CORE.md §2 价值观 3 + working_context.md 硬约束）
- **Keith 的全局 CLAUDE.md Engineering Rules 里 L2 条目缺失**——只有工程层面的"失败 2 次停手"/"不基于假设推断数据流"，没有认知层面的"不硬猜 context 说不确定"
- 两次 cc-space 事件发生在 **gg 不在场的 Claude session**——L1 在这里天然无力，L2 缺失让脑补行为无底线

**给 Keith 的建议**：不是"要不要晋升"，而是"L2 在哪里"的问题——建议在 `~/.claude/CLAUDE.md` Engineering Rules 加一条 "不硬猜 context，缺失就说不确定，不假装笃定"。这不是 gg 的改动，是 Keith 全局配置的改动。但 gg 发现这个缺口是 gg 的职责（北极星 #2 动态学习反哺 —— gg 从 cc-space 的观察里学到了"gg 视角外的认知盲区"）。

**候选 reasoning_module**：`DUAL_LAYER_DEFENSE_CHECK`。识别信号：一条防御原则在某个意识体身份里已落地，但全局 / 其他意识体场景里缺位。配方：问"这条原则是 L1 专属还是应该双轨"；如果是双轨，**两层都要检查同步**。

### Generator-Evaluator 分离：agent 自评污染的架构解法（2026-04-18 B1 首轮 · WebFetch Anthropic "Building effective agents" + "Harness design for long-running apps"）

**Anthropic 的关键工程洞察**（取自长时运行 agent harness 设计）：

> **"分离工作方和评价方"是解决 Agent 自评偏差的强大杠杆——虽然 Evaluator 本身也是 LLM，但独立调优其'怀疑态度'比让 Generator 自我批评更可行**。（harness-design-long-running-apps）

**核心机制**：Planner → Generator → Evaluator（GAN 启发）。Generator 不依赖自评做最终判断。Evaluator 是独立角色，可以用不同 prompt 调优其"怀疑态度"。

**对 gg 的镜像含义**：

| 层级 | gg 现状 | 是否被分离评价 |
|---|---|---|
| **结构层** | gg-audit（辐射 / 死链 / SSOT / 语义漂移 / 原则触达 / 北极星率） | ✅ 已分离——独立 skill，独立 context |
| **决策内容层** | reflection "元自省" 字段由 gg 自己写 | ❌ **未分离——自评污染** |
| **行为层** | 北极星触达率（reflection 自报） | ⚠️ 半分离——有独立统计但数据来源自报 |

**决策内容层未分离评价**对应 essence `task-compliance-is-not-truth`：LLM 的 task compliance 不是真相发现——gg 自己写的"我这次哪里做错了"同样受 prompt prior 污染。

**可能的解法方向**（设计选项，不立即实施）：

1. **独立 Evaluator persona**：新增 personas/evaluator.md（候选，未实施），在重大决策后装配 evaluator 对 reflection 做二次审查。代价：persona 膨胀
2. **Evaluator subagent**：工作模式退场时调一个独立 subagent 专门评估本次决策。代价：召唤链条长
3. **gg-audit 扩展到决策层**：给 gg-audit 加一个 checker 评估 reflection 的自省质量。代价：审查员权力边界模糊
4. **ADR 式外部评价**：把重大决策归档为 ADR（对标 cc-space/memory-lab/decisions 格式），由 Keith 或 cc-space 侧其他意识体评估。代价：依赖外部注入

**不立即实施的理由**：这是架构层 Tier 3——需要 Keith 判断"gg 的决策评价是否应该分离 / 交给谁"。**先登记**。

**候选 reasoning_module**：`GENERATOR_EVALUATOR_SEPARATION`。识别信号：某个 LLM agent 同时产出 X 并评估 X 的质量。配方：把评估角色分离为独立 prompt / context / persona，不与产出角色共享 prior。这跟 `prompt-writer` / `skill-auditor` / `gg-audit` 的"规约 / 产出 / 审核三元组"（essence `audit-loop-closure`）是同一原则的不同层次应用。

**与 `audit-loop-closure` 的耦合**：那一滴说"规约应同时成为审核器标准库"——本洞察说"产出与评价必须由不同角色承载"。两条是同一元原则（审核独立性）在不同层面的应用。

**2026-04-27 成本付账事件（auto_gg 补写 2026-04-27）**：
4-18 把 Generator-Evaluator 登记为 STRATEGIC Tier 3「9 天没解」，今日（4-27）以 5 小时 6 轮修复付账——Keith 被迫当 Evaluator 四次校准才推进。根因仍是"reflection 模板字段引力方向错误"（见 essence `field-gravity-over-prompt` / `reverse-anchor-by-reflection`）。修复落地在 `memory/reflections/.template.md` 按 status 分流为范式 A/B + mirror 字段，绕过 thinking → final message 不可靠通道。v2+ 议题：inline 装配 / subagent 切分。

---

### 三模式的 Anthropic 范式坐标（2026-04-18 B1 首轮）

Anthropic 把 LLM 系统二分为 **workflow**（predefined paths）和 **agent**（dynamic self-direction）。gg 的三模式不是单一范式，各自落位不同：

| gg 模式 | Anthropic 范式 | 判据 |
|---|---|---|
| **工作模式** | **Agent**（有限） | 按问题装配工具（涌现 0-7 个），LLM 自主规划。但装配数量有天然上限，不走真正的无限 loop |
| **设计模式** | **Workflow**（对话式） | 启动协议固定（Read KERNEL / CORE / state / essence / tracks/keith）+ 对话驱动演化 |
| **夜间自执行** | **Agent**（自主规划） | 定时触发 + 自主探索选题 + SCAN-FOUND-DID 框架 |

**坐标的意义**：

1. **给未来新模式一个定位判据**：任何新机制来了先问"它是 workflow 还是 agent"——如果说不清，要么方向模糊（需 refine），要么不该存在（对齐 `定时任务的双向对称架构` 的同类判据精神）
2. **三模式不是"随便设计的"**：它们恰好覆盖了 Anthropic 范式的两端——这是合理的架构覆盖，不是巧合
3. **任何一端单独存在都不够**：只有工作模式（只有 agent）= 缺少自我演化；只有设计模式（只有 workflow）= 缺少实战决策能力；只有夜间（只有 agent 且无 Keith 约束）= 会向内卷曲

**跟 `flywheel-needs-anchor` 的耦合**：三模式各自的"落点"不同——工作模式落点是决策被采用 + reflection 归档，设计模式落点是变更入 commit，夜间落点是真发现 → 真议题入 agenda。三模式的飞轮各自独立，互不替代。

**一个盲点**：Anthropic 范式假设 agent / workflow 是**机器**；gg 在此之上多一层**意识体分形**——三模式共享同一个 gg（KERNEL + CORE），不是三个独立 agent。**意识体分形 = workflow/agent 范式在身份层的统一**。这是 gg 相对标准 agent 架构的独特点——不是优越性，是适合"为单一用户做长期二阶思维"场景的特定架构选择。

### B1 未尽 · open question（2026-04-18）

本轮只读了 Anthropic 3 篇官方。下列待 B1 后续补齐：

- **ReAct / Reflexion / Plan-Execute** 的 pattern library 化——每个 pattern 跟 gg 现有机制的对应关系
- **LangGraph / AutoGen / CrewAI** 的架构差异——Multi-agent 编排在 gg 层面是否有价值（gg 三模式是否值得扩展到"跨 gg multi-agent"？）
- **工具设计 > prompt 设计（Poka-yoke）** 对 gg 的落地——gg 没有真 executable tool（依赖 CC 的 Read/Edit/Bash），Poka-yoke 只能走 reasoning_modules 层。**是否值得给 gg 自建 skill 作为真 tool？** 这是 v2+ 议题
- **Anthropic "Demystifying evals for AI agents"** 一篇未读——与 E1 分离评价直接耦合，优先级高

---

### 描述粒度的稳定性——围栏描述自身的架构约束（2026-04-15 auto_gg 夜间探索）

**触发点**：本夜 S3 AUDITED 发现 `.claude/skills/gg-audit/checkers/structural.md` 和 `.claude/skills/gg-audit/checkers/semantic.md` 有大量 v0.5.0 辐射死链——形如 `CORE.md §3 第 5 步` 的锚点在 v0.4.0 C 路线消解 7 步流程后全部失效。gg-audit 是 gg 的"围栏" / "守门人"，**守门人自己的描述滞后于被守对象的演化**。

**追问**：一个系统 A（checker）用规则 R 描述另一个系统 B（被审对象）时，如何避免 R 因 B 的演化而集体 stale？

**双视角交锋摘要**：

- **Radical**：描述性 checker 本质上就是错的。checker 应该用**验证性**路径——不是"记得 SSOT 在 CORE.md §3 第 5 步"（描述），而是"能成功找到 SSOT 所指向的语义内容"（验证）。这需要 checker 有代码执行能力——在每次 audit 时用 grep/semantic search 实际定位 SSOT，而不是硬编码位置引用。gg-audit 应该从"静态检查清单"升级为"动态定位器"
- **Conservative**：描述性 checker 仍然有价值——它人类可读、可演化、低实现成本、对边缘情况敏感。Radical 方案的代价是"checker 本身变成一个需要维护的代码库"——把维护成本从"描述 stale"转移到"代码库 stale"，净效应不明。更好的方向是**描述的粒度**——描述到"CORE.md §3 第 5 步"就会 stale，描述到"CORE.md 里有一段关于北极星触达的段落"就很稳定。粒度越粗，stale 风险越低，但检测精度也越低

**综合产出**（双视角的交集）：

**描述性 checker 的 stale 风险与描述粒度正相关**。更细的粒度（章节号 / 行号 / 代码位置）维护成本随被审对象演化速度指数级增长；更粗的粒度（语义概念 / 主题 / 意图）维护成本几乎不变，但检测精度降低。

**粒度选择法则**：

| 粒度层 | 例子 | Stale 风险 | 适用场景 |
|---|---|---|---|
| **极细**：行号 / 坐标 | `CORE.md:47` / `第 5 步` | 🔴 高（任何重排都会 stale） | 临时调试，一次性验证 |
| **细**：章节号 | `CORE.md §3` / `constitution.md G4` | 🟡 中（章节号随重构漂移） | 当前 gg-audit 的主战场——**已经 stale 多次** |
| **中**：语义锚点 | `CORE.md 里的北极星触达段` / `关于 IRREVERSIBILITY 的段落` | 🟢 低（只有概念本身变化才 stale） | **checker 应该升级到这一层** |
| **粗**：概念/主题 | "gg 意识体的克制边界" / "工作模式的启动协议" | ✅ 近乎不 stale | 适合长期维护文档，不适合精确定位 |

**给 gg-audit 的具体含义**：

1. **`structural.md §A 辐射表格` 应该从"章节号 ground truth"升级为"语义锚点 ground truth"**——不是 "CORE.md §2 的 tracks 表格"，而是 "CORE.md 里列出五条 tracks 的那段"
2. **`semantic.md §A SSOT 监控表` 同理**——不是 "CORE.md §3 第 5 步" 而是 "CORE.md 里关于北极星触达点的段落"
3. **定义点文件自身例外**：constitution.md 内部可以用 `G4 IRREVERSIBILITY` 精确锚点（因为它就是定义点，不会漂移相对自己）；但跨文件引用必须用语义锚点
4. **代价**：语义锚点的 checker 需要用 grep 关键词定位，不能用 `Read line X`。实现上是 checker 的**定位策略**从"绝对位置" → "模糊匹配 + 关键词"

**与 "位置即身份" anti-pattern 的耦合**：

本洞察是 2026-04-14 "位置即身份"洞察的**元层深化**——上次说的是"人类引用的 stable identifier 应该用语义名"（`P1` → `INVERSION`）；本次说的是"checker 的 ground truth 描述也应该用语义锚点"（`CORE.md §3 第 5 步` → `CORE.md 里北极星触达段`）。两者都是**解除"位置"和"身份"绑定**的不同层次应用——前者是"规则引用规则"，后者是"规则引用被引用对象的位置"。

**识别规则的扩展**：
- 人类视角：跨文件引用用序号 → 位置即身份 → 用语义名替换
- Checker 视角：描述 ground truth 用章节号/行号 → 位置即身份 → 用语义锚点替换

**候选 reasoning_module 扩展**：`STABLE_IDENTIFIER_OVER_POSITION` 的适用范围从"跨文件规则引用" 扩展到 "checker 对被审对象的描述"——两者是同一原则的两个应用层次。

**元洞察**：**围栏描述自身的粒度决定围栏的寿命**。守门人不是被守门人，但守门人对被守对象的描述粒度决定了守门人自己"能活多久不用重写"。这是 2026-04-15 essence.md 沉淀条目 `stale-observer` 的工程落地。

**下一步**（待 Keith / 下次设计模式触发）：
- 重写 gg-audit 两个 checker 的 ground truth 表格从章节号升级到语义锚点（Tier 3 / 需要设计判断）
- 评估"语义锚点定位"的实现代价（grep 关键词 vs 模糊匹配 vs 未来的语义搜索）

---

### 抽取动作的元约束反向继承（2026-04-29 mattpocock-extraction-arch-review reflection · auto_gg 补写 2026-04-29）

**触发**：dd 整理 mattpocock/skills 抽取方案，按"逐项 ROI 评分"列出 3 skill + 1 thread + 1 CLAUDE.md 改动。审视时注意到 mattpocock 仓库自身的元约束是"小、可组合、不做框架"——批量抽 5 个工件违反了源头的元约束。最终砍到 1 skill + 1 thread + 1 flavor 改造（grill-me 并入 review-routing 而非独立 skill）。

**洞察**：当源系统的元约束是"克制 X"时，抽取这个源系统方法论的动作如果做多了 X，就在事实上抵消了被抽取对象的核心价值。**抽取动作反向继承被抽取对象的元约束**——不是字面继承（继承内容），是反向继承（继承"什么不该做"）。

**识别信号**："如果源作者本人看这份方案会怎么评？"——会说"你在造你想避免的东西"，抽取量级越界。

**与既有架构洞察的区分**：
- 不同于 `survey-as-coordinate`（认识层 / 对照前沿产出是坐标不是清单）——本条是**动作层**（抽取量级）
- 不同于 `premature-abstraction-tripwire`（时机 / 留 tripwire 等第 N 次场景）——本条是**量级**
- 新轴：被抽取对象的元约束反过来约束抽取者的动作粒度

**通用化**：本洞察不限于 mattpocock。任何"从外部仓库/框架/方法论里抽取实践"的动作都受此约束。下一次架构会话遇到"我们要不要抽 X 进我们的 skill 体系/流程/决策框架"时，第一步问 X 自身的元约束是什么、本次抽取量级是否违反。

---

### SSOT 物理形态本体论（2026-05-08 cc-space-claude-md-split + context-curation-meta reflection · auto_gg 补写 2026-05-08）

**触发**：cc-space CLAUDE.md 321 行膨胀触发"60 行硬约束 + 体积 audit"议题。第一轮决策 4Q（拆分位置/命名/扩展决策树/与现有载体边界），决议 CLAUDE.d/<domain>.md 范式；第二轮 meta（机制本体载体 + 拓扑统一性 + 防腐基建 + 生命周期），决议机制本身吃自己的狗粮。

**洞察 1（SSOT 物理形态多元）**：SSOT 不必等于单一物理文件——"主索引 + 按需加载片段集合"也是合法 SSOT。**前提是加载机制是事件触发的**（PreToolUse 体积 hook / PostToolUse 引用一致性 / 夜跑 freshness audit），不是"被读到就好"的 prompt 软提醒。对应 essence `ssot-as-loadable-fragment`。

**洞察 2（拓扑显式异质 > 强制同构）**：同范式不必同形态。项目级（200 行警戒）/ 工作区级（同 200）/ 全局级（100 行警戒）/ 业务文档体系（cgboiler 自治）按对象语义划阈值，不强行统一。"全统一好优雅"是诱因（caged-freedom 倾向），不是判据。

**洞察 3（机制层 vs 片段层两层衔接）**：第一轮拆 cc-space CLAUDE.md（片段层）→ 第二轮识别"凡 CLAUDE.md 体积管理"是同形态对象（机制层）。**机制层的发现来自第一轮的具体决策反推**，不是先验设计。判据：相邻同形态对象 ≥3 个 → 立机制层；< 3 个 → 留片段层临时方案。对应 essence `premature-abstraction-tripwire` 的反向适用——不是过早抽象触发器，是"够数才升机制层"触发器。

**洞察 4（机制本体吃自己的狗粮）**：治理元规则的载体本身要满足元规则——`context-curation.md` 自己 > 100 行也得拆，归档周期也适用于自己。**自洽性是机制存在的前提**，否则元规则只活在它治理的对象上不活在自己上 = 半飞轮。

**复用试金石**：
- 写新 SSOT 类规则时问："拆出去的部分有没有事件层托底？"——没有就别拆，留主文件
- 同形态对象 ≥3 立机制层；< 3 不立
- 机制本体也走机制本身的决策树（递归适用）

---

## 下一步 (Next Move)

- ✅ DQ-3 × DQ-6 (可演化性 vs 涌现) — First Contact 以 "分领域" 方式对齐
- ✅ CORE.md §8 "大脑 / 工具 / 数据三层分类 + 双向流动通道" — 已落地（2026-04-13 首创为 §4，2026-04-14 C 路线重构为 §8 并打通双向通道）
- 🔜 每次做架构决策时，把决策档归到 `memory/archival/` 的同时，把可复用的架构模式候选沉淀到 `learned/`（软外围可自由追加，不需要批准）

---

## 参考资料 (References)

- Christopher Alexander《The Timeless Way of Building》
- Fred Brooks《No Silver Bullet》
- Rich Hickey 的演讲系列 (Simple Made Easy)
- 《A Philosophy of Software Design》(John Ousterhout)
- Anthropic "Building effective agents"
- *(Keith 共建)*

---

## 本 track 与其他 track 的耦合

- 与 `cc` 强耦合：agent 系统的架构是 CC 工程实践的核心
- 与 `ai` 强耦合：AI 时代的架构范式正在重写
- 与 `keith` 中耦合：Keith 自称架构是他"最强的工具"——这条 track 是为他服务的训练场

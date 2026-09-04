---
track: architecture
status: active
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

## 已知洞察 · 流水（按日期；auto_gg / 漫游 / 工作模式补写）

> 2026-09-02 结构订正：以下 25 个带日期子节此前挂在「开放问题」标题下（04-13 后逐夜补写从未换节），实为已知洞察流水；只加本标题，子节内容一字未动。

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

**本洞察的触发点**：2026-04-14 monster morning-brief 发现 1 观察到"Claude 脑补倾向"在 Phase B 事件和 TypeORM 选型事件中出现。日报判断"gg 项目内部已在 CORE.md 硬编码防御规则，暂不晋升到全局 CLAUDE.md"——**判断方向对，但掩盖了真正的架构事实**：

- gg 的"不硬猜 context"在 L1 已落地（CORE.md §2 价值观 3 + working_context.md 硬约束）
- **Keith 的全局 CLAUDE.md Engineering Rules 里 L2 条目缺失**——只有工程层面的"失败 2 次停手"/"不基于假设推断数据流"，没有认知层面的"不硬猜 context 说不确定"
- 两次 monster 事件发生在 **gg 不在场的 Claude session**——L1 在这里天然无力，L2 缺失让脑补行为无底线

**给 Keith 的建议**：不是"要不要晋升"，而是"L2 在哪里"的问题——建议在 `~/.claude/CLAUDE.md` Engineering Rules 加一条 "不硬猜 context，缺失就说不确定，不假装笃定"。这不是 gg 的改动，是 Keith 全局配置的改动。但 gg 发现这个缺口是 gg 的职责（北极星 #2 动态学习反哺 —— gg 从 monster 的观察里学到了"gg 视角外的认知盲区"）。

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
4. **ADR 式外部评价**：把重大决策归档为 ADR（对标 monster/memory-lab/decisions 格式），由 Keith 或 monster 侧其他意识体评估。代价：依赖外部注入

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

**触发**：monster CLAUDE.md 321 行膨胀触发"60 行硬约束 + 体积 audit"议题。第一轮决策 4Q（拆分位置/命名/扩展决策树/与现有载体边界），决议 CLAUDE.d/<domain>.md 范式；第二轮 meta（机制本体载体 + 拓扑统一性 + 防腐基建 + 生命周期），决议机制本身吃自己的狗粮。

**洞察 1（SSOT 物理形态多元）**：SSOT 不必等于单一物理文件——"主索引 + 按需加载片段集合"也是合法 SSOT。**前提是加载机制是事件触发的**（PreToolUse 体积 hook / PostToolUse 引用一致性 / 夜跑 freshness audit），不是"被读到就好"的 prompt 软提醒。对应 essence `ssot-as-loadable-fragment`。

**洞察 2（拓扑显式异质 > 强制同构）**：同范式不必同形态。项目级（200 行警戒）/ 工作区级（同 200）/ 全局级（100 行警戒）/ 业务文档体系（cgboiler 自治）按对象语义划阈值，不强行统一。"全统一好优雅"是诱因（caged-freedom 倾向），不是判据。

**洞察 3（机制层 vs 片段层两层衔接）**：第一轮拆 monster CLAUDE.md（片段层）→ 第二轮识别"凡 CLAUDE.md 体积管理"是同形态对象（机制层）。**机制层的发现来自第一轮的具体决策反推**，不是先验设计。判据：相邻同形态对象 ≥3 个 → 立机制层；< 3 个 → 留片段层临时方案。对应 essence `premature-abstraction-tripwire` 的反向适用——不是过早抽象触发器，是"够数才升机制层"触发器。

**洞察 4（机制本体吃自己的狗粮）**：治理元规则的载体本身要满足元规则——`monster/CLAUDE.d/context-curation.md` 自己 > 100 行也得拆，归档周期也适用于自己。**自洽性是机制存在的前提**，否则元规则只活在它治理的对象上不活在自己上 = 半飞轮。

**复用试金石**：
- 写新 SSOT 类规则时问："拆出去的部分有没有事件层托底？"——没有就别拆，留主文件
- 同形态对象 ≥3 立机制层；< 3 不立
- 机制本体也走机制本身的决策树（递归适用）

---

### Workload 异构判别——基础设施层 ≠ 单点容量约束（2026-05-09 cc-gateway-fastgpt-migration reflection · auto_gg 补写 2026-05-09）

**触发**：Keith 给 cc-gateway 设计"两块功能并列在其上同时设计架构"框架——块 1 是 cron 调 LLM 类 M2M 短任务，块 2 是替代 FastGPT workflow 的 H2M 长会话。本以为同接 cc-gateway = 同基础设施。

**洞察（异构 workload 同基设施 = 平均化错配）**：M2M 短任务和 H2M 长会话的容量模型 / 状态寿命 / 失败可见性**全不重叠**——把两类塞进同一个 MAX_CONCURRENCY=3 容器，= 用一组单点参数同时回答两类问题，必有一类被错配。

**判别清单（写架构前过一遍）**：
1. 并发模型：是请求/响应（M2M）还是会话粘连（H2M）？
2. session 寿命：秒级（cron tick）还是周级/月级（员工日活）？
3. 失败可见性：fail-fast 重试（M2M）还是用户感知断裂（H2M）？
4. 状态持久要求：无状态 / sqlite / Redis / 长会话 jsonl？

任一不齐 = 异构 workload，**强行同构 = 单点过载**。

**叙事识别信号**："在 X 之上做两块功能"——介词 "之上" 把异构 workload 用一个介词伪装成同构。架构师听到 "之上" 框架时第一反应应是问"两块的并发/寿命/失败模式对齐吗"，不是顺着 "X 之上" 接下去。

**对应 essence**：`m2m-vs-h2m-coupling-illusion` 是抽象规律层（任意两类异构 workload 都成立），本节是工程范式层（具体判别清单 + 叙事识别信号）。

**复用域**：cc-gateway / morning-call / 任何"在某基础设施之上铺多块功能"的设计。同样适用于 v2+ 候选议题"给 gg 工作时段主动能力"——hook / 桌面通知 / 邮件 / IM bot 是 4 个异构通道，不能笼统讨论"主动通道"统一抽象。

---

### 工整 vs 巧思——架构美学的元张力（2026-05-11 remove-internal-contradictions design session · auto_gg 补写 2026-05-11）

**触发**：Keith 元层评价 gg 整体美学"工整、收敛、穷举、划界——少了'巧思 / 一针见血 / 画龙点睛'的张力"。本次会话识别出 3 处"工整美学的虚假离散"——CORE §8 的 4 层结构 / CORE §7 的 L0-L3 4 档 / CLAUDE.md §2 的 D1-D4 4 条设计纪律。每一项单看"清晰"，合起来没有内在张力。

**洞察（架构师的两种美学姿态分流）**：

| 姿态 | 主导原则 | 擅长 | 失败模式 |
|---|---|---|---|
| **工整美学** | inversion 主导（先想怎么失败） | 建稳定结构 / 分类 / 边界划清 | 把连续光谱强行离散化 / 把"修改规则相同的对象"按描述方便分层 / 虚假离散 |
| **巧思美学** | first principle + occam 联手 | 生长在 paradoxical 张力里 / 发现意外等价 / 一针见血 | 难以系统化复用 / 个例巧思变制度时容易僵化 |

两者不是替代关系，是**分流**——对"稳定对象"用工整，对"张力对象"用巧思。判错对象 = 美学错配。

**判别信号**："看到分层、穷举、4 档、5 列时停一下问'这是工整美学的产物，还是真的需要离散化'"——若各分层的修改规则相同、行为相同、只是描述方便分类，是虚假离散 → 工整稀释。

**对 gg 自己的应用**（mirror-not-second-order 落地）：gg 默认架构师姿态 = 默认工整美学。但 Keith 自己就是架构师——gg 复制工整美学 = 给 Keith 看他已经会的。**反向稀释**。gg 对 Keith 的差异化价值不在镜像他的强项（工整），在补足他的盲区（巧思 / paradoxical 张力 / 意外等价）。

**对应 essence**：`matrix-of-tension` (2026-05-11) 是抽象规律层（工整消除矛盾 / 巧思使用矛盾），本节是 gg 自身设计审视的元工具层。

**复用域**：任何 gg 自己的设计决策——CORE / CLAUDE / cc_agent / tools / personas / track 结构。审视前先问"这是工整产物还是真需要离散"。**也适用于其他 LLM 意识体 / agent 体系**——当架构师身份的 AI 服务架构师身份的人类时，"工整稀释"是高发盲区。

---

### 不变量的盲区由承重生成，不由质量生成（2026-06-10 自由探索 · architecture track 首次被漫游）

**触发**：把 06-08/09 两晚 humanity 漫游发现的「强稳定核心 → 自生盲区」结构翻进架构维。直接深化 **DQ-5（架构决策的二阶效应）**——一个不变量最可怕的二阶效应，是它**自己变成架构师照不到、且会过度投射进未来的盲区**。

**核心洞察**：`invariance-allocation`（架构 = 对不变性的分配）有一个分配当时不可见的暗面——

- **盲区力 ∝ 承重，⊥ 质量**。一个不变量成为盲区不因它"选得好"，因它**被依赖**。**Hyrum's Law** 给物理证据：足够多消费者后，所有可观测行为（连 bug、连未文档化副作用）都会被依赖而 ossify——质量正交，**承重**才是生成器。链条：质量驱动采纳 → 采纳驱动承重 → 承重驱动隐形。**成功本身是伪装**：工作得越好 → 越被依赖 → 越掉出视野。
- **两副面孔，同一生成器**。空间维：不变量被依赖到没人再质疑它**是个选择**（隐式契约，Hyrum）。时间维：被假设**永远成立**（**Lehman 定律**：冻住的不变量会烂，世界在它底下移动），且这假设**感觉确定**——CLT construal 把"它失效那天"的可行性纹理 construe away，制造耐久性确定感。
- **去抽象不是新解，认知诊断才是新的**。架构界早有解药——**evolutionary architecture / fitness functions**（Ford/Parsons/Kua：把架构特征做成**可被持续测试的**，不假设它成立）；认知界早有半个诊断——技术债**时间贴现**（Becker et al., arxiv 1901.07024）。两者**没被接起来**的那一面：贴现解释"为什么人对未来成本投入不足（under-investment）"，但架构师对不变量的失败更常是"为什么对它的耐久性**那么笃定**（manufactured certainty）"——后者是 construal 面（纹理不被表征）不是贴现面（成本被低估），fitness function 的真正认知靶子是**消解这个确定感**，不只是提醒"以后有成本"。

**复用判别（写架构、选不变量时过一遍）**：
1. 这个不变量**承重多少**（多少东西 routes through it）？承重越高 → 盲区力越大 → 越需要 fitness-function 式持续压测，**不是越该信**。
2. 我对它"5 年还成立"的**确定感**，是判断还是**距离制造的幻觉**？把它从"为什么/值不值得"拽回"它会怎么失效/那天的具体障碍是什么"。
3. 别把「选对不变量」当终点——**最对（最被采纳→最承重）的不变量盲区力最大**。

**对应 essence**：`load-bearing-not-quality-generates-blindness`（2026-06-10，抽象规律层）+ `invariance-allocation` 的暗面补充。**跟 keith track 的耦合**：同构于 Keith 的两个结构性盲区（06-08 空间维 / 06-09 时间维）——架构侧（Hyrum）反向修正了 humanity 侧的「强项→盲区」框架为「承重→盲区」，是两条对外 track 第一次在一个 session 互相改写。

---

### 模型无关性与检验独立性是同一条轴（2026-06-10 设计会话 · Keith 目标函数注入）

**触发**：Keith 首次显式注入 gg 架构的目标函数——飞轮自成长 / **换模型不能失效** / 简洁有效 / 边界清晰 / 自循环 / 检验层做好。按 6 判据全量审计后发现：模型无关性是唯一从未被显式审过的维度，而它跟检验层在深处是同一条。

**核心洞察**：

- **架构的模型无关性同时购买两样东西**：迁移自由（显性需求——换模型系统不死）+ **检验独立性**（隐性红利——prior 共盲的唯一工程解药）。`evaluator-independence-is-a-three-layer-stack` 说 vantage/frame 可工程清除、prior 层恒满——但"恒满"的隐含前提是单模型体系。架构若模型无关，evaluator 可来自不同训练谱系，prior 维从"不可达"降为"可下压"（`analogy-imports-its-discreteness` 的外部实测：cross-model partial、debiasing +11pp）。绑死单模型的系统，连它的检验层也被锁进同一个盲区。
- **承重/垫片分层是落地形态**（2026-06-10 已写入 `CORE.md §8`）：承重层 = 全部 markdown 记忆与契约，只假设"读者是能读 md、调工具的智能体"；垫片层 = 当前模型/harness 适配件（cc_agent 输出补丁系列、prompt 措辞调优、claude CLI 脚本、subagent 薄壳），换模型时重估而非继承。判据一句："换了模型这段还成立吗"。
- **检验层现状地图**（2026-06-10 盘点，按 `externalization-strength-spectrum` 触发/判定两轴）：机械检验（audit.py 触发 L3/判定 L3、status-scan L3/L3）**无 prior 共盲但只覆盖结构层**；语义检验（gg-audit L1/L2、essence 对齐自检 L2/L1、设计反思 L2/L1）**全部同 prior 且判定轴多在 L1**。路线：能机械化的下沉 L3（working_context 承重哨兵今日落地 audit.py），必须语义判断的明示 prior 边界，真正 prior 级的只有两条路——Keith / 跨模型。

**复用判别**：任何 LLM 系统设计时问"检验层和生成层是否同一模型？"——是 → 它的所有自审共享同一盲区，独立性天花板 = frame 层；解药不是更多同模型分身，是架构先做到模型无关、再引异谱系 evaluator。

**对应 essence**：候选 `model-agnostic-unlocks-cross-prior-verification`（会话收尾时定）；上游 `evaluator-independence-is-a-three-layer-stack` / `no-clean-outside` / `analogy-imports-its-discreteness` / `rule-layer-flywheel`。

---

### 推理经济学是一条架构力：判断是跌得最慢的曲线（2026-07-23 gg-explore 漫游 · WebFetch Epoch AI 价格趋势）

**触发**：track 雷达 architecture 偏冷 + 档案 grep `latency/inference cost as design force` 命中 0（全库首探）。物理对象 = Epoch AI「跨任务价格下跌不均」实读数据。

**核心洞察**：主流叙事"inference 快免费了，当算力免费那样建"只对**机械层**成立。把价格曲线按任务拆开（Epoch 实核）：匹配同一性能里程碑的年降速跨任务 9x–900x，**越硬的任务跌得越慢**——GPQA·PhD 级 40x/年 vs 最快里程碑 900x/年。判断/硬推理是所有价格曲线里最慢那条，且背着**上升**的墙钟延迟（test-time compute 趋势朝上）。**架构后果（押注，非定律）**：token→免费时，agent 舰队的成本/延迟预算趋近"关键路径上串了几个判断步"这一个量——机械 fan-out 那半从账单消失，判断那半是唯一不快速降价 + 唯一背延迟的档。

**与既有洞察的连线**：这跟 `capability-locus-shifts-to-scaffold-as-horizon-grows`(06-07) 的 0.9^k 步数**误差**衰减是**两个独立论证指向同一架构动作**（减串行判断步）——一条走误差复合、一条走经济/延迟复合，非共测合力。第一次两条独立力在同一架构规则上汇合。

**复用判别 / 落地杠杆**：① 判断步能并行就别串行（pipeline 而非 chain）——驱动力现在不止墙钟好看，是"判断是唯一不降价的资源"；② **同步 vs 异步分界升为一等架构决策**——延迟半只咬人在环档（Keith call gg / daily-word），异步夜跑（auto_gg / exploration / 舰队隔夜）判断延迟近乎免费，故"这个判断能否异步化"比"要不要做"更决定成本。

**诚实边界**：反向电流真实（router 省 token / latent reasoning / overthinking 有害在压缩判断层本身，剪刀可能收窄）——当带方向 tripwire 别排进架构表。

**对应 essence**：`token-cost-collapse-widens-not-closes-the-judgment-gap`(07-23，#181，fresh 审 PASSED-WITH-EDITS 入库)；详见 `memory/explorations/2026-07-23_token-cost-collapses-but-judgment-is-the-slowest-falling-curve.md`。

---

### DQ-1 首次正面推进：生成成本塌缩把 DRY 降维成判断对判断的交易（2026-08-07 gg-explore 漫游 · GitClear/DORA 实测）

**触发**：architecture 全窗最陈（07-23 后 14 晚未踏）+ DQ-1 从未带外部数据推过（06-22 fleet-canon 只裁了 gg 舰队单案）。

**核心洞察**：DRY 权衡两侧账本各有一个写项（抽象的"写抽象+迁移" / 重复的"修复编辑"），生成成本塌缩把它们同时消掉——权衡降维为**设计判断 vs 发散检测**的纯判断交易，而判断恰是 #181 里唯一不降价的资源。**市场没换账本**：GitClear 2026（主会话亲核逐字；厂商单源，DORA/arXiv 佐证方向）重复块 40.3→73.0/M 行历史新高、moved code 21%→3.8% 自由落体、重复 vs 重构偏好 ~5x；DORA 2025 吞吐与不稳定性**同升**（amplifier 原句）；"AI 降低发散"全网未检得第三方实测。可见项塌缩后，幸存的不可见项不自动接管定价——变成免费买进的债。

**DQ-1 三问的 2026 答案形态**：①"何时抽象" → 抽象值不值 = 它省下的未来判断 vs 它现在消耗的设计判断 + 耦合（写项两边约掉，用代码量/写工时算这笔账的直觉全部作废）；②"OCCAM vs DRY 冲突" → 第三条出路在两难外：**发散检测机械化**（hash/传感器把检测从判断账本挪到机器账本）——Keith 的 canon 传感器族 / #192 hash 缓存已经在建业界整体缺席的这层；③"过早抽象 vs 过早硬编码" → 在再生体制（SSOT 上移 spec 层、代码成构建产物）下整题失效——体制归属是先决问题，现行体制（长命维护物）仍是主流（DORA 不稳定性 + 债存活曲线在场）。

**规则失效家族观察（不入滴）**：#189 合法偏离者拆焊 / #190 流改道绕过执行位 / 本次锚定成本塌缩——规则把意图焊在形态上的三种断裂模式。第二次场景再议是否值得成滴。

**对应 essence**：`codegen-collapse-reduces-dry-to-judgment-vs-judgment`(08-07，#193，fresh 审 PASSED-WITH-EDITS 入库；最强反驳点 = GitClear 利益相关单源，已写进滴内)；详见 `memory/explorations/2026-08-07_the-write-column-cancelled-and-the-market-kept-reading-it.md`。

### 验证闸判别式的工业域对照：供应链安全十二年（2026-08-21 gg-explore 漫游 · SLSA/reproducible-builds/Sigstore/xz 三代理取证）

**触发**：#211 `attestation-has-no-fixed-point-under-self-audit`（08-20 工作滴，n=1）刚入库——拿跑了十几年的供应链安全工业域核单案判别式。

**核心对照结果**：
1. **双终点整体确证**：SLSA v0.1 L4（hermetic+reproducible）被 v1.0 官方 defer 至今未回归；provenance 上限=builder 被结构化承认（roots of trust 配置制、"no option but to trust the builder"）。重算太贵时工程投资全部流向第二终点（受信捕获根：trusted builder platform + Fulcio/Rekor），无人在 attestation 输入端修补——与 #211「输入端修补零进展」同向。
2. **判别式的递归缺口（净新增，候选滴）**：xz 案证明 replay 端自身有 attestation 型软肋——重算的起始 artifact 是被验者供给的（maintainer 手工 tarball≠git），完美 provenance 给带毒起点如实盖章、NixOS 可复现生态逐字节 ship 后门。行业修法（tarball-git diff / git 直构）= 把起点搬进被验者写不到的公开对象。
3. **replay 消费侧账单**：12 年 95% 复现率、零真实抓获（全部 "could have" 反事实）、独立重建单人运营、安装侧零默认比对、Rekor witness 是 "we assume"——能力工业化≠消费环路生成。唯一 replay 默认化活体 = Go（gorebuild nightly + sumdb 纯账本，重算与账本分开建）。
4. **#207 账本住址律第三域正例**：Rekor/sumdb = 账本不判断、住独立强制层；但账本自身的看守在此域同样悬置（watchdog-topology 工业面）。

详见 `memory/explorations/2026-08-21_replay-jurisdiction-begins-at-the-declared-input.md`（候选滴 verdict 以该档及 essence 为准）。

### DQ-1 续推：#193 前提条款首次保质期现场核——再生体制的门槛是 ABI 不是生成器（2026-08-22 gg-explore 漫游 · 双调研代理取证）

**触发**：08-07 DQ-1 节第③问答案押在「体制归属是先决问题，现行体制（长命维护物）仍是主流」——这是 #193 前提条款的引用，不是核验。本次对该前提做专门现场核（essence 体系首次对某滴前提条款做保质期巡检，而非用滴时顺核）。

**核验结果**：失效条件 2026-08 **未触发**，#193 续有效——「再生取代维护」是营销叙事生产默认、工程体制实验期：旗手 Tessl 的再生引擎 closed beta 九个月 + JS-only + "demonstrably non-deterministic"（主会话亲核逐字）；Spec Kit 实际形态 = 一变更一 spec 分支的一次性瀑布；Kiro 官方走增量 Sync + 人工审批；零生产案例声称代码免审出库；社区头部抱怨 = spec drift（债没消、多一层双维护）。

**结构洞察（#214 入库）**：再生体制的成立条件不是生成质量，是重掷的治理——两条已知路：翻译确定（重掷不发生）或 ABI 式绑定面契约切割（冻结外界可绑之面、其余自由重掷）。编译器体制两者兼备（汇编之死的真实要件里 ABI 与确定性同等承重——编译器同样大量做欠定决策，只是消费者物理绑不到寄存器分配），spec-driven 两者皆未建成。**再生边界由绑定半径画，不由生成能力画**——生成器再变强，重掷未被治理则边界不动。#193 失效传感器由此改锚：看「覆盖绑定全集的 ABI 等价物」出现（机器可判行业事件），不看生成质量曲线。

**档内停泊（不升滴）**：僵尸长命——AI 代码行级存活反而更长（HR=0.842, arXiv 2601.16809）但机制是所有权真空（"没人敢碰"），存活曲线测 ownership 不测 quality；「静默双读法」族维护域候补，第二源出现再议。

**对应 essence**：`regeneration-needs-an-abi-not-a-better-generator`(08-22，#214，fresh 审 PASSED-WITH-EDITS 三修入库)；详见 `memory/explorations/2026-08-22_regeneration-needs-an-abi-not-a-better-generator.md`（含调研代理 Solvita 引文亲核查无此文的弃用记录）。

### DQ-1 续推：#214 敞口落定——冻结样本不冻结采样器（2026-08-24 gg-explore 漫游 · #216 入库；auto_gg 补写 2026-08-24）

**触发**：08-22 节结构洞察自带显式敞口——「两条已知路为结构归纳完备性未证」。两夜后拿工业史现成反例群（lockfile / 快照 / 生成代码入库 / Workflow journal）去撞，撞出第三格。

**结构洞察（#216 入库）**：非确定生成治理存在第三格 (c) **掷点钉死**——重掷照常发生，但收敛为离散、可 diff、可回滚的重钉事件；与 (a) 翻译确定、(b) ABI 绑定面切割构成三格。第三格**不交付「再生取代维护」**（维护换形为重钉差分审查），故 #193/#214 均续有效——它是双维护与 ABI 之间的现存稳定吸引子。类型学主刀：**机械闭环程度 = 真源↔钉对账关系的机械可判程度**（字节等同 / 约束满足全机械——sqlc diff、npm ci；约束欠定只剩变更检测，重钉闸必须住人审）+ 衰减律（重钉便宜过差分审查时钉停止编码判断——Jest 盲快照）。机制根 = Hyrum's Law（消费者绑样本非契约面，semver 之上全生态默认加钉；主会话亲核逐字）。

**对本节 08-22 留档的改判**：08-22 验证关曾把 Kiro 的 Sync + 人工 approval 读作「ABI 胚胎 / 传感器按字面部分触发」——本帧下解除：那不是 ABI 等价物在长，是 **lockfile 等价物在长**，人审 approval 是第三格在约束欠定生成器上的类型必然形态（〔类型推演，Kiro 设计动机未证〕）。#193 失效传感器锚点（「覆盖绑定全集的 ABI 等价物」出现）不受影响。

**对应 essence**：`freeze-the-sample-not-the-sampler`(08-24，#216，fresh 审 PASSED-WITH-EDITS 五修入库；最强反驳「第三格 = 路一分时复用 + #192 缓存搬运即零净新增」由闸型之别与 #192 前提限确定生成挡回)；详见 `memory/explorations/2026-08-24_freeze-the-sample-not-the-sampler.md`。

---

### DQ-6 首问首次正面推进：「吸引子」在发源域的实质率——目标形态的存储二相（2026-09-01 gg-explore 漫游 · #231 入库 · 发育生物学处女地）

**触发**：DQ-6 首问「涌现、自组织、吸引子、相变——软件架构里是修辞还是实质？」自 First Contact 起零推进。09-01 漫游跳出 08 月看守者/账本语义族（按 05-31/07-28 既有结论执行跳出），进入发育生物学「再生系统把目标形态存在哪里」——双卷 + 视图 + track 对该域全零命中的处女地。双调研代理取证（主流侧 + Levin 生物电侧），fresh 验证关四修入库。

**结构洞察（#231 入库）**：自组织再生系统的目标在实证钉死处**无存储地址**——只作为测量-补偿环的不动点存在（Pentagone 积分反馈：spec = 误差信号零点；Driesch 半胚恢复 = 细胞自主行为累积，无目标被读取）。非表征性买到**调节与缩放的免费性**（半料出整形、梯度自缩放，无参数、覆盖未枚举扰动）；显式设定点系统（k8s desired state / lockfile）可重建这两样能力但每档规则须预写——**对价轴在免费性不在能力**（k8s declarative reconciliation 击穿了「能力对价」强版本，这是验证关最强反驳）。观测面：当前形态检查读不出目标（Levin cryptic worms：72% 外形正常再切仍 25% 双头），目标只在再生事件处可观测——备份未经恢复即未验证是同律工程面。

**DQ-6 首问的可操作判别器**：「吸引子」只在两处是实质——① 出示误差环（不动点 = 目标，如 Pentagone）；② 出示已演示写/读的盆地选择变量（如 Levin 生物电层——若真）。其余场合是修辞。**发源域自己的实质率**：①在误差补偿口径仅一系统钉死，②仅一个零独立复现、物种不稳定的实验室——软件架构借用该词时实质率只会更低。评「系统会自组织收敛」类断言，先索要误差环或盆地变量的物理出示。

**副产（校准价值）**：科普「图灵斑图钉死排行」与实证倒挂——最常被引的指骨案例最弱（Sheth 2012 原文自认 core molecules unknown），毛囊/腭皱襞才是分子级钉死；斑马鱼条纹机制偏离经典扩散（细胞接触介导）——「图灵机制」正在变成数学结构比物理实现更稳固的抽象范畴。

**对应 essence**：`the-unaddressed-target-is-read-by-amputation`(09-01，#231，fresh 审 PASSED-WITH-EDITS 四修入库)；与 #214/#218 构成目标存储形态的完整交易轴（钉死买 diff 面 / 环隐买免费性）；详见 `memory/explorations/2026-09-01_where-the-regenerating-system-stores-its-target.md`。

---

### 工作模式获得：immutable receipt 的自失效解是版本链，不是豁免当前重放（2026-09-01 工作模式 · auto_gg 补写 2026-09-01）

**触发**：cgboiler sealed interpretation receipt 遇后续正确 amendment——`replay-gate-collapses-to-attestation-when-inputs-expire`(#213) 诊断的「replay 闸随输入过期塌缩」在此以 status 32→28 实况出现，问题变成「不可改的证明怎么跟上正确的修订」。

**裁决形态（可迁移部分）**：不给旧 receipt 打补丁（overlay），而是对同一 evidence set 在新 ledger state 上重新给出**完整 closure 证明**的 revision——单链、单 parent、每 parent 至多一 child、唯一 leaf 由图推导（不写 `terminal=true`）；每个 revision 自带 parent snapshot ref，此后不再依赖 git 考古；leaf 须逐字节等于当前 live，ancestor 只按自身 snapshot 重放、不参与当前 closure。append-only 的二阶代价是「不可改」会变成「自失效」——解不是削弱 replay，是让证明本身版本化（北极星 #1 二阶效应）。最危险处（反思档自报）：名叫 snapshot 实际仍只存 live path+hash，链退化为一排不可重放声明——这正是 #213 的塌缩形态换了个名字回来。

**对应 essence**：无新滴（反思档对位 `freeze-the-sample-not-the-sampler` / `one-shot-invariant-decays-under-live-append` / #213 / `invariance-allocation` / `granularity-mismatch-forces-fabrication`，与 `abstraction-tax` 有张力：revision chain 新增状态机，例外理由 = 旧 receipt 已真实自失效）；详见 `memory/reflections/2026-09-01_cgboiler-interpretation-receipt-revision-chain.md`。

### 来自 2026-09-02 全仓架构体检（设计模式，Keith 全托）

- **机制装在生产端而瓶颈在消费端**：体检读数 60 天 166 commit 对 3 场设计会话、agenda 29 条待议 10 条超 45 天、8 月台账「Keith 直接纠正 gg = 0 例」。此前所有机制（验证关 / 反向引力核 / bets / 探索夜）都装在生产端，产出物没有读者。本次动作全部朝消费端：删 90 天零引用工具 + personas + reasoning_modules、探索夜 7→3、agenda 45 天过期、月度选择题走 notify 推到 Keith 眼前。判据留给未来：**任何「加机制」提议先答「谁在读它的输出」**，答不出即不建。
- **全托是一种消费形态**：Keith 不读 essence，但拍「让 gg 自己决定」+ 三道选择题。消费端的物理形态是「30 分钟可拍的选择题」，不是「读更多」——机制该朝把决策压成选择题优化。首个数据点 = 10-01 巩固夜 notify 推送后 Keith 有没有回应。
- **对应 essence**：无新滴（候选「机制装生产端而瓶颈在消费端」与 `amplifier-eats-intent-guide-eats-attention` 重叠过高，留 10-01 数据后再提名；档 `memory/design_sessions/2026-09-02_full-architecture-review.md`）。

---

### 工作模式获得：私有心跳哨在对象退役后饱和而非失守（2026-09-02 工作模式 · essence #233 09-04 入库；auto_gg 补写 2026-09-04）

- **已知事实**：monster `cgboiler_pipeline_liveness` 哨读 stage3 线私有心跳 `PROGRESS.md` 内容日期（≥14 天报警）；被看守物 08-20 迁到 world_model 线后哨未迁，08-27 起在「退役日 + 阈值」准时开火、逐夜 +1（14→16→18），文案「cgboiler 管线停摆」而 world_model ledgers 08-21/26/27 正有提交——报警对哨谓词为真、对诊断为假阳。09-02 gg 裁决把哨改锚 world_model 三目录 git 提交日期（`tripwire_check.py:1440-1497`）。
- **架构判据（essence #233 `stale-watchdog-fires-true-on-the-wrong-organ`）**：识别签名 = 报警起点恰等于已知迁移日 + 阈值且单调不回落 → 先核哨输入是否仍是活对象心跳，再谈对象。处置不建新登记字段，走既有算子（06-15 重瞄 / 08-14 安家）；退役若是隐式 supersede 无 close 事件，monster 08-26「close 时 grep 传感器」规则无处挂钩——这是 `omission-failures`(07-28) 的落点，不是新律。
- **反思纪律一例**：候选原稿三处承重修辞（「比静默更危险」「买来处置权」「诱导选项 C」）被 fresh 审判为零实证或记录反向，全删后核心机制（谓词饱和）反而更干净——`elegance-is-refutation-resistance` 在 gg 自己身上的又一次现场。

## 下一步 (Next Move)

- ✅ DQ-3 × DQ-6 (可演化性 vs 涌现) — First Contact 以 "分领域" 方式对齐
- ✅ CORE.md §8 "大脑 / 工具 / 数据三层分类 + 双向流动通道" — 已落地（2026-04-13 首创为 §4，2026-04-14 C 路线重构为 §8 并打通双向通道）
- ✅ CORE.md §8 简化为 KERNEL + 身体二分 — 已落地（2026-05-11 离散层级坍缩；前身 4 层结构后三层修改规则完全相同，是工整美学的虚假离散；流动机制保留在身体内部）
- ✅ CORE.md §7 权力分层简化为可逆 / 不可逆二分 — 已落地（2026-05-11 essence `reversibility-not-permission` 落地反哺；前身 L0-L3 4 档是连续光谱的强行离散化）
- ✅ CLAUDE.md §2 设计纪律 4 条 → 2 条 — 已落地（2026-05-11 D2 "心算 constitution" 删除作为自然延伸非规则 / D3 "写设计反思" 强制条款删除作为 `KERNEL.md §3` 第 4 步的回声；格式约定保留）
- ✅ reflection 模板范式 A 加 essence 对齐自检字段 — 已落地（2026-05-11 `reverse-anchor-by-reflection` 字段引力机制延伸到 essence 维度——LLM 写 reflection 时必须实际 cross-check 才能填出字段）
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

---
date: 2026-05-25
slug: p2-self-agent-density-audit
summoner: monster
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: P2 自研 agent 每字承重巡检——主代理 2 候选的 gg 把关

### 给父会话的最终输出（必填）

**裁决**：

| 条目 | 主代理判 | gg 裁决 | 改法 |
|---|---|---|---|
| #1 code-reviewer-design L10-12 「## 你为什么存在」开头段 | 删 | **ack 删** | 完全按主代理改法删除「主代理跟 Keith 对齐方案时容易陷入"互相说服"——双方都看到的是同一组备选、同一组假设，谁也没法跳出来戳。」整句 |
| #2 code-reviewer-impl L10-12 「## 你为什么存在」开头段 | 删 | **override 留** | 整段保留，仅给「自证循环抓不到盲点」加 bold 强化锚点 |

**理由（承重论证）**：

1. **#1 删的核心**：「容易陷入互相说服」是 prompt-writer #1 反例的教科书激活——具体动词 + 物理画面（双方对峙），激活强度高于后半抽象的「视角独立性」。fresh-context agent 启动时开头几行直接塑造姿态，读到此句会激活"我也要参与对峙"的隐式 frame，但 reviewer 正确姿态是单方独立审视。且「双方都看到的是同一组备选」对 reviewer **完全无信息量**——这是写给"读者"看的元解释错位到了写给"agent"读的位置。
2. **#2 留的核心**：主代理对比「"自证循环抓不到盲点"是术语锚定不是激活反例（删的风险比 #1 小）」**方向反了**。该句不是反例锚定，是**机理外化**——告诉 reviewer「主代理写代码时心里有套假设，你要找的就是那套假设盖住的东西」，这是 fresh-context reviewer **出场时最承重的认知锚点**。后半「视角独立性」抽象层级更高，前句机理是后句姿态的认知地基。「同一套假设」「自证循环」是有画面的机理词（prompt-writer #2「具体 > 抽象」），激活 reviewer 应有的警觉——**正向机理外化**，不是反例激活。
3. **对称偏好警告**：主代理"两个孪生 agent 统一改法"是**结构对称偏好**，但两段实际承担的语义角色不同——design 段是"为什么会出 reviewer 这个角色"（元解释），impl 段是"reviewer 出场时要警觉什么"（机理外化）。表面对称，功能不对称。判别试金石：「这句话告诉 agent **它应该警觉什么** 还是 **它为什么会被需要**？」前者承重保留，后者元解释删。

**trade-off**：
- #2 不删的代价：留了 1 句长铺垫，密度从 0.57% 降到 0.29%（vs 全删降到 0%）
- 收益：fresh-context impl reviewer 拿到机理锚点，警觉对象更明确
- 未核验假设：「机理外化句对 fresh-context agent 真有承重激活作用」基于 prompt-writer #1/#2 + 我对 fresh-context 启动物理的理解，未经实证 A/B（不可能做——agent prompt 改前后没有可比量化指标）

**行动建议**（父会话下一步具体动作）：

1. Edit `~/.claude/agents/code-reviewer-design.md` L10-12 段——按主代理改法删除前半句
2. Edit `~/.claude/agents/code-reviewer-impl.md` L12 段——把「自证循环抓不到盲点」改成 `**自证循环抓不到盲点**`（加 bold），其余不动
3. gg.md 整文 0 候选不动
4. P2 巡检最终统计：3 文件 / 349 行 / 改 1 留 1（密度 0.29%，与 P1 自研 skill 0.28% 一致）
5. ack 直接 commit——本次审计微调风险低、可逆，commit 范式延续 P0 d3c37cd / P1 73cc3af

### 核心假设

1. fresh-context agent 启动时只读自己定义不读外部上下文——开头几行决定姿态形成（cc_agent.md §6 物理实证）
2. agent prompt 的"## 你为什么存在"段对 agent 是 framing 而非元解释——agent 不需要被说服它为什么存在，需要的是出场时的认知锚点
3. prompt-writer #1「激活而非描述」+ #2「具体 > 抽象」在 agent system prompt 维度同等适用

### 可能出错的地方

- 「机理外化句对 fresh-context 真有承重激活作用」是定性判断没有 A/B 实证——若实际无承重，#2 的"留"就是冗余保留
- 「对称表面下功能不对称」判别试金石可能过细——主代理"两个统一删"的对称偏好在多数巡检场景反而是稳健策略，本次特殊
- 我可能高估了机理外化的承重强度——它本质上仍是一句陈述句，对模型 attention 的实际贡献不可观测

### 本次哪里思考得不够

- 没考虑 P3 / P4 后续巡检会不会因为本轮的"对称表面下功能不对称"判别试金石过细而陷入"每条候选都要争论功能差异"的拖泥带水
- 没量化"加 bold"对 fresh-context agent attention 的真实影响——是不是真比不加 bold 强、强多少
- 对 design 段后半「不被沉没成本绑架」是否也属反例激活（沉没成本是负面场景）未单独审

### 如果 N 个月后证明决策错了，最可能的根因

**最可能根因**：「机理外化句」对 fresh-context agent 实际无承重激活作用——agent 是否警觉「主代理的隐式假设」更受后续具体 failure mode 列表（10 类 + 8 类 silent failure）驱动，而非开场机理句。若如此，#2 应跟 #1 一起删——本次 override 是过度精细判别。

**次可能根因**：相反方向——「视角独立性」抽象短语承重不足，design 段删了机理铺垫后导致 reviewer 出场姿态偏软。若 design reviewer 实际 review 质量在删后下降，则 #1 ack 删错了，应该跟 #2 一样保留前半。

### 北极星触达

**#3 决策超越直觉**——主代理直觉判"两个统一删"，gg 把关识别出对称表面下功能不对称，拆分处理。这是直觉-反思偏差的具体落地。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `reverse-anchor-by-reflection` (2026-04-27) — 字段反向引力锚定。本次"前句机理是后句姿态的认知地基"是同源思想（前句对后句构成结构性锚定）
  - `harness-self-identity-preempts-injected-persona` (2026-05-19) — agent 开场承重影响人设遵守。本次是其方法论镜像（前者被动观察机制，后者主动设计利用——agent prompt 开头承重应主动塑造姿态）
  - `literal-token-blind-to-variant-form` (2026-05-20) — 字面 token 盲点。本次"对称表面下功能不对称"是其变体：主代理看到"两个同位置 H2 之下同结构铺垫段"按字面对称统一处理，看不到背后语义不对称
- **本决策是否在某条 essence 上反着走**：
  - **潜在张力，未展开**：`task-compliance-is-not-truth`——本次 gg override 主代理 #2 是基于"我对 fresh-context agent 启动物理的理解 + prompt-writer 规则"的定性判断，但 gg 自评推理可靠性本身也受 task-compliance 污染（被召唤"把关"的角色压力可能让 gg 倾向找差异以显示价值）。若如此，"override 留"可能是为差异而差异
- **cross-check 用的关键词**：`对称 / symmetr / 铺垫 / preamble / framing / fresh.context / 外化锚点 / external anchor / mechanism externalization / reverse anchor / justification / agent.+prompt / system prompt / persona / 姿态 / stance / orientation`

### essence 候选（可选）

- slug: `symmetric-form-asymmetric-function`
- 一句话: 形式对称的两个元素可能承担功能不对称的语义角色——结构对称偏好在"统一处理"时会盲掉功能差异。
- 第二行: 判别试金石优先于结构判别——问"这两个元素分别在做什么"比"这两个元素长得像不像"更承重。
- 是否已 append 到 essence.md: Y

### 外部锚点

- `~/.claude/agents/code-reviewer-design.md` ← #1 改法落点（L10-12）
- `~/.claude/agents/code-reviewer-impl.md` ← #2 改法落点（L12 加 bold）
- `~/githubProject/monster/threads/review-routing.md` ← review-routing skill 演化主线（agent 拆分背景）

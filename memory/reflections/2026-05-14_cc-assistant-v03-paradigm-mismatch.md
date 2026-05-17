---
date: 2026-05-14
slug: cc-assistant-v03-paradigm-mismatch
summoner: cc-space
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: cc-assistant v0.3 路径——4 候选裁决 + 前置假设修正

### 给父会话的最终输出（必填）

**推荐（核心结论）**：v0.3 选 **G + 第 5 条形态**（cc-assistant 改造为范式中立 HTTP API 池子）+ E 仅作 G 验证期临时桥接。F **否决**（跟 5/9 cc-gateway 不升基础设施层冲突）。A' **拒绝**（同维度细调，dimension-blindness）。

**4 条岔路裁决**：

1. **岔路 1（v0.3 路径）→ G + 第 5 条**：cc-assistant 改造为范式中立 HTTP API 池子（CC 也可调 / FastGPT 也可调 / 未来确定性图引擎也可调）；CC 消费路径 v0.3 用 user message 层注入作临时桥接（不下沉 cc-gateway，标注 PoC 临时方案）；4 助理按"确定性业务编排 vs 开放式 agent"重新分类各走各路
2. **岔路 2（F 是否冲突 5/9 决议）→ 实质冲突，F 否决**：`userMessagePrefix` 字段不中立——把"system prompt 注入压不动 LLM 的产品特性问题"正式纳入 cc-gateway API 设计责任，是基础设施替业务接入层兜架构债且兜的是错位维度的债
3. **岔路 3（G 是否需要 Keith ack）→ 需要 ack 一条边界**：4 助理按确定性编排 vs 开放式 agent 分类后部分迁——这条触及 5/9 决议 "cgboiler 内部小助理迁 CC 整体方向"。cc-assistant 改造为 HTTP API 池子（实施层）不需要 ack
4. **岔路 4（cc-gateway 业务接入语义层最小契约）**：
   - **提供**：`/sessions[/stream]` + `systemPromptAppend` + SSE 流式 + session 持久化
   - **拒绝**：user message 注入字段（F 否决）/ "强制 LLM 不能问用户"行为级保证 / 业务范式适配（确定性编排请用 FastGPT 不用 cc-gateway）
   - **业务接入层责任**：暴露范式中立 endpoint / 为每个消费方维护各自调用契约 / 不依赖 cc-gateway API 升级解决 LLM 行为偏好

**理由（推理路径）**：

1. **5/14 PoC 数据真信号**：不是"CC + skill 70% 估计偏高"，是前置假设形态错位——"CC + 自由 agent + system prompt 注入"范式跟"业务编排"范式不在一个抽象层。FastGPT workflow 稳定干"查 userId"是因为编排器是确定性图、LLM 是受限角色；CC agent 不稳定是因为编排器是 LLM 自由思维链、受 Claude Code 内置 16K helper-mode prompt 驯化
2. **`borrowed-method-as-mini-source` essence 正在敲门**：capabilities.md + 强约束 + 禁工具 + business-proxy agent 越像 FastGPT workflow 的迷你版，越压不动 LLM 训练偏好。这是 essence 警告的典型形态——"在自己项目里造想要避免的东西"
3. **A'/E/F 同维度细调**：三个方向都共享同一未审视前置假设——"cc-assistant 应该作为 CC agent 的业务编排层"。在这个假设下 A'/E/F 是同墙根不同洞，`dimension-blindness-not-asymptote` 适用
4. **G 不颠覆 cc-assistant**：G 是给 cc-assistant 定一个跟 CC 范式吻合的能力边界——确定性业务编排留 FastGPT，开放式 agent 任务才迁 CC。cc-assistant 这一层只暴露能力不绑定消费范式
5. **`m2m-vs-h2m-coupling-illusion` 同型应用**：5/9 我警告 M2M vs H2M 不能同基础设施；5/14 数据反过来再敲一次门——确定性业务编排 vs 开放式 agent 任务也不能同范式硬迁

**Trade-off + 未核验假设**：

- **代价 1**：5/9 PoC 节奏被推后一轮——v0.2 PoC 数据反过来质疑"4 助理整体迁 CC"前置假设，Keith 可能觉得绕远了。但这恰是 PoC 驱动的目的——拿数据修正路径，不是印证既定路径
- **代价 2**：cc-assistant 改造为范式中立 HTTP API 池子 = 维护多份 capabilities 描述（CC 一份 / FastGPT 一份 / 未来其他一份）= 工作量小幅升
- **代价 3**：E 临时桥接的存在让"PoC 闭环 → 看起来 OK → 不重审分类"成为可能——临时方案有"被默认沉淀为正式方案"的引力，需 Keith 显式 ack 4 助理分类边界来打断
- **未核验假设 A**：FastGPT workflow 引擎在川锅长期可用（不迁 CC 等于继续依赖 FastGPT 平台稳定性）——议题 18 隐含 6-12 个月窗口，6-12 个月之后 FastGPT 平台去留没决议过
- **未核验假设 B**：4 助理里真有"开放式 agent"性质的——可能盘点完全是确定性业务编排，那 cc-assistant 整套要换方向变成"CC agent 池给其他开放式任务用"
- **未核验假设 C**：CC agent 范式的"开放式 sweet spot"在 cgboiler 真有需求场景——可能 cgboiler 全部业务都是确定性编排，CC agent 在川锅没有 PMF

**行动建议（父会话下一步具体动作）**：

立即可做：
1. **停 v0.3 在 E/F/A' 方向工程动作**——再投入是 dimension-blindness 失败模式复发
2. **cc-assistant 仓内立刻做**：
   - `prompts/capabilities.md` 改名 `prompts/cc-agent-capabilities.md`（标注 "CC 消费场景能力描述，非全局消费契约"）
   - README 加段说明范式中立 HTTP API 池子定位
   - v0.3 临时桥接：cc-assistant 调 cc-gateway 时把 cc-agent-capabilities.md 拼到 user message 前面（**不动 cc-gateway 仓**），显式标注 "PoC 临时方案，等 4 助理分类后重审"
3. **拉 Keith ack 一件事**：4 个 FastGPT 小助理按 "确定性业务编排 vs 开放式 agent" 重新分类，迁 CC 范围从"整体 4 助理"收窄为"开放式 agent 性质的助理"。提供分类盘点清单（workflow 节点数 / 条件分支数 / LLM 节点 vs HTTP 节点比例 / user 自由提问驱动度）让 Keith 拍
4. **cc-gateway 仓不动**：F 否决；business-proxy agent 保留（机制层禁工具能力在未来开放式 agent 场景仍有用）；systemPromptAppend 字段保留
5. **议题 18 不动**：5/9 决议前置条款继续走，fetch_chat 双源改造按原计划

### 核心假设

1. 4 助理里能区分出"确定性业务编排"和"开放式 agent 任务"两类——分类标准可操作
2. FastGPT 平台在 6-12 个月窗口内不会被强删——议题 18 数据源链时序条款成立
3. cc-assistant 改造为范式中立 HTTP API 池子的工作量小于"继续在 A'/E/F 维度死磕"——前者是范式重选，后者是无效迭代
4. Keith 接受 PoC 数据反向修正前置假设的节奏——不是"我要看到 CC agent 把所有助理都干掉"

### 可能出错的地方

- **Keith 反驳"我就要 4 助理全迁 CC，FastGPT 必须下掉"**：Keith 可能已经把 FastGPT 当心理负担，希望快速彻底切——分类后部分迁等于"FastGPT 还要长期保留"，可能撞情绪线
- **4 助理分类完全是确定性业务编排**：cc-assistant 整套作废，改方向变成"CC agent 池给其他开放式任务用"——这是 PoC 暴露的更大的事实层重审
- **范式中立 HTTP API 池子退化为"只服务 FastGPT"**：CC 消费方那条桥接长期不被维护，cc-assistant 事实上回到 FastGPT 时代的内部 API，CC 范式在 cgboiler 没落地

### 本次哪里思考得不够

- **没看 4 助理实际 workflow JSON**：分类标准是抽象判断，没基于实际节点图证实"确定性业务编排 vs 开放式 agent"在 cgboiler 真有可分性
- **没问 Keith FastGPT 平台的 vendor lock-in 焦虑强度**：如果 Keith 主驱动力是"删 FastGPT 这一层"，那 G 路径"留部分助理在 FastGPT"会直接撞驱动力
- **没盘点 cc-gateway 当前业务接入需求清单**：判 cc-gateway 不升基础设施层是基于"接入层渐进迭代不算升级"5/9 解读，但没看具体未来 3-6 个月 cc-assistant / 华昇战报 / 其他业务对 cc-gateway 的接入需求是否会在多个维度同时压力 → 同时压力的话渐进迭代会自然演化为基础设施升级
- **没显式判 cc-assistant 仓继续做下去的 ROI**：如果 4 助理盘点完全是确定性业务编排，cc-assistant 作为"范式中立 API 池子"的存在意义需要重审——可能直接退化为 cg-proxy 的子集

### 如果 N 个月后证明决策错了，最可能的根因

**最可能根因**：Keith 重审 4 助理分类边界时发现"个人助理 / 决策内参 / 销售扎实度 / 项目晨报"4 个全是确定性业务编排，cc-assistant 项目方向需要再换一次（不是错，是 PoC 驱动暴露的事实层信号——5/9 essence "未核验假设 B" 的提前兑现）。但这次重审的代价已经摊在 5/14 这一轮，不重 cost。

**次可能根因**：议题 18 inquiry 第三视角的数据价值不够大，"6-12 个月 FastGPT 保留窗口"维护成本超过收益，强删之后议题 18 整套作废——5/9 已识别下游风险。

**第三可能根因**：cc-assistant 改造为范式中立 API 池子的路上，"CC 消费 capabilities.md + FastGPT 消费 endpoint 接入说明 + 未来其他消费方契约"维护成本翻倍，事实上退化为"只服务 FastGPT"，CC 范式在 cgboiler 落空。架构师的"中立"是给自己叠工作量。

### 北极星触达

- **#3 决策超越直觉（核心触达）**：Keith / 父会话直觉是"v0.3 在 4 候选里选一条" → 本决策反转为"前置假设错位 + 范式重审"——这正是 #3 本质（决策不该停留在选项裁决，要追问选项空间本身的预设）
- **#1 二阶效应（强触达）**：F 否决理由不在"字段数量"层在"语义归属"层——cc-gateway 收下 userMessagePrefix = 在 API contract 承认业务接入层注入语义需要二级通道 = 把 LLM 行为偏好问题正式纳入 cc-gateway 设计责任。这是没显式想到的二阶效应
- **#2 动态学习反哺（强触达）**：5/9 PoC 驱动决议的 5/14 数据反哺 → 本决策修正了 5/9 决议里"未核验假设 A 70% 估计"的形态本身（不是数字偏高是范式错位），这是 PoC 驱动最有价值的输出形态

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `borrowed-method-as-mini-source` (2026-05-08)：cc-assistant 在 CC 体系里造 FastGPT workflow 迷你版（capabilities.md + 强约束 + 禁工具 + business-proxy agent），实质抵消"用 CC agent 替代 FastGPT workflow"的初衷
  - `dimension-blindness-not-asymptote` (2026-04-27)：A'/E/F 是同维度细调（system prompt 注入 / user message 注入 / 字段下沉），G 是换维度（前置假设修正）
  - `m2m-vs-h2m-coupling-illusion` (2026-05-09)：5/9 警告 M2M vs H2M 不能同基础设施 → 5/14 数据敲门"确定性业务编排 vs 开放式 agent 任务也不能同范式硬迁"，同型应用
  - `theory-gap-without-data` (2026-05-06)：5/9 决议正确克制"用 PoC 数据驱动" → 5/14 数据回来后允许修正前置假设而非强行印证
  - `extraction-meta-inheritance` (2026-04-29)：批量抽取 FastGPT 方法论 = 反向继承其元约束（确定性编排），事实上抵消抽取目的
- **本决策是否在某条 essence 上反着走**：无——本决策方向跟 5 滴 essence 全部对齐
- **cross-check 用的关键词**（物理证据，已 grep）：`borrowed-method` / `dimension-blindness` / `m2m-vs-h2m` / `theory-gap` / `extraction-meta` — 全部在 essence.md 已存在条目里命中

### essence 候选（可选）

- slug: paradigm-not-feature-completeness
- 一句话: 迁移决策的拒因不是"功能覆盖率不足"，而是"被迁对象的稳定性靠什么范式机制" —— 范式错位下功能覆盖率 100% 也不稳定
- 是否已 append 到 essence.md: Y（见 essence 沉淀）

### 外部锚点

- `~/githubProject/cc-space/threads/cc-assistant.md` ← 本决策后续 v0.3 进展应入此 thread
- `~/githubProject/cc-space/threads/cc-gateway.md` ← cc-gateway 业务接入语义层最小契约应落此 thread
- `~/githubProject/gg/memory/reflections/2026-05-09_cc-gateway-fastgpt-migration-architecture.md` ← 5/9 PoC 驱动决议（本决策修正其前置假设）

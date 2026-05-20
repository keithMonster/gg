---
date: 2026-05-19
slug: cc-gateway-harness-paradigm-mismatch-dual-backend
summoner: cc-space
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: cc-gateway 业务后端形态——第五次根因收敛，harness 范式错配，裁双后端

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**一句话**：第五次根因收敛。前四轮共同隐含前提"claude -p 是合适的业务对话后端，只要解决注入方式"被本次 spike（人设前置进 user message 仍自报 Claude）物理证伪——根因是 claude -p 这个为 agentic coding 设计的 harness 自带 16K 抢占式内置身份，结构性压制任何业务人设，与注入位置无关（位置维度已穷尽）。裁决：**(b) 双后端，切分轴是「是否受人设/行为约束」**——personal-assistant 走 cc-gateway 直连 new-api /v1/messages + 自管 tool-use 循环（绕开病灶 harness）；task-runner/华昇/cg-meetos 保留 claude -p 无损（人设无关 + skill 指令在 user message）。(a) 单后端全直连否决（重写 agentic loop 代价极不对称且对确定性流水线零收益）。**阶段 B（MCP over claude -p）否决**（仍经 16K 污染层，MCP 解决工具可见性不解决人设遵守，是错范式的精致迷你版）。阶段 A（P2/permissionMode）不回滚，标注对 personal-assistant no-op。中立定位**不颠覆反而首次真兑现**——重定义为"多后端中立 runtime"，agents.json 加 backend 字段，cc-gateway 仍业务零感知。跨消费方安全从三轮 P0 下调为"随 messages backend 工程一并解决"（task-runner 族经核证不受影响，真受影响仅 personal-assistant 单点，正解=代码层强制本就是工程一部分）。

**决策详情**（推荐/理由/trade-off/行动建议）已作为 final message 完整输出给父会话——含 6 块裁决（后端形态/中立定位/阶段AB存废/安全重定性/v0.2闭环/essence）+ 7 步行动建议。父会话以 final message 为主。本字段为事实副本锚点：

- **后端形态**：(b) 双后端，切分轴=「受人设/行为约束 vs 不受」（非 prompt 里写的"对话 vs agentic"——personal-assistant 既对话又调工具，那个轴错且会复发同形态 bug）。直连 messages 分支代价：cc-gateway 自实现 tool-use 循环（有界一次性，且这是工具空间约束最彻底形态——LLM 物理无逃逸路径，解掉 llm-autonomy reflection 那个未验证 spike 闸门）；session 持久化重做（减负不增负，workspaceId/cwd 锁死复杂度本为迁就 claude CLI jsonl，直连后简化）。
- **中立定位**：不颠覆。"经 claude -p 的中立"是伪中立（harness 自带非中立身份）；正解"多后端中立 runtime"+ agents.json `backend` 字段，比当前更中立。workspaceId 一等公民保留，但与 cwd 物理耦合只对 claude-cli backend 成立，messages backend 退化为逻辑标签——契约分叉点，落 cc-gateway CLAUDE.md。
- **阶段 A**：P2/permissionMode 对 claude-cli backend 保留（task-runner 族需要+确定性 bug 正交），对 personal-assistant no-op，不删不回滚。**阶段 B MCP 否决**（本轮相对三轮 llm-autonomy reflection 的实质反转——spike 抽掉其地基）。
- **安全重定性**：task-runner/华昇/cg-meetos 经核证不依赖 system 沙箱遵守（指令在 user message + CLI permission-mode 进程层），沙箱 appendSystemPrompt 对它们一直是冗余第二层。personal-assistant 是真实安全债但正解=messages backend tool-use 循环代码层强制（network-cannot-cut 正解形态）。优先级 P0→随工程一并做，仍告知 Keith Context Asymmetry，不停服。
- **v0.2 闭环**：确认。v0.2(user msg) 与 v0.4(systemPromptAppend) 同根，机制=16K agentic prompt 结构性压制，注入位置维度第五次也是最后一次穷尽。
- **行动**：① 拉 Keith 范式轴 ack（话术见 final message）② spike messages+tool-use 循环最小 vertical slice ③ runner 加 backend 路由 ④ 阶段A 标注 no-op ⑤ 阶段B 删 ⑥ 落两 thread ⑦ 安全告知不停服。

### 核心假设

1. spike 四铁证（system 送达/new-api 三格式遵守/111KB 回放无视/user message 前置仍自报 Claude）构成确凿定位——采信父会话陈述的 prod 实测证据链，我未独立在 prod 容器复跑（物理实证降级为采信，显式标注；但本轮证据链比三轮强——含原样回放铁证，已排除格式/通道/位置三维度）。
2. 直连 new-api /v1/messages 短 system 完美遵守（spike [[STR-OK]]/[[ARR-OK]]/[[CC-OK]]）——采信父会话证据；这是 (b) 直连分支可行性地基。
3. cc-gateway 容器网络可直达 new-api（claude -p 当前就经此跳，ANTHROPIC_BASE_URL 实证），自管 HTTP 调用工程可行——拓扑高置信。
4. cg-meetos 判断层结构上不依赖 system 沙箱遵守（其架构定义"纯代码算兑现率 AI 绝不碰 + 判断走 cc-gateway 接口"）——采信前序 thread 陈述 + 架构推断，未独立 grep 每个调用点。
5. tool-use 循环工程量"有界一次性"——基于 messages API tool-use 是标准模式的判断，未核 cc-gateway 零依赖 node:http 架构容纳成本（spike 会暴露）。

### 可能出错的地方

- **最可能崩点**：直连 messages 自管 tool-use 循环的工程复杂度被低估——多轮工具调用 + 错误处理 + session 历史管理 + 流式（企微 replyStream 需要）叠起来，"有界一次性"变成持续工程负担，事实上在 cc-gateway 里重造了一个简化版 agentic runtime（borrowed-method-as-mini-source 在我自己裁决上的复发风险）。概率中等——已用"spike 前置闸门"对冲（最小 vertical slice 先验证，不直接铺开），但 spike 只验证可行性不验证长期维护成本。
- **次可能**：Keith 否决范式轴、坚持 claude -p 路线——但四次实证（v0.2/v0.4/三轮 spike/本轮 spike）顶着，否决成本由 Keith 显性承担。
- **第三**：cg-meetos/华昇判断层实际有依赖 system 沙箱遵守的隐藏分支（核心假设 4 错）→ "task-runner 族不受影响"判断要重画，安全优先级下调失当。已显式标注未独立 grep，置信度标注为"架构推断高但非物理核验"。
- **第四**：messages backend 丢失 claude -p 的"自动 model 路由 / 完整工具链"对 personal-assistant 未来若需要文件处理（docx/xlsx，台账已列）时露出缺口——直连后文件处理工具要 cc-gateway 自己实现或保留混合（部分能力回 claude-cli）。本轮按"personal-assistant 当前阶段对话+受控查询为主"裁，文件处理能力迁移是后续 vertical slice，未在本轮展开（边界画粗）。

### 本次哪里思考得不够

1. **没在 prod 容器独立复跑 spike** —— 整个第五次收敛建立在采信父会话四铁证。证据链本身比三轮强（含原样回放 + 排除三维度），逻辑闭环，但物理实证铁律要求标注：范式轴裁决我拍（四次实证累积，轴极硬），证据真实性采信父会话。
2. **没量化直连 tool-use 循环 + 流式的真实工程量** —— 说"有界一次性"但没拆解（tool-use loop / session 历史 / 企微 replyStream 流式适配 / 文件处理工具迁移）各自成本，"代价不对称有利"的不对称程度画得偏乐观。spike 是把这个采信转回物理核验的必经步骤——已设为前置闸门。
3. **没核 cc-gateway 零依赖 node:http 架构与 messages tool-use 循环的契合度** —— MCP/HTTP client 是否引入依赖、流式 SSE 解析在原生 http 下的复杂度，未核（同三轮 llm-autonomy reflection 漏的"cc-assistant 零依赖能否容纳 MCP"同形态盲区，本轮在 cc-gateway 侧复现）。
4. **没读 index.js/queue.js 路由层** —— backend 字段路由的具体落点（runner.js 分发 vs 上游 queue 分发）未核物理结构，按"runner.js 按 agent.backend 分发"推断，实际可能要动多文件。本决策不依赖此细节（范式裁决正交于路由实现），但行动建议第 3 步的工程量估计建在推断上。

### 如果 N 个月后证明决策错了，最可能的根因

**最可能根因**：直连 messages backend 自管 tool-use 循环在落地中持续膨胀——为支撑 personal-assistant 的多轮对话 + 受控工具 + 文件处理 + 企微流式，cc-gateway 事实上长出一个简化版 Claude Code agentic runtime。即范式轴判对（claude -p harness 对受人设约束对话错配），但"绕开 harness 自建"的实现路径低估了 harness 替我们承担的复杂度——本该是"用 Anthropic Agent SDK / 轻量 agent 框架替代 claude -p"而非"cc-gateway 从零手写 loop"。这是 `borrowed-method-as-mini-source` 在我自己裁决上的活体复发：我裁掉了"在错 harness 上加层"，却可能引入"自己造 harness 迷你版"。已用 spike 前置 + 双后端（不是全量迁）部分对冲，但对冲的是可行性不是长期成本。

**次可能根因**：Keith ack 范式轴后，直连分支把 cc-gateway 从"agent runtime"实质演化成"两套不同范式的执行器拼装"，中立定位第四次被撕（5/14 disallowedTools / 5/15 人设解耦 / 三轮 MCP 议 / 本轮直连），最终需要更大架构重定——把 cc-gateway 拆成两个独立服务（agentic-runtime + chat-backend）。

### 北极星触达

- **#3 决策超越直觉（核心触达）**：父会话直觉（含我前三轮）在"怎么让注入被遵守 / 修通道 / 上工具空间约束"框内。本决策第五次穿透——前四次都在"注入这条路怎么走通"，本轮跳出框：注入这条路的地基（claude -p harness）本身对这个用例是错的，正解是绕开整个 harness。这是对我自己三轮裁决共同隐含前提的二阶证伪（三轮都假设 claude -p 是合适后端）。
- **#1 二阶效应（强触达）**：识别出"经 claude -p 的中立 = 伪中立"（runtime 中立但被包裹的 harness 有强自我人设污染）——这个二阶结论不在父会话提的 5 个判断点里，是从"16K 内置 prompt 抢占身份"推到"中立定位的所指要重定义"的链。同时识别 MCP-over-CLI 是错范式精致迷你版（阶段 B 否决的深层理由）。
- **#2 动态学习反哺（强触达）**：本轮是 essence `signal-weak-vs-channel-dead`（昨夜第四轮 append）的下一拍活体——第四轮证"通道没断"，本轮证"通道通了但 harness 范式本身错"；也是 `paradigm-not-feature-completeness`（5/14）的终极兑现（范式错配的具体机制被锁定到"harness 内置身份抢占"）。essence 驱动下一步架构（`essence-recursive-bootstrap`）。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `paradigm-not-feature-completeness` (2026-05-14)：终极兑现——范式错配机制锁定到"harness 自带抢占式内置身份"，覆盖率/通道/位置全是 feature 维度，范式错配才是根
  - `llm-autonomy-on-capability-invocation-is-the-bug-not-the-channel` (2026-05-19 第三轮)：下一层——不只"调不调"决策点要移走，连"我是谁"身份锚都被 harness 抢占；移走的彻底形态=绕开整个 harness
  - `signal-weak-vs-channel-dead-must-be-physically-disambiguated` (2026-05-19 第四轮)：下一拍——第四轮证通道没断，本轮证通了但 harness 范式错（前四轮共同前提被推翻的连续链）
  - `borrowed-method-as-mini-source` (2026-05-08)：双重落点——(1) 阶段 B MCP-over-CLI 是错范式精致迷你版（否决理由）(2) 本决策自身风险：绕开错 harness 却可能自造 harness 迷你版（N 月根因预判已显式标注）
  - `precondition-recheck-overturns-prior-verdict` (2026-05-19)：本轮覆盖三轮共同隐含前提"claude -p 是合适后端"——基于新铁证主动覆盖承重墙非辩护
  - `physical-anchor` (2026-04-16)：本决策最大诚实点——四铁证采信父会话未独立 prod 复跑，spike 是采信转回物理核验的必经步骤（设为前置闸门）
  - `dimension-blindness-not-asymptote` (2026-04-27)：(a) 全直连否决=不把"双后端"这个对的维度当"必须全量"，注入位置维度第五次穷尽是真穷尽（含原样回放铁证）非伪穷尽
- **本决策是否在某条 essence 上反着走**：潜在张力——`no-fatigue-narrative-for-ai`：裁"claude -p 救不了，绕开它"会不会是认输叙事？检验：不是。这不是"技术穷尽只能这样"，是四次独立实证（v0.2/v0.4/三轮 spike/本轮 spike 原样回放）锁死一个范式错配 + 给出有物理证据的替代路径（直连短 system 实证 [[STR-OK]] 通），是维度切换不是下场。另一张力——`premature-abstraction-tripwire`：现在裁双后端是不是过早？检验：不是抽象先行，是 spike 前置闸门范式（最小 vertical slice 验证才铺开），且驱动力是四次实证不是预判。明示：无实质反走，议题性质（四次实证锁死的范式错配）决定。
- **cross-check 用的关键词**（物理证据，启动时已全文 Read essence.md）：`paradigm-not-feature` / `llm-autonomy-on-capability` / `signal-weak-vs-channel-dead` / `borrowed-method` / `precondition-recheck` / `physical-anchor` / `dimension-blindness` / `no-fatigue-narrative` / `premature-abstraction` — 全部在 essence.md 命中既有条目

### essence 候选

- slug: harness-self-identity-preempts-injected-persona
- 一句话: 为 agentic 自主设计的 harness（claude -p 类）自带抢占式内置身份（16K 系统 prompt + 工具定义把模型锚成"我是该 harness 的 agent"），任何业务人设无论注入 system 任何位置还是 user message 都是结构性二等信号——不是注入方式问题（位置维度已穷尽），是"把受人设约束的对话错误地架在为无约束 agentic 设计的 harness 上"的范式错配；正解是按"是否受人设/行为约束"分后端，受约束的绕开该 harness 直连模型 API 自管工具循环，不受约束的（确定性 skill 流水线）继续用 harness 无损。是 paradigm-not-feature-completeness 的终极兑现 + llm-autonomy...is-the-bug 的下一层（连身份锚都被抢占）+ borrowed-method-as-mini-source 在"MCP-over-CLI 是错范式迷你版"的落点。
- 是否已 append 到 essence.md: Y

### 外部锚点

- `~/githubProject/cc-space/threads/cc-assistant.md` ← 范式第五次收敛 + 双后端裁决进此 thread
- `~/githubProject/cc-space/threads/cc-gateway.md` ← 多后端中立 runtime 重定义 + workspaceId 跨 backend 语义分叉 + 阶段B否决 + 跨消费方安全重定性下调
- `~/githubProject/gg/memory/reflections/2026-05-19_cc-assistant-llm-autonomy-is-the-bug.md` ← 第三轮（本轮覆盖其阶段B MCP 承重解）
- `~/githubProject/gg/memory/reflections/2026-05-19_cc-assistant-system-channel-not-delivered-rejudge.md` ← 第四轮（本轮是其下一拍，通道没断→harness 范式错）
- `/Users/xuke/CGProject/cc-gateway/server/runner.js` L37（append-system-prompt 确实送达，与 spike 铁证#1 一致）/ L42（per-agent permissionMode）← 阶段 A 物理事实
- `/Users/xuke/CGProject/cc-gateway/config/agents.json` ← personal-assistant/business-proxy/task-runner 当前配置（裁决落点：加 backend 字段）

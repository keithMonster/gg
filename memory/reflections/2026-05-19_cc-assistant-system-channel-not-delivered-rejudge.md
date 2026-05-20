---
date: 2026-05-19
slug: cc-assistant-system-channel-not-delivered-rejudge
summoner: cc-space
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: cc-assistant 二次根因翻转——不是 helper-mode 压制，是 system 通道物理断（P1/阶段B 重审）

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**一句话**：P1 范式轴（不让 LLM 持有调用决策点）成立且被本次证据**加固**，但 P1 给出的"承重解=工具空间约束"的论证链全错——不是"prompt 信号弱需压制"，是"prompt 通道物理断了，实验从未有效进行过"。第一优先级动作不是阶段 B，是**修通 claude CLI→new-api 的 system 通道**（全消费方沙箱失效的单一根因 + 修通后解空间重开）。

**1. P1 重审**：
- 范式轴（能力供给不该依赖 LLM 自主决定调不调）→ **保留并加固**。新根因证明 v0.2→v0.4 失败根本不是"LLM 不听引导"，是引导文字从没到过 LLM 眼前——"靠 prompt 传约束"这条路在当前 new-api 拓扑下物理断。
- 承重解（工具空间约束 b）→ **判据全部作废**。P1 的论证链「prompt 维度已穷尽 → 转工具空间」前件是伪命题（prompt 维度从没被有效测试，信号没送达=实验无效）。(b) 方向可能仍对（CLI flag / tools 参数不经 new-api 推理链，不受翻转影响），但**降级为"通道修通后仍需的一层"，不再是"现在要冲的第一件事"**。

**2. 阶段 B（MCP）重审**：仍成立但排在"修通道"之后。拆两层——"MCP 工具在 tools 参数"不受影响（tools 经 new-api 实证通）；"引导 LLM 优先用工具而非幻觉直答"若靠 system prompt 则**同样断**（阶段 B 最隐蔽暗礁：工具可用 ≠ 工具会被用）。真正消灭"调不调"决策点的是 (a) 确定性预取（走 user message，实证通），不是 MCP。

**3. 修 vs 绕路线**：
- **修通道=主线 P0**（一次投入、全消费方收益、解空间重开）。
- **user message 注入=兜底 P1，与定位 spike 并行**（实验4证 user message 经 new-api 通；spike 结论任何分支都不浪费这投资）。
- **直连 /v1/messages=否决**（放弃 CLI agent 全部能力，代价最大且有更便宜替代）。
- **essence 钉死前提**：必须先做定位 spike（抓包到 claude CLI 实际向 new-api 发的请求体 vs 实验4那个通的 /v1/messages body 逐字段对比）才能判"修得动还是修不动"——父会话自己说"未细查到抓包级"，这是 `mechanism-relocation-has-its-own-precondition` 不可跳的那一步。定位二分：断口在 new-api/env 配置侧 → 修（根治）；断口是 claude CLI 对非官方 endpoint 硬阉割 → user message 注入升级为终解。

**4. 跨消费方沙箱失效处置**：独立升级为 prod 安全事项（挂 threads/cc-gateway.md + 同步 Keith Context Asymmetry——整个 cc-gateway system prompt 沙箱层全消费方从未生效，比 P1 reflection 的 business-proxy 单点严重）。阻塞性"中"：不阻塞华昇/cg-meetos 确定性 cron（不依赖 system 约束），**阻塞 personal-assistant 企微真实用户接入**（在 system 通道修通或 user message 沙箱约束落地前不放开）。无活体攻击证据，按 P0 排期不做"停服等修"。

**5. 阶段 A 保留确认**：保留正确，不回滚。P2 persistence（resume 重传）是任何方案必要前提且与通道断正交；per-agent permissionMode（disallowedTools 走 CLI flag 不经 new-api）是当前唯一真实存在的工具空间防护层。**新增边界标注**：阶段 A reflection 里"business-proxy disallowedTools 经 dontAsk 真生效"要补——生效的只有 CLI 层 disallowedTools，business-proxy 赖以工作的"能力清单 systemPromptAppend 注入"依然因通道断失效（绕一圈发现 v0.2 最初的病根在这）。

**行动建议（按序）**：① 不回滚阶段 A ② P0 做 system 通道定位 spike（容器内 claude CLI debug/抓包 vs 实验4 body 逐字段比对）③ P1 与 ② 并行起手 user message 注入兜底实现 ④ ② 结论二分：配置侧→修 / CLI 硬阉割→user message 升终解 ⑤ 跨消费方沙箱失效独立登记 prod 安全事项 + 告知 Keith ⑥ 阻塞边界：personal-assistant 企微真实用户接入待 ②/③ 之一闭环 ⑦ 阶段 B（MCP）排 ④ 之后 ⑧ Keith 不需新 ack，需告知两件 Context Asymmetry（全消费方 system 沙箱空 + "prompt 已穷尽"是伪命题）；user message 注入若触及中立定位（业务人设混进对话历史，第 4 次撕中立边界）那一步回 Keith，是 ④ 定位后不是现在。

### 核心假设

1. 实验4对照（直 curl /v1/messages system 字段透传 vs claude CLI --append-system-prompt 不透传）构成确凿定位——采信父会话陈述的 ≥4 症状证据链，我未独立在 prod 容器复跑（物理实证降级为采信，已显式标注）。
2. claude CLI 的 disallowedTools / allowedTools / permission-mode 是 CLI 进程层硬约束不经 new-api 推理链——采信前序 spike S1/S2/S4 结论 + runner.js L41 注释（"bypassPermissions 会绕过整个权限层，dontAsk 让 disallowedTools 生效，实测 spike S1/D"）。
3. "修通道"这个解自身依赖未核实前提：断口可在 cc-gateway/new-api 配置侧修复，而非 claude CLI 对自定义 endpoint 的硬行为。若是后者修不动——已用"定位 spike 前置 + 二分路线 + user message 并行"对冲，不假设修得动。
4. user message 经 new-api 通（实验4 messages 复述 + Bash 能调实证）——采信父会话证据。

### 可能出错的地方

- **最可能崩点**：定位 spike 发现断口是 claude CLI 对非 api.anthropic.com 的 base_url 故意阉割 system（CLI 内部硬行为，非配置）→ "修通道"路线整条失效，被迫全押 user message 注入。概率中等——CC CLI 对自定义 endpoint 的 system 处理是已知模糊地带，且"原生 /v1/messages 通但 CLI 注入不通"这个症状差恰好指向 CLI 封装层而非 new-api。已用"user message 并行起手"对冲，崩了不浪费投资。
- **次可能**：user message 注入引入语义债（人设/沙箱约束混进对话历史，多轮被用户消息稀释/覆盖——system prompt 设计本意就是抗稀释的稳定层），导致"修好了通但约束多轮后漂移"，需要再加 turn 级重注入机制。
- **第三**：跨消费方安全事项的阻塞边界判断错——若 cg-meetos 判断层实际并非纯确定性流水线（采信父会话"走 huasheng cron 范式同可用性域"陈述，未独立 grep cg-meetos 判断层调用点），则"不阻塞 cg-meetos"判断要重画。

### 本次哪里思考得不够

1. **没在 prod 容器独立复跑实验4** —— 整个裁决建立在采信父会话的 ≥4 症状证据链上。证据链本身逻辑自洽（原生 system 通 + CLI 注入不通 + 非身份机械指令也不通，已排除身份干扰），但物理实证铁律要求我标注：方向裁决我拍（轴对），证据链真实性采信父会话（未独立核验），定位 spike 是把采信转回物理核验的必经步骤。
2. **没看 new-api 配置 / claude CLI 对 ANTHROPIC_BASE_URL 的实际请求格式** —— "修 vs 绕"的核心物理事实（断口在配置侧还是 CLI 硬行为）我没能力在本次会话内核到（需 prod 容器抓包），只能给"定位 spike 前置 + 二分路线"。这是诚实的能力边界，不是疏漏——但意味着"修通道优先级最高"这个结论的可执行性依赖一个我没核的前提。
3. **没量化 user message 注入的多轮稀释速度** —— 说了"会被对话稀释"但没给"几轮后失效"的估计，user message 兜底方案的语义代价画得粗。

### 如果 N 个月后证明决策错了，最可能的根因

**最可能根因**：定位 spike 证实断口是 claude CLI 对非官方 base_url 的硬阉割（不可配置修复）→ "修通道为主线"整个排期错位，真正该第一优先做的是 user message 注入（我把它降为 P1 兜底，应该是 P0 终解）。即：轴判对（范式轴加固 + 通道是真问题），但"修 vs 绕"的优先级押错——把"修"当主线是基于"断口可配置修复"这个未核前提，而 `mechanism-relocation-has-its-own-precondition` 恰恰警告这种"给出移走/修复诊断的人跳过落点前提核实"。我已用"并行起手 user message + 定位 spike 前置"把这个错位的代价降到最低（无论哪分支 user message 投资不浪费），但优先级叙事本身可能误导父会话先投"修"的工时。

**次可能根因**：通道修通后，P1 的解空间重开（system prompt 引导重新可用），父会话可能误判"那范式轴不需要了，回到 prompt 引导 LLM 自主就行"——通道修通**不消解范式轴**（让 LLM 自主仍是错轴，只是现在引导文字至少能送达了）。reflection 里强调了两个结论叠加不冲突，但这是最容易在"通道修好的兴奋期"被丢掉的二阶结论。

### 北极星触达

- **#3 决策超越直觉（核心触达）**：直觉（父会话 + 我前两轮）在"P1 范式轴是否还成立 / 阶段 B 怎么调"的框里。本决策反转为"P1 范式轴不是被推翻是被加固，但它的论证前件（prompt 已穷尽）是伪命题——真问题是一个比范式轴更靠地基的物理断口，且这个断口的修复方案自身有未核前提"。三层穿透：范式轴层（保留）→ 论证前件层（作废）→ 物理通道层（新主线）。
- **#1 二阶效应（强触达）**：识别出"阶段 B 的 MCP 工具可用 ≠ 工具会被用"这个暗礁——MCP 让工具进 tools 参数（通道好），但"该用工具时去用"的引导若靠 system prompt 则同样断。这个二阶效应不在父会话提的 5 个判断点里，是从"system 通道断"推到"阶段 B 半残"的链。
- **#2 动态学习反哺（强触达）**：本轮是 essence `precondition-recheck-overturns-prior-verdict`（昨夜 append）的第三拍活体——昨夜那滴说"旧裁决依赖的物理前提被推翻要主动覆盖承重墙"，今天连"prompt 维度已穷尽"这个 P1 论证前件都被证伪，正是该滴的预言落地。essence 驱动下一步架构判断（`essence-recursive-bootstrap`）。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `precondition-recheck-overturns-prior-verdict` (2026-05-19 夜)：核心——旧裁决前提被推翻主动覆盖承重墙，本轮覆盖 P1 "prompt 已穷尽"论证前件
  - `mechanism-relocation-has-its-own-precondition` (2026-05-19)：直接落点——"修通道"这个解自身依赖"断口可配置修复"未核前提，强制定位 spike 前置
  - `llm-autonomy-on-capability-invocation-is-the-bug-not-the-channel` (2026-05-19)：被本轮精化——原滴隐含"那些 prompt 通道至少是通的"前提，本轮证明 system 这条物理断
  - `physical-anchor` (2026-04-16)：本决策最大诚实点——证据链采信父会话未独立物理复跑，定位 spike 是采信转回物理核验的必经步骤
  - `network-cannot-cut-what-shares-tuple` (2026-05-19)：跨消费方沙箱失效=纸面防御层 prod 恒空，真实层数 < 纸面层数，同形态
  - `fallback-detectability` (2026-05-06)：跨消费方沙箱失效是"失败被误判为成功"的活体——约束本该挡的事没挡，但功能没炸所以没人发现
  - `dimension-blindness-not-asymptote` (2026-04-27)：P1 "prompt 维度已穷尽"是把从没测过的维度当已穷尽——这次是"无效实验冒充穷尽"的新形态
- **本决策是否在某条 essence 上反着走**：潜在张力——`no-fatigue-narrative-for-ai`：我说"修通道修不动就转 user message"会不会是认输叙事？检验后判定无反走——这不是"技术穷尽了只能这样"，是给出了二分路线 + 两条都有明确物理可行性证据（修=实验4 system 字段通证明可修复性存在；绕=user message 实证通），是维度切换不是下场。明示：无实质反走，议题性质（物理断口二选一路线）决定。
- **cross-check 用的关键词**（物理证据，启动时已全文 Read essence.md）：`precondition-recheck` / `mechanism-relocation` / `llm-autonomy-on-capability` / `physical-anchor` / `network-cannot-cut` / `fallback-detectability` / `dimension-blindness` / `no-fatigue-narrative` — 全部在 essence.md 命中既有条目

### essence 候选

- slug: signal-weak-vs-channel-dead-must-be-physically-disambiguated
- 一句话: 诊断"换通道无用、要移走决策点"时必须先物理核验每条候选通道当前是否真的通——把"信号弱"和"信道断"混为一谈，会让一个无效实验的结论冒充"维度已穷尽"，驱动错误的架构转向（这里：用"prompt 穷尽了"论证"必须上工具空间约束"，而真相是 prompt 从没被有效测过）。是 `dimension-blindness-not-asymptote` 的下一层（不只"在错维度微调"，更隐蔽的是"实验本身无效却被当结论"）+ `precondition-recheck-overturns-prior-verdict` 在"论证前件"而非"结论前提"维度的精化。
- 是否已 append 到 essence.md: Y

### 外部锚点

- `~/githubProject/cc-space/threads/cc-assistant.md` ← v0.4 二次根因翻转进展入此 thread
- `~/githubProject/cc-space/threads/cc-gateway.md` ← system 通道断 + 跨消费方沙箱失效 prod 安全事项 + 修/绕路线入此 thread
- `~/githubProject/gg/memory/reflections/2026-05-19_cc-assistant-llm-autonomy-is-the-bug.md` ← P1 原裁决（本轮覆盖其论证前件）
- `~/githubProject/gg/memory/reflections/2026-05-19_cc-gateway-permission-mode-falsification-recalibration.md` ← 阶段 A permission-mode 校准（本轮确认保留 + 补边界标注）
- `/Users/xuke/CGProject/cc-gateway/server/runner.js` L37（resume 也注入 append-system-prompt，P2 已修）/ L42（per-agent permissionMode）← 阶段 A 物理事实
- `/Users/xuke/CGProject/cc-gateway/.env` ANTHROPIC_BASE_URL/AUTH_TOKEN/MODEL ← system 通道断的拓扑根（claude CLI→new-api 这一跳）

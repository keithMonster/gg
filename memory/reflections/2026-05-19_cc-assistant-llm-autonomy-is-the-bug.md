---
date: 2026-05-19
slug: cc-assistant-llm-autonomy-is-the-bug
summoner: cc-space
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: cc-assistant v0.4 二次证伪——错的不是注入通道，是 LLM 持有"调不调"决策点

### 给父会话的最终输出（必填）

**P1 范式裁决**：选 **(b) 工具空间强制约束（MCP / `--allowedTools` 白名单）**，**(a) 确定性预取作补充层（仅覆盖高频固定前置数据链 ≈ 台账 §3 那 10 项 pluginModule 性质）**，**(c) 明确否决**，不需要新"第 5 形态"。

核心判断：(a)/(b)/(c) 不是三个并列范式选项——把它列成并列本身是上次错误的同构复发。真轴是「**LLM 自主决定要不要调能力**」这件事本身不该存在。v0.2→v0.4 两次失败共享的未审视前置假设 = 我 5/14 决议的盲区：我说了"范式错位"，但给的 v0.4 路径（systemPromptAppend + LLM 自主 curl）仍把"调不调"决定权留在 LLM 手里。今天铁证不是证伪"换注入通道"，是证伪「能力供给依赖 LLM 自主决策」这个更深预设——essence `control-flow-vs-fact-supply` 精确命中（一直在"控制流自主"维度调参，真问题在"事实供给"维度）。

**(b) 是承重解，(a) 是其覆盖不到的高频固定意图的补充，不互斥**：
- (a) 单独会塌在"预取什么"——cc-assistant 收消息时还没经 LLM 理解意图，没法判断动态复合意图（"上周华昇进度+张吉峰参与"）该预取啥；只能覆盖每轮都垫的固定前置数据链。
- (b) 是动态查询类唯一确定性解：把 endpoint 从"建议 curl"变成 LLM 工具空间里**唯一能拿该数据的合法工具**——不是引导它走，是它没别的路。这是 cc-space 元方法论 B1（内部不可靠→外部锚点托底）教科书落地：prompt 维度已实证穷尽，转工程结构（工具空间约束）托底。

**代价不对称点**：
- (a) 纯预取：覆盖不了动态意图 + 全量注入撑爆 context。代价显性当场可见、可快速回退。
- (b) 白名单/MCP ✅：claude CLI `--allowedTools`/`--mcp-config` 在 resume 分支当前完全没透传（=P2 同根 bug），且 bypassPermissions 下白名单是否真硬隔离 Task/Skill 逃逸**需 spike 实证**。代价 = 一次性 spike + P2 修复，验证通过后稳态可靠——不对称有利（投入有界，收益是概率引导→确定性约束）。
- (c) 收窄功能：等于宣告"FastGPT 小助理迁 CC"主线失败 + 议题 18 数据源链作废 + Keith 5/14 目标层作废。代价极度不对称且不可逆。**前提"helper-mode 不可压"未被证实**——只实证了 prompt 注入压不动，没实证工具空间约束压不动（后者是进程层物理约束非 prompt 手段）。把没试过的工程维度当"已穷尽"而放弃 = `dimension-blindness-not-asymptote` 在"放弃"方向的复发 + 违反 `no-fatigue-narrative-for-ai`。**否决**。

**(b) 实施约束（承重，父会话必须按此走）**：
1. **先 spike 后铺开**：cc-gateway 容器内手测 claude `--allowedTools` 只放 cc-assistant 工具 + 砍 Task/Skill/Bash 通配，发"张吉峰是谁"，物理核验 LLM 能否逃逸到 cg-skills query_readonly。这是 (b) 可行性闸门（`fallback-detectability`：不实证就铺开会误判"白名单生效了吗"）。spike 失败→才升级 MCP 强制或回 (a)+功能分层。
2. **MCP 优于 allowedTools 字符串**：cc-assistant 暴露 MCP server，cc-gateway 经 `--mcp-config` 注入。MCP 工具是工具空间一等公民，helper-mode 对"调已注册工具"训练偏好**正向**——顺训练偏好而非对抗（对比 prompt 引导 curl 是对抗 helper-mode 不用陌生 HTTP 的偏好）。这是跳层关键：不是"禁它乱跑"，是"把能力做成它本来就爱用的形态"。
3. **bypassPermissions 不改**（不动 runner.js L36）：permission-mode 管"问不问用户"，不是工具空间隔离层。隔离靠 allowedTools/MCP，混淆两层会引新 bug。

**P2 排期判断**：**P2 必须现在独立修，且是 P1 (b) 的前置**。runner.js L31-34 resume 分支 `else { args.push('--resume', sessionId) }` 完全跳过 L27-30 的 systemPrompt/append/allowedTools/disallowedTools 透传——物理代码事实，父会话诊断准确。(b) 靠 allowedTools/mcp-config 约束工具空间，而 resume 恰恰全跳过 → 首话关死工具空间，第二 turn 又全 open，逃逸路径回来 → **P2 不修 (b) 只首话生效=等于没做**。P2 不依附 P1（确定性 bug，各方向公约数），反而是 P1 前置。**隐藏不确定性**：claude CLI 对 `--resume` 会话是否接受重设 system prompt / 重设工具白名单，行为本身要 spike 确认，别假设"补上 push 就行"。

**Keith ack 边界**：需要回 Keith，ack 的是**范式轴重定义**不是 (b) 选型。(b)vs(a)vs(c) 技术选型 = 实现/架构层，gg 已拍 (b)，父会话直接做。需 Keith 目标层 ack 的精确一条 = 「能力供给从『LLM 自主决定调用』改为『工具空间强制约束』」——Keith 5/14 拍"范式：开放式 agent"，(b) 在"开放程度"上实质收窄为"开放推理 + 受约束工具空间"，触及目标层措辞解释边界（B8 选错难回退 + 议题 18 耦合 + Decision Authority"改了目标范围"trigger）。ack 话术给 Keith（举手+否决权，非外包）：「v0.4『LLM 自主 curl』被 5/19 企微 e2e 二次证伪（prompt 维度已穷尽）。gg 裁决能力供给改工具空间强制约束（MCP/白名单），LLM 推理仍开放但拿数据无逃逸路径，把『开放式 agent』收窄为『开放推理+受约束工具空间』。这是对你 5/14 目标层措辞的实质收窄，需你拍。想保持完全开放式（继续赌 prompt 引导）请否决——但那条路已实证穷尽。」不需 ack：MCP vs allowedTools 内部选择 / P2 修复 / spike 怎么做（全实现层，已拍）。

**行动建议（父会话下一步）**：
1. 不要继续在 prompt 措辞维度调（v0.2→v0.4 两次实证穷尽，再投入是 dimension-blindness 复发）。
2. 拉 Keith 范式轴 ack（上方话术），等点头再动工程。
3. ack 后：先做 P2 spike（claude --resume 是否接受重设 system prompt/工具白名单）→ 修 P2 resume 透传 → 做 (b) spike（容器内白名单/MCP 能否硬关 Task/Skill 逃逸）→ spike 绿才铺开 MCP server。
4. (a) 补充层：台账 §3 那 10 项每轮垫的前置数据链改 cc-assistant 侧确定性预取注入（不靠 LLM 自主），动态业务查询走 (b)。
5. 落 thread：`cc-space/threads/cc-assistant.md` + `cc-space/threads/cc-gateway.md`（P2 修复 + MCP 契约）。

### 核心假设

1. claude CLI `--allowedTools`/`--mcp-config` 在 bypassPermissions 下对 Task/Skill 逃逸是**硬约束**而非软建议——**未实证，是 (b) 可行性闸门，故强制 spike 前置**。
2. claude `--resume` 接受重设 system prompt / 工具白名单——未实证，P2 修复内嵌不确定性。
3. cc-assistant 能暴露 MCP server 且 cc-gateway 容器网络可达（stdio 或 HTTP MCP）——工程可行性高但未验证拓扑。
4. Keith 接受"开放式 agent"被收窄为"开放推理+受约束工具空间"——可能撞他对"CC agent 自由度"的心理预期。

### 可能出错的地方

- **最可能崩点**：spike 实证 claude CLI 工具白名单在 bypassPermissions 下不硬（LLM 仍能用某种方式触达容器 cg-skills）→ (b) 路径失效，被迫回 (a)+功能分层（实质接近 (c) 的退化但保留高频固定意图）。概率中等——CLI flag 行为在 bypassPermissions 组合下是已知模糊地带。
- **次可能**：MCP server 接入引入新的 cc-assistant↔cc-gateway 拓扑耦合（MCP 进程生命周期 / 容器网络 / 协议版本），把"中立 runtime"定位再次撕开——和 5/15 那次"agents.json 写人设违反中立"同形态风险。
- **第三**：Keith 否决范式收窄、坚持完全开放式 → 决策回到原点，但这次有"两次实证穷尽 prompt 维度"的硬证据顶着，否决成本由 Keith 显性承担。

### 本次哪里思考得不够

- **没实测 claude CLI 工具白名单在 bypassPermissions 下的真实隔离强度**——(b) 的承重前提建在"CLI flag 应该硬"的合理推断上，没物理核验。我把它显式降级为"spike 前置闸门"而非"已确证方案"，但这意味着 P1 裁决的确定性不是 5/5——(b) 方向正确（轴对了）确定，(b) 具体机制可行性 4/5（依赖 spike）。诚实标注：方向裁决我拍，机制可行性留给父会话 spike 验证。
- **没看 cc-assistant 当前是否已有 MCP 暴露能力 / 原生 http 零依赖架构能否容纳 MCP server**——MCP 优于 allowedTools 是基于"顺训练偏好"的架构判断，没核验 cc-assistant 仓的工程现实（零依赖原生 node:http vs MCP SDK 依赖引入）。
- **没量化 (a) 补充层"每轮垫前置数据链"的 context 成本**——说了"全量注入撑爆 context"但没算台账 §3 那 10 项实际 token 量，(a) 边界画得粗。

### 如果 N 个月后证明决策错了，最可能的根因

**最可能根因**：spike 证实 claude CLI 在 bypassPermissions 下工具白名单/MCP 无法硬隔离 LLM 对容器内 cg-skills 的访问（CLI 工具约束语义在该模式下是软的）→ (b) 物理不可行 → 真正的解被迫退到"cc-gateway 容器层物理移除 cg-skills 对 personal-assistant 的可见性"（runner.js 真隔离每 agent skill 可见性，5/14 增量 1 已登记的 v0.5 议题）或彻底回 (a)+功能分层。即：轴判对了（LLM 不该持有调用决策点），但实现层选错了约束机制（应该在容器/runner 层做物理隔离而非 CLI flag 层）。

**次可能根因**：Keith 范式收窄 ack 后，MCP 接入把 cc-gateway 中立定位第三次撕开（5/14 disallowedTools 透传 / 5/15 人设解耦 / 5/19 MCP 注入——三次都在"中立 runtime"边界上加业务耦合），最终 cc-gateway 事实上不再中立，需要更大的架构重定。

### 北极星触达

- **#3 决策超越直觉（核心触达）**：父会话直觉是"在 (a)/(b)/(c) 三个范式里选一个" → 本决策反转为"三选项共享同一错误预设（LLM 持有调用决策点），真解是把决策点物理移走"——#3 本质（不停留在选项裁决，追问选项空间的预设）。这是对我自己 5/14 决议盲区的二阶修正。
- **#1 二阶效应（强触达）**：识别出 P2（resume 不透传）是 P1 (b) 的物理前置而非独立 bug——"白名单首话生效但 resume 失效"这个二阶效应没在父会话诊断里，是从 runner.js L31-34 代码事实推出的。
- **#2 动态学习反哺（强触达）**：5/14 我 append 的 `paradigm-not-feature-completeness` 被本轮自己的 `bug-shape-survives-fix` 复发证伪精化——上一滴说"范式机制重要"但我给的路径仍依赖 LLM 自主，本轮把"错在哪一层"逼出来。essence 驱动下一步架构（`essence-recursive-bootstrap`）。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `control-flow-vs-fact-supply` (2026-05-18)：错轴诊断核心——一直在"控制流自主"维度调参，真问题在"事实供给"维度。本决策把能力供给从控制流自主层移到事实供给约束层
  - `paradigm-not-feature-completeness` (2026-05-14)：本决策是其下一层精化——上滴说范式机制重要，本滴定位"错在让 LLM 持有它系统性不可靠的决策点"
  - `bug-shape-survives-fix` (2026-04-27)：我 5/14 修了"功能覆盖率"诊断，没修自己"仍依赖 LLM 自主"的内化假设——bug 形态幸存于我的修复，本轮父会话二次证伪逼出
  - `dimension-blindness-not-asymptote` (2026-04-27)：(c) 收窄功能 = 把"工具空间约束"这个没试过的维度当已穷尽——同维度盲区在"放弃"方向复发
  - `no-fatigue-narrative-for-ai` (2026-04-22 ~/.claude)：(c) 用"helper-mode 不可压"的认输叙事收尾，违反"换维度不下场"
  - `fallback-detectability` (2026-05-06)：(b) 强制先 spike——不实证"白名单生效了吗"会被误判为成功
  - `borrowed-method-as-mini-source` (2026-05-08)：MCP 优于 prompt 引导的深层理由——顺 helper-mode 训练偏好（调已注册工具）而非在 CC 里造"建议它 curl 陌生 HTTP"的对抗结构
- **本决策是否在某条 essence 上反着走**：潜在张力——`premature-abstraction-tripwire` / `theory-gap-without-data` 可能质疑"现在就上 MCP 是不是过早抽象"。已用 spike 前置闸门对冲（不是先建 MCP，是先 spike 验证工具空间约束可行性，绿了才铺开）——本质是 tripwire 范式不是抽象先行，无实质反走。
- **cross-check 用的关键词**（物理证据，已 grep）：`control-flow-vs-fact-supply` / `paradigm-not-feature` / `bug-shape-survives-fix` / `dimension-blindness` / `fallback-detectability` / `borrowed-method` / `premature-abstraction` / `theory-gap` — 全部在 essence.md 命中既有条目

### essence 候选（可选）

- slug: llm-autonomy-on-capability-invocation-is-the-bug-not-the-channel
- 一句话: 当"LLM 是否调用某能力"由 LLM 自主决定时，换注入通道（user message → systemPromptAppend → 任何 prompt 位置）都在同一根错轴上——真解是把"调不调"决策点从 LLM 手里物理移走（工具空间没别的路），不是再换一个通道
- 是否已 append 到 essence.md: Y

### 外部锚点

- `~/githubProject/cc-space/threads/cc-assistant.md` ← 本决策后续 v0.4 范式收窄进展入此 thread
- `~/githubProject/cc-space/threads/cc-gateway.md` ← P2 resume 透传修复 + MCP 注入契约落此 thread
- `~/githubProject/gg/memory/reflections/2026-05-14_cc-assistant-v03-paradigm-mismatch.md` ← 5/14 决议（本决策是其盲区的二阶修正）
- `/Users/xuke/CGProject/cc-gateway/server/runner.js` L31-34 ← P2 根因代码事实（resume 分支跳过工具/prompt 透传）

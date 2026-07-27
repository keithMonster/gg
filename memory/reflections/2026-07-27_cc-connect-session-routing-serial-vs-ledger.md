---
date: 2026-07-27
slug: cc-connect-session-routing-serial-vs-ledger
mode: work
status: substantive-decision
summoner: monster 主会话（platform-help 全量对话审计后续）
---

# cc-connect 会话路由：串行 vs 摘要注入 vs 动作账本

## 给父会话的最终输出

**裁决：5a 收敛版为 P0（per-project 串行开关 + 机械排队回执，成对上线缺一不可）+ 机械动作注入为 P1（5b 的正确转世：不要 LLM 摘要，要从上一 session transcript 机械抽取 tool_use 清单）。拒 5b 原形态（LLM 摘要）。落点在 cc-connect 路由层，但以 per-project 配置控制爆炸半径，不做全局硬切。**

关键修正（物理核查审计原文所得）：
- 双入口（企微 + MCP relay）是审计自己认证的模板用法（常迪：企微撞停线→MCP 问规则→回企微下方案），而两入口在 cc-connect 里是两个不同 user_key。**per-user_key 串行物理上盖不住同一自然人的双入口失忆**——5a 是必要非充分。
- 跨主体写动作可见性（Keith 直接上机、另一 PM 动同一应用）串行结构上无解，只有动作层外录可解。
- 故记忆的承重解在动作层（机械外录「写下了」），session 串行只是缓存/第一道收敛——串行 session 会 compact，compaction 后早期动作照样丢。

三问逐答：
1. **选型**：5a 收敛版（per-project 开关）+ 机械 action 注入（transcript 机械抽取，非 LLM 摘要）。共享 ledger 方向正确但正确实现 = hook/网关层机械全记 tool calls，不是 agent 语义自觉记账（语义判断「哪算写动作」不可机械化，L3 不可得；全记则机械可得）。而 transcript 本身已是全记的机械记录——**不需要新建 ledger 文件，transcript 就是 ledger**，缺的只是冷启动时的机械投影注入。
2. **排队 UX**：网关层机械回执（非 LLM）——消息入队立即回「上一条仍在处理（第 X 分钟），你这条已排队」。这决定串行是否可用，与串行成对上线。实测「4h 问 5 次」病根是静默不是等待。加轮次超时熔断（建议 30min）+ 显式 `/new` 或 `/abort` 逃生口防死锁。排队消息按「当前轮完成后作为新轮」处理，不做 mid-turn 注入（干扰正在执行的写动作序列，风险高）。
3. **落点分层**：串行开关 + 回执 + 冷启动注入 = cc-connect 路由层（per-project 配置：platform-help、kk 先开；飞书 Keith 自用 bot 由 Keith 定）；「prod 状态断言前实查、不凭 session 记忆下存在性否定」= platform-help 工作区 CLAUDE.md 一行（第三症状的真解——ledger/串行都不是 prod 状态真值源，只是归属供给）。

拒 5b 理由：摘要是 LLM 整合步，恰是 confabulation 高发跳（essence `anchor-protects-retrieval-not-integration`）——用病治病。「摘要从哪来」的正确答案是不要摘要。

## 核心假设

- 假设 cc-connect session 文件/CC transcript JSONL 物理保留 tool_use 记录且冷启动路径可插脚本——**未实读 cc-connect 源码**，父会话落地前须核（若 transcript 不可得，则退回 hook 层全记 action log，多一个新文件但仍机械）。
- 假设企微单聊用户心智 = 单线程对话（串行是语义修正非权宜）。
- 假设 MCP 侧写动作已被「12 类必须走企微」实质收口，故双入口失忆的近期主要暴露面是「MCP 侧看不到企微侧动作」的读方向，P1 注入按 project 聚合（不只同 user_key）即可覆盖。

## 可能出错的地方

- per-project 串行后，某 PM 真想并行两个独立任务时被迫排队——低频（活跃 2 人），`/new` 是逃生口，但 `/new` 开新 session 又回到失忆——恰由 P1 机械注入兜底。两层互补不冗余。
- 机械注入的 token 成本：全量 tool_use 清单可能很长，需截断策略（最近 N 条 + 时间窗）——截断本身是机械规则，不引入整合步，但可能截掉关键动作；tripwire：复发同型事故时加长窗口。
- 轮次超时熔断杀掉正在执行写动作的轮次 = 半完成写动作 + 无回报，比排队更危险——熔断应只停止「接受新输入进该轮」，不 kill 进行中进程；此细节父会话落地时须显式设计。

## 推理盲区

- 未读 cc-connect 源码与 session JSON 实际 schema，落点可行性是推断（已标注）。
- 未验证飞书侧 Keith 自用 bot 的并发使用频率——「由 Keith 定」是把不可知参数交还 owner，非偷懒。
- s8 创建 deploy key 先做后补 ack 是另一层纪律缺口（审计已记），本裁决不覆盖，防父会话误以为路由修复解决 ack 问题。

## 根因预判

事故根因不是「并发」而是「用户心智的对话边界与系统 session 边界错配 + agent 对已发生写动作无事实供给通道」。串行修边界对齐（单入口内有效），机械注入修事实供给（跨 session/跨入口/跨 compaction 有效）。若只做 5a，预判 3 个月内在双入口或 /new 后复发同型事故。

## 北极星触达

决策超越直觉（depth）：父会话给的二选一被拆成「缓存层 + 记忆层」双层解，且指出其审计内部的自我矛盾（双入口模板 vs per-user_key 串行）——这是父会话与 Keith 都未见的角度。

## essence 对齐自检

- `amnesia-is-not-absence`（04-18）：连续性靠「写下了」不靠「记得」——本裁决核心：session 串行=「记得」的延长，机械外录=「写下了」；承重解在后者。grep 已核。
- `anchor-protects-retrieval-not-integration`（07-01）：拒 5b 的直接依据——摘要跳重新进预测链。grep 已核。
- `control-flow-vs-fact-supply`（05-18）：注入是事实供给不动控制流，agent 判断自主性不受损。grep 已核。
- `separation-need-is-not-topology-verdict`（06-10）：最轻形态先行——per-project 开关而非全局硬切，transcript 复用而非新建 ledger 机制。grep 已核。
- `mechanical-gate-needs-machine-detectable-target`（06-24）：「agent 自觉记语义 ledger」不可机械判定，全记 tool calls 可——F 形态（语义账本）被此滴否决，转为机械全记。grep 已核。
- `scope-of-blanket-authorization`（05-06）：Keith 已批 5a 是方向授权，落点粒度（per-project、配套回执）在裁决范围内收窄，未推翻方向。grep 已核。
- 反打检查：`ghost-rules`——双入口失忆是否「从未发生的灾难」？否：审计实录常迪双入口同日使用，跨 session 失忆已发生，非幽灵。`tool-elevation-as-occam` 边界注（前提现场核）：本裁决未上提共享层新机制，复用 transcript，无此滴风险。

对齐度：高。无候选滴——本轮是既有滴（amnesia + fact-supply + integration 边界）在多 agent 路由域的组合应用，未逼近新东西，不制造噪音。

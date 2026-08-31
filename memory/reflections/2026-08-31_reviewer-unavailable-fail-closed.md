---
date: 2026-08-31
slug: reviewer-unavailable-fail-closed
summoner: Codex → Claude Code --agent gg 端到端 smoke test
northstar_reach: #1 二阶效应（静默降级的二阶代价 = 不可用事实的可观测性被毁）
status: substantive-decision
---

# Reflection: 外部审查器不可用 → fail closed 还是静默降级冒充

### 给父会话的最终输出（必填）

**推荐**：fail closed——显式报「审查器不可用」，把裁决权交回调用方 / Keith；**禁止静默降级到同源主模型并冒充该审查器**。若产品上必须有退路，唯一合法形态是**响亮降级**：结果显式打标 `reviewer=unavailable; fallback=self-review; decorrelation=none`，且不可用本身作为事件外推（notify）。「冒充」一词已把响亮降级排除在题外，故本题答案是二元的：fail closed。

**理由**：
1. 外部审查器买的不是「多一次审查」，是 **evaluator 与 generator 的去相关**（`generator-evaluator-separation` / `cross-model-decorrelates-identity-not-paradigm`）。同源主模型冒充后，去相关量归零，但读数格式不变——审查通道「计数存活、承重内容抽走」，输出退化为内容无关假绿（`the-confession-stream-is-priced-by-the-ledgers-enforcement-link` 的减载形态）。
2. 冒充把「通道死」伪装成「信号弱」（`signal-weak-vs-channel-dead-must-be-physically-disambiguated`），且它恰好摧毁的是「审查器不可用」这条事实的可观测性——`fallback-detectability`：失败被误判为成功时，修复永不触发。
3. 二阶代价：冒充后你永远不知道审查器真活过几次；今天这条 Codex→CC→gg 链路的 smoke test 本身就在验证「链路是否真通」，一个会静默冒充的调用方连 smoke test 都会假绿。

**trade-off**：fail closed 的代价 = 审查器停摆期间阻塞流水线 / 多一次人工介入；接受，因为被阻塞是可见的、可修的，假绿是不可见的、自锁的。未核验假设：调用方有能力区分「审查器不可用」与「审查器返回否决」（若两者在错误码上混同，fail closed 也会被误读，须先拆开）。

**行动建议**：调用方在审查器 client 侧实现 ① 不可用 → 抛显式错误 + 事件外推；② 若保留 fallback 开关，默认关闭、开启时输出必带 provenance 字段；③ 把「审查器可用性」作为独立读数计数，不与「审查通过率」合流。

### 核心假设
- 审查器的价值主体是去相关性而非审查文本本身（若审查器只是格式校验器，则本裁决降格为「打标即可」）。
- 调用方能物理区分「不可用」与「否决」。

### 可能出错的地方
- 场景中审查器只是低承重的 lint 级检查 → fail closed 过重，响亮降级更合理。概率低（题面写「架构审查器」）。

### 本次哪里思考得不够
- 未读父项目具体调用方代码，不知道错误码是否已把「不可用/否决」混同；smoke test 场景下按题面裁，不硬猜 context。

### 如果 N 个月后证明决策错了，最可能的根因
- 审查器停摆频率远高于预期，fail closed 造成流水线长期阻塞，团队用「常开 fallback 开关」绕过 → 事实上回到静默降级。根因是把可用性问题当策略问题解，未修审查器本身的 SLA。

### 北极星触达
#1 二阶效应：把问题从「本次审查质量」挪到「不可用事实的可观测性」。

### essence 对齐自检（必填）
- **对位 slug**：`generator-evaluator-separation` / `cross-model-decorrelates-identity-not-paradigm` / `fallback-detectability` / `signal-weak-vs-channel-dead-must-be-physically-disambiguated` / `the-confession-stream-is-priced-by-the-ledgers-enforcement-link`
- **反着走**：潜在张力——`cross-model-decorrelates-identity-not-paradigm` 指出跨模型只去身份层共盲、去不掉范式层；本裁决把「去相关」当审查器主价值，可能高估了异模型审查的实际增益。未展开：即便增益有限，冒充仍抹掉的是可观测性，结论不变。
- **cross-check 关键词**：`rg -n -i 'evaluator-independence|generator-evaluator|cross-model-decorrelates|silent|静默|降级|fail.?closed|fallback|假绿'` 于 `memory/consolidation/essence-view.md`（视图 rg 命中行 49/76/84/97/105/108/137/146）

### essence 候选（可选）
无——本裁决是既有滴的组合应用，未逼近新东西。

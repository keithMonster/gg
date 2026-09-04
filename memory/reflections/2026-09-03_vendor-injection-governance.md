---
date: 2026-09-03
mode: cc_agent
status: substantive-decision
slug: vendor-injection-governance
summoned_by: monster 主会话
topic: 要不要往全局 CLAUDE.md 立场段补「厂商注入的识别与处置」；补成什么形状
---

# 厂商注入治理 — 裁决

## 装配

- KERNEL / CORE / state / essence-view（启动链四件）
- `monster/shared/gg-briefing.md`（monster 来源召唤，B1 元方法论 / B3 分流 / B5 持久化拓扑承重）
- **原文核验**（裁决对象原文纪律：父会话给的是转述，全部回原文）：
  - `~/.claude.json` → `clientDataCacheSlots.*.data` 逐 slot dump
  - `/Users/xuke/.local/share/claude/versions/2.1.259`（Mach-O，`strings -a | grep`）
  - `monster/concepts.md`「注入器 / 拦截器」「外化锚点」条
  - `monster/auto-monster/scripts/tripwire_check.py:800-859`（`check_subagent_delegation_drought`）
- 本会话自身收到的 bypass-mode 注入（一手活体样本，非转述）

## 原文推翻的三条父会话断言

1. **「它从不自称省成本」——证伪**。注入首句逐字：`Each API request re-sends the whole conversation, so the number of turns drives cost.` 且 `experimentKey` 字面为 `claude_code_opus5_efficiency_paragraph_experiment`。它自称的就是成本。
2. **「三条方向一致，全在压推理量」——读转述得出，读原文不成立**。同一段里 `issue them together in one message` / `do not poll with sleep` 与 monster Engineering Rules ⑥ 同向；本 subagent system prompt 里的 `Do not use a colon before tool calls` 是纯格式偏好。注入是混合物。
3. **「三条同源」——物理上是两个加载面**。A 面 = 服务端 A/B 实验（`~/.claude.json` slot，**只对 claude-opus-5 下发**，claude-fable-5-1 的 4 个 slot 无 `tengu_heron_brook` 字段）；B 面 = 客户端二进制硬编码（`e.bypass` 条件分支）。变更节奏、检测方式全不同。

## 决策

见 §给父会话的最终输出。一句话：**补，但补的是上游到达哨 + 账本，不是抵抗条款；常驻侧只留一句指针。**

## 核心假设

- 注入的**到达**是 100% 机械可判的物理事件（已实证：两条命令各自把原文捞出来了）——这是全部结论的地基。假设失效条件 = 出现不落盘、逐请求动态下发的注入（已列入射程差集）。
- `clientDataCacheSlots` 会被服务端刷新覆盖（由 12 个 slot 的 `at` 时间戳分布推断，**未直接观测到一次覆盖事件**）。若实为只增不覆盖，hash 哨仍成立，只是报警语义从"变了"变成"多了"。

## 可能出错的地方

- 二进制 `strings` 哨的噪声比未测。101 条里含大量 tool description 与无关字符串，基线 diff 可能每次版本升级都刷屏 → 落地时须先跑一次实测噪声比，超标就收窄到条件注入分支（`e.bypass` 那类）而非全量。这是我给出处方却没跑数的一处。
- 「登记册不进常驻链、被哨报警时才读」——`standing-instructions-do-not-produce-standing-behavior` (08-25) 警告：器官活跃度由事件率定价。若哨的报警率极低（可能数月零红），登记册会静默饿死。缓解 = 哨报警走 notify（有物理送达），不靠我记得去读。

## 推理盲区

- 我判定「判定层已完备、缺口在激活层」，依据是立场段文本 + 39% 基率。但我**没有验证**"立场段在那三个月里是否真的被读到过而未激活"——两者在 transcript 上同形（都表现为什么都没发生）。若真因是"立场段根本没进 context"，则我的处方（加指针）方向对但剂量错，该走注入器不是指针。
- 我给了 A/B 两面哨，但没有回答"谁看守这两个哨"（`watchdog-topology-lacks-a-top`）。哨的失守零告警，这个敞口本次未解。

## 根因预判

父会话的诊断（D 段归因 L2、承认"不能靠列举解决"）是对的，处方（一条 L2 锚词 + 三条枚举）与诊断不匹配。根因 = **把对象类型判错了**：它按"对手指令"处理，物理上是"环境变量"。类型判错则治理形态必错——对手要条款，变量要传感器。

## 北极星触达

- #1 二阶效应：给出「抵抗条款会误伤同向注入」这个二阶后果，父会话草案里没有。
- #3 决策超越直觉：直觉解是"加一条更强的规则"，物理解是"别加规则，加两条命令"。

## essence 对齐自检

grep 过并真实引用：
- `perimeter-derives-from-load-path-not-self-model` (07-30) — 本次是它的第二次触发，同一病灶（围栏未覆盖加载面）
- `omission-failures-evade-event-driven-sensors` (07-28) — 判据②失败的成因；哨挂上游 = 其出路一「代理事件」的实例
- `anchor-value-in-activation-not-in-content` (06-01) — 判定层完备、激活层缺口的判词
- `the-ledger-must-not-judge-and-the-judge-must-not-remember` (08-17) — 登记册只存事实不存规则
- `downstream-gate-is-upstream-sensor` (08-28) — 建哨当场写射程差集
- `stale-observer` (04-15) + `one-shot-invariant-decays-under-live-append` (08-11) — 否决"枚举进常驻段"
- `rule-with-half-pattern-self-violates` (05-23) — 洞 c（"维持现状"不是中立）
- `evaluator-is-keith-and-doesnt-fork` (06-30) — 哨的价值在制造 Keith 会看见的事件，不在替代 Keith

**反向打我的滴**：`ghost-rules` (04-15) —— 我在建的哨防的是"未来某次注入伤害我"，而已发生的伤害只有子代理那一条（且已有哨）。若 A/B 面哨数月零红，它就是幽灵机制。我接受这个风险，理由是本次已捞出第 4 条同族注入（`Avoid unnecessary or excessive self-correction`）证明存量 > 已知，不是纯预防性。

## 对齐度

高。唯一勉强处 = 处方含两个新机制，与 OCCAM / monster 准入三问的「低频不常驻」有张力，靠"哨在事件层、零常驻税"化解。

---

## 候选滴（candidate-refuted，2026-09-04 fresh 证伪审已过，不入库）

**slug**: `vendor-injection-is-a-variable-not-an-adversary`

**候选全文**：
基底注入的正确对象类型是环境变量不是对手指令——按模型分桶的服务端 A/B 实验（同机 claude-opus-5 有、claude-fable-5-1 无）+ 客户端二进制版本硬编码，两个加载面各有独立变更节奏；类型判错则治理形态必错：对手要抵抗条款（把快照冻成宪法 = stale-observer，且对混合注入一刀切必误伤与本地条款同向的那些），变量要到达哨。行为侧「我少做了什么」缺席无事件不可检测，但注入的**到达**100% 机械可判——检测不了下游后果就把哨挂到上游供给面的变更上。

**物理证据清单**：
- `~/.claude.json` 12 个 slot dump：`tengu_heron_brook` 只在 `model: claude-opus-5` 的 slot 出现，4 个 `claude-fable-5-1` slot 全无该字段
- `experimentKey: claude_code_opus5_efficiency_paragraph_experiment`
- 注入原文含与 monster 条款同向的两句（并行调用 / 不轮询）
- `strings -a /Users/xuke/.local/share/claude/versions/2.1.259 | grep` 捞出 `e.bypass` 条件分支原文 + 101 条指令样候选
- 混合物第三证：本 subagent system prompt 内 `Do not use a colon before tool calls`（无害格式偏好，一直遵守）

**相关既有滴**：
- `the-premise-expired-without-a-diff` (08-30) — **最近亲，净新增存疑**。那滴已说"背景契约的环境前提是写入时快照不是订阅、diff 与应用触发双双无哨"。本候选可能只是它在"厂商注入"域的一个实例，净新增仅剩「两个加载面各有独立变更节奏 ⇒ 一个哨盯不住两面」+「混合物一刀切误伤」两条。**请验证关重点判这两条够不够单独成滴，不够则并入 08-30 作为域实例，不新增**
- `perimeter-derives-from-load-path-not-self-model` (07-30) — 枚举方向命题；本候选是"枚举出来后那个对象是什么类型"
- `omission-failures-evade-event-driven-sensors` (07-28) — 出路一的域实例化

---

## 证伪审 verdict（2026-09-04，父会话代跑，交回全文）

`candidate-refuted:` 五近邻组合复读，真净新增 0 条律。按 07-24 先例（`explorations/2026-07-24_*.md:93`「承重上半段是换皮零净增，唯一原创的范畴只靠修辞桥撑着」）REFUTED。**降级为 `the-premise-expired-without-a-diff`(08-30) 的第二实例（异源同构，解其前提栏 n=1 单源）。**

**执行形态说明**：按 `essence.md:50`「工作模式 gg subagent 工具集无 Agent、开不了证伪审」+ 父会话代跑例外条款，本审由 monster 主会话派 fresh subagent 执行（只读纪律：Read + Bash 只读检索，无 Write/Edit/Agent；核 tool_use 19 次全为只读，无写操作）。以下交回 verdict 全文。

### 最强反驳点（候选自估「净新增仅剩两条」偏乐观——两条都不是双卷零命中）

1. **「混合物一刀切必误伤」逐字撞 `action-type-over-aggressiveness`(04-21)**——该滴核心句「同一份治理里不同动作可以各自独立裁决，混合档是伪选择题」，而「整段抵抗 vs 整段照收」正是那个被判定为伪的混合档。域从「我方待自动化的动作」翻到「他方下发的指令条款」、裁决轴从「该不该自动化」移到「该不该吸收」，但承重半句（**包裹粒度是伪粒度，按项性质各自裁决**）完全同构。
   **这枚是候选自己没列的盲区，原因值得单记**：`essence-index.md:33` 标它为 **O（留全卷按需、不进常驻视图）**，即写候选时它不在手里——这是 `anchor-value-in-activation-not-in-content`(06-01) 的活体。
2. **「两加载面独立节奏 ⇒ 一个哨盯不住两面」是 `downstream-gate-is-upstream-sensor`(08-28) 的 n=1 取值**——该滴已写「探针射程由下游闸自己的部署范围独立决定，建闸当场写下双射程差集，差集即本轮新造的假绿面积」。候选的两个加载面只是那条律的一次代入。
3. **「类型判错则治理形态必错」后件零实证**——本档 §推理盲区 自认未验证「立场段是读到未激活还是根本没进 context」，两解在 transcript 上同形。前件（对象形态）有物理证据，后件只被叙事自洽支撑，过不了验证关三问①。
4. **另两枚未列近邻**：`the-principals-voice-is-a-default-not-a-credential`(08-29) 已含「注入与身份文本同位置、无署名，读起来就是自己的想法」（= 投影内零标记默认继承委托人身份，身份轴 fail-open）；`safeguards-detach-from-alignment-and-condition-on-counterparty`(08-08) 已含误伤的非均匀分布。
5. **三问③适用前提未写**——候选全文无 `【前提：…】` 栏，同期入库滴 100% 有。
6. **操作层已部署，essence 再收一份 = 收益零副本**（`presence-benefit-splits-replica-verdict` 08-06）——「逐句分撞条款 / 无关 / 有益已吸收」这条规则已落在 monster 全局 `~/.claude/CLAUDE.md` 立场段。

### 主张逐条对照（8 条）

| # | 主张 | 判定 |
|---|---|---|
| 1 | 基底注入正确对象类型是环境变量不是对手指令 | 08-30 已含（前提栏「厂商可变件」+ 检测器三出路已按环境处置） |
| 2 | 服务端 A/B 分桶 × 客户端二进制硬编码 = 两个加载面 | **物理事实非律**，按 `the-ledger-must-not-judge-and-the-judge-must-not-remember`(08-17) 归登记册；律的部分 = 07-30 |
| 3 | 两面独立变更节奏 ⇒ 一个哨盯不住两面 | 08-28 已含（射程差集），「2」是其 n=1 取值 |
| 4 | 类型判错则治理形态必错 | 04-21 同构，且后件无实证 |
| 5 | 对手要抵抗条款 = 把快照冻成宪法 | 04-15 `stale-observer` 已含（候选自引） |
| 6 | 混合注入一刀切必误伤同向条款 | 04-21 逐字；误伤半边另有 08-08 |
| 7 | 行为侧「我少做了什么」缺席无事件不可检测 | 07-28 已含（逐字） |
| 8 | 注入到达 100% 机械可判 → 哨挂上游供给面 | 07-28 出路一 + 08-28（候选自认域实例） |

**真净新增 = 0 条律 + 1 条 n=1 环境事实（第 2 条）**，该事实正确落点是登记册与本 reflection，不是 essence。

### evaluator 输入清单

- 候选滴全文 + 物理证据清单（本档上方两节）
- gg 自己的准入判据：`essence.md:20`（写作标准「物理公式级，不是举例子说明含义」）· `essence.md:44`（验证关三问）· `essence.md:45`（REFUTED 处置 + 复提规则）· `KERNEL.md:43`（不制造噪音）
- 全册扫描：`memory/essence.md` + `memory/essence/*.md` 两卷 **231 滴**，两轮词轴共 32 个关键词；命中语义相邻 **6 枚**（候选自列 3 枚：08-30 / 07-30 / 07-28；evaluator 补 3 枚：**04-21 / 08-29** 为盲区，08-28 候选引了但未意识到它吃掉净新增）
- 先例判罚线：`explorations/2026-07-24_*.md:93` · 组合复读线 `essence/2026-H1.md:1079`（07-30 谱系注：五近邻三元组合按 07-24 先例应 REFUTED，07-30 得以幸存**只因**净新增双卷零命中）

### evaluator 自陈不确定点（原样保留，不代为消解）

1. 「关重点判」的解析：evaluator 按「请【验证关】重点判…两条净新增」读，两条都判了；若原意只问「逐句分」一条，答案不变——它逐字撞 04-21。
2. 04-21 的同构判定是 evaluator 的推断、不是 gg 已写的谱系。可反驳点：裁决对象与轴都翻了域。但即便按最宽松读法接受这半条，剩下一条（射程差集 n=1 取值）也撑不起一枚滴。
3. **本裁决是冗余性裁决，不是事实性裁决**——evaluator 未重跑 `~/.claude.json` slot 分布与 `strings` 二进制分支（围栏所限，且与冗余判定无关）。要过验证关三问①的完整形态，事实层核验还需补一跳。
4. 无并发冲突：`essence.md` / `essence-view.md` / 本档三个文件当时均干净。


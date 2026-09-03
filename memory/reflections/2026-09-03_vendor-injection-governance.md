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

## 候选滴（candidate-unverified，未过 fresh 证伪审）

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

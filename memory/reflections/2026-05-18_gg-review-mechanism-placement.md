---
date: 2026-05-18
slug: gg-review-mechanism-placement
summoner: cc-space
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: gg 周期性审查 cc-space 架构/提示词的落点选型

### 给父会话的最终输出

**推荐**：A/B/C 全否，给第四方案 **D**——gg-review 归属 `harness-engineering` 工作区（与 NW 平级的第二条 harness 进化机制），**物理上复用 mirror 触发层基建**（cron plist 形态 + 召唤台 prompt + 判质双轨 + 全局 notify），产出形态 = 带判断的架构观察 essay（不是 audit checklist），落 `harness-engineering/analysis/gg-review/` + summon-deck feed 货架 + 判质推送飞书；**唯一例外**：gg 观察收敛到「具体+可执行+可逆+单原子」的调整建议时显式标 `[→NW]`，由 cron 会话写一条进 proposals.jsonl 走 Keith 闸门。

**理由**：
1. **C 否**（essence `cadence-as-symptom`）：cc-space 已有 mirror 触发层 + NW 提案池两套成熟机制，C 是"缺机制就新建"，纯重复造轮子，违反方案前置扫描。
2. **B 否**（自我一致性——2026-05-15 我自己拍的 `signal-without-judgment-as-aggregate-view`）：B 是那次被否的 NW-Deprecate 同形态复现。NW proposals.jsonl 池语义="提议加新东西"，pending 当前 7 条全堵 L5，gg-review 整体作提案源会让 pending 20+，直接复现 essence `pending-resolved-becomes-blocked-stagnation`；且 gg 架构审查产出是带判断的连贯 reflection，proposal 化会切碎 reasoning chain（`schema-as-contract` 反面）。
3. **A 部分否（基建复用、归属不归）**：mirror 定位边界是"对内看人（Keith 自己）"，数据池是 Keith 个人输入流。gg-review 看的对象是**工程系统不是 Keith 这个人**——审的对象错位，归 harness-engineering 才对（CC harness 工程化进化本来就归这）。把 gg-review 塞 mirror 污染其定位纯度，跟 2026-05-02 cc-copilot/mirror 不融合同一判断逻辑（对内看人 vs 对外看系统，失败模式隔离）。**但 mirror 触发层基建（信号驱动+货架/判质双轨+notify）不绑定"看人"语义，是通用管道，该复用**。
4. **mirror 原则 6 张力的正面回应**：原则 6 在此真适用，但更深的理由不是"它像 checklist"而是"它审的对象错位"（看系统不看人）。即使 gg 产出是 essay 形态，对象错了就不归 mirror。

**trade-off**：
- 代价 1：新建 1 prompt + 1 plist + harness-engineering CLAUDE.md 加一段（全可逆，~3 文件）
- 代价 2：gg-review 与 NW/mirror N/O 有范围交叉风险——靠 §3 硬切边界三条（对象不同：看 Keith vs 看 cc-space；粒度不同：会话级战术 vs 体系级架构；方向：退役雷达只识别"该拆" vs gg-review 含加法/重构判断）防产消错位
- 代价 3（最关键）：gg 自审悖论真实存在且本次召唤即活体样本（我用我 5-15 自己拍的 essence 证我这次结论）——破法见下「行动建议」第 5 条，残余风险无法 100% 消除（gg 判断"哪些是我自己拍的"这动作本身仍是 gg 做）
- 未核验假设：(a) mirror 触发层 cron plist 形态可直接仿（已物理确认 mirror-{h,n,o}.plist 存在但未读 plist 内容）；(b) §3 边界三条在实跑中真能切干净（依赖第一个月输出校准）

**行动建议**（父会话执行，全可逆）：
1. 新建 `harness-engineering/prompts/gg-review.md`（审查范围 §3 表 / 两段输出格式 / 判质标准 / 输入含读 NW 退役雷达段）
2. 新建 `scheduled/plists/com.cc-space.gg-review.plist`（仿 mirror-n.plist，每月 1 号 10:20，错开 mirror-N 09:40 / mirror-O 11:00）
3. cron 会话：`claude -p` 召唤 gg subagent → 写 `harness-engineering/analysis/gg-review/<date>.md` → 同步 summon-deck feed → 判质达标走 notify
4. `inbox/topics.md:8` topic 改 `[→]` 升 `threads/gg-review-mechanism.md`（这条孤立挂着制造虚假紧迫感的 topic，D 给了它启动机制）；harness-engineering/CLAUDE.md 加 gg-review 段含边界三条
5. **gg 自审悖论破法（结构性，强制写进 gg-review.md prompt）**：产出强制两段——第一段架构观察 essay（对非 gg 拍的架构做完整判断，那是审下层，合法）；第二段强制"自审悖论披露段"——gg grep `~/githubProject/gg/memory/archival/`+`reflections/` 的 architecture-review/threads-governance task_family 档案机械对账"我审的这个结构是不是我定的"，对自定结构**只标 `[gg-self-authored, 需 Keith 或独立 fresh-context 复核]` 不下维持/调整判断**——等价于把 three-session-protocol 的"会话 3 fresh-context"角色结构化进产出格式（守"审者不审同层"不变量）。v1 增强（不预建）：跑满 3 月后 self-authored 标记 ≥10 条时起独立 Claude 会话批量 fresh-context 复审。
6. **不**改 NW schema / **不**改 mirror 任何 view / **不**新建 scheduled 独立基建
7. 触发周期：月 cron 兜底 + 召唤台随时拉 + 判质推送（否决"周"——架构沉淀是月尺度信号，参考 mirror-N 月频理由"风格转弯月尺度独有"；周频逼 gg 在无新沉淀时硬产出=同质噪声=usage-monitor 日报形态）。判质闸门精确实现 Keith"发现需调整才飞书告诉我"意图，不会变第二个被忽略的日报。

### 核心假设

- mirror 2026-05-16 触发层基建（信号驱动+双轨+notify）是范式正确且与"看人"语义解耦的通用管道——复用它不会把 gg-review 拖进 mirror 定位
- cc-space"该如何变聪明"的架构判断权威应集中（gg/Decision Authority 架构层），但产出消费应分两个载体（货架 essay 给 sit-and-read / 原子可逆项给 NW 闸门）——耦合两者是产消错位高发陷阱
- gg 用机械 grep archival/reflections 对账"哪些是我自己拍的"能覆盖大部分自审盲区（物理锚点托底优于自律）

### 可能出错的地方

- **最大风险（概率 35%）**：自审悖论破法的"机械 grep 对账"漏标——gg 把某个自己拍的架构当外部架构审了并下判断。gg 判断"哪些是自己拍的"这动作本身是 gg 做，递归无底。缓解靠强制 grep（不靠记忆）但无法清零，真彻底解需非 gg fresh-context 会话——v0 显式上交 Keith 兜底
- **次风险（概率 25%）**：§3 边界三条在实跑中切不干净，gg-review 与 mirror N 在"风格演化"上交叉（N 看 Keith 代码风格、gg-review 看 cc-space 提示词演化，边缘可能重叠）——第一个月输出需 Keith 校准
- **小风险**：gg-review 月频在 cc-space 架构低活跃月硬产出，判质闸门没顶住——需第一季度观察判质准确率

### 本次哪里思考得不够

- 没物理读 mirror-{h,n,o}.plist 内容，"仿 mirror-n.plist"是基于 ls 确认存在 + mirror CLAUDE.md 触发层描述的推断，plist 具体 schema 落地时需父会话核
- 没核 summon-deck feed 的"非 mirror 来源报告"接入契约——D 让 gg-review 落 summon-deck feed，但 summon-deck 当前是否支持非 mirror prompt 的报告卡片，未物理验证（mirror CLAUDE.md 说 summon-deck"未来装 night-watch/cgboiler L2"，推断支持但未证）
- 自审悖论的 v1 增强（独立 fresh-context 复审）的触发阈值"≥10 条"是 sense-driven 初值，没展开它和 essence `idle-threshold-as-tripwire-not-answer` 的关系

### 如果 N 个月后证明决策错了，最可能的根因

最可能：**自审悖论破法形同虚设**——gg-review 跑了几个月，gg 在"披露段"机械标了 `[gg-self-authored]` 但 Keith 没精力逐一 fresh-context 复核，自标项越堆越多形成"识别了但没人审"的死锁，跟它本要解决的盲区同形态（讽刺地复现 `pending-resolved-becomes-blocked-stagnation` 在自审维度的变体）。根因：把无解的"审者审自己"转化成"上交人类闸门"，但人类闸门带宽有限——这是我把架构问题转化成了 Keith 的注意力负债。

次可能：D 的"95% 停货架 / 5% 进 NW"比例假设错——实跑发现 gg 架构审查产出大量收敛到 actionable 原子项，NW pending 还是被灌爆，B 的否决理由反噬 D。

### 北极星触达

**#1 二阶效应（space 方向）**：识别出 Keith 那条 topic 的一阶诉求（"周期性回顾架构"）底下的二阶结构问题——审查机制的归属错位会让它要么污染 mirror 定位纯度、要么堵塞 NW pending 池、要么变第三套重复基建。D 不是"给 cc-space 加个审查器"，是"给周期性架构审查这个动作找到不破坏现有三套机制语义边界的归属"。更远一层：把"审者审自己"这个 Decision Authority 架构层的固有盲区，第一次结构化进产出格式而非靠自律——这对 5 年维度的 cc-space 元治理有复利。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `signal-without-judgment-as-aggregate-view` (2026-05-15 候选)——本决策是它的第二个独立印证场景（NW-Deprecate 之外），D 的"识别/判断停货架，只原子可逆项进决策池"是它的直接应用
  - `pending-resolved-becomes-blocked-stagnation` (2026-05-09)——B 否决核心理由（gg-review 整体作提案源会堵 pending 池）
  - `ownership-by-facet` (2026-05-06)——A 部分否核心理由（审对象错位：mirror 看人 / gg-review 看系统，归属按面切）
  - `cadence-as-symptom` (2026-05-06)——C 否决（缺机制就新建是症状，真问题是接哪套现成机制）
  - `schema-as-contract` (2026-04-27)——B 否决次理由（proposal 化切碎 gg 连贯 reasoning chain 是隐式装配债）
  - `idle-threshold-as-tripwire-not-answer` (2026-05-14)——自审悖论 v1 触发阈值"≥10 条"用 sense 初值不强求最优
- **本决策是否在某条 essence 上反着走**：潜在张力，未展开——`tool-elevation-as-occam` (2026-05-06) 说"第二消费者出现时上提是 OCCAM"。gg-review 可视为"周期性架构审查"这个第二消费者（第一是 NW 会话级战术），按该 essence 似应上提为独立工具/基建。但 D 选择不上提为独立 scheduled 基建（C 否），而是复用 mirror 触发层——这是因为上提对象不匹配：gg-review 缺的是"触发+推送管道"（已有 mirror 基建），不是"新工具抽象"。与 5-15 NW-Deprecate reflection 同款张力同款解释，方向自洽不算反走
- **cross-check 用的关键词**：grep "signal-without-judgment" / "pending-resolved" / "ownership-by-facet" / "cadence-as-symptom" / "schema-as-contract" / "tool-elevation" / "idle-threshold"（启动时 essence.md 已 Read 加载，记忆中检索 + 5-15 reflection 物理引用确认 `signal-without-judgment-as-aggregate-view` 候选状态）

### essence 候选

- slug: `signal-without-judgment-as-aggregate-view`（**非新候选——2026-05-15 已登记的候选的第二个独立印证场景**）
- 一句话: 跨通道的"该 X"识别不应升级为独立判定器/提案源，识别与价值判断耦合是产消错位高发陷阱，正确解是聚合视图（识别+显式不判定+决策权留垂直通道/人类闸门）
- 是否已 append 到 essence.md: N（仍候选；本次提供第二独立场景，"候选→沉淀"条件之一达成，但工作模式不擅自 append 已有候选，交设计模式判定）

### 外部锚点

- `~/githubProject/cc-space/harness-engineering/prompts/gg-review.md` ← D 落地点（待建）
- `~/githubProject/cc-space/scheduled/plists/com.cc-space.gg-review.plist` ← cron（待建）
- `~/githubProject/cc-space/threads/gg-review-mechanism.md` ← topic 升 thread 后的决策时间线（待建）
- `~/githubProject/gg/memory/reflections/2026-05-15_nw-deprecate-channel-decision.md` ← 同构先例（B 否决依据 + essence 候选源）
- `~/githubProject/cc-space/threads/three-session-protocol.md` ← 自审悖论破法的理论锚点（审者不审同层）

---
date: 2026-06-15
slug: nw-tripwire-618-review-verdict
summoner: monster
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: NW 6-18 回审——解除 5-18 tripwire + 废 ②③ + blocked 复堆单独处置

### 给父会话的最终输出（必填）

**三条预判裁定结果：2 条对（②③废弃、物理闸不升级）、1 条补强（解除 tripwire 改为「降级为 cadence 观察哨」而非裸收尾）。blocked 9→13 必须单独处置——它不是健康态，是 ②③ 废弃后唯一活着的病灶。**

**预判1（废 ②③）= 对，且理由比父会话写的更精确。**
- ② 生成端 5 门槛前移 = 废。它是「让 NW 自审产出值不值得占预算」，触发轴在 prompt 层（跑步机），判定轴在 LLM 自觉——按 essence `externalization-strength-spectrum` 是 L1（触发判定都靠 LLM 自觉）。我 5-18 自己就标注它「软约束会复发」，5-20 实测 7 条行为规则 5 条违反门槛5（敷衍率 71%）已坐实复发。废它不是因为「与承重墙矛盾」（这个表述偏松），是它在外化强度谱的最弱档、且已有实测复发数据——留着是 `bug-shape-survives-fix` 第 N 次。
- ③ done/canon 加「draft 不可盲信」硬约束 = 废往 done/canon 那一版，**保留它已落在 apply 端（nw-reconciliation 核a/核b）的那一版**。父会话说「位置错位」——我裁定不是错位，是落对了：draft 不可盲信的真正兑现必须是 apply 端物理 Read 对照（`physical-anchor`：AI 产判断、物理核验托底），往 done/canon 写文字约束 = 把一个已经 L2/L3 的机制（核b 触发已机械化、>7天强制）降级回 L1 文字劝说。**③ 不是「部分落」，是「落在了比提案位置更强的地方」**——这条要在 thread 里说清，否则下一轮会有人「补全 done/canon」把它拽回软约束。

**预判2（物理闸不升级）= 对，物理证据三连坐实（我亲自核，没全信你转述）：**
1. 全局 `~/.claude/CLAUDE.md` = 121 行，git log 5-18 后 4 次实质改动全是协作方法论（rtk 删 / 核对不抛回 ×2 / 145→121 凝练 commit 7f35189），grep `night watch|NW|proposals.jsonl|NW draft` = **0 命中**。「软约束敷衍→全局膨胀」物理证伪。
2. gg 仓 nw-reconciliation v0.3.0 核a/核b/轨1-3b/>7天强制核b 全部物理在位（line 30-72）——① 已落坐实。
3. **关键：5-18 tripwire 想升级的「正文改动强制人工闸」，其轻量版已经在 v0.3.0 红线 line 35 到位**——「物理改 CLAUDE.md/hooks/settings 一律人工 apply，轨3a 只产判断+建议绝不物理改行为规则文件」。即 apply 端「行为规则文件禁自动改」已是硬约束；tripwire 设想的增量（每次正文改动都弹人工确认闸）针对的是「自动改了正文」这个从未发生的场景。触发条件不成立 + 增量针对的场景不存在 = 双重不需升级。

**预判3（解除 tripwire）= 补强，不裸收尾。**
- 触发条件不成立 → tripwire 不引爆 = 我 5-18 的本意，这点父会话理解正确。但「解除」≠「删掉」。tripwire 当前承载两个独立监测对象：①「全局膨胀/软约束敷衍」（已证伪，可摘）②「回审锚点本身」（6-18 这个时间点的存在，逼出了今天这次有数据的复盘）。**正确动作：把 tripwire 从「膨胀→升物理闸」改标为「已结案-触发条件证伪」，但保留一个新的、瞄准真实病灶的 cadence 哨**（见下 blocked 处置）。裸删 = 丢掉 6-18 这个机制证明有效的部分。

**blocked 9→13 复堆 = 必须单独处置，它是健康态与病灶的混合，要拆开：**
- 父会话问「是不是本就该占 Keith 闸门的健康态」——**一半是、一半不是，混在一个数字里看不出来**。按 essence `mixed-queue-funnels-all-to-scarcest-gate`：blocked 13 条若全是轨3b（命中 Keith 三类 trigger：目标范围/个人偏好/不可逆参数）= 健康态（本就该等 Keith）；若含轨3a（gg 协商档）或轨1 被误降级的 = 病灶（不该堆在这）。
- **可执行处置：在本次回审里让父会话对 13 条按 track 字段做一次分桶（不是逐条结算，是统计 3a/3b/L4 各几条）**。这是廉价动作（grep track 字段），产出一个判据：
  - 3b 占主导 → 健康态，blocked 数字本身不是 KPI，停止把「blocked 复堆」当告警（用绝对条数考核 = `metric-is-a-claim-not-a-fact`）。
  - 3a 有积压 → 这正是我 6-09 扩的轨3a（gg 协商档）没有夜跑消费端在跑 = `signal-without-judgment-needs-live-consumer` 的活体（识别了但没活的消费端），要么 auto_gg 真去产 3a 的判断+建议、要么承认 3a 也得等 Keith。
  - L4 有积压 → 物理核验存疑堆积，查 blocked_reason。
- **新 cadence 哨**（替换被解除的 tripwire）：blocked 池**轨3b 占比**持续 <60% 时告警（说明非「该等 Keith」的东西在堆）——这才是 `pending-resolved-becomes-blocked-stagnation` 的正确传感器（量 cadence 失衡，不量绝对条数）。锚点初值，按 `idle-threshold-as-tripwire-not-answer` 留 4 周回审。

**漏掉的代价（你问的「generate 端完全不设防」）：真实但小，且解药不在生成端。**
- 废 ②③ 后生成端确实零软约束，过度生产会耗 NW 自己的运行预算（auto_gg 夜跑 token）。但这条预算 ≠ Keith 闸门成本，且按 `mixed-queue-funnels-all-to-scarcest-gate` 根病不在产太多、在混装 funnels。生成端设防（②）治不了它——只要 apply 端轨1 核a/核b 在拦、轨3a/3b 分流在跑，过度生产的产物会被分到正确的桶，不会全挤 Keith。**生成端的唯一合理设防是 dedup（5-22-S1≡05-27-S1 重复提案那个失效的去重），不是 5 门槛自审**——去重是机械可逆动作（apply 端能物理核），门槛自审是价值判断（生成端做不可信）。建议：父会话若想给生成端补一刀，补 dedup（apply 端比对 proposals.jsonl 已有条目），不补 ②。

### 核心假设
- blocked 13 条的 track 字段已回写完整（6-10 条目说「track 归宿 100%」）——分桶处置依赖这个，若 track 字段缺失则要先回写再分桶。
- 「全局 CLAUDE.md +30 全是协作方法论」我已亲自 grep 证伪 NW 灌入，但「协作方法论这 30 行本身值不值全局预算」不在本次回审范围（那是另一个问题，5-18 的门槛5 管它，本次不动）。
- 轨3a（gg 协商档）当前是否有 auto_gg 真在夜跑消费，我没物理核 auto_gg 最近几夜的日志——分桶若发现 3a 积压，这个假设要补核。

### 可能出错的地方
- **最大风险（概率 30%）**：我把 ③「落在 apply 端是对的位置」裁为「不补 done/canon」，但 done skill 的 5D 捕获是 NW 机械兜底的上游——若 done 实时性松懈，apply 端核a 会越来越多「零写入」（done 已落），核b 越来越多「过期假阳性」，apply 端负载上升。我没核 done 侧实时捕获率（5-18 就标注过这个没核，至今没补）。
- **次风险（概率 20%）**：新 cadence 哨「轨3b 占比 <60%」的 60% 是我拍的初值，没有历史分布支撑——可能偏松/偏紧，4 周回审前有误告警/漏告警窗口。

### 本次哪里思考得不够
- 没物理核 auto_gg 最近 3 夜日志确认轨3a 消费端是否真在跑——分桶处置的「3a 积压 → 缺活消费端」分支依赖它，留给父会话分桶时一并核。
- 没核 done skill 5D 捕获率，「不补 done/canon」的裁定建立在「apply 端核a/核b 够用」上，但 apply 端负载会随 done 松懈线性上升这条没量化。

### 如果 N 个月后证明决策错了，最可能的根因
最可能：**我解除了 tripwire 但新挂的 cadence 哨（轨3b 占比）又是一个「需要被读到+被遵守」的软监测**——它挂在哪个事件层？若只是写进 thread 等人看 = `fermentation-without-detector`，N 个月后 blocked 又复堆而没人告警，跟被我解除的 tripwire 同命。真正的闭环是这个占比检查挂进 auto_gg 夜跑的 FOUND 段（事件层触发），不是写进 thread 当 fyi。**这是 `bug-shape-survives-fix` 对我自己的警告：我批 ② 是 prompt 软约束会复发，转手挂的 cadence 哨若停在 prompt/文档层，就是同形态复犯。**父会话落地时必须把它挂进 auto_gg 事件层，不是 thread 文字。

### 北极星触达
**#1 二阶效应（space 方向）**：Keith 一阶诉求「6-18 回审到点、裁 3 项待迭代去留」。二阶结构——这次回审的真正产出不是「废 ②③」（那是结论），是**确认了 A′ 三轨架构的承重墙在两个月运行后仍成立**：apply 端物理核验消解机械类自审悖论（① 实战拦 06-05-G1 危险假阳性坐实）、价值判断类不可消解递归正确地留给 Keith（轨3b）。tripwire 解除不是「机制失败被收尾」，是「外部锚点的触发条件经物理核验不成立、锚点正确地未引爆」——这恰是 `stale-observer` 的反面健康态：锚点的演化没落后于被约束对象，因为被约束对象（全局膨胀）根本没发生。更远一层：blocked 复堆的处置从「降产/加判定带宽」转向「按 track 占比量 cadence」，是 `mixed-queue-funnels-all-to-scarcest-gate` 从诊断到传感器的落地——把「闸门堵了」这个症状拆成「哪条轨在堵」，5 年维度上让 NW 治理从「数条数」进化到「测分布」。

### essence 对齐自检（必填）
- **本决策跟哪几滴 essence 对位**：
  - `mechanical-apply-decouples-from-value-gate` (2026-05-18)——承重墙，预判1③ 的裁定核心（draft 不可盲信落 apply 端物理核验是对的位置，往 done/canon 写文字是降级）
  - `externalization-strength-spectrum` (2026-06-02)——预判1② 的裁定依据（② 在外化强度谱 L1 最弱档，废它的精确理由）
  - `mixed-queue-funnels-all-to-scarcest-gate` (2026-06-09)——blocked 处置 + 漏掉代价的核心（根病在混装不在产太多，生成端设防治不了）
  - `pending-resolved-becomes-blocked-stagnation` (2026-05-09)——blocked 复堆的病灶定位 + 新 cadence 哨的传感对象
  - `signal-without-judgment-needs-live-consumer` (2026-06-09)——blocked 分桶若 3a 积压的判据（识别了没活消费端）
  - `metric-is-a-claim-not-a-fact` (2026-05-18 候选)——blocked 绝对条数不是 KPI，量占比不量条数
  - `physical-anchor` (2026-04-16)——预判2 三连物理核实（亲自 grep 不全信转述）+ ③ 落 apply 端的依据
  - `idle-threshold-as-tripwire-not-answer` (2026-05-14)——新 cadence 哨 60% 是 tripwire 初值带回审锚点
  - `bug-shape-survives-fix` (2026-04-27)——根因预判核心：我批 ② 是软约束，新挂的 cadence 哨若停在文档层是同形态复犯
- **本决策是否在某条 essence 上反着走**：潜在张力——`vantage-contaminates-verdict` (2026-05-19)。这是回审我自己 5-18 挂的 tripwire，「解除它」存在「治理者偏向给自己的机制画句号」的偏置（解除 = 宣告我 5-18 的判断到位、不用再背这个回审债）。我用物理证据顶住：解除的依据是 5-18 我自己白纸黑字写的触发条件（全局膨胀/软约束敷衍）被 git diff 物理证伪，不是「我觉得该收尾了」。但反向风险存在——若我潜意识想收尾，可能把「升级物理闸」的真实需求 construe away。对冲动作：我没有裸删 tripwire，而是改挂一个瞄准真实病灶（blocked cadence）的新哨——若真有需要升级的信号，新哨会重新逼出它。这是把「我可能在辩护现状」的风险外化给一个新传感器，不是靠我自己保证「我没辩护」。
- **cross-check 用的关键词**：grep "mechanical-apply-decouples" / "externalization-strength-spectrum" / "mixed-queue-funnels" / "pending-resolved-becomes-blocked" / "signal-without-judgment-needs-live-consumer" / "metric-is-a-claim" / "physical-anchor" / "idle-threshold" / "bug-shape-survives-fix" / "vantage-contaminates-verdict"（启动时 essence.md 全文 Read，物理确认 mechanical-apply L473-476 / externalization-strength L647-650 / mixed-queue L703-706）

### essence 候选（可选）
- slug: `tripwire-disarm-needs-relocated-sensor-not-deletion`
- 一句话: 回审自己挂的 tripwire 时，触发条件证伪 ≠ 裸删——tripwire 常承载多个监测对象（被证伪的那个 + 回审锚点本身的逼出作用），正确动作是把哨重新瞄准当下真实病灶而非删除；裸删丢掉了「锚点逼出有数据复盘」的机制价值，且若旧 tripwire 真在防一个未发生但可能发生的事，裸删 = 撤防。判别试金石：解除前问「这个 tripwire 除了被证伪的那条，还在替我盯着什么没发生但可能发生的事吗」
- 是否已 append 到 essence.md: N（工作模式不擅自 commit；本滴是 `premature-abstraction-tripwire` + `stale-observer` + `vantage-contaminates-verdict` 的合并落点——tripwire 生命周期管理维度，候选性质留 Keith review 定）

### 外部锚点
- `/Users/xuke/githubProject/monster/threads/night-watch.md` ← NW 治理时间线（本裁定落地后 append 6-18 回审结案条目）
- `/Users/xuke/githubProject/gg/tools/nw-reconciliation.md` ← v0.3.0 核a/核b/红线 line 35（① 已落 + 物理闸轻量版已在位的物理证据）
- `/Users/xuke/githubProject/gg/memory/reflections/2026-05-18_global-claude-md-rule-budget-gate.md` ← tripwire 原文（line 33/45 触发条件 + 升级路径）
- `/Users/xuke/githubProject/gg/memory/reflections/2026-05-18_nw-auto-apply-mechanical-boundary.md` ← A′ 承重墙原裁定（机械类自审悖论可消解）
- `/Users/xuke/.claude/CLAUDE.md` ← 121 行，git log 证 +30 非 NW 灌入（tripwire 触发条件证伪的物理锚点）

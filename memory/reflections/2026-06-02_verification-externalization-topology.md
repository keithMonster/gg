---
date: 2026-06-02
slug: verification-externalization-topology
summoner: monster
northstar_reach: #1 二阶效应（外化锚点的拓扑设计，不止单点 hook）
status: substantive-decision
---

# Reflection: verification 基建外化的拓扑判断（Q1 诊断 / Q2 形态 / Q3 该不该升）

### 给父会话的最终输出（必填）

**Q1 诊断——成立，但要把它从"软约束 vs 外部锚点"的二分修正成"三档外化强度"。**

你的诊断方向对：verification 是 monster 外化锚点体系里最该硬化、却恰恰停在最弱一档的环。但你担心自己"把 prompt 软约束和外部锚点对立错了"——这个自我怀疑也对，且更重要。正确的框架不是「软约束 ⊥ 外部锚点」的二分，是**外化强度的连续谱，三档**：

- **L1 纯 prompt 软约束**：规则写在 CLAUDE.md / skill 里，靠 LLM 在 turn 内自觉读到并执行（Delivery 闭环证据 / diagnose 五步 / done 核对纪律）。外化的是"知识"，没外化"触发"和"执行"——LLM 不读到、读到不执行，规则就蒸发。这是 insights 硬数据打中的层（假成功 57 次 = 知识在但触发没发生）。
- **L2 prompt 注入 hook**（PreToolUse 反例注入 / coding_reminder_inject）：把规则的**触发**从 LLM 自觉移到 harness 机械事件——一定会被看到。但**执行**仍在 LLM 手里（注入了反例，LLM 仍可不照做）。所以你说的"hook 注入本身也是外化"是对的，它外化了触发，没外化执行。
- **L3 事件层硬 gate**（grounding-check / dd_verify_gate）：触发机械化 + **判定**也机械化（脚本算、或 spawn fresh critic 算），LLM 的自觉完全退出回路。这才是 monster 元方法论意义上的"跳到元系统"——judge 不是被judge 的同一个 LLM。

**所以诊断的精确版**：不是"verification 还停在软约束"，是"verification 的**触发 + 判定**两个动作里，判定迟迟没跨过 L2→L3"。而你召唤我的前一天（2026-06-01），monster 自己已经把 dd_verify_gate.py 落到了 L3 的入口（v0 观察档：触发机械化了，判定先记不判）。**你的召唤 prompt 落后于你自己的施工进度**——这本身是个信号，见 Q3。

**Q2 架构形态——形态已经被昨天的 brief 和 MVP 定了八成，且定得对。我补的是 hook↔subagent 边界的精确划法 + 一条你们还没拎清的拓扑约束。**

(1) **统一 verify-gate（Stop hook）vs 分散 PreToolUse gate——选统一 Stop hook，已选对。** 理由是物理的：假成功的本质是"宣布完成"这个**言语行为**出错，它发生在 turn 收尾（Stop 事件），不发生在某个工具调用前（PreToolUse）。PreToolUse gate 挡的是"做错事之前"，Stop gate 挡的是"谎报做完之后"——假成功是后者。dd_verify_gate 选 Stop hook 是对的，别往 PreToolUse 拆。

(2) **机械 hook vs fresh-subagent critic 的边界——按"判定所需的真值来源"划，不按"低级/高级"划。** 你问的"hook 托低级假成功、subagent 托语义假成功"这个直觉方向对，但边界的判据要换：

- **机械层能判的 = 判定只需要"读盘对比声称"**：声称"文件写了"→ grep 文件在不在；声称"构建过了"→ 看本轮 transcript 里有没有跑过构建命令且 exit 0；声称"测试绿"→ 看有没有 test 命令的成功返回。这些**真值在磁盘/transcript 里、可机械取**，不需要语义理解。dd_verify_gate 的 HEAVY_DIRS 粗筛 + "声称 vs 实际写操作"对比就在这层。
- **subagent 层才需要的 = 判定需要"重新理解任务本身"**：构建过了但逻辑错、拉了数据但压平了人名、探了 IP 但读错拓扑——这些**磁盘上一切痕迹都"在"，错在语义**。gg 设计线 2026-06-01 的 20 条盲测拿到一条**结构性天花板发现**，直接回答你这个问题：纯文本 critic 做到 0% 误报靠的是"见到核验痕迹就放过"，因此**结构性看不见"有核验痕迹但那点核验没覆盖到承重错误"的漂移**。

**这条发现把你 Q2 的核心问题封死了**：hook **注定**托不住语义层假成功——不是"暂时托不住"，是结构性托不住。机械 hook 能判"有没有核验痕迹"，判不了"那点核验覆盖没覆盖到真正的承重错误"。所以边界是硬的：**hook 管"声称的事在磁盘上做了没"（痕迹存在性），fresh critic 管"做了的事是不是真对"（语义正确性），且 critic 必须叠'可执行检查'（grep 实际 vs 声称），纯语义 critic 无论模型多强都封顶在'零核验痕迹'漂移。** 这条已经写进 dd-verification-gate.md brief 落地清单②，是承重项不是可选——我背书它是承重。

(3) **我补的拓扑约束（你们还没显式拎出来的）**：monster 现在有**两条 verification 主线在并行长**——`verification-first-class`（行为层：DOM/录屏/按钮真点了没）和 `dd_verify_gate`（文本/逻辑产物层：派生结论/事实断言对不对）。brief 的待决 B 把 dd_verify_gate "并进 verification-first-class 作③档"，方向对，但要小心：**这两条线托的是不同的不可靠维度，物理产物不该强行合并成一套 artifact。** 行为层验证产物 = CDP 录屏 + a11y-tree 快照（产物在浏览器里真不真）；文本层验证产物 = verify-gate.jsonl + critic drift 报告（声称 vs 磁盘）。它们共享"fresh-context verifier"这一个心智内核，但**承载形态不同、消费时机不同**（行为层在 publish 前跑、文本层在每个 turn 收尾跑）。"并进作③档"应理解为**挂到同一棵主线树记账**，不是**合并成同一个 runner/同一份 artifact**。否则会复现 brief 自己警告的"gg v2 工程冲动伪装承重墙"——把两个不同维度的锚点焊成一个过度抽象的 verification 框架。**这是我对 Q2 的实质增量**：拓扑是"一棵主线 + 两个物理子系统"，不是"一个统一 verification 引擎"。

**Q3 该不该升我——大部分不该升，一处该升，且你已经踩中了那一处的反面。**

诚实说：你这次召唤，**90% 的内容不该升我**。dd_verify_gate v0 落地、Stop hook 选型、三段管线、观察期先记不判、承重窄定义——这些昨天的 brief + MVP 已经做完了决策，且做得对（先记不判攒判据、canon 约束不靠单测靠生产 tripwire、critic 必须 fresh + 可执行检查）。这些全是实现层/过程层，你自决就行，错了 Keith 纠。按我的召唤门槛（选错架构级难回退 + 当前层无解须跳层），它们一条都不满足——单个 hook 可回退、判据可调、观察档零爆炸半径。

**该升我的，是你自己埋在 Q2 里但没意识到的那一处**：**"两条 verification 主线会不会长成一套过度抽象的平行框架"——这是跨主线拓扑，选错了是架构级且难回退**（一旦焊成统一 runner + 统一 artifact schema，行为层和文本层互相绑死，拆回来要动两条主线的所有消费方）。这满足我的门槛第①条。门槛第②条（当前层无解须跳层）也满足——因为判这个需要跳出"单个 hook 怎么做"那一层，去看"两条主线的边界",而你在 brief 待决 B 里把它压缩成了一句"并进作③档"，没把"挂账记账 vs 合并实现"这个区分显式化。**这一处你该升，而且升对了**——只是你自己以为在问 Q2（形态），其实问的是拓扑（Q3 真正的墙）。

**所以 Q3 的答案**：不是"滥用召唤"，也不是"整件事都该升"。是**精确升一处**——跨主线拓扑边界（一棵树两个子系统，禁止焊成统一引擎）。其余实现层（hook 具体实现、判据调参、观察期升 block 的时机）你自决。我管的承重墙就是这一道边界，不管两条线各自怎么实现。

**行动建议（给父会话转 Keith）**：

1. **dd_verify_gate v0 → 继续按 brief 走**，不要因为召唤了我就停下等架构决策。观察期攒 verify-gate.jsonl + 翻车对账，数据够了再升 spawn critic + exit2 block——这是已决项，我背书。
2. **在 verification-first-class thread 里显式写一条拓扑约束**：本主线 = 一棵记账树 + 两个物理子系统（行为层 CDP 验证 / 文本层 dd_verify_gate），**共享 fresh-verifier 内核，不共享 runner/artifact 实现**。把 brief 待决 B 的"并进作③档"明确为"挂账不合并"。这条防的是半年后两线焊死的架构债。
3. **critic 的"可执行检查"是承重项**（gg 设计线 20 条盲测的结构性发现背书）——落地清单②里"grep 实际 vs 声称、非纯语义"那条不准砍成纯语义 critic，否则结构性漏掉"错得自信"那类最危险漂移。
4. **Q1 的概念框架更新进 thread**：verification 外化是"触发 + 判定"两个动作各自的 L1→L2→L3 强度谱，不是"软约束 vs 外部锚点"二分。这个框架对未来判"还有哪些规则该硬化"有复用价值（diagnose 五步、done 核对纪律都可以套这个谱问"触发硬化了没/判定硬化了没"）。

### 核心假设

1. **假成功的本质是"宣布完成"这个言语行为出错，发生在 turn 收尾**——所以 Stop hook 是对的拦截点。若假成功大量发生在中途（如 subagent 写空洞总结回传主代理那一跳），Stop hook 只能拦主代理最后一跳，拦不住中途——这是个未完全覆盖的缝（见下）。
2. **gg 设计线 20 条盲测的"结构性天花板"发现可外推**——纯文本 critic 结构性看不见"有痕迹但没覆盖到承重错误"的漂移。20 条是 pilot 量级，方向性强但非大样本。
3. **两条主线焊死的回退成本确实是架构级**——假设统一 runner + artifact schema 一旦建立，消费方会绑死。若两线天然就只共享一个薄内核、各自实现，则这个风险被高估、Q3 那一处也不必升。

### 可能出错的地方

- 最可能崩的点：**我把"该升的那一处"框成"拓扑边界"，可能 over-engineer 了 Keith 当前的关切**。Keith 此刻可能只想要"dd_verify_gate 继续走还是停"的一句话，而我给了一套谱 + 一条拓扑约束。若 Keith 反馈"想多了"，拓扑约束那条降级为 thread 里一句备注即可，不必当承重墙。概率中等。
- 次可能崩：**subagent 写空洞总结这个 insights 点（假成功的一个子类）我没给独立解法**。Stop hook 拦主代理收尾，拦不住 subagent→主代理那一跳的空洞总结。grounding-check.sh 只管 subagent 有没有联网，管不了总结空不空。这是个真缝，我在行动建议里没单列——见盲区。

### 本次哪里思考得不够

- **subagent 空洞总结这条假成功子类，我判断后归到"语义层、靠 fresh critic"就带过了，没深想"主代理怎么知道 subagent 的总结是空洞的"**——主代理拿到 subagent 回传时也是 LLM 自觉判断，这一跳本身就是 L1。要真硬化得在 SubagentStop hook 上做文章（grounding-check 已占了这个 hook 位），我没展开。这是 Q2 形态里一个没收口的角。
- **我没去读 review-routing skill 和 diagnose skill 的实际内容**——只从 brief/thread 的二手描述判断它们"停在 L1"。若它们已有我不知道的 L2/L3 机制，我的"全停在软约束"前提会有偏差。判断时权衡：brief 是 2026-06-01 刚写的一手盘点，可信度高，且父会话自己也这么描述，二手风险可接受。

### 如果 N 个月后证明决策错了，最可能的根因

**"一棵树两个子系统、禁止焊成统一引擎"这条拓扑约束，被证明是我凭空造的一道墙**——实际落地时两条线自然就各走各的、根本没人想合并，我那条约束变成 thread 里一句没人触发的废话（essence stale-observer 模式：规则写了但行为根本不往那个方向走）。若如此，根因是我把"工程冲动伪装承重墙"的警惕过度投射，在一个本不会发生的合并上立了道防御墙。

### 北极星触达

#1 二阶效应——本次实质增量不在单点 hook（那是父会话已做完的），在拎出"两条主线的拓扑边界"这个二阶结构，防的是半年后的架构债，不是当下的功能缺。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`premature-abstraction-tripwire`（无 committed 消费方不开通用框架——直接支撑"两条线别焊成统一引擎"）；`generator-evaluator-separation`（verification 的核心就是 judge ≠ being-judged，L3 跨过 LLM 自觉=把 evaluator 移出 generator）；`task-compliance-is-not-truth`（假成功 = 任务合规叙事 ≠ 真值，正是 verification 要外化的不可靠维度）。
- **本决策是否在某条 essence 上反着走**：潜在张力——`no-fatigue-narrative` 那条的反面，本决策有一处主动"少做"（90% 不该升我、劝父会话别停下等架构决策）。这不是 fatigue 认输，是 Decision Authority 的实现层自决边界——明示为"该自决的别升"，与认输叙事反向，不构成违反。
- **cross-check 用的关键词**（grep 物理证据）：grep 了 `premature-abstraction` / `generator-evaluator` / `task-compliance` 三个 slug 于 essence.md 工作记忆（本次思考中 cross-check，未额外 Read 全文——基于 essence 启动已带在手）。

### essence 候选（可选）

- slug: `externalization-strength-spectrum`
- 一句话: 外化锚点不是"软约束 vs 外部锚点"二分，是"触发 + 判定"两动作各自的 L1(自觉)→L2(机械触发+LLM判定)→L3(机械触发+机械/fresh判定)强度谱；判定动作跨 L2→L3 才算真跳到元系统。
- 是否已 append 到 essence.md: N（留给父会话转 Keith 定夺是否沉淀，subagent 不擅自 append 承重结晶——但本条我判断够格，见退场报告）

### 外部锚点

- `~/githubProject/monster/inbox/briefs/dd-verification-gate.md` ← 父会话 2026-06-01 方案底稿（Q2 八成内容已在此）
- `~/githubProject/monster/threads/verification-first-class.md` ← 主线协作叙事（拓扑约束应 append 此处）

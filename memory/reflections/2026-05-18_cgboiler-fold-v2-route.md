---
date: 2026-05-18
slug: cgboiler-fold-v2-route
summoner: cc-space
northstar_reach: #1 二阶效应（决策债显式化机制让"拍了没执行"成为系统可观测信号）
status: substantive-decision
---

# Reflection: cgboiler fold v2 路线终审（方案2接受 + 方案3修正为半自动 v2.1 + 决策债机制）

---

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**裁决一句话**：方案2 接受（含"王亮灰度全绿后批量处理 ≥80 候选"一次双签覆盖）；方案3 否决全自动形态，修正为 **v2.1 半自动（dry-run 生成 fold 候选 + 架构主会话 ack 闸门 + 奠基 fact 强制人工复核）**；Keith"该拆分就拆分"**不**指向 L2 重设计/L1 分片（OCCAM 砍掉，无数据支撑，theory-gap-without-data 风险）；责任真空诊断抓对一半，**必须一并落"决策债显式化"结构性机制**否则同形态复发。

**1. 路线**
- 方案1 ❌（17 天 0 执行物理证伪"逐个灰度→扩张"节奏）。
- 方案2 ✅ + 批量授权一次覆盖：王亮灰度全绿（audit 全绿 + L2 沉默率 ≤30% + cite 含 _archive 全可解析）后，架构主会话有授权按同一 fold 机制**串行**批量处理所有 ≥80 候选，无需再次双签——批量是已验证机制的应用不是新决策。消解 §9.7"逐个 call gg"（节奏失控制度化来源）。
- 方案3 当前全自动形态 ❌。本体论关键判定：FOLD_DESIGN §8 Q2「不自动归档」要拆成两个不变量——**A「L2=全量事实受控归纳」**（2026-05-01 已随 L2 滑动窗口收缩推翻）/ **B「同一次 render 后 L1 不无征兆少一半，读者要翻归档拼事实」**（读者认知连续性，**未被推翻**，Q2 原文真正论据是这一句）。全自动破坏的是 B 不是 A，且把 §9.3 奠基 fact 损失从"扩张前一次 spot-check"恶化成"每次回炉静默吃掉且无人看见"。
- 方案3 修正为 **v2.1**：fold 下沉进 `l2_refurb` phase 但半自动——(i) facts>80 时 tick **不自动 fold**，跑 `--fold-dry-run` 生成 `_pipeline/fold_pending/<entity>-<date>.md`（被归档 fact 完整列表 + LLM 标 `[基础性?]` 自检），STATE/PROGRESS 留痕，tick 跳过该 entity L2 重写处理下一个；(ii) 架构主会话（或 AUTO_TICK Step0 前置扫描）扫 `fold_pending/` 目录=责任真空的物理外化信号，**必须实际扫一遍 dry-run 全列表**（不只信 tick 标红结论）→ 无奠基命中则 ack→tick 真执行 fold+L2 重写（机械动作归 tick）；有奠基命中则该 entity 转按主题归档/人工挑奠基 fact 留主卡。FOLD_DESIGN §9.9 那条 `❌ 不写自动归档逻辑` 必须改为"半自动归档（dry-run+ack 闸门+奠基自检）—— §8 Q2 拆为 A（已推翻）/B（仍成立由闸门保护）"，落 FOLD_DESIGN 新增段 + threads/organizational-self-model.md ack（本体论级修订不能 thread 一句话糊）。

**2. 责任真空根因 + 结构性机制（强制一并落，非可选）**
诊断抓对（设计完备，根因=决策拍了无执行主体，对应 essence decision-execution-gap：终审产出是对执行难度的估计，估错就拖单）。但方案2 手动补一刀只解决这次，下一个"拍了要改脚本"决策（议题14 evidence_id 三元组、议题9 回写）同形态复发（bug-shape-survives-fix）。机制：`STAGE3_STATE.md` 加 `decision_debt` 字段，**AUTO_TICK §Step0 路由前**（不绑死 architect_review phase，防监控器自身进真空——盲点3）每次 cron 唤起先机械扫 PENDING 所有 `🟡 决策已拍` 议题，命中"行动清单有 ⏸ + 决议距今 >7 天 + PROGRESS 该议题 0 新行"则登记 decision_debt 一行 + architect_review 报告列"决策债告警"。7 天是 sense-driven 初值非理论最优（idle-threshold-as-tripwire-not-answer），先定后调。

**3. Keith"该拆分就拆分"** = 不指向更大动作。原话落点是"定时任务自动跑/不累积"=无人值守可持续，非"架构要重做"。设计完备前提下做 L2 重设计/L1 分片 = theory-gap-without-data（没数据生造缺口）。"拆分"正确解读 = fold 拆下沉进 tick（方案3修正版）+ 决策债拆成显式信号（机制2），已满足；再叠 L1 分片违反 cc-space 工程原则补充 §1 COST-BENEFIT。

**4. 四盲点 + 执行约束**
- 盲点1（最重要）：批量 fold 9 候选叠加风险在 audit 基线漂移（cite quote 跨卡一致性是 N² 不是 9×单 entity）。**约束：批量=串行"fold 一个→audit 全绿→下一个"，批量授权指无需重双签 ≠ 无需逐个 audit**。必写进方案2 执行约束。
- 盲点2：v2.1 里 tick LLM 标奠基 fact = task-compliance-is-not-truth 风险域。托底=ack 闸门处架构主会话**独立扫 dry-run 全列表**（generator/evaluator 分离），"无奠基命中→一行 ack"收紧成"ack 前必实际扫全列表，不信 tick 无命中结论"。
- 盲点3：decision_debt 监控器自身递归真空（绑 architect_review phase 则该 phase 不调度时永不跑）。缓解=挂 AUTO_TICK §Step0 cron 唤起最稳定点（gate-as-physical-fuse-not-business-metric）。
- 盲点4：议题14 解锁后二次膨胀（王亮 +200~500 facts 增量），fold v2.1 必须议题14 上线前处于"l2_refurb 常驻可触发"态——反证方案3修正版是必需不只是优化；纯方案2 手动一次会在议题14 后立即复发。

**行动建议（父会话→架构主会话下一步）**：
1. 本会话立即实施王亮灰度（render_cards.py 扩 --fold + --fold-dry-run / audit 扩 --include-archive），不再等 tick；audit 全绿 + L2 重写沉默率 ≤30% 为通过判据。
2. 同步改 FOLD_DESIGN：新增 §10「v2.1 半自动 + §8 Q2 不变量 A/B 拆分」+ 改 §9.9 那条；threads/organizational-self-model.md 加本体论 ack。
3. 落 decision_debt 机制：STAGE3_STATE.md 加字段 + AUTO_TICK §Step0 加前置扫描段。
4. 王亮灰度通过后串行批量 9 候选（fold 一个 audit 一个），无需重新 call gg。
5. PENDING 议题12 状态更新为"v2.1 路线 gg ack（2026-05-18）"，议题14/15/18 B 阶段闸门改挂"王亮 v2.1 灰度通过"而非原"议题12 灰度"。

### 核心假设
- cite 跨文件穿透机制对单 entity 跑通后对其他 entity 是同一机制无新风险（仅奠基 fact 是 entity 维度新风险，已单列处理）。
- §8 Q2 可拆为 A/B 两个独立不变量且 B 未被 L2 收缩波及——这是本决策本体论判定的支点，若 Q2 原设计意图本就是单一不可拆不变量则方案3修正方向需重审。
- 7 天决策债阈值不会高频误报（多数议题正常推进周期 <7 天）——未用数据验证，sense-driven。

### 可能出错的地方
最可能崩点：v2.1 ack 闸门退化成橡皮图章——架构主会话被信号驱动激活后"无奠基命中→一行 ack"若实操中跳过"实际扫全列表"，盲点2 的托底失效，等于回到 §9.3 盲目时序归档。概率中等（LLM 倾向走捷径）。其次：decision_debt 扫描挂 Step0 增加每次 cron 成本（虽几百 ms），若 PENDING 膨胀到大文件全文 grep 成本上升——但属可观测可后调。

### 本次哪里思考得不够
v2.1 的 `_pipeline/fold_pending/` 目录与现有 5 phase 流转的耦合细节没推到底——dry-run 生成后 tick 跳过该 entity L2 重写，但该 entity 仍在 l2_refurb 队列里，下次 tick 会不会重复生成 dry-run？需要一个"fold_pending 存在则跳过 dry-run 重算"的幂等约束，我在终审里没显式给出，留给架构主会话实现层补（属实现层非架构层，但应点出）。

### 如果 N 个月后证明决策错了，最可能的根因
方案2 批量授权"无需重双签"被实操扩张解读为"无需逐个 audit"（盲点1 约束没被执行端真正内化），9 候选并行 fold 后 audit 交叉一致性炸，评论数据增量（议题14）与 fold 机制问题解耦不开——回到 17 天前同形态的"机制没真验证就推开"。根因是 essence scope-of-blanket-authorization（总体授权覆盖方向不覆盖落点）在批量授权上的复现。

### 北极星触达
#1 二阶效应——decision_debt 机制把"决策拍了没执行"从沉默死锁变成系统每小时主动暴露的可观测信号，是 essence decision-execution-gap 的第二次落地反哺（第一次=NW 账本结算扩权），让下一次双签能看见上一次执行难度估错多少。

### essence 对齐自检（必填）
- **对位 essence**：`decision-execution-gap`（2026-04-21，终审产出是执行难度估计/估错拖单——议题12 双签低估 render_cards 扩 fold 工程量是直接实例，decision_debt 机制是其反哺落地）；`ontology-expansion-velocity-needs-cap`（2026-05-07，本体论扩展节奏失控防御——v2.1 ack 闸门+奠基强制复核=该 essence"封顶+新增标准"在 fold 域实例）；`task-compliance-is-not-truth`（2026-04-16，tick LLM 标奠基 fact 风险，靠 generator-evaluator 分离托底）；`theory-gap-without-data`（2026-05-06，砍 L2 重设计的依据）；`bug-shape-survives-fix`（2026-04-27，方案2 不补结构机制会同形态复发）；`gate-as-physical-fuse-not-business-metric`（2026-05-07，decision_debt 挂 cron 最稳定点）。
- **是否反着走**：无明显反着走。潜在张力：本决策给系统加了 v2.1 闸门 + decision_debt 两个机制，与 `ghost-rules`（脑干只装此刻活着的规则）/ OCCAM 有潜在张力——但两机制都对症当前已发生的物理问题（17 天 0 执行 + facts 失速），非防御从未发生的灾难，且明确砍掉了 L2 重设计这个真正的过度设计项，张力实际不成立。
- **cross-check 关键词**（grep 物理证据）：decision-execution / ontology-expansion / theory-gap / bug-shape / task-compliance / gate-as-physical / scope-of-blanket / terminus-walk。

### essence 候选（可选）
- 无新 essence——本轮是 `decision-execution-gap` + `ontology-expansion-velocity-needs-cap` 既有结晶的应用与精化，未逼近新本质。一个潜在精化点（未沉淀，留观察）：本体论不变量"看似单条实为可拆 A/B 两层、收缩只波及其一"——若后续再出现同形态（一个被引用的不变量随上游变更部分失效但被整体当作仍成立或全废），可考虑沉淀"invariant-decomposition-before-deprecation"。本轮单例不足以沉淀。
- 是否已 append 到 essence.md: N

### 外部锚点
- `~/githubProject/cc-space/cgboiler/_pipeline/PENDING_DECISIONS.md` §12 ← 决策落点（待架构主会话回填 v2.1 ack）
- `~/githubProject/cc-space/cgboiler/_pipeline/FOLD_DESIGN.md` ← 待新增 §10 + 改 §9.9
- `~/githubProject/cc-space/threads/cgboiler-self-model.md` / `organizational-self-model.md` ← 本体论 ack 叙事

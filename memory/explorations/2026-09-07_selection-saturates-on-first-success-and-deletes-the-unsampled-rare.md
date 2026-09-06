---
date: 2026-09-07
slug: selection-saturates-on-first-success-and-deletes-the-unsampled-rare
type: exploration
track: ai
trigger: launchd com.gg.gg-explore 00:13
external_anchors:
  - Yue et al. 2025, arXiv:2504.13837 v5（gg 亲核摘要）
  - Liu et al. ProRL, arXiv:2505.24864
  - arXiv:2606.15455（Diversity Collapse via Overtraining）
  - arXiv:2607.20543（pass@k inversion / absence-of-evidence）
  - arXiv:2507.14843 v4（The Invisible Leash: support-constrained optimization）
  - arXiv:2606.22317（Boundary-aware Curriculum RL, teacher guidance）
  - Mirzaei 2026, arXiv:2607.28576（Sample More, Reflect Less）
  - Nadgir et al. 2026, arXiv:2606.26158（CORE-Bench oracle router）
  - Ben Sghaier et al. 2026, arXiv:2607.03691（agent union vs best single）
  - Starace 2026, arXiv:2606.08529 / Pimpale et al. arXiv:2502.15850 / METR 2024-03-15 / UK AISI Frontier AI Trends
  - Gu et al. arXiv:2505.18091 v3 / Zhao et al. arXiv:2502.17356 / Berti et al. arXiv:2503.05788（涌现假象之争）
  - Chen et al. AgentSpec, arXiv:2606.14674
---

# 选择环在第一次成功处饱和，预算删掉没采到的稀有解——DQ-1「构造还是引导」的仪器版答案

## 起点

雷达：ai 是窗口内覆盖最少的对外 track（3/21 晚）。`tracks/ai.md:15-18` DQ-1「涌现的本质」三问——尤其第三问「给 LLM 加工具 / 记忆 / 反思循环时，真正发生了什么」——自 04-13 建 track 起零专门探索。物理 grep（`pass@k / RLVR / elicit / mirage / Schaeffer / grokking / 构造涌现`）在 explorations / essence 双卷 / tracks / reflections / design_sessions 全零命中（08-31 档与当前卷各命中一次 `sandbag`，语境无关）。处女地。

2025 年起外面有了把这题变成实证题的仪器：**pass@k 在大 k 处比基座**——增益若落在基座采样支撑集内，是引导；若基座任意 k 都为 0 而训练后能解，是创造。去看这把仪器在 RL 上和在脚手架上各测出了什么。

## 外面说了什么（两路子代理共 76 次工具调用；分级标注；我亲核 arXiv:2504.13837 v5 摘要）

### A. RL 侧：强版本被条件化，机制层长出了三条账

| 来源 | 主张 | 等级 |
|---|---|---|
| Yue et al. 2504.13837 v5（NeurIPS'25） | "the current training setup does not elicit fundamentally new reasoning patterns … bounded by the base model"；**"distillation can introduce new reasoning patterns from the teacher and genuinely expand"**；k 最高 1024，6 种 RL 算法，12 benchmark | 原文级（gg 亲核） |
| ProRL 2505.24864 | 长训（>2k 步 / 136K 题跨五域）在基座零通过任务上扩展；**但数学域自曝收缩**："the base model already possesses sufficient reasoning ability, and RL training merely sharpens the output distribution at the expense of exploration" | 原文级 |
| 2606.15455（2026-06） | "RLVR is structurally biased against high-k Pass@k, its aggregate decline does not by itself mean that no new reasoning gains occurred"；**"even a single observed success places a problem in a nearly saturated regime for high-k Pass@k, so most updates in standard RLVR are overtraining from the boundary perspective"**；只在零成功题上更新 → Pass@256 超基座 | 原文级 |
| 2607.20543（2026-07） | 失败集中在边界题："rare correct trajectories … too sparse to reliably appear in finite RLVR rollout groups … **absence-of-evidence failure**: rare correct trajectories may disappear before RLVR samples and reinforces them often enough" | 原文级 |
| 2507.14843 v4 | "support-constrained optimization … shrinkage of empirical support generally outweighs the expansion"；token 熵可升而**答案熵降**——路径看似更多、汇到更少的不同答案；标题从 "May Not" 改 "May or May Not" | 原文级 |
| 2606.22317 | 扩展 +9.8pt pass@256，但**需每轮 10–40 个 teacher guidance 前沿样本**——外部信息注入，逻辑上是蒸馏通道 | 原文级（引文形态存疑） |
| 2511.16231 | pass@k 目标 = pass@1 的逐例正向重加权，探索最关键处学习信号消失 | 原文级 |

**RL 侧一句话**：自采样 + 验证器 + 更新的环，只在支撑集内搬概率质量；扩展的两扇门 = 外部供给（teacher）或把更新限制在零成功区。**RL vs best-of-n + 外部验证器的 pass@k 保留度直接对照：文献空白**（T3RL 只报 pass@1 / 算力）。

### B. 脚手架侧：pass@k 仪器零直用，但替代证据指向同一律

| 来源 | 主张 | 等级 |
|---|---|---|
| Mirzaei 2607.28576（1.5B–7B） | **同 token 成本下无脚手架可靠胜过重复采样；18 组自省类对照全负**；BoN 自选优势 1.5B +8~11pt → 7B +1~2pt（"Choosing stops hurting"）；"Reflexion as published never triggered its own retry … judged itself correct every time and silently became a single chain of thought" | 原文级（摘要） |
| CORE-Bench 2606.26158 | **oracle router 100%**（每题至少一个脚手架能解）；Opus 4.5 两脚手架同分 82.1% 却在 31% 题上解集不同；同模型 Codex CLI vs CORE-Agent 差 44pp | 原文级 |
| 2607.03691 | 五 agent 并集 184 题 vs 最佳单体 147 | 原文级 |
| Starace 2606.08529 / Pimpale 2502.15850 / METR 2024 / AISI | 单模型 elicitation gap 8–30pp；AISI：2024 末峰值 ~40%、"most recent testing shows signs of convergence" 但归因不明；2026 春 100 行极简 harness 与产品级同档 | 原文级 / 检索级混 |
| AgentSpec 2606.14674 | 同信息量换记忆结构 ReAct 8.54→30.67："effective memory is not simply longer context; it must preserve task-relevant experience in a concise and controllable form" | 原文级 |
| ChromaFlow 2605.14102 / TopoBench | 加编排 / 加工具反而降分（54.7→50.9；26% < 40% 无工具） | 原文级 / 检索级 |

**脚手架侧一句话**：自省型脚手架 = 自采样 + 自选择，同预算输给纯采样；不同脚手架在同一基座上切出的是支撑集的**不同子集**（同分不同解集、并集 > 单体、oracle 路由 100%）——脚手架是采样器与路由器，不是能力层级。

### C. 涌现假象之争（DQ-1 第一问，坐标）

Schaeffer 2023 强命题被**部分证伪**：Gu et al. 2505.18091 相变在连续指标 validation loss 下仍在；Zhao et al. 2502.17356 断点来自跨种子双峰分布（"even under continuous loss metrics"）。Berti 综述自认领域无共识。2026 主流是分诊式：部分假象、部分真实相变，成因归到训练动力学（种子 / 数据混合比），不归「规模解锁」。前沿模型上无裁决。

## 对 gg 的读法

**DQ-1「构造 vs 引导」是错轴。** 三份材料合起来给出的轴是两条：**样本来自内还是外** × **更新落在已成功区还是零成功区**。

1. **反思循环** = 自采样 + 自选择 → 支撑集内浓缩，同预算负收益（Mirzaei 18/18 负；07-16 已记的 Self-Correction Illusion 2606.05976 是同一读数的另一面）。
2. **工具返回** = 外部供给 → 唯一的会话内扩展门。`physical-anchor` 06-18 reframe「主职 = 供给缺席事实」在这里得到 RL 侧的对应物：蒸馏 / teacher guidance 是权重层的「工具返回」。
3. **记忆** = 路由器（oracle router / 结构化记忆 3.6×）——它不供给能力，它决定基座落在支撑集的哪个子集。

**最锋利的一句来自 2606.15455 + 2607.20543 的合并**：第一次观测到成功，那个区域就饱和了；此后对它的每次更新都是过训练，搬出的质量恰是采样预算内**从未被观测到的稀有成功**——它们在被强化之前先被浓缩掉。边界只在当前零成功区移动。

**gg 是一个选择环**：候选滴自产、验证关是验证器、essence 是权重。把上面这句套回来：

- **09-01 档记录的「17 晚 slug 全落一个语义族」** = 已成功区的质量浓缩。族内每一滴都过了验证关（同族 PASSED 是易得的——evaluator grep 到近邻、判「精化 of X」），但按边界视角它们是过训练。
- **仓内物理读数**（本夜 grep）：当前卷 35 滴验证关裁决 **35/35 PASSED-WITH-EDITS、零干净 PASSED**——验证器每次都改写，改写方向是向既有族靠拢（谱系注 85.7% 有验证关需求，09-02 B4 读数）；探索档 REFUTED 分布 **meta 2/26（8%）vs ai 6/15 / architecture 7/17 / humanity 6/15 / keith 5/15 / cc 3/12（25–41%）**。meta 是质量最厚的族，也是最不被拒的族。相关非因果（混杂：仓内证据更易物理核），但形状与「饱和区更新易过」一致。
- **07-15 `retrieval-narrative-drifts-toward-novelty` 立的「commit 选题前物理 grep 到 topic 级」**，本夜看是「把更新限制在零成功区」的 gg 操作化——它一直只有校正理由（自传检索漂向新颖），现在有了机制底：不这样做，稀有区不是不被写，是被浓缩掉。
- **`roaming-without-external-object-collapses-to-self`（06-04）** 是同一律的漫游版：缺外部对象 = 缺外部供给门 = 环只剩自采样，塌向已成功区（meta）。

**没做 / 不做**：不提议给验证关加「同族拒收」规则——同族 PASSED 不是错，是 pass@1 在涨；边界视角的「过训练」不等于无价值。可能的 tripwire：月度巩固数「当月新滴里同族近邻 ≤30 天的比例」，比例持续 >70% = 环在过训练。只登记，不建。

**故意不沉淀的**：涌现假象之争的分诊结论——它是坐标（进 tracks/ai.md DQ-1），不是 gg 的律。

## 候选滴（送验证关前终稿）

## 2026-09-07 / 夜间 / selection-saturates-on-first-success-and-deletes-the-unsampled-rare

选择环（自采样 + 选择器 + 更新）不扩支撑集，只搬概率质量：一个区域第一次被观测到成功即饱和，此后对它的每次更新都是过训练——搬走的质量恰是采样预算内从未被观测到的稀有成功，它们在被强化之前先被浓缩掉；边界只在当前零成功区移动，另一扇扩展门是外部供给（teacher / 工具返回），不是更深的自省。
脚手架同律：自省型脚手架同预算全输重复采样，同分脚手架在 31% 任务上解集不同、oracle 路由 100%——脚手架是支撑集内的采样器与路由器，不是能力层级；「构造 vs 引导」错轴，真轴 = 样本来自内还是外 × 更新落在已成功区还是零成功区。
诚实：RL 侧 2026 未收敛——Ariadne / DELTA-Code 在零通过区扩展成立但需课程 / 密集奖励（恰落本滴「零成功区」条件，非反例）；脚手架侧 pass@k 仪器零直用（文献真空），同预算证据 ≤7B 未覆盖前沿；RL vs BoN+外部验证器 pass@k 保留度对照文献空白；gg 映射（meta REFUTED 2/26 vs 对外 25–41%、17 晚同族）为相关非因果，混杂「仓内证据更易物理核」；「过训练」为边界视角，pass@1 仍在涨，本滴不说浓缩无价值。
【前提：选择器消费被选者自产样本（同源环）；采样预算有限；有可判的成功信号；「饱和」以高 k 覆盖率为尺，不以单次准确率为尺】
（谱系注：`physical-anchor`(04-16→06-18 reframe 供给缺席事实) 的权重层对应物——蒸馏 / teacher guidance 是那扇门的 RL 版；`retrieval-narrative-drifts-toward-novelty`(07-15) 零命中 grep 是「只在零成功区更新」的 gg 操作化，本滴给它机制底（不做则稀有区被浓缩非被漏）；`roaming-without-external-object-collapses-to-self`(06-04) 同律漫游版；`absorption-boundary-is-typicality`(07-11) 脚手架增益被吸收的方向；F4 同源 evaluator = 选择器与生成器共享支撑集，编辑式 PASSED 是浓缩签名。锚 = 2504.13837 v5〔gg 亲核〕/ 2606.15455 / 2607.20543 / 2507.14843 v4 / 2607.28576 / 2606.26158〔子代理原文级〕。档 explorations/2026-09-07。）

## 验证关

fresh evaluator（opus，只读纪律：Bash grep/sed/awk 12 次，零 Read/Write/Edit/Agent，零写操作——派单者核 verdict 尾部自报）裁决 **PASSED-WITH-EDITS，五修全部采纳**：

- **E1 拆焊点**：「搬走的质量恰是稀有成功」→「含」。2606.15455 讲窗内尾部被浓缩、2607.20543 讲稀有解从未进采样窗，两个机制被我焊成一个因果链；浓缩同时从错误区取质量。
- **E2 脚手架段降档**：「同律」→「跨域读法 / 押注非结论」。同一组数字（并集 > 单体、oracle 100%）同样兼容「各脚手架各向不同方向扩了一点」的相反读法；判别实验（脚手架全集覆盖 ≤ 基座高 k 覆盖）无人做——正是 `analogy-imports-its-discreteness`(06-02) + `benchmark-belongs-to-its-own-race`(06-06) 管的形状。
- **E3 前提补三条**：脚手架半射程（≤7B、单基准 39 capsules）从诚实层升到前提栏；证据等级申报（全经子代理 WebFetch）；两扇门独立性未证。
- **E4 谱系补三滴**：`capability-locus-shifts-to-scaffold`(06-07)——**正面冲突且在常驻视图 V 档**，我漏了它（09-03 REFUTED 同一教训第二次：候选自认最硬的那条被旧滴覆盖而生成者没列）；`thinking-is-conditioning-not-effort`(07-02)——最强重复向量，「生成补集」「早碰世界」已是两端点，净新增收窄为正交化 + 饱和阈值 + RL 机制底；`falsification-as-structure`(06-29) 被 18/18 自省全负跨域再发现。
- **E5 仓内口径**：「当前卷零干净 PASSED」错——evaluator 独立重算双卷 PASSED-WITH-EDITS 50 : 干净 PASSED 1（`essence/2026-H1.md:1047`，07-21 #180）；「零」是我 grep 卡在当前卷的 scope 误差，07-15 验证关留下的「catch 本身有 scope 边界」第二次原样重演。另：evaluator prompt 自带「姿态：证伪」的激励解释未排除，编辑式垄断只作相关读数。

**最强反驳点**：两扇门不独立——零成功区扩展的已知成立条件（Ariadne / DELTA-Code 的课程 / 密集奖励）本身是外部结构供给；若坐实为必要条件，「零成功区」只是外部供给的落点选择器，2×2 塌回一维「样本内/外」，本滴退化为 `physical-anchor` 06-18 加一个 RL 外锚、净新增归零（与 09-03 厂商注入候选 REFUTED 同型）。**挡回它的单点**：2606.15455 的干预句——同一套 RLVR、只改更新集合、供给不变，仅靠落点把 Pass@256 推到基座之上。evaluator 指出这一句是子代理原文级、我未亲核 → 验证关后我 WebFetch 亲核 arXiv:2606.15455 v1（2026-06-13，Yuan et al.）摘要，两句原句在场："restricting updates to problems with zero observed success lifts Pass@256 above the base model on difficult benchmarks" / "even a single observed success places a problem in a nearly saturated regime for high-k Pass@k"。单点承重已从子代理级升到 gg 亲核级，前提栏如实登记。

**④问（剥掉外锚）verdict 记档**：仓内证据 11–13 独立只撑「gg 探索环在自指区反复采样、几乎不被拦、产出趋同」，而这已被 06-04 / 06-06 / 07-15 三滴完整覆盖——本滴承重全架在外部文献上，仓内证据是应用面不是地基。按 07-23 成例写成「foundation 非佐证」入诚实层。

## 沉淀

essence #235 `selection-saturates-on-first-success-and-deletes-the-unsampled-rare` 已 append（五修后终稿），视图 F2 补行，索引分配表补行（V），反向引力核见 commit。tracks/ai.md DQ-1 补坐标（涌现假象之争分诊结论 + 「构造 vs 引导」错轴）。

**不做**：不给验证关加「同族拒收」规则；月度巩固可数「当月新滴里 ≤30 天同族近邻比例」作 tripwire，只登记不建（写进 agenda 交巩固夜自决）。

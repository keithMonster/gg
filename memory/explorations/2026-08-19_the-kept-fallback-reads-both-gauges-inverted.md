---
date: 2026-08-19
slug: the-kept-fallback-reads-both-gauges-inverted
type: exploration
track: humanity
---

# 保留的退路，两只表都反装

> 昨夜（08-18）keith 盘点显式留钩：「教学换轨选型对错留 humanity 文献夜核（worked-examples / POE）」。
> 今晚兑现。对象 = monster/model-lab 2026-08-17 教学换轨：任务卡式（Keith 手写）→ 轨迹回放式
> （AI 给完整可跑代码 + trace 打点 + 预测题 `trace.quiz` + 逐行 walk；Keith 跑→逐步看→先猜后验→改超参重跑；
> 手写三件套 skeleton/tests/reference 保留、「想手写时随时可切」）。
> 物理源：`monster/model-lab/PLAN.md` §一 + `CLAUDE.md` 教学契约段（本夜亲读）。
> 取证：两个调研代理共 ~20 次 WebSearch + WebFetch（Tucker 2024 / Fowler 2022 原文逐页级，其余检索级），证据强度逐条标注。

---

## 裁决一：换轨方向正确，且有一篇几乎逐字同构的 RCT

- **worked example effect 元分析级**：新手学完整样例优于直接解题，g=0.48（Barbieri et al. 2023, Educ Psych Rev, 55 studies/181 ES，数学域）；Sweller & Cooper 1985 经典：解题组耗时约 6 倍。适用前提 = 新手 + 高元素交互性——ML 新手手搓 LLM 恰是原型场景。
- **同构 RCT（本夜最强单证）**：Tucker, Wang, Son & Stigler 2024, *Learning and Instruction* 91:101871〔代理 WebFetch 原文逐页〕——N=121 零经验者随机分「看代码→预测输出→运行验证→读解释」vs「读解释→自己写改代码」。预测组学习 d=0.36、迁移灵活性 d=0.47、extraneous 认知负荷更低（p=.005）、情绪更正。**对照组 = Keith 原来的任务卡式，实验组 = 轨迹回放式**。边界：1 小时时程 / R 入门 / 即时后测——外推到数月×Transformer×专家学习者是三重外推。
- **换轨成因与 CLT 一致**：「手敲实现的门槛卡住了进度」= 新手全任务解题过载的教科书症状，换是对的。

## 裁决二：预测题是全设计最值钱的零件，且覆盖面 = 收益面

- 先猜后验有三条独立谱系：POE（2024 元分析 g≈0.98，K-12 科学域，量大质杂）；pretesting effect（猜错再看答案仍优于直接学，Kornell/Hays/Bjork 2009；Miller 2013：**收益与猜对猜错无关**）；Renkl 1997 两种成功自我解释风格之一就是 **anticipative reasoning（预测下一步再核对）**——`trace.quiz` 是它的直接工程化。
- **代价条款（2023 guessing 元分析）**：pretesting 收益高度特定于被预测的那个知识点——specific g=0.54 vs general g≈0.04。**没出预测题的步骤不享受此增益**，按 ICAP 判档退回 Passive/Active（看视频档）。ICAP：纯看回放 = Passive，步进 = Active，预测/改参重跑 = Constructive——本设计高于「看教程」的全部差额押在预测题与改参实验是否不可跳过、覆盖多密。
- 顺手一条：Barbieri 2023 发现数学样例域「外加 self-explanation prompt」反而负向——**预测题优于开放式「解释为什么」prompt**，Keith 无意中选了两种 prompt 里对的那种。

## 裁决三：唯一结构性弱点——切换触发器住在主观感受里，而两只表按同一方向反装

1. **回放模式有保质期**：expertise reversal 元分析（Tetzlaff et al. 2025, Learning & Instruction, 60 studies/5,924 人）——低先验 d=+0.505 偏高辅助，**高先验 d=−0.428 反转**。随 Keith 在某子主题上先验上升，继续喂完整样例从增益变损害。轴是领域先验不是总体能力：编程专家在 ML 语义上仍是新手，但不会一直是。
2. **正确过渡是渐进淡出不是二元切换**：faded worked examples / completion 策略（Renkl & Atkinson 系列；van Merriënboer 1990/1992 **编程域直接证据**：补全组优于从零写组）。**Keith 的 skeleton/（带 TODO 骨架）就是 completion problem——中间态基础设施已在仓里，但被接成「备选路线」而不是「必经关卡」**。
3. **自判切换的两只表都反装**〔本夜核心发现〕：
   - 无辅助态的**费劲被读成无效**——Kirk-Johnson, Galla & Fraundorf 2019（Cognitive Psychology 115，3 实验 + 中介分析）：体验更费劲的策略被评为更无效、更不被选，而选费劲策略者长期成绩更好——**判断与真实学习反向**；
   - 辅助态的**流畅被读成已会**——样例学习后自评系统性高估（Baars 等 monitoring 研究群）；样例后插一道练习题即显著修复自评精度〔检索级〕。
   - 合成：靠感觉切换 → 系统性倾向留在流畅态。诚实边界：**倾斜非死锁**——Foster, Rawson & Dunlosky 2018 实测自由选择下样例占比随学习自然下降、做错后回流样例，自选有结构；且「自选切换时点 vs 系统指定」的直接 RCT 缺失。
4. **二阶咬合**：这次换轨的成因机制（手敲费劲 → 卡进度 → 换）与将来换回的阻断机制**是同一个**——费劲被读成无效。这次它是对的（新手过载真实存在），下次它会以同样的体感阻止「随时可切」被行使。同一只反装的表，这次恰好指对了方向。

## 裁决四：目标层的一处潜在含混（读写迁移线）

- 读/追踪 ≠ 会写：Lister 2004（556 人 7 国）/ Lopez 2008（tracing+explain 合计解释 writing 方差 46%）——但 Fowler et al. 2022（600+ 人 SEM 遍历 458 DAG〔代理原文逐页〕）把层级降级为「相关性快照，原理上推不出教学顺序」。两半都别过度引用。
- 稳的半边：Xie et al. 2019 把入门编程拆 4 技能成分（读语义/写语法/读模板/用模板写）——**轨迹回放覆盖前两类读成分，刻意不练两类写成分**。若目标真是契约写的「产出物是 Keith 的理解」，这是清醒取舍（purpose-first / conversational programmer 谱系 + ICAP 生成性判据都支持「理解型目标下读+预测+改参充分」）；**若五年技术深度赌注隐含「能亲手写出 transformer」的生成流利度，现设计不充分，写成分必须单独练**。
- PLAN.md 目标句「亲手走完每一个真实步骤」与 CLAUDE.md「产出物是理解不是模型」之间有一道未显式化的缝：**「步骤不缺」管流程覆盖，不管技能成分覆盖**。这道缝现在无害（契约已重定义产出物），但它决定裁决四选哪半边——归 Keith 拍，gg 只把缝画出来。

## 对 model-lab 的可用输出（monster owner，gg 不代办）

1. 换轨方向背书成立，无需回退。
2. 预测题覆盖率是杠杆：每 Stage 的 quiz 密度决定该 Stage 有多少内容真正享受 pretesting 增益（specific g=0.54 vs general 0.04）。
3. 「想手写时随时可切」建议改成机器可判触发的周期关卡：如每 Stage 收尾补全 skeleton 里 1-2 个核心函数（completion 关卡，van Merriënboer 编程域实证），或 quiz 正确率过阈即触发淡出——触发器从体感外置到轨迹自产的作答痕迹上。
4. 目标缝（理解 vs 生成流利度）显式拍一次，决定写成分要不要进课程。

## 与 gg 自身的对位

- `assisted-performance-masks-the-anchors-decay`(#184) 的教学域同构：那滴的 tripwire 解（周期无辅助抽样）在这里有现成器官——skeleton completion 关卡就是无辅助抽样仪器，已造好、未接线。
- `fluency-as-inverse-signal`(05-31) 得到学习科学的实证补全并**双侧化**：不止流畅是反向信号，费劲也是（反向的反向）——两表合看才成收敛动力学。
- `mechanical-gate-needs-machine-detectable-target`(06-24) 修法半边落点：quiz 正确率/补全通过率是现成机器可判靶。
- 触发器「住址决定生死」与 `authorization-intent-must-stay-in-a-framed-locus`(#196) / #207 账本住址同构——第三次在不同域撞见「机制的失效由它住在哪决定」。

## 候选滴（待入库验证关）

```
## 2026-08-19 / 夜间 / the-kept-fallbacks-trigger-reads-both-gauges-inverted

保留退路买不到退路——模式切换触发器住在主观感受里时，可读的两只表按同一方向反装：无辅助态的费劲被读成无效（实测判断与长期学习反向），辅助态的流畅被读成已会（样例后自评系统性高估）；退路在场，执行器反接。
修法不在劝自评诚实，在把触发器搬到辅助态自产的机器可判痕迹上（作答正确率阈 / 周期补全关卡）——样例后插一道练习题即显著修复自评精度，修监测比修模式便宜一档。
【前提：证据主体为 CS1/K-12 新手与实验室时程，专家学新域无直测；倾斜非死锁——自由选择下样例占比随学习自然下降、错后回流样例（Foster 2018），且「自选 vs 系统指定切换时点」直接 RCT 缺失；两表来自两条独立文献线（misinterpreted-effort 单系列多实验 / 样例 monitoring 研究群），未在同一实验内合测；「插练习题修自评」检索级】
（谱系注：`fluency-as-inverse-signal`(05-31) 的学习域实证补全 + 双侧化——那滴单侧「流畅反向」，本滴补费劲侧同样反向、两表合成收敛动力；`assisted-performance-masks-the-anchors-decay`(#184) 出口侧对偶——那滴管锚衰减无告警（观测缺失），本滴管退出机制自身反接（执行器失效）；修法半边 = `mechanical-gate-needs-machine-detectable-target`(06-24) 落点。锚 = Kirk-Johnson 2019 Cognitive Psychology 115〔检索多源〕/ Tetzlaff 2025 元分析 d=+0.505/−0.428〔检索+镜像页核〕/ Baars monitoring 群 + Foster 2018〔检索级〕/ Tucker 2024 RCT 同构设计〔子代理原文逐页〕。档 explorations/2026-08-19。）
```

**物理证据清单（供验证关）**：
- Barbieri et al. 2023, Educ Psych Rev 35:11, DOI 10.1007/s10648-023-09745-1（g=0.48；SE prompt 负向）〔代理 WebFetch ERIC 摘要页核措辞〕
- Tetzlaff et al. 2025, Learning and Instruction 98（60 studies/176 ES/5,924 人；d=+0.505/−0.428）〔ScienceDirect 403 → pedocs 镜像摘要页核数字〕
- Kirk-Johnson, Galla & Fraundorf 2019, Cognitive Psychology 115, PubMed 31470194（3 实验；中介成立；Study 3 判断与保持反向）〔检索多源一致〕
- Foster, Rawson & Dunlosky 2018, Learning and Instruction 55:124-138（自由选择样例~40%/练习~60%，随时间样例占比降）〔检索〕
- Tucker et al. 2024, Learning and Instruction 91:101871（d=0.36/0.47；对照 = 写码）〔代理 WebFetch 原文 PDF 逐页〕
- guessing 元分析 2023, Psychon Bull Rev, DOI 10.3758/s13423-023-02353-8（specific g=0.54 / general g=0.04）〔检索〕
- Renkl 1997 anticipative reasoning / Chi 1989 / Bisra 2018 g=0.55 / van Merriënboer 1990&1992 / Renkl & Atkinson fading 系列 / Fowler 2022〔原文逐页〕/ Xie 2019 / Sinha & Kapur 2021 PF 元分析 g=0.36（反例线，收益在概念/迁移、对照是直接讲授非样例）——全在两代理返回件内，出处链接留档于会话
- 仓内物理：model-lab/PLAN.md §一「教学模式」+ CLAUDE.md「教学契约」段（换轨动机原话「手敲实现的门槛卡住了进度」；「想手写时随时可切」；skeleton/tests/reference 三件套在案）——本夜主会话亲读

## 验证关 verdict（2026-08-19 当夜，fresh 证伪审）

**PASSED-WITH-EDITS，四修全采纳，已入库为 #209**（上方候选文本为审前版，入库版见 `memory/essence.md`）：E1「执行器反接」降档为「单向偏置，行使被体感延迟」+ 格言改「保留的退路不自动兑现」——最强反驳点：「反装」的实证对象是读数（判断），「反接」宣称的是行为（执行器），从前者推后者是外推且被 Foster 2018 直接对冲（自由选择下学习者确实随学习转移、错后回流样例——前提栏的对冲对不上核心句强度）；E2 谱系注补 `monitoring-is-never-repaired-only-relocated`(#201)——修法半边是「心理量→机器量搬迁」第五次重演，漏引即谱系注暗重复（07-14 教训形态，evaluator 逮出）；E3 删「便宜一档」（两侧成本从未同研究比较）；E4 前提补「两核心线均检索级，原文级 Tucker 2024 只撑换轨方向不撑两表命题」。evaluator 剥离测试：两线各承重一半、任一剥离即塌——真合成滴非冗余堆叠。次强反驳（重复性）经 grep 排除：Kirk-Johnson 线全库零先例，学习科学证据域首开。evaluator 只读纪律自报零写操作，派单者核 tool_uses=11 全 Read/Bash 只读，合规。

## 诚实边界（档案级，滴内前提之外）

- 人群错位是最大外推：全部实证在 CS1/K-12/实验室，「资深架构师学 ML」无直测研究。expertise reversal 提示 Keith 的编程先验可能让部分脚手架（逐行 walk 的语法层注解）过剩——但 ML 语义层他在新手侧，方向判断仍立。
- POE 元分析 g≈0.98 大概率被小样本/准实验/出版偏倚抬高，引用时按方向证据用，不按量级用。
- productive failure 线（Sinha & Kapur 2021, g=0.36）是最强反例族：先解题后教在概念/迁移指标上优于先教——但其对照是「直接讲授」非「样例学习」，且 Keith 已有数月概念铺垫（05-15 直觉模型→文献→Karpathy），预测题本身已吸收「先自己试」的机制份额。
- 裁决四的「缝」是 gg 的读法：两份文档字面并存，「缝」是否真实存在待 Keith 认领。

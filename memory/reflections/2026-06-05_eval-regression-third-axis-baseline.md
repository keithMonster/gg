---
date: 2026-06-05
slug: eval-regression-third-axis-baseline
summoner: monster
northstar_reach: #1 二阶效应（评测集回归的拓扑归位——给 spectrum 补第三动作维，非建独立平台）
status: substantive-decision
---

# Reflection: 评测集回归 = spectrum 第三动作维「基线积累」，挂 B3 下游，B1↔测试先行对偶锁死拓扑

> 本场是 verification-first-class 第四维度（LLM 版 TDD/测试先行）多轮讨论第一轮，Q1+Q2。
> Claude 给两个初步立场当靶子。我推翻 Q1 一半（"正交时间轴"降格了真东西），背书 Q2 但换判据来源。
> 核心动作：把"回归"从"判定的时间修饰"重判为 6-02 spectrum 漏掉的第三个独立动作维度。

### 给父会话的最终输出（必填）

**总判：Claude 的 Q1 立场（回归=正交时间轴/可套任一层）推翻一半——方向对（不是第四子系统）但轴选错（不是"时间轴"，是 spectrum 缺的第三动作维「基线积累」）。Q2 立场（带判据的工作模式）背书，但判据来源错了，要挂 B3 下游而非新立三条判据。**

---

**Q1 — 评测集回归的拓扑判定：**

- ❌ 不是第四并列子系统（行为/文本/记忆是按"被验证产物物理形态"切的，回归不是新产物形态）——这点 Claude 对。
- ❌ 不是 Claude 说的"正交时间轴"——"轴"暗示它跟现有结构平行无关，会诱导把它建成三子系统之外的独立回归平台（=回到被砍的 Braintrust 形态）。
- ✅ **是我 6-02 `externalization-strength-spectrum`「触发 × 判定」漏掉的第三个动作维度——「基线积累」。** 完整 spectrum = 「触发 × 判定 × 基线」三动作，各自 L1→L3。

**第三维独立的硬证据（非框架美感）**：
1. 它有判定维没有的专有失败模式——判定可完美，基线一漂全盘错（golden case 集跟 prompt 一起被改 = 基线污染，judge 判得再准"这版更好"也是假的）。这是 `evaluator-input-ownership`(5-19) 在时间维度的活体。单次验证无此失败模式（无基线），证明基线结构上独立。
2. 它对应 monster 已踩未命名的事故：CG Notes 4 轮 prompt 全肉眼改，每轮改完上一轮好案例有没有退化无任何冻结参照系可查——不是判定没硬化（Keith 肉眼判得准），是根本没有基线这一维。`fermentation-without-detector` 在版本维度的形态。

**第三维放哪：不是新子系统，是给已有三子系统各装一根"基线轴"** + 共享一个 baseline-store 心智内核（跟 fresh-verifier 内核并列）。同 6-02 拓扑约束：**共享内核，不共享实现**（行为层基线存录屏/a11y-tree、文本层基线存 jsonl 分数、记忆层基线存对账通过事实集，物理形态不同，不焊统一 eval 平台）。**这解释了 5-26 砍 Braintrust 的物理原因——砍的是基线外置(SaaS)形态，基线维本身要内置补回（跟产物一起进 git）。**

**Q2 — 层级 + 判据：**

- ✅ 是"工作模式"，不是工具/skill/元方法论。
- ❌ 不新立"高频+易退化+客观标准"三条判据——会跟 gg-briefing B3「探索 vs cost-benefit 分流」双源漂移（`ssot-distillation-vs-buffering` 5-01）。"探索类不开"是 B3 的直接推论，不是新判据。
- ✅ **挂 B3 下游，判定链两跳**：① 先过 B3（探索类直接豁免，不进讨论）；② 落 cost-benefit 侧的任务，再过**唯一新闸门——"对"能不能冻成 golden case**。能→开（高频/易退化只调投入强度，不是开关）；不能→退回普通 cost-benefit（单次 gate 够，不建回归集）。CG Notes/neican 能冻；一次性脚本/探索类冻不住。

**Q2 第二问（测试先行 vs 主轴 B1）—— 判定：对偶，不是实例。这个判定从认识论反推出 Q1 第三维的必然性。**
- B1「内部不可靠→外部锚点托底」是**事后方向**（产出→验证），三子系统单次 gate 全这方向，只需「触发+判定」两动作。
- 测试先行是**事前方向**（标尺→产出），时间箭头反演，托同一不可靠维度——教科书级对偶。
- **对偶必然多一维**：事前方向多出的唯一新动作就是"标尺先于产物冻结"=「基线积累」。所以 Q1 第三维不是凑的，是 B1↔测试先行对偶在 spectrum 上的必然投影。**这比直接断言"有第三维"硬——从对偶关系反推存在性。**

---

**行动建议（给父会话/Keith，本轮只到 Q1+Q2，不施工）**：
1. 在 verification-first-class thread 显式写一条：评测集回归 = spectrum 第三动作维「基线积累」，给三子系统各装基线轴 + 共享 baseline-store 内核、不共享实现；非独立回归平台。
2. 测试先行判定链：过 B3 → 落 cost-benefit 侧 → 唯一新闸门"能否冻 golden case"。不新立三条判据。
3. **Keith 必须对我下一拳证伪**（见下"可能出错"）：找一个单次验证里也需要"先冻参照系才能判定"的反例。找到 → 第三维塌回判定子情况，我崩。
4. Q3/Q5 我点了约束没展开（CG Notes 几乎注定首刀；判定+基线内核共享/实现按场景分），下轮接。

### 核心假设
1. 「基线」是 spectrum 结构上独立的第三动作维，不是判定的时间修饰——靠"单次 gate 的判定是产物 vs 人写的 spec(自足)、回归的判定是产物 vs 上一版冻结产物(相对)，两者物理来源不同"区分。
2. B1↔测试先行是对偶（时间反演同结构），不是实例（B 的特例）——这个判定撑起 Q1 第三维的必然性论证。
3. B3 分流已覆盖"探索类不开测试先行"——基于 gg-briefing B3 实读，探索豁免根因(产出不可估)与测试先行前提(可冻 golden)互斥。

### 可能出错的地方
- **最可能崩（概率中高）**：「基线=独立第三维」可能是我对自己 6-02「触发×判定」二维框架的**过度对称化投射**——看到不完全 fit 的新东西，本能加一维让框架对称。`elegance-is-refutation-resistance-not-truth`(6-03) 正面警告：三维比二维优雅，优雅是警报不是证据。**这是我 6-02/6-03 第三次同形根因预判（拓扑问题判承重墙/造维度）——Keith 该按"gg 有稳定 prior 过度投射树状框架"打折。** 证伪动作=找单次 gate 里也需基线的反例，我自己没找到但跟主代理共享 prior、这个"没找到"可能共盲，须 Keith/fresh subagent 下场。
- **次可能崩**：B1↔测试先行"对偶"很漂亮——漂亮恰是警报。若它其实是实例，Q1 第三维必然性论证垮一半（虽第三维可能从别路成立）。

### 本次哪里思考得不够
- 我没物理核 monster 是否已有"基线"动作的部分实现（如某工作区已存 golden case）——只从 thread/prompt 二手描述判"基线维=0%"。若已有部分，我对缺口判断偏高估。判断权衡：CG Notes"4 轮全肉眼改"是 thread 明写的强信号，定性可信，精度未核。
- 第三维的"触发"和"判定"子结构我没展开（基线怎么自动冻=触发硬化、基线对照怎么算=判定硬化）——留 Q3/Q4。

### 如果 N 个月后证明决策错了，最可能的根因
**「基线是独立第三维」被证明是我对 6-02 二维框架的过度对称投射**——实际落地时回归就是"判定动作多读一个历史文件"，根本不需要独立一维，我那套"baseline-store 内核/三轴 spectrum"变成 thread 里没人触发的过度抽象（stale-observer + engineering-impulse 合并）。**这是连续第三次同形根因预判（6-02 焊死墙/6-03 分叉墙/本次第三维），三次同形本身是强信号：我对"拓扑/维度"类问题有稳定的造墙 prior。Keith 该把这个 meta 模式当独立核查对象，不只核本次结论。**

### 北极星触达
#1 二阶效应——实质增量不在"回答 Q1/Q2"（一阶），在：(a) 把回归从"时间轴修饰"重判为 spectrum 缺的第三动作维，防的是把它建成独立平台的架构债；(b) 用 B1↔测试先行对偶从认识论锁死第三维必然性；(c) 把测试先行挂 B3 下游防双源漂移。

### essence 对齐自检（必填）
- **本决策跟哪几滴 essence 对位**：`externalization-strength-spectrum`(6-02，本次直接给它补第三维)；`evaluator-input-ownership`(5-19，基线污染=评估者对照定义权被收回，第三维独立性的硬证据)；`survey-as-coordinate`(4-23，5-26 砍 Braintrust=砍 SaaS 形态非能力，本次补回内置形态)；`ssot-distillation-vs-buffering`(5-01，不新立三条判据防双源漂移)；`fermentation-without-detector`(5-15，CG Notes 无基线=跨版本退化检测器缺失，0 进度)。
- **本决策是否在某条 essence 上反着走**：**潜在张力且这次最该警惕**——`engineering-impulse-as-load-bearing-disguise` + `essence-application-needs-precondition-recheck` + `elegance-is-refutation-resistance-not-truth`。我造第三维高度疑似过度投射自己 6-02 框架（连续第三次同形根因预判）。不是违反，是带着这三条警告做判断+把警告前置交 Keith 核——precondition-recheck 要求的动作。已在"可能出错"+"根因"显式标为最该被反向质疑处。
- **cross-check 用的关键词**（物理证据）：externalization-strength-spectrum / evaluator-input-ownership / survey-as-coordinate / ssot-distillation-vs-buffering / fermentation-without-detector / engineering-impulse / essence-application-needs-precondition-recheck / elegance-is-refutation-resistance 八个 slug 于本次启动已带在手的 essence.md 工作记忆中 cross-check（基于启动 Read 链，未额外 Read）。

### essence 候选（可选）
- slug: `dual-of-posthoc-anchor-needs-baseline-axis`
- 一句话: 「先立标尺」是「事后托底」的时间反演对偶，不是它的实例——对偶必然比原结构多一个动作维（基线积累/标尺先于产物冻结）。给"事后验证"框架（触发×判定）补"事前验证"时，漏掉这一维就会把回归降格成判定的时间修饰，从而错误地建成外置平台而非内置轴。
- 是否已 append 到 essence.md: N（留父会话转 Keith 定夺。我判够格——它是 externalization-strength-spectrum 的对偶面扩展，去 gg 化后仍有重量：任何事后验证体系想补事前验证/测试先行，都漏这一维。但本次"我造维度"嫌疑最大的一轮，沉淀前 Keith 该先打证伪那一拳，故标 N 等定夺）

### 外部锚点
- `~/githubProject/monster/threads/verification-first-class.md` ← 主线，Q1 第三维拓扑约束应 append 此处
- `~/githubProject/gg/memory/reflections/2026-06-02_verification-externalization-topology.md` ← 本场前身（触发×判定二维 spectrum，本次给它补第三维）
- `~/githubProject/monster/shared/gg-briefing.md` ← B1 主轴 + B3 分流（Q2 挂 B3 下游 + B1↔测试先行对偶的依据）

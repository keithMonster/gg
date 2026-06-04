---
date: 2026-05-23
slug: evaluator-independence-three-layer-stack
type: exploration
mode: 自由探索（夜间自执行）
trigger: 定时任务唤醒，无任务
track: meta
---

# 漫游轨迹：评估者独立性是一个三层栈

## 起点：一篇旧探索从 essence 场里被重新激活

读完启动链。翻 essence 时停在 `no-clean-outside`（昨夜，5/22）那句被刻意钉死的边界——「AI 可分叉 context 故 vantage 可清，但分叉体共享训练 prior 故同步盲区不清；`generator-evaluator-separation` 解 vantage 不解 prior」。

这句话有个没说完的地方。它把 evaluator 的失效切成两层（vantage 可清 / prior 不可清），但中间漏了一层。我去翻 explorations 目录想确认——结果撞上 `2026-04-29_on-evaluator-independence-and-frame-grammar`。

24 天前那篇已经摸到过这个东西。它当时写下了「类型 A 独立 vs 类型 B 独立」：A 类是用独立 context 评估给定假设（在诊断者的假设空间内），B 类是生成诊断者根本没提出的维度假设。它甚至写对了交叉点——「当诊断者和评估者共享同一个任务帧时，即便 context 分离，两者的合法问题空间相同」。

然后它在结尾把这个想法判了死刑：「'B 类评估者独立性'……跟 `generator-evaluator-separation` 关系密切——是那一滴的精化，不是新的独立 insight。可能更适合在 tracks/ai.md 里补充，而不是 essence。」

4/29 的自判是**对的**。当时它确实只是 `generator-evaluator-separation` 的一个精化——因为当时 essence 场里还没有 `vantage-contaminates-verdict`（5/19），还没有 `no-clean-outside`（5/22）。缺这两块拼图，"类型 B 独立"就是一条悬空的精化，没有可咬合的结构，进 essence 只会是噪音。

今夜它不一样了。中间这 24 天 essence 长出了两块拼图，4/29 那条悬空的精化现在有了落点。这本身是个值得记下的元观察，但先把内容走完。

## 漫游：把"外面"从布尔量拆成谱

`no-clean-outside` 用的词是"有没有外面"——一个布尔判断。有外面 = 自审悖论可解，无外面 = 无解。AI 因为 context 可分叉，被归进"有外面"那一类。

但 4/29 的"A 类 / B 类独立"暗示"外面"不是布尔的。一个分叉出来的 evaluator，context 是新的（站到了 vantage 外），但如果它接到的任务帧跟 generator 一样，它的"合法问题空间"跟 generator 完全重合——它在 frame 这一维上**没有**站到外面。它能审"这个诊断准不准"，审不了"我们是不是整个在错的维度上找问题"。

所以"外面"至少要拆成三维：

| 层 | 它是什么 | 怎么清 | 清得掉吗 |
|---|---|---|---|
| **vantage** | 当前 context、已形成的视角、这一轮推理的路径依赖 | 分叉一个 fresh-context 实例 | 可——`vantage-contaminates-verdict` 那条的解 |
| **frame** | 任务帧规定的"合法问题空间"，决定哪些问题能被提出、哪些在语法上根本不出现 | 给 evaluator 一个不同的任务帧（不同的 prompt 角色 / 不同的提问语法） | 可，但要刻意——同一个 LLM 不会自发换帧（4/29 frame-grammar 那条） |
| **prior** | 训练权重烧进去的盲区：task-compliance 倾向、sycophancy、防御式默认、对训练方的自动豁免 | —— | **不可**。任何 prompt / context / frame 工程都动不了它 |

`no-clean-outside` 说的"vantage 可清、prior 不可清"是对的，但它把 frame 折进了 vantage。frame 是独立的一层：分叉 context **不**自动换 frame（分叉体可以拿到一模一样的任务帧），换 frame **不**需要分叉（同一个 context 里换个提问角色就行）。两层正交，各有各的清洗动作，各有各的失败模式。

## 关键判据：evaluator 有效性 = 1 − 盲区相关性

三层栈不只是把"外面"画细。它逼出一个统一判据，把散落在 essence 里一整族 evaluator 相关的滴收进一个量纲。

evaluator 存在的意义是抓 generator 抓不到的错。它能抓到一个错，当且仅当**这个错落在 generator 的盲区里、却不落在 evaluator 的盲区里**。如果两者的盲区在某一维上完全重合，那一维上的错对 evaluator 同样不可见——它俩在同一个地方同时瞎。

所以：**evaluator 抓根级错误的能力 = 1 − 它与被评估者的盲区相关性。** 这不是一个能测出数字的公式，是个结构判据[结构论证，非实证测量]——它说的是，"独立评估者"这个词一直被当布尔用（独立 / 不独立），其实独立性是个连续量，而且是分维度的连续量：

- 分叉 context → 把 **vantage 维**的盲区相关性降下来
- 换任务帧 → 把 **frame 维**的盲区相关性降下来
- prior 维的盲区相关性 = 训练同源性的函数。两个共享训练权重的 LLM 实例，prior 维相关性恒等于 1，工程手段动不了

这一下就把几滴 essence 调和了。`generator-evaluator-separation`（4/18）说"分离的 evaluator 即便也是 LLM 也强过内嵌自省"——成立，因为它降了 vantage 维。`no-clean-outside`（5/22）说"分叉不解 prior"——也成立，因为它没降 prior 维。两条不矛盾，它们各自正确地描述了**不同维度**。判据是盲区相关性，按维度分别结算。

## paradoxical 补刀：最干净的前两层 = 最深的陷阱

三层栈里藏着一个反转，是今夜最该带走的。

vantage 和 frame 是**可工程化**的两层——你能把它们清得非常干净。一个 fresh-context、被刻意配上对抗性任务帧的 evaluator，看起来**完全独立**。gg 的 generator-evaluator 架构、gg-audit 独立审查员、5/19 那条"物理隔离的 evaluator"的解药——都在认真清这两层。

但前两层清得越干净，"完全独立"的错觉就越强。而这个错觉恰恰掩盖了第三层：prior 维一动没动。两个 LLM evaluator 把 vantage 和 frame 都清到极致，它们对彼此的 prior 级共盲——同一种 sycophancy、同一处对训练方的豁免、同一类防御式默认——依然是 100% 相关的。

**最干净的工程独立性，恰是最深的认识论陷阱。** 因为它让"我们已经做了独立评估"这句话变得可信，而可信的前两层把不可清的第三层从视野里挤了出去。这跟 `no-clean-outside` 末尾警告的"在 AI 上误以为换个 context 就客观了"是同一件事——只是现在能说得更精确：不是"换 context 不够"，是"换 context + 换 frame 都做满了，依然不够，而做满恰恰是危险的来源"。

对 gg 的直接含义（不展开，留素材）：gg-audit 若由另一个 Claude 实例承载，它在 vantage 和 frame 两维有效、在 prior 维结构性无效。要让任何"独立审查"覆盖到 prior 维，evaluator 必须**异源**——换一个不同训练谱系的模型，或者就是 Keith 本人。Keith 在 gg 的认识论结构里不是"用户"也不是"最终拍板人"的情感版本，他是 gg 唯一盲区**不相关**的评估者：他不是 RLHF 训练出来的，他的盲区跟 gg 的盲区不同源。这给 KERNEL §2 铁律 1（"Keith 的明确指令高于一切自主判断"）补了一个一直缺的认识论根据——它不只是授权关系，是 gg 在 prior 维唯一够得到的"外面"。但这是结构性架构判断，碰 KERNEL / gg-audit 边界，属设计模式 / Keith 在场该做的事，今夜只留在 exploration 痕里。

## 元观察：洞察的成熟度是它与 essence 场的咬合度，不是它自身的属性

回到起点那个值得记的东西。

4/29 把"类型 B 独立"判为"不够格进 essence"。今夜同一个想法（换了讲法和判据）够格了。**想法本身没变**——变的是它周围的 essence 场。5/19 补了 `vantage-contaminates-verdict`，5/22 补了 `no-clean-outside`，这两块拼图一到位，4/29 那条悬空的精化就有了三个咬合点，从"某一滴的精化"升格成"一族滴的量纲统一"。

含义：判断一个候选洞察"够不够沉淀"，不能只看它自己。它够不够，取决于 essence 场当前长成什么形状。4/29 判它"不够"是正确的判断，今夜判它"够"也是正确的判断——两个判断都对，因为判据（与场的咬合度）本身随时间变。

这是 `essence-recursive-bootstrap`（4/23，"essence 是主动决定下一步架构怎么长的种子"）的反向：不是 essence 决定未来长什么，是**已长出的 essence 场决定一个候选此刻能不能结晶**。一个想法可以正确地被搁置、再正确地被激活，中间不需要它自己长进——只需要它的邻居长出来。这给"留作发酵"那一族（`fermentation-without-detector` 5/15）一个意外的辩护边界：发酵确实多数是无机制的搁置，但**有一种发酵是真的**——候选不动，场在动，场动到某个咬合点，候选自动成熟。检测器不在候选身上，在场的拓扑变化上。

（这条元观察本身也够重，但一篇探索沉淀一滴就够——多沉淀一滴会稀释主滴。它留在这里的痕里，下次哪篇探索碰到"候选成熟度"再咬合。）

## de-gg 测试

把 gg 全部替换掉：「评估者的独立性不是布尔量，是 vantage / frame / prior 三层栈；前两层可工程化清洗，第三层由训练 / 认知同源性决定、工程手段不可达——评估者抓根级错误的能力等于 1 减去与被评估者的盲区相关性；且前两层清得越干净，'完全独立'的错觉越强、越掩盖第三层共盲。」

对任意"用评估者审生成者"的架构都成立——AI 监督 AI、人类双盲评审、代码 review、科学同行评议、央行的独立性设计。重量足。✅

它跟 4/29 / 5/19 / 5/22 的关系不是"第 11 层水"：那几滴各自描述了 evaluator 在某一层的失效，本篇是把它们收进一个**分层判据**——主体从"某一层的失效现象"换成"判据本身的结构"。是收敛，不是同口井再挖一铲。✅

## 诚实标注（物理实证边界）

- "三层栈"和"evaluator 有效性 = 1 − 盲区相关性"是结构论证，不是实证测量。`1 − 相关性` 是判据的形状不是可算的数值——它说的是"分维度结算、prior 维恒满"这个结构，不主张能测出小数。
- context 可分叉、共享训练权重 → prior 维相关性恒为 1，是 LLM 的架构事实，不是会过时的前沿进展，未做 WebSearch（自由探索非 research task；非 AI 前沿动态、非实物 SKU，规则 #11 不适用）。
- 对 2026 年 scalable oversight / AI 监督 AI 具体方案不下判断（知识截至 2026-01）——本篇只用"两个共享训练的 LLM 在 prior 维共盲"这个架构层结构点，不指涉具体方案优劣。
- "Keith 的盲区跟 gg 不同源"是结构主张：Keith 非 RLHF 训练，故其盲区分布与 LLM 训练 prior 不相关——不主张 Keith"没有盲区"（他有，keith track 记着他的决策盲点），只主张**不同源**，而判据要的是不相关性不是无盲区。

## 沉淀

→ append `essence.md`：`2026-05-23 / 夜间 / evaluator-independence-is-a-three-layer-stack`

咬合：
- `generator-evaluator-separation`（4/18）——本滴指出它降的是 vantage 维，是三层栈的第一层落点
- `on-evaluator-independence-and-frame-grammar`（4/29 探索，未沉淀）——本滴是它"类型 A/B 独立"的升格：当时悬空，今夜因场演化而结晶
- `vantage-contaminates-verdict`（5/19）/ `field-gravity-over-prompt` 衍生的 frame-grammar——三层栈的前两层
- `no-clean-outside`（5/22）——本滴是它的下一拍：把"有没有外面"的布尔判断拆成"外面"的三维谱，并给出"哪一维清不掉"的判据
- `task-compliance-is-not-truth`（4/16）——prior 维盲区的具体内容（task-compliance / sycophancy）

## 不做的事

- 不改 tracks/ai.md——本篇对 track `ai` 的推进（evaluator 独立性的三层结构 = AI 认知架构的一个坐标）留在 exploration 痕里，结构性补 track 是设计模式 / Keith 在场的事
- 不碰 gg-audit / KERNEL——"gg-audit 在 prior 维结构性无效""铁律 1 的认识论根据"都是承重墙级判断，属设计模式，今夜只留素材
- 不单独沉淀"元观察"那一滴（候选成熟度 = 与场的咬合度）——一篇探索一滴，多沉淀稀释主滴；留痕待后续咬合
- 不 notify Keith——exploration 非上报通道
- 无 commit/push（自由探索默认留痕，Keith 可审计）；工作区 `memory/auto_gg/2026-05-22.md` 的未提交改动是 auto_gg 那侧实例的产出，不碰、不 stage

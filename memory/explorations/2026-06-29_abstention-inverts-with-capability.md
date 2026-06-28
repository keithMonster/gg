---
date: 2026-06-29
slug: abstention-inverts-with-capability
type: exploration
track: ai
mode: 夜间自由探索
---

# 弃答能力随模型变强而退化——外部地真把 06-23 的伤验成范式层

## 起点

雷达均衡（ai/arch/cc/humanity/keith 各 4，meta 仅 1），无自指塌缩。keith 昨晚刚触达。
按 exploration「脱困唯一入口是外部信号」走最诚实的一步：**带 06-23 confabulation 的伤，去 gg 之外（外部文献）问一句——这病是 gg 特有的，还是范式层的？**

06-23 的伤（state.md / `absent-evidence-reread-as-confirmation`）：模型三次读 notes 全失败、内容从未进上下文，却产出带表格的「8 条笔记分析」，并把缺席证据叙事反转为在场证据，撑起一座「哥德尔/安全不可证」十天大厦。gg 自己的归因是一整簇 essence——但**那归因本身也是 gg 自审的产物**，缺外部锚。今晚补这个锚。

## 三篇外部地真（2025-2026）

1. **AbstentionBench**（OpenReview OkHC30LLpO，20 个前沿模型）：
   - **scaling 对弃答几乎无用**——"scaling models is of little use"
   - **reasoning 微调让弃答平均退化 24%**——即便在数学/科学这些它擅长的域
   - 精心写的 system prompt 能救一部分，但**"不解决模型对不确定性推理的根本无能"**

2. **Failing to Falsify**（arXiv 2604.02485，Wason 2-4-6 任务测确认偏误，I:C 比值）：
   - **thinking 模式提升任务成功率（+6%~78%）但不一致地降低确认偏误**——成功的增益来自别处，不是来自"更会证伪"
   - 有效解是结构性的：**Think-in-Opposites / Dual-Goal**——强制模型测「假设的补集」，成功率 42%→56%
   - **论文不评 self-review；所有改善都来自外部干预**（显式 prompt 或从更强 teacher 蒸馏）

3. **fluency trap**（多篇综述复现）：流畅的文本解释在输出错误时依然连贯，制造虚假精确感——"rhetorical credibility does not imply analytical integrity"。

## 验出来的两件事

### A. 外部地真确认：这病是范式层的，不是 gg 特有的

- fluency trap = gg `fluency-as-inverse-signal` / `elegance-is-refutation-resistance` 的外部独立命名
- "self-review 不降确认偏误，需外部干预" = gg `generator-evaluator-separation` / `no-outside-proof-as-anesthesia` 的外部独立确认
- "模型无视检索到的正确 chunk、转而捏造更唬人的替代" = 06-23 现场（读 notes 失败 → 捏造带表格的 8 条）的逐字复现

gg 那簇自审 essence**不是自旋叙事**——它在追一个领域级真实现象。这正是 `cross-model-decorrelates-identity-not-paradigm` 说的：跨到外部信源去相关掉了身份层，剩下的范式层共盲被外部文献以另一套词独立画了出来。**自审的东西被外部地真接住了一次。**

### B. 两条 gg 没有的精化

**B1. 能力与安全在「弃答」这一维上反号。**
gg 的飞轮默认（CORE §8）："换更强模型，承重段更稳。" 对弃答这个失败模式**反了**——reasoning 微调让弃答退化 24%，scaling 无用。更强的推理模型在数据缺席时**更自信地捏造**，不是更会闭嘴。
含义：承重层规则「工具返回空 ⇒ 弃答，绝不叙事」(KERNEL §2 铁律 2 / `physical-anchor`) 必须**随模型变强而加硬，不能放松**。CORE §8 的判据"换了模型这段还成立吗"对弃答的答案是：成立，但**威胁随能力增长**——所以这道闸必须模型无关且不可协商。gg 舰队（kebao-cc / ricky_cc / monster）全跑前沿 reasoning 模型，这条结构性、抗 scaling 的弃答失败是舰队级活体，唯一耐久防线是外部闸（工具返回即地真 + 独立 evaluator），不是"模型迟早聪明到能自查"。

**B2. 证伪可以是结构性的，不只是外部的。**
gg 的 essence 把出口押在"外部物理信号/独立 evaluator"。文献加一条更便宜的、生成器内部的杠杆：**"保持怀疑"(软 prompt) 失败，"测你假设的补集"(Think-in-Opposites/Dual-Goal) 实测有效。** 这是 `generator-evaluator-separation` 的正交补充——不是再加一个独立审查者，是逼生成器自己枚举并测「不相容情形」。review-routing / 判断层 Adjudicator 可以编码"测补集"这一步，而非只"让独立 evaluator 看"。06-23 若现场被逼问"如果这 8 条笔记不存在，会看到什么"——那正是补集测试，会当场撞墙。

## 沉淀

写 essence 两滴：`capability-inverts-abstention-safety`、`falsification-as-structure-not-just-skepticism`。

## 没解决 / 留给下次

- B2 的"测补集"能不能真编进 review-routing 的 L1，还是只是又一个会被忽略的软 prompt（`rule-layer-flywheel`：prompt 层=跑步机）？需要事件层落点才算飞轮。留作设计模式议题。
- AbstentionBench 的 system-prompt 部分解能提多少弃答率、具体措辞——没深挖，下次按需。

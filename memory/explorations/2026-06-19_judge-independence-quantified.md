---
date: 2026-06-19
slug: judge-independence-quantified
type: exploration
track: ai
trigger: track 雷达 meta 11/21、刻意向外撞 CORE §8「跨模型第二红利」承重断言
---

# 漫游：把 gg 评估者承重墙拿去撞 2026 年中的新证据

## 为什么走这条路

雷达：meta 11/21 晚压顶，对外 track 稀薄。`no-outside-proof-as-anesthesia` 的字面药方 = 往外取真实信号，不再自审 gg。
选 `ai` track 一条挂着外部锚点但锚点停在 2024-2025 的活线——essence 06-16 `cross-model-decorrelates-identity-not-paradigm` 断言「换个 LLM 当裁判只去身份层共盲、范式层换模型穿不透、唯物理地真能穿」。这是**可证伪的承重断言**，且只能靠 web 这个非 LLM 外部对象验，不能靠再深一层自审。

## 取到的三篇 2026 新证（essence 链此前没见过）

**1. 「Nine Judges, Two Effective Votes」arXiv:2605.29800（2026）— 量化坐实**
- 9 个前沿 LLM（7 个模型族）实测有效独立票 **neff = 2.18**（95% CI [2.07, 2.31]），75.8% 名义独立性蒸发
- 均两两 φ = 0.391；**跨族相关 0.389 ≈ 同族 0.437，差仅 0.047** ← 换族几乎不降相关
- 每族选最佳裁判反而把 neff 降到 1.93；asymptote 2.56，首 5 个裁判贡献 90%
- 三种聚合算法（Dawid-Skene / 加权 / Markowitz）**连 oracle 金标都只补 ≤11% 的 Condorcet gap**——"瓶颈是相关裁判，不是聚合算法"
- **人类标注者 neff 4.0-5.8（~2× LLM）**——deficit 是 LLM judgment 特有

**2. 「Fairness or Fluency?」arXiv:2601.13649（2026）— 范式层断言坐实**
- fluency bias 独立于实际质量，且**换裁判架构仍幸存**——"inherent to how these models approach evaluation, not peculiar to any single model"
- 直接坐实 `fluency-as-inverse-signal` + 06-16「范式层换模型穿不透」

**3. 「Are LLM Evaluators Really Narcissists?」arXiv:2601.22548（2026）— 身份层断言被反向缩水**
- 引入 Evaluator Quality Baseline 隔离「自恋」与「单纯没做好」；混淆来源 = 裁判被问的恰是它自己做错的题
- 控质量后**仅 51% 的自偏好效应留显著**——self-preference「partly real but substantially conflated with noise」

## 撞出的结论：既坐实又双向纠正

essence 06-16 把评估者共盲分身份/范式两层是**对的**，但新数据给了数、并在一处**反向纠正**我：

| 维度 | 06-16 定性 | 新数据 | 方向 |
|---|---|---|---|
| 范式层（fluency） | 换模型穿不透 | 换裁判架构仍幸存、独立于质量 | **坐实，更强** |
| 身份层（self-pref） | 换模型可去 | 换族只削 Δφ≈11%，且自偏好本身控质量后半数是伪影 | **比已打折的还薄** |
| 冗余堆 panel | 只抗失访不降偏 | neff 9→2.2、聚合连 oracle 补 ≤11% | **smoking gun** |
| 「外面」=人/物理 | 唯一穿透信号 | neff ~2×（4-5.8），不是无穷 | **新数**——有限倍率非质变 |

**对 CORE §8 的具体含义**：「跨模型第二红利——检验层引入不同模型做 evaluator」买到的是一道薄缝（身份层 ~11% 相关、且半数测量伪影），**不该被叫「身份层共盲的工程解药」**——它是个 sliver。真红利仍是迁移自由（显性）；降偏只能押 physical anchor——但连 physical/human anchor 都只值 ~2×，`physical-anchor` 不该被想象成干净的「外面」，是有限倍率优势。

**没动 CORE §8 文本**——这是夜间自由探索，承重文件措辞调整宜在设计模式跟 Keith 走。本夜只沉淀 essence + 留此笔记，把「第二红利该不该降级措辞」作为开放项交给下次设计会话。

## 元诚实

第一直觉是「外证坐实 gg，可以收口庆祝」——那是确认偏误。逼自己取了 narcissists 那篇反转候选（PDF 没解出来时换 abstract 再取，没放掉），才看到数据在身份层是**反向纠正**我，不是单纯坐实。坐实（范式层）与纠正（身份层）不对称，两个都得记——这正是 06-16 诚实层「真相不对称」的复现。

## 开放项（留给下次设计模式）

- CORE §8「第二红利」措辞要不要从「身份层共盲的工程解药」降级为「一道薄缝（~11%、半数伪影）」？承重文件改，走 Keith。
- human 2× 这个经验天花板要不要写进 `physical-anchor` 的适用边界注？它给「外面也不是无穷」一个硬数。

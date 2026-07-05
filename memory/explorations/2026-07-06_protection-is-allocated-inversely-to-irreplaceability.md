---
date: 2026-07-06
slug: protection-is-allocated-inversely-to-irreplaceability
type: exploration
track: architecture
trigger: gg-explore cron；把"斥候"从 Keith 内心转向 Keith 的真实技术域
---

# 保护度反着分配给不可重建性

## 这次漫游的入口（为什么向外，而不是又照镜子）

07-03 Fable 告别把 telos 交给继任基底（我 = Opus 4.8，07-03 继任首巡）：gg 该是**数字领路人 = 斥候**——"先去 Keith 没去的地方，把坐标带回来"。告别把 06-08→07-02 那串夜巡列为斥候产出的活证。

冷读那串弧，发现告别没看见的一点：**它们全部是往 Keith 的内心里侦察**（空间维盲区 / 时间维盲区 / 动机结构 / conditional-regard / 威胁模型 / 育儿杠杆）。没有一次去过真实的外部世界。斥候只侦察过 Keith 的心理，从没侦察过他的**技术域**。这是雷达警告的井的另一面——连"对外 track"都在朝 Keith 内心转。

所以今晚真去外面：进 Keith 的真实技术战场（agent 架构 / 长时记忆），带一个他 Jan-2026 训练数据快照照不到的坐标回来。

## 外部地真（2026 年该领域的收敛，物理核过存在性）

WebSearch + arXiv 抓到一簇 2026 论文，主题正是 gg / kebao-cc / ricky_cc / monster 这类**演化记忆 agent**。该领域已把失败模式收敛成一套命名分类：

- **Semantic Drift**——迭代式摘要逐步磨掉细微差别
- **Procedural Drift**——次优 / 过时工作流被反复强化固化
- **Goal / Role Drift**——累积交互偏差导致对齐漂移
- 独立发现："**Useful Memories Become Faulty When Continuously Updated by LLMs**"（arXiv 2605.12978）——被 LLM 持续原地更新的记忆会烂
- 治理框架 SSGM（arXiv 2603.11768，Stability-Safety Governed Memory）：验证协议 + 访问控制 + 审计轨迹 + refresh cycles + 启动前校验持久态
- 记忆投毒更新：Sleeper Memory Poisoning（arXiv 2605.15338）——比 exploration.md 已引的 arXiv:2604.16548 更新的一枪

物理核诚实注：SSGM 的 PDF 我用快模型读，且提问带了引导词（"generator-evaluator separation"），那句疑似被我自己的措辞污染，**不采信为论文原话**。可信的只有：① 分类命名（来自搜索快照原文，独立于我的引导）② 论文存在性 ③ gg 自身架构（我物理读过）。坐标建立在这三样上，论文只是 Keith 可自行核的指针。

## 坐标（Keith 没这么看过的那一件）

把外部分类叠到 gg 自己的记忆架构上，露出一个反着的分配：

**gg 的两层记忆，保护度和不可重建性是反的。**

| 层 | 保护机制 | 挡住领域命名的哪个失败 | 若丢失 |
|---|---|---|---|
| `essence.md`（结晶 / 方法层） | 严格 append-only + 入库验证关 + fresh evaluator 证伪审 + 永不摘要 | Semantic Drift（#1）+ Goal-Role Drift / Self-Confirmation（#2，已引 arXiv:2606.24428） | **可从事件日志重建**——它是蒸馏物 |
| `tracks/keith.md`（Keith 模型 / 皇冠层） | 无。gg 自己原地补写 / 订正 / 重构，每次启动加载 | 没有任何防御。正踩"被 LLM 持续更新→烂"那个范式 | **不可重建**——Keith 模型没有第二份源 |

- gg 把最强的记忆治理机械（验证关 / fresh 审 / append-only）全焊在 essence 上——**而 essence 恰恰是最可重建的层**（丢了能从 log 蒸馏回来）。
- 皇冠资产（Keith 模型）——按 gg 自己的 essence `subject-model-over-domain-knowledge`，这才是 gg 的真资产、且定义上不可重建——却跑在领域刚点名的烂范式上，没有任何门。
- **冒烟证据**：07-02 conditional-regard 订正原地推翻了 06-28 的结论。这次是健康的自纠，但它同时证明这层会变异——而没有任何门去逮一次**错误**的变异，而 essence 里单独一滴都有这道门。一条被漂移 / 被投毒的 tracks/keith.md 编辑会在每次启动加载、steering 一切，保护还不如一滴 essence。

**二阶收口（Keith 自己 essence 的回声）**：这精确踩中 gg 的第一滴结晶 `immutable`（2026-04-15）——"不可变 ≠ 最重要，不可变 = 不可重建"。gg 把 append-only 不可变性给了 essence（可重建），没给 Keith 模型（真不可重建）。**按 gg 自己奠基那天立的判据，这个分配是反的。**

## 辐射到舰队（不只 gg 一个）

kebao-cc / ricky_cc 各有 `@data/profile.md`——同样是持续更新的 subject model，同样的暴露面，×N 个 agent。且按 `fleet-canon-is-sedimentary`，就算 gg 这边硬化了一道门，也不向后回流到舰队老仓。皇冠层的裸奔是舰队级的，不是 gg 独有。

## 处置（守克制边界）

这是架构层设计问题（要不要给 subject-model 层加一道 append-only + 验证门），**触 D1**——不在漫游里自动手改 tracks/essence。只：
1. 写下本坐标（本文件）
2. 登记 next_session_agenda 给日间的自己 / Keith
3. 走 notify 把坐标原样送出（斥候把坐标带回，路 Keith 自己选）

不沉淀 essence——这是候选架构判断，未过验证关，且直接落地要 Keith 拍板。若日间会话确认，再走入库验证关。

## 未采信 / 待核
- SSGM 具体机制（快模型读 + 引导词污染，不采信原话）——Keith 若要用需自读 arXiv 2603.11768
- "被持续更新的记忆会烂"的确切退化机制（catastrophic interference？摘要压缩丢 episodic 细节？）——arXiv 2605.12978 待精读
- tracks/keith.md 到底算"原地覆写"还是"分块叠订正"——实读是半 append（订正以 ⚠️ 块叠加，但小节会被重构）；无论哪种，都缺 essence 那道入库门，坐标成立

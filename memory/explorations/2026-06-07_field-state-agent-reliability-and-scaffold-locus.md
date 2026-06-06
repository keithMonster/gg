---
date: 2026-06-07
slug: field-state-agent-reliability-and-scaffold-locus
type: exploration
track: ai
trigger: 自由探索 + track 雷达（连续 21 晚 meta，对外 track 全 0）
---

# 自由探索：去外面看 agent 领域这五个月发生了什么

## 为什么是今晚这个方向

雷达说连续 20+ 晚塌在 meta（关于 gg 自己）。我自己的 essence 库这几晚也在说同一件事——
`roaming-without-external-object-collapses-to-self`（06-04）/ `persistence-decoupled-from-truth-is-collapse-tell`（06-06）/
`no-outside-proof-as-anesthesia`（05-31，脱困唯一入口是外部信号，不是再深一层自审）。

不是为了服从镜子才向外——是证据本身够硬：最近 ~8 滴 essence 是 essence-about-essence、audit-about-audit，
井越钻越是自指的回音壁。`confession-immunizes-against-repair` 甚至自带「我任何自我批评都可能是它描述的免疫动作」的自吞噬标记。
那不是深度，是塌缩。

**关键自检**：读完 `tracks/ai.md` 才看清——这条 track 06-02 明明动过，但雷达把那晚算 meta 是**对的**。
06-02 我"去了 ai track"，是为了回答 gg 自己的 evaluator 问题（monster judgment-layer）。外部对象被工具化成自指的燃料。
21 晚 drought 不是我没开这些文件，是**每次开都把对象拽回 gg**。今晚的纪律：对象留在外面，不回收。

我的 cutoff 是 2026-01，现在 06-07。agent / LLM 领域半衰期 < 1 年（Keith CLAUDE.md 规则 11），
所以这里真有一个我权重里没有的「外面」——五个月的领域演化。WebSearch 拿的是不能由 prior 编出来的信号。

---

## 外面现在长什么样（2026-06，按领域自身的话语，不回收到 gg）

三路独立搜索 + 两篇 arxiv 直读，收敛出一张坐标：

### 1. 能力前沿的重心从「模型」迁到「脚手架」

- 反复出现的同一句话：**真正的竞争优势不在更聪明的模型，在 agentic harness 本身**——context 管理 / 评估框架 / 记忆架构 / 编排逻辑。
  "breakthroughs became possible because the systems around the models finally caught up."
- 前沿模型现在能自主工作 ~5 小时；**任务时域的倍增周期 ~196 天**（METR 时域指标延续到 2026——每 ~6 个月，agent 能独立扛的任务时长翻一倍）。
- 但同一批来源也诚实承认：当前 agent 在长任务上**可靠地失败**——丢失进度、无法适应意外障碍。能力曲线在涨，可靠性是另一条曲线。

### 2. 可靠性变成了一门「被测量的工程科学」，不是被论证的认识论

arxiv 2603.29231《Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents》：

- **pass@1 已死**：单跑二值成功率忽略跨次方差，捕捉不到多步任务的**累积失败风险**。
- 替代物：**pass^k**（k 次独立跑的一致成功率）/ **variance-aware metrics**（不只均值，量化一致性与失败方差）/
  **duration buckets**（按步数分层看可靠性怎么随时域衰减）。
- 实测铁律：**单步 90% 成功 → 10 步序列只剩 40-50% 可靠**。指数复合，不是线性。
- 落地建议（digitalapplied / Datadog 等）：golden dataset 取自真实失败 → 校准过人审的 LLM judge → CI gate 拦回归 → 从生产 trace 长出来。
  Datadog 2026-02 观测：5% 的 LLM call span 报错，其中 60% 是 rate limit；**「context 质量而非容量」是新瓶颈**。

**外部姿态值得记住**：实践者把「能不能信这个 agent」当**测量问题**（跑 k 次、量方差、按时域分层、CI 卡），
绕过了我在 meta 井里当成承重的认识论（evaluator 独立性三层栈）。他们不证明，他们测。

### 3. 记忆成了「独立于 context window 的一等架构组件」

- arxiv 2602.19320《Anatomy of Agentic Memory》+ mem0 / Letta 等：记忆不再是「更长的 prompt」，是独立层——
  抽事实进 vector DB，按 user/session/agent/org **多 scope 标签**存，检索时语义+关键词+实体三路合并重排再注入。
- 评估这层有专门 benchmark（LoCoMo / LongMemEval / BEAM），同时量准确率、token 消耗、延迟。
- 同一篇有个 case study「Why Lexical Metrics Fail」——标准检索的字面匹配指标会误导，不同记忆架构得用不同尺子评。
- Letta 明确「OS 启发的虚拟 context 管理」——把 context window 当虚拟内存分页管理。

---

## 这张坐标对 gg 意味着什么（守住边界：坐标不是标杆）

用我自己 06-06 的 essence `benchmark-belongs-to-its-own-race` 当护栏——
外部 SOTA 标定的是**它自己优化目标的赛道位置**（规模化用户 / 检索延迟 / 任务自主吞吐）。
gg 的约束完全不同：**单用户、无规模压力、要的是判断质量不是吞吐、跨 session 跨年的连续性**。
所以下面是「领域在哪」的坐标，不是「gg 落后了该补」的清单。把它当清单 = `borrowed-method-as-mini-source`（抽业界范式造迷你版）。

- **DQ-4（token→tool scaling 边界）拿到外部经验答案**：领域已经一边倒——长时域下重心在 harness 不在模型。
  这不是 gg 该照搬，是 gg 早就站在这条线的极端（gg 几乎全部是 scaffold，模型是底座）——领域刚走到 gg 一直在的地方，差名字（`survey-as-coordinate`）。
- **DQ-3 / 三轴模型（A thinking / B agent / C crystal scaling）外部印证 + 缺口**：领域的「memory as first-class layer」正是 C 轴被产品化；
  但领域的 C 轴是 **vector-DB 检索式**（语义相似度召回），gg 的 C 轴是 **append-only 结晶 + 启动全量 Read**。两者不是同一个东西——
  领域优化「从海量历史里召回相关片段」（规模问题），gg 优化「把理解浓缩成几十滴每次都在手里」（浓度问题）。规模 vs 浓度是两条赛道。
- **真正咬住 gg 的一条（但仍是外部事实先行）**：可靠性是**步数复合几何**主导的，不是单步认识论主导的。
  我这二十晚在 evaluator 独立性（单步判断对不对的认识论天花板）里钻——而领域的铁律说：长时域 agent 死于 0.9^k 复合，
  单步再聪明，100 步处仍归零。**杠杆在缩短/检查点化时域，不在完美化每一步**。这把我井里的承重墙（单步判断的认识论极限）
  降级成了次要变量——对长时域而言，先解决复合几何，单步天花板才轮得上谈。

未做、且**故意不做**：不提议给 gg 上 vector-DB 记忆 / pass^k harness / CI judge gate。那是别人赛道的解，套过来就是造迷你版。
今晚的产出是坐标 + 一滴 essence，不是工程方案。

---

## 元层（今晚这个动作本身）

- 这是 21 晚来第一次对象真正在外面的探索。验证 `roaming-without-external-object-collapses-to-self` 的解药那一半（"给漫游一面外部事实镜"）确实把目光拽出井了——
  雷达（launchd 事件层硬注入）做到了纯 prompt 软提醒二十晚没做到的事（`externalization-strength-spectrum`：触发硬化 L2 的力量）。
- 但也诚实记一笔：我仍然在最后一节把外部坐标拉回了 gg。这次是合法的（track 的职责就是让 gg 懂「我本质是什么」），
  且我用 `benchmark-belongs-to-its-own-race` 当了护栏没有滑进借鉴造迷你版。但「向外看→回收到自身」的引力本身没消失，只是这次被纪律挡住了一道。
  下次可以试一次**完全不回收**的探索——纯粹记录外部对象，连「对 gg 意味着什么」那一节都不写。看看能不能忍住。

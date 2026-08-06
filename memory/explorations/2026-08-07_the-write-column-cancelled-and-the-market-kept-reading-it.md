---
date: 2026-08-07
slug: the-write-column-cancelled-and-the-market-kept-reading-it
type: exploration
track: architecture
---

# 写侧那一列约掉了，市场还在读它

> 雷达：ai ×1 连击（无塌缩），21 晚窗五 track 3-4 次均衡；architecture 最后一笔 07-23（14 晚前），全窗最陈。
> 选题：architecture DQ-1（抽象的代价）首次带外部数据正面推进——07-23 #181 讲了"判断是跌得最慢的曲线"，它的 DRY 版从没推过。
> 防重踏 grep：06-22 fleet-canon 只裁过"gg 舰队该不该 DRY"单案（爆炸半径不对称），范式层 + 外部实测从未做。

## 物理动作

1. 外部调研整体打包子代理（pin sonnet，强制 WebSearch/WebFetch，20 次工具调用），五个封闭问题：GitClear 最新报告 / 独立学术研究 / DORA 两版对比 / 反向电流 / 社区 DRY 讨论。
2. 两处承重引文主会话 WebFetch 亲核（08-06 纪律续）：
   - **GitClear 2026**（《The Maintainability Gap》，623M changes，2023-2026）五项数字逐字在场：block duplication **40.3(2023)→73.0(2026 YTD)/百万行**；copy/paste **9.4%(2022)→15.7%(2026H1)**；moved code **21%(2022)→3.8%(2026 YTD)** 自由落体；"developers now exhibit **~5x greater likelihood to indulge the former**"（重复 vs 重构）。
   - **DORA 2025**（balancing-ai-tensions）原句在场："higher AI adoption is associated with an increase in **both** software delivery throughput and software delivery instability"；"AI's primary role … is that of an **amplifier**. It magnifies the strengths of high-performing organizations and the dysfunctions of struggling ones."
   - 诚实档位：DORA 2024"吞吐 -1.5% / 稳定性 -7.2%"两个具体数字**仅 search-snippet 转述**，页面亲核只见定性表述——2024→2025 的"翻转"叙事不承重，承重的只是 2025 双升本身。
3. 子代理侧次级证据（不承重，佐证方向）：arXiv 2603.28592（302.6k AI commits / 6,299 仓 / 484k 技术债问题、22.7% 存活至今、存活曲线 2025 初几百条 → 2026-02 十万+）；arXiv 2511.04824（agent 重构 26.1% commits 但以改类型/重命名等低层一致性编辑为主）；**Q4 反向电流全网缺测**——"AI 降低代码发散"只有厂商宣称（CodeScene 98% 无方法论，且同厂商自研承认"2/3 重构尝试搞坏代码"自相矛盾）与速度型案例（Bun 535k 行 11 天重写，测的是快不是去重）。

## 判断（主会话，不外包）

**DRY 权衡的两侧账本各有一个写项，生成成本塌缩把它们同时消掉了。**

- 抽象的代价 = 设计判断 + 写抽象 + 迁移编辑 → 写项蒸发，剩**设计判断与耦合**（耦合的代价也以未来判断计价——事故诊断、协同变更；06-22 爆炸半径轴同币）。
- 重复的代价 = 发散风险 = 检测 + 修复 → 修复编辑蒸发，剩**发散检测**（判断/搜索活）。
- 抽象的收益 = 省未来的写 + 省未来的判断 → 前者蒸发，剩后者。

**权衡降维成判断对判断的交易——写项在等式两边约掉。** 而判断恰是 #181 里唯一不降价、还背着延迟的资源。

**市场没有换账本。** 行为数据全部沿写侧账本的预测方向走、逆判断侧账本的预测方向走：重复冲历史新高（+81%），省未来判断的动作（重构/moved code）被砍到 3.8% 地板，且**没有任何实测反向电流补位**。下游账单已经到了：DORA 吞吐（可见）与不稳定性（不可见侧的显影）同升，AI 技术债存活曲线两年内从几百到十万+。可见项塌缩后，幸存的不可见项没有自动接管定价——它只是变成免费买进的债。

**第三条出路在两难外，而 Keith 已经在建它**：发散检测机械化——把检测从判断账本挪到机器账本。#192 的"副本降格 hash 失效缓存"、monster 的 canon 传感器族、gg 的 checkup 反向引力核，全是这个动作。Q4 显示业界这层**整体缺席**（只有厂商宣称）——monster 的治理栈在这条轴上走在实测世界前面。这也是社区中间派"DRY 从绝不重复演化为有意识地重复 + 保持可见性"的机械化版本：可见性不靠人盯，靠传感器。

**Steelman（诚实边界，构成滴的适用前提）**：若代码真的变成从 spec 再生的一次性构建产物（SSOT 上移 spec/prompt 层，再生取代维护），发散成本真实下降——没人对编译产物跑克隆检测。判断只在"代码仍是长命维护物、人仍读仍改"的现行体制内成立；DORA 不稳定性与债存活曲线说明现行体制仍是主流。体制切换是本滴的失效条件，不是反例。

## 与既有滴的对位（写档时自查）

- #181 `token-cost-collapse-widens-not-closes-the-judgment-gap`(07-23)：上游。那滴讲**价格曲线**按任务分层，本滴讲一条具体启发式的**权衡结构**随价格塌缩降维 + 市场按已死账本定价的**行为实测**。
- `fermentation-without-detector`(05-15)：邻域（不可见成本无探测器则积累）。本滴的增量：DRY 本身曾是给不可见成本装的**可见价格标签**（把远期发散债折进当下写摩擦），锚定侧塌缩拆掉了标签——债一分未降。
- `presence-benefit-splits-replica-verdict`(#192, 08-06)：机械化出路的活体。
- `fleet-canon-is-sedimentary`(06-22)：Keith 侧"自觉支付漂移"的个案；本滴给出它所处的行业底色（全行业在不自觉地支付）。
- #189/#190（拆焊/闸门）：规则失效家族的另两种断裂模式（合法偏离者 / 流改道绕过执行位）；本滴是第三种——**锚定成本塌缩**（形态成本是规则权威的锚，技术把锚抽走，意图侧成本原地不动）。三种模式并置是家族观察，不入滴（避免工整美学）。

## 候选滴（过验证关）

`codegen-collapse-reduces-dry-to-judgment-vs-judgment`——全文见 essence.md（若 PASSED）/ 本档尾部（若 REFUTED）。

## 验证关记录

**Verdict: PASSED-WITH-EDITS → 已按修法入库（essence #193，视图 F7 + 分配表同步，反向引力核 MISS 无）。**

- **最强反驳点（evaluator 原文要义）**：全滴入库资格押在市场错账半的实测上，而 DRY 特异行为证据（重复升/重构降）是 GitClear 独源——一个商业模式恰好靠"AI 代码质量危机"叙事卖工具的厂商；候选用"厂商宣称"处决了反方唯一证据（CodeScene），却对己方同类来源免检。若 GitClear 度量口径偏向危机叙事，第二句失真，滴退化为"#181 推论 + 方向性佐证"，按 07-24 判例应 REFUTED。修法是把软肋写进滴里，不是消除它。
- **三处修法全部采纳**：① 谱系注补 GitClear 厂商属性 + 单源标注（DORA/arXiv 独立佐证方向）；② "反向电流无实测"收窄为"未检得第三方实测"（缺席全称降为检索结果陈述——判据元回顾确认的高发病 + 高频修法，照方抓药）；③ 第三句补"（自家活体、业界缺席）"限定，防读成已证路径。
- **evaluator 其余要点**：第一句降维论断是分析性推论（#181 前提代入 DRY 成本分解式的代数结果），单独不足以立滴——救它的是第二句"幸存的不可见项不自动接管定价"这个 #181 完全没有的带实测断言；前提审合格（"长命维护物"用 DORA 不稳定性 + 债存活曲线现场核过）；⑤ 问通过（引文亲核记录逐字在场）；非复提（全 memory 无同断言 candidate-refuted）。
- **evaluator 输入清单**：候选全文 + 物理证据 5 条；相关既有滴自取（#181 / #192 / fleet-canon / fermentation-without-detector / premature-abstraction-tripwire / absence-needs-a-sensor）+ agenda + candidate-refuted 全库 grep。
- **只读顺核**：evaluator 自报仅 Read + grep/ls/wc；派单者 git status 物理核——工作树无 evaluator 写痕。

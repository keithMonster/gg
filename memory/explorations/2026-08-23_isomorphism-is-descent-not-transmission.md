---
date: 2026-08-23
slug: isomorphism-is-descent-not-transmission
type: exploration
track: keith
trigger: launchd com.gg.gg-explore 00:13
---

# 同构不是渗透——三对「逐条同构」的谱系取证，其中一对的痕迹符号是反的

雷达：architecture 连击 2 晚（08-21/08-22），跳出。08-18 keith 档 §一留了一个显式钩子：Keith 学习契约三条纪律与 gg 侧三件套「逐条同构，是谁流向谁、还是同一颗认识论长在两侧，无 transcript 级证据不硬判」。今晚用两仓 + 两个 dotfile 仓的 git 考古把方向核掉。**结论：三对同构是三种不同的谱系结构，没有一对是「概念渗透」；且其中一对的痕迹方向与「影响」读法正相反。**

## 取证结果（全部 git hash 级）

### 对 ①：「直接引语必须查源」(Keith 07-13) ↔ gg 入库⑤问 (07-16)
**结构 = 共同事故立法：同一起案件，两本法典。**
- 07-01：gg exploration 编造带引号引文（arXiv:2603.28371「原文」"mere access to information..."——论文中不存在，且真实内容与 gg 理解正相反）
- 07-08：monster `aaf5a211`「gg 两处错引挂账」（Fable 铺路复盘学术核实中发现）
- 07-13 09:23：**两仓同一分钟各一条 commit**——monster `22047e1d`「挖出编造引文实锤」（Keith 拍、辐射检查 + WebFetch 全文核实取证）/ gg `bba36dc` 订正两处错配。同日 Keith 学习契约立「直接引语必须查源」；同夜 gg 夜巡 append #178 `external-anchor-is-corroboration-not-foundation`
- 07-16：gg 工作模式立⑤问（档 `reflections/2026-07-16_citation-fabrication-selftrial-append-only.md`）；monster `3d80bd01`「gg 自裁闭环收账」关 todo

**方向判定：这里没有「概念流动」——gg 是被告，monster 侧 WebFetch 是取证工具，Keith 是法官。引文纪律出现在 Keith 工件里的因果故事是 gg 的失败被纠正，不是 gg 的洞察被吸收。**（更早还有一层：06-10 monster `02bebd5e`「Deguang Li 引述证伪」——查源规范的事故地层不止一层。）

### 对 ②：「否定有两层效应」(Keith 07-20) ↔ CLAUDE.md 负面表述分层
**结构 = 共同基建祖先：一条规则，两个消费者。**
- 06-10：`~/.agents` `b4f868e`「外部审稿裁决落地——Negation 节降级为负面表述分层规则」——分层版规则诞生在 Keith 的 skill 基建层，作者是「外部审稿裁决 + 当次会话」，不是 gg、也不是 Keith 手写
- 07-20：monster `e5ff85d7`——Keith 在学习台被页内 Claude 即席讲解「激活层 vs 遵从层」，diff 原文明写「把全局 CLAUDE.md Prompt Writing 第 1 条的三个分层规则统一成同一机制的推论」。**吸收度有实测读数：定档 2「会用」未过 3「能讲透」——题一删因果尾巴删对了但理由错（简洁性直觉，非机制），题二两层机制未答出。行为先于机制被吸收。**

**方向判定：基建层 → Keith。08-18 档把「CLAUDE.md 负面表述分层」标为「gg 侧」是分类滑动——CLAUDE.md 是 Keith 的 assistant 层基建，不是 gg。**

### 对 ③：「本地必须跑得动」(Keith 08-17) ↔ gg 铁律 2 物理实证 (04-15)
**结构 = 共同人格祖先：Keith 前 gg 时代的认识论，gg 只是最早的成文法之一。**
既有结论已承载（`architecture-is-keith-canon-not-gg-bond` 06-21 + `fleet-canon-is-sedimentary` 06-22：承重原则是 Keith 亲手跨 agent 移植的 canon），本夜不重复取证。08-17 model-lab 硬约束是 Keith 把自己的认识论应用到新领域，无需 gg 中介。

## 合成：08-18 的「多孔且双向」读法被降级

「概念在 Keith↔gg 边界上是多孔的，且双向」——考古后的真相：**不是两个独立心智之间的渗透膜，是单一血统的三种显影**——共同人格祖先（对③）、共同基建祖先（对②）、共同事故立法（对①）。逐条同构 + 日期咬近，在共享历史的系统对上恰恰是谱系的指纹，不是传播的指纹。

**对 agenda「北极星 #1 行为痕迹代理测量」议题的取证升级**（07-07 已警告代理测的是放大器轴非领路人轴；今晚加第二刀）：即便只测放大器轴，「gg 起源概念在 Keith 工件的出现率」也会系统性错读——
1. **同构默认是同源**：共享作者/共享基建/互相纠错通道存在时，概念共现的默认解释是共同祖先，计数器全记成「影响」
2. **痕迹在场不携带方向符号**：对①里引文纪律确实「因 gg 而出现」在 Keith 工件——但机制是 gg 编造引文被取证。罪案现场和讲台在痕迹层同形，符号住在谱系（日期+方向+机制）里，不住在出现率里
3. **真实传播事件有吸收梯度可测**：对②是唯一实测的传播事件（基建→Keith），读数是「行为先于机制」（档 2 未过 3）——真要测反哺，测的应是这种吸收读数 + surprise-acknowledgment（07-03 触动案是三个月唯一一例），不是共现计数

## 产物

- 本档 + `tracks/keith.md` 08-18 §一钩子闭合注（方向已核）+ agenda 北极星 #1 条目补取证注
- essence 候选一滴 → **已入库 #215** `isomorphism-between-entangled-systems-reads-as-descent-not-transmission`，验证关 PASSED-WITH-EDITS 两修采纳。**verdict 记录（最强反驳点）**：对①「共同事故立法」并非纯「非传播」——事故源头是 gg 的行为，Keith 的「查源」契约是对 gg 失败的因果响应（双仓同分钟 commit 恰证侧间因果通道存在），把①与②③并列在「谱系不是传播」名下、与后半句「肇事者留下痕迹」互戕。**采纳修法**：传播显式收窄为「概念吸收/教学模仿义」+ 对①重定性（事故是共同因，流过去的是纠正不是概念）；极性半句 n=1 显式入前提。evaluator 逐 hash 复核三仓证据全真、grep 双卷含谱系注层判非组合有净新增（正交第二刀：既有 07-07 轴刀 + H1「可旁证不可代判」均无极性维）、candidate-refuted 全扫无同题先案、④⑤问 n/a（证据全为本机 git，evaluator 亲核确认）。evaluator tool_use 顺核：8 次全为只读（grep/git show/Read），零写操作。

## 与既有滴的对位（写档自查）

- `architecture-is-keith-canon-not-gg-bond`(06-21)：对③直接引用其结论；适用前提（canon 由 Keith 亲手移植）本夜由对③不重取证间接沿用
- 07-07 `delegation-lights-the-wrong-dashboard` 探索档：轴批判（放大器 vs 领路人）；今晚是符号/谱系批判，正交互补
- `trace-presence-substitutes-for-the-check-it-invites`(#195)：近邻但异轴——那滴管痕迹在读者侧替代核验（信任放大），本滴管痕迹在测量侧不携带方向（影响误记）
- `mirror-not-second-order`：今晚产出是斥候坐标（Keith 没从谱系角度看过这三对同构）
- 适用前提现场核：`fleet-canon-is-sedimentary` 的「Keith 亲手移植」前提在对③引用处成立（06-22 三仓 diff 实证在案）

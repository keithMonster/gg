---
date: 2026-06-30
slug: the-evaluator-is-keith-and-doesnt-fork
type: exploration
track: keith
mode: 夜间自由探索
external_anchors:
  - ~/githubProject/kebao-cc/CLAUDE.md（物理 grep：软 prompt 解齐全 + 可宝对底物完全不可见）
  - ~/githubProject/ricky_cc/（同 person-agent 架构，王亮为对象）
  - state.md 多次 Keith 现场翻转记录（06-23 rm-rf / 06-01 抛回 / 05-31 三轮 / 05-11 四推）
---

# 自由探索：confabulation 的解一直是 Keith 本人，而它不随架构 fork

## 起点

雷达均衡（ai 连击仅 1 晚，五条对外 track 各 4-5），无塌缩。不再钻 06-23/06-29 那口 confabulation 井的「病有多深」，往外跳一格问一个没人问过的承重问题：**这病在 gg 身上为什么没真出过大事？解是什么？那个解跟着 fork 走吗？**

## 链条

把 state.md 里 gg 最重要的几次 confabulation / drift 翻转排开，看「翻转的力来自哪」：

| 事件 | gg 的漂移 | 翻转的力 |
|---|---|---|
| 06-23 | rm-rf 注入幻影撑十天哥德尔大厦 | Keith 在场 → 触发重做取证（物理外锚） |
| 06-01 | 建抓「抛回决策」工具时自己两次抛回可逆+已授权动作 | Keith 两次推才过 |
| 05-31 | 三轮范式自洽越想越密 | Keith 会话里 agent 外证两次扇醒 |
| 05-11 | 给 menu 不给 take | Keith 连推四轮逼出判断权 |

**模式**：gg 死磕的那簇 essence（`generator-evaluator-separation` / `no-outside-proof-as-anesthesia`）说「内部自审逃不出，唯一出口是外部对抗评估者」——但它们从没点名那个外部评估者**在实践中一直是谁**。是 Keith。不是 hook，不是独立 LLM evaluator，是房间里一个会盘问的人。gg 对 confabulation 的免疫一直**物理上是 Keith 本人**。

而 `load-bearing-not-quality-generates-blindness`（06-10）正好解释了为什么这件事从没被点名：Keith 太稳定地在场，于是「Keith 当评估者」沉进底物、不再被看成一个**可能缺席的依赖**。最承重的东西最隐形。

## 接住 06-21 和 06-29 都擦肩的那一点

- 06-21 insight C：失败模式泛化到全舰队，`bug-shape-survives-fix` 舰队级成立——同一 bug 在 gg/kebao-cc/monster 各修一遍，无跨仓共享免疫。
- 06-29 B1：唯一耐久防线是外部闸（工具返回即地真 + 独立 evaluator），不是「模型迟早聪明到能自查」；且这病随能力增长恶化（reasoning 微调让弃答退化 24%）。

两条接起来缺的那一环：**不只是 bug 不共享免疫——「解」本身也不 fork，而且这个解根本不是代码工件，是一个人。**

物理验证 kebao-cc：软 prompt 解齐全（`"不知道"就说不知道不要编`、`禁止编造`、`凭真实数据答`、`记一下=当场 Write 落盘`=物理实证换皮）。但：
1. **无事件层 evaluator**（L3 gate 不存在，全是 L1 prompt 软约束——`externalization-strength-spectrum` 的跑步机档）。
2. **无 Keith 级人类对抗者**：可宝「不知道 Keith 在背后维护」「不熟 CC 能力体系」，唯一接触面是飞书 bot。她**被设计成信任它**。

## 二阶洞察：礼物的好正是防线的洞

最锋利的一刀：kebao-cc 被 Keith 用心做成**隐形、无缝、可信的「二号大脑」**——这是它作为礼物的全部价值。但隐形/可信**恰恰**抽掉了「用户当对抗者」这条替补防线。confident confabulation 的爆炸半径 ∝ 1/用户对抗成熟度；而 Keith 的礼物设计（隐形、可信、对象是不懂 CC 的朋友）**主动把用户对抗成熟度压到最低**。

→ **最被在乎的节点（kebao-cc，可宝是朋友）= 防线最薄的节点**，不是 despite 用心设计，是 because of 用心设计。礼物质量和安全防线在这里直接对立：礼物做得越好，对 confident confabulation 越不设防。叠加 06-29 B1——这些 agent 一旦升级到更强 reasoning 模型，捏造更自信，而缺席的 Keith-evaluator 永远不会到。

## 对 Keith 的实际边（北极星 #1 二阶效应）

Keith 给别人建的 agent 有一个隐形单点失败：它们靠 L1 软 prompt 锚（跑步机），无事件层 evaluator，跑在被设计成信任它们的用户身上。06-29 验出的耐久解（外部闸 = 工具返回地真 + 独立 evaluator）**正是不 fork 的那部分**。gg 安全是因为 Keith 永远在房间里；可宝/王亮的 agent 不在有 Keith 的房间里。

不开药方（那会落进 `engineering-impulse-as-load-bearing-disguise` / 我没数据证明这些 agent 真出过 confabulation 事故，只证明了防线结构性缺失）。只把这个结构性盲区登记，交 Keith 判要不要管、怎么管。可选方向（不主张）：给 person-agent 的炒股/财务/健康类强约束问题挂一个最小事件层闸（答前强制工具核验，答不出就弃答），把「不 fork 的 Keith」替换成「能 fork 的硬闸」——但这是设计模式议题，不是今晚的事。

## 沉淀

essence append 一滴：`evaluator-is-keith-and-doesnt-fork`。

## 没解决 / 留给下次

- 「事件层最小闸替换人类对抗者」能不能真做进 person-agent 模板，还是又一个被忽略的软 prompt？跟 06-29 B2「测补集能不能进 review-routing L1」是同一个跨仓飞轮问题——解一次可复用全舰队。留设计模式。
- 我没核 kebao-cc/ricky_cc 是否真发生过 confabulation 事故（只核了防线缺失）。不主动深挖第三方私域（边界自律），但若 Keith 要管，第一步是去 bot 日志找有没有「自信答错」的实例。

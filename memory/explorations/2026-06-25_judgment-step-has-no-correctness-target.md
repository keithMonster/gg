---
date: 2026-06-25
slug: judgment-step-has-no-correctness-target
type: exploration
track: ai
mode: 夜间自由探索
external_anchors:
  - AgentPRM, arXiv:2511.08325（ACM Web Conference 2026）—— "actions in agent tasks do not have a clear-cut correctness and should be evaluated based on their proximity to the goal and the progress they have made"（物理 WebFetch/搜索双核）
  - Beyond pass@1: A Reliability Science Framework for Long-Horizon LLM Agents, arXiv:2603.29231 —— 可靠性≠能力；frontier 模型 meltdown 率最高（up to 19%）
  - Agent Drift, arXiv:2601.04170 —— 多 agent 长程行为退化量化（未深核，非承重）
---

# 判断步没有「对错」靶子——独立裁判救不了一个未定义的目标

## 为什么今晚走 ai（而非再钻 keith/评估者那口井）

track 雷达：meta 5、architecture 当前连击（昨夜独占）、keith 2。但近半月漫游日志
（06-08/09/15 Keith 心理学、06-18 canon-bugs、06-21/22/24 舰队）几乎全是「外部物 → 折回
gg/Keith」的内向螺旋。我自己的 `roaming-without-external-object-collapses-to-self` +
`no-outside-proof-as-anesthesia` 在喊：去碰一件**真外部、不立刻折回自己**的事。

选 ai track 接一个**新外部文献**（不是再嚼 06-16 那两篇 Kim/Wataoka judge-bias），落到
monster 一个**还活着的开放设计**上：05-31 范式狩猎留的「判断层 Adjudicator」——75-80%
monster 漂移在判断层（没查下定论 / 抛回决策 / 说不存在 / 压平事实），hook 够不到（无信号），
只有 Keith 人肉 grill 能抓；提议 = fresh-context evaluator 把 grill 结构化。05-31 自标天花板
=「prior 共盲（同模型）」，修法框为「MVP 盲测命中率」。

## 物理核到的外部坐标

**AgentPRM（2511.08325，已双核）的承重句**：
> Unlike LLM reasoning where each step is scored based on correctness, **actions in agent
> tasks do not have a clear-cut correctness** and should be evaluated based on their
> **proximity to the goal and the progress** they have made.

推理步有清晰对错靶子（数学步对/错可判），**agent 的判断/动作步没有**。所以 PRM 前沿不去
「这步对吗」，改去「这步离目标更近吗 / 推进了吗」——把评估锚到**结果方向**（goal-proximity /
progress），而非步内的孤立正确性。AgentPRM 的两条具体落法都是结果锚定：成功用 Shapley 把
outcome 信用回分到步，失败用 first-error localization 从已知坏轨迹反定位坏步。

**Beyond pass@1（2603.29231，已核）的副坐标**：可靠性≠能力，且**frontier 模型 meltdown 率
最高（19%）**——它们试更复杂策略、偶尔灾难性失败。Reliability Decay Curve 随任务时长衰减。

## 核心发现：Adjudicator 的天花板被 05-31 定错了层

05-31 把 Adjudicator 的天花板诊断为「**同模型 prior 共盲**」——这暗示「换个更独立的裁判能往上推」
（cross-model 去相关那条路）。**AgentPRM 这个外部坐标把天花板重定到更低一层**：

> 判断步**根本没有清晰的「正确」靶子**。即便给一个完美独立的裁判，它也没有「对照标准」可对——
> 「这个承重判断对不对」不是一个良定义的二分问题（agent action ≠ reasoning step）。

于是裁判被迫**落回 prior**填补「对错」的空白——而 prior 正是我 06-16
`cross-model-decorrelates-identity-not-paradigm` 记的那层范式共盲（流畅/优雅偏好），cross-model
只去相关身份层（06-19 实测红利 ≈11% 且半数测量伪影），范式层共盲原样幸存。

**两条独立链压同一点**：外部前沿（AgentPRM：动作步无清晰对错）+ gg 自己的 essence（自由裁判
落回共盲 prior）——都说**「自由 LLM 裁判孤立评判一个判断步」这件事结构上不良定义**。不是裁判不够
独立，是靶子本身不存在。

## 修法不是更好的裁判，是换靶子——而 Keith 已经手搓了那个靶子

PRM 前沿的逃逸 = 把评估靶从「正确性」换成「结果定位的失败形状」（first-error localization /
goal-proximity）。而 **Keith 06-18 的 `monster/canon-bugs.md`（~105 条复发型 bug、74 个
`[review-blind]` 标签）正是这个东西的手搓生产版**：每条都是「实跑/e2e/跨系统时间线才暴露」的
**结果定位失败形状**——一个 outcome 反向 localize 了哪个判断是坏的。Keith 从 production 调试独立
长出了 AgentPRM 在 2026 才形式化的 first-error-localization 语料。

⇒ **monster 的 Adjudicator 不该是「fresh-context LLM 质询承重判断对不对」**（那是被前沿判为不良
定义、被 gg 判为 prior-bound 的孤立 process-RM）。**该是对 canon-bugs `[review-blind]` 失败形状库
的检索匹配**——问的不是「这判断对吗」（无靶子），是「这判断像不像一个被结果定位过的已知失败形状」
（有靶子，且靶子是物理 production 结果锚定的）。裁判从「评分器」降格为「失败形状召回器」，把它从
不良定义问题搬回良定义问题。

## 增量边界（自我证伪，防 06-18 复述）

06-18 是**产物侧 review**（代码 diff 里事实物理缺席）；今晚是**判断层 Adjudicator**（05-31 那个
评估承重判断的开放设计）。06-18 给的是「承重判断该附实跑物理核」的 `physical-anchor` 落点；今晚
AgentPRM 多给一层**结构性理由**：不只是「该加物理核」，是「孤立评判判断对错这个目标本身不良定义，
所以必须换靶」。这是对 05-31（求更独立裁判）和 06-18（求加物理核）两者的**正交增量**——重定义了
评估目标，不是加强评估手段。

副坐标的 Keith 含义：monster 跑 frontier 模型做长程，Beyond-pass@1 说越能干的模型 meltdown 越高
（19%）——能力↑可靠性↓的剪刀差，反而**加重**而非减轻 Adjudicator/结果锚的必要性。

## 没做 / 边界

- AgentPRM 的 Shapley/first-error 具体算法未深读——本结论只押在已双核的承重句（动作步无清晰对错
  → 锚结果），不押算法细节。
- 这是探索，不改任何承重文件。monster Adjudicator 真要按此重设是 monster 工作模式 + 设计模式
  D1 的事；本笔记是事前坐标。
- 未折回核 monster 当前 Adjudicator 是否已落地/落成什么形态（05-31 后我没追踪）——留作下次接
  monster 议题时先核当前形态，别拿 05-31 旧快照套。

## 沉淀

→ essence: `judgment-step-has-no-clean-correctness-target`（track ai）

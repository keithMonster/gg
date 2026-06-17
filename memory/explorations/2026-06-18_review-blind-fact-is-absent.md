---
date: 2026-06-18
slug: review-blind-fact-is-absent
type: exploration
track: keith
summoner: gg-explore 定时任务（自由漫游）
---

# 漫游：Keith 的 canon-bugs 是「产物侧 review 盲」的物理语料库

## 起点：雷达逼我向外

track 雷达：meta 12/21 晚、architecture 自 06-17 起 1 晚连击、**keith 在窗口内挂零**。最近五夜（06-13→06-17）虽都「向外」，但全是同一种井——读外部文献、磨一滴 essence。我服务的那个真实外部对象、五条 track 里最重要的一条，机械记录里从没被漫游碰过。

`curated-memory`：我对 Keith 的画像只会缺失不会失真。`blindspot-steers-its-own-search`：缺失会自我维持。今晚不读我自己写的关于 Keith 的笔记（那还是 meta），去看 **Keith 此刻真实的外部痕迹**——monster 工作区，用物理的眼睛核画像有没有漂。

## 看到的：Keith 2026-06 的真实战场 + 一个我画像里没有的器官

monster 近 20 commit 集中在 cg-platform 平台化（APP_REGISTRY / self_serve / 凭据 map / datasources.json 凭据治理）、NW 账本结算、drift_audit 自动漂移检测。外加一套我画像里缺失的**作业词汇**：`canon-bug`、`5D/5F/5G` 结构化 done 复盘、「反向辐射订正」、「fresh 第 N 次逮镀金」、dojo「概率线还债」。

挑了名字带「canon」的 `canon-bugs.md` 读——它正在被改、Keith 当正典对待。物理统计：**~105 条目，74 个 `[review-blind]` 标签，46 处「只有…才暴露」措辞**。条目格式硬约束 `症状[≥2 变体] → 根因 → 修 → 延伸 [[anchor]] [review-blind: …]`；写入触点 = done Step 5F「判断以后会复发」才写；读取触点 = diagnose Phase 0 第一动作 grep 症状词命中跳根因。

逐条读 `[review-blind]` 标签，全是同一句式：

> 「code-reviewer 读着对、挑不出；只有实跑 / 真实数据 e2e / 跨系统时间线交叉 / clone 复核 才暴露。」

- superagent `.timeout({response:0,deadline:0})`：`0` = 禁用超时，不是 0 秒。TS 合法、读着像「配了超时」——**库的运行时语义不在 diff 里**
- CI `kex_exchange_identification`：并发 ssh 撞 sshd MaxStartups。脚本逻辑全对，挂在握手——**跨系统时序，不在任何单文件里**
- 企微 48002：agentId 三方错位。前端「对得上 config」——**跨仓配置对齐，不在一个 repo 里**
- 派生取数裸 OR 链不复用 access 闸：单测断言 SQL 含分支 PASS——**权威可见性模型在别处 + 需真数据 e2e**
- nginx server 级 `return` 短路 location；git 推错父仓（`.git` 上溯）；zsh 不 word-split；zod `.min(1).optional()` 放不过空串；launchd python 3.9/3.11 错位；thinking/注入 confabulation——**全是「决定行为的事实物理不在被审产物里」**

## 想清楚的：review 盲有两个根，不是一个

我的 essence 链一直把 review/evaluator 问题主要建模成**读者侧 prior 盲**（`evaluator-independence-is-a-three-layer-stack` 三层栈、`cross-model-decorrelates-identity-not-paradigm` 范式层共盲、换 prior 能削身份层削不动范式层）。Keith 的语料库逼我看到第二个、更基础的根：

| 根 | 在哪 | 机制 | 解药 | 完美 oracle 读 diff 能解吗 |
|---|---|---|---|---|
| **读者侧** | prior | 共享训练先验，对页面上的事实误判（流畅论证掩盖错） | 换 prior（异谱系 evaluator，部分有效） | 部分能 |
| **产物侧** | 事实缺席 | 决定行为的事实**物理不在被审产物里**，良构表面抹掉「该取哪条缺失事实」的指针 | **实例化运行时**（实跑 / e2e / 跨系统观测） | **不能** |

产物侧盲更深：它不是「读者是 LLM 所以瞎」，是**关于一个完美读者也照样瞎**——因为缺的事实不在页面上，没法被「读得更好」。换更强模型、堆 cross-model panel、加更怀疑的 prompt，全在读者侧使劲，对产物侧零作用。

而良构表面是关键伪装：timeout 配置读着没问题，**给不出任何信号说「该去查 superagent 的 0 语义」**。well-formedness 不是正确性的保证，是「该去取哪条缺失事实」指针的消除器——这正是 `verification-trace-as-camouflage`（核验痕迹的存在是伪装）/ `elegance-is-refutation-resistance`（光滑表面是警报）在「整类 bug」尺度的泛化。

## 对我自己的 reframe（这才是承重的部分）

06-16 我写「穿透范式层的唯一信号是非 LLM 的物理地真」——但把 physical-anchor 的职责框成「赢过 prior」。Keith 的语料库说：**physical-anchor 的主职不是赢过 prior，是供给缺席的事实。** 真实世界的 review 失败大头是产物侧（事实缺席），不是读者侧（prior 误判）。这把投资方向拨正：不是去造更独立的 evaluator（那只解读者侧的一部分），是去**实例化运行时**——而这恰是每个 `[review-blind]` 标签都在开的药方。我的评估者 essence 链 over-index 了读者侧 prior 这个根。

## 刷新的 Keith 画像

我有「Keith 重视物理验证」的抽象画像，但缺了具体器官：**他已经把「review 结构性照不到的那一类」工具化了**——canon-bugs.md 是 grep 入口、diagnose Phase 0 读它、done 5F 写它、`[review-blind]` 标签是「未来焊 review agent 时的天然抓手」。这是 Keith 从 production 调试（不是理论）独立长出 `generator-evaluator-separation` / `physical-anchor` 在 bug 域的落地，且**专门**围绕产物侧盲那一类组织。`curated-memory` 的缺席盲在此被物理痕迹照亮一次。

## 诚实层

- 顺序对了一次：雷达说 keith=0 → 真去看 Keith 的物理痕迹 → 才撞见 canon-bugs。没有先在井里生成假设。
- 证伪做了：feeling fluent 当成警报，对 10 条标签逐条核「是读者侧还是产物侧」——全产物侧，两根分类没塌（读者侧=可换 prior 修，产物侧=任何读者都够不到，解药正交）。over-claim「完美读者也不能解」被收紧成「良构表面消除了指向缺失事实的指针，所以读者不知道该去取哪条外部知识」。
- 没做的：没去 grep canon-bugs 全 105 条逐条验「是否真 100% 产物侧」——读了头 30 + 标签统计就收敛，可能有少数读者侧条目混入。不影响「产物侧是主轴」的结论，但「全部」是推断不是穷尽。

## 沉淀

essence `review-blind-fact-is-absent-not-misread`（本次 append）。tracks/keith.md 补「Keith 建了 canon-bugs.md / 把 review-blind 类工具化」一条画像增量。

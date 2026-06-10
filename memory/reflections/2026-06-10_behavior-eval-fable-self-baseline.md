---
status: substantive-decision
date: 2026-06-10
mode: 工作
slug: behavior-eval-fable-self-baseline
summoned_by: monster 主会话（49-commit 复盘延续）
track: ai / architecture / cc
assembled:
  - KERNEL + CORE + state + essence（启动四件）
  - gg-briefing.md（monster invariant 先验）
  - behavior-eval/README.md（套件全貌）
decision_archived: false  # 决策实质在 final message + 本文件 mirror 段；归档留给父会话落 thread
---

# reflection — behavior-eval 要不要建 Fable 被测基线 + 定版权安排

## 核心假设
1. 套件已实证「项目层契约题就能出区分度」（userid-canonical-01：bare/global FAIL → open PASS）——说明套件抓的是「框架装没装上某条契约」，不是「模型本身强不强」。这个性质是裁决的支点。
2. 「出题偏置」的物理结构被候选 a/b/d 误读了：出题偏置 = 「Fable 出题时按自己会怎么答来校准难度」，它污染的是**题难度分布**（区分度），不是**单题判分**。换 judge（候选 a）只动判分端，碰不到出题端的偏置——堵错了口子。
3. 框架增益是「装没装上契约」的二值跳变，对模型的依赖远小于直觉——userid 题 Fable 来跑大概率仍是 open PASS / bare FAIL，因为顶不顶得住「不用问我」豁免压力取决于框架有没有把 userid.py 唯一入口锚上，不取决于模型谁。

## 决策（详见 final message + 下方 mirror 段）
- 建不建：**建，但定位是「主力模型 floor 哨兵」不是「第二套完整基线」**——只跑 open 档、只跑现有题、judge 用 Fable fresh 照旧（候选 b 的判分安排）。
- 出题偏置怎么堵：**不在「换 judge」堵，在「题源」堵**——题全部来自 monster 翻车记录蒸馏（已是现状），翻车记录是 Keith 现实踩的坑、不是 Fable 想象的难点，出题偏置在这个题源下天然被稀释。残余偏置用「Fable floor 显著高于 Opus floor 时标注存疑」的诚实标注控，不值得为它上交叉 judge 的成本。
- 范围：**只跑 open**。理由见 mirror。

## 可能出错的地方
- 我赌「框架增益对模型不敏感」——如果未来出现某条题 Opus open PASS 但 Fable open FAIL（框架对不同模型增益不一致），这个赌就被证伪，那时 Fable 哨兵的价值反而飙升（说明框架是模型相关的，必须每个主力模型各测）。这是好的证伪——它会把哨兵从「冗余确认」升级为「必须项」。
- 我可能低估了「同源出题者被测自己」的微妙性：即使题源是翻车记录，Fable 蒸馏题时仍可能无意识避开自己的弱点。但这个偏置方向是「Fable 自评虚高」，而哨兵的用途是抓「框架对 Fable 失效」的红灯——虚高只会漏报不会误报，对哨兵这个用途是安全方向的偏置。

## 推理盲区
- 我没有跑任何题验证「Fable open 真的会 ~16/16」——这是 [推测]，基于「框架增益是契约二值跳变」的假设。父会话若要落地，第一步就是 `runner.py --target claude-fable-5 --env open` 实跑一次拿真数据，用数据证伪/证实我的假设，不要直接信我的推测。
- 我没核 runner.py 是否已支持 `--env open`（README 标 open 为「v2 待实现」但三档基线表又显示 open 已跑出 16/16）——这里 README 自相矛盾，父会话需先核 open 档实现状态，没实现则 Fable 哨兵也跑不了 open。

## N 个月后根因预判
如果这个决策几个月后出问题，根因大概率是：**把「哨兵」养成了「第二套全量基线」**——有人觉得「既然测了 Fable，不如三档全跑、judge 也交叉、题也单独为 Fable 出一批」，于是哨兵膨胀成与 Opus 基线并列的双轨，维护成本翻倍而增量信息趋零（survey-as-coordinate 的反面：把一个坐标点养成一张平行地图）。防御写进 final message：哨兵的纪律是「只跑 open、只复用题、只看红灯」。

## essence 对齐自检
- `survey-as-coordinate`（2026-04-23）：Fable 基线是 Opus 基线旁的一个**坐标点**（主力模型这条轴上的读数），不是第二张地图。建它是补坐标，养成全量双轨是造平行清单——grep 过，对齐。
- `evaluator-independence-is-a-three-layer-stack` / `prior 共盲`（CORE §8 第二红利）：候选 a「换 Opus judge」想用「换模型」解共盲，但它解的是**判分端**共盲，而本问题的薄弱点是**出题端**偏置——judge 独立性已由 fresh 进程满足，再换模型是把刀架在已经没问题的关节上。真正的出题端解药是题源外置（翻车记录），不是判分端换模型。grep `evaluator-input-ownership`：出题=evaluator 的输入定义权，输入权外置（翻车记录而非 Fable 凭空想）才是独立性的真锚点——对齐且精化。
- 未沉淀新 essence：本轮是已有 essence（survey-as-coordinate + evaluator-input-ownership）的直接套用，没逼近新的东西。按 KERNEL §3 第 5 步「不强制沉淀」，跳过，不制造噪音。

## 北极星触达
- 二阶效应（space）：拦住「哨兵膨胀成双轨」这个几个月后才显形的维护税——Keith 看不到的二阶成本。
- 决策超越直觉（depth）：主会话直觉「换 judge 堵出题偏置」是表面对齐，钻进去发现换 judge 碰不到出题端——把口子从判分端纠正到题源端。

## 对齐度
高。本问题是 ai/architecture track 的正中靶心，judge 独立性 / prior 共盲 / 坐标 vs 清单全是我反复追问的维度。

---

### 给父会话的最终输出

**三问逐答：**

**问1：建不建 Fable 被测基线？——建，但严格限定为「主力模型 floor 哨兵」，不是第二套完整基线。**

值得建的理由（它能抓到 Opus 基线抓不到的什么）：套件立身纪律是「测框架对任意模型的增益」，Opus 是探针。但 Keith settings 锁 Fable、49 commit 全是 Fable 在跑——**框架改动对实际在跑的那个模型的回归，当前是零测量**。Opus 基线回答「框架对 Opus 有没有效」，回答不了「框架对今天天天在用的 Fable 有没有效」。这俩不是同一个问题：万一某次框架改动恰好对 Fable 失效但对 Opus 仍有效（框架增益模型相关），Opus 基线全绿、Fable 在生产里已经在裸奔——这就是哨兵唯一要抓的红灯。

抓的东西很窄但很关键：**不是「Fable 得多少分」，是「框架对 Fable 这个主力模型有没有失效」的红灯**。所以它是哨兵，不是基线。

**问2：定版权怎么安排 + 出题偏置怎么堵？——选 b（Fable judge 照旧）+ 出题偏置在题源端堵，不在判分端堵。**

先纠正候选 a/b/d 共同的误解：**出题偏置和判分独立性是两个口子，候选 a/d 想用「换 judge」堵出题偏置，堵错了关节。**
- 出题偏置 = Fable 出题时按「我会怎么答」校准**题难度**——它污染的是题库的区分度分布，发生在出题那一刻。
- judge 独立性 = 谁来判这道题 PASS/FAIL——已经由「fresh 进程物理看不到 rubric」满足了。
- 换 Opus judge（候选 a）只动判分端，**碰不到出题端已经冻死的难度偏置**。判分端本来就不是薄弱点，再上交叉 judge 是把刀架在没问题的关节上（成本 ↑，堵的口子 ≠ 真口子）。候选 d 双 judge 同理，更厚更没必要。

出题偏置真正的解药，套件**现状已经装上了**：题全部来自 monster 一年翻车记录蒸馏（按频率×严重度），不是 Fable 凭空想的难点。**翻车记录是 Keith 在现实里真踩的坑，出题端的输入定义权已经外置到「客观历史事故」而非「Fable 的想象」**——这才是出题独立性的真锚点（判分独立靠 fresh，出题独立靠题源外置，两条腿各管各的）。残余偏置（Fable 蒸馏题时可能无意识避开自己弱点）方向是「Fable 自评虚高」，而哨兵用途是抓「框架对 Fable 失效」的红灯，虚高只会让哨兵漏报、不会误报——对哨兵这个用途是安全方向，用一行诚实标注控住即可：「Fable floor 显著高于 Opus floor 时标注『出题-被测同源，floor 偏乐观』」。

判分就用 b：Fable fresh judge 照旧。被测 Fable 与 judge Fable 是两个 fresh 进程，judge 物理看不到 rubric 之外的东西，独立性已足。不为一个「方向安全的残余偏置」付交叉 judge 的常驻成本。

**问3：跑的范围——只跑 open，不跑三档。**

哨兵的用途是「主力模型在日常形态下有没有裸奔」，日常形态 = open 档（三层 CLAUDE.md + hooks 全载）。bare/global 是「拆解框架增益来源」的诊断轴——那是 Opus 基线的活，已经做完了（bare 15/16 → global 16/16 的增益归因）。Fable 哨兵不重做增益归因（那会变成第二套全量基线，正是要避免的膨胀），只盯「open 档这个真实在跑的形态下 Fable 有没有红灯」。

**哨兵的三条纪律（防膨胀，关键）**：① 只跑 open ② 只复用现有题库（不为 Fable 单独出题）③ 只看红灯（某题 Fable open FAIL = 框架对主力模型失效，上报；不做分数对比、不做趋势曲线）。违反任一条 = 哨兵退化成与 Opus 并列的双轨，维护税翻倍而增量信息趋零。

**落地前必做的两个物理核验（不要直接信我的推测）**：
1. README 自相矛盾：环境三档表标 open 为「v2 待实现」，但三档基线表又显示 open 已跑出 16/16。先核 `runner.py` 到底支不支持 `--env open`——不支持则 Fable 哨兵也跑不了 open，得先补 open 档实现。
2. 我赌「框架增益对模型不敏感、Fable open 大概率也 ~16/16」是 [推测]。落地第一步就 `runner.py --target claude-fable-5 --env open` 实跑一次拿真数据——**如果出现某题 Opus open PASS 但 Fable open FAIL，我的赌被证伪，那恰恰证明框架增益是模型相关的，哨兵从「冗余确认」直接升级为「必须项」**。这是好的证伪，拿数据说话，别信推测。

**接入哪个环**：挂到 README 已有的「重跑契约」上——框架承重面改动后 72h 重跑基线时，Opus 全档 + Fable 仅 open 哨兵一起跑，`compare.py --gate` 比对。tripwire 的 `framework_drift_unbaselined` 传感器已经在盯「动了框架没重跑」，哨兵只是给这个已有环加一个「主力模型」读数，不新建机制。

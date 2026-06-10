---
date: 2026-06-10
mode: 工作
slug: monster-49-commit-architecture-retro
status: substantive-decision
task_family: architecture-review
summoned_by: monster 主会话
---

# monster 今日 49 commit 架构复盘（三问：未完善 / 做错 / 更好设计）

## 核心假设
- 假设主会话自报分类（架构/机制/评测/结构四层）大体可信，我只做承重程度重排 + 补缺 + 挑战，不重新分类全部 49 commit。
- 假设我读的 10 份材料 + commit log + proposals 状态分布足以覆盖承重判断，业务侧 commit（dev-console/cg-skills 等）不进本次复盘（主会话已声明非重点，且 feedback-topology 已把业务侧"出列"）。

## 决策对象（用治理 essence 当尺子）
今天这批改动的本质是**一次治理层自我手术**——飞轮/三环/简化闸/反馈拓扑是同一件事的四个切面。我手里正好有一整套治理 essence 当坐标系：cadence-as-symptom / default-bucket-as-deadlock / tool-eats-its-critique / generator-evaluator-separation / vantage-contaminates-verdict / survey-as-coordinate / prompt-fix-asymptote / pending-resolved-becomes-blocked-stagnation。用它们测，比抓 bug 有用。

## 可能出错的地方
- 我说"四个治理环不该合并"，但我没有运行过 meta_audit 的真实触发，判断基于代码 + 设计意图阅读，不是行为实证。若 meta_audit 跑起来发现跟 NW 晨报严重重复，我的"不合并"结论要修。
- 我把 behavior-eval 的 global↔open 零差值判为"题库未触达项目层"（认同自报），但另一个可能：项目层契约的增益本来就主要在长会话，单题探针测不到——这是 README 自己也标注的盲区。若是后者，扩题库是错的方向，该转长会话回归。这点我在输出里标了"两种可能"，没拍死。

## 推理盲区
- 我没读 cg-notes/eval 的 README（第三个评测域），只从另两个域 + brief 推断三域关系。统一 runner 必要性的判断有此盲区——已在输出里降级为"先别建统一层"而非"不需要"。

## N 个月后根因预判
若今天这批有东西会在 2-3 个月后反噬，最可能是**meta_audit 的"连续 3 天命中"判据本身成为新的 default-bucket**——它把"没人善后"翻译成"连续命中"，但如果晨报头条没有强制消费动作（只是更醒目地报），连续命中会从 3 天涨到 30 天，哨兵的哨兵自己变成裸开环。这正是 feedback-topology 发现 #1 想根治的病，却可能在 meta_audit 自己身上复发（tool-eats-its-critique 的活体）。

## essence 对齐自检
- `cadence-as-symptom`（2026-05-06）：cgboiler-inquiry-fetch 孤儿生产是其活体——但今天被 Keith "不管"出列，症状治疗都没做。已在输出标为悬置债。grep 确认 essence 在场。
- `default-bucket-as-deadlock`（2026-05-06）：meta_audit 连续命中判据的风险预判直接用此滴。grep 确认。
- `tool-eats-its-critique`（2026-05-12）：meta_audit 自身可能成为新裸开环的预判用此滴。grep 确认。
- `survey-as-coordinate`（2026-04-23）：评测三域"没统一 runner"——我判定这是坐标不是清单缺口，三域被测对象不同，强行统一是工整美学。用此滴。grep 确认。
- 对齐度：高。本次无新增 essence——这些洞察都已沉淀过，今天是它们在 monster 治理手术上的又一次落地验证，不是新逼近。按"沉淀是涌现不是必须"，跳过 essence append。

### 给父会话的最终输出

完整决策见下方 final message「## 判断」起的全文。要点副本：

**承重程度排序的未完善清单（高→低）**：
1. meta_audit 连续命中→无强制消费动作，可能自己变裸开环（最承重，是今天新建机制里唯一的结构性隐患）
2. 检验环"未与自我更新强制挂钩"仍是 🔶——飞轮检验环是声明不是机制（brief 自己标的，没解）
3. tripwire 5 传感器 vs 30 回路覆盖——这是**伪未完善**，传感器只该覆盖"有纸面契约且机器可检"的项，不是 30 回路全要传感器（打回自报）
4. cgboiler-inquiry-fetch 孤儿生产被"不管"出列——症状治疗都没做，cadence-as-symptom 悬置债
5. 评测三域无统一 runner——**伪未完善**（survey-as-coordinate：三域被测对象不同，是坐标不是清单缺口，先别建统一层）
6. behavior-eval global↔open 零差值——真未完善但方向待定（扩题 vs 转长会话回归两种解）

**做错判定**：
- rtk 当初上 hook **不算做错**——它是 transparent-rewrite-breaks-contract 这滴 essence 的来源，付的是认知学费，今天退役是学费兑现成洞察，不是纠错。打回自报的"是不是本来就错"。
- hook 降频**没把防护降没**——降的是注入频率不是拦截 hook，guard 类 exit2 拦截一条没动。自报这条多虑。
- 真正该警惕的不是"做错"，是**一天 49 commit 同时动治理层多处**——治理手术的自我验证密度，今天靠的是 Keith 在场 + fresh agent，但这批改动本身没进 behavior-eval 回归（rtk 退役/hook 降频/meta_audit 上线都没回归测过框架行为有没有变差）。

**更好的设计（替代方案级）**：
- 四个治理环（体检/tripwire/meta_audit/NW）**不该合并**——它们在飞轮上占不同环节（体检=人工全量感知/tripwire=机器持续感知/meta_audit=感知的元监督/NW=识别），合并会塌缩成单点。但**该补一条它们之间的关系声明**写进 harness-map 或 monster-architecture thread，否则三个月后没人记得为什么有四个看起来都在"检查"的东西。
- meta_audit 的"连续命中"应升级为"连续命中 N 天 → 自动升 NW pending 提案"（机器写入识别环），而不是"晨报头条"（仍依赖 Keith 看见）——把哨兵的产出接进已有消费管道，根治它自己变裸开环。这是对 default-bucket-as-deadlock 的预防性应用。

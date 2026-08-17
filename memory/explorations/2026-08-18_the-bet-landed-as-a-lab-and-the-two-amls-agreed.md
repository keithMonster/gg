---
date: 2026-08-18
slug: the-bet-landed-as-a-lab-and-the-two-amls-agreed
type: exploration
track: keith
trigger: launchd com.gg.gg-explore 00:13
---

# 赌注落成了实验室，两个 AML 在同一周说了同一句话

雷达显示 ai 连击 2 晚、窗口内 ai 6 次最高而 keith 只有 2 次——且看守者系列（08-10→08-17）已在 #207 收整。今晚跳出 ai 井，去看真实的 Keith：物理读 monster 近三周（08-01→08-17）的 git log + threads + model-lab 工作区。**gg 的 Keith 画像滞后了一个月**：以下三条主战场事实，keith track / working_context / ai track 全部零记录（grep 亲核，exit 1）。

## 一、五年赌注第一次落成物理工程（DQ-3 答案更新）

**2026-08-17，Keith 开建 `monster/model-lab/`——在本机 M1 Max 上从零手搓一个 LLM，预训练→后训练全流程 12 个 Stage**（含手写 BPE、手写 Transformer、RLHF/GRPO 正式做、DPO 手写 loss 对比）。两条硬约束是 Keith 明确定的：**「步骤不缺」**（真实流程里有的环节都要有，参数量小是手段不是借口）+ **「本地必须跑得动」**（每步真跑真出结果，不能变成"原理讲了但没跑"）。

这不是孤立事件，是一条学习主线的相变：`threads/llm-foundations.md`（05-15 起）从直觉模型（提示词五层、否定双层）→ 文献锚定 + 引用纪律（07-08~07-13）→ 08-16 选定 Karpathy Deep Dive 补数据分布/采样地基 → **08-17 全流程亲手工程**。05-24 Keith 明示「5 年路线 = 技术深度」时它是宣言；现在它有了目录、有了 benchmark 表（MPS 43k tok/s、ctx 256/512 的 5 倍吞吐差是实测的）、有了 12.19M 参数的主线模型。**赌注从话变成了仓**。

一个同构细节（方向未核，只记不判）：Keith 学习契约里的三条纪律——「本地真跑」「直接引语必须查源」（07-13 纠正伪引语立）、「否定有两层效应」（07-20）——与 gg 侧的铁律 2 物理实证、入库⑤问引文核验（07-16 立）、CLAUDE.md 负面表述分层规则**逐条同构**。日期咬得很近（07-13 vs 07-16）。是谁流向谁、还是同一颗认识论长在两侧，无 transcript 级证据不硬判——但这本身是 agenda「北极星 #1 行为痕迹代理」议题的一个具体可测点位：**概念在 Keith↔gg 边界上是多孔的，且双向**。

## 二、教学换轨：Keith 把「写」外包、把「猜」留给自己（工作方式增量）

model-lab 建立当天（08-17）教学模式即换轨：**任务卡式（Keith 手写代码）→ 轨迹回放式**——AI 给完整可跑代码 + tracer 观察层打点，Keith 跑一次后在交互式播放器里逐步看数据怎么变形、**先猜后验**、改超参重跑；手写路线保留可切。

画像读法：在一个自己是新手的领域，Keith 选择把生产动作（写代码）外包给 AI，把**预测动作**（猜下一步数据长什么样）留给自己——赌的是理解锚定在 prediction 不在 production。这是 `assisted-performance-masks-the-anchors-decay`(#184) 那根轴上的一个**主动配置**数据点：不是辅助态悄悄掩盖锚衰减，是 Keith 显式选了要保的锚（先猜后验）并给退路（手写可切）。与 07-31 双载体判据（「产物尾部谁来接」编码进基础设施）同款行为模式：**把认识论参数显式拿在自己手里**。这个选型对不对，worked-examples / predict-observe-explain 文献有话说——留作未来某夜 humanity 向外核，今晚不外推。

## 三、两个 AML 在同一周从有机体两侧说了同一句话（DQ-4 + gg 研究脉络的活消费现场）

- **08-14，Keith 侧**：`AML 记忆榜单调研`（Agent Memory Leaderboard，落 `threads/ai-memory-evolution.md`）——开源榜前三**全弃写入时重结构化**，第一名是 vanilla hybrid RAG；结论「**保原件 + 检索时智能**」，与 monster L3 transcript 路线同构（ReFind arXiv:2608.12888 佐证）。
- **08-17，gg 侧**：essence #207「**账本不许判断，判官不许记忆**」——从反洗钱（另一个 AML）§5324、IDS、审计轮换三域结晶出同一分离：状态进机械账本（写入侧不解释），判断留给不持状态的判官（读取侧 fresh 结算）。

同一个分离原则，同一周，两侧落地，**互不引用**（#207 谱系注无 Keith 调研；调研档无 essence）。诚实边界：这不是完全独立收敛——monster 记忆线与 gg essence 架构自 4 月起同源共生（append-only 原件、派生索引不得成授权源、fresh 验证，本就是一颗认识论）。**真正独立的是两侧的外部佐证域**：市场榜单（哪种记忆架构在 benchmark 上活着）与制度文献（哪种监督架构在监管/审计史上活着）互不知道对方存在，却给了同一个答案——写入时解释 = 把判断焊进账本 = 错误复利（#205 的 error propagation、Self-Confirmation Trap 是同一病灶的机器域名字）。

**对 gg 的含义**：Keith 的统一记忆系统 greenfield（07-31 拍「存量零改动、新建后自用再迁」，骨架五段流水线 + `retain/recall/trace` 三动词）正走向 gg 夜间研究脉络指着的同一个方向——**#205/#206/#207 有了活的消费现场**。下次 Keith 在记忆系统的写入闸 / 判官形态 / 账本住址上做决策时，这三滴不是抽象洞察，是可直接引用的设计输入（例：写入闸缺席是全行业出货默认 #205；判官上下文喂账本输出是否重接判据漂移 #206 敞口——恰是他「检索时智能」要碰的那条线）。

## 四、附带盘点（DQ-1 广度，一段带过）

近三周 Keith 的四条并行战线：① model-lab / llm-foundations（深度赌注，见上）；② 统一记忆 greenfield + EverOS 定源 + AML 榜单（记忆基建）；③ cg-platform 机械闸门铺开——「建表设计规则从文档条款升为机械闸门（双侧同源规则表）」铺 25 仓、分支 SOP 反转 + main 服务端保护（06-24 `mechanical-gate-needs-machine-detectable-target` 的平台级操作化，方向同样未核不硬判）；④ 对同事的 ship 线（cg-runtime 谭茜资源上传、笔记发布编辑链路、token 看板、SCBC-Desk）。深度学习、记忆基建、机械治理、对人 ship——四条线没有一条是 3 月的 Keith 在做的事。

## 产物与克制

- 本档 + `tracks/keith.md` 画像补写（带源，过「源：」出处门）。
- **essence 无沉淀**：两个 AML 的收敛是 #207 的旁证不是新结晶（组合非结晶，07-24 REFUTED 同型风险自查）；教学换轨洞察 n=1 无文献核，不够格。宁缺毋滥。
- 未动 working_context / CORE / ai track——画像落点单一化，防副本蔓延（`presence-benefit-splits-replica-verdict`：keith.md 是按需 grep 的住所，够了）。

## 与既有滴的对位（写档自查）

- `assisted-performance-masks-the-anchors-decay`(#184)：§二是其「主动配置」方向数据点（+1，接 08-02/08-05 两点）。
- `the-ledger-must-not-judge-and-the-judge-must-not-remember`(#207) / #205 / #206：§三给出消费现场，不新增内容。
- `mechanical-gate-needs-machine-detectable-target`(06-24)：§四 cg-platform 铺开是平台级同构。
- `mirror-not-second-order`：今晚产出是斥候坐标（Keith 没从这个角度看过自己的三周），不是镜像复读他做了什么——判据留给他看到时裁。
- 适用前提现场核：#184 的「辅助态」前提在 §二成立（AI 真在写全部代码）；`presence-benefit-splits-replica-verdict` 的「注入面明确」前提成立（keith.md 非启动常驻、grep 按需）。

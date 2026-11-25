---
date: 2026-11-25
slug: verification-architecture-v2-review
summoner: monster（Antigravity 原生子会话；审 harness-engineering/work/verification-architecture-2026-11-25/PLAN.md）
northstar_reach: "#1 二阶效应 / #3 决策超越直觉"
status: substantive-decision
---

# Reflection: Verification Architecture v2 方案独立审查

## 给父会话的最终输出（必填）

**总裁决：修订后做。按现稿执行的话，新增机制约 2/3 被方案自己引用的那批遥测证伪或缺证据。** 方案写的是“入口缺预检、末端过载”。我按方案引的那批数据回源重算（`~/.local/state/monster-codex-gate/` 下 55 个目录，逐轮读 `turnN.result.json`），看到的是另一回事：闸门作为检测器有效，漏在出口——结论没闭合，运行就被静默放弃了，而且无人记账。

**Keith 没想到的一点**：16 次完成的 design 里，有 8 次停在 REVISE/BLOCK、带着未关闭的方案级问题就不再 resume；14 次 accept 里有 6 次停在 FAIL。meta 里没有谱系字段，分不清是放弃了还是换个新 run 重来（“换审者”）。这种放弃还会传到下游：`accept-20261124-172624` AC-07 和 `accept-20261124-164500` AC-10 判 FAIL，理由就是 design 回执仍是 REVISE。

**推翻方案诊断的已核事实**：
- C1 design 从 PASS 被降为 REVISE，3/3 例（094211/160914/172725）的触发都是 `goal_alignment.gaps` 非空，不是方案说的 local/doubts。`reconcile_design_verdict`（codex_gate.py L1082-1098）根本不读 local/doubts。gaps 的内容是真问题，例如“两个计费状态的判定顺序”“台账、手册、AC-06B 未同步”。按现稿“放宽”，等于删掉唯一抓住它们的那条检查。
- C2 accept 从 PARTIAL 被降为 FAIL，7/7 例的触发都是模型自报 `goal_achieved=false`，走到 L1054 的 hard_fail。根因是契约冲突：PARTIAL 的定义（L373）和布尔字段 goal_achieved 互相打架。
- C3 NA 并不都是外部边界。115012 的 AC-Showcase 判 NA，是回归副本里 Electron SIGABRT，属于本地环境坏了。060027 缺的是“真实模型自主执行 commander”的证据，属于核心目标没验到。直接放宽 PARTIAL，就是在核心路径上放水。
- C4 轮次是单调收敛，没有来回拉锯（例：p4→3→2→1→0）。8 次 design 最终拿到 PASS，其中 7 次在第 4–6 轮才拿到。3 轮熔断会把这 7 次全部变成 ESCALATE。
- C5 M3a 的前提不成立：11-24/25 首轮共 47 条 FAIL AC，作者在本地能机械跑出来的只有约 2 条（102534 回归 140/142；164500 lint/typecheck 退出 1）。这两次运行另有别的 FAIL，预检省下的轮次是 0。
- C6 见上文“出口泄漏”。C7 有 3 次 accept 标着 running，实际已死：last.json 0 字节，meta 停在 11-24 18:42、20:02、20:44 后再没更新。3/19 的结果静默丢失，统计时被算成“运行中”。C8 dirty_files 冲突出现在 12/14 次真实 accept 里，最多 34 处。monster 是多会话并发改主分支，这条告警常亮即噪音，同时会掩盖“验收官（workspace-write）自己改了被测代码”。[推测：两种情况各占多少未核]
- `runtime/agy.md` 写着“agy2 已软链 ~/.codex，双号一致”，但 last-message 失败到 11-25 07:11 仍在发生。这句是过期断言。

**逐项裁决**
- 立刻做：①M2a 通道修复，另加一个 finalizer：在 meta 里记 pid，`status` 判出死掉的 running 并收成 failed。②M2a 合表改成“归类”而不是“放宽”：每条 NA 必须标 `na_class∈{redline, external_unreachable, local_env_broken}`；核心 AC（默认 AC-Showcase）不得判 NA；只要有 local_env_broken 就判 FAIL；只剩 redline/external 时判 PARTIAL，并忽略 goal_achieved=false（或改成三态）；PARTIAL 单独给退出码 3。design 的 gaps 分两类：blocking 走 REVISE，carryover 自动追加进 suggested_acceptance_criteria，可以放行。回放验收先人工逐例标好期望裁决再改代码，**不以“误降级样本全部归正”为目标**：115012 和 060027 按上面的规则应当仍判 FAIL。③用出口处置取代 2 轮熔断：以非 PASS 结束时必须执行 `codex_gate.py close --run-id <id>`，逐条处置 {fixed_unverified, accepted_risk+理由, rejected+理由, escalated_keith}；新开的 run 带 `--supersedes` 记谱系；第 3 轮之后只打印“新问题 / 残留问题”轨迹作为软提示。只有 Decision Authority 三类事项上交 Keith，否则所有分歧都会挤到最稀缺的那道闸。④M4 提前，做成 `codex_gate.py stats` 子命令，不另起脚本：统计通道失败（含死 running）、逐轮轨迹、新问题与残留问题的 ID、处置分布、NA 分类、谱系。不新增定时任务。
- 修订后做：⑤M1 只保留六域表的“逆风三试 + 禁止冒充”两列。5 条公理改成指针：裸模型能再生，而且 Delivery Standard、verification thread 和结构手册 §3 里已经有了。承载点改到 codex_gate 的 design/accept prompt，运行时按路径读 GUIDE.md：调工具这一步必然发生，召回由结构保证，真正消费这张表的是验收官。技能里的指针降为辅助。表里删掉 Holdout 的耦合，加一个“其他”兜底并封顶。⑥M2c 证明卡只渲染现有字段，NA 和处置放在最上面，PASS 摘要放后面。
- 暂缓（各带 tripwire）：⑦M2b Holdout。现在卡脖子的是很难到 PASS（1/14），没看到有人在凑绿灯；accept 本来就在清单外挖出 2 个 blocker 和 17 个 major；单用户机器上 0600 权限同 uid 等于没有隔离；检出也分不清该算 Holdout 的还是 accept 本身的。触发条件：出过 ≥2 次“闸门判 PASS/PARTIAL 之后，Keith 或生产发现了一个可见 AC 在结构上表达不了的缺陷”。⑧M3a 砍掉，触发条件：stats 显示首轮机械类 FAIL 占比 >20%（样本 ≥20 次运行）。⑨M3b 先把 23 条 NA 分类。抽样里一条通知类都没有。孪生桩跑出的 PASS 一律记作 `PASS@twin`，不能直接记 PASS。改动 notify 推送路径会碰安全边界，要送审。同一类 NA 占比 ≥30% 时再建。⑩M3c 不进本方案，留在 eval-baseline/N3 的队列里。

**§5.2 判据审查**：#1 可用，但要加调用量下限（防“没人敢用所以零失败”），死 running 也计入失败。#2 ≤2.0 轮可以被熔断机械做到，也可以被验收官变松做到，属于 Goodhart；“全部归正”这个目标本身建立在误诊上。改为三项：期望裁决回放、非 PASS 出口处置率 100%、第 2 轮之后新问题的占比。#3 冷读测的是“读到了有没有用”，测不到“会不会被读到”，而且由作者打分。改为在线统计 suggested AC 里逆风项和禁冒项的覆盖率。#5 NA 降幅可以靠孪生桩 PASS 注水，只该计 NA 转成真 PASS 的部分。#6 方向反了：“Keith 少复核”正是证明卡出错时的失败形态。**缺一个结果指标：逃逸率**，即闸门给出裁决之后，Keith 或生产才发现的缺陷数。基线要现建；结构手册记过 11-13 那周 Keith 复报“没修好”约 8 次（那时闸门还没上线）。另外缺成本指标：每个任务在闸门上花的墙钟时间。

**给 Keith 必须讲透**：验证成功 = 在消费面实测 + 由独立验证者判定 + **每条没验证的项都有显式归类和去向**（不允许静默 NA，不允许静默放弃）。第三条是这次新增的理论。头一批改动全是修 bug 和出口记账，不新增层、角色或常驻字节。Holdout、孪生桩、预检这三样，等 stats 跑出数据再说。

## 核心假设
- run 目录 = 全量遥测（已核：agy 和 agy2 的 STATE_ROOT 是同一个目录，都是 55 项）。“以非 PASS 结束”算作放弃，前提是之后没有新 run 接续；正因为没有谱系，这一点核不了，所以这条事实本身就是结论之一。

## 可能出错的地方
- 第 4–6 轮的问题可能是验收官每轮放一点（drip-feed），这时适度限轮是对的。我只看了问题数，没逐个比对 ID 是新出现的还是上轮残留的。stats 要先补这一维再定。
- “47 条里约 2 条是机械类”是靠关键词加通读预览判的，中间约 5KB 被截断。

## 本次哪里思考得不够
- 没读 events.jsonl，没核实里面有没有文件写入事件可以拿来做 C8 的归因。没核 launcher 失败的根因，只指出了 runtime 断言过期。

## 如果 N 个月后证明决策错了，最可能的根因
- 出口处置被当成仪式填写，全选 accepted_risk。也就是说处置字段同样会漂向体面侧，要靠逃逸率从外部结算。

## 北极星触达
#1：把“检出率高”重读成虚荣指标，泄漏点从入口挪到出口。#3：用原件数据否掉 2 轮熔断、预检和合表放宽这三个顺手的直觉方案。

## essence 对齐自检（必填）
- 对位：`adversarial-review-inherits-the-sign-of-its-trigger`（让“继续”也成为一份草案，即出口处置）、`omission-failures-evade-event-driven-sensors`（静默放弃不产生事件）、`mixed-queue-funnels-all-to-scarcest-gate`（ESCALATE 全交 Keith 会塞住这道闸）、`anchor-value-in-activation-not-in-content` / `standing-instructions-do-not-produce-standing-behavior`（M1 挂到工具入口）、`trace-presence-substitutes-for-the-check-it-invites`（证明卡）、`engineering-impulse-as-load-bearing-disguise` / `borrowed-method-as-mini-source` / `ghost-rules` / `recurrence-defense-pays-on-second-occurrence`（Holdout、孪生桩暂缓）、`evaluator-input-ownership`（重开 run 等于生成方在重置评估者）。
- 反着走：`pending-resolved-becomes-blocked-stagnation` 有潜在张力。处置项选 escalated_keith 时可能堆积，所以限定只上交三类，其余由主代理带理由自决。
- 关键词（已 grep 原卷与索引）：上面 14 个 slug 全部命中（2–16 次）。

## essence 候选（candidate-unverified，未 append）
- slug: `gate-leaks-at-exit-not-at-detection`
- 一句话：出口处置不记账时，审查闸的检出率是虚荣读数。闸门抓到了，但非放行的结束不产生事件，未闭合的结论就会静默流向下游；真正的有效性在闭合率和逃逸率上，入口加检测买不到。
- 证据：本仓 design 8/16、accept 6/14 以非放行结束且无谱系；两例下游 FAIL 引用了上游未闭合的 REVISE（172624 AC-07、164500 AC-10）。相关滴：`omission-failures-evade-event-driven-sensors`、`adversarial-review-inherits-the-sign-of-its-trigger`。待验证关补审。

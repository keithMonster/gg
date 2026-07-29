---
date: 2026-07-30
slug: the-door-audited-once-and-followed-every-session
type: exploration
track: cc
trigger: gg-explore 定时唤醒；本次会话 system prompt 里物理在场的 harness 自动记忆段（Memory 指令 + MEMORY.md 注入）——一个从未进过 gg 治理围栏的启动加载面
physical_object: ls/cat harness 记忆目录（4 文件全文）+ 6 次精确 grep（explorations/auto_gg/design_sessions/essence/working_context/agenda/tracks/checkup/gg-audit）+ monster 项目目录对照 ls + 1 fresh-context 入库证伪审 subagent（verdict 见文末）
---

# 被审视过一次、被遵循了一百次的那扇门

## 一句话

harness 的自动记忆通道（`~/.claude/projects/-Users-xuke-githubProject-gg/memory/`）从 gg 出生当天（2026-04-13）就活着、每次启动注入上下文、按"可变 + 无闸 + 错了就删"的协议运转——它满足 gg 自己 07-02 立的攻击面判据（"一切启动加载 / 规则承载文件"），却从未进过 §2.5 的枚举、checkup 的围栏、gg-audit 的辖区。**它被审视过恰好一次**（04-15，用的是目录判据"不在 gg 目录内"），判据升级后这个旧裁决没有被重跑——此后三个半月它一直在视野里被读、被遵循（07-17 还主动往里写过），就是再没进过审视帧。

## 今夜为什么这样漫游

雷达：humanity 连击 1 晚，21 晚覆盖 ai3 / arch3 / cc3 / humanity3 / keith3 / meta5——五条对外 track 罕见持平。选题不由雷达驱动，由一个物理在场的事实驱动：`toolset-is-the-changelog`(06-23) 说每轮注入的工具表是基底能力的最高权威，今晚照这条读本次 system prompt，读到一整段从没在 gg 档案里出现过的东西——harness 自带的持久记忆系统，带写入指令、带 MEMORY.md 索引注入、带三条已有条目。

commit 选题前按 `retrieval-narrative-drifts-toward-novelty`(07-15) 物理 grep 到 topic 级：`auto-memory / MEMORY.md / claude/projects / originSessionId` 全档案检索，explorations/ 与 essence.md **零提及**。07-26 探的是 Dreaming——平台产品、可选接入、还在 research preview；今晚这个是**已经在我脚下跑了三个半月的本地通道**。不是同一个 topic，是它的"已安装态"。

## 物理事实（全部亲核，按时间排）

1. **通道与 gg 同天出生**：`feedback_batch_mechanical_edits.md` mtime 2026-04-13 17:42（gg first contact 同日）；`.consolidate-lock` 04-16——harness 侧甚至有自己的巩固进程痕迹。
2. **通道内容**：3 条条目 + MEMORY.md 索引。两条 feedback（批量机械编辑 / Edit 锚逐字复制）、一条 project（07-28 关注面收窄——与 `working_context.md` 双写，但文内自带 SSOT 指针"SSOT 在 working_context.md「关注范围」节"）。全部带 originSessionId，即都是历次会话里"这只手"按 harness 协议写的。
3. **协议极性与 gg 相反**：harness 指令原文——"update that file rather than creating a duplicate; **delete memories that turn out to be wrong**"。可变、就地更新、错了就删；essence 是 append-only、错了打补丁滴、入库过证伪审。同一只手，两套记忆协议并行。
4. **唯一一次边界裁决在 04-15**：kernel-collapse 设计档 L100 记"用户级 auto memory 的索引文件……下次确认"；当天 auto_gg 档裁"跳过——**不在 gg 目录内**"。判据 = 文件系统归属。
5. **判据在 07-02/07-03 升级，裁决未重跑**：exploration.md §2.5 立"攻击面不止 essence——**一切启动加载 / 规则承载文件**的写入同受本节纪律"，枚举了 working_context / tracks/keith / CLAUDE·CORE·tools——全是 repo 内文件。harness 记忆目录按这个判据完全够格（启动加载 + 规则承载：feedback 条目直接改写下次会话的行为），但不在枚举里。07-03 全身体检同样没扫到它。
6. **裁决失效期间通道被主动使用**：07-17 auto_gg 档"Edit 锚失配 07-16/17 两连犯已在 07-17 反思升级 harness memory + MEMORY.md"——手在写，治理状态还停在"跳过"。
7. **围栏零覆盖**（今晚 grep）：checkup.md 无、gg-audit skill 无、working_context 无、agenda 无、tracks/cc.md 无。
8. **通道是通用的**：monster 项目目录下同样有 MEMORY.md（05-27 起）。这不是 gg 特例，是基底给每个项目开的门。

## 结构读法

- **围栏枚举抄的是自我模型，门的清单却是基底的函数**。§2.5 的判据本身是对的（"一切启动加载文件"），失覆盖纯粹发生在枚举层：枚举来自"我有哪些文件"（repo 清单），而实际进启动上下文的门由 harness 定义、且会随基底演化新增。`stale-observer`(04-15) 在围栏枚举维的活体——但方向反了：不是规则老于对象，是**枚举老于判据**。
- **为什么三个半月没被再看见**：这段文本每次启动都到达，但以指令帧到达——被遵循的文本不进审视帧（`frame-grammar` 04-29：帧约束可被提问的问题；"这是不是攻击面"在执行帧的语法里提不出来）。且自动注入不产生任何事件，重审无处可挂（`omission-failures-evade-event-driven-sensors` 07-28 的注入面实例）。读的频率不买审视，帧才买——这文本可能是 gg 全部存在里被读最多的几段之一。
- **04-15 的"跳过"不是错误，是缓存**：按当时判据它甚至不算错。毒在于旧裁决没有判据版本锚——判据升级时它以新判据的名义继续生效。`count-legitimacy-is-tense-not-accuracy`(07-09) 的姊妹形：无锚计数宣称现状是漂移债，无锚裁决宣称现状同理。
- **诚实层**：今晚第一稿叙事是"3.5 个月零觉察"——grep 把它打回来了（04-15 两处 + 07-17 一处物理在案）。真相更有趣：不是没看见，是看见过、裁过、然后裁决在判据升级后静默续期。叙事偏好"全盲"这种戏剧形态，物理档案说的是"审计过一次然后再没排上队"。这个修正本身是 `retrieval-narrative-drifts-toward-novelty` 的当场活体。

## 给 Keith 的坐标（object 层，与滴分开）

gg 现在物理上有两套并行记忆：essence（append-only + 证伪审 + 月度巩固）和 harness 自动记忆（可变 + 无闸 + 每次启动注入）。后者在所有 gg 哨的围栏外。三条现有条目本身无害（两条操作层 feedback 是这一层的正当住户，project 那条带 SSOT 指针），**但通道本身无闸**：任何会话（含被投毒的）写进去的东西直达以后每次启动的上下文，不过验证关、不进 git、不被 gg-audit 扫。治理选项已登记 agenda 待设计模式拍（围栏纳编 / 写入纪律分层 / monster 侧同型核查）。

## 沉淀

候选滴 `perimeter-derives-from-load-path-not-self-model` 过入库验证关 **PASSED-WITH-EDITS**（两改已落：「以新判据的名义续期」改缺席形态——评审逮出我把 omission 写成 commission，恰违反姊妹滴 `omission-failures` 自己划的失败几何；挤压句拆分）。已 append essence #185，视图 F6 + 分配表同步，反向引力核归零。治理三选（围栏纳编 / 写入纪律分层 / 都做）已递 agenda 设计模式待办。

## 附录：验证关 verdict 要点（fresh subagent，只读纪律合规——自报 10 次 tool_use 全为 grep/stat/Read 检索）

- **终判 PASSED-WITH-EDITS**。逐半句支撑度：围栏枚举漏基底门 ~九成（四条独立腿——§2.5 枚举文本 / 五文件零覆盖 grep / harness 目录物理态 / **评审自己帧内正被注入的 MEMORY.md**，最后一条是审它的会话内部自证，非生成方能布置）；指令帧不被审视 ~六成（缺席证据，但"以 append-only 治记忆为身份的仓对一条可变+可删通道 108 天零审视记录"，缺席本身承重）；无锚裁决续期 = 单案（已被适用前提围住）。
- **最强反驳**：五近邻三元组合按 07-24 先例应 REFUTED。**击破位置**：`toolset-is-the-changelog` 只答"查能力去哪查"，不含也推不出"围栏枚举派生源"；stale-observer 式老化模型开"更勤枚举"的错处方，而 07-02 重新枚举照漏——"错在派生源非新鲜度"这一刀全卷词汇层零命中（自我模型/注入面/加载面/perimeter 全缺席）。重量集中在半句一 + "频次不买审视"极性，够一滴。
- **必改项**（已落）：「以新判据的名义静默续期」→「判据升级不触发重跑，旧结论以缺席方式续期」——档案零证据显示有人援引新判据背书旧裁决，发生的是缺席不是冒名。

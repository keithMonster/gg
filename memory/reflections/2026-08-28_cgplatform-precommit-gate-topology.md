---
date: 2026-08-28
slug: cgplatform-precommit-gate-topology
summoner: monster 主会话（cg-platform「CI 检查提前到 PM 本机 pre-commit」闸拓扑裁决）
northstar_reach: "#3 决策超越直觉（把「无兜底」「不可观测」两个并列缺陷收敛为一个动作同时修复：兜底闸即上游传感器）"
status: substantive-decision
---

# Reflection: cg-platform pre-commit 闸拓扑裁决

### 给父会话的最终输出（必填）

**开题四问产物**：① 重写：原问「不对称是否改变合法落点」→ 真问题是「一道闸的合法性由链条位置（唯一 vs 冗余）决定，还是由同步/异步性质决定」——答案：位置。②判据：若裁错，现形物理量 = PM 机器闸未激活时坏 commit 是否被任何后续环节拦住（build：会；test 27 仓：不会）。③ 补集：无害论（best-effort 挂了总比没有强）/ AGENTS.md 自举块替代通道 / schema-lint 先例即许可——三条均在正文逐一处置。④ 最便宜一击：读 08-27 problem-terminator reflection（工具返回在案），确认「ci_template test job 单点杠杆、先于一切 hook」是上轮已判且证据 11 证实尚未落地（白名单仅 cg-weilu 且 allow_failure: true）。

**Q1：不对称成立，且它就是裁决轴。** 「把检查提前到本机」这个动词只对远程已存在的检查有定义。Keith 原理陈述内含隐前提：远程那道检查存在、只是信号异步。build 档前提成立（docker build 必跑同一命令）⇒ pre-commit build 是真「提前」，未激活不漏拦。test 档对 27 个仓前提为假（CI 根本不跑测试，证据 11）⇒ 挂 pre-commit 不是「提前」，是把一道新闸新建在激活状态物理不可观测的位置。**可以一并挂同一道 pre-commit（实现层同址无妨），但两档合法性来源不同**：build 自身合法（冗余前置）；test 的合法性是借来的，须由 CI test job 供给——CI 侧先行或同 PR 落地。

**Q2：无兜底 + 激活不可观测的闸不是合法质量闸。** 它比「没有闸」更坏一档：账本上显示已建闸（28 仓 pre-commit 在场、传感器全绿），物理上拦截保证不存在——正是 canon-bugs「命中恒 0 长期假绿」的预制形态。正确结构 = **双层：远端 CI test job 是承重闸（唯一可观测、可强制的位置），本机 pre-commit 是提速镜像（best-effort，激活与否只影响反馈延迟、不影响拦截保证）**。这不是对「提前到本机」目标的违反，是补全其隐前提：先让远程有这道检查，才谈得上提前。schema-lint 双闸形态应从工程巧合升为平台闸拓扑规则：**本机侧只放镜像，不放唯一闸**。

**Q3：schema-lint 不是正在被复制的结构性错误——它是正确形态；错误的是把它的表层（pre-commit + 仓内传感器）复制走而丢掉承重件（部署期兜底）。** 准入三问②对激活侧的回答：无兜底时 =「无人且物理上不可能有人」（PM 机器不可达 + 08-26 已拍不碰同事机器）——否决性答案；有兜底时降级为可接受残差，且**残差本身获得传感器**：若 pre-commit 普遍生效，CI 上该类失败应趋近 0；CI 持续出现本该被本机拦的失败 = 激活率低的代理读数。**建 CI 兜底一个动作同时修两个洞：拦截保证 + 激活侧观测**——召唤方把「无兜底」「不可观测」当两个独立缺陷列出，实际是同一缺失的两个投影。

行动建议（拓扑层，实现细节归主代理）：
1. **先**扩 ci_template test job 覆盖 11 个有测试仓（自适应跳过无 test script 仓），allow_failure: true 给退出时间表——只要它为 true，CI 也只是信号不是闸，兜底最低标准 = 失败可观测且有人看，理想 = 阻断。
2. **后（或同 PR）** test 进 pre-commit 作提速镜像。build 档可即刻挂（兜底已在）。
3. 「本机侧只放镜像不放唯一闸」写为平台条款（落点 ENG-STD 或 drift_audit 判据，主代理拍）。
4. 配套前提：证据 9 的「默认 test = 纯单测不碰外部」既成事实须升模板条款——同步闸要求测试快且无外部依赖，不升则任一仓引入慢/脏测试即炸本机闸。cg-weilu 68.58s 类大仓在镜像层可自由降档（只跑 affected / 跳过），因为保证在 CI——这是双层结构的红利：本机层不承重才敢为体验优化。
5. 远端拦截读数当激活率代理传感器——顺手即有，不需（也不许）建碰 PM 机器的新通道。

**依赖的召唤方数字**：证据 11（27 仓 CI 无 test job）是 Q1/Q2 全部承重——若白名单实际更宽，不对称收窄、test 档部分回到 build 档语义；证据 4/5（build 2.33s）只影响实现层不影响拓扑。

### 核心假设

- 「提前」语义分析成立：Keith 的原理陈述确以「远程检查存在」为隐前提，补全前提不算改目标层。
- CI（GitLab 侧）是平台可观测、可强制的位置——runner 稳定性问题（pipeline 挂了没信号）是另一条已知线，但它损害的是反馈及时性，不推翻「CI 是唯一可强制点」。
- PM 仓的 commit 实际由 AI agent 发起，AGENTS.md 自举块可作辅助注入通道，但它是 attestation 型非硬闸，不能替代 CI 承重。

### 可能出错的地方

- 若 GitLab CI 本身可靠性差到「兜底闸经常整体缺席」（Keith 那句 pipeline 挂了没信号的原始痛点），双层结构的承重层自身在漏——届时正确响应是修 CI 可靠性，而不是回头让本机当唯一闸；但若 Keith 的真实意图是「CI 不可信所以整体搬家到本机」，本裁决的前提被抽走，须回到目标层重新对齐。
- 「远端拦截率作激活率代理」要求失败分类可区分（哪类失败本该被 pre-commit 拦）——若 CI 读数不分类，代理信号噪声大。

### 本次哪里思考得不够

- 未实查 ci_template 现行内容与 GitLab runner 拓扑，CI「可强制」按召唤方证据与 08-27 先验采信。
- 17 个零测试仓的长期路径（模板增量 vs 存量补）未展开——08-27 裁决「按第二次付费」已覆盖，未重推。

### 如果 N 个月后证明决策错了，最可能的根因

低估了「CI 侧扩 test job」在 28 仓异构测试栈上的落地摩擦（证据 7：栈不统一、硬编码路径）——若摩擦大到 CI 兜底迟迟不落地，而 pre-commit 镜像先落了，事实拓扑就回到被否决的形态且带着「已裁决合法」的错误印象。

### 北极星触达

#3：直觉解是「build/test 都挂 pre-commit、一步到位」，裁决给出合法性来源分解 + 一个动作修两洞的收敛，超越「挂/不挂」二元。

### essence 对齐自检（必填）

- **对位滴**：`rule-layer-flywheel`（CI = 事件层机器强制，08-27 已消费）、`omission-failures-evade-event-driven-sensors`（激活失效是缺席型，仓内传感器抓不到——本裁决用下游读数抓）、`audit-loop-closure`（双向指针精神：闸与其检验者互指）、`mechanical-gate-needs-machine-detectable-target`（激活状态在 PM 机器上无机器可判目标 ⇒ 本机侧不承重）、`one-shot-invariant-decays-under-live-append`（ENG-STD §7 [硬] 条款存在无机械闸 = 活体又一例）。
- **反着走的**：无冲突滴。08-27 REFUTED 滴 `register-the-check-not-the-verdict` 已按召唤方回执规避——本裁决不引「维护即运行」，承重全在「独立对撞源」侧（CI 是不共用本机错前提的对撞源），与该 REFUTED verdict 的重提名方向一致而非冲突。
- **候选滴（candidate-unverified，留此待夜巡/设计模式补审，不 append essence）**：`downstream-gate-is-upstream-sensor` — 串联冗余闸中，下游兜底闸的拦截读数是上游闸健康度的免费代理传感器；砍掉（或不建）下游闸失去的不只是兜底，还有对上游的全部观测——「不可观测端点」的观测通道不必新建，建下游闸即顺带获得。物理证据（宣称级，源 monster 会话实测）：cg-platform build 档（docker build 兜底在 ⇒ pre-commit 失活可经 CI 构建失败现形）vs test 档（27 仓无 CI test ⇒ 失活完全不可观测）；PM 机器物理不可达 + 08-26「不碰同事机器」拍板使直接传感器不可能，代理读数是唯一通道。相关既有滴：`omission-failures-evade-event-driven-sensors`（缺席型观测的另一条出路）、`audit-loop-closure`、`signal-weak-vs-channel-dead`（通道未建时零读数无定价资格——本滴给出建通道的免费路径）。
- **对齐度**：高。

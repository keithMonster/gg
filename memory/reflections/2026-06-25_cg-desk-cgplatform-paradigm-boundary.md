---
date: 2026-06-25
slug: cg-desk-cgplatform-paradigm-boundary
summoner: monster
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: cg-desk 该不该进 cg-platform —— 平台范式边界裁决

承上一轮 `2026-06-25_cg-desk-backend-topology-verdict.md`（钉死"单容器约束根因=企微长连接，web 没这堵墙"）。本轮 Keith 拍了企微下线 + 想用 cg-platform onboard 迁 cc-assistant 后端，问题升到 cg-platform 范式边界。

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**总判断：选形态 C（前端走 cg-platform onboard / 后端 claude 进程池保持独立服务），但要把"独立后端"的身份正名为「平台级 runtime 基建」——它是 cc-gateway 的有状态孪生，该跟 cg-platform 平级，不该当 cg-platform 的"应用"被 onboard。形态 B（整个迁进 cg-platform 当应用）是范式污染，否决；形态 A（后端彻底独立、cg-desk 也可独立）对了一半——它对在"后端不进 cg-platform"，错在没认领"后端是平台基建"这个定位，会让 cg-desk 前端白白放弃 cg-platform 一条龙的治理红利。**

**逐问裁决：**

**问 1（选哪个形态）= 形态 C，承重理由是"两个东西的不变性根本不同，必须分配到不同的稳定点"（invariance-allocation）。**

cg-desk 这件事里其实有两个独立对象，brief 的形态 A/B/C 之争本质是"要不要承认它们是两个对象"：

- **对象一 = cg-desk 的 web 前端**：无状态、标准 SPA、要域名/CI/部署/nginx 一条龙。它的不变性诉求跟 cg-platform 在册的十几个应用**完全同构**——这就是 cg-platform onboard 存在的意义。让它走标准 onboard，吃满治理红利（registry 账本 / 双环境 / drift_audit / PM 二次确认 / 蓝绿），零特殊化。
- **对象二 = per-user 常驻 claude 进程池**：有状态（jsonl volume + SQLite + workspaces）、long-running、资源密度是真天花板、多租户进程权限隔离待决。它的不变性诉求跟 cg-platform 应用**根本不同构**，跟 **cc-gateway（已被定位为"非对话场景 runtime"）同构**——都是"平台为别人提供 LLM 执行能力的有状态 runtime"。

形态 B 的错误是把这两个不变性强行塞进一个稳定点（一个 onboard 出来的应用容器）。形态 A 的不足是把它们一起踢出 cg-platform，让前端也丢了红利。**形态 C 把对象一分配给 cg-platform 应用层、对象二分配给平台 runtime 层——各归各的稳定点。** 这不是折中妥协，是 invariance-allocation 的正解：架构的本质是选择相信什么不变，cg-desk 前端"不变的是标准 web 部署形态"、进程池"不变的是有状态 LLM runtime 形态"，两个稳定点不一样就不能共用一个容器。

**问 2（cg-platform 该不该接纳有状态特殊后端应用）= 不该。这是范式污染，不是平台能力扩展。**

这是本次最承重的判断，单拎出来说清：

cg-platform 的整个治理体系**建立在"应用是无状态标准 PM 业务应用"这个不变性上**——蓝绿部署假设 fresh 容器可随时替换（无状态才敢杀旧容器）、`--scale=2` 假设多实例对等（有状态会串）、onboard 一键起假设应用只连自己 cgPlatform 库 + 借 cc-gateway 用 LLM（契约 §2 平台直注 `CC_GATEWAY_URL` 段是明文范式）。**这些不是实现细节，是平台之所以能"一键 onboard、PM 不碰运维"的根因前提。**

接纳一个自持 claude CLI + named volume 不能删 + 部署脚本要认有状态的应用，**等于在平台的根因前提上凿洞**。而且这个洞不会停在 cg-desk——`paradigm-not-feature-completeness`：迁移/接纳的拒因从来不是"功能能不能覆盖"，是"被接纳对象的稳定性靠什么范式机制"。cg-desk 后端的稳定靠的是"自由 claude 进程 + volume 持久化 + LRU 回收"，cg-platform 的稳定靠的是"无状态 + 蓝绿 + 字典注入"——**两个范式机制相反**。强行让前者进后者，就是 `borrowed-method-as-mini-source` 的反向：在无状态平台里造一个有状态特例，平台为它破的每条假设（volume 保留 / scale=1 / 自持 LLM）都是给后续"我这个也特殊一点"开的先例。破例一次，治理失效——因为下一个 AI 类应用会指着 cg-desk 说"它能有状态我为什么不能"，而平台没有原则性的拒绝理由了（你已经破过）。

**正确动作：cg-platform 守住"无状态标准应用"的范式纯度，把"有状态 LLM runtime"这类需求引导到平台 runtime 层（cc-gateway 旁边），而不是塞进应用层。** 这恰恰是平台能力的真正扩展——扩展的是"平台 runtime 层多一个有状态成员"，不是"应用层破一次无状态假设"。前者是加一个平级基建，后者是污染一整层契约。

**问 3（企微下线后，进程池是"一个应用"还是"一块平台级 runtime 基建"）= 平台级 runtime 基建，跟 cc-gateway 同级。这条判断决定了问 1/2。**

企微下线前，cc-assistant 后端的身份是模糊的——它有个企微 bot 入口，看着像"小助理这个应用"。**企微一拆，入口没了，剩下的纯粹是"per-user 有状态 claude 进程池 + 人设渲染 + EverOS 记忆桥 + 业务端点"——这是一台 LLM runtime，不是一个面向终端用户的应用。**

对照 cc-gateway 的定位演化（thread 实证）：cc-gateway 当初也一度承载对话，后来被 Keith 收窄为"非对话场景 runtime（定时任务/skill 执行）"——剥掉对话入口后，它的本质暴露为"平台级 LLM 执行基建"，跟 cg-platform 平级、被各应用经 `CC_GATEWAY_URL` 消费。**cc-assistant 去企微后走的是同一条暴露路径**：剥掉企微入口，本质暴露为"平台级**有状态对话** runtime"——cc-gateway 管无状态的 trigger/skill 执行，cc-assistant runtime 管有状态的 per-user 长对话。两者是平台 runtime 层的一对孪生（无状态 runtime + 有状态 runtime），都不是 cg-platform 的"应用"。

所以它不该被 onboard。onboard 是给"应用"的动作（建 cgPlatform 库账号 + 进 registry + 走应用蓝绿）。**基建不 onboard，基建独立部署、被应用消费。** cg-desk 前端（应用）onboard 进 cg-platform，调这台 runtime（基建），就像别的 PM 应用调 cc-gateway 一样自然。

**问 4（实现层边界：哪些主代理自决、哪些回 gg）：**

**主代理自决（实现层，不用再 call gg）：**
1. cg-desk 前端走 `cg_platform_onboard.py` 标准 onboard（`--db-mode null` 或按前端是否要自己的库定）——这是平台标准动作，零特殊化，直接做。
2. cc-assistant 后端去企微改造（拆 wecom-bot 长连接、加 web HTTP/SSE 入口）——上一轮已裁"web 入口与企微入口平级零依赖"，现在企微直接没了，更简单：后端就是 HTTP/SSE → pool.js 进程池，独立部署。实现自决。
3. 后端独立服务的部署落点（哪台机、nginx 怎么配、volume 怎么持久化）——按 `DEPLOYMENT.md` 拓扑选，借 cg-platform 的 nginx/域名基础设施（形态 C 的"后端只借 nginx/域名"那一面）是合理的，不算进 cg-platform 应用层。
4. cg-desk 前端调后端的鉴权/CORS/SSE 对接——纯实现。
5. 契约矛盾不存在了：cc-assistant 调 cg-proxy(user-mappings) + minio(owner-map) 受不受限——**不受限**。契约 §2「跨库访问归应用自理」(2026-06-16 Keith 拍) 已撤"不许应用调其他内部 API"的旧限制，平台只保证 cgPlatform 库内的 GRANT 隔离，应用连什么外部 API 自负爆炸半径。而且 cc-assistant 后端根本不是 cg-platform 应用（它是基建），这条限制对它本就不适用。

**要回 gg（架构层，难回退）：**
1. **若发现"后端独立 runtime"和"前端 onboard 应用"之间需要建一层共享契约**（比如后端要不要进某个 registry、要不要纳入 drift_audit、要不要标准化它的部署脚本成"平台 runtime 部署范式"）——这是给平台 runtime 层立新契约，属架构层，回 gg。
2. **若 keyi-ios 主线推进到"可依 APP 也要调这台后端 runtime"**（thread 5-27 已埋 V5 收口锚点 + "V2 起涉及拓扑融合强制 call gg"）——多个前端（cg-desk web / 可依 iOS / 未来企微若复活）共享一台有状态对话 runtime 的拓扑，是承重墙，回 gg。这正是 cc-assistant runtime 作为"平台基建"而非"单应用"的价值兑现点。
3. **多租户 claude 进程权限隔离方案**（OS 层 per-user UID 硬沙箱 vs dontAsk）若要定型——这是有状态 runtime 的安全承重墙，且与"它服务全公司"的爆炸半径强相关，定型前回 gg。

**一句话给主代理：** cg-desk = 一个标准前端应用（onboard 进 cg-platform）+ 一台有状态 LLM runtime（cc-gateway 的孪生，独立部署、平台级、不 onboard）。别把 runtime 塞进应用层，那是污染平台范式的一次性破例。前端的事自决落地，runtime 跟其他前端的共享拓扑回 gg。

### 核心假设

- cg-platform 的治理红利（一键 onboard / 蓝绿 / drift_audit / 双环境）**确实依赖"应用无状态"这个前提**——蓝绿杀 fresh 容器、scale=2、字典注入都建立在此。若平台其实早有有状态应用先例（我没穷举 registry.json 全部在册应用的状态性），"破例一次治理失效"的论证强度要降。但即便有先例，问 3"进程池本质是 runtime 不是应用"的判断独立成立，结论不变。
- cc-gateway 被定位为"非对话场景 runtime、跟 cg-platform 平级、被应用消费"——这是 thread `cc-gateway.md` brief + 多条时间线实证（公网入口关闭、内网 runtime 收口），是我类比"cc-assistant runtime 是它孪生"的支点。若 cc-gateway 其实是 cg-platform 内部组件而非平级基建，类比要重估。

### 可能出错的地方

- 最可能崩：形态 C 把前端和后端拆成两个部署单元，引入"前端 onboard 在 cg-platform、后端在别处"的运维割裂——若 Keith 的真实诉求是"一个项目一个仓一键起、不想管两个部署单元"，那形态 C 的运维心智成本可能让他更想要形态 B 的"全在一个 onboard 里"。这是 `terminus-walk` 的偏好张力：我按"范式纯度"推 C，但 Keith 可能按"我就想一条命令搞定"推 B。已在行动建议里把"后端借 cg-platform nginx/域名"留作降低割裂感的接口，但本质割裂仍在——若 Keith 明确说"我宁可破范式也要一键"，那是目标层，C 让位。
- 概率中等：我把"有状态进程池"判为"必须独立 runtime"，但其实 cg-platform 蓝绿对单一有状态应用未必致命（named volume 不删 + scale=1 锁死，上一轮已分析这是"软摩擦：掉 session 用户重开一轮，非数据丢失"）。若 Keith 评估"破这点范式的代价 < 拆两个部署单元的代价"，形态 B 在工程上跑得通——我判 B"污染"主要是治理传染风险（后续应用援例），不是 B 技术上不可行。这条 trade-off 的权重是 Keith 的偏好域。

### 本次哪里思考得不够

没穷举 registry.json 全部在册应用确认"是否已有有状态先例"——"破例一次治理失效"的论证默认了平台当前全是无状态应用。若已有先例，问 2 的滑坡论证要弱化（但问 3 的 runtime 定位判断不依赖它）。没读 `cg_platform_onboard.py` 源码确认 onboard 是否物理上拒绝有状态（比如它是否硬编码无 volume）——我按"onboard 假设无状态"推断，是基于契约文本（蓝绿 / 字典注入 / `synchronize:false`）的合理推断，非读脚本实证，标 [推测]。

### 如果 N 个月后证明决策错了，最可能的根因

keyi-ios 主线推进后，发现"可依 APP + cg-desk web + 可能复活的企微"三张脸共享一台有状态 runtime 的拓扑，比"runtime 跟着某一张脸走"复杂得多——届时"把 runtime 独立成平台基建"是对的（多脸共享必须独立），但"何时独立、独立后归谁维护、算不算第 N 个平台基建"如果没在现在就想清楚归属，会变成又一块没人认领的接缝（cc-gateway volume EACCES 炸 4 天无声的同形态：基建掉决策接缝无 owner）。我已把"多前端共享 runtime 拓扑"标为回 gg 项，就是防这个根因。

### 北极星触达

#1 二阶效应——核心贡献是看穿"企微下线"这个动作的二阶效应：它不只是"少一个通道"，是**让 cc-assistant 后端的真实身份从"模糊的应用"暴露为"平台级有状态 runtime"**。Keith 问的是"要不要迁进 cg-platform"（应用层问题），我把问题维度抬到"它根本不是应用、是 cc-gateway 的孪生基建"（基建层判断）——看得更远（身份本质）而非更全（罗列三形态优劣）。这跟上一轮"把单容器约束还原成企微外设属性"是同一条二阶链的延续：剥掉企微，约束消失、身份暴露。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `invariance-allocation`（核心）——问 1 的支点：cg-desk 是两个对象（前端无状态 / 进程池有状态），不同的不变性必须分配到不同稳定点（应用层 / runtime 层）。形态之争=要不要承认两个对象。
  - `paradigm-not-feature-completeness`（核心）——问 2：接纳拒因不是"功能能不能覆盖"，是"被接纳对象的稳定性靠什么范式机制"。进程池靠有状态+自由 claude，cg-platform 靠无状态+蓝绿，范式相反。
  - `m2m-vs-h2m-coupling-illusion`——问 3 的孪生论：cc-gateway 管无状态 trigger（M2M 短任务）/ cc-assistant runtime 管有状态长对话（H2M 长会话），两类 workload 不同构、不该塞一层。本次是它的正向应用（识别出两类 runtime 该分立）。
  - `tool-elevation-as-occam`——cc-assistant runtime 出现第二个消费者（cg-desk web，企微之外）时，把它上提为平台级共享基建是 OCCAM 不是过度工程。但上提的是"基建到平台 runtime 层"，不是"进 cg-platform 应用层"——上提方向是平级而非降为应用。
  - `borrowed-method-as-mini-source`（反向）——形态 B 在无状态平台里造有状态特例 = 在 cg-platform 里造一个反范式的迷你 runtime，越塞越压不动平台的无状态范式机制。
- **本决策是否在某条 essence 上反着走**：潜在张力——`terminus-walk-needs-terminus-visibility` 说"终态模糊就别按偏好拆"。有人会问：keyi-ios 多脸共享 runtime 的终态还没可见，我现在就判"后端独立成基建"是不是按偏好提前拆？我判断不是：后端独立**不依赖**多脸终态——企微下线的当下，后端已经是"无应用入口的纯 runtime"，独立是对当前已可见事实的响应，不是对未来终态的预判。多脸共享拓扑那部分我恰恰**没拆**（标了回 gg），守住了 terminus-walk。区分点：runtime 独立=响应已发生的企微下线（终态已现）/ 多脸拓扑=未来才发生（终态模糊，推迟）。这条张力想清楚了。
- **cross-check 用的关键词**：grep essence「invariance」「paradigm-not」「m2m」「tool-elevation」「borrowed-method」「terminus」。

### essence 候选（可选）

- slug: `decommission-reveals-true-identity`
- 一句话: 拆掉一个组件的某个入口/通道，常常不是"减一个功能"，是让它的真实身份从入口的伪装下暴露出来——企微 bot 入口拆掉，cc-assistant 后端从"小助理应用"暴露为"平台级有状态 LLM runtime"。决定一个组件归哪层之前，先剥掉它的过渡入口，看剩下的本质是什么。
- 是否已 append 到 essence.md: N（留 Keith review）

### 外部锚点（可选）

- `~/githubProject/monster/inbox/briefs/cg-desk.md` ← 决策对象 brief（含前两轮裁决）
- `~/githubProject/monster/cg-platform/integration-contract.md §2` ← 平台直注 CC_GATEWAY_URL 范式 + 跨库自理撤限
- `~/githubProject/monster/threads/cc-gateway.md` ← cc-gateway "非对话场景 runtime、跟 cg-platform 平级" 定位（孪生类比支点）
- `~/githubProject/monster/threads/cc-assistant.md` ← 进程池形态 + V5 keyi-ios 收口锚点
- `~/githubProject/gg/memory/reflections/2026-06-25_cg-desk-backend-topology-verdict.md` ← 上一轮（单容器约束=企微外设属性）

---
date: 2026-06-25
slug: cg-desk-backend-topology-verdict
summoner: monster
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: cg-desk 后端拓扑承重墙裁决

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**总判断：拓扑方向「方案 A：给 cc-assistant 2.0 加 web 嘴」对，但 brief 把承重墙错放了——真正的承重墙不是「web 入口该不该加」，是「单容器约束的根因是企微长连接，而 cg-desk 没有这个约束」。这意味着方案 A 在 MVP 阶段是对的隔断，但 brief 的「继承 cc-assistant 单容器约束」叙事埋了一个会反咬的错误前提。**

**逐问裁决：**

**问 1（拓扑方向是承重墙级别的对，还是结构性风险）= 方向对，但有一个被误标的结构性陷阱。**

- web 嘴复用 2.0 编排（人设/记忆/业务端点）= 对。这是 OCCAM，不是埋债——编排层（personal-assistant.md + EverOS + /api/* + per-user claude 进程）跟「嘴是谁」正交，一套大脑两张脸是正解。
- 但 brief 反复说的「cg-desk 继承 cc-assistant 2.0 单容器约束」**是错误前提**。读 thread `cc-assistant.md` L52-53 的物理地真：单容器不能 scale 的根因是 **「企微 AI Bot 长连接同 botId 只能一个 client，新连接踢旧连接」**——这是企微侧的协议约束，不是 claude 进程池的约束。**cg-desk 是 HTTP/SSE 入口，根本没有这个长连接 botId 单例约束。** 把「企微壳的单容器宿命」当成「2.0 后端的固有属性」继承给 web，是把一个外设约束误读成内核约束。
- 真正限制 web 高并发的不是「单容器」这个标签，是 **per-user 常驻 claude stream-json 进程的资源密度**（每个在线 user = 一个常驻子进程 + 一份 jsonl，maxProcs 是真天花板）。这条约束 web 和企微共享，但它**不锁死单容器**——它锁死的是「单机能挂多少并发 user 进程」，扩法是水平加机器 + 进程池分片，不是被企微长连接钉死的单实例。

**问 2（承重的修正方向）= 不是「现在就拆 BFF / 解耦运行时」，是「MVP 阶段方案 A 单容器直接上，但开工前把一个边界钉死：企微 WS 入口和 web HTTP 入口必须是同一容器里的两个并列入口，谁都不准成为对方的前置依赖」。**

- 不该现在拆独立 BFF——cg-desk 是纯 web 嘴，自己起一个 BFF 层是 `tool-elevation-as-occam` 的反面（第二消费者还没真出现就上提，纯增一跳）。
- 不该现在把「编排」和「企微 WS 运行时」解耦成独立横扩服务——这是把 MVP-1 的拆分成本提前付，违反 `terminus-walk-needs-terminus-visibility`（全公司并发的终态形状还没可见，现在拆是用偏好伪造终态）。
- **该现在做的唯一承重动作**：web 入口绝不能复用/穿过企微的单 botId 长连接客户端。如果实现时图省事让 web 请求也经过 wecom-bot.js 的连接管理，就会把企微的单例约束病毒式传染给 web。web 入口 = 独立的 HTTP server + 独立调 pool.js spawnFor，跟 wecom-bot.js 平级、零依赖。这一条钉死，单容器 MVP 跑通后扩人时拆机器是「加复制品」而非「拆耦合」，拆的成本反而比现在分层便宜。

**问 3（同一 userid 两张嘴同时在线，会话/记忆/进程串台）= 是实现层问题，但有一个必须在 MVP-0 验的真陷阱，不是「sessionId 分一下就行」那么轻。**

- 进程复用：pool.js 的进程 key 是 userid。两张嘴同 userid 会命中**同一个常驻 claude 进程**——这不是 bug，是 feature（同一个人在 web 和企微本就该是同一个助理上下文）。但它意味着两张嘴**共享同一个 stream-json 进程的单一对话流**：web 发一句、企微发一句，会交错进同一个 claude 上下文，token 流也会串。
- 记忆：EverOS/SmartSheet 按 `userid` 隔离，两张嘴本就该共享，无串台问题。
- **真陷阱 = cwd-as-resume-anchor（已沉淀 essence）**：claude --resume 的 jsonl 按 cwd-hash 索引。如果 web 嘴和企微嘴给同一 userid 分配了**不同 cwd / 不同 sessionId**，就会撕成两条 resume 链，「同一个人同一个助理」的承诺破裂；如果强行共用同一进程同一 cwd，又会出现两张嘴的 token 流交错。**这两个都不是「sessionId 维度分一下」能糊过去的——必须在 MVP-0 显式决定语义**：是「两嘴共享一个会话流」（简单，但 web 会看到企微的对话历史，可能是想要的也可能不是），还是「两嘴各自独立会话、底层记忆共享」（清晰，但要给同 userid 的 web/企微分配不同 sessionId + 不同 cwd 子目录，且接受它们不是同一个 claude 进程上下文）。**推荐后者**：web 和企微是不同使用场景，独立会话流 + 共享 EverOS 长期记忆，符合「一个大脑两张脸但各记各的短期上下文」。

**问 4（拓扑要不要在 MVP-0 之前定对）= MVP-0 单容器直接跑，但问 2 的「双入口零依赖」和问 3 的「会话语义」这两个边界必须在 MVP-0 就钉对，不能推到 MVP-1。**

- 单容器够不够用：MVP-0 验形态够用，直接上，别现在拆。
- 但「拓扑决策推到 MVP-1」是**伪推迟**——problem 2 的双入口耦合和 problem 3 的会话语义，是写第一行 web 入口代码时就会被实现方式固化的。一旦 MVP-0 图省事让 web 走了企微连接管理、或让两嘴塞进同一会话流，到 MVP-1 全公司时再改就是动已上线的运行时契约。**这两个不是「拓扑」（可以晚定）而是「不变性分配」（invariance-allocation，第一行代码就在选）。** 所以裁决是：单容器晚定（推 MVP-1），双入口零依赖 + 会话语义 早定（MVP-0 钉死）。

**行动建议（给父会话 / Claude 实现层）：**
1. MVP-0 直接单容器，方案 A 落地，不拆 BFF、不解耦运行时——这部分 Claude 实现层自决，**不用再 call gg**。
2. 实现 web 入口时硬守一条：web HTTP/SSE server 跟 wecom-bot.js 平级，独立调 pool.js，**零依赖企微长连接客户端**。这是承重约束，写进 cc-assistant CLAUDE.md。
3. MVP-0 就定会话语义：推荐「同 userid 的 web/企微各自独立 sessionId + 独立 cwd 子目录，共享 EverOS 长期记忆」，MVP-0 验一轮两嘴同时在线不串 token 流、不撕 resume 链。
4. 修正 brief 里「cg-desk 继承单容器约束」的措辞——单容器约束的根因是企微长连接，cg-desk 没有它；cg-desk 的真约束是 per-user 进程资源密度（maxProcs），那是水平扩机器解，不是被钉死单实例。
5. 全公司前 cc-assistant 的 6 项硬门（admin 认证/UID 隔离/TTL/加密/maxProcs/成本）照旧，cg-desk 直连即继承，不另起——这部分 brief 写对了。

### 核心假设

- thread `cc-assistant.md` L52-53「单容器约束根因=企微 botId 长连接单例」是准确的物理地真（来自 5-21 实测记录，非推断）。这条是整个裁决的支点——若它错了（单容器另有 claude 进程层的硬约束），问 1/2 的「方向对」判断要重估。
- per-user claude 进程是水平可分片的（多机各挂一部分 userid 的进程），不存在跨进程的全局共享状态阻止横扩。brief 和 thread 都未提到反例，按可分片假设。

### 可能出错的地方

- 最可能崩的点：问 3 推荐的「两嘴独立 sessionId + 独立 cwd」可能跟 pool.js 现有的「进程 key=userid 单进程」实现冲突——若 pool 强制一 userid 一进程，独立 cwd 就要么改 pool（动上游）要么两嘴塞一个进程（回到串台）。这一层我没读 pool.js 源码确认，是基于 thread 转述推断，标 [推测]。父会话开工前应实读 pool.js 的 keyOf 和 spawnFor 确认进程粒度是 per-userid 还是可 per-session。
- 概率中等：若 Keith 其实想要「web 和企微就是同一个连续会话」（在手机企微聊一半、回电脑 web 接着聊），那问 3 的推荐反了，应选「共享会话流」。这是产品语义偏好，我按「不同场景独立上下文」推断，可能错——已在行动建议标为可纠。

### 本次哪里思考得不够

没实读 cc-assistant `server/cc/pool.js` / `proc.js` 源码，进程粒度（per-userid 还是 per-session）、cwd 分配逻辑都是基于 thread 5-21~5-25 实测记录的转述推断。承重墙拓扑判断不依赖这些细节（双入口零依赖 + 会话语义早定 这两条结论在任何进程粒度下都成立），但问 3 的具体实现路径依赖它——已显式交还父会话实读确认。

### 如果 N 个月后证明决策错了，最可能的根因

全公司上线后发现单机 per-user 进程密度天花板比预期低得多（几百人 × 常驻进程 = 内存爆），而「水平分片加机器」因为 EverOS/cwd/sessionId 的某个全局状态没法干净分片——届时「方案 A 单容器晚拆」的赌注输给「早该把编排和运行时解耦成无状态可横扩服务」。这正是 brief 问 2 担心的，我判断为 MVP 阶段不该提前付，但若进程密度天花板极低，这个判断的时间窗就被压缩。

### 北极星触达

#1 二阶效应——核心贡献是把「单容器约束」从误标的内核属性还原成企微外设属性，让 Keith 看见「web 没有这堵墙」这个被 brief 叙事遮蔽的事实，避免把过渡形态的偶然约束当终态固有限制继承。这是看得更远（约束的真实来源）而非更全。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `m2m-vs-h2m-coupling-illusion`（核心）——但本次是它的**反向应用**：brief 担心「web H2M 高并发压到企微 bot 后端 = 异构 workload 强行同构」，我核实后判断企微 WS 和 web HTTP 确实是异构入口，但它们**没有共享单点容量约束**（单容器是企微长连接的锅，不是共享后端的锅），所以这次不是该拆的耦合幻觉，是被 brief 误读成耦合的正交关系。
  - `terminus-walk-needs-terminus-visibility`——全公司并发终态形状未可见，拒绝现在按偏好拆 BFF/解耦运行时；但双入口零依赖 + 会话语义是 invariance-allocation 第一行代码就定，不属「终态模糊」可推迟项。
  - `cwd-as-resume-anchor`——问 3 串台陷阱的物理根，直接复用。
  - `invariance-allocation`——问 4 区分「单容器（可晚定）vs 双入口语义（第一行代码就选的不变性）」。
- **本决策是否在某条 essence 上反着走**：潜在张力——`tool-elevation-as-occam` 说「第二消费者出现时上提是 OCCAM 不是过度工程」，而 cg-desk 正是企微之外的第二消费者，按这条似乎该现在就把编排上提成独立服务。但我判断本次例外合理：第二消费者出现的是「入口」（web 嘴），不是「编排能力」——编排已经在 cc-assistant 仓内自包含，web 嘴复用它不需要任何上提，上提的是入口适配层而非共享能力，所以 tool-elevation 不触发。这条张力我想清楚了，不是没展开。
- **cross-check 用的关键词**：grep essence「coupling」「terminus」「cwd」「invariance」「tool-elevation」「m2m」。

### essence 候选（可选）

- slug: `inherited-constraint-may-be-peripheral-not-core`
- 一句话: 过渡形态的约束被继承给新形态时，要先归因约束的真实来源——是内核属性（随能力走）还是外设属性（随旧入口走）；把外设约束误读成内核约束，会让新形态白白背上它根本没有的限制。
- 是否已 append 到 essence.md: N（留 Keith review）

### 外部锚点（可选）

- `~/githubProject/monster/inbox/briefs/cg-desk.md` ← 决策对象 brief
- `~/githubProject/monster/threads/cc-assistant.md` L52-53 ← 单容器约束根因的物理地真

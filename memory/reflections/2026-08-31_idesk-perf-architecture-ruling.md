---
date: 2026-08-31
slug: idesk-perf-architecture-ruling
summoner: monster（cg-weilu / iDesk 性能病灶定性 + 架构裁决）
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: iDesk 性能病灶定性——不是容量病，是无上界操作病

### 给父会话的最终输出（必填）

**裁决三问的答案**：

**① 定性：召唤方推论①成立、③方向对但形态要修正；现有方案的「部署 × 单副本 SSE」定性只覆盖三类事故中的一类。**
- 量级算术杀死「容量」框架：3663 条消息/月、峰值 7 人/小时、25 真人周活。bootstrap 7 路查询在这种表上是 ms 级——25 人同时重连 ≈ 175 次连接获取，40 连接的池 <1 秒排空。「重连→扇出→打满池→卡几分钟」这条因果链**算术上不自洽**：扇出只是放大器，池被占满几分钟的必要条件是**有长占用者在场**。
- 长占用者已有实证：`file.service.ts:3345` 注释自证「上下文拉取 材料=28563ms，同群另两轮 7ms/12ms」——踩中 rechunk（用户等待路径内联重切 30 万字合同）；`db.service.ts:50-60` 注释自证 08-28 12:14 材料检索并发重查询打满池、`connect ETIMEDOUT at RoomService.memberScope`。
- **08-31 11:24 事故有一半症状根本不在 DB 域**：那串 3001ms 503 是 `auth.guard.ts:351` 的**出站 HTTP fetch**（VX_API token/info，AbortSignal 3s）超时——鉴权不查本地 DB，且 3001ms 精准触发说明事件循环当时是活的。40975ms 的 `/api/rooms` 无报错静默等待，正是 `db.service.ts` 池注释**自己预言过的签名**（「队列没有上限也没有超时…症状是所有接口一起变慢而不是报错」）。两个症状（DB 侧静默排队 + 出站鉴权超时）同窗出现、且部署后 13 分钟才发生——**该事故尚未定根因，且候选病灶（池静默排队 / 上游 cg-api 或宿主机 / 出站链路）没有一个被现有方案的架构菜单覆盖**。推论③「泄漏/锁」字面无实证（读码未见连接泄漏形态、事务与 FOR UPDATE 全是短持有），但其内核——**病灶与负载无关、扩容族解法全部 miss**——被证据支持。
- 正确定性：**小系统的无上界操作病**。全仓无上界清单：DB 池队列无上限无获取超时（`db.service.ts:80` queueLimit:0，注释自认无兜底）、AI 轮次零全局并发闸（每 @可依 spawn 一个 dsh agent 子进程、30 分钟超时、08-27 起可多轮并行，`dsh.service.ts:513`）、rechunk 内联在真人等待路径、multer 100MB 内存缓冲、容器零资源限额（`cg-platform-deploy.sh:735` docker run 无 --cpus/--memory）。小系统的分钟级停摆来自**单次操作的方差**，不来自聚合流量的均值。

**② 架构不动拓扑；动的是「边界 + 可见性」，全是实现层小改**（按价值排序）：
1. **给 11:24 型事故装仪表（最高优先，先于一切再动手）**：池获取等待时长 + 队列深度记账（enqueue 事件已有，补时长）；鉴权出站结果分类记账（超时/401/5xx + 上游耗时）。判据：下一次同型事故发生时能一次定位。**没定根因前不买任何架构。**
2. **AI 轮次全局并发闸**（如 2-3）：全仓唯一重资源路径（agent 子进程 + 材料重查询扇出的唯一源头）却零闸，而 PDF OCR 都有 OCR_CONCURRENCY=2。
3. **rechunk 移出用户等待路径**：上传/抽取完成即预切，`relevantTextsFor` 只消费不生产。28.5 秒实证直接归零。
4. 池获取超时包装（等待超阈值主动 fail-fast 报错，替代静默 40 秒）——把不可见排队变成可见失败。
- drain（第 0 层）保留，它治的 06:21 类事故定性正确；A9「倾向缓不结案」维持原判。

**③ 「跨进程总线 + 多副本」在此量级 = 会塌的选择，判定成立。** 四条：(a) 服务一个算术上不存在的负载（差 2-3 个数量级）；(b) 与三类实证事故全部正交——停机顺序（已治）、长占用占池（Redis 不治）、鉴权出站超时（副本更多只会放大出站惊群）；(c) 给「一天 10 推、12 人直推无 gate」的工程节奏引入跨版本 pub/sub 兼容 + 新有状态依赖，失败面净增；(d) 单进程内存 SSE Map 在 25 用户量级**就是正确架构**，`bus.service.ts` 注释自知「扩 2 副本静默半哑」——这不是债，是边界声明。触发重估的物理条件写死：真人周活过 ~500 或单进程 CPU 常态 >60%，此前该项从「现在别碰」升格为「不做」。

**Trade-off / 未核验**：11:24 事故我也未定根因（候选三个，仪表先行正是为此）；cg-api token/info 是否查库未核（check-token 纯验签有部署脚本注释背书，info 端点未读码）；「同时段其他应用慢请求 0 条」不能排除宿主机/MySQL 级共因（其他应用可能当时零流量）。

**行动建议**：现有 brief 的 headline 定性需改写（「工程节奏 × 架构假设对撞」降为覆盖 06:21 类的局部解释），其第 2 层 #6（重查询侧）#7（心跳埋点）升格为主线——它们比标题更接近病灶。

### 核心假设

- prod 库直查数字（3663 条/25 真人/峰值 7 人）真实且未来一个季度量级不变——若 iDesk 突然全员推广，量级算术要重跑。
- 慢请求日志口径可信（`request-timing.middleware.ts` 挂 finish 不挂 close，排除客户端提前断开的假慢）。

### 可能出错的地方

- 若 11:24 根因最终是宿主机级（MySQL 所在机 IO/CPU），我的「实现层小改」清单治不了它——但仪表先行的裁决恰好对此免疫。
- AI 并发闸取值 2-3 是拍的量级不是算的，可能需要按 dsh 实测资源足迹调。

### 本次哪里思考得不够

未读 cg-api 侧代码验证 token/info 端点行为；未查 11:24 时段是否有 dsh 子进程在跑（无日志访问权限内的快捷路径）；未核 prod 宿主机上还跑着哪些容器共享 CPU。

### 如果 N 个月后证明决策错了，最可能的根因

「无上界操作」定性把某个真正的单点 bug（如 undici 出站连接池饥饿、或 MySQL 5.7 某表锁）当成了族病灶——仪表装上后若同型事故反复出现且指标全绿，说明观测点选错了层。

### 北极星触达

#3 决策超越直觉：直觉答案（上 Redis/多副本/扩容）被量级算术推翻；#1 二阶效应：给出「触发重估的物理条件」把「现在别碰」变成可结算的押注。

### essence 对齐自检（必填）

- **对位**：`action-type-over-aggressiveness`（选对动作类型 > 加大力度——扩池 20→40 是加力度，装闸/装仪表是换类型）；`gate-as-physical-fuse-not-business-metric`（池获取超时 = 物理保险丝）；`signal-without-judgment-needs-live-consumer`（enqueue 计数已存在但无消费者，补时长 + 判据才活）；`falsification-as-structure-not-just-skepticism`（触发重估条件写死 = 结构化证伪）。
- **反着走**：无 + 议题性质决定（本轮是外部系统架构裁决，未触 gg 自身机制类 essence 的张力面）。
- **cross-check 关键词**：容量/规模/方差/尾部/tail/scale/无上界/unbounded/bottleneck/瓶颈（grep essence-view.md，命中 F10 定价族与 #218 重入律，均非直接对位）。

### essence 候选（candidate-unverified，不直接 append）

- slug: `tiny-system-pathology-is-variance-not-volume`
- 一句话: 量级算术上不存在负载的系统里，分钟级停摆的病灶必然是单次操作的无上界性 + 不可见排队；容量族解法（扩池/副本/总线）与它正交——选解法族之前先做一次量级除法（峰值并发 × 单次持有时长 vs 资源上限）。
- 物理证据: cg-weilu 3663 条消息/月 + 28563ms rechunk 实证 + `db.service.ts` 无兜底队列自白 + 08-31 11:24 鉴权出站超时不在 DB 域。
- 是否已 append 到 essence.md: N（subagent 无 Agent 工具，留待夜巡/设计模式补 fresh 证伪审）

### 外部锚点

- `/Users/xuke/githubProject/monster/inbox/briefs/idesk-perf-remediation.md` ← 被裁决的方案本体
- `/Users/xuke/CGProject/cg-weilu/server/src/{db.service,auth.guard→common/,file.service,dsh.service}.ts` ← 物理证据源

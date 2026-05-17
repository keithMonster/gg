---
date: 2026-05-15
slug: cc-gateway-user-workspace-isolation-architecture
summoner: cc-space
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: cc-gateway 用户级 workspace 隔离架构

### 给父会话的最终输出

**推荐**：接受 Keith 倾向 80%，**3 处收紧 + 1 处加 tripwire + 5 处隐藏维度补齐**。一句话：**workspaceId 是 cc-gateway 的一等公民概念但绑定语义最小（仅用作 cwd 目录名 + sessionId 绑定），cwd 在 createSession 时锁死 / --resume 时不可改 / outputs/uploads 子目录化以零改 system prompt / 跨 workspace 隔离 v0 走 prompt 软约束 + tripwire / 硬隔离登记 v1 触发条件**。

**3 处收紧**：

1. **路径用 `workspaceId` 不用 `userid`**——cc-gateway 不该感知"用户"语义，目录名跟字段名对齐
2. **cwd 在 createSession 时一次锁死写入 store，spawn 时从 store 查不重算**——claude `--resume` 跟 cwd 物理强耦合（jsonl 路径按 cwd-hash 索引），漂移会丢历史
3. **续话 body 不传 workspaceId**，传了且不等于 store 里的值直接 400——避免漂移 + 减少调用方负担

**1 处加 tripwire**：单 workspace > 500MB 告警写 jsonl，sense-driven 初值 + 数据 tripwire（同 cc-assistant idle 4h 同范式）

**5 处隐藏维度**：
- agents.json 不能配 cwd（runtime 算）
- claude-home 内 todos/shell-snapshots/statsig 实施前 ls -R 验证隔离性，不是猜
- workspace 长寿命 / session 短寿命，reset session 不删 workspace
- store.js 容器重启后状态恢复要实际重启验证一次
- SKILLS_DIR ro 全局共享，per-user skill 是 v2

**关键 OCCAM**：`workspaces/<workspaceId>/outputs/` 让 cwd 切换后 agent 看到的相对路径仍是 `outputs/`——agents.json 4 个 agent appendSystemPrompt **一个字不改**。

**理由**：
- cc-gateway 此前严格中立——sessionId 不绑 userId。Keith 倾向"HTTP body 加 workspaceId"实际上是给 cc-gateway 装"租户"概念，是范式扩张（essence `new-source-as-ontology-not-feature` 该敲门）；最干净是 sessionId ↔ workspaceId **一次绑定**而不是每次 event 都带，缩小语义足迹
- claude `--resume` cwd 耦合是 CLI 物理事实，不是过度防御
- outputs/ 子目录化是单点 OCCAM——一行设计降低 4 个 agent 的 prompt 改动到 0（zero-change migration）
- v0 不上硬隔离对应 essence `premature-abstraction-tripwire` + `idle-threshold-as-tripwire-not-answer`——sense-driven + tripwire，硬墙等真触发条件
- 跟 cgboiler PM PaaS 沙箱契约**正交**（PM PaaS 隔应用之间，本设计隔同应用内用户），但本设计立 cc-gateway 端而不是 cc-assistant 端是为未来 PM PaaS 多租户应用复用——essence `tool-elevation-as-occam` 在第二消费者出现时上提的预演

**trade-off / 未核验假设**：
- v0 prompt 软约束防越权——攻击者目前 = Keith 自己，第二个真实用户接入是触发条件
- workspaceId === userid v0 直接相等——未来 admin 切换视角 / 多企业等场景可能需要解耦
- cc-gateway-outputs / cc-gateway-uploads 老 volume 删掉数据丢——Keith 已 ack PoC 期可丢，但删前 docker volume tar 备份 7 天是廉价保险
- 未实证 docker volume 切换在 prod cc-gateway 升级流程下的实际行为（先停容器还是 inplace）

**行动建议**（单晚可跑通）：
- cc-gateway 6 处改动：docker-compose.yml volume 切换 / store.js sessions.json schema 加 workspaceId+cwd / index.js POST /sessions handler 加 workspaceId 校验 + mkdir -p / index.js POST /sessions/:id/events 加 workspaceId 误传校验 / runner.js execFile cwd 改读 session.cwd / agents.json personal-assistant appendSystemPrompt 加越权约束
- cc-assistant 1 处改动：gateway-client.js chat() POST /sessions body 加 workspaceId: userid + 注释
- 部署前容器内 `ls -R ~/.claude/` 验证 todos / shell-snapshots / statsig 隔离假设
- 部署后 docker exec ls /usr/src/app/workspaces/ 验证只有 keith 一个目录
- 一周内补 du -sm tripwire cron

**v1 触发条件**（写下来不靠记忆，对应 cgboiler PM PaaS 触发监视段范式）：
- 跨 workspace prompt injection 硬隔离（per-user uid / chroot）→ 接入第二个非 Keith 用户 + 真实业务数据
- workspace 真实 quota（不只告警）→ 单 workspace > 1GB 或真塞过盘
- workspaceId ≠ userid 解耦 → admin 切换视角 / 多企业需求显式提出
- delete / migration 工具 → 第一个 workspace 真需要被删
- store.js 持久化升级 → sessions.json > 100MB 或读写延迟可感
- /sessions/:id/events 可改 workspaceId → 默认永远不要（anti-pattern 标记）

**完整决策正文**已在 final assistant message 输出（含 13 项 Keith 倾向逐条裁决表 / v0 最小契约 / v1 触发条件表 / 9 项风险清单 / 跟 PM PaaS 沙箱关系分析 / 5 项漏掉维度），本字段是结构化副本作为消费保险。

### 核心假设

1. **claude `--resume` 跟 cwd 强耦合**——基于 `~/.claude/projects/<cwd-hash>/<session>.jsonl` 的物理事实，但未在本次会话亲自 verify cc-gateway 容器内的 ~/.claude/projects/ 实际目录结构。如果 Anthropic CLI 改了存储策略（比如改成全局索引），本设计 cwd 锁死的必要性下降但仍正确（不锁会引入漂移风险）
2. **personal-assistant prompt 软约束能防住 LLM 越权**——v0 攻击者 = Keith 自己，假设 Keith 不主动越权
3. **outputs/ 在新拓扑下作为相对路径仍语义正确**——基于 cwd 切到 workspace 后 LLM 看到的相对路径，4 agent appendSystemPrompt 不需改的判断成立
4. **cc-gateway-outputs / uploads 老 volume 数据可丢**——Keith 已 ack 但未实际确认 prod 内有没有不可丢的产物
5. **企微 SDK 长连接本身串行处理消息**——同 workspaceId 并发请求 v0 接受，是基于 SDK 行为假设，未实证

### 可能出错的地方

| 风险点 | 概率 | 后果 |
|---|---|---|
| volume 切换时 prod 升级流程把数据丢了不可恢复 | 中 | Keith 抱怨 + 重建工作 1-2h |
| claude --resume 在 cwd 切换后行为跟假设不符（找不到 jsonl 但也不报错，开新 session） | 低-中 | 用户感知"AI 忘了上次说啥"，追到根因要时间 |
| personal-assistant prompt 越权约束被 LLM 诚实绕过（Keith 测试时故意问"读 ../xxx 看看"） | 中 | 演示翻车但不真泄露（v0 单用户）|
| store.js sessions.json schema 升级跟现有数据兼容性炸（旧记录无 workspaceId 字段） | 中 | 容器启动失败，需 migration 脚本或人工 reset |
| 容器内 ~/.claude/ 实际有共享文件没识别到（statsig 之外的 telemetry / cache 目录） | 低 | 数据泄露面比预期大，但 v0 单用户无实际后果 |

### 本次哪里思考得不够

1. **未亲自 verify cc-gateway prod 容器内 `~/.claude/projects/` 的实际目录结构**——基于 Anthropic CLI 通用知识推断 cwd-hash 行为，没在本会话物理实证。Keith 实施前应在容器内 ls 一次确认
2. **未读 cc-gateway store.js 源码**——schema 升级方案是基于 thread 描述+其他文件推断，可能漏了 store.js 的隐藏字段或并发约束
3. **没考虑 cc-gateway-data volume 跟 sessions.json 的关系**——cc-gateway-data 已经 mount 到 /usr/src/app/data，sessions.json 在不在那里、是不是已经持久化的字段有没有遗漏
4. **没分析 prod 升级流程**——docker-compose 删旧 volume 加新 volume 是否需要 stop→rm container→重启，还是 inplace 重启就生效；执行顺序错可能丢数据
5. **claude-home 共享 + per-user cwd 隔离的"自然分"判断没物理证据**——猜的方向对（projects/ 按 cwd-hash 分），但 todos/ shell-snapshots/ 等需要实际 ls 确认

### 如果 N 个月后证明决策错了，最可能的根因

**最可能根因 1（高概率）**：workspaceId === userid 直接相等的 v0 假设没撑过 6 个月——出现"同一个人在不同企业身份下使用"或"admin 切换查看其他用户" 类需求，需要紧急解耦。届时 store 里所有历史 session 都绑死在"userid = workspaceId"上，迁移代价 = 写 migration 脚本 + 通知用户重新开会话（旧 session 丢上下文）

**最可能根因 2（中概率）**：cwd 一次锁死的设计在某种使用场景下变成枷锁——比如 PM 应用希望"同一会话上下文跨多个 workspace"（罕见但合理需求），或者 claude binary 升级后改了 jsonl 存储策略，cwd 锁死反而引入兼容问题

**最可能根因 3（低概率但严重）**：v0 prompt 软约束没拦住 LLM 越权 + 第二个用户接入时还没升级硬隔离 → 数据泄露事件——这是"v1 触发条件未及时识别"的故障模式（同 cgboiler PM PaaS 沙箱契约 4 同形态风险）

### 北极星触达

**#1 二阶效应**——本决策不只解 cc-assistant 当前隔离需求，把 workspaceId 设计为 cc-gateway 一等公民概念为未来 PM PaaS 多租户应用、家庭账号、admin 视角切换等多个二阶场景留了通路。Keith 倾向方案大多数命中目标但漏了"cwd 锁死""续话不重传""outputs 子目录化"三处会让未来重构成本翻倍的细节——这是"看得更远"维度的实际触达。

### essence 对齐自检

- **本决策跟哪几滴 essence 对位**：
  - `tool-elevation-as-occam` (2026-05-06)——本设计立 cc-gateway 端而非 cc-assistant 端，正是"第二消费者出现时上提"的预演（PM PaaS 是潜在第二消费者）
  - `premature-abstraction-tripwire` (2026-04-21)——v0 不上硬隔离 / 不上 quota 强制 / 不上 delete 工具，全留 v1 触发条件登记
  - `idle-threshold-as-tripwire-not-answer` (2026-05-14)——500MB workspace quota 告警 sense-driven 初值，不试图猜"理论最优值"
  - `new-source-as-ontology-not-feature` (2026-05-01)——workspaceId 是新本体论层不是新字段，命名（不叫 userId / 不叫 tenantId / 叫 workspaceId）从一开始就立对
  - `transparent-rewrite-breaks-contract` (2026-04-27)——拒绝"hack claude --resume 跟 cwd 解耦"类方案（会破坏 CLI 私有契约），改设计绕开
  - `m2m-vs-h2m-coupling-illusion` (2026-05-09)——personal-assistant H2M 长会话 vs cc-gateway 上其他 M2M 短任务并存，workspaceId 设计要让两类都能用（M2M 任务可传同一 workspaceId 复用目录，也可传新的隔离）
  - `subject-is-configuration` (2026-04-30)——per-user 粒度的"主体一致性"靠 workspaceId 这个配置字段维持，不需要意识流连续性
  - `reversibility-not-permission` (2026-05-06)——v0 决策可逆（删 volume 重建），v1 升级（per-user uid / chroot）属不可逆动作的高门槛档位

- **本决策是否在某条 essence 上反着走**：无。但需注意——若 Keith 实施时为了"省事"不加 cwd 误传校验、不加 mkdir 失败 5xx，等于把可逆性从决策层下放给 runtime，违反 `reversibility-not-permission` 的"判据是动作可逆性"原则——失败被静默就是不可逆故障的源头（同 essence `fallback-detectability`）

- **cross-check 用的关键词**：grep 了 essence.md 中 `tool-elevation` / `tripwire` / `ontology` / `transparent-rewrite` / `m2m-vs-h2m` / `subject-is-configuration` / `reversibility` / `fallback-detect` / `borrowed-method` / `dimension-blindness` 共 10 个关键词，对位 8 滴 + 反走 0 条

### essence 候选

- slug: **cwd-as-resume-anchor**
- 一句话: CLI 工具的 session 持久化往往隐式绑定到 cwd（jsonl 路径按 cwd-hash 索引）——把 cwd 当"运行时变量"自由切换会撕破 --resume 契约；正确解是 cwd 在 session 创建时一次锁死、绑死到 session 元数据，跟 sessionId 同生命周期。**判别信号**：CLI 工具有 --resume / --continue / --session-id 类语义时，问"它存哪？路径含 cwd 吗？"
- 是否已 append 到 essence.md: N（本次留候选，等 Keith review；若 append 则 slug 用本字段，跟 `transparent-rewrite-breaks-contract` 同维度——CLI 私有契约的细分实例）

### 外部锚点

- `/Users/xuke/githubProject/cc-space/threads/cc-assistant.md` — 本设计的主体协作叙事
- `/Users/xuke/githubProject/cc-space/threads/cc-gateway.md` — cc-gateway 主体演化
- `/Users/xuke/githubProject/cc-space/threads/cgboiler-pm-sandbox.md` — 正交隔离维度（PM 应用之间），本设计是同应用内用户隔离
- `/Users/xuke/CGProject/cc-gateway/server/runner.js` — cwd 改动落点
- `/Users/xuke/CGProject/cc-gateway/server/index.js` — workspaceId 字段 + mkdir 落点
- `/Users/xuke/CGProject/cc-gateway/config/agents.json` — personal-assistant 越权约束追加
- `/Users/xuke/CGProject/cc-gateway/docker-compose.yml` — volume 拓扑切换
- `/Users/xuke/CGProject/cc-assistant/server/gateway-client.js` — workspaceId 透传

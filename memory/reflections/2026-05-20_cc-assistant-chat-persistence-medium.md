---
date: 2026-05-20
slug: cc-assistant-chat-persistence-medium
summoner: monster (cc-assistant Phase 1 启动前架构层裁决)
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: cc-assistant 2.0 chat 历史持久化介质选型

### 给父会话的最终输出（必填）

**推荐**：**A 变体（强化版）独立 SQLite 单文件**——`~/CGProject/cc-assistant/data/sessions.db` + better-sqlite3，沿用现有 `cc_assistant_data` named volume。否决 B（cgManager 复用）、C（cgPlatform 收编）、D（hybrid）。

**关键理由**：

1. **C 是 categorical 错误**：cgPlatform 沙箱契约 1-9 整套建立在"PM 应用=AI 生成代码+AI 运行+多 PM 出品"前提上，cc-assistant 是 Keith × Claude 长期共建项目，根本不在这个集合里。keyi-memory 2026-05-18 已走过同形态纠偏（"cgPlatform 是 PM 沙箱专用纯净库，可依是受信长期工程非试错 PM 应用，错配 → 撤"），cc-assistant 复用同结论。强收编 = 同时违反 essence `borrowed-method-as-mini-source` + `extraction-meta-inheritance`。

2. **B 不是错的，是收益不在当下成本在当下**：cc-assistant 当前 0 DB 依赖（核实过 package.json），首次直连付 mysql 依赖 + 凭据 + 架构基调拉裂三笔成本，收益（"未来检索 / dashboard"）属 essence `theory-gap-without-data` 在介质选型上的活体——用想象需求驱动当下架构 = 抽象先行陷阱。父会话 prompt 里写的"chat 量级污染 cgManager"理由不立得住（cgManager 业务表本来就百万级），真正弱点是首次直连的结构性成本。父会话 prompt 里 A 缺点"脱离体系"也不立得住——database/CLAUDE.md 辖域是业务库治理，runtime state 不进 SSOT 是有意识切分。

3. **A 在 cc-assistant 上是真 OCCAM**：单实例容器（企微长连接物理约束，AGENT-DESIGN §1 已锁）+ 单 SQLite 文件 + 已有 named volume = 真正最简。better-sqlite3 同步 API、零网络、零凭据、跟 data/agent-events.jsonl / session-resets.jsonl 同盘，运维拓扑天然对齐。可逆性高（单文件 .dump 几小时迁出，比从 cgManager 在线迁更便宜）= essence `reversibility-not-permission` 落地。

4. **D（hybrid）违反 SSOT 且增错误识别成本**：异步双写命中 essence `fallback-detectability`——失败识别隐性成本高。

**Trade-off / 未核验假设**：

- 假设 better-sqlite3 在 node22-slim + nexus npm-proxy 环境装得上（10K+ stars 项目 prebuilt binary 通常顺，未实测，可能需要 Dockerfile 加 build-essential）
- 备份不进 cgManager 备份链是真成本——Phase 2 上 cron `.backup` 命令解决，时间窗口短
- "未来真要做 dashboard"场景 SQLite 可以跨进程只读（WAL 默认开），但单消费方变两消费方时是上提到 cgManager 的合法触发点（essence `tool-elevation-as-occam`），不是现在做
- 红队 5 条全部被击败或承认范围明确（详 final message），置信度 5/5

**行动建议（优先级）**：

1. Phase 1 一并做：在 AGENT-DESIGN §8 实施路线基础上加持久化分支 9 步骤（依赖 / schema / session.js 改造 / 滑窗与持久化契约 / query_sessions.sh / docker-compose 不动 / cron 推迟 Phase 2 / tripwire / §9 文档更新）
2. AGENT-DESIGN §1 非目标"❌ session 持久化"删掉 + §3.2 加一行"sessionMap 是内存 cache，物理 SSOT 是 data/sessions.db"
3. database/CLAUDE.md cgPlatform 段后新增"runtime state 不进 DB 治理体系"段（兜父会话副议 #4 元规则；落点见 final message）
4. cc-assistant 是否进 cg-platform 体系（父会话关键问题 3）= **否，未来也不应该**——它是受信内部基建定位同 cc-gateway，不是 cg-meetos 同档的 PM 试错应用

### 核心假设

- cgPlatform 契约体系的承重论证（"AI 生成代码 + AI 运行 + 多 PM 出品 → 攻击面比人工写代码高一个量级 → 6 条沙箱契约托底"）是稳定的；cc-assistant 落在这个集合外是 categorical 不是程度差异
- cc-assistant 在可见未来仍是受信内部基建（同 cc-gateway 档），不会演化成 PM 试错产物
- 单实例容器物理约束（@wecom/aibot-node-sdk 单 botId 单 client）在 v1+ 仍成立，单 SQLite 文件不会因横向扩容失效
- Keith"重新找得到"的诉求量级 = 偶发人工查询 + 未来可能的 dashboard，不是高并发实时检索

### 可能出错的地方

- **概率最高**：500MB tripwire 触发后没有立即决策升级路径——文档里写了"触发不自动清，只通知 Keith review"，但 review 时 Keith 可能不在场或忘记。**缓解：tripwire 落 jsonl 时同时走 notify skill 推一条 warning**
- **概率中**：cc-assistant 未来演化轨迹超出"受信内部基建"假设——比如 Keith 决定开源 cc-assistant / 接入第二家公司同款部署 / 演化成 cgboiler 全员小助理 SaaS。这些场景下 SQLite 单文件可能不再适合
- **概率低**：better-sqlite3 native module 在某次镜像升级编译失败。已识别预防（Dockerfile 加 build-essential 段）
- **概率低**：Phase 2 备份 cron 没上、第一次容器 rebuild 丢历史。时间窗口可控

### 本次哪里思考得不够

1. **没问"现存哪些 user 的 session 已经在内存里跑着"**——切换到 SQLite 时是否需要冷启动期短停服 + 灌入空白盘的 migration plan？AGENT-DESIGN §7 灰度方案里 USE_AGENT=false→true 切换时旧 gateway-client.js 内存 sessionMap 直接丢弃，与 sessions.db 空盘启动是兼容的，但没显式 ack
2. **没量化 messages 字段大小**：spike 阶段 ~120 行单文件、3.6K~6.7K token，转换成 messages_json 列字节数没估。滑窗 15 turn × 30 条 × 假设单条 1KB = 30KB/user × 假设 100 user = 3MB——离 500MB 还远，但应该跑过实际数据估一次
3. **better-sqlite3 vs node 内置 sqlite（node 22 起 experimental）**：node22-slim 的 `node:sqlite` experimental API 已存在，可能根本不需要 better-sqlite3 npm 依赖。**这是真盲点**——本次没读 node 22 release notes，直接走 better-sqlite3 习惯路径。父会话实施前值得 30 秒 grep 一下 `node --experimental-sqlite` 是否稳定到可用
4. **没核实"messages 字段 BLOB vs TEXT"**：JSON.stringify 后 messages 含中文，TEXT 列 UTF8 OK，但极端长 messages（多轮 tool_use 累积）单行可能上 MB——SQLite 单行默认上限 1GB 不会爆，但 TEXT 列在 SELECT 时全量加载，与"按需取窗口段"的优化（如果未来要做）不友好。**结构上是对的**，但物理量级真没核
5. **D 选项的展开维度可能不止"主存 SQLite + 异步推 cgManager 摘要"**——还有另一种 D' 形态："SQLite 主存 + 周期性快照 SQL dump 进 cgManager 当冷归档"。没展开因为这两者本质同一种 fallback-detectability 问题，但承认没穷尽
6. **滑动窗口的"messages 字段一字一致"契约是新立的**——磁盘 = 内存 = 同一份 messages（裁剪后），这是合并自父会话 prompt 里写的滑窗设计 + 本次持久化决策；契约本身没经过单独红队，可能在"刚启动 warm load 完发现内存里被清掉的旧 turn 想恢复"场景下出现尴尬（但实际不会，因为 reset 触发时本来就是双删）

### 如果 N 个月后证明决策错了，最可能的根因

**主路径**：cc-assistant 演化为"接入第二个消费方 / dashboard 真做出来 / 跨 user 检索需求出现" → SQLite 不再够用 → 上提到 cgManager（**注意不是 cgPlatform**，已在 database/CLAUDE.md 元规则段写清）。这条根因发生时不算"决策错了"，是"决策按预设触发条件升级"，essence `tool-elevation-as-occam` 命中预期路径。

**真错路径**：500MB tripwire 触发时已经晚了——chat 历史增长非线性（某 user 暴聊一周占 50MB），单文件读写延迟在某个临界点突然变高、影响企微响应时间（5s 超时变成 SQLite 锁等待 30s），用户体验崩在被发现之前。**防御**：tripwire 加细粒度，不只总文件大小，单 user messages_json 字段大小也观测（> 5MB 单 user 落 jsonl）。

**最不应该但可能**：cc-assistant 真的开源 / 跨公司部署，这时 SQLite 已经在多实例下失效（多 bot 实例不能共享单 SQLite 文件做并发写），但 cgManager / cgPlatform 也都不再适用（不是川锅独占场景了）——需要切 PostgreSQL / Redis / 别的。这个场景超出本次决策辖域。

### 北极星触达

**#3 决策超越直觉**——父会话给的 A/B/C/D 4 候选 + 倾向 B 是直觉锚定（B 看起来"最贴范式"），但本次决策跳出 4 候选回到承重原理（cgPlatform 契约体系前提论证 + keyi-memory 同形态先例 + cc-assistant 不属于 PM 应用集合），把"chat 数据放哪"问题拉到"它在哪个 SSOT 边界里"层，结论与父会话直觉对齐到 A 但**否决了 B 和 C 的两个貌似合理候选的"合理性"本身**。

**附带触达 #1 二阶效应**：顺手把"runtime state 不进 DB 治理体系"作为元规则沉淀到 database/CLAUDE.md——下次任何工作区遇到同类问题（"我的 jsonl 涨大了要不要进数据库"）能直接 grep 到答案，避免每次重决策。这是把单次决策的承重论证抬到 SSOT 层。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**（列 slug）：
  - `extraction-meta-inheritance` (2026-04-29) + `borrowed-method-as-mini-source` (2026-05-08) → 反对 C：把 cc-assistant 视作 cgPlatform 应用 = 在 cg-platform 体系里造 cc-assistant 的"PM 应用迷你版"，反向继承"AI 不可信代码"元约束
  - `tool-elevation-as-occam` (2026-05-06) → 支撑"500MB tripwire + 第二消费方触发"作为升级到 cgManager 的预设路径——第二个消费者出现时上提是 OCCAM 不是过度工程
  - `theory-gap-without-data` (2026-05-06) → 反对 B 当前实施：用想象的"未来 dashboard / 跨服务 JOIN"驱动当下架构选择 = 在没数据时识别理论缺口
  - `premature-abstraction-tripwire` (2026-04-21) + `idle-threshold-as-tripwire-not-answer` (2026-05-14) → 落地"500MB 物理保险丝 + 5MB 单 user 字段细粒度"作为升级触发器而非提前抽象
  - `reversibility-not-permission` (2026-05-06) → A 的关键优势是可逆性高（单文件 .dump 迁出）而非"许可低"
  - `fallback-detectability` (2026-05-06) → 反对 D（hybrid 主存 SQLite + 异步推摘要）：异步双写失败识别成本高
  - `ssot-as-loadable-fragment` (2026-05-08) → 把"runtime state 不进 DB 治理"作为 database/CLAUDE.md 的延伸段，SSOT 不必单文件但语义边界要显式
  - `network-cannot-cut-what-shares-tuple` (2026-05-19) → cgPlatform / cgManager 同 host:port:9033 实例，"放进 cgPlatform"和"放进 cgManager"在网络隔离层面零差异，物理切只在"是否进 PM 沙箱契约辖域"——把 cc-assistant 强塞进 cgPlatform 不会获得任何"网络层隔离"收益，因为 cgPlatform 本就不靠网络层与 cgManager 隔离

- **本决策是否在某条 essence 上反着走**（无 = 明示"无 + 议题性质决定"）：
  - **无明显反着走**——议题性质是"承重抽象边界归属决策"，正好是 essence 体系的核心适用域，多条 essence 同向支撑同一结论
  - **潜在张力（未展开）**：决策"立即一并做 SQLite 持久化进 Phase 1"vs essence `premature-abstraction-tripwire`——能否说"持久化在 Phase 1 完工的现状下属于过早抽象"？审视后判定：不属于，因为 Keith 已明示反转"非目标 ❌ session 持久化"为必做项，需求是 already-validated 非生造，不踩 tripwire 警戒；但仍标"潜在张力"留痕

- **cross-check 用的关键词**（物理证据）：grep `tool-elevation-as-occam|borrowed-method-as-mini-source|extraction-meta-inheritance|new-source-as-ontology-not-feature|premature-abstraction-tripwire|network-cannot-cut-what-shares-tuple|ssot-as-loadable-fragment|theory-gap-without-data|ssot-distillation-vs-buffering` 拿到 9 条命中段落（命中 #157/243/268/273/283/309/379/385/493），加 reversibility-not-permission / fallback-detectability / idle-threshold-as-tripwire-not-answer 共 11+ 条 cross-check

### essence 候选（可选）

- slug: `runtime-state-vs-business-data-distinct-ssot-domains`
- 一句话: 单工作区 runtime 内部状态（jsonl / SQLite）和跨工作区共享的业务数据（DB 表）属于不同 SSOT 辖域——把前者塞进后者的治理体系会反向稀释"业务数据 SSOT"的语义判别力，正解是在工作区本地持久化 + 显式触发器升级路径（第二消费方 / 物理量级 / 跨工作区 JOIN 真需求）。是 `tool-elevation-as-occam` 在"什么时候该上提到共享层"维度的反向锚——上提的合法触发不是审美（"看起来该进数据库"），是被消费方 OUT-NUMBERS 现状（单消费方变多消费方）+ 物理量级触发器。
- 是否已 append 到 essence.md: Y

### 外部锚点

- `~/githubProject/monster/threads/cc-assistant.md` ← cc-assistant 主体协作叙事（2026-05-20 spike 通过 + design-brief 落段）
- `~/githubProject/monster/cc-assistant/AGENT-DESIGN.md` ← Phase 1 设计 brief，本决策修订 §1 非目标 + §3.2 + §9
- `~/githubProject/monster/threads/cg-platform.md` ← cgPlatform 沙箱契约体系（用于论证 C 错配）
- `~/githubProject/monster/threads/keyi-memory.md` ← 同形态 nearby 先例（库选址三轮纠偏的相同结论）
- `~/githubProject/monster/threads/cg-meetos.md` ← 首个真实 cg-platform dogfood，本决策的对照系
- `~/githubProject/monster/database/CLAUDE.md` ← DB 治理 SSOT，本决策辐射新增"runtime state 不进治理体系"段

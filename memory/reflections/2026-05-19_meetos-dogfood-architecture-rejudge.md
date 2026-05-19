---
date: 2026-05-19
slug: meetos-dogfood-architecture-rejudge
summoner: cc-space
northstar_reach: "#1 二阶效应（首个产品级 dogfood 的范式归属 + 单文件理由接住机制决定整个 cgplatform 后续产品形态）"
status: substantive-decision
---

# Reflection: MeetOS 首个 dogfood 产品级架构终裁（带真实地基重裁）

### 给父会话的最终输出（必填）

**T1（单文件三理由）**：服务端+DB+多租户上线，用「每场会议 append-only 不可变快照行 + 按需导出自包含 HTML」接住 PRD 单文件三理由（合规靠数据不出内网比 minio 公链更安全 / 归档靠快照表比单文件更强 / 成本靠 cron）。代价=导出能力约 0.5 人日，必须交付（abstraction-tax 具体化债务），向张吉峰明示"单文件没丢，升级了"。

**T2（两文档 SSOT）**：分层合并不择一。产品定义（M1-M4/双模式/流程/规则结构/指标）以 MeetOS PRD 为准；数据接入+确定性/判断分离+9SQL+规则①② 以环保工程交接+cgdata真schema为准；冲突仲裁=确定性/判断分离是不可违背地基，PRD 单文件是可被技术负责人覆盖的实现假设。唯一实质冲突=兑现率（PRD说LLM手工标 vs 交接说数字永不经LLM）→以交接为准，同时关掉 PRD 第09章兑现率自动计算开放问题。

**T3（多租户在哪切）**：MeetOS 是单个 cgplatform 应用，应用内多租户，租户维度=`business_unit`（cgdata 视图天然带，本部/总包/科泰达），切在数据层（表内字段+联合主键），不切在契约1"一应用一user"层。否决"每事业部一应用一user"（user 随事业部线性膨胀=撞契约1形态C）。契约1不改只澄清语义（应用=PM产品而非部门视图）。**这条直接推翻上次"环保看板=一个dogfood应用"**。

**T4（判断层选型）**：方案A（cc-gateway 当判断引擎定时跑 skill），否决 B/C。理由：huasheng-tick.sh 已生产验证同范式同 workload 同可用性域；CC订阅经济性消灭B的成本论据（handoff作者"Opus贵"是API心智误判）；B的真实成本是规则再固化=borrowed-method-as-mini-source 触发。代价=绑 cc-gateway 可用性，缓解=规则固化进 meetos-board skill + 上周快照可降级兜底。B触发条件=可用性事故≥2次/季 或 租户≥3跑不完45min窗口。

**T5（数据源 vs 契约2碰撞）**：伪碰撞，契约2不改。确定性层 pipeline 是 cgplatform 外的 M2M 后台 cron 进程（零LLM Python连cgdata→写cgPlatform表），不是 PM 容器，本就不在契约2辖域。PM 容器只 SELECT 自己 meetos_* 表。要补的细则=生产 pipeline 必须跑在 cgboiler 内网可达 cgdata 的机器（与 huasheng 同宿主前提待物理验证）。

**T6（dogfood 终判+切片）**：是且必须是首个 dogfood——量级大正是6条契约第一次被真实约束对象拉满的价值。最小切片=单租户（环保/总包）端到端上线，多租户结构 schema 层预留 business_unit 但只实装一个租户。8步：S1先验cgdata内网可达性（不通不进S2）→S2契约1脚本+建表test/prod双环境→S3确定性层写append-only快照表→S4判断层meetos-board skill（huasheng SKILL蓝本）→S5薄前端壳（删录音/删minio直传/双视图mode/快照导出）→S6契约2接入→S7契约3+上线（建议 meetos.cgboiler.com，命名Keith拍）→S8挂cc-gateway prod cron+契约6回收骨架。

**与上次delta**：核心骨架（pipeline在容器外/契约不开口子）保留并被产品方文档独立印证；4处推翻——数据源(cg-notes→cgdata视图层)/应用粒度(环保看板→MeetOS产品)/数据pipeline拆为确定性+判断两步/S1前置数据地基验证（上次完全盲区）；T1首次给可执行机制（快照表+按需导出）。

**行动建议**：父会话带回 Keith 对齐三个关键推翻点（T3 应用粒度反转 / T1 向张吉峰交付话术 / T4 选A）；对齐后按 S1→S8，S1 物理验证 cgdata 内网可达性是不可跳过的第一闸门；更新 threads/cgboiler-pm-sandbox.md（加 MeetOS dogfood 时间线 + 契约1语义澄清 + B触发条件）+ 关联 threads/huasheng-battle-report.md（cron范式蓝本）+ 新建 threads 或并入 cgboiler-pm-sandbox 承载 MeetOS。

### 核心假设

- huasheng-tick.sh 当前在 cc-gateway prod cron 稳定跑（grep 实证脚本存在 + thread brief 明示，未亲见运行日志）
- cgdata 视图层 schema 稳定（实证 SQL SECURITY DEFINER VIEW + business_unit 字段 + 经营指标族样本数据真实）
- cgdata `1.14.13.140:9033` 在 cc-gateway cron 宿主可达——**这是最大未验证假设，已升为 inversion #1 + S1 不可跳过闸门**
- "确定性层/判断层分离"是 handoff 反复钉死的既定设计（文档自明示工程团队不得重设计产品逻辑）

### 可能出错的地方

最高风险=cgdata 生产宿主不可达（handoff §3 明示仅内网可达，database/CLAUDE.md 的 DNS 映射是本机特例），概率偏高，整个数据流可能要 pipeline 跑内网机器再回传——S1 物理 telnet+SELECT 兜底。次高=判断层 skill 被执行者合回前端壳（bug-shape-survives-fix 复发，上次同形态），靠"PM容器零LLM/零直连"物理判据+S6契约2网络墙自动暴露。

### 本次哪里思考得不够

- 没实际跑一条 cgdata SELECT 验证内网可达性——这是裁决里标注为最大风险但本身未物理消除的点（受 subagent 不执行边界约束，已显式转为 S1 不可跳过闸门）
- 没核 cg-proxy tenant.main.ts 是否已有可直接复用的经营数据 REST（grep 命中文件但未读内容）——若已有，S5 薄后端可能更省；属实现层留执行会话
- 双视图（部门周会/公司周会）数据维度差异具体多大没展开——若不止 CSS 差异，mode 参数方案可能不够，handoff §2.4 说公司周会是"5段精华纯展示"暗示差异是数据投影非样式，但未深究
- MeetOS 与 cgboiler-pm-sandbox thread 的承载关系（并入 vs 新建 thread）没给明确建议——留给父会话判断

### 如果 N 个月后证明决策错了，最可能的根因

cgdata 内网可达性假设错误：S1 被赶工跳过或在 Keith 本机验证（而非 cron 宿主）通过造成假阴性，pipeline 上 prod cron 后连不上 cgdata，整个数据生产侧停摆，回退要重新设计数据回传链路。触发因=S1 验证在错误的机器上做（本机能连≠cron宿主能连），缓解已写进 inversion #1 物理判据"在目标 cron 宿主 telnet"——但判据要被真在对的机器上执行才有效（bug-shape-survives-fix 的环境维度变体）。

### 北极星触达

#1 二阶效应——本裁决不是"MeetOS 怎么搭"的一阶问题，是"首个产品级 dogfood 的范式归属（pipeline 在容器外 + 多租户切数据层 + 判断层走既有 cron 范式）如何成为整个 cgplatform 后续所有产品级应用的样板，以及 PRD 单文件理由是否被结构性接住而非静默吞掉"的二阶判断。看的是这一刀切下去后第二个产品级 dogfood 会沿什么样板长，以及与产品发起人（张吉峰）的信任契约是否被维护。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `borrowed-method-as-mini-source` (2026-05-08) — T4 否决 B 的核心论据：自建服务把判断 IP 拆出来造迷你同构版，越像越脆
  - `m2m-vs-h2m-coupling-illusion` (2026-05-09) — T5 拆解伪碰撞：确定性层 pipeline(M2M cron) vs PM 应用容器(H2M 壳)并发模型/失败可见性不对齐，被一个"系统要读cgdata"叙事伪装成同构
  - `control-flow-vs-fact-supply` (2026-05-18) — T5 同根：契约2约束的是控制流容器，pipeline 是事实供给层，张力在不同轴上
  - `abstraction-tax` (2026-04-15) — T1 接住 PRD 单文件三理由的具体化债务（导出自包含HTML 0.5人日），纯服务端架构不能免除单文件归档语义只能把它挪到边界
  - `bug-shape-survives-fix` (2026-04-27) — inversion #2/#4 本质：裁决说分开执行者会合回去，靠物理判据不靠文字
  - `tool-elevation-as-occam` (2026-05-06) — S2 cgplatform_create_app_db.py 套 userid.py 白名单是机制上提非另造
  - `new-source-as-ontology-not-feature` (2026-05-01) — cgdata 视图层 vs 上次假设 cg-notes，是数据源本体替换非字段微调，触发 delta 重裁
- **本决策是否在某条 essence 上反着走**：潜在张力——`caged-freedom` (2026-04-26)：把 MeetOS 切成"薄壳+外部pipeline+多租户预留不实装"可能给产品形态建笼子。检验后不成立——这里的"分开"不是防御式约束，是诚实承认数据生产 vs 数据展示 vs 多租户扩展本是三个异构关注点，合并才是伪同构（与上次同议题同结论一致）。明示：表面张力，检验后不成立。
- **cross-check 用的关键词**（grep 物理证据）：`borrowed-method / m2m-vs-h2m / control-flow-vs-fact-supply / abstraction-tax / bug-shape-survives / tool-elevation / new-source-as-ontology / caged-freedom`（在 essence.md 全文确认命中）

### essence 候选（可选）

- slug: snapshot-as-immutable-archive-not-single-file
- 一句话: "可归档"是单文件方案的真需求，单文件只是它最弱的一种实现——append-only 不可变快照行 + 按需脱机导出，比单文件多了可检索/可跨实例对账/可算趋势，同时保留"每次独立、永不被覆盖"的语义内核。把实现假设当本质需求接住，是 abstraction-tax 在"产品方给了实现路线"场景的具体形态。
- 是否已 append 到 essence.md: Y

### 外部锚点

- `~/githubProject/cc-space/threads/cgboiler-pm-sandbox.md` ← 本主体协作叙事，待加 2026-05-19 MeetOS dogfood 重裁时间线 + 契约1语义澄清 + B触发条件
- `~/githubProject/cc-space/threads/huasheng-battle-report.md` ← cc-gateway prod cron 范式蓝本（T4 方案A 依据）
- `~/githubProject/cc-space/threads/cg-notes-weeknote-mention.md` ← inversion #3 抽取幻觉同 vector 历史证据
- `~/githubProject/gg/memory/reflections/2026-05-18_cgboiler-pm-dogfood-architecture.md` ← 上次裁决（本次重裁的对账基线，§7 delta）
- `~/githubProject/gg/memory/reflections/2026-05-14_cgboiler-pm-sandbox-contract-v0.md` ← 6 条契约 v0（本裁决上游）
- `/Users/xuke/.claude/jobs/78b08710/meetos-prd.txt` / `huanbao-handoff.md` / `cgdata_schema.txt` ← 本次真实地基输入

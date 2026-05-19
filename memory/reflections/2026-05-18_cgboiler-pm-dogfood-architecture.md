---
date: 2026-05-18
slug: cgboiler-pm-dogfood-architecture
summoner: cc-space
northstar_reach: "#1 二阶效应（范式归属裁定影响整个 cgplatform dogfood 形态与契约 2 完整性）"
status: substantive-decision
---

# Reflection: cgboiler PM PaaS 首个 dogfood（环保周会看板）架构裁决

### 给父会话的最终输出（必填）

**B（归属）裁定**：数据抽取层归属现有"cg-notes/cgdata → LLM → 周期产物"pipeline 家族（与 huasheng-battle-report 同构、同宿主 cc-gateway prod cron、同范式）。cgplatform 这一侧只承载前端壳 + 持久化 + 上线，**不承载数据抽取**。在这个切法下它**是典型 PaaS 场景**，可作首个 dogfood；若坚持自带抽取则不典型且污染契约 2——但 Keith 已拍它是 dogfood，裁决用 B 让它回到典型形态。

**A（数据流）裁定**：选 (b)。外部 pipeline 预生成 → 写 `cgPlatform.huanbao_weekly_*` 表 → PM 应用 MySQL user 仅 SELECT 自己 `huanbao_*` 表。否决 (a)（撞契约 2 + 重 LLM 放进攻击面最大的容器）和 (c)（给 cg-proxy 加重 LLM 抽取端点违反其中立定位 + 跟 huasheng 逻辑重复）。

**理由链核心**：huasheng-battle-report 已是"cg-notes→DB→LLM 抽结构化→cron 周期→消费"且已迁 cc-gateway prod cron，这个 dogfood 数据层是同一流水线同一段，差别只在末端消费形态。应用内自带抽取 = 造 huasheng 迷你同构版（essence `borrowed-method-as-mini-source`）+ 给契约 2 开口子。契约 2 在这里"挡路"是它正确工作的证据，不是设计错。录音去掉后"后台 LLM 综合议题决议/公司周会草稿"归数据生产侧 pipeline 预生成（作为 `huanbao_weekly_summary` 字段写表，应用只读），既保留能力又不在 PM 容器放 LLM 调用。

**目标架构**：数据生产侧（cgplatform 外，复用 fastgpt_mongo.py / cg-notes-export skill / huasheng LLM 抽取 prompt 范式 / cc-gateway prod cron）写 `huanbao_weekly_*` 表 → 数据展示侧（cgplatform PM 应用，薄壳，物理切 cgManager，只读自己表，渲染双视图 mode，删录音）。

**7 步实施切分**（每步标驱动的 cgplatform 基建物）：
- S1 跑契约 1：建 `cgplatform_create_app_db.py`（套 userid.py 白名单）+ huanbao_user/GRANT + registry.json 首条 →【契约 1 脚本首个触发点】
- S2 数据 pipeline：定 huanbao_weekly_* schema + 抽取脚本（huasheng-tick.sh 蓝本）+ 本地手跑验真数据 →【paas-db-schema skill 雏形】
- S3 薄后端：cg-proxy 蓝本轻量版，单一只读端点 →【paas-backend-scaffold skill 雏形】
- S4 前端壳：静态 HTML 删录音 + DOM 硬编码改 fetch + 双视图保留 →【paas-frontend-scaffold skill 雏形】
- S5 契约 2：cgplatform-net --internal + pmAppGuard + acl + slug↔IP 反向校验，接入 huanbao 容器 →【契约 2 全套首个约束对象】
- S6 契约 3 + 上线：pmapp@ 三机 + nginx 子目录 + deploy → huanbao.cgboiler.com →【契约 3 全套 + paas-nginx-conf/paas-deploy 雏形】
- S7 pipeline 挂 cc-gateway prod cron 周期跑通 + 契约 6 回收脚本骨架（消费 S1 registry.json）→【契约 6 骨架】

顺序与原 v0（1→3→2→6）差异：有 dogfood 驱动后，基建物由真实需求逐步拉出（契约 2 提前到容器跑起来时 S5，契约 3 后移到上线时 S6），符合 OCCAM，呼应 thread "脚本推迟到首个 PM 应用进来再写"同一判断。

**Inversion 四点（按概率）**：① 最可能——pipeline 被当应用一部分实施，B 裁定被悄悄架空（`bug-shape-survives-fix`），物理判据=应用后端零 LLM 调用、零 cg-notes/cgManager 直连；② 契约 1 脚本被 dogfood 压力赶工白名单没套到位，防御=S1 独立验收不绑上线时间压力；③ cg-notes @mention 归属幻觉复现（threads/cg-notes-weeknote-mention.md 已记录同 vector，这次喂决策场景代价更高），防御=抽取 prompt 硬约束 unknown 不脑补 + 首跑 Keith 人眼校；④ 双视图被拆成两个前端工程量翻倍，防御=一前端一 mode 参数。

**行动建议**：父会话带回 Keith 对齐 B 裁定（这是核心，A 与切分都是推论）；对齐后按 S1→S7 执行；S1 与 dogfood 上线解耦验收；S2 首跑 Keith 校抽取结果再上线；更新 threads/cgboiler-pm-sandbox.md 时间线 + 关联 threads/huasheng-battle-report.md（pipeline 同构蓝本）。

### 核心假设

- huasheng-battle-report 当前确在 cc-gateway prod cron（thread brief 明示），新 pipeline 可同宿主复用其调度/可用性域决策
- `huanbao_*` 表前缀 + 一 user GRANT（契约 1 v0 设计）能承载"pipeline 持写凭据 / app_user 仅 SELECT"的双凭据分离——pipeline 不走 app_user
- 那份已跑过一次的静态 HTML 数据结构能干净映射成 huanbao_weekly_* 表（未实际看 HTML，假设其 DOM 数据结构非病态）

### 可能出错的地方

最高风险即 inversion ①——执行者"一个应用一套代码"惯性把 pipeline 合回应用后端，概率偏高（图省事是默认引力），靠"两个零"物理判据 + S2/S3 独立产物兜底。次高=cg-notes 抽取幻觉随发布污染周会决策场景（inversion ③），概率中，代价高于普通内部周报。

### 本次哪里思考得不够

- 没实际 Read 那份静态 HTML（minio 上），数据结构到表 schema 的映射难度是假设的——S2 实施时可能发现 HTML 数据结构不规整，抽取脚本工作量被低估
- 没核 cg-proxy 是否已有可直接复用的环保板块经营数据 REST（cgdata 那条数据源我假设"复用 cg-proxy 已有经营数据 REST"，但没物理 grep 确认存在；若不存在，cgdata 聚合也要 pipeline 侧从 DB 直查，工作量比裁决里写的多）
- 双视图 report-mode 的"数据精简"具体差异没展开——若两视图数据维度差异大（不只是 CSS），mode 参数方案可能不够，但这属实现层，留给执行会话

### 如果 N 个月后证明决策错了，最可能的根因

B 裁定被执行层架空：pipeline 实际写进了应用后端，契约 2 被开口子，半年后第二个 dogfood 沿用此错误样板，huasheng 同构逻辑出现第三份。触发因=裁决说了"分开"但没有物理 review 闸门强制，靠执行者自觉——`bug-shape-survives-fix` 的典型路径（修者改了显式那处没改内化那份）。缓解已写进 inversion ① 的"两个零"判据，但判据要被真执行才有效。

### 北极星触达

#1 二阶效应——B 裁定不是"这个 dogfood 怎么搭"的一阶问题，是"首个 dogfood 的范式归属如何影响整个 cgplatform 后续所有应用的形态 + 契约 2 完整性 + huasheng pipeline 家族是否被复制"的二阶结构判断。看的是这一刀切下去后第二、三个 dogfood 会沿什么样板长。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `borrowed-method-as-mini-source` (2026-05-08) — 应用内自带抽取 = 在 cgplatform 容器造 huasheng pipeline 迷你同构版，反向继承被抽取对象元约束，事实抵消复用。B 裁定的核心论据
  - `m2m-vs-h2m-coupling-illusion` (2026-05-09) — "周期数据生产(M2M cron)"和"PM 应用展示(H2M 薄壳)"被一个容器伪装成同构，并发模型/session 寿命/失败可见性全不对齐，强行同构=单点过载
  - `bug-shape-survives-fix` (2026-04-27) — inversion ① 的本质：裁决说分开，执行者"一应用一套代码"内化惯性会合回去；防御靠物理判据不靠文字约束
  - `tool-elevation-as-occam` (2026-05-06) — S1 的 cgplatform_create_app_db.py 套 userid.py 白名单风格，是机制上提复用不是另造
- **本决策是否在某条 essence 上反着走**：潜在张力——`caged-freedom` (2026-04-26)：把 dogfood 切成"薄壳 + 外部 pipeline 喂数据"可能给 PM 应用形态建笼子（限制了"应用自带能力"的自由度）。但本场景张力不成立——这里的"分开"不是防御式约束，是诚实承认数据生产 vs 数据展示本就是两个异构关注点，合并才是伪同构。明示：表面张力，检验后不成立。
- **cross-check 用的关键词**（grep 物理证据）：`borrowed-method / m2m-vs-h2m / bug-shape-survives / tool-elevation / caged-freedom`（在 essence.md 全文确认命中）

### essence 候选（可选）

- slug: dogfood-pulls-infra-not-infra-precedes-dogfood
- 一句话: 平台基建的正确实施顺序由首个真实 dogfood 逐步拉出，不是先把脚手架建空——纯基建顺序是"无需求时的占位顺序"，有 dogfood 后正确顺序是让每个契约被它首个真实约束对象触发。
- 是否已 append 到 essence.md: N（本次不沉淀——这是 `premature-abstraction-tripwire` + thread 已有的"脚本推迟到首个 PM 应用再写"判断在实施顺序维度的应用，非新洞察，强行沉淀违反 essence-degg-test）

### 外部锚点

- `~/githubProject/cc-space/threads/cgboiler-pm-sandbox.md` ← 本主体协作叙事，待加 2026-05-18 dogfood 架构裁决时间线
- `~/githubProject/cc-space/threads/huasheng-battle-report.md` ← 数据生产 pipeline 同构蓝本（cc-gateway prod cron 范式来源）
- `~/githubProject/cc-space/threads/cg-notes-weeknote-mention.md` ← inversion ③ 的同 vector 历史证据（抽取幻觉）
- `~/githubProject/cc-space/inbox/briefs/pm-paas-platform.md` ← v0 决策快照
- `~/githubProject/gg/memory/reflections/2026-05-14_cgboiler-pm-sandbox-contract-v0.md` ← 6 条契约 v0 决策（本裁决的上游）

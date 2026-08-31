---
date: 2026-08-31
slug: cgboiler-checkpoint-semantics-split
summoner: monster（川锅可审计时态世界模型 checkpoint 语义裁决）
northstar_reach: "#1 二阶效应 / #3 决策超越直觉"
status: substantive-decision
---

# Reflection: checkpoint 只能证明一个单调命题

### 给父会话的最终输出（必填）

**裁决：立即把单体 checkpoint 拆成 source ingest checkpoint + interpretation batch receipt；query coverage 是两者交集的第三种派生证明，不允许任一 checkpoint 单独赋予 unknown。** 现闸把可机械全量的摄取绑到须逐条真读的 44020 条解释上，等于让快轨永久挤最稀缺判断闸；`sources.json` 已声明 ingest 语义，而 `checkpoint_gate.py` 实际声称「前九步业务处理完成」，两者不能同时为真。

**Ingest checkpoint** 只证明一个 source watermark 前的 raw capture、artifact/manifest hash、逐记录 accounting、locator resolve、watermark-aware production reconcile。它推进 source ingest cursor，不推进任何 assertion/query/migration 权威。28 条 unknown type 不设容忍阈值，改为集合不变量 `RawVersionSet = CanonicalSet ⊎ TypedGapSet`；每个 gap 必须带 native key、raw locator/hash、枚举 reason，且两集合不相交。当前 `_report.json` 只有 `Counter{unknown_note_type:28}`，没有逐记录 gap ledger，故原则可放行、当前尚不可放。reconcile 的 manifest loader 修复必要但不充分：现 `SELECT id FROM notes` 无 upper bound，8/21 后新增会被误报 unseen；必须按冻结 watermark 分类，`unseen_at_or_below_bound=0` 才能清关。

**Interpretation 不设时间游标。** 每个 receipt 钉死显式 evidence-set（列表或 selection manifest+sha），并证明该集合的 assertion / blocked / reviewed-no-fact 处置无静默遗漏、validate 报告新鲜、publish roundtrip/golden 方向合法、fresh review 分歧逐条处置。关闭 receipt 只把 evidence_id 加进 set-based interpretation index；重复解释不加覆盖量，改判走 supersede。当前 31/44020 只能登记为已解释 evidence 集，绝不形成全局前缀或完成宣称。

**Coverage 迁移：保留 `coverage.json` 作为唯一 runtime query-coverage SSOT，但升级为 v2 派生账，强制同时引用 ingest receipt 与 interpretation receipt；`complete` 仅在两轴均闭合时派生。** `coverage_notes_backfill.json` 只作为一次性迁移输入，迁入后退出 runtime；禁止 reader 运行时 union 两文件。现 3 条 legacy `coverage.json` 记录显式标 `legacy_partial`，缺 semantics 的记录 fail-closed。`checkpoint_gate`/`validate_ledger`/`query` 统一经一个 loader；现 Step6 只检查 legacy 文件“有 records”是假绿，必须改成核对本批 source/run/receipt/hash。

**状态迁移：新建 source-specific ingest state，旧 `world_model_cursor/world_model_runs` 只作一次性导入，不双写。** 有旧 cursor 但无 ingest receipt 的环境标 `legacy_semantics_unverified`、不得激活；当前物理状态 cursor 缺失、runs=0，可无损切换。`checkpoint_gate.py` 暂作兼容 CLI 外壳，输出 ingest 与 interpretation 两段，但只有 ingest gate 能写 source cursor；旧「patch Step1/7 让 gate 变绿」测试退役，改测两轨互不推进。

**production reconcile 未完成前继续不推进**：source ingest checkpoint/world_model_cursor、`history_complete`、query coverage complete/unknown、全域 interpretation、shadow/ledger authority、plist。capture progress 的 `completed=true` 保留为摄取进度事实；现有 10 批可补 interpretation receipts 并继续解释，不必等 reconcile，但它们永远不能反向抬高 source/query 全域状态。

**淘汰两路**：保留单闸并把“本批”改成任意解释子集，会让 source cursor 的未选证据被完成宣称吞掉；完全取消 cursor、只靠 manifest 去重，能服务一次性 backfill，服务不了 live 增量 watermark/编辑/硬删。拆轨是唯一不伪造任一语义的方向。

### 核心假设

raw artifact 永久可重放，且 interpretation 能用 evidence_id 集合独立于 source cursor 继续；若 evidence 保留契约失效，两轨同时失去地基。

### 可能出错的地方

实现者只改命名却继续共用 `coverage.complete`，或用 aggregate gap count 冒充逐记录集合等式；这两种会把旧错原样搬进新文件。

### 本次哪里思考得不够

未实跑生产 reconcile，hard_deleted 在冻结上界前后如何定时只能给结构判据，不能报告现实分布。

### 如果 2 个月后证明决策错了，最可能的根因

把 interpretation 的真实最小审计单元误定为 evidence；若一条 evidence 内多段同时有 assertion 与 blocked，receipt 必须以 worksheet segment/disposition 为核算单元，evidence_id 只作外层集合。

### 北极星触达

#1：拆出第三种 truth——query closure 不是 ingest 或 interpretation 任一方的属性，而是二者交集；#3：用零未记账集合等式取代容忍阈值。

### essence 对齐自检（必填）

- **对位**：`mixed-queue-funnels-all-to-scarcest-gate`、`runtime-state-vs-business-data-distinct-ssot-domains`、`invariance-allocation`、`granularity-mismatch-forces-fabrication`、`replay-gate-collapses-to-attestation-when-inputs-expire`。
- **反着走**：与 `separation-need-is-not-topology-verdict` 有表面张力；本案不是凭嗅觉造墙，`sources.json` 与 `checkpoint_gate.py` 已出现不可同时成立的语义、且人工全读让单闸物理不可终止，分离需求已被实证。
- **cross-check 关键词**：checkpoint / ingest / runtime state / mixed queue / granularity / replay / invariance。

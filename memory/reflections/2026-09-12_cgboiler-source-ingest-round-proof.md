---
date: 2026-09-12
slug: cgboiler-source-ingest-round-proof
summoner: monster / cgboiler world model
northstar_reach: "#1 二阶效应 / #3 决策超越直觉"
status: substantive-decision
---

# Reflection: Notes 多轮 source-ingest 的冻结证明

### 给父会话的最终输出（必填）

**裁决 A：候选可作为冻结变更闸输入，不需要换方案。** 关键限定是：`upper_bound` 只承担「把 append-only manifest 唯一切成轮」的职责，不承担轮完成或历史完整证明；完整性继续由 progress 终态、全 manifest artifact 重放、accounting/resolve、独立 watermark reconcile 的合取结算。

**必要不变量**：manifest 非空且每行继续经过 source/path/hash/row_count/id 重放；轮定义为 append 顺序中 upper_bound 相同的最大连续块，bound 先按固定格式解析、不同块严格递增；全局 cursor 链连续，且每个非空 artifact 内 `(COALESCE(updatedAt,createdAt),id)` 严格递增、首 key 大于 cursor_in、末 key 等于 cursor_out、时间不越本轮 bound；所有 drifted/vanished 为空。当前 progress 必须 `completed=true`、bound/cursor 对最新轮末端，并将 batches 按固定字段投影后与 manifest 尾部有序匹配。为保留 adapter 已写明的 progress 丢失续跑，匹配应允许「最新轮的非空有序 suffix」；强制等于整轮会误拒合法恢复。若不接受 suffix，就必须先改 adapter/runbook，不能在本次窄改里静默废约。

**严格递增正确**：只约束不同连续块；同 bound 的中断续跑仍是同一逻辑轮。`B1,B2,B1` 或 `B2,B1` 必须失败。轮界按 bound 对当前 Notes 契约足够，但不是跨 adapter 的通用 round id。

**零行**：默认 fail closed。现 adapter 在 discover 返回 0 行时只把 mutable progress 写成 completed，不调用 capture，因而没有 immutable manifest artifact；裸 `completed=true` 不构成可重放证明。未来只有新增 content-addressed、绑定 source/bound/cursor/query-or-adapter 指纹的空轮 receipt（或把 reconcile receipt 明确定义为该 no-op 证明）后才可放行；裸空 JSONL/空 manifest 行不够。

**未来替换范围**：只替换 `check_capture_manifest()` 可以成立；`ingest_gate()` 仍须四闸合取，`check_reconcile()` 仍绑定最新 progress upper_bound、全 manifest hash、known-id hash、adapter/query/connection 与 immutable observation 重放。append 新轮后旧 reconcile 必须因 bound/hash stale 转红，故 Capture 变绿不能单独抬 `history_complete`；coverage 的 `query_closed = ingest_closed ∧ interpretation_closed` 与 history_complete 派生规则不动。

**反例测试**至少锁：真实 37 行三轮通过；单轮旧格式通过；bound 回退/非连续复现失败；轮内及跨轮 cursor 断链失败；artifact key 乱序、末 key≠cursor_out、时间越 bound 失败；任一 drift/vanished 失败；progress 未完成、旧 bound、错 cursor、batch 缺失/多出/重排/字段漂移失败；progress 丢失后同 bound 合法续跑的非空 suffix 通过；新 bound 零行且 batches=[] 失败；artifact path/hash/row_count/id 漂移仍失败；多轮 Capture 通过但 reconcile 仍钉旧 manifest/bound 时总 ingest 与 history_complete 继续失败。

**物理出处**：`/Users/xuke/githubProject/monster/cgboiler/_pipeline/world_model/checkpoint_gate.py:68-90,173-260,385-425`；`/Users/xuke/githubProject/monster/cgboiler/_pipeline/world_model/adapters/notes.py:156-172,227-250,254-346,512-563,598-700`；`/Users/xuke/githubProject/monster/cgboiler/_pipeline/world_model/DATA_RUNBOOK.md:122-133,199-203,1067-1111,1167-1177`；`/Users/xuke/githubProject/monster/cgboiler/_pipeline/world_model/WORLD_MODEL_SCHEMA.md:458-527,611-628`；`/Users/xuke/githubProject/monster/cgboiler/_pipeline/world_model/test_checkpoint_gate.py:83-147`；`/Users/xuke/githubProject/monster/inbox/briefs/cgboiler-checkpoint-separation-2026-08-31.md:22-43`；真实三轮：`/Users/xuke/githubProject/monster/cgboiler/_pipeline/world_model/manifests/notes.jsonl:0-36` 与 `/Users/xuke/githubProject/monster/cgboiler/_pipeline/world_model/pending/notes-backfill-progress.json:0-16`。

### 核心假设

`check_reconcile()` 与 coverage 派生规则保持独立且不随本次 Capture/Manifest 解释器一起修改；manifest 仍是 append-only 顺序账。

### 可能出错的地方

把 progress.batches 的「逐项吻合」实现成整轮全等，会与 `load_progress()` 明示的丢失恢复路径冲突；反向若只做任意子序列匹配，则会放过删批/重排，必须是结束于 manifest 尾部的有序非空 suffix。

### 本次哪里思考得不够

未写 scratch helper、未跑 synthetic fixtures（Keith 明示本轮不改文件）；只对真实 37 行 manifest 做了只读投影，并额外核了 67324 行 artifact 的 key 顺序与 cursor 内容一致性。

### 如果 3 个月后证明决策错了，最可能的根因

正式实现把 `upper_bound` 从分组键悄悄升级成完成证书，或为放行零行轮开始信 mutable progress/裸空 artifact，令 Capture 自签替代独立 reconcile。

### 北极星触达

#1：识别「轮界足够」与「完成证明足够」不是同一命题；#3：在 A/B 二选中保留 A，同时用 recovery 与 cursor-content 两个反例修正候选边界。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`invariance-allocation`、`anchor-protects-retrieval-not-integration`、`attestation-has-no-fixed-point-under-self-audit`、`replay-jurisdiction-begins-at-the-declared-input`、`mechanical-gate-needs-machine-detectable-target`。
- **本决策是否在某条 essence 上反着走**：与 `hardening-exemption-covers-thickness-not-existence` 有潜在张力；这里加 cursor-content 核不是泛化加墙，而是候选已把 cursor 连续性列为证明命题后补足其可重算对象。
- **cross-check 用的关键词**：invariance / anchor / attestation / replay / mechanical gate / upper_bound / cursor / manifest。

### 外部锚点（可选）

- `/Users/xuke/githubProject/monster/inbox/briefs/cgboiler-checkpoint-separation-2026-08-31.md`
- `/Users/xuke/githubProject/monster/threads/cgboiler-world-model.md`

---
date: 2026-09-01
slug: cgboiler-interpretation-receipt-revision-chain
summoner: monster（sealed interpretation receipt 遇后续正确 amendment 的演化模型裁决）
northstar_reach: "#1 二阶效应 / #3 决策超越直觉"
status: substantive-decision
---

# Reflection: immutable receipt 需要版本链，不需要豁免当前重放

### 给父会话的最终输出（必填）

**裁决：采用 `<batch>/revisions/rNNNN/receipt.json` 的单链、全状态快照 revision；拒绝独立 receipt-amendment overlay。** revision 不是对旧 receipt 打补丁，而是对同一 evidence set 在新 ledger state 上重新给出完整 closure 证明。root receipt 字节/hash 永不改；index 从图推导唯一 leaf，不写 `terminal=true`，只消费 leaf。

每个 revision 必须包含 parent receipt path+sha、严格递增 revision、恒定 evidence-set ids+hash、parent/child state manifest refs、batch-scoped amendment slice ref、完整当前 segment dispositions、outcome migrations、bounded validate/publish、fresh review。state manifest 覆盖 worksheet/candidates/evidence/assertion/entity/blocked/dependencies；文件是 revision 内 immutable snapshot，未变角色可复用 parent snapshot ref。leaf 另须逐字节等于当前 live 同批文件；ancestor 只按自身 snapshot 历史重放，不参与当前 closure。

首个 revision 允许一次 bootstrap：从 commit `6dc83b31` 取旧 batch ledger，逐字 hash 对 parent validate inputs。物理已核：旧 assertion ledger SHA256=`158668…` 与 parent report 相等，当前 live=`636a…`。把 g8 plan 的 5 个 recast 在临时 parent snapshot 上重放，输出必须 byte-equal current child；以后 parent 自带 snapshot，不再依赖 git 考古。

链不变量：同 batch、单 parent、每 parent 最多一 child、revision+1、无环/无缺口、唯一 leaf；fork/多 leaf/错 parent hash/跨批 parent 整批 fail closed。amendment slice 必须精确列出同 batch item hashes，transition runner 用 parent snapshot 重放后与 child state 全字节相等；少一项、多一项、借别批均失败。删除 leaf 时 live ledger 与 ancestor state 不符，index 不得回落祖先。

Disposition 采用完整 child 集，不叠 overlay；除 `outcome_migrations` 列出的 occurrence 外，其余逐字一致。`recast`：old assertion outcome 迁到唯一 active superseding successor，且 evidence/quote 仍命中同 occurrence；`rejudge`：只认 expected_assertion 全字段重放，new evidence/quote 命中同 occurrence，否则 fresh review 重判；`retract`：不能把“已撤回”当终态，旧 outcome 删除后若无其他 outcome，必须落当前 blocked / reviewed_no_fact / 新 assertion。blocked 从易漂的 `item_index` 升为 normalized blocked-item SHA256，parent index 先对 parent snapshot 解引用再迁移。

`receipt_index` 先验整条拓扑，再只对唯一 leaf 做 current replay；closed evidence 恒等 root evidence set，revision 不增加也不减少。为防再次 32→28，sealed batch 禁止 `amend.py` 直改：只能走 staged revision transaction；同 batch lock 下验证 live=parent、生成/审查 child、写 receipt last。未完成或崩溃态 fail closed，不以历史 receipt 兜底。

### 核心假设

同批 amendment 能在隔离 state snapshot 上确定性重放；当前 `amend.py` 七类 op 若有读全局隐式状态，revision runner 必须把该依赖加入 state manifest，不能靠环境偷渡。

### 可能出错的地方

最危险的是名叫 snapshot、实际仍只存 live path+hash；下一修订后历史节点再次失去物理输入，链退化成一排不可重放声明。

### 本次哪里思考得不够

未逐 op 实跑 parent→child transition；尤其 recovery 与跨批 entity merge 是否读了未显式注入的全局文件，须实现期用变异测试暴露。

### 如果 2 个月后证明决策错了，最可能的根因

全状态 revision 成本逼人绕回直接改 live ledger，说明 state manifest 边界选得过宽或 revision 生成没有被工具化，而不是 overlay 在语义上更正确。

### 北极星触达

#1：append-only 的二阶代价是“不可改”会变成“自失效”；解不是削弱 replay，而是让证明本身版本化。#3：把 receipt 修订从文件覆盖题重写成状态转换证明。

### essence 对齐自检（必填）

- **对位**：`freeze-the-sample-not-the-sampler`、`one-shot-invariant-decays-under-live-append`、`replay-gate-collapses-to-attestation-when-inputs-expire`、`invariance-allocation`、`granularity-mismatch-forces-fabrication`。
- **反着走**：与 `abstraction-tax` 有张力——revision chain 新增状态机；例外合理，因为旧 receipt 已真实自失效、status 32→28，且 commit hash-matched parent snapshot 证明可重放路径在场，不是预想未来。
- **cross-check 关键词**：immutable / receipt / replay / snapshot / append / invariant / granularity。

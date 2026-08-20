---
date: 2026-08-20
slug: cgboiler-world-model-v01-freeze-gate
summoner: monster
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: 川锅世界模型 v0.1 冻结闸

### 给父会话的最终输出（必填）

**MODIFY。** 六层方向与 assertion-first 已可保留，但 v0.1 还不能冻结；只需收掉四个机制契约歧义，不必本轮跑 Notes/inquiry/DB 数据。

阻塞项：

1. `migration.json` 只有 `all_existing_cards=true` 的全局 legacy scope，契约未定义窄 scope 与全局 scope 重叠时的优先级/拆分规则，也未写 `legacy_authoritative -> shadow_parity` 入闸条件；因此无法无歧义地只迁王亮切片。
2. `coverage.json` 的 `note-comments-not-ingested` 没有 `scope.entity_ids`，直接违反 schema 对每个 coverage segment 显式、非空 entity scope 的要求。应把 source-level 未接入状态留在 source registry，或写明只作 gap sentinel 且绝不参与 closure 的例外。
3. predicate 契约自相矛盾：schema 要求每条 assertion 至少两个 participants，但 `expressed_view`、`reported_violation` 的 catalog 合法最小形态可只有一个；同时 schema 称“首批已验证”，catalog 全部仍是 `provisional`。需统一 unary/binary 语义和状态文案。
4. assistant-chat locator 契约未对齐：runbook 要求 `chat.updateTime`，`sources.json` 的 required locator fields 没有对应 canonical 字段。需统一为一个正式字段名并纳入 schema/registry/validator。

下一迁移闸：修完以上四项即冻结 v0.1；随后只让“王亮 Q2 + 明确 source/window/entity scope”进入正式 `shadow_parity` Gate 1。先完成 immutable raw capture、canonical locator/hash 回放、coverage closure 输入与 eid/quote/locator/golden-query parity；L1 继续权威。publisher roundtrip 与 legacy write guard 通过前，禁止进入 `ledger_authoritative`，也不要把贫样本第二切片当成 Gate 1 替代品。

trade-off：本审按要求只读契约与账本，没有读 validator/实现源码，所以结论限定为机制契约放行，不宣称实现存在或不存在额外 bug。

### 核心假设

分批迁移必须允许一个窄 scope 先影子运行，其余存量继续 legacy；若真实意图是全库存量一次切换，阻塞项 1 的权重会下降，但那与当前切片式迁移叙述冲突。

### 可能出错的地方

最可能漏判的是 validator 已在代码里定义了上述例外/优先级；但契约 SSOT 未承载它，fresh adapter 仍会得到两种合法读法，因此不改变 MODIFY。

### 本次哪里思考得不够

按召唤边界没有运行 validator，也没有读取 query/migration 实现，无法判断四项中哪些已被实现层临时兜底。

### 如果 2 个月后证明决策错了，最可能的根因

把“可表达一个样本”误当成“可分批迁移权威”，低估了 scope algebra 对三态迁移可执行性的承重度。

### 北极星触达

触达 #3：没有被五题绿灯和三轮修复带到 PASS，而是检查下一次真实迁移能否在契约内唯一落位。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`paradigm-not-feature-completeness`、`separation-need-is-not-topology-verdict`、`one-shot-invariant-decays-under-live-append`、`mechanical-gate-needs-machine-detectable-target`。
- **本决策是否在某条 essence 上反着走**：无；议题本身要求先修承重歧义、同时拒绝继续扩层，正好受前两滴双向夹持。
- **cross-check 用的关键词**：`shadow_parity`、`all_existing_cards`、`entity_ids`、`participants 至少两个`、`provisional`、`chat.updateTime`、`source_updated_at`。


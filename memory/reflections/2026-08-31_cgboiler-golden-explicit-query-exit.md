---
date: 2026-08-31
slug: cgboiler-golden-explicit-query-exit
summoner: monster（golden drift 对合法 rejudge 查询退出的审计语义裁决）
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: 事实存续与查询成员资格退出必须分型

### 给父会话的最终输出（必填）

**裁决：在同一 `rejudge` amendment 内新增逐字段 `golden_dispositions[]`，把合法退出单列为第五类 `explicit_query_exit`；不改 g6、不保留旧谓词、不普遍放宽 rejudge。** 本轮 7 条事实仍在账本，只是从 `proposed_strategy/expressed_view` 纠正为 `planned_action/requested_support` 后，正确退出题意为「表达哪些判断」的 g6。把它继续算真丢是类型混同；直接 freeze 则拆闸。

每条 disposition 只准 `kind=query_membership_exit`、`reason_code=predicate_scope_exit`、精确 `question_id`、固定 `field=matched_assertion_ids`、冻结 query 的 canonical hash、非空 reason。old/new id 可为可读性重复，但必须分别等于 enclosing `item.id` 与 `expected_assertion.assertion_id`；更小实现可直接从外层派生。

Direction tool 只有在现有 `approved_rejudge` 已通过（旧条撤下、expected 新条当前唯一、全字段类型敏感相等）后才消费 disposition，并重算五件：① old id 真在 before 的该 field；② question id 唯一且 query hash 与 snapshot/current 均一致；③旧 predicate 在冻结 `query.predicates`；④新 predicate 不在；⑤new id 当前真未命中该 field。一个旧成员退出多个 field 必须逐 field 明列；重复、多余、未消费 disposition 同样判红。

故 plan 删除、expected 篡改、错 question/field/hash、old/new id 不符、普通事实消失继续落 `lost`。输出分类改为 growth / recast / rejudged-in-field / explicit-query-exit / true-loss，只有前四类允许 freeze。

**拒绝改 g6**：它的问题文本与 predicate 范围一致指向「判断」，把 `planned_action/requested_support` 加进去是改考题消漂移，且混淆判断、计划、请求。若产品确需看后两类，新增新的 question_id，不能借本轮回归改写既有基线。**拒绝保留旧谓词**：那会为了测试稳定性保留已知假解释。**拒绝任意 rejudge 可退出**：expected 全字段吻合只证明新事实存在，不能证明它从哪个问题退出是合法的。

落点只在 rejudge 清单，不另造 golden amendment 账本：语义改判是原因，query exit 是该事件的审计后果；拆成两账会产生可被单删的配对关系。`validate_ledger` 管结构与 expected 链，direction tool 管 before/current query membership。

### 核心假设

g6 的稳定语义确为「判断」，且其 predicate 列表是成员资格的承重条件；现物理题面支持该假设。

### 可能出错的地方

最大风险是把 `golden_dispositions` 做成自由文本豁免，或只检查指定 qid 存在、不检查 old membership 与 query hash，届时错题号仍可清关。

### 本次哪里思考得不够

只裁当前 `matched_assertion_ids + predicate_scope_exit`；未来 uncertain→matched、时间窗退出或 participant 改判应重新立 reason_code，不预先泛化。

### 如果 2 个月后证明决策错了，最可能的根因

golden question 本身被允许原地改写而 snapshot 未钉 query hash，使 disposition 对着另一张考卷仍能通过。

### 北极星触达

#3：没有在「冻结 / 留假事实」二选一里妥协，而是把事实存续与查询成员资格拆成两个独立可审计命题。

### essence 对齐自检（必填）

- **对位**：`evaluator-input-ownership`、`approval-gate-gates-status-not-consumption`、`authoring-rules-do-not-govern-record-layers`、`invariance-allocation`、`hard-rule-welds-intent-to-form-breaks-at-first-legal-deviant`。
- **反着走**：与 `ontology-expansion-velocity-needs-cap` 有轻微张力（新增第五分类）；合理例外是四分类已物理把合法退出误记真丢，现有本体装不下，且新类被单一 reason_code 封顶。
- **cross-check 关键词**：golden / baseline / evaluator input / status / record / invariant / legal deviant。

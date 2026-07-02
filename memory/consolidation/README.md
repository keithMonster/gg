# memory/consolidation/ — 记忆巩固产物（essence 的"当前有效视图"）

> 建立：2026-07-02 设计会话（五机制之一）。协议 SSOT 在 `auto_gg.md §2 月度巩固相位`。
> essence.md 是 append-only 的 event log；本目录是它的 projection——**永不反向修改 essence 原件**。

- 产出节奏：每月**第一个** auto_gg 夜巩固（`YYYY-MM.md`）；每月**第二个** auto_gg 夜差值审计（`YYYY-MM_gap.md`）。两相位协议 SSOT 都在 `auto_gg.md §2`
- 巩固五节契约：修正链 / 活跃簇 / 冲突重复候选 / 过期候选（后两节只标记不裁决）/ divergence 台账（本月 gg 独立判断 ≠ Keith 判断的实例 + 后验——`progress-evidence-is-divergence`：分歧实例是进步的唯一合法证据）
- 差值审计三节契约：候选池（已论证未兑现）/ 不建清单（tripwire 类显式留空）/ 裁决去向（agenda 交 Keith，auto_gg 不自建机制）
- 消费方：Keith review、设计会话的 essence 对齐自检、未来可能进启动链（连续两期质量被认可后再议——tripwire）
- 理论依据：`reconsolidation-safe-iff-original-immutable`（essence 06-10）+ `theory-outruns-structure-in-self-evolving-systems`（07-02）；外部坐标：Anthropic Dreaming、arXiv:2601.04170

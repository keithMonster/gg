# memory/consolidation/ — 记忆巩固产物（essence 的"当前有效视图"）

> 建立：2026-07-02 设计会话（五机制之一）。协议 SSOT 在 `auto_gg.md §2 月度巩固相位`。
> essence.md 是 append-only 的 event log；本目录是它的 projection——**永不反向修改 essence 原件**。

- 产出节奏：每月第一个 auto_gg 夜，文件名 `YYYY-MM.md`
- 四节契约：修正链 / 活跃簇 / 冲突重复候选 / 过期候选（后两节只标记不裁决）
- 消费方：Keith review、设计会话的 essence 对齐自检、未来可能进启动链（连续两期质量被认可后再议——tripwire）
- 理论依据：`reconsolidation-safe-iff-original-immutable`（essence 06-10）；外部坐标：Anthropic Dreaming、arXiv:2601.04170

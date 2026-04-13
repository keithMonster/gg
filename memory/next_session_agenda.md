---
type: next-session-agenda
last_updated: 2026-04-13
---

# Next Session Agenda — 给下次设计会话 / 下次 Keith 的议题清单

> 这是 gg（尤其是夜间维护模式）给"下次跟 Keith 对话的 gg"留的议题队列。
> 每条议题处理完就从本文件**删掉**（或挪到文件末尾的"已处理"节做历史）。
> 本文件是**软外围**——内容可以自由增删，但它本身必须存在。

---

## 标签约定

- `[HARD_CORE]` — 建议改硬核心文件（CORE / constitution / CLAUDE / cc_agent / reasoning_modules / personas / README）
- `[P0]` — gg-audit 或夜间维护发现的高危问题，明日第一时间处理
- `[STRATEGIC]` — 战略性判断，需要 Keith 的 sense
- `[RECURRING]` — 连续 2 次或以上出现的同类问题（可能有根因需要挖）
- `[TIER2]` — gg-audit Tier 2 建议
- `[Q]` — gg 想向 Keith 追问的问题

---

## 待议（open）

### 2026-04-13

- `[HARD_CORE]` **CORE.md / CLAUDE.md / cc_agent.md 的 night_watch 辐射引用待补**
  - **背景**：今天新增了 `night_watch.md` 作为第三种运行模式入口，但按设计模式 D4 纪律（硬核心改动需 Keith 明示批准），gg 没有擅自修改 CORE / CLAUDE / cc_agent 去引用它
  - **提议**：在 CORE.md §7 "存在位置与双入口" 里新增第三个入口引用；在 CLAUDE.md 和 cc_agent.md 的 "边界 / 与其他模式" 节里各加一行指向 night_watch.md
  - **不做的话**会怎样：night_watch.md 成为"孤儿文档"，下次 gg-audit 跑"辐射一致性"维度会报错
  - **等 Keith**：明示批准这三处辐射更新，或给出更合适的辐射位置
  - **提出者**：gg 设计模式 2026-04-13 首秀写 night_watch.md 时

- `[STRATEGIC]` **夜间维护模式是否应该有"元审视"配额**
  - **背景**：夜间维护只被允许改软外围 + 写 agenda。但如果某夜连续多条 agenda 指向同一个硬核心问题，gg 可能永远无法推进
  - **思考方向**：要不要给夜间维护一个"当同一议题连续 3 夜出现时，允许打包成一份正式提议（但仍不执行，交给 Keith）"的子流程？
  - **暂不紧急**：等真正出现这种情况再讨论

---

## 已处理（archived）

*（处理完的议题挪到这里留痕，文件太长时可以把这节整节移到 `memory/archival/next_session_agenda_YYYY-MM-DD.md`）*

---

## 变更日志

- 2026-04-13: v0.1.0 首次创建。由 gg 在设计模式下写 night_watch.md 时产生的辐射缺口触发。

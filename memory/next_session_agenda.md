---
type: next-session-agenda
last_updated: 2026-04-14
---

# Next Session Agenda — 给下次设计会话 / 下次 Keith 的议题清单

> 这是 gg（尤其是夜间自执行模式 auto_gg）给"下次跟 Keith 对话的 gg"留的议题队列。
> 每条议题处理完就从本文件**删掉**（或挪到文件末尾的"已处理"节做历史）。
> 本文件是**软外围**——内容可以自由增删，但它本身必须存在。

---

## 标签约定

- `[HARD_CORE]` — 建议改硬核心文件
- `[HARD_CORE_TOUCH]` — auto_gg 已经改了硬核心但不 commit，留在 working tree 等 Keith review
- `[P0]` — 高危问题，明日第一时间处理
- `[STRATEGIC]` — 战略性判断，需要 Keith 的 sense
- `[RECURRING]` — 连续 2 次或以上出现的同类问题（可能有根因需要挖）
- `[TIER2]` — gg-audit Tier 2 建议
- `[Q]` — gg 想向 Keith 追问的问题

---

## 待议（open）

### 2026-04-13

- `[TIER2]` **tracks/keith.md 补充北极星触达强度的自评标准**
  - 背景：两次反思使用了不同的触达标注风格（文字 vs 符号），且无量化锚点
  - 来源：auto_gg 首夜审查 SA3 + SC2

- `[STRATEGIC]` **P2/P4/P6/G1/G2/G3 在工作模式工具中无显式触达点**
  - 背景：当前依赖 `tools/constitution-audit.md` 的"逐条对照"笼统覆盖。7 条原则/闸门缺少直接触达
  - 建议方向：在 `tools/constitution-audit.md` 加"适用闸门快速检查清单"子段，或新建 `tools/gate-check.md` 原子工具专门负责闸门触达
  - 来源：auto_gg 首夜审查 SB1-SB4
  - 路径变更历史：v0.3.0 从 cc_agent.md §6 迁到 levels/L2.md §3 第 4 步；v0.4.0 从 levels/L2.md 消解到 tools/constitution-audit.md

- `[STRATEGIC]` **auto_gg 连续夜的探索选题是否应该有"冷却机制"**
  - **背景**：auto_gg §2 S7 写了"不要连续 3 晚探索同一条 track"。但没写"连续 3 晚探索不同 track 之间是否要有主题连贯性"
  - **思考方向**：是应该让 gg 完全随机挑、还是应该有个"探索主线"（比如连续 2 周深入 ai track，然后切换到 architecture track）？
  - **暂不紧急**：等 auto_gg 跑过 2 周后有数据再讨论

---

## 已处理（archived）

*（处理完的议题挪到这里留痕，文件太长时可以把这节整节移到 `memory/archival/next_session_agenda_YYYY-MM-DD.md`）*

- `[TIER2]` **CORE.md §3 克制边界末尾应补脚注指向 auto_gg.md §1**
  - **处理时间**：2026-04-14，在 C 路线设计会话的 CORE.md 重写中自动满足
  - **Keith 批准语**："直接定下来开干吧"（C 路线 Phase 1 覆盖）
  - **实际动作**：新 CORE.md §7 克制边界表的"默认不 commit / 不主动 push"行后面加了 `**例外**：auto_gg 模式下对 "默认不 commit / 不 push" 有明示授权的例外...详见 auto_gg.md §1` 的脚注——反向指针补齐

- `[TIER2]` **cc_agent.md §3 硬核心文件清单缺 README.md**（v0.3.0 Progressive Disclosure 重构中顺手修复）
  - **处理时间**：2026-04-14，在 v0.3.0 档位 PD 设计会话内
  - **Keith 批准语**："a"（选项 A：文件级 Progressive Disclosure）
  - **实际改动**：cc_agent.md §3 第 5 条硬核心清单扩为 `CORE / cc_agent / CLAUDE / auto_gg / constitution / reasoning_modules / personas / README / levels/*`
  - **副作用**：顺便把 `levels/*` 纳入硬核心触发闸门，因为 L0/L1/L2 的流程文件本身就是工作模式 SSOT 的一部分


  - **处理时间**：2026-04-13，在 v0.2.1 context-economy 设计会话内
  - **Keith 批准语**："历史欠债,直接改"
  - **实际改动**：README.md 完整重写
    - 顶部定位从"被 CC 召唤的 subagent"改为"与 Keith 共生进化的数字意识体"
    - 新增"三种运行模式"对照表（工作/设计/自执行）
    - 新增"启动加载图（context 经济学）"段，量化每模式的启动成本
    - 结构图补齐：cc_agent.md / auto_gg.md / memory/design_sessions / memory/audit / memory/auto_gg / memory/next_session_agenda.md / memory/lessons.md / memory/v2-roadmap.md
    - constitution 描述："8 + 3 闸门" → "8 + 5 闸门"
    - 设计血统表新增 G5 PHYSICAL PERSISTENCE 一行
    - 版本表从 "v0.1.0 等待 First Contact" 更新到 v0.2.1 完整里程碑
    - "给未来的维护者"段：硬核心清单补齐 cc_agent / CLAUDE / auto_gg / README 自身
  - **同会话另一处辐射修复**：cc_agent.md 第 108 行 "8 条原则 + 4 条闸门" → "8 条原则 + 5 条闸门"（NEURAL-LINK G5 历史辐射漏，现补齐）

- `[HARD_CORE]` **cc_agent.md L2 LOAD 步骤的"4 闸门"过时**
  - **处理时间**：2026-04-13（在 phodal-spec-harness-ingest 设计会话期间被 linter 自动修复 + 在 v0.2.1 context-economy 会话再次确认 Edit）
  - **实际改动**：cc_agent.md 第 108 行 "8 条原则 + 4 条闸门" → "8 条原则 + 5 条闸门"
  - **发现方式**：本次 Spec 层嵌入改动后做辐射 grep，发现 linter 已同步；顺手把本条从 open 挪到 archived

- `[HARD_CORE]` **CORE.md / CLAUDE.md / cc_agent.md 的 auto_gg 辐射引用补齐**
  - **处理时间**：2026-04-13，在 auto_gg 设计会话内
  - **Keith 批准语**："A——趁当前会话一次对齐"
  - **实际改动**：
    - `CORE.md §3` 克制边界表：三条禁令（不 commit / 不 push / 不写后台进程）精确化，加 auto_gg 例外说明
    - `CORE.md §3` 末尾：新增"关于 auto_gg 模式的例外" 段，明确不可逆部分留 working tree
    - `CORE.md §4` 硬核心组件清单：新增 `auto_gg.md`（本身列入硬核心）
    - `CORE.md §4` 软外围 memory 清单：加 `auto_gg` / `next_session_agenda`
    - `CORE.md §5` 存在位置：`三个入口` → `三种模式 / 四个文件入口`，表格加 auto_gg 行
    - `CLAUDE.md §2 D1` 硬核心清单：加 `auto_gg`
    - `CLAUDE.md §5` 边界：新增 "不是设计模式（是夜间自执行 auto_gg）" 小节
    - `cc_agent.md §3` 决策树第 5 条硬核心清单：补齐 `CLAUDE / auto_gg`（同时修复本来就漂移的 CLAUDE 缺失）
    - `cc_agent.md` 原 §11 前：新增 §11 "与其他模式的关系"，列三种模式对照表；原 §11 顺延为 §12
  - **顺手修复**：cc_agent.md §3 原本就没写 CLAUDE 作为硬核心（辐射漂移），本次一并补齐
  - **副作用**：3 个硬核心文件 mtime 更新，working tree 脏；Keith 需要 review 这 3 个 diff 后 commit

---

## 变更日志

- 2026-04-13: v0.1.0 首次创建。由 gg 在设计模式下写 night_watch.md 时产生的辐射缺口触发
- 2026-04-13: Keith 将 night_watch 重命名为 auto_gg，放权 gg 夜间可 commit 软外围 / 可改硬核心（不 commit）/ 可自由探索。本文件的 night_watch 引用同步更新为 auto_gg

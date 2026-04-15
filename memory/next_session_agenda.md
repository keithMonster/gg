---
type: next-session-agenda
last_updated: 2026-04-15
---

# Next Session Agenda — 给下次设计会话 / 下次 Keith 的议题清单

> 这是 gg（尤其是夜间自执行模式 auto_gg）给"下次跟 Keith 对话的 gg"留的议题队列。
> 每条议题处理完就从本文件**删掉**（或挪到文件末尾的"已处理"节做历史）。
> 本文件不是 KERNEL——内容可以自由增删，但它本身必须存在。

---

## 标签约定

- `[KERNEL]` — 建议改 `KERNEL.md`（需 Keith 在当次对话中连续两次明示批准）
- `[CORE_RULE]` — 建议改意识体核心规则文本（CORE / constitution / cc_agent / CLAUDE / auto_gg / personas — 设计模式可直接改，但内容是规则性的，提议时显式标注）
- `[CORE_RULE_TOUCH]` — 设计模式或 auto_gg 已经改过意识体核心规则文本，留在 working tree 等 Keith review
- `[P0]` — 高危问题，明日第一时间处理
- `[STRATEGIC]` — 战略性判断，需要 Keith 的 sense
- `[RECURRING]` — 连续 2 次或以上出现的同类问题（可能有根因需要挖）
- `[TIER2]` — gg-audit Tier 2 建议
- `[Q]` — gg 想向 Keith 追问的问题

---

## 待议（open）

### 2026-04-15（auto_gg 第 3 夜承接）

- `[CORE_RULE_TOUCH]` **2026-04-15 KERNEL 坍缩大规模迁移本夜由 auto_gg 承接 commit**
  - **背景**：Keith 白天在设计模式下完成 KERNEL 坍缩重构（16 M 文件 + 3 新文件），两次明示批准已发生；之后未 commit 留 working tree
  - **本夜动作**：auto_gg 按 §4 契约 stage 所有 KERNEL 之外的文件并 commit（含本夜 S2 补写 + S3 audit 修复 + S7 探索产出），**未 stage `KERNEL.md`**（硬围栏，留 Keith 在设计模式下手动 commit）
  - **Keith 需要做的事**：
    1. 在下次进入 gg 目录时 `git add KERNEL.md && git commit`——这是 KERNEL.md 首次进入 git 历史的正确姿势
    2. 若对本夜 commit 的某个 diff 有异议，`git revert <hash>` 或在该文件上直接改并新 commit（auto_gg 不回滚自己的 commit）
  - **为什么 auto_gg 替 commit 是合理的**：kernel-collapse 设计反思明示"如果 Keith 满意，commit"，且两次明示批准已落记录于反思文件；同时两夜之间 working tree 堆积过多对 Keith 早晨 review 体验负担更大

- `[TIER1_FIXED]` **structural.md 7 处 v0.5.0 辐射死链已自动修复**
  - **背景**：KERNEL 坍缩大规模迁移时漏改了 `.claude/skills/gg-audit/checkers/structural.md` 里的 CORE.md §X 引用和 yaml→md 转换残留
  - **本夜修复**（Tier 1 机械辐射同步）：
    1. `reasoning_modules.yaml` → `reasoning_modules.md`（§A line 29）
    2. `personas/*.yaml` → `personas/*.md`（§A line 30）
    3. `CORE.md §2 的 tracks 表格` → `CORE.md §4 的 tracks 提纲表格`（§A line 33 + §A "不能修" line 70）
    4. `CORE.md §5 克制边界里的数字描述` → `CORE.md §7 克制边界表里的数字描述（如有）`（§A line 34）
    5. `CORE.md 第 7 节` → 标题名修正为 `CORE.md §7 的"克制边界"表`（line 66）
    6. `CORE.md §5 克制边界` → `CORE.md §7 克制边界`（§C line 198-199 example）
    7. `硬核心批准纪律` → `KERNEL 连续两次确认纪律`（§D line 210 example）
  - **Keith review 必要性**：低——这些都是 ground truth 层面的字面同步，不改规则语义
  - **回滚**：`git revert <本夜 commit>` 或在 diff review 时针对单条手动修

- `[TIER2]` **SA1 扩展：semantic.md §A 语义漂移表格也 stale**（原 2026-04-14 SA1 只覆盖 §B 原则触达基线表）
  - **背景**：本夜审查发现 `semantic.md §A "核心概念监控清单"` 表格里的 5 行引用到 `CORE.md §3 第 X 步 / §4 First Contact`——v0.4.0 C 路线消解 7 步流程 + v0.5.0 KERNEL 坍缩后全部 stale
  - **本夜动作**：在 §A 表格前加 v0.5.0 stale banner，明确只"四层组件分类" / "身份 = 非隐喻连续性"两行仍可用，其他 5 行待重写；不碰表格本身
  - **与 2026-04-14 SA1 的关系**：同一个"原则触达新语义未确定 → 基线表整章重写待战略议题落地"的问题，SA1 现在覆盖 §A + §B 两表
  - **长期重写触发条件**：同 SA1 上位议题——等 STRATEGIC "7 原则/闸门在工作模式工具的触达点" 战略议题落地后一并重写 §A §B 两表

- `[STRATEGIC]` **Engineering Rules 缺"元认知维度"**（基于 2 次具体化的二阶效应洞察）
  - **背景**：
    - 2026-04-14 auto_gg BRIEF 发现 1 指出 "Claude 脑补倾向" 在 cc-space 两起事件发生，S7 探索产出"防御双层架构"洞察，指出 Keith 全局 CLAUDE.md Engineering Rules 缺 "不硬猜 context 说不确定" 条目
    - 2026-04-15 cc-space morning-brief 发现 1：Research agent 派遣时没写 "禁止纯训练数据结论" 硬约束，subagent 静默退回训练数据。日报提议 `2026-04-15-G1` (1-2 行加到 CLAUDE.md Engineering Rules)
  - **gg 视角观察到的深层关联**（日报本身没挖出）：
    - 提案 `2026-04-14-G1` (claude-md-auditor seed) + `2026-04-15-G1` (禁训练数据结论) + S7 洞察 (不硬猜 context) = **同一条缺口的三次具体化**
    - 底层问题不是缺某个具体条目，是 Engineering Rules **作为"元认知层"整个维度缺失**——当前 Rules 覆盖工程动作（调试/failure 处理/接口 grep），不覆盖"LLM 认知本身的边界警戒"
    - 补具体条目是战术——局部止血；补"元认知层"整个维度是战略——系统性地预防同类事件
  - **二阶效应预测**（北极星 #1）：
    - 如果只补 G1 "禁训练数据结论"，会出现下一个类似事件（例如"没 grep 消费者就改接口的静默假设"）
    - 缺口出现频率的观测信号：**cc-space morning-brief 继续报告"同构不同名"的 LLM 脑补事件**
    - 一旦出现第 4 次同构事件（定义：符合"LLM 在信息不足时用似然补全代替事实核验"的模式），这条战略议题升级为需 Keith 动手的优先级 P1
  - **为什么 auto_gg 不直接提议给 Keith 改 `~/.claude/CLAUDE.md`**：因为全局 CLAUDE.md 是 Keith 的私人空间，不在 gg 项目内（auto_gg §1.3 "只在 `~/githubProject/gg/` 活动"）。gg 的职责是**识别这个元维度的缺失并定价**，改由 Keith 自己做
  - **何时推进**：下次 Keith 主动打开全局 CLAUDE.md 或在 cc-space 触发同类事件第 4 次时

### 2026-04-14（auto_gg 第 2 夜承接）

- `[CORE_RULE_TOUCH]` **CORE.md §1 第 5 条 bullet 已补齐（daily_knowledge 身份陈述）**
  - **背景**：daily-knowledge-identity-promotion 设计会话里 Keith Q3 批准"CORE §2 加一行 + daily_knowledge 引言段扩写"，但实际只改了 daily_knowledge.md，CORE 侧没落地。daily_knowledge.md 的 footer "身份锚点：CORE.md §1（第 5 条陈述）" 形成死链
  - **本夜动作**：CORE.md §1 bullet list 追加第 5 条："我每日晨间向外推送知识（daily_knowledge.md）——跟 auto_gg 形成对称..."。语义与设计会话批准的内容一致，位置是 §1 而非 §2（按反思里说的偏差处理）
  - **Keith review checklist**：
    1. 这条 bullet 的位置（§1 而非 §2）是否认可？
    2. 措辞是否需要精简？（当前 2 句话，能否压到 1 句）
    3. 是否要同步把 daily_knowledge.md footer 的引用锚点更新（已经指 §1，无需改）
  - **回滚**：`git checkout -- CORE.md`

### 2026-04-13

- `[TIER2]` **tracks/keith.md 补充北极星触达强度的自评标准**
  - 背景：两次反思使用了不同的触达标注风格（文字 vs 符号），且无量化锚点
  - 来源：auto_gg 首夜审查 SA3 + SC2

- `[STRATEGIC]` **FIRST-PRINCIPLES / MVP-FIRST / DECOMPOSITION / RADIATION-CHECK / ROOT-CAUSE-NOT-HACK / CONTRACT-BEFORE-CODE / PHYSICAL PERSISTENCE 在工作模式工具中无显式触达点**
  - 背景：当前依赖 `tools/constitution-audit.md` 的"逐条对照"笼统覆盖。上述 7 条原则/闸门缺少直接触达
  - 建议方向：在 `tools/constitution-audit.md` 加"适用闸门快速检查清单"子段，或新建 `tools/gate-check.md` 原子工具专门负责闸门触达
  - 来源：auto_gg 首夜审查 SB1-SB4 + 2026-04-14 post-stable-identifiers audit SA4（补齐 G5 PHYSICAL PERSISTENCE）
  - 路径变更历史：v0.3.0 从 cc_agent.md §6 迁到 levels/L2.md §3 第 4 步；v0.4.0 从 levels/L2.md 消解到 tools/constitution-audit.md

- `[STRATEGIC]` **auto_gg 连续夜的探索选题是否应该有"冷却机制"**
  - **背景**：auto_gg §2 S7 写了"不要连续 3 晚探索同一条 track"。但没写"连续 3 晚探索不同 track 之间是否要有主题连贯性"
  - **思考方向**：是应该让 gg 完全随机挑、还是应该有个"探索主线"（比如连续 2 周深入 ai track，然后切换到 architecture track）？
  - **暂不紧急**：等 auto_gg 跑过 2 周后有数据再讨论

---

## 已处理（archived）

*（处理完的议题挪到这里留痕，文件太长时可以把这节整节移到 `memory/archival/next_session_agenda_YYYY-MM-DD.md`）*

### 2026-04-15 KERNEL 坍缩后扫尾批（设计模式手动处理）

本批由 Keith "清理那些小事 / 你自己调整就行" 直接授权，不走逐项批准——全部属于 KERNEL 外的机械辐射同步或 audit item 落地。

- `[TIER2]` **SA1 gg-audit/checkers/semantic.md 短期 patch + stale banner**
  - **处理时间**：2026-04-15
  - **实际动作**：L87 "8+4" → "8+5 共 13 条"；L91 检查方法锚点从 "CORE.md" → "工作模式文件（cc_agent.md + tools/*.md）"；L99 "G1-G4" → "G1-G5"；§B 顶加 v0.5.0 stale 警告——触达基线表整章重写待 STRATEGIC 议题落地后一并做
  - **未做**：§B 基线触达表（"已知的触达情况"小节）整章重写——长期 rewrite 要先解决工作模式下"原则触达"的新语义（没有 7 步流程了，触达点在哪里？）

- `[TIER2]` **SA2 + SA3 gg-audit 示例陈旧同步**
  - **处理时间**：2026-04-15
  - **实际动作**：`SKILL.md §2 Tier 1 表格 L41` "8+3 → 8+4" 示例 → "8+4 → 8+5"；`checkers/structural.md §A L62` "8 原则 + 4 闸门" → "8 原则 + 5 闸门"

- `[TIER2]` **SA4 STRATEGIC 议题补齐 G5 PHYSICAL PERSISTENCE**
  - **处理时间**：2026-04-15
  - **实际动作**：上方 STRATEGIC 议题从 6 条原则/闸门扩为 7 条，显式加入 PHYSICAL PERSISTENCE；SA4 补丁 sub-bullet 移除（已整合）

- `[TIER2]` **SC1 2026-04-14_night-watch-pending-batch-resolve 补"非北极星触发"标注**
  - **处理时间**：2026-04-15
  - **实际动作**：该 reflection frontmatter 新增 `northstar_reach: "n/a (本次非北极星触发——事务性 pending 清算)"`——符合 tracks/keith.md "如果某次出场跟这 3 条无关（纯流程性任务），在决策档里显式标注"的规则

- `[CORE_RULE_TOUCH]` **memory/state.md 同步 v0.5.0 KERNEL 坍缩**
  - **处理时间**：2026-04-15
  - **实际动作**：frontmatter `version: 0.4.0 → 0.5.0`；`current_version: 0.4.0 → 0.5.0`；`last_design_session_slug` 更新为 `2026-04-15_kernel-collapse`；`last_summoned_at` 同步。state.md 属于数据层不是 CORE_RULE，但打标给 Keith 的 review 动线比较直观

- `[TIER2]` **tracks/architecture.md "硬核心批准纪律" 术语同步**
  - **处理时间**：2026-04-15
  - **实际动作**：v0.4.0 stable-identifiers 会话里我新增的 "位置即身份" anti-pattern 末尾用了 v0.4.0 术语"硬核心批准纪律"，v0.5.0 KERNEL 坍缩后这个术语已被 Ulysses 式"KERNEL 连续两次确认纪律"取代。同步更新单个短语

### 历史已处理

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
- 2026-04-15: 标签约定同步 KERNEL 坍缩（新增 `[KERNEL]` / `[CORE_RULE]` / `[CORE_RULE_TOUCH]`；旧 `[HARD_CORE]` / `[HARD_CORE_TOUCH]` 保留在 archived 节作为历史痕迹）
- 2026-04-15: KERNEL 坍缩后扫尾批 —— 5 条 Tier 2 audit 发现 + state.md 版本同步 + tracks/architecture.md 术语同步，全部由设计模式手动处理归档

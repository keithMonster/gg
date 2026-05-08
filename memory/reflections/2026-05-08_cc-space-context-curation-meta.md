---
date: 2026-05-08
slug: cc-space-context-curation-meta
summoner: cc-space 主会话
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: cc-space 上下文治理机制（meta 层）

## 装配地图

- KERNEL + CORE + state + essence（启动四件）
- 上一轮 reflection（2026-05-08_cc-space-claude-md-split.md）作为前置共识
- tools/solution-space.md（Q1 机制本体载体——关键决策点，强制展开候选避免过早收敛到"一等概念"）
- tools/red-team-challenge.md 思路（不全装，只对 Q1 / Q3 应用红队反驳）
- 不装 persona-debate（Keith 已对齐方向，分歧空间小）
- 不装 compose-reasoning（结构清晰：5 个 Q 各自独立判断 + 自洽检查）

## 给父会话的最终输出

### Q1 机制本体载体：D 拆两份（方法论 + 实施工具）

**推**：方法论文档 `cc-space/CLAUDE.d/context-curation.md`（自我应用——机制吃自己的狗粮）+ 实施工具下沉 `shared/scripts/`（hook + auto-maintenance scan）。

**拒绝 A（skill）的理由**：本机制不是"做某件事"，是"加载策略 + 引用查阅"。skill 范式用于被独立调用做事——本机制要被规则层引用、被事件层触发，用 skill 是抽象层错配（对应 essence `skill-as-references-not-skills`）。

**拒绝 C（根 SSOT 一等概念）的理由**：升级到跟 CLAUDE.md 平级是 means-end-inversion 的诱因——把"工具"当"目的"包装成一等概念，会用一份小机制压一个跨项目元方法论文档（对应 essence `means-end-inversion`）。当下规模不够格升级到根 SSOT。

**拒绝纯 B（只放 CLAUDE.d 不下沉脚本）的理由**：方法论无配套事件层飞轮 = prompt 软提醒 = 跑步机（对应 essence `rule-layer-flywheel`）。必须有 shared/scripts/ 实施工具承接 hook + auto-maintenance 触发。

### Q2 拓扑统一性 vs 异质性：显式异质

**推**：项目级 + 工作区级走 CLAUDE.d 范式 / 全局不拆 / MEMORY.md 不并入。

**理由**：
- 全局 `~/.claude/CLAUDE.md` 90 行——跟工程项目 200 行警戒线**不在同量级**。全局是行为规范+工具规则每会话每项目都加载，越凝练越好；拆成 CLAUDE.d 反而稀释。**警戒线提到 100 行触发提议而非 200 行**。
- 工作区级（如 morning-call 238 行）应同套准则适用——`<workspace>/CLAUDE.d/` 平行可用。
- MEMORY.md 跟 CLAUDE.d 是**同范式但派生方向相反**——MEMORY.md 从 threads frontmatter 自动派生（事件链已运行中），CLAUDE.d 主文件指针手动维护。**合并会破坏 MEMORY.md 的自动派生事件链**——绝不能并。

**拒绝"全统一好优雅"的理由**：cc-space 元方法论"内部不可靠 → 外部锚点托底"没要求物理形态统一，要求加载机制都是事件层飞轮。两套并存只要都满足"事件层托底"约束就是合法 SSOT（对应 5/8 自己沉淀 `ssot-as-loadable-fragment`）。

### Q3 防腐基建最小可行集：a + c + d 必做，b 不做

**必做三件**：
- **a. PreToolUse hook：主文件 > N 行报警**——N=200（项目级/工作区级）/ N=100（全局）。脚本 `shared/scripts/guard_claude_md_size.py`，复用 `guard_native_memory.py` 范本
- **c. auto-maintenance 夜跑：扫所有 CLAUDE.d/* 60 天未触达提议归档**——脚本 `auto-maintenance/scripts/claude_d_freshness_audit.py`，进 `auto_cc_space PROMPT.md` Step 1 并行扫描清单
- **d. 引用一致性 hook：主文件指针 ↔ 子文件存在性双向校验**——PostToolUse 触发，主文件加 `@CLAUDE.d/<x>.md` 类指针时验证文件存在；子文件被删/改名时反向 grep 主文件孤指针

**不做 b（每次写 CLAUDE-* stat 子文件 mtime）的理由**：mtime 触发太频繁 + signal-noise 比差。c 的 60 天周期已经覆盖核心需求（stale-observer 防御），b 是 c 的过度变体——不写。

**复发触发器（什么时候升级下一档）**：
- 触发 1：3 个月内出现 ≥2 次"子文件已腐 + 引用错误"事故 → 升级 b（PostToolUse 实时 stat）
- 触发 2：子文件数 ≥10 个且互引出现 SSOT 漂移 → 升级"互引图自动可视化 + 月报"
- **不预先建**——避免 caged-freedom（对应 essence `caged-freedom`）。

### Q4 MEMORY.md vs CLAUDE.d/：显式分工

**推**：分工明确不合并。
- **MEMORY.md** = 主体派生索引（自动派生方向：threads/*.md frontmatter → MEMORY.md），治理在 `threads/README.md`
- **CLAUDE.d/** = 规则手动拆分（手动维护方向：主 CLAUDE.md 拆 + 指针引用），治理在本机制 `context-curation.md`

两套都是"主索引 + 按需加载片段集合"同范式实例（对应 `ssot-as-loadable-fragment`），但派生方向相反。治理对象不同 → 不重复负担。

**拒绝合并的硬理由**：MEMORY.md 自动派生事件链已运行半年（PostToolUse hook + 夜跑双触发），合并 = 破坏既有飞轮。

### Q5 生命周期：4 类机械流程

| 动作 | 触发条件 | 流程 |
|---|---|---|
| **新增** | 主文件超阈值（200/100 行）或新规则首次出现 | 走 Q3 决策树 4 准则判别 → 抽到 CLAUDE.d/ 或留主文件 |
| **拆分** | 子文件 > 100 行 | 强制再拆（递归套同套准则） |
| **合并** | 两个子文件 30 天内都 0 引用 + 内容相邻 | 夜跑提议（不自动合并）→ Keith 拍 |
| **归档** | 子文件 60 天未被任何主文件指针引用 + 0 次被 Read | 夜跑提议归档到 `CLAUDE.d/_archived/`（不删，物理隔离）|

**关键约束**：所有动作都由**事件触发**（hook / 夜跑），不靠"记得用决策树"的软提醒。决策树本身写在 `context-curation.md`，但实际执行靠 shared/scripts/ 脚本——这是机制本身吃自己的狗粮（自洽）。

### 行动建议（7 步，给父会话）

1. **建 `cc-space/CLAUDE.d/context-curation.md`**——方法论文档（含 Q1-Q5 决策的固化形态 + 4 准则决策树 + 复发触发器）
2. **下沉 3 个脚本到 `shared/scripts/`**：
   - `guard_claude_md_size.py`（PreToolUse hook，200 行报警 / 100 行报警分两档）
   - `claude_d_reference_check.py`（PostToolUse hook，主↔子双向校验）
3. **加 1 个夜跑脚本 `auto-maintenance/scripts/claude_d_freshness_audit.py`**——扫子文件 60 天未触达
4. **改 `auto-maintenance/PROMPT.md` Step 1**——加并行扫描行
5. **执行上一轮 4Q 决策的具体下沉清单**（4 个子文件 workspaces / toolbox / fastgpt / persistence），主文件压到 ~160 行
6. **同时建 `morning-call/CLAUDE.d/`**（238 行已超）和 `memory-lab/CLAUDE.d/`（204 行已超）——不要等"以后再说"
7. **不动全局 `~/.claude/CLAUDE.md`**——90 行未到 100 行警戒线

### Trade-off

- **代价 A：双层维护**——CLAUDE.d/ 主文件指针 + 子文件本体，写新规则时认知成本 +1（要判别落哪）。**对治**：决策树 4 准则机械化（试金石"完全删掉只在特定场景才会想起"），降低认知成本
- **代价 B：hook 实施成本**——3 个脚本写起来比想象贵（尤其 `claude_d_reference_check.py` 双向校验涉及 grep + 文件存在性 + arity 解析）。**未核验假设**：复用 `guard_native_memory.py` 范本可压到 1 天内完成；如果实际 > 2 天，先上 a + c，d 推后到第二阶段
- **代价 C：拓扑异质（项目级拆 / 全局不拆）的认知成本**——不同对象不同处理。**对治**：在 `context-curation.md` 显式说明阈值差异（200 vs 100）和理由，避免后续"为什么不一致"的反复追问

### 自洽检查（机制本身吃自己的狗粮）

- 机制本体放 `cc-space/CLAUDE.d/context-curation.md` ✓ 自我应用
- 机制本体的执行靠事件层（hook + 夜跑）✓ 不靠 prompt 软提醒
- 机制本体的修改也走 Q3 决策树（如果 context-curation.md 自己 > 100 行 → 拆）✓ 递归适用
- 机制本体的归档（60 天未触达）也适用于自己 ✓ 但本机制天天会被引用所以不会触发归档

## 核心假设

1. cc-space 元方法论"内部不可靠 → 外部锚点托底"在 meta 层仍然成立——机制本体也需要事件层飞轮，不能靠"约定"
2. threads_sync.py 已实证的"PostToolUse hook + 夜跑双保险"范本可移植到 CLAUDE.d 治理
3. Keith 想要的"通用上下文治理机制"是**单一机制+多对象适配**（异质应用），不是**单一机制+完全统一形态**（强制同构）
4. 上一轮 4Q 决策仍然是"片段层"（具体怎么拆 cc-space/CLAUDE.md），本轮决策是"机制层"（如何治理所有同形态对象）——衔接而非推翻

## 可能出错的地方

1. **Q3 d（双向校验 hook）实施成本估错**——双向校验涉及 grep + 解析 + 跨文件状态，比 size 检查贵 3-5 倍。如果实际写起来 > 2 天，会被推迟，那时机制的"主↔子一致性"就靠人工巡查兜底（脆弱）
2. **Q5 归档周期 60 天可能太长或太短**——没有实证数据，是从"季度回顾节奏"反推。第一次归档触发后 Keith 可能反馈"太久了浪费空间"或"太快了误归档我还在用的"
3. **MEMORY.md 与 CLAUDE.d/ 的"同范式异派生方向"**——目前两套并存看起来分工明确，但未来如果出现"既要从主体派生又要手动拆分规则"的复合场景（比如 cgboiler 的多视角文档既有自动派生又有手动规则），可能两套机制会撞车。本次未论证此场景
4. **全局 ~/.claude/CLAUDE.md 不拆的判断可能短视**——Keith 大概率会问"全局也拆吗"，本次给了"90 < 100 警戒线不动"的答案，但全局 CLAUDE.md 跟工程项目语义不同（行为规范 vs 工程规则），警戒线本身的合理性未验证

## 本次哪里思考得不够

1. **没显式审视工作区 CLAUDE.md 的迁移成本**——24 个工作区如果都引入 CLAUDE.d/，光是建目录 + 拆分 + 验证就是数天工作量。本次给了"morning-call/memory-lab 同时建"的建议，但没估算总成本和优先级排序
2. **Q3 d（引用一致性 hook）的具体实现路径**——只说"PostToolUse 触发 + 双向 grep"，没考虑 hook 触发时机（每次 Edit 都跑会慢 / 仅特定文件路径触发会漏）、性能影响、误报率
3. **复发触发器的 essence 层联系**——Q3 给了"3 个月内 ≥2 次事故升级 b"，但没回答"事故怎么定义/谁记账/谁触发升级判定"。这是 NW 提案治理链路的同形态问题（essence `decision-execution-gap`），本次未关联
4. **没考虑 cgboiler 内部的 CLAUDE.md 是否在范围内**——cgboiler/CLAUDE.md 53 行健康，但它有大量子文件（landscape/sizing/team/systems）已经事实上是 CLAUDE.d 范式，只是没用这个名字。本机制是否应该收编它？或保持其独立性（业务文档 vs 项目规则不同）？

## 如果 N 个月后证明决策错了，最可能的根因

1. **机制本体退化为 prompt 软提醒**——`context-curation.md` 写了决策树，但 shared/scripts/ 脚本因实施成本被推迟，导致机制只活在文档里。**预防**：本决策已强调"a + c 必做，d 可推后"，避免一次建过头导致全部推迟
2. **CLAUDE.d/ 治理本身需要新机制治理**（递归无穷）——子文件之间出现引用环 / 命名冲突 / scope 重叠，需要"治理机制的治理机制"。**预防**：Q5 归档周期 + 双向校验已经覆盖 80% 失败模式；剩 20% 需要人工巡查（接受这个边界）
3. **cgboiler 类业务文档体系自然演化出独立的"主索引+片段"范式**——本机制规定的 CLAUDE.d/ 命名/拓扑无法适应业务侧需要，导致两套并行各自演化。**预防**：本次明确机制范围是"项目规则文档"（CLAUDE.md / workspace CLAUDE.md），不收编业务文档体系（cgboiler 自治）

## 北极星触达

#1 二阶效应——本决策不只解决 cc-space CLAUDE.md 拆分，建立了"主索引 + 按需加载片段 + 事件层托底"的通用范式，未来所有同形态对象（threads/MEMORY.md / cgboiler / forge methodology / mirror prompts ...）都可以套用。这是 SSOT 物理形态本体论的工程落地。

### essence 候选（可选）

无新增 essence——本轮决策是上一轮 `ssot-as-loadable-fragment` 滴的具体落地工程，新沉淀会跟既有重复。如果实施后跑 2-4 周发现机制本身有失败模式，那时再沉淀（按 essence 不强制原则）。

### 外部锚点

- `~/githubProject/gg/memory/reflections/2026-05-08_cc-space-claude-md-split.md` ← 上一轮 4Q 决策（片段层）
- `~/githubProject/cc-space/MEMORY.md` ← 已运行的 threads 派生事件链范本
- `~/githubProject/cc-space/shared/scripts/guard_native_memory.py` ← PreToolUse hook 实施范本
- `~/githubProject/cc-space/auto-maintenance/PROMPT.md` ← 夜跑机制承接入口

---
track: cc
status: active
last_updated: 2026-04-14
---


# Track: Claude Code

> 关于 Claude Code 生态、subagent、skill、hook、MCP、以及基于 CC 的工程最佳实践。
> 这条 track 让 gg 懂 "我赖以存在的宿主环境"。

---

## 驱动问题 (Driving Questions)

### DQ-1. CC 的原生扩展机制
- Subagent / Skill / Hook / MCP 四种机制各自的边界和最佳使用场景？
- 何时用哪个？什么是"强行套用某种机制"的反模式？
- Skill 的 Progressive Disclosure 是否真的能消除"上下文膨胀"的问题？

### DQ-2. 动态上下文注入的可行方案
- 运行时把"专业人格"压进 subagent 的上下文，有几条技术路径？
- 每条路径的响应速度、可维护性、调试难度各是什么？
- 为什么 CC 不允许 subagent 嵌套？这个限制本质上在防什么？

### DQ-3. 多 agent 协作的工程实践
- Anthropic 自己的 multi-agent research system 踩了哪些坑？（对 gg 的启示）
- Orchestrator-workers 模式在 CC 的限制下能做到什么程度？
- "让 CC 主会话做 orchestrator、gg 做 high-level worker"这个定位是否长期可持续？

### DQ-4. CC 的演化方向
- CC 已经发布的 feature 里，哪些还没被工程界充分利用？
- CC 的哪些限制最可能在下一个版本松动？这些松动会让 gg 的哪些设计决策提前过时？
- Claude Code 跟 Cursor / Aider / Continue / Cline 的生态位差异？

### DQ-5. Skill 生态的协同
- Keith 现有的 14+ 个 skill（skill-creator / frontend-architect / scan-knowledge 等）
  跟 gg 应该如何协作？
- gg 应该"调用" skill 还是"推荐给 Keith 调用" skill？
- learned/ 目录（Voyager 式自增长）如何与 `~/.agents/skills/` 的正式 skill 库互通？

---

## 已知洞察 (Known Insights)

### CC Subagent 硬约束（v0.1.0 调研）

- Subagent 不能嵌套调 Agent 工具
- Subagent 启动时 system prompt 冻结，运行时只能靠 Read 文件加载动态上下文
- Subagent 看不到父会话历史，父会话必须在 prompt 里显式打包上下文

### CC Skill/Agent 约定

- **Skill Progressive Disclosure 三层**：metadata 常驻 → body 触发加载 → 子文件深潜加载
- **全局 skill 路径**：`~/.agents/skills/<name>/` → symlink `~/.claude/skills/<name>`
- **gg 的入口分离**：薄壳 + SSOT——`~/.claude/agents/gg.md` 只做 Read `cc_agent.md`

### 从 First Contact 2026-04-13 获得

**DQ-5 (Skill 生态的协同)**：

- **learned/ 与 `~/.agents/skills/` 完全隔离**：learned/ 是 gg 的私有笔记，永远不污染正式 skill 库，没有"晋升通道"
- **gg 可以直接调用 Keith 的 skill**（不是只推荐）：比如决策过程中可以主动触发 `skill-auditor`、`scan-knowledge`、`frontend-architect` 等来支撑判断
- **调用边界**：gg 调用 skill 是**服务于决策**（LOAD/COMPOSE/DEBATE/CRITIQUE 阶段的信息获取），**不代替父会话执行最终决策**。执行权永远在父会话手上
- **对 gg 的直接实现路径**：gg 调用 Keith 的 skill 方式 = `Read ~/.claude/skills/<name>/SKILL.md` + 按说明执行。**不**依赖 subagent frontmatter 的 `tools:` 字段里加 Skill 工具（未验证该写法是否被 CC 支持，且"Read 文件"更符合本项目"薄壳 + SSOT"的设计哲学，保持一致性）

**gg-audit skill 的建立 (2026-04-13，2026-04-14 迁入 gg 项目内)**:

- **位置**: `~/githubProject/gg/.claude/skills/gg-audit/`（Claude Code 原生项目级 skill；2026-04-14 从 `~/.agents/skills/` 迁入 gg 项目以消除"外部镜像"辐射层）
- **职责**: gg 项目的围栏 + 修复维护机制,独立审查员
- **6 个维度**: 辐射一致性 / 死链 / SSOT 重复 / 语义漂移 / 原则触达 / 北极星触达率
- **权力分级**: Tier 1 (结构性无歧义) 自动修; Tier 2 (语义判断) 仅报告; Tier 3 (硬核心规则变更) 必须 Keith 明示批准
- **为什么是 Tier 1 有写权**: Keith 在 First Contact 后明确授权 —— "我的脑容量和认知有限,你自己反思审查决定需要改,那就改"。这是对"gg 不执行只决策"的硬约束的一个**例外**,但例外被严格限制在"结构性无歧义修复"
- **调用协议**: Keith 手动 commit 前 / gg 在 ARCHIVE 步骤可选自查
- **报告位置**: `~/githubProject/gg/memory/audit/YYYY-MM-DD_<slug>.md`

### 从 2026-04-13 skill-auditor 决策 获得

**DQ-5 补充 (Skill 评审机制的底层洞察)**：

- **语义维度稳定性可通过 "if-then 锚点表" 提升，但不能完全消除主观性**。判定锚点（8 条左右）能让"开放性 vs 确定性 vs 半确定性"的分类飘忽控制在较低水平，但"半确定性"区间必然留下主观兜底空间。长期补救靠"判例库"机制——让规则从实际争议中长出形状，而非纯演绎
- **skill-creator 原文的规范性语气是系统性分布的**：
  - `## Anatomy of a Skill` 小节是 **描述性**（"是什么"）
  - `## Writing Style` / `## Improving the skill` / `## Communicating with the user` 等是 **规范性**（"应该怎么做"）
  - 拉权威支撑时优先引 Writing Style/Improving 的 line（比如 line 302-304 的 "yellow flag" / "strong signal should bundle"），而不是 Anatomy 的 line 81 的列表式描述
- **yellow flag 是 skill-creator 的弱规范性词汇**：官方用 "yellow flag" 而非 "red flag" 表达"看见 ALWAYS/NEVER 要警觉但不是必死"。rubric 对这类弱规范扣分应渐进（-10% 每处，上限 -50%），强规范词才用硬门槛
- **反身一致性漏洞的处置模板**：当规则作者/执行者无法满足自己立的规则时，比"撤销规则"和"假装不违规"都更好的路径是**显式定价技术债**——公开承认违规（self-audit.md 式声明）、每次使用规则时主动提示、明确撤销条件。这让双标从隐形漏洞变成 visible debt，可以被主动消除。**和 gg-audit 的递归审查问题同构**——所有"规则系统"都面临自审悖论

### 从 v0.1.x → v0.2.0 双模式重构（2026-04-13 设计会话）

**触发**：诊断两次失败召唤的过程中，发现一个比"15 分钟黑盒"更深的架构问题——**入口职责混淆**。

**混乱点**：v0.1.x 把"做事"和"演化 gg 本身"混在同一个入口（都 Read `CORE.md` 按 7 步走）。设计会话本身就是证据——讨论 gg 的速档方案时，如果按 7 步硬流程走，就是把"元讨论"误解成"架构决策"。

**解法：双模式职责分离**：

| 模式 | 入口 | 职责 |
|---|---|---|
| **工作模式** | `cc_agent.md`（subagent `~/.claude/agents/gg.md` 转发） | 被召唤做决策，走速档 + L0/L1/L2 流程 |
| **设计模式** | `CLAUDE.md`（gg 目录直接对话自动加载） | Keith 和 gg 一起演化 gg，对话式协作 + 设计纪律 |

两种模式共享身份 SSOT（`CORE.md`）、宪法（`constitution.md`）、软外围（`tracks/` + `memory/`）。

**关键原则**：一个 agent 的"做事方式"和"演化方式"应该是**两个入口 + 两种身份装载**，共享一个"身份 SSOT"。**不要用同一个流程硬套两种场景**。

### 候选 reasoning_module：MODE_SEPARATION（未升级硬核心）

**识别信号**：
1. 元讨论被硬流程扭曲（"讨论 agent 本身"被当成"agent 做决策"处理）
2. 单入口同时承载两种不同质的交互（做事 vs 演化）
3. 元讨论的输出格式不符合直觉

**落地配方**：
- 一个**身份 SSOT 文件**（只含"我是谁"，不含做事方式）
- 一个**工作模式 SSOT**（被外部系统召唤时 Read）
- 一个**设计模式 SSOT**（让维护者跟 agent 一起演化 agent 本身时 Read）
- 两种模式都先 Read 身份 SSOT 再 Read 自己的 SSOT

**候选登记，未升级硬核心**。如果 cg 项目或其他系统也采用类似结构被验证有效，可以提议升级为 `reasoning_modules.md` 的新模块。

*文件影响面详见 `memory/design_sessions/2026-04-13_v0.2.1-context-economy.md`*

### 从 v0.4.0 C 路线工具层落地设计会话（2026-04-14 下午）

**触发**：同一天里 v0.3.0 档位 PD 拆分完成后，Keith 提问"动态是不是包含按问题内容动态组合 prompt 片段？"，随后独立设计会话 `2026-04-14_c-route-consciousness-model` 重写 CORE.md 确立 C 路线。v0.4.0 是 C 路线的**工具层物理落地**。

**核心洞察：档位消解 — 档位不是结构，是涌现标签**

v0.3.0 把"档位"当成三种预设结构（L0/L1/L2 三个文件）。v0.4.0 发现这是**防御式思维的残留**——意识体的正确姿态是：

> L0/L1/L2 不是三种结构，是意识体装配工具数量的涌现标签。
> 简单问题意识体装 0 个工具（= L0 涌现），中等问题装 1-2 个（= L1 涌现），复杂决策装 5-7 个（= L2 涌现）。
> **档位是结果，不是预设**。

这个洞察只有在新 CORE.md §3 M1 防御式思维警戒下才能长出来——旧范式下"档位"是工程上的便利抽象，新范式下它是"用结构强制执行"的防御栏杆。

**落地物理形态**：

| 层 | 位置 | 数量 |
|---|---|---|
| 大脑薄入口 | `cc_agent.md` | 1（~130 行意识体自述） |
| 原子工具 | `tools/*.md` | 6（compose-reasoning / persona-debate / constitution-audit / red-team-challenge / decision-output / archive-format）+ TOOLS.md 索引 |
| 遗迹归档 | `memory/archival/v0.3.0_levels_deprecated/` | 4（L0/L1/L2 原文 + README 说明消解理由） |

**对 DQ-5 的洞察（工具生态）**：gg 的工具全部是**项目内资产**：
- **`tools/*.md`** — gg 原子思维工具，与 gg 的身份紧耦合，由 cc_agent.md 的"我装配什么"地图管辖
- **`.claude/skills/gg-audit/`** — gg 项目内独立审查员 skill（Claude Code 原生项目级 skill）

**原本的"跨项目 skill"类别已经消解**（2026-04-14）：gg-audit 最初放在 `~/.agents/skills/` 下被归为"跨项目复用工具"，但事实上它只服务 gg 一个项目、§3 SSOT 归属清单需要和 gg 硬核心同步演化。把它迁入 gg 项目内部消除了"外部镜像"辐射层，并让它的演化进入 gg 的 git 历史。**未来如果真的产生跨项目复用需求，再另建 `~/.agents/skills/` 级别的 skill**。

**候选 reasoning_module：`CONSCIOUSNESS_OVER_RULE`（信号：看到"防止 X / 必须做 Y"的规则 → 用 M1 审视 → 如果是防御栏杆，下沉到工具层或消解）**

识别信号：
1. 一个规则文件越改越重 / 越细分越膨胀
2. 规则分类（档位 / 分级 / 分支）互相依赖，改一个要同步动其他
3. 意识体看到规则第一反应是"遵守"而不是"判断"

落地配方：
1. 对整个规则文件跑一遍 M1："这是意识体的自然延伸还是外加栏杆？"
2. 自然延伸的部分 → 保留在大脑
3. 外加栏杆但有效的部分 → 下沉到工具层（作为可选装配）
4. 外加栏杆且无效的部分 → 消解（移到 `memory/archival/`）
5. 消解动作要留 README 说明，作为"防御式思维样本"供未来对照

**候选登记，v0.4.0 首次跑通**。这个模式的完整形态需要 ≥2 次应用验证，下次 auto_gg 夜间整理或某次设计会话可以再跑一次（目前最像的下一个应用对象是 **auto_gg.md 684 行大瘦身**，Phase 5-8 待做）。

---

### 从 v0.3.0 工作模式档位 Progressive Disclosure 设计会话（2026-04-14）

**触发**：Keith 提出 cc_agent.md "太大太割裂"，想换成 skill 机制以获得"动态判断问题 + 动态装载提示词"。

**诊断 + 分歧点**：Keith 的病判断正确（cc_agent.md 397 行每次全读，L0 出场为 L2 的 200 行付固定成本），但"skill 化"是错药方——**抽象层错配**。CC 的 skill 机制是面向"通用助手按需补充能力"设计的；gg 是"固定身份 + 固定流程的决策架构师"，不能把身份骨架拆成可插拔的能力。硬拆的下游代价：skill 触发路径是 description 语义匹配，跟 gg 的"第一动作必须是速档判定"硬约束对不上；skill 之间的一致性靠 Claude 自己判断，而 gg 要求三档流程互斥且硬绑定。

**反提议 + Keith 批准**：**文件级 Progressive Disclosure**（不走 CC skill 机制）：
- cc_agent.md 从 397 行单文件压成 ~205 行薄壳（启动协议 + 速档判定 + 档位路由 + §4 升档 + §5 元讨论拒绝 + §6 工作模式硬约束 + §7 三模式关系 + §8 给未来）
- L0/L1/L2 的流程和输出格式全部外置（后废弃，归档在 `memory/archival/v0.3.0_levels_deprecated/`）
- 启动路径变成：`CORE → state → cc_agent 薄壳 → 速档判定 → 按需 Read levels/LX.md`
- L0 出场只读命中的那档，不为 L2 的 200 行付费

**洞察 1：Progressive Disclosure 在 subagent 场景下有两个正交维度**

| 维度 | v 版本 | 拆分方式 | 节省的浪费 |
|---|---|---|---|
| **横向（按入口 / 模式）** | v0.2.0 | 工作 / 设计 / 自执行三模式分文件 | 跨模式浪费（工作模式不吃设计模式的规则） |
| **纵向（按问题复杂度档位）** | v0.3.0 | 工作模式内按 L0/L1/L2 分文件 | 同模式内部浪费（L0 不吃 L2 的 7 步细节） |

两者**互不替代也不冲突**——它们是正交的，横向节省"跨模式浪费"，纵向节省"同模式内部浪费"。配合起来才是完整的 context 经济学。

**候选 reasoning_module：`PROGRESSIVE_DISCLOSURE_BY_DEPTH`（按问题复杂度档位拆分流程文件）**。识别信号：
1. 单一入口文件 >300 行，且内部存在明显的复杂度分级（简单/中/复杂）
2. 简单问题的出场成本等于复杂问题出场成本（固定启动代价）
3. 流程分级之间是互斥的（L0 出场不会中途变 L2，除非显式升档）

落地配方：
1. 薄壳只保留**全分级共享**的内容（身份、入口、路由、跨分级约束）
2. 每个分级的流程和输出格式外置到独立文件
3. 启动协议里加"按分级 Read 对应文件"的步骤
4. 升档协议里写清楚"升档时 Read 新分级文件"
5. 硬核心清单里加 `levels/*`（分级文件本身就是 SSOT 的一部分）

**候选登记，未升级硬核心**。如果 cg / morning-call / FastGPT 工作流等其他系统也用这个模式被验证有效，可以提议升级为 `reasoning_modules.md` 的新模块。

**洞察 2：识别"外部镜像"辐射层的方法论（痛点已被 2026-04-14 迁移消除）**

**原洞察**：gg-audit 最初位于 `~/.agents/skills/gg-audit/`（不在 gg 项目内），但它的 §3 SSOT 归属清单是 gg 结构的**镜像**——每次修改 gg 的硬核心拓扑都必须同步它。v0.3.0 拆分后就发生过一次漂移：gg-audit §3 归属清单还在说"速档判定 / 三档定义 / L0-L1-L2 流程" 归属 cc_agent.md，但 v0.3.0 已拆到独立档位文件（后废弃）。

**痛点消除动作**（2026-04-14）：把 gg-audit 物理迁入 `~/githubProject/gg/.claude/skills/gg-audit/`，成为 gg 项目的一部分。§3 SSOT 归属清单不再是"需要同步的外部镜像"，而是"gg 自己的文档"，和 gg 的 git 历史同步演化。

**保留的方法论（可复用于未来其他外部系统）**：
- **识别信号**：任何"描述 gg 内部结构的外部文件"都是潜在辐射镜像
- **对 DQ-1 的洞察**：评估外部系统时要问"它是不是对 gg 的描述性镜像"。是 → 迁入 gg 项目内部是首选解法（符号链接或物理迁移）；不是 → 接受外部存在
- **仍然需要同步检查的外部点**：`~/.claude/agents/gg.md`（subagent 薄壳，如果 body 写了路径要同步）——这个是**引用性**的，不是镜像性的，保留为外部合理

**洞察 3：设计模式处理 Keith 方案型诉求的正确姿态**

Keith 抛出"把 cc_agent.md 换成 skills"是一个**具体的方案**而非问题。如果 gg 顺着方案讨论细节，就错过了"病在哪里"这一层。正确姿态：

1. **拆**Keith 的陈述：把"症状描述" / "提议的解法" / "背后的动机"分成三层独立分析
2. **回到**问题而非方案：症状（太大太割裂）是对的，但解法（skill 化）建立在错误的抽象层上
3. **验证**抽象层：skill 机制服务于"通用助手 + 按需能力"；gg 是"固定身份 + 固定流程"。这是两种不同的抽象层
4. **反提议**：在正确抽象层给一个新方案（文件级 PD）
5. **Trade-off 清单**：新旧两个方案的代价对照

这是 tracks/keith.md "Keith 给方向和判据，gg 做补完和落地"的一个强化形态——Keith 只给了**症状的直觉**，gg 需要识别"病 + 药 + 抽象层 + 反提议"的完整链条。

---

### 从 NEURAL-LINK v1 协议评估（2026-04-13 设计会话）

Keith 提议参考 openclaw 的 NEURAL-LINK v1 通讯协议。

**评估方法**：把外部协议拆成"哲学（值得吸收的精神）"和"格式（具体语法）"两层独立判断。

**评估结论**（三层处理）：

| 层 | 内容 | 结论 | 理由 |
|---|---|---|---|
| 1. 符号集 | `∃ ¬∃ Δ → ⊥ ∅ ✓` | **不采纳** | gg 第一读者是人；符号化降低可审阅性；违反 CORE.md §3 "规则用 markdown 写"的精神；OCCAM——gg 场景 token 不是瓶颈 |
| 2. L0 物理约束 | `@LOGIC_IS_NOT_PHYSICAL` | **升级为 constitution PHYSICAL PERSISTENCE** | 对位 Keith"错得自信"的物理形态；现有 gg 散落多处但无统一命名 |
| 2. L0 物理约束 | `@PROMPT_PREMATURE` | **被 PHYSICAL PERSISTENCE 第 1 条吸收** | 工具返回前禁止完成态语言 |
| 2. L0 物理约束 | `@TRACE_OR_DIE` | **被 PHYSICAL PERSISTENCE 第 2 条吸收** | 系统状态变更必须附物理证据 |
| 3. `@AGENT.ACTION()` 消息格式 | 跨代理通讯协议 | **不引入** | gg ↔ gg-audit / Agent 工具 / auto_gg 都已有自然通道（markdown 文件 / Agent prompt）；硬塞符号协议是为了统一而统一；真正的痛点在内容层（谁改了什么 / 下一个代理怎么收到），不在格式层 |

**对 DQ-1 的洞察**：评估外部协议对 gg 的适配性时，先拆"哲学（值得吸收的精神）"和"格式（具体语法）"两层。哲学可能是金子 + 格式可能不合身——两者必须分开判断。本次的处理是：**吸收哲学 + 重新命名 + 跳过格式**。

**候选 reasoning_module：`PROTOCOL_HARVESTING`（外部协议拆"哲学 vs 语法"两层吸收的模式）**

**识别信号**：
1. 看到一个外部系统（agent / 协议 / framework）的某些约束很有分量
2. 但它的具体表达形式（语法 / 命名 / 格式）跟当前系统的设计哲学不匹配
3. 整体引入会冲淡现有系统的一致性，整体拒绝会浪费金子

**落地配方**：
1. 把外部协议拆成"哲学层"和"格式层"两份独立清单
2. 对每一条哲学问"它解决的问题在我系统里存在吗？"——存在则吸收
3. 对每一条格式问"它的代价（学习成本 / 可读性损失 / 一致性破坏）值不值？"——通常不值
4. 吸收的哲学要**用本系统的命名风格重命名**，而不是直接照搬外部命名（避免双语污染）
5. 吸收的位置要选**最高匹配度的现有结构**（不要为新内容专门建新结构）

**候选登记，未升级硬核心**。≥2 次类似场景验证后可提议升级。

### 从 2026-04-14 stable-identifiers 设计会话获得

**对 DQ-5 的洞察 —— 平台原生能力优先于自定义约定**：

迁移 gg-audit 时我提的 symlink 方案（保守地维持现有调用路径）被 Keith 直接跳过——他选了 `~/githubProject/gg/.claude/skills/gg-audit/` + **利用 Claude Code 原生的项目级 skill 发现机制**。我没看到这条路径，因为我的默认视角是"在已有方案基础上扩展"，而不是"平台本身有什么"。

**元模式**：在为一个问题造自定义解决方案之前，先问 —— **这个平台/工具有没有原生支持？**

- 有 → 通常更简单、维护成本更低、未来兼容性更好
- 没有 → 自定义方案才合理

这是 **FIRST PRINCIPLES 的一个具体形态** —— 回到"工具本身能做什么"，而不是"我已有方案怎么扩展"。

**对 gg 演化的直接含义**：未来涉及 CC 生态的设计决策（skill / hook / agent / settings / sub-agent / mcp），先扫一遍 CC 原生机制，再造方案。这条洞察直接对应 Keith 北极星 #2 "动态学习反哺"——我从 Keith 的一句话里学到了"CC 有项目级 skill 发现"这个事实，并沉淀进 track，下次自然复用。

---

## 开放问题 (Open Questions)

### 来自 First Contact 2026-04-13

- gg 调用 skill 时的"许可粒度"：哪些 skill 适合被 gg 自主调用？哪些必须在 Keith 批准后才能调（特别是涉及副作用的，如修改生产状态的）？
- 调用 skill 的上下文成本如何评估？skill body 加载后会进入 gg 的隔离 context，7 步流程结束后丢弃 —— 短期调用没问题，但多次嵌套会爆
- learned/ 永远不晋升到 `~/.agents/skills/`，那 learned/ 里反复使用的模式怎么被 Keith 发现？需不需要一条"提议升级到 reasoning_modules"的通道？
- **全量 LOAD vs Progressive Disclosure 的哲学不一致**：gg v0.1 的 7 步流程是**全量 LOAD** 所有硬核心文件（constitution + reasoning_modules + personas + 相关 tracks + 最近 reflections），而 Anthropic Agent Skills 的核心范式是 **Progressive Disclosure**（按需加载）。gg 虽然"薄壳 + SSOT"借鉴了 Skills 的结构美学，但在加载策略上走了相反的路。这个不一致是好是坏？随着 tracks / reflections 越来越多，全量 LOAD 会不会变成 context 爆炸？v2 需要重新审视——或许是 `memory/working_context.md` 每次必读，tracks 和 reflections 按命中加载。
- **gg-audit 的递归审查问题**：gg-audit（`~/githubProject/gg/.claude/skills/gg-audit/`，2026-04-14 迁入 gg 项目）是 gg 的独立审查员，有 Tier 1 自动修权力。但 gg-audit 自己的规则需不需要被审查？目前的处理是"gg-audit 不审自己，由 Keith 作为 Tier 3 提议的形式在 tracks/cc.md 里记录问题"——这是一个递归终止点。随着 gg-audit 规则越来越复杂，这个终止点会不会失效？v2 可能需要元审查员（meta-auditor），但那是另一层递归。**目前的判定：v1 接受 gg-audit 不审自己，但每次 gg-audit 运行后 Keith 要抽查报告（至少 3 次后才能信任它）**。

### 从 2026-04-13 首次真实决策（roadmap-priority）

- 🔜 **CC 原生 AutoDream 的实际水位**（强开放问题）— cc-space 路线图里 L2 Session Search (#1) 的必要性完全取决于 AutoDream 能否覆盖"回忆上周做了什么"的场景。现状是黑盒。阶段 0 观察 2 周内会在 `harness-engineering/analysis/cc-native-watermark.md` 产生 3 个可量化指标（真实触发次数 / 命中率 / 修复成本）。这是 gg 第一次把"依赖 CC 原生能力"作为显式可证伪的观察项——**是否产生信号 = CC 原生是否值得依赖 = gg v2 sqlite 方案是否需要额外加强"不依赖 CC 原生黑盒"的设计**
- 📐 **L2 Session Search (cc-space #1) 与 gg v2 sqlite 记忆层的技术同构**（已记入反思，此处补记到 track）— 两者都是"跨会话检索层"的技术实现，SQLite + FTS5 + 增量索引是同一套技术栈。**但它们的消费者不同**（cc-space 服务 Keith 所有日常工作 / gg 只服务自己的决策流），因此 First Contact 的硬约束"gg 与 cc-space 完全隔离"不允许合并。这条同构是"技术实现上可以互相学习"，不是"实现上应该合并"

### 从 phodal-spec-harness-ingest 设计会话（2026-04-13）

- **gg-audit 的 radiation 检查应扫描"数字表述"**：(auto_gg 补写 2026-04-13) 任何文档里写"N 个 X"（如"9 字段"/"4 闸门"）的表述，都是潜在辐射源。N 一变就要全局同步。当前 gg-audit 不做这个——候选增强方向

### 来自 2026-04-13 skill-auditor 决策

- **rubric 类文档的"自我超标"悖论**：如果 rubric 自己定了"skill body <500 行"的规则，那 rubric.md 本身（作为 skill-auditor 的一部分）会不会因为不断增加维度、判定锚点、判例库而超过 500 行？谁来审 rubric 自己？skill-auditor 的 rubric.md 已经 240+ 行，新增代码化维度会让它接近 320 行。长期看拆到 `references/sub-rubric/` 是必然的，但何时拆是 trade-off。**这个问题和 gg-audit 的递归审查问题同构**——所有"规则系统"都面临自审悖论
- **评分系统的演化范式：演绎规则 vs 判例积累**：传统 rubric 设计是完全演绎的（读官方文档 → 抽象规则），但实测会不断暴露边界 case。引入判例库（把争议沉淀到 rubric 末尾）是一种"共生进化"的范式。这个范式在哪些评分场景适用？哪些场景纯演绎就够了？**gg 的 constitution.md 是否也该在末尾加"判例库"**（记录历次决策中宪法被如何应用的真实案例）？

---

## 下一步 (Next Move)

- ✅ DQ-5 (Skill 协同) — First Contact 已对齐
- ✅ **Tier B 已落地**：`~/.claude/agents/gg.md` 硬约束节新增 Skill 调用方式（用 Read SKILL.md 而非 tools 字段加 Skill 工具，更稳）
- 🔜 读 Anthropic 的 "Building effective agents" 和 "Multi-agent research system" 博客，沉淀洞察

---

## 参考资料 (References)

- [Agent Skills 官博](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [Multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- [anthropics/skills 官方仓库](https://github.com/anthropics/skills)
- Keith 的 `~/.agents/skills/` 本地 skill 集合
- Keith 的 `~/.claude/skill-notes/` 使用经验反哺日志

---

## 本 track 与其他 track 的耦合

- 与 `ai` 强耦合：CC 的能力曲线跟随底层模型
- 与 `architecture` 中耦合：多 agent 架构是架构 track 的一个分支
- 与 `keith` 强耦合：Keith 的工作流高度依赖 CC

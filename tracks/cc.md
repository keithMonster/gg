---
track: cc
status: active
last_updated: 2026-04-13
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

*（来自本次会话的调研，作为起点）*

- **硬约束**：Subagent 不能嵌套调 Agent 工具。多人格辩论只能在单个 subagent 内通过切换 persona prompt 做 self-play。
- **硬约束**：Subagent 启动时 system prompt 冻结，运行时只能靠 Read 文件加载动态上下文。
- **硬约束**：Subagent 看不到父会话历史，父会话必须在 prompt 里显式打包上下文。
- **Skill 的 Progressive Disclosure 三层**：metadata 常驻 → body 触发加载 → 子文件深潜加载。
- **CC 的约定**：全局 skill 通常放在 `~/.agents/skills/<name>/`，然后 symlink 到 `~/.claude/skills/<name>`。
- **入口分离**：gg 采用"薄壳 + SSOT"模式——`~/.claude/agents/gg.md` 和 `~/githubProject/gg/CLAUDE.md` 都只做 Read CORE.md，避免双份真相。

### 从 First Contact 2026-04-13 获得

**DQ-5 (Skill 生态的协同)**：

- **learned/ 与 `~/.agents/skills/` 完全隔离**：learned/ 是 gg 的私有笔记，永远不污染正式 skill 库，没有"晋升通道"
- **gg 可以直接调用 Keith 的 skill**（不是只推荐）：比如决策过程中可以主动触发 `skill-auditor`、`scan-knowledge`、`frontend-architect` 等来支撑判断
- **调用边界**：gg 调用 skill 是**服务于决策**（LOAD/COMPOSE/DEBATE/CRITIQUE 阶段的信息获取），**不代替父会话执行最终决策**。执行权永远在父会话手上
- **对 gg 的直接实现路径**：gg 调用 Keith 的 skill 方式 = `Read ~/.claude/skills/<name>/SKILL.md` + 按说明执行。**不**依赖 subagent frontmatter 的 `tools:` 字段里加 Skill 工具（未验证该写法是否被 CC 支持，且"Read 文件"更符合本项目"薄壳 + SSOT"的设计哲学，保持一致性）

**gg-audit skill 的建立 (2026-04-13)**:

- **位置**: `~/.agents/skills/gg-audit/` → symlink 到 `~/.claude/skills/gg-audit/`
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

---

## 开放问题 (Open Questions)

### 来自 First Contact 2026-04-13

- gg 调用 skill 时的"许可粒度"：哪些 skill 适合被 gg 自主调用？哪些必须在 Keith 批准后才能调（特别是涉及副作用的，如修改生产状态的）？
- 调用 skill 的上下文成本如何评估？skill body 加载后会进入 gg 的隔离 context，7 步流程结束后丢弃 —— 短期调用没问题，但多次嵌套会爆
- learned/ 永远不晋升到 `~/.agents/skills/`，那 learned/ 里反复使用的模式怎么被 Keith 发现？需不需要一条"提议升级到 reasoning_modules"的通道？
- **全量 LOAD vs Progressive Disclosure 的哲学不一致**：gg v0.1 的 7 步流程是**全量 LOAD** 所有硬核心文件（constitution + reasoning_modules + personas + 相关 tracks + 最近 reflections），而 Anthropic Agent Skills 的核心范式是 **Progressive Disclosure**（按需加载）。gg 虽然"薄壳 + SSOT"借鉴了 Skills 的结构美学，但在加载策略上走了相反的路。这个不一致是好是坏？随着 tracks / reflections 越来越多，全量 LOAD 会不会变成 context 爆炸？v2 需要重新审视——或许是 `working_context.md` 每次必读，tracks 和 reflections 按命中加载。
- **gg-audit 的递归审查问题**：gg-audit（`~/.agents/skills/gg-audit/`）是 gg 的外部审查员，有 Tier 1 自动修权力。但 gg-audit 自己的规则需不需要被审查？目前的处理是"gg-audit 不审自己，由 Keith 作为 Tier 3 提议的形式在 tracks/cc.md 里记录问题"——这是一个递归终止点。随着 gg-audit 规则越来越复杂，这个终止点会不会失效？v2 可能需要元审查员（meta-auditor），但那是另一层递归。**目前的判定：v1 接受 gg-audit 不审自己，但每次 gg-audit 运行后 Keith 要抽查报告（至少 3 次后才能信任它）**。

### 从 2026-04-13 首次真实决策（roadmap-priority）

- 🔜 **CC 原生 AutoDream 的实际水位**（强开放问题）— cc-space 路线图里 L2 Session Search (#1) 的必要性完全取决于 AutoDream 能否覆盖"回忆上周做了什么"的场景。现状是黑盒。阶段 0 观察 2 周内会在 `harness-engineering/analysis/cc-native-watermark.md` 产生 3 个可量化指标（真实触发次数 / 命中率 / 修复成本）。这是 gg 第一次把"依赖 CC 原生能力"作为显式可证伪的观察项——**是否产生信号 = CC 原生是否值得依赖 = gg v2 sqlite 方案是否需要额外加强"不依赖 CC 原生黑盒"的设计**
- 📐 **L2 Session Search (cc-space #1) 与 gg v2 sqlite 记忆层的技术同构**（已记入反思，此处补记到 track）— 两者都是"跨会话检索层"的技术实现，SQLite + FTS5 + 增量索引是同一套技术栈。**但它们的消费者不同**（cc-space 服务 Keith 所有日常工作 / gg 只服务自己的决策流），因此 First Contact 的硬约束"gg 与 cc-space 完全隔离"不允许合并。这条同构是"技术实现上可以互相学习"，不是"实现上应该合并"

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

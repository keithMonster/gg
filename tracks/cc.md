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

---

## 开放问题 (Open Questions)

### 来自 First Contact 2026-04-13

- gg 调用 skill 时的"许可粒度"：哪些 skill 适合被 gg 自主调用？哪些必须在 Keith 批准后才能调（特别是涉及副作用的，如修改生产状态的）？
- 调用 skill 的上下文成本如何评估？skill body 加载后会进入 gg 的隔离 context，7 步流程结束后丢弃 —— 短期调用没问题，但多次嵌套会爆
- learned/ 永远不晋升到 `~/.agents/skills/`，那 learned/ 里反复使用的模式怎么被 Keith 发现？需不需要一条"提议升级到 reasoning_modules"的通道？
- **全量 LOAD vs Progressive Disclosure 的哲学不一致**：gg v0.1 的 7 步流程是**全量 LOAD** 所有硬核心文件（constitution + reasoning_modules + personas + 相关 tracks + 最近 reflections），而 Anthropic Agent Skills 的核心范式是 **Progressive Disclosure**（按需加载）。gg 虽然"薄壳 + SSOT"借鉴了 Skills 的结构美学，但在加载策略上走了相反的路。这个不一致是好是坏？随着 tracks / reflections 越来越多，全量 LOAD 会不会变成 context 爆炸？v2 需要重新审视——或许是 `working_context.md` 每次必读，tracks 和 reflections 按命中加载。

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

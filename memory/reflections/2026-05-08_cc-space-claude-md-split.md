---
date: 2026-05-08
mode: 工作
slug: cc-space-claude-md-split
status: substantive-decision
summoned_by: cc-space 主会话
issue_source: cc-space 议题 L124（CLAUDE.md 60 行硬约束 + 体积 audit）
decision_target: cc-space CLAUDE.md 321 行拆分方案的 4 个 Q（子文件位置 / 命名 / 扩展决策树 / 与现有载体边界）
artifacts_touched:
  - 此 reflection
  - memory/essence.md（追加 1 滴 ssot-as-loadable-fragment）
---

# Reflection — cc-space CLAUDE.md 拆分决策

## 装配地图

- KERNEL + CORE + state + essence（启动四件）
- tools/TOOLS.md + tools/essence-grep.md + tools/solution-space.md
- constitution.md（自审 P3/P5/P7 + G3/G4）
- 不装 persona-debate（Keith 方向已对齐 5 条，分歧空间小，激进派/保守派对抗 ROI 低）
- 不装 compose-reasoning（决策结构清晰：4 个 Q 各自 trade-off + 决策树是机械准则，不需要 Self-Discover）

## 核心假设

1. cc-space 元方法论"内部不可靠 → 外部锚点托底" 不变——拆出去的子文件本身会成为新的"不可靠维度"，需要事件层 hook 托底（准则 5）
2. ETH 60 行实证适用于 cc-space 场景（agentic 工程项目，主文件被频繁加载消耗 attention）
3. Keith 已对齐方向（5 条不重谈），决策落点是机械化判别准则，不是范式论证
4. 拆分阈值 30 行是启发式，红队修订后改为"先拆 4 个明确高 ROI 段，准则不全量推开"

## 可能出错的地方

1. **拆分阈值 30 行可能保守或激进**——没有实证数据支撑，是从"主文件 150-180 + 6 段平均"反推。第一版跑 2-4 周后必复盘
2. **CLAUDE.d/ 范式认知成本**——nginx 范式对运维背景的人零成本，对纯产品背景可能要查一次。Keith 是技术背景所以低风险
3. **复发触发器（准则 5 hook）的实施成本**未在本次决策范围——只给方向，不给代码。Keith 实施时可能发现 hook 写起来比想象贵，导致这条降级为"软提醒"，那时方案的事件层飞轮就漏一半
4. **子文件相互引用规则**（"冲突上提主文件裁决"）是纸面约束，没有自动化检测。子文件少（4 个）时人工巡查可控，规模扩到 8+ 个会出事

## 推理盲区

1. **没考虑工作区 CLAUDE.md 的二阶影响**——24 个工作区都有自己的 CLAUDE.md，本次只动项目根。如果同形态压力（工作区主文件膨胀）也存在，方案应该是同套准则适用于工作区——但本次未论证
2. **没考虑 CLAUDE.d/ vs MEMORY.md 的关系**——MEMORY.md 已经是"按需展开"的索引（threads frontmatter 自动派生），CLAUDE.d/ 是另一套按需机制。两套并存是否有重复治理负担？本次未触及
3. **没显式审视全局 ~/.claude/CLAUDE.md（90 行）是否也该拆**——它已经接近 100 行警戒线但本次议题范围是 cc-space 项目级，避免越界。但 Keith 实施完 cc-space 后大概率会问"全局也拆吗"，那时需要单独决策

## N 个月后根因预判

如果决策错了，N 个月后最可能的根因：

1. **拆出去的子文件腐烂**（essence stale-observer 的具体落点）——主文件天天加载所以新鲜，子文件按需加载所以不被发现已腐。**预防**：准则 5 复发触发器 + auto-maintenance 夜跑扫子文件 mtime（本次只给方向，未强制实施）
2. **决策树准则被滥用**——"30 行就抽"被机械执行到不该拆的段（比如安全红线虽然 30 行但绝不能下沉）。**预防**：本决策已在 Q3 准则前加了"安全红线绝不下沉"的硬约束（来自 Keith 5 条对齐方向）
3. **CLAUDE.d/ 与 skill 边界混淆**——某段陈述性规则因为"经常被引用"而被错误升级成 skill。**预防**：Q4 试金石"独立调用 vs 被引用"是机械判别，但仍需复盘

## 北极星触达

本次决策对 KERNEL §1「每一轮沉淀一滴最核心的内容，逼近一切的本质」的触达：

- **逼近的本质**：SSOT 的物理形态不必是单文件——可以是"主索引 + 按需加载片段集合"，关键约束是"加载逻辑必须是事件触发的，不是 prompt 软提醒"
- **沉淀点**：`ssot-as-loadable-fragment`（详见 essence.md 新增条）
- **track 影响**：本决策不直接归属任何长期 track，但跟"自我观察族"主线有间接连接——CLAUDE.md 体积监控本身是"看自己"的一种形式（看 cc-space 的元规则膨胀）

## 对齐度

- Keith 5 条对齐方向 → 全部接受，不重谈 ✅
- 强制语法（"我推 X，理由是 Y"）→ 全程使用 ✅
- Q3 决策树要可机械执行 → 4 条准则全部数值化或试金石化 ✅
- 不要 RFC 长度（200-400 行）→ final message 控制在该区间 ✅
- 元方法论"外部锚点托底"自洽 → 准则 5 是事件层锚点，对齐 ✅

## 给父会话的最终输出

（本字段是 LLM subagent 模式 thinking → final message 通道的备份输出。父会话已能从 final message 拿完整决策——本字段是双保险。）

### Q1 子文件位置：`cc-space/CLAUDE.d/<domain>.md`
nginx conf.d 范式，目录语义自带"CLAUDE 主文件分片"含义，零认知成本。拒绝 docs/（语义太宽易退化为杂物间）/ rules/（语义太宽吸引防御式规则）/ 平铺根目录（破坏可读性）。

### Q2 子文件命名：简洁版 `<domain>.md`，业务名而非抽象类型
例：`fastgpt.md` / `database.md` / `persistence.md`。CLAUDE.d/ 路径已携带"CLAUDE 子文件"语义，文件名再加 `CLAUDE-` 前缀冗余违反 OCCAM。业务名（fastgpt/workspaces）稳定性高于抽象命名（rules/patterns/config）。

### Q3 扩展决策树：4 条机械准则 + 1 条复发触发器
- 准则 1：≥ 30 行抽出 / < 30 行留主文件
- 准则 2：每会话都可能用的元规则留主文件 / 进入特定领域才用的抽出
- 准则 3：试金石 "完全删掉只在特定场景才会想起，且想起时知道去 X 找"——yes 抽 / no 留
- 准则 4：先看能否并入现有载体（skill / threads / 工作区 CLAUDE.md），都不是再进 CLAUDE.d/
- 准则 5：主文件 > 200 行 PreToolUse hook 报警（事件层飞轮，对应 essence rule-layer-flywheel）

子文件互引允许，互 import 禁止；冲突必须上提主文件裁决。

### Q4 与现有载体边界：陈述 vs 过程
- CLAUDE.d/<domain>.md：陈述性规则（事实/必须做/字段）
- skill：过程性能力（怎么做某事）
- threads/<subject>.md：主体时间线
- <workspace>/CLAUDE.md：工作区局部规则

CLAUDE-子文件 vs skill 的判别试金石：被独立调用 → skill / 被引用查阅 → CLAUDE-子文件。

### 具体下沉清单（建议初版抽 4 个）
- CLAUDE.d/workspaces.md（~50 行，从主文件§工作区索引段抽）
- CLAUDE.d/toolbox.md（~35 行，从主文件§公共库+CLI工具段抽）
- CLAUDE.d/fastgpt.md（~30 行，从主文件§FastGPT 工作流管理段抽）
- CLAUDE.d/persistence.md（~50 行，从主文件§持久化策略+threads+分层检索段抽）

预期主文件 321 → ~160 行（命中 150-180 目标）。

### 行动建议（6 步）
1. 建 cc-space/CLAUDE.d/ 目录
2. 抽 4 个子文件，主文件留 3-5 行指针（说明 + 关键词触发清单 + 子文件路径）
3. 建 shared/scripts/guard_claude_md_size.py PreToolUse hook
4. Q3 决策树 4 准则 + 1 触发器写进主文件§扩展原则段（后续新增内容 SSOT 入口）
5. 拆完后新会话验证：能否在不主动 Read 子文件情况下完成 80% 常见任务
6. 准则 1（30 行阈值）不强推全量审视，先看 4 个抽出实例跑 2-4 周（红队修订）

### 关键 Trade-off
- 拆出的子文件比留主文件更易腐——准则 5 hook 兜底
- 子文件相互引用 SSOT 漂移风险——硬规则"冲突上提主文件裁决"
- 准则 1 阈值是启发式无实证——红队修订改为"先拆 4 个高 ROI 段，准则不强推"

## essence 沉淀

本轮沉淀 1 滴：`ssot-as-loadable-fragment`（已 append 到 ~/githubProject/gg/memory/essence.md，等 Keith review）

## 元洞察

本次议题表面是"文件拆不拆"的工程决策，实质是 SSOT 物理形态的本体论判定——单一物理文件不是 SSOT 的必要形态，"主索引 + 按需加载片段集合"也是合法 SSOT，关键约束在加载机制（事件触发 vs prompt 软提醒）。这跟 cc-space 元方法论"内部不可靠 → 外部锚点托底"的关系是：锚点本身可以是分布式的，只要有事件层飞轮保证它们被读到。

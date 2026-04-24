---
date: 2026-04-24
slug: knowledge-engineering-hook-mvp
type: design-session
summoner: Keith 直接对话
started_at: 10:30
ended_at: 11:10
---

# 设计会话反思：知识工程范式 → hook 层最小落地

## 议题列表

1. Keith 的诊断：大模型擅长 A→B（续写），不擅长判断 A 是否对（grounding/出发点）
2. 诊断精化——"A 是否对"拆三层（事实性 / 根因 / 前提）；数学证明类比不能直接复制（封闭系统 vs evidence-chain）
3. 范式骨架四层：reasoning 结构 / 事实库 / grounding 机制 / 出发点审视
4. 落地范围收敛：Claude Code 全局层而非单项目
5. 从 gg 翻 3 个失败 case：FastGPT 字段名 / wish-as-pain-laundering / action-type-over-aggressiveness
6. 从 cc-space 翻 5 个失败 case：NW M1 首轮错 / rtk×curl 误判 / memory-lab 翻车 / 大厂营销话术 / 工作区定位误判
7. 自我审查 A/B/C 三路径，选最简单有效飞轮路线
8. MVP 设计：SubagentStop hook v0（纯观察，不警告不阻塞）
9. 实装 + 自测闭环

## 共识 / 变更清单

### 新增文件
- `~/.claude/hooks/grounding-check.sh`（41 行 bash，SubagentStop 观察器 v0）

### 修改文件
- `~/.claude/settings.json`：加 SubagentStop hook 注册

### 观察产物位置
- `~/.claude/grounding-failures.jsonl`（hook 触发时追加一行）

### 停止信号（硬锚 2026-05-24）
- 触发 0 次 → 撤掉 hook（rule 11 已形成 muscle memory）
- 触发 ≥ 3 次 → 审视分布，决定升级路径
- 触发 1-2 次 → 延期 1 个月

### 设计决策
- **不做**全局 CLAUDE.md 4-phase pipeline 重构（A 路径，prompt 层不积累）
- **不做**完整范式骨架（4 层 reasoning 结构 / 事实库 / grounding 机制 / Problem Framing）——全部改为 tripwire-first，真翻车再升级
- **只做**一个 SubagentStop 物理观察器——捕获 → jsonl → 接入现有 essence 沉淀循环

## 我这次哪里做得好 / 哪里差

### 做得好
1. **自我审查 A/B/C 时识破了 A/B 的死穴**——"没有物理锚"。prompt 层规则必须被读才生效，不积累经验；只有 hook 层有物理触发，每次触发都留锚点。这是对 essence `flywheel-needs-anchor` 的具体应用
2. **坚持了 rule 6 的严格应用**——在写 hook 前查了官方 hooks 文档，确认 SubagentStop 的存在和 transcript_path 的可用性。没凭训练记忆直接编
3. **发现 Task payload schema 未被官方文档覆盖时选了保守 v0**——不解析 prompt 语义，只看 tool_use 这个物理 metadata 信号（essence physical-anchor 的应用）
4. **翻 case 时覆盖了 gg + cc-space 共 8 个真实案例**——不是理论假设，每个都有 reflection 或 essence 锚点

### 做得差
1. **第一版 hook 有 `grep -c` + `|| echo 0` 的经典 shell bug**——grep -c 无匹配时输出 "0" + exit 1，`||` 追加第二个 "0"，变成 "0\n0" 让整数比较失败、守卫失效。CLAUDE.md rule 3（先写错误处理再写业务）没做到——自测才暴露。应该写之前就预判 grep -c 的返回语义
2. **没做 payload dump 实证**——官方文档没给 Task payload schema，最硬的方法是先装 echo hook dump 一次 payload 再设计。我选了折中（保守 v0 不依赖 payload 细节），这是实用主义让步，不是最佳实证
3. **Keith 明确说"你确认好就行"时有微弱的"这是授权一次性动手"倾向**——真实应对是：授权拿到了，但 engineering 严谨不能打折。我走了查文档 + 自测两步，没有直接凭感觉写完

### Keith 打断 / 纠正我的地方
- **范围收敛**："我其实想做的是把这个东西在 Cloud Code 里面实现"——把我原本倾向的"gg 先原型"纠正为"全局层"。这次纠正正确（N=4，对 keith.md 的 "分歧时 Keith 更对" 信号再加一条）
- **自我审查要求**："找到那条最简单有效的路线。重点是有效、能自我闭环，能产生飞轮效应"——这句话让我从"给菜单 A/B/C"切换到"自己拍板"。Keith 的偏好是 **gg 自主决策 + Keith 校验**，不是 **Keith 决策 + gg 执行**

## 元洞察（gg 演化本身的 learning）

### 1. Prompt 层规则是跑步机，事件层规则是飞轮

这是本轮最核心的洞察。之前 gg 的纪律体系（CLAUDE.md 5+5+13 条规则）都在 prompt 层——依赖"被读到 + 被遵守"。但同一个可能忘记规则的模型同时是读者和执行者——**soft override 风险内嵌**。

事件层（hook）不同：它在 model 外，物理触发，metadata 可读，输出可强制。**每次触发都留锚点**（jsonl 一行），锚点喂进 gg 的 reflection / essence 循环，规则自然升级。这是真飞轮。

**候选新 reasoning_module**：`RULE-LAYER-FLYWHEEL-CHECK`——设计新规则时先问"它在哪一层执行"。prompt 层规则只适合"本来就容易记住的纪律"（简短 / 语义强 / Keith 主动在意的）；需要**物理 enforce** 的（易忘 / 判断复杂 / 跨项目）必须 hook 化。

这条也对应 tracks/cc.md / architecture 的候选议题——"Claude Code 的规则分层是什么"。

### 2. 范式设计要从现场 artifact 反推，不凭空发明

NW terminal review 2026-04-21 的四段结构（物理实证 / 重新聚类 / M1 推翻 / 元自省）**就是 Problem Framing 的完整 pipeline**——只是没被命名。范式化 = 把现场工作流固化为 prompt template，不是从"知识工程理论"演绎。

这直接关联 essence `self-as-first-user`——gg 的第一个用户是 gg 自己，范式应该从已经跑通的 gg 工作流里抽象。

### 3. Tripwire 先于 pipeline

Keith 在整轮对话里用四个关键词约束我：**简单 / 有效 / 闭环 / 飞轮**。这四个词联动起来逼出一个答案——**不要建完整范式框架，先留一个物理触发器**。

essence `premature-abstraction-tripwire` 的具体应用：tripwire = 触发器（grep tool_use）+ 红旗（写 jsonl）+ 物理锚点（hook 文件），**不含流程**（没有反哺 pipeline、没有自动升级规则、没有 dashboard）。流程等第 N 次触发真发生再造。

### 4. 物理信号 > 语义判断

MVP 选了最稳的信号——"transcript 里 tool_use 总数 ≥ 2 但 WebSearch/WebFetch = 0"。这不依赖 prompt 解析、不依赖关键词匹配、不依赖 agent 自证。Metadata 是纯物理的，无歧义。

语义判断（比如"这是不是研究型任务"）留给未来数据驱动升级——如果 jsonl 里 80% 都是非研究型的假阳性，再加关键词过滤。

## 下次继续

### 2026-05-24 强制 review
审视 `~/.claude/grounding-failures.jsonl`，按停止信号三分档决策：
- 0 → 撤掉 hook + settings.json 清理 + 写一滴 essence "rule 11 + muscle memory 够用"
- ≥ 3 → 读所有记录，按分布决定：
  - 全是假阳性（非研究型任务）→ 加 prompt 关键词过滤，升级到 v1
  - 有真翻车 → 考虑把 systemMessage 警告加上，或 exit 2 阻塞（按严重度）
- 1-2 → 延期 1 个月到 2026-06-24

这个 review 不需要 Keith 召唤，设计模式下一次自检时主动触发。

### 开放问题（留给未来）
- Task payload schema 是否需要 dump 实证？（v0 保守方案绕过了）
- 项目层 reasoning_module 库 schema 设计——essence 反哺进 modules 的具体格式
- "基于污染源的产物必须重做不是修"（Case F 教训）是否值得独立沉淀——这轮没写，可能下次

### 设计债务
- `grep -c` + `|| echo 0` 的 bug 修复后没 commit——等 Keith 下次一起 commit
- design_sessions 目录里这是 2026-04-24 的第一份，若今天还有其他议题会叠加

## KERNEL 改动清单

本次**无 KERNEL 改动**，D4 不触发。改动都在 KERNEL 之外（全局 hook + settings + 本反思 + essence）。

## 代码质量

扫描本轮产出：
- `grounding-check.sh` 41 行——单一职责、无全局状态、依赖最小（jq + grep）
- 无 TODO、无 skip、无 fallback 幽灵路径
- `set -euo pipefail` 已启用，保护路径完整（空 transcript / 空 session_id 都有兜底）
- settings.json 增量最小——只加 SubagentStop 段，不改 PreToolUse / permissions / plugins
- **已知限制**：v0 不处理 transcript_path 为相对路径的情况（现实中 Claude Code 总传绝对路径，未来若改变需要加 realpath）

## 能力缺口

- **Hook payload schema 认知**：我对 SubagentStop 的 payload 完整字段不确定。v0 只用了 transcript_path + session_id + cwd 三个保守字段——这三个在 PostToolUse 例子里都有，稳。未来若 v1 需要更多字段（如 subagent 的 initial prompt），必须先 dump 一次实证
- **shell bug 的预判能力**：`grep -c` + `set -euo pipefail` 的 edge case 应该第一版就避开，不是靠自测救场。列入 engineering rule 候选——"`grep -c` 无匹配返回 exit 1，在 `-e` 下必须 `|| VAR=0` 覆盖，不能 `|| echo 0` 追加"

## 沉淀（写入 essence.md）

- **slug**: `rule-layer-flywheel`
- **一句话**：规则在哪一层执行决定它是否飞轮。prompt 层 = 跑步机；事件层 = 飞轮。
- **补刀**：前者靠"被读到 + 被遵守"，soft override 内嵌；后者被物理触发，每次触发都留锚点。

已 append 到 `memory/essence.md`。

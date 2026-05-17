---
date: 2026-05-14
slug: prompt-engineering-foundations-boundary
summoner: cc-space
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: cc-space 提示词工程基础抽取的边界拍板

### 给父会话的最终输出（必填）

**推荐**：

1. **粒度边界**：抽到"结构片段 + Why"层就停（合格 anchor：`❌` + 事故案例 + 日期 + 翻车细节，12 处实例佐证）；再升一层（"否定先于肯定"/"负面注意力工程"）= 过度抽象，进入 promptingguide.ai 通用学术语言。判别试金石：**这条范式去掉 cc-space 实例是否还成立**——还成立 = 太抽象（在造通用 best practice）；不成立 = 粒度合格。

2. **假设处置**：从 7 砍到 4 + 1 子机制。**H1+H4 合并**（强制语法是反例锚定的句子级落地，同根） / **H2 保留**（Decision Authority 强证据） / **H3 降级**为 H1/H2 的子机制（自唤起 = 如何被读到） / **H5 剔除**（单一锚点，样本不足，且容易跑偏 LLM long-context 通用理论） / **H6 保留**（多源佐证） / **H7 提升为顶层元假设**（H1-H6 都是它的派生）。收敛动机：让 LLM 验证 7 条会找到 7 条证据（task-compliance-is-not-truth），4 条更难掺水。

3. **产出形态**：推荐 **(c) reject** + 一行 reject 理由进 inbox/closed，**backup (b)** CLAUDE.md 补 1-2 条工程原则。理由：cc-space 提示词决策已**事实上一致**，brief 的 H1-H7 实例佐证已经够多——"已经一致 ≠ 没显式化是问题"。(a) thread 综述是 prompt 层（跑步机，无事件层飞轮，rule-layer-flywheel）；(d) 派生新议题应在调研后，不在塑形阶段预设。

**trade-off**：

- (c) reject 看似浪费——但抽取动作本身的元自指 = 抽取 cc-space 提示词范式的方法论就是 cc-space 提示词工程的实例，源作者赞许 ≠ 抽取成功（borrowed-method-as-mini-source）。"已隐式做到位"必须是合法终态，否则 reject 选项就是假的。
- (b) backup 触发条件：调研真发现新事故对应的范式缺口（不是已有范式再描述）。
- 未核验假设：brief 没列"因提示词决策范式不一致导致的事故案例"。**调研启动前先做 1 小时预扫**——grep cc-space 历史 thread / inbox/closed，找 ≥3 例真事故 → (b)；0-2 例 → (c) reject。

**行动建议**：

1. Keith 拍板是否接受 4 条收敛后假设清单（H7 顶层 + H1+H4 / H2 / H6 + H3 子机制）
2. 启动 1 小时预扫（不是 brief §3 的 60 文件 grep，是历史事故 grep）
3. 预扫结果决定 (b) vs (c)，**禁止跳过预扫直接进 brief §3 的全量调研**——会跑成 task-compliance-is-not-truth 的产出，cc-space 自己看了会说"对，差不多"——抽取失败信号

### 核心假设

1. cc-space 提示词决策已**事实上一致**（brief 的 H1-H7 实例佐证就是证据，连 brief 起草人都能列出 7 条范式）
2. 抽取 cc-space 提示词范式的方法论本身就是 cc-space 提示词工程的实例（元自指——这条决定了 reject 必须是合法终态）
3. "源作者会说差不多就这意思"是抽取失败信号，不是抽取成功信号
4. 没有事故牵引的范式综述 thread = prompt 层（跑步机），不会被消费

### 可能出错的地方

- 假设 1 可能假阳性——cc-space 提示词决策可能并不一致，只是 brief 起草人能 cherry-pick 出 7 条假设；要靠预扫的事故记录证伪
- 把 H5 剔除可能漏掉真信号——元方法论位置确实只有一处锚点，但这条恰好可能是 cc-space 区别于通用 best practice 的关键。剔除是"宁可漏不可造词"的保守选择
- 推荐 (c) reject 可能让 Keith 觉得"gg 太消极"——但 backup (b) 已经留了出口；如果预扫真有事故，(b) 自动激活
- 4 条收敛后假设可能仍然不够窄——验证时如果发现 4 条都"恰好通过"，应再次怀疑是 task-compliance

### 本次哪里思考得不够

- 没去预扫 cc-space 历史 thread / inbox/closed 看真事故数据——这步本应是我做的；但 gg 工作模式边界是"拍边界不出产出"，所以把预扫挂回给父会话执行。如果预扫数据强烈反转结论（≥5 例真事故），4 条假设可能要重新展开
- H7（反通用 best practice）提升为顶层元假设的判断有些快——只跑了一遍"它是元方法论的具体落地"逻辑，没充分对照其他 6 条假设是否真是它的派生
- 产出形态推荐 (c)/(b) 的判别阈值（≥3 例 vs 0-2 例）是 sense-driven，没数据支撑——按 idle-threshold-as-tripwire-not-answer 的范式应该写"先猜 3 例，N 周后调"

### 如果 N 个月后证明决策错了，最可能的根因

1. **最可能根因（45%）**：cc-space 提示词决策事实上不一致，brief 的 H1-H7 是 cherry-pick 后的样子货；真实情况是 skill 之间 / CLAUDE.md 之间 / hook 之间风格混乱，事故隐性发生但没被记录。这种情况下 reject 等于错过真问题。**反证机制**：1 小时预扫如果找到 ≥3 例真事故 → 自动激活 (b)，反证生效
2. **次可能根因（30%）**：4 条收敛后假设仍是过度抽象——H7 提升为元假设的判断不够审慎，应该全剔除假设清单只跑 5W 问题。这种情况下产出会变成"4 条假设的实例佐证 = 任务顺从"
3. **第三可能（15%）**：粒度边界没拍稳——"结构片段 + Why"层这个 anchor 在实操中会被反复争议（什么叫结构片段？怎么界定 Why 的边界？），需要更具体的判别准则
4. **第四可能（10%）**：(c) reject 是对的但 Keith 本意是探索驱动（不算 ROI），按 explore 节奏走 = (a) thread 综述也合法。这种情况下 reject 是过度防御——但 brief §0 没声明 explore 上下文，按工程原则补充走是默认

### 北极星触达

**#1 二阶效应**——本次决策的二阶效应是**对未来"显式化 cc-space 已有决策"类议题的范式贡献**：从这个议题开始建立"显式化前先问'有事故牵引吗' + 抽取动作元自指审视"的判别习惯，避免 cc-space 退化成 borrowed-method-as-mini-source 的迷你 promptingguide.ai。这条触达的是范式层，不是当下 brief。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  1. `extraction-meta-inheritance` (2026-04-29) + `borrowed-method-as-mini-source` (2026-05-08)——抽取动作反向继承被抽取对象的元约束，本议题是这条 essence 的直接应用场景（cc-space 提示词工程抽取 = 在自己项目里造 promptingguide.ai 的迷你版风险）
  2. `task-compliance-is-not-truth` (2026-04-16)——H1-H7 假设清单让 LLM 验证 7 条会找到 7 条证据，砍到 4 条是这条 essence 的具体防御
  3. `survey-as-coordinate` (2026-04-23)——"已做，差名字"的判定，推荐 (c) reject 的核心依据
  4. `paradigm-not-feature-completeness` (2026-05-14 今日)——抽取动作的范式错位风险（功能覆盖率 100% 也不稳定，cc-space 提示词工程综述大概率落入这个陷阱）
  5. `rule-layer-flywheel` (2026-04-24)——(a) thread 综述是 prompt 层（跑步机）的判断依据，(b) CLAUDE.md 工程原则是事件层（SessionStart 加载）
  6. `idle-threshold-as-tripwire-not-answer` (2026-05-14 今日)——≥3 例事故的判别阈值是 tripwire 范式（先猜一个、N 周后调），不是预设最优值
  7. `premature-abstraction-tripwire` (2026-04-21)——抽到"结构片段"层就停，更高抽象按 tripwire 等真痛点触发

- **本决策是否在某条 essence 上反着走**：无明显反着走。唯一需要警惕的是 `essence-recursive-bootstrap` (2026-04-23)——essence 是主动决定下一步架构的种子；本决策大量引用 essence，可能是过度依赖既有结晶而不是新洞察。但本议题本质是"已有 essence 的具体应用场景"而不是"长出新 essence 的场景"，所以依赖既有 essence 是合理而非懒惰

- **cross-check 用的关键词**：grep "extraction" / "borrowed" / "task-compliance" / "survey-as-coordinate" / "paradigm-not-feature" / "rule-layer-flywheel" / "tripwire" / "premature-abstraction" 在 essence.md——全部物理命中

### essence 候选（可选）

- slug: explicit-articulation-needs-incident-evidence
- 一句话：显式化"已隐式做到位"的决策必须有事故牵引（≥N 例 tripwire），无事故牵引的显式化 = borrowed-method-as-mini-source 的范式生成器
- 是否已 append 到 essence.md: N（待 Keith 拍板是否值得沉淀——这滴跟 borrowed-method-as-mini-source 同源，是它在"显式化已有决策"场景的具体应用，可能仍不够"去 gg 化"重量，倾向不沉淀）

### 外部锚点（可选）

- `~/githubProject/cc-space/inbox/briefs/prompt-engineering-foundations.md` ← brief 底稿
- `~/githubProject/cc-space/threads/concepts-glossary.md` ← 同主线（cc-space 自创方法论术语的显式化已有先例，可对照其事故牵引 vs 范式声明的平衡）

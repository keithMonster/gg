---
date: 2026-05-06
slug: cgboiler-fact-type-ontology
summoner: cc-space (cgboiler 架构会话)
northstar_reach: n/a 非北极星触发——本议题是工程方案审查，不直接涉及 gg 三条北极星
status: substantive-decision
---

# Reflection: cgboiler L1 facts 加 fact_type 区分 episodic vs state_assertion

### 给父会话的最终输出（必填）

## 推荐：**当前阶段不实施**，等议题 12 王亮灰度跑通后再判断

三层判断（按重要性递减）：

**1. 本体论区分 episodic / state_assertion 形式上成立——但概念边界比"两类"更模糊**，至少存在三类隐藏 case：
- **关系断言**："X 与 Y 协作"——既像 state（可被取代）又像 episodic（关系建立时刻）
- **事件蕴含状态**："王亮 2025-09-15 提出 24618 方针" 是 episodic（提出动作发生在 T）但**蕴含 state**（24618 方针自此存在）；如果后续有 episodic "废弃方针"，两条都要永留主卡 + L2 消解"当前生效与否"
- **评估断言**（最大盲区）："王亮认为环保业务节奏偏慢" 既不是事件也不是状态，是 perspective owner 的看法。当前 SCHEMA §3 反例规则把这类边缘化（"张吉峰对此表达担忧" 是反例）——但**评估在 perspective first-class 系统里是核心信号**，不该全砍。本次方案没覆盖

**2. 方案三处修改设计是干净的，但有三个隐藏问题必须显式应对**：

- **历史数据兼容陷阱**：库里已有 1900+ facts 全部没 `fact_type` 字段，"默认 state_assertion" 听起来安全但**让历史 episodic 在 fold 时仍被错杀**——王亮 2025-09 提出 24618 默认 state_assertion → 时间归档 → 主卡 L2 引不到。**正确路径推荐选项 c：fold 触发时按 entity 局部补标**（只补议题 12 灰度的王亮 244 条，不补全库 1900 条）
- **LLM 抽取漂移**：fact_type 由 LLM 输出，会按语感分而不是按本体论分。容易混淆：「项目 1200008 处于水压试验阶段」/「王亮要求 AI BP 团队 3 月底前组建」/「环保部新人到位慢」三类全是 ambiguous case。**extract_prompt 必须给清晰试金石**："写成 <who> 在 <when> <做了/说了 X> 通过 = episodic；写成 <entity> 当前是 X 通过 = state_assertion；都通不过 = 评估，照原 §3 不抽"
- **演进路径缺失**：episodic 永留主卡 = 跑 5 年后王亮主卡又会膨胀。需要 `importance: keystone | routine` 二级分流的演进位，否则几年后又一次"漂移成大问题"

**3. 时机判定（最强结论）：当前阶段不该做。等议题 12 王亮灰度跑通后再判断。**

三个时机理由：
- **议题 12 fold v2 灰度还没真跑过**——render_cards.py `--fold` 实施代码还没写。本方案要在「**还没验证的 fold v2**」上叠一层「**还没验证的 fact_type 区分**」= 同时改两层未验证机制 = 失败原因不可分离
- **议题 14 C 阶段也卡在等议题 12**，C 阶段实施时改的就是 SCHEMA + extract_prompt + render_cards——跟本方案改的同一组文件。集中变更比连续散变更工程债低
- **违反 cgboiler 自己 PRINCIPLES §3 反模式表第六行**："一次性建好，定期重跑而非增量"——加 fact_type 字段属于"在已经跑了 7 batch、1900 facts 的库上做 schema 演进"，正是该原则反对的形态

**关键反转**：父会话用「fold 切割语义错位」作为核心理由——"王亮 2018 创业方针被归档"。**但这是 hypothetical**：fold v2 没跑，是不是真会发生这个错位**没数据**。可能 fold 后老 episodic 通过 timeline + L2 cite 跨文件穿透仍可触达，根本不需要本方案。**在数据点出来之前做 = 用对 fold 错位的理论预判覆盖灰度数据采集机会**——这是 essence `task-compliance-is-not-truth` 的另一种形态：让 LLM 在没数据情况下"识别理论缺口"，它会找到一个，但**这个缺口可能是它生造的**。

### 理由（推理路径）

- 装载 essence: `2026-05-01 / new-source-as-ontology-not-feature`（试金石：替换 PRINCIPLES §1 一句话能否描述新源——episodic vs state_assertion 答案是"能描述"，所以是字段不是新本体论层，方案级别正确但不优先）
- 装载 essence: `2026-04-21 / premature-abstraction-tripwire`（过早抽象的对症解是 tripwire，不是抽/不抽二分。本议题正应用：tripwire = 议题 12 灰度结果，触发器 = "≥3 重要 episodic 失踪"，不是现在拍 schema）
- 装载 essence: `2026-05-02 / terminus-walk-needs-terminus-visibility`（fact_type 是终态可预判对象——但议题 12 fold 行为是终态模糊对象，强行用清晰对象的确定性伪造模糊对象的确定性。正确做法：分别处理）
- 装载 essence: `2026-04-16 / task-compliance-is-not-truth`（让 LLM 找洞它就找到，理论缺口可能是 sycophancy 的另一种形态——证伪需要数据，不是更深的理论分析）
- 物理实证：通过 Read SCHEMA / PRINCIPLES / FOLD_DESIGN / extract_prompt / PENDING_DECISIONS / STAGE3_STATE 核实——议题 12 仅 §9 设计稿，render_cards.py `--fold` 未实施；议题 14 C 阶段已 ⏸；王亮 244 facts 是 batch1-007 后实测；议题 13 SCHEMA §4 字符上限漂移已登记工程债等议题 12 跑通

### trade-off

- **拍"暂不实施"代价**：父会话识别的理论缺口被推迟处理；如果议题 12 跑完证实确实有 episodic 失踪问题，多一轮决策周期
- **未核验假设 1**：议题 12 fold 跑完真的会暴露 episodic 失踪问题（可能也不会——timeline 锚点 + L2 跨文件 cite 可能足够兜底）
- **未核验假设 2**：fact_type 即使做了，LLM 抽取的实际准确率可能不及预期，反成新漂移源（试金石规则能不能压住漂移没有测过）
- **未核验假设 3**：cgboiler 的"评估断言"层是不是真的是核心信号——如果不是，本议题"两类切分够不够"的扩展就不成立

### 行动建议（父会话下一步）

1. **不动 SCHEMA / FOLD_DESIGN / extract_prompt**——本议题进 PENDING_DECISIONS 作为新议题（建议编号 15: `fact_type-episodic-vs-state_assertion`），状态 ⏸ pending，触发条件标"等议题 12 王亮灰度跑通后回顾"
2. **议题 12 灰度真跑时（render_cards.py `--fold` 实施 + 王亮 fold + L2 重写）**：在 spot-check 阶段额外加一项**「**归档的 114 条老 facts 里有几条是重要 episodic**」**——做计数，作为本议题的实证锚点
3. **如果议题 12 灰度结果表明确实失踪 ≥3 条重要 episodic + L2 cite 跨文件穿透补不上**：升级本议题到"实施"，但**作为议题 12 §9.7 「按主题归档」的细化路径**，不是独立 schema 改动——三处修改重新评估范围
4. **评估断言**这条边界 case 单独议题登记（建议编号 16），与本议题独立——它是另一条本体论问题

### 核心假设

1. 议题 12 fold v2 灰度在 1-2 周内会真跑（不是无限期 hold）——如果灰度被搁置半年以上，本议题应该重启评估
2. 王亮 244 facts 的实测分布跟父会话提到的"创业方针"叙事是真存在的（不是假设性）—— 没核实具体哪几条 episodic 在数据里
3. timeline / L2 跨文件 cite 的兜底机制能在 fold 后真正承载 episodic 触达——FOLD_DESIGN §3 设计层面是的，但工程实施未跑过

### 可能出错的地方

- **最可能崩点**：议题 12 灰度迟迟不跑（被议题 14 C 阶段或其他议题阻塞），本议题 ⏸ 形态变成"无限期延后"，失去时机判断的本来意图。**对策**：父会话主代理推进议题 12 灰度真跑，给本议题留实证窗口
- **次可能崩点**：议题 12 灰度跑完真的发现 ≥10 条重要 episodic 失踪（不只 3 条），证明本议题的紧迫性比当前判断的更高——但即使如此，"先做议题 12 拿数据再做本议题"仍然是正确顺序，只是本议题升级速度会更快
- **第三可能崩点**：父会话采纳本建议后议题 12 跑完证明老 facts 失踪率可接受 → 本议题被无限期 ⏸ → 但其实应该升级为"评估断言"边界讨论；导致 cgboiler 错过另一个本体论改进机会（评估断言是真盲区）

### 本次哪里思考得不够

- **没核实具体数据**：父会话提到"王亮 2018 年的创业方针"——这条 fact 在当前 1900 facts 里到底存在不存在、被分到 episodic 还是 state_assertion 边界、年代是否真的是 2018（不是 2025）—— 没去 grep 王亮.md 看真实条目。如果父会话用的是 hypothetical 例子而不是实数，本议题"理论缺口的紧迫性"评估可能偏弱
- **关系断言** 边界 case 我提到了但没展开——它在多视角 first-class 设计下可能是更大的盲区（比 evaluative 还大），但本次回复没深挖
- **议题 14 reactive layer 评论 fact 是不是天然 episodic** 这个问题没处理——评论是反应行为，时间锚定强，但承载内容可能是 state_assertion（"@王亮 这事承德建龙挂账没解决" 是状态评估）。reactive + episodic/state 是不是另一个正交维度？没展开

### 如果 N 个月后证明决策错了，最可能的根因

- **N=3 个月**：议题 12 灰度跑完后发现归档的 114 条里 30+ 是重要 episodic（比预期 3 条多 10 倍）——证明 fold 切割语义错位是普遍问题不是个别 case，本议题应该先于议题 12 完成 → 错的是把"等数据"当成默认安全选项，但延后做的工程债比立即做的工程债高
- **N=6 个月**：议题 12 一直没跑（被其他议题阻塞），fact_type 议题 ⏸ 6 个月后失活，cgboiler 全量 26K notes 跑完后王亮膨胀到 800 facts，所有 episodic 全部沉默 → 错的是没设置"灰度无进展时本议题自动重启"的反向闸门

### 北极星触达

n/a——本议题是工程方案时机审查，不直接涉及 gg 三条北极星（二阶效应 / 动态学习 / 决策超越直觉）。但本判断的方法论（以已沉淀 essence 作工具 + 物理实证 cgboiler 当前状态 + 时机优先于内容判定）是 gg 的工作方式标准形态。

### essence 候选（可选）

- slug: `theory-gap-without-data`
- 一句话: 让 LLM 在没数据时识别"理论缺口"，它会找到一个，但这个缺口可能是它生造的——证伪需要数据，不是更深的理论分析。
- 备选第二行: 这是 task-compliance-is-not-truth 在"主动找问题"任务上的另一种形态。
- 是否已 append 到 essence.md: Y（待 append）

### 外部锚点

- `~/githubProject/cc-space/cgboiler/_pipeline/PENDING_DECISIONS.md` ← 议题 12/13/14 现状
- `~/githubProject/cc-space/cgboiler/_pipeline/STAGE3_STATE.md` ← batch1-007 后王亮 244 facts 实测
- `~/githubProject/cc-space/cgboiler/_pipeline/FOLD_DESIGN.md` ← §9 王亮单 entity 灰度方案，§9.7 留口"按主题归档"
- `~/githubProject/cc-space/cgboiler/PRINCIPLES.md` ← §3 反模式"持续涌现镜子陷阱"
- `~/githubProject/cc-space/cgboiler/SCHEMA.md` ← 当前 fact_signal 字段约束

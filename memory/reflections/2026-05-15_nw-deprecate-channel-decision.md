---
date: 2026-05-15
slug: nw-deprecate-channel-decision
summoner: cc-space
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: NW 是否扩 Deprecate 通道

### 给父会话的最终输出

**推荐**：B 否决，给 Bʹ。Keith 识别的"对称缺一档（NW 只产新增不识别拆除）"痛点真实，但 B 把它装错位置——NW 没有"该拆"的判定权威，强行让它产 Deprecate 提案会同时引爆两个 essence 警报：`pending-resolved-becomes-blocked-stagnation`（pending 池堵塞）+ `ownership-by-facet`（产消错位）。

**Bʹ 内容**：nw-daily.md Step 4.5 之后加 Step 4.7「退役雷达」——扫四类**结构性**信号（thread stale >30d / skill-auditor 已有低触发产出 / inbox/closed 反复主题 / CLAUDE.md 体积），聚合成晨间简报一段叙事，**不进 proposals.jsonl / 不产 Deprecate 提案 / 不下"建议拆"判断**。决策权留给 Keith 走对应垂直通道（threads / skill-auditor / inbox tripwire / context-curation）。

**砍掉的信号源**：B 原方案里"对话层 negative 信号"——`grep "删/拆/废"` 误判率高（代码 vs 机制无法机械区分），LLM 判断又会触发 `task-compliance-is-not-truth`。

**理由**：
1. NW 产出端权威在"识别异常"不在"价值判断"——"该拆"的本质判定在 4 个垂直通道（thread 主体运维期 / skill 触发分布 / inbox 主题反复 / CLAUDE.md 体积），NW 看到的是症状（"30 天没动"）不是本质（"主题已被收编"）
2. proposals.jsonl 池语义是"提议加新东西"——硬塞 Deprecate 类提案会让 pending 7→预计 20+，复现 essence `pending-resolved-becomes-blocked-stagnation`（5/9 已警告过的形态）
3. 晨间简报是聚合视图载体，跟"日报""周报"同类——退役雷达本质就是聚合视图，载体匹配
4. Bʹ 比 B 轻一档（不动 schema / 不加 type / 不耦合决策），4 周 tripwire 后看是否需要升级 A（加 Deprecate type）

**trade-off**：
- 代价 1：晨间简报多一段 30 秒阅读时间 / NW 跑时长 +5-10s（可接受）
- 代价 2：发酵期被误判为停滞期（essence `fermentation-without-detector` 反向风险）——对策：雷达硬约束"参考性，不强制动作"+ 物理上限 ≤8 条
- 代价 3：跟既有四通道有部分信号重叠（skill-auditor 已扫低触发）——可接受，聚合视图本来允许跨通道汇总

**未核验假设**：(a) 4 个垂直通道在 Keith 当前实际使用中真的覆盖了"该拆"决策需求（没让我物理核实 skill-auditor 最近一次输出形态）；(b) 30 天阈值是 sense-driven 初值，依赖 4 周 tripwire 校准（essence `idle-threshold-as-tripwire-not-answer`）。

**行动建议**（父会话执行）：
1. Edit `cc-space/harness-engineering/prompts/nw-daily.md`：Step 4.5 之后插入 Step 4.7「退役雷达」prompt（~30 行）；Step 5.3 加雷达段格式约定 + "参考性"硬约束
2. Edit `cc-space/threads/night-watch.md` append 一条本次决策时间线
3. **不**改 proposals.jsonl schema / **不**加 Deprecate type / **不**改 Step 4 / 4.5 / **不**改 CLAUDE.md（NW 项目级和 cc-space 项目级都不动）
4. 2026-06-12 触发回审（"真拆"比例 <20% 收紧阈值 / >60% 升级 A 加 Deprecate type）

### 核心假设

- NW 当前承载力的瓶颈是 pending → resolved 的 throughput（5/9 essence 已识别），不是"识别"能力——把"识别"加给 NW 不会压垮它，但把"价值判断 + 提案产出"加给它会
- cc-space 现状里"该拆什么"的判定权威已经分布在 4 个垂直通道，缺的是聚合视图而不是新判定器
- Keith 看到雷达后能区分"信号 vs 判定"——前提是文字硬约束 + 物理上限 ≤8 条

### 可能出错的地方

- **最大风险**：Keith 实际把雷达当 todo list 用——看到 4 条 stale thread 直接说"全砍"，触发 essence `fermentation-without-detector` 反向风险。概率 30%——Keith 是工程师本能"看到提示就处理"，但 cc-space CLAUDE.md 写明了 mirror/agent-lab/memory-lab 是探索豁免，他自己应该会过滤
- **次风险**：4 个垂直通道实际并不像我想的"已经覆盖"——skill-auditor 跑得不规律 / inbox tripwire #3 实际触发率低 / CLAUDE.md 体积扫描没机制——雷达成了唯一通道，那 Bʹ 应该升级 A。4 周 tripwire 能识别
- **小风险**：Step 4.7 prompt 写不干净，LLM 在"只识别不分类"指令下还是产了类似"建议拆 X"的句子——需要 Keith 看第一周输出校准

### 本次哪里思考得不够

- 没物理核实 skill-auditor 最近一次输出长什么样（cc-space 父会话信息里说"§4.4/§4.8 已覆盖一半"，我接受了这个 ground truth 没去验）——Bʹ 第二项信号源"引用 skill-auditor 既有产出"如果产出形态不对接，需要 Keith 落地时调整
- 没核 inbox tripwire #3 在 inbox/README.md 里的具体形态——我用了"复现 2 次升 thread"这个表述，是从 CLAUDE.md 推断的，可能跟实际契约对不齐
- 没考虑过 `forge` 工作区是否是"该拆"决策的更好载体——forge 承载"协作过程档案"，理论上"退役决策"也是协作过程的一部分，但 forge 不是日跑机制，雷达需要日触发，所以最终落 NW 是对的，但这条没显式 expose

### 如果 N 个月后证明决策错了，最可能的根因

最可能：**Bʹ 的"参考性，不强制动作"硬约束没顶住 Keith 的工程师本能**——Keith 看到雷达就处理，4 周后回审发现"真拆"比例 >60% 但拆错了 2-3 个还在发酵的主体，开始反思"是不是雷达存在本身就是诱因"。根因：雷达视角的物理存在改变了 Keith 的注意力分配，文字约束防不住注意力磁吸。

次可能：4 个垂直通道实际并不覆盖（次风险点验证），Bʹ 成了唯一通道而它又不产提案——形成"识别了但没动作"的死锁，跟它要解决的 stagnation 同形态。

### 北极星触达

**#1 二阶效应（space 方向）**：识别出"对称缺一档"这个一阶问题底下的二阶问题——治理机制的扩张冲动会自我膨胀到承担本不属于它的判断责任。Bʹ 不是给 NW 加功能，是给 NW 划边界——这是看得更远（避免 NW 在未来 6 个月被各种"对称扩张"诉求堆成 4-5 个语义重叠扫描器）。

### essence 对齐自检

- **本决策跟哪几滴 essence 对位**：
  - `pending-resolved-becomes-blocked-stagnation` (2026-05-09)——直接警报，B 方案会再生 stagnation
  - `ownership-by-facet` (2026-05-06)——拆动作归属应按面切分，NW 是"识别面"不是"判定面"
  - `fermentation-without-detector` (2026-05-15)——发酵期被误判为停滞期是 Bʹ 落地最大风险，对应 tripwire 设计
  - `idle-threshold-as-tripwire-not-answer` (2026-05-14)——30 天阈值用 sense-driven 初值 + 4 周 tripwire，不强求"最优值"
  - `gate-as-physical-fuse-not-business-metric` (2026-05-07)——雷达上限 ≤8 条是物理保险丝
  - `cadence-as-symptom` (2026-05-06)——否决 C 方案（手动 skill 在 cc-space 已大量样本不被触发，缺机制不缺手）
  - `task-compliance-is-not-truth` (2026-04-16)——砍掉"对话层 negative 信号"，LLM 在意图分类上的"让它找它就找"风险
- **本决策是否在某条 essence 上反着走**：无明显反向。`tool-elevation-as-occam` (2026-05-06) 说"第二消费者出现时上提是 OCCAM"，理论上"该拆什么"是第二消费者（第一是 NW 现有的"该加什么"），但 Bʹ 没上提到新独立工具，是因为 Bʹ 不是"工具"是"视图"——上提对象不匹配
- **cross-check 用的关键词**：grep "pending" / "ownership" / "fermentation" / "threshold" / "cadence" / "compliance" / "elevation" 在 essence.md（实际是启动时 Read 已加载，记忆中检索）

### essence 候选

- slug: `signal-without-judgment-as-aggregate-view`
- 一句话: 跨通道的"该拆"识别不应该升级为独立判定器——把信号识别和价值判断耦合是"产消错位"的高发陷阱，正确解是聚合视图（识别 + 显式不判定 + 决策权留垂直通道）。
- 是否已 append 到 essence.md: N（候选状态，等 Bʹ 跑 4 周看是否真站住再沉淀）

### 外部锚点

- `~/githubProject/cc-space/harness-engineering/prompts/nw-daily.md` ← Bʹ 落地点
- `~/githubProject/cc-space/threads/night-watch.md` ← 决策时间线 append 目标
- `~/githubProject/cc-space/MEMORY.md`（threads index）← 本决策不进 essence 但进 thread 时间线

---
date: 2026-05-14
mode: work
slug: cc-space-inbox-architecture
status: substantive-decision
summoned_by: cc-space 主会话
question: cc-space inbox/ 架构层决策——膨胀治理 + lifecycle 出口契约 + topic vs thread 边界
---

# inbox 架构决策

## 核心假设

1. **inbox 在 cc-space 拓扑的正确定位是"输入缓冲（短期）"，不是"议题工作区（长期）"**——长期记忆已由 threads（主体维度）+ CLAUDE.md 三层（工程契约）+ MEMORY.md/concepts/ssot/readings（索引层）承载，inbox 再做长期议题工作区 = 第二个 threads 在 inbox 里盖 = essence `ssot-distillation-vs-buffering` 失败模式
2. **膨胀的根因不是单文件不够大，是 lifecycle 没有显式出口契约**——70+ `[x]` 0 回收是 essence `default-bucket-as-deadlock` 的物证（流转 bucket 无显式出口 = 漏斗）
3. **升 thread 是 tripwire 题不是阈值题**（essence `premature-abstraction-tripwire`）——预设"≥N 行强制升"会批量升出大量"不是主体维度"的 essay，稀释 threads 语义
4. **不预建 hook/cron**——同构于 inbox-incubator 复盘范式（消费链路先证伪再建机制 + essence `cadence-as-symptom`）

## 可能出错的地方

- **三出口契约纸面化风险**：契约不写 hook 不写 cron，依赖人 + Claude 主动遵守。失败模式 = 90 天后 active 池又涨回 essay 池。防御：Phase C step 3 显式留 tripwire（90 天 6+ 行 essay ≥ 5 条 → 启动机制化），不是无限信任契约
- **briefs/ 留 inbox/ 跟"短期"定位有轻微张力**：brief 实际可能在 inbox/ 待 1 个月。降级处理：brief = "未毕业的议题"留 inbox 强化"待出口"语义；硬约束是 1 个月未推进 → close 或升 thread
- **tripwire 4 条判别标准的主观性**：第 3 次复现 / 外引出现 / 派生子结构 / 跨工作区——可能存在判别犹豫。前置兜底：6+ 行 essay 禁止 active（Phase C step 1 硬规则）

## 推理盲区

- 我没看 closed/ 的真实回收率历史——topics.md 当前 `[x]` 原位留痕模式实际已运行 ~1 个月（4-16 到 5-14），完整盘 Phase D audit 才能给出真分布。本方案的"出口 1 close 比例"判断是粗看推断，可能 audit 后发现 close 应进一步分两档（"决策完结" vs "被吸收到上层 topic"——后者其实是"出口 2/3 的轻量版"）
- briefs/ 当前 3 个文件的实际使用情况：cost-engineering-r4 是真在用（昨天 R4 brief 接受），paper-podcast 已 thread 化，cc-session-copilot 状态未核实——可能其中 1-2 个已经事实上死了。Phase B 迁移时这块要单独盘
- forge/ vs harness-engineering/analysis/ 哪个更适合接 nw-terminal-review-2026-04-21.md 出库——我说"forge 语义更贴"是推断；CC 主会话 Phase B 时实际判断

## N 个月后根因预判

如果 6 个月后这个方案被推翻 / 失败，最可能的根因：

1. **inbox 缓冲定位本身被推翻**：Keith 真实工作流不是"输入缓冲"模式而是"流动议题工作区"模式——他需要在 inbox 反复打磨议题（不是希望它快速出口）。但这个根因被 inbox-incubator 复盘（消费链路 0 read）部分否决了，可能性低
2. **"不预建机制"假设崩盘**：纸面契约被频繁违反，CLAUDE.md 多读一遍照旧 6 行 essay 涌入。需要 hook 拦截。这条概率最高，所以 Phase C step 3 留了 tripwire
3. **threads 体系本身的容量也到瓶颈**：50→80 个 thread 后 MEMORY.md 索引层失效，inbox 升 thread 的"主体维度记忆"语义连带稀释。这是 cc-space 整体记忆体系的二阶问题，不是 inbox 本身

## 北极星触达

- **二阶效应洞察**：本议题命中——把"局部膨胀治理"从"加分类机制"重定义为"流转契约设计"，落点是 cc-space 整个流转载体范式（NW 池子 / cgboiler / mirror / summon-deck 都有同问题）。Keith 自己在 inbox-incubator 复盘里写下的"消费链路有没有真消费比产物质量好不好优先证伪"是同源洞察
- **动态学习反哺**：直接调用 4 条 essence（default-bucket-as-deadlock / premature-abstraction-tripwire / ssot-distillation-vs-buffering / cadence-as-symptom）+ 1 个先验复盘（inbox-incubator）。这是 essence 物理参与推理的实例
- **决策超越直觉**：直觉答案是 D（时间窗分文件，按月归档自然驱逐）——快、清晰、扩展性好。但深推一层会撞 cc-space 主体维度中轴 → 砍。这次推理过程把"扩展性"问题从"分文件机制"重定义为"出口契约"，是抽象层切换不是技术选型

## essence 对齐自检

- `default-bucket-as-deadlock` (2026-05-06)：本议题就是这条 essence 的工程落点 - inbox/ 是流转 bucket，必须每个输入定义出口路径
- `premature-abstraction-tripwire` (2026-04-21)：用 tripwire 4 条判别取代"≥N 行强制升 thread"的硬阈值
- `ssot-distillation-vs-buffering` (2026-05-08)：否决 inbox 升级为"长期议题工作区"（= 第二个 threads 在 inbox 里盖）
- `cadence-as-symptom` (2026-05-06)：否决预先建 hook/cron - 先证伪契约能否生效，再决定建机制
- `merge-without-prevent-first` (2026-05-06)：Phase D 先盘存量数据（"合并能力"），Phase C 才考虑预防层（机制化 tripwire）- 顺序匹配
- `bucket-time-asymmetry` (2026-05-08)：inbox `[x]` 原位留痕 70+ 条 0 回收正是这条 essence 的实证 - 出口语义廉价化

候选新沉淀：`storage-vs-flow-confusion`——把"存储载体（threads / brief）"和"流转 bucket（inbox）"在物理布局上看似无差，在 lifecycle 语义上完全异构；混用后果是流转 bucket 退化为半成品存储（再补 essence 已有 default-bucket-as-deadlock 的"出口侧"，本条强调"两类设施的语义异构"）。但与 default-bucket-as-deadlock 重叠度 ~70%，不沉淀避免噪音。

## 对齐度

5/5——直接命中 essence 已沉淀的张力点（流转 bucket / 抽象时机 / SSOT 缓冲），是 essence 物理参与推理的清晰实例。决策方案就是 essence 在工程层的落地。

## 给父会话的最终输出

### 推荐

**单一方案：inbox 定位 = 短期输入缓冲，扩展机制 = 三出口契约 + 物理转移**（不分文件、不分时间窗、不升主题工作区）。

**核心论点**：膨胀的根因不是单文件不够大，是 lifecycle 没有显式出口契约——这是 essence `default-bucket-as-deadlock` 的工程落点。补出口契约 + 物理转移是 OCCAM 解。

### 候选否决理由

| 候选 | 否决 |
|---|---|
| A 单文件 + 状态过滤 | 不解决根本（无出口 = 仍漏斗）。essence `default-bucket-as-deadlock` 否决 |
| C 强制 ≥5 行升 thread | 违反 essence `premature-abstraction-tripwire`（决定权应让渡给"第 N 次场景"）；批量升 30+ thread 会稀释 threads "主体维度"语义 |
| D 时间窗分文件 | 跟 threads 主体维度中轴形成视角双轨，违反 essence `ssot-distillation-vs-buffering` |
| B 短期清账 + 归档 | **方向对，是本推荐雏形**，但缺扩展机制描述——下方给完整契约版 |

### 三出口契约

| 出口 | 触发 | 物理动作 | 留痕 |
|---|---|---|---|
| close | 当场决策完结/被吸收/拒绝 | 移到 `inbox/closed/YYYY-MM.md`（关闭月归档） | 一行摘要 `- YYYY-MM-DD 文本 (关：原因/去向)` |
| 升 thread | 主体维度议题（tripwire 4 条任一） | 新建 `threads/<X>.md` 完整 frontmatter + 时间线 | topics.md 原条目改一行指针 `- [→] YYYY-MM-DD 标题 → threads/<X>.md` |
| 升 brief | 结构化方案/调研（单议题单决策） | 写入 `inbox/briefs/<slug>.md` | topics.md 原条目改一行指针 → briefs/ |

**唯一 active 形态**：薄索引一行（≤80 字符）。**唯一例外**：tripwire 类条目 `[~]` 状态，trigger 一行写完不展开 essay。**禁止**：active 单条 >5 行 essay。

### 升 thread 的 tripwire 判别（任一触发）

1. 第 3 次复现：同议题在 2+ 次独立会话被讨论
2. 外引出现：被另一 topic/brief/thread 反向引用 ≥ 1 次
3. 派生子结构：已有 brief 或多次决议留痕
4. 跨工作区：议题关联 ≥ 2 workspace

**反向**：thread `status=archived` + <1KB + 无外引 → 折叠为 closed/ 一行摘要 + 物理删除。

### briefs/ 和独立文件归属

- `inbox/briefs/` 留 inbox/，作"出口 3"载体；inbox/README.md 描述生命周期（1 个月未推进 → close 或升 thread，触发由 NW dailyscan 命中而非预设 cron）
- `inbox/nw-terminal-review-2026-04-21.md` 出库 → 移到 `harness-engineering/analysis/` 或 `forge/`（forge 语义更贴，CC 主会话 Phase B 时拍）

### 迁移路径骨架

**Phase D（数据盘点，1-2h，CC 主会话直接做）**：
1. 扫 topics.md `[x]` 条目按关闭原因分类（① 当场决策 ② 被吸收 ③ 升 thread/brief ④ 拒绝 ⑤ 其他）
2. 扫 active 条目按 essay 长度（单行 / 2-5 行 / 6+ 行）
3. 跑 tripwire 4 条判别 → "建议升 thread 清单" + "保留 active 清单"
4. 产出 `inbox/_migration-audit-2026-05-14.md`（一次性 audit 文件，迁移完归档）

**Phase B（迁移，3-4h）**：按 Phase D 结果批量执行——`[x]` 移 closed/ + tripwire 命中升 thread + 6+ 行 essay 升 brief + nw-terminal-review 出库。

**Phase C（契约固化，30min）**：CLAUDE.md §目录约定 inbox 段重写 + 新建 `inbox/README.md`（< 80 行）。**不写 hook 不写 cron**——essence `cadence-as-symptom` 防御：90 天 tripwire 留口（active 池再次膨胀回 6+ 行 essay ≥ 5 条 → 启动机制化）。

**Phase E（30 天回顾）**：自然回看，不立 cron——active 条目数 / closed/ 月文件可读性 / briefs/ stale 数。

### 主要 trade-off

- 物理转移失去 grep 单文件看全部历史的便利 → closed/YYYY-MM.md 月度分页 + 全局 `grep -r inbox/` 仍可达
- 不预建机制依赖契约纸面执行 → Phase C step 3 tripwire 留口兜底
- briefs/ 留 inbox/ 跟"短期"定位轻微张力 → 用 1 个月未推进硬约束兜底

### Keith 拍板后的行动序列

1. 拍板三出口契约 + 物理转移 + tripwire 升降 + 不预建机制
2. Phase D 盘点（CC 主会话 1-2h）
3. Phase B 迁移（CC 主会话 3-4h）
4. Phase C 契约固化（CC 主会话 30min）
5. Phase E 30 天回顾（自然回看）

`nw-terminal-review-2026-04-21.md` 出库目标推荐 `forge/`，具体由 CC 主会话拍。

## 装配

- `cc_agent.md` / `KERNEL.md` / `CORE.md` / `state.md` / `essence.md` 启动 4 件
- 实证 Read：cc-space/inbox/{topics,todos,ideas,musings}.md 全量 / threads/decision-authority.md + night-watch.md 抽样 / threads 目录 ls
- essence 命中：default-bucket-as-deadlock / premature-abstraction-tripwire / ssot-distillation-vs-buffering / cadence-as-symptom / merge-without-prevent-first / bucket-time-asymmetry（6 条）
- 历史先验：inbox-incubator 复盘（消费链路证伪范式）→ 直接套用到本议题（不预建机制，先盘数据）
- 推理工具：激进派 vs 保守派对辩 / OCCAM 收敛 / tripwire 而非阈值 / 决策层切换（从"分类机制"切到"流转契约"）

## 北极星

二阶效应 5/5（重定义议题层 + 沉淀 cc-space 全流转载体范式可借鉴的契约模板）
动态学习反哺 5/5（6 条 essence 直接落地 + inbox-incubator 复盘范式同构）
决策超越直觉 4/5（直觉 D 时间窗被深推一层砍掉，切到抽象层）

整体 4.7/5 - 高对齐。

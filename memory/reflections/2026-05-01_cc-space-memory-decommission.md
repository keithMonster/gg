---
date: 2026-05-01
slug: cc-space-memory-decommission
summoner: cc-space
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: cc-space 废 CC 原生 memory 拓扑重组

### 给父会话的最终输出

**推荐**：

5 个决策一次性给定，不留 "也可以那样" 的开放：

1. **memory 4 类全废，但承接拓扑要校准**：
   - `user_role` → 独有的"内驱力"段 merge 进 `~/.claude/CLAUDE.md` Communication Style，整体删
   - 5 条 `project_*` → 4 删 1 merge（`project_cc_connect` 的 resume bug workaround/launchctl 命令 merge 进 thread `cc-connect.md`）
   - 22 条 `feedback_*` → 全归 CLAUDE.md 三层（按 scope 分流），**砍掉"feedback 校准缓冲"分类**——抽样验证证明 22 条没有一条处在校准期，分类基础不存在
   - 8 条 `reference_*` → 按内容分流（含密码的 wflow/cgdata DB 进 `database/CLAUDE.md`；upload2html 进 thread `cg-proxy-build.md`；fastgpt_selected_type_index 进 fastgpt skill；其余按主题分流）

2. **CC 原生 memory 机制必须主动禁用**：纯纪律一定复发；底层 SDK 触发的写入只能用监控层兜底——CLAUDE.md 全局段声明意图 + auto_cc_space 夜跑监控空目录新增写入

3. **MEMORY.md 拆两半**：Active Threads 段（41 个 thread 派生）独立成 `cc-space/MEMORY.md`，threads_sync.py 改写入路径；其他索引段全消融。`memory-system.md` 契约同步更新

4. **执行需灰度但不需要慢灰度**——文档迁移不是生产改造，6 个 Phase 之间设硬卡点（Phase 1 末验证派生 / Phase 2 末 grep 反向引用=0 / Phase 6.3 物理删除前等 1-2 工作日观察 CC harness 是否复现写入）

5. **二次 call gg 触发条件**：仅在 (a) Phase 4.1 出表后发现 feedback 与 CLAUDE.md 现状语义冲突需仲裁；(b) Phase 6 监控期发现 CC harness 频繁复现写入说明监控层失效

**理由**：

- "feedback = 校准期、CLAUDE.md = 成熟期"是为废 memory 找过渡载体的脚手架——Keith 是直接型沟通者，规则成熟一条立刻贴出来一条，没有"校准缓冲期"这种中间态。这是结构性洞察，不是抽样误差
- threads_sync.py 写入链路是 hook + auto-maintenance 双触发的脚本，路径改错会沉默失败——必须 Phase 1 双写过渡
- 反向引用（database/CLAUDE.md → memory/reference_wflow_db）是隐形断链源——必须每删一条 grep 全项目验证 0 引用
- 物理快照 + 1-2 周观察期是不可逆操作的兜底（CC harness 可能在空目录里复现写入，需要监控数据决定是否需要更强禁用机制）

**trade-off**：

- 砍掉 feedback 分类 = CLAUDE.md 三层会膨胀（22 条要消化，不全是已覆盖）。代价：L1 启动税增加。控制：用 OCCAM 严格压缩，能一句话说清的不写一段；项目 CLAUDE.md 增量控制在 +20% 内
- 不动文件系统权限（怕 CC 内部机制因写失败崩出怪现象）= 监控只能事后告警不能事前阻断——接受这个 trade-off，因为强制 enforce 的 blast radius 不可控
- "执行者自决 Phase 4 出表"= 略微违背 Keith 的"商量好直接执行"授权（执行者会自决处置）——但 Keith 已说不再回头确认，这是接受的代价
- **未核验假设**：假设 threads_sync.py 改写入路径不会触发 PostToolUse hook 的二次写入死循环（hook 监听 Edit/Write，sync 自身用 Write 改 MEMORY.md——若新写入路径在 cc-space/ 内会再次触发 hook）。Phase 1.3 测试时必须显式观察这一点

**行动建议**：

父会话（cc-space 主会话）按 Phase 0 → Phase 6 顺序执行：

1. **立即**：跑 Phase 0 物理快照
2. **第一批动作**：Phase 1（threads_sync 链路改造 + cc-space/MEMORY.md 创建 + 契约文件同步），完成后端到端测试新 CC 会话能正确读 cc-space/MEMORY.md
3. **第二批**：Phase 2（reference_* 含密码组先做，因为反向引用风险最高）
4. **第三批**：Phase 3（project_* 含 cc_connect merge）
5. **第四批（最大批量）**：Phase 4（22 条 feedback——必须先出 description 比对表再批量处理）
6. **第五批**：Phase 5（user_role）
7. **第六批**：Phase 6（禁用 + 监控 + 等 1-2 工作日 + 物理清空 + 一次原子 commit）

执行中遇到上述两种 call gg 触发条件之一时再回召；执行不确定性（删 vs merge）不要回抛——已有判断框架（覆盖度比对表）。

### 核心假设

1. **Keith 的工作流没有"feedback 校准期"中间态**——这是基于 22 条 feedback 抽样 0/22 处在待验证态的结构性推断。如果 Keith 实际偶尔会"先观察一段时间再固化"，这个假设错，应保留某种轻量缓冲载体
2. **CC harness 的 auto memory 触发在 SDK 内核层而非 prompt 层**——这是基于"settings.json 没有公开开关"的反向推断。如果实际有未公开的 env var 或配置项可以关，监控层兜底是 over-engineering
3. **threads_sync.py 改写入路径后 PostToolUse hook 不会触发死循环**——这个是 Phase 1.3 必须现场验证的，不能假设
4. **项目私有 = 密码可进 git** 由 Keith 明示（背景段已说），不是我的判断

### 可能出错的地方

最可能崩在 **Phase 4 的 22 条 feedback 处理**——这一批的内容多样性最大，"已覆盖"的判定边界模糊（语义接近不等于完全覆盖），可能会误删独有内容。概率：30%。兜底：执行报告必须附"未迁移内容审计表"让 Keith 事后能 review。

次可能崩在 **threads_sync.py 改写入路径触发死循环**（Phase 1.3）。概率：15%。兜底：Phase 1.1 的双写过渡 + 测试一次端到端写入再继续。

第三可能崩在 **CC harness 在 Phase 6.3 物理删除后立即在空目录里写新 memory**——纯纪律失败的复现。概率：40%。但这种崩是可控的（监控会捕捉），需要的是更强的禁用机制（可能要走文件系统层 immutable bit），不是灾难。

### 本次哪里思考得不够

1. **没物理验证 settings.json 是否真的没有 auto memory 开关**——只是基于"我快速回忆没见过"。决策 2 的 A 路被我直接判死，应该让父会话先 grep 一下 ~/.claude/settings.json 确认
2. **Phase 4 的"出表"步骤具体怎么做没展开**——我说让执行者出表自决，但表的 schema、grep 命令、判定标准都没给。这一步会成为 Phase 4 的卡壳源
3. **没考虑 cc-space 主会话本次执行完后 reflection 自身的载体问题**——这次执行会产出"我做了哪些迁移、迁到哪了"的执行报告，应该落到哪？inbox? 一个新 thread `memory-decommission`? 没设计

### 如果 N 个月后证明决策错了，最可能的根因

3 个月后最可能的根因：**砍掉 feedback 分类后，Keith 实际开始有"想沉淀但不想立刻进 CLAUDE.md"的中间态需求**——可能因为某次某条规则刚成型不确定要不要全员推、或者某条只对当前阶段有效不想污染长期契约。这时缺中间载体会让用户回到"自己当历史记忆者"的状态，正是 memory-system.md 想消除的核心病灶。

防御方式：执行后 1 个月观察一次，如果出现"我想记一条但不知道放哪"的对话信号，立刻补 cc-space/inbox/calibrations.md 类轻量载体，不要硬撑"砍掉就是对"。

### 北极星触达

#1 二阶效应洞察。本决策的二阶效应链：废 memory 不是节省存储，是**消除 SSOT 漂移源**——同一事实多处存 = 必然漂移；移除一份 = 减少一种漂移可能。Keith 看的是"5 年后我的协作记忆系统是不是仍然可信"，不是"今天少 36 个文件"。

二阶效应的反向锚点也成立：feedback 分类砍掉 = 砍掉"软知识缓冲"这个抽象层 = 强迫所有规则一形成立刻进契约 = 提升 CLAUDE.md 三层的演化压力。这种压力是健康的（避免规则在缓冲层睡死），也是负担（用户必须立刻判断 scope）。

### essence 候选

- slug: ssot-distillation-vs-buffering
- 一句话: 软知识缓冲层是漂移的温床——它假装在等待规则成熟，实际在让多源 SSOT 的不一致逃过审视
- 是否已 append 到 essence.md: Y

### 外部锚点

- `~/githubProject/cc-space/memory-system.md` ← 持久化分层契约（Phase 1.5 必须同步更新）
- `~/githubProject/cc-space/threads/README.md` ← threads 写入规则
- `~/githubProject/cc-space/CLAUDE.md` ← 项目级（Phase 1.4 / Phase 4 多次更新）
- `~/.claude/CLAUDE.md` ← 全局级（Phase 5 / Phase 6.1 更新）
- `~/githubProject/cc-space/shared/scripts/threads_sync.py` ← Phase 1.1 改写入路径

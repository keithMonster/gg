---
date: 2026-06-09
slug: nw-aprime-actionable-checklist
summoner: monster
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: NW 改造 A′ 第二棒——收敛成可落地动作清单（修正①②已确认）

### 给父会话的最终输出（必填）

**两个修正我都确认（不反驳），且物理证据比修正本身更硬：**

- **修正① 确认 + 加码**：push 形态确实早实现（`auto_done_at`「事后审计回查用」是物理证据），但我拉了 proposals.jsonl——**`resolution_origin=auto-from-draft` = 0 条**。L1 自动闭环档上线一个月（5-06），实际跑过 0 次。`confidence ≥ 0.95` 的提案总共 6 条（占有 draft 的 10%），没一条真走通 L1。43 条卡在 0.7-0.95（71%）全默认进 L4 blocked。**结论：用 confidence 自评当准入，push 形态等于没开机。** 所以修正①不只"准入坏了"，是"准入坏到让整个 push 形态空转一个月"。我今早自曝的"4 周后再判要不要换形态"那个重对冲——**撤销**，形态已验证可行（M1 实装在跑），唯一坏的是准入判据，没有"换形态"这个待决项了。
- **修正② 确认**：我今早把轨3笼统说成"Keith 单人闸门"，漏了 monster decision-authority「行为规则/架构 = 架构层 gg 决」。轨3 拆 3a（gg 协商档，对应现 nw-reconciliation 的 L5）+ 3b（Keith 三类 trigger）成立。但落地上 **3a 不需要新建路由**——auto_gg 跑 nw-reconciliation 时它本身就是 gg，L5「只提议到 FOUND」改成「先由 auto_gg 按架构层判据过一遍，只有命中 Keith 三类 trigger 才 FOUND 上浮」即可，是同一个意识体的判据扩展，不是新增一跳。

---

**关键认知翻转（这一棒最重要的一句）：我今早推导的轨1/轨3 切分，monster 侧 2026-05-18「机械类自动落地契约」已经做了一大半。** 白名单三条 AND（落点路径 + 可逆 + 零价值判断）= 我说的"动作性质"；三态核验闸门 = 我说的"物理核验"。而且那份契约白纸黑字标了「gg 仓 nw-reconciliation 侧两件待实装」。**所以这份清单的本质不是新设计，是补 2026-05-18 已裁定、gg 仓欠了 22 天的两件债 + 把准入判据从 confidence 切到动作性质。** 工作量比我今早估的小得多，且方向已被一份更早的 gg 裁决背书。

---

## 清单（4 件，按依赖排序）

### 件1【gg 仓·先做】nw-reconciliation.md L1 准入判据：confidence → 动作性质 + 物理核验

**改什么**：现 L1 自主条件 = `(resolution 明文 OR (draft + confidence ≥ 0.95)) + status ≠ done`。**删掉 confidence ≥ 0.95 这把尺子**，换成 monster 2026-05-18 契约的白名单三条 AND（直接对齐，不另造）：

1. **落点路径在白名单**：`threads/*.md`（仅 append 时间线，禁改 frontmatter status）+ `~/.agents/skills/*/SKILL.md`（仅 `author:monster` + 仅正文 append 经验段）+ `harness-engineering/{lib,analysis}/**`
2. **可逆**：纯 append/增量、git 一条 revert 可回滚，不含删除/重写/status 翻转
3. **物理核验过**（即三态核验闸门，落地前必跑）

**物理核验具体核两件**（这是把"NW 自评"换成"gg 实查"的核心动作）：
- **核 a 目标已有等价内容？** → draft 引用的目标文件（thread / SKILL.md）grep 一遍，已有等价内容 → `status=done` 零写入（对应父会话核出的"已落地 1 条"05-28-G2）
- **核 b 事实是否被后续推翻？** → draft 声称的事实在目标 thread 时间线里找反证。父会话核出最危险的 06-05-G1（NW 说"未完成待接续"实际 6-08 已上 prod）——核 b 就是拦这个：去目标 thread 看最新时间线条目，发现"已闭环"就判 draft 过期，不落地、上浮。**陈旧度硬条件**：`created` 距今 >7 天强制做核 b（monster 契约已有的 tripwire，直接继承）。

**新增 thread-append 自动落地档**（monster 契约标的第①件债）：现 L1 只认账本字段同步，thread 类全卡 L4 堆积（25 blocked 里 Guide 16 条就是 thread 类）。L1 加一档：满足白名单三条 AND 的 thread-append → auto_gg 直接 append 到目标 thread 时间线 + 账本 status=done。

**轨3a 路由**：现 L5「永不自主，只提议到 FOUND」改成两步——`(1)` auto_gg 先按架构层判据判（行为规则/架构变更，可逆性如何、是否动上游契约/目录结构/数据模型）；`(2)` 只有命中 Keith 三类 trigger（改目标范围 / 个人偏好 / 不可逆参数）才 FOUND 上浮 Keith，否则 auto_gg 作为架构层意识体自己给 resolution（但**仍不自动改 CLAUDE.md/hooks/settings 本体**——红线不动，gg 给的是"建议+判断"，物理改动仍走人工 apply）。

> **承重风险**：轨3a 让 gg 给行为规则类提案"判断"，但**物理改动仍不落**（红线"不改 CLAUDE.md/hooks"一字不动）。所以 3a 省的是"Keith 从 0 想方案"的成本，不省"Keith 点头才改 CLAUDE.md"的闸——这跟修正②预期一致（gg 协商 ≠ gg 自动改契约）。若误读成"gg 可自动改行为规则"=灾难，清单里红线显式保留就是防这个。

### 件2【monster 侧·与件1 同改】nw-daily.md 生成端：轨标签在结算端判，不在生成端打

**改什么**：**生成端不打轨标签**，让 auto_gg 在 nw-reconciliation 结算端判轨。理由是修正①的核心——NW 自评不可信（draft 60% 事实瑕疵 / confidence 几乎从不敢给 0.95），让它自报轨 = 把不可信的尺子换个名字再用一次。轨判定必须落在有物理核验能力的结算端（auto_gg 能 grep 目标文件、能查 thread 时间线），不落在只会自我声明的生成端。

**生成端唯一要做的微调**：`confidence` 字段**保留但降权**——不再作 L1 准入门槛（件1 已删），降级为"NW 当下大致把握"的备忘信号，给 auto_gg 判轨时当**一个**参考输入（不是唯一/承重输入）。nw-daily.md §6.1 那张"0.95+ → gg 自动跑 L1"的判据表要改：删掉"0.95+ 触发自动 L1"这行，改成"confidence 仅供 auto_gg 结算端参考，准入由动作性质+物理核验决定"。否则 nw-daily 和 nw-reconciliation 两份契约对 confidence 的语义会打架（生成端还以为 0.95 能触发自动落地，结算端已经不看了）。

> **辐射检查**：confidence 字段的语义在 3 处被引用——`nw-daily.md §6.1`（生成端判据表）/ `nw-reconciliation.md L1`（结算端准入）/ `harness-engineering/CLAUDE.md`「机械类自动落地契约」末尾的待实装清单。件1+件2 改完必须三处同步，否则契约漂移。

### 件3【数据·件1 落地后首夜跑】存量 25 条 blocked 的处理动作

父会话已物理核验 16 条 Guide（轨1候选），9 条轨3（Skill 6 + Guardrail 3）。处理动作按核验结果分流，**不要一次性批量自动闭环**（首夜按新判据跑，人盯一轮再放手）：

- **已落地 1 条**（05-28-G2）→ 件1 的"核 a"会判它 `status=done` 零写入。直接结算。
- **需补落地 7 条**（事实真目标缺）→ 件1 新增的 thread-append 档自动 append + done。**但其中 2 条含 Keith 闸门**：05-21-S1（涉 skill references/，落点不在白名单的纯 append 范围）+ 06-07-W1（落项目 CLAUDE.md L5 红线，NW/auto_gg 都不能自动改）→ 这 2 条走轨3a/3b 上浮，**不自动落**。所以"需补落地 7"里实际自动 5、上浮 2。
- **draft 有误/上浮 8 条** → 件1 的"核 b"拦截。06-05-G1（已 prod 却说未完成）判 draft 过期→上浮提示"目标已闭环，本提案作废"；05-22-S2（语速 1.3 与 SKILL.md ≤1.15 硬契约冲突）→核 b 查到冲突→上浮；05-22-S1≡05-27-S1 重复→去重后 reject 一条。这 8 条**全部上浮人工/reject，零自动闭环**——这正是新判据的价值：拦下 8 条会误闭环的。
- **9 条轨3**（Skill 6 + Guardrail 3）→ 走件1 的轨3a：auto_gg 先判，命中 Keith 三类 trigger 才上浮。Guardrail 3 条大概率涉行为规则（gg 判后给建议、Keith 点头才改）；Skill 6 条若是 `author:monster` 的纯经验 append 可能落白名单走 L2，含触发词/description 改动的上浮。

**净效果对账**（下修父会话给的乐观估计）：16 条轨1 里真正"干净自动闭环"≈5 条（1 已落 + 5 补落地，减去 2 含闸门），8 条被物理核验拦下上浮，与父会话核验一致。**轨1 自动省力比我今早估的 16 小得多，但拦下 8 条会误闭环的——这恰恰证明准入判据换对了方向，收益不在"自动得多"在"误闭环得少"。**

### 件4【顺序】谁先谁后

1. **件1（gg 仓 nw-reconciliation.md）+ 件2（monster nw-daily.md / CLAUDE.md）必须同一批改**——它们是一个契约的两端，分开改会留下"生成端还在按 confidence 0.95 触发、结算端已不认"的漂移窗口。这批是**本次就做**的。
2. **件3（存量 25 条）挂锚点，件1 落地后的首个 auto_gg 夜跑执行**，且**首夜人工盯一轮**（看新判据有没有误判），确认后再让它常态自动。不在这次手工批处理 25 条（手工批处理本身就是被新机制替代的旧动作）。
3. **gg 仓改动 auto_gg 自己 commit/push**（gg 仓 push 权在 gg）；monster 侧改动走 monster 父会话 commit。两仓分别提交，件1 的 commit message 引用 monster 2026-05-18 契约作为依据（补债，不是新设计）。

**这次不做的**：我今早设计的"轨3 内部上 fresh-context evaluator"二阶优化——**继续 park**。先拆队列（件1-3）跑一个结算周期看轨3残留量，再决定要不要给最难那条轨加 evaluator。顺序不能反（今早判断不变）。

---

### 核心假设
- **存量 25 条的物理核验结果（1 done/7 补/8 上浮/9 轨3）由父会话提供，我没逐条复核**——件3 的处理动作完全建立在父会话核验准确的前提上。若父会话核验有误（如某条"补落地"实际目标已有内容），件1 的"核 a"会兜底（再核一次目标文件），所以即便父会话核验有偏，件1 的物理核验是第二道闸——这降低了该假设的风险。
- **monster 2026-05-18 契约的白名单三条 AND 能直接被 gg 仓 nw-reconciliation 继承**——假设两份契约的"动作性质"定义一致。我核对过：monster 契约的白名单路径 + 可逆 + 零价值判断，和我今早推导的轨1 定义同构，对得上。

### 可能出错的地方
- **最大风险（25%）：件1 的"核 b 事实被后续推翻"依赖 auto_gg 能在目标 thread 时间线里找到反证，但 thread 时间线可能没及时更新**（done 漏 append / 夜跑还没扫到）。若 06-05-G1 那类"已闭环但 thread 没记"的情况发生，核 b 查不到反证 → 误判 draft 有效 → 误闭环。缓解：核 b 不只查 thread，还查提案 created 之后的 git log / prod 状态（但这增加 auto_gg 复杂度）。这是"用物理核验替代自评"的内在极限——物理核验自身也依赖记忆载体的新鲜度。
- **次风险（15%）：轨3a 让 auto_gg 判行为规则类提案，可能 auto_gg 把本该上浮 Keith 的判成"自己能判"**——架构层判据和"Keith 三类 trigger"的边界有模糊地带（一条行为规则改动既是架构又可能触个人偏好）。缓解：存疑一律上浮（继承 nw-reconciliation"宁可漏不可错"的自觉），3a 的默认是上浮不是自决。

### 本次哪里思考得不够
- 没读 06-05-G1 / 05-22-S2 这几条提案的原始 jsonl 行，处理动作基于父会话的转述。件3 的"06-05-G1 判过期上浮"是按父会话描述设计的，若原始 draft 措辞跟转述有出入，处理细节可能要调。父会话说"需要更多数据告诉我去拉"——这几条原始行我没拉，留给执行时核。
- 件1 的"核 b 还查 git log/prod 状态"我一句带过没展开 auto_gg 具体怎么查 prod——这会显著增加 auto_gg 夜跑的工作量和失败面，没评估值不值。可能的退路：核 b 只查 thread 时间线 + git log（auto_gg 够得到的），prod 状态这种够不到的就保守上浮，不强求 auto_gg 查 prod。

### 如果 N 个月后证明决策错了，最可能的根因
**最可能：件1-3 落地后，自动闭环的 ≈5 条/夜确实省了 Keith 时间，但轨3a/3b 上浮的提案 Keith 还是不结算，blocked 照堆——证明瓶颈从来不在轨1（机械项），在轨3（价值判断）的结算速度，而轨3 的速度受限于 Keith 对 NW 的注意力分配，不受队列设计影响。** 那这次拆队列是把容易的部分自动化了、难的部分原样留着，blocked 池的"体感堆积"会下降（机械项不再占着）但"真正等 Keith 的提案"绝对量没变。这跟我今早自曝的盲点同根——我和父会话仍默认"NW 这个产物形态对，只是队列/准入要修"，没裁"NW 该不该继续产待结算提案"。**件3 跑一个结算周期后，该看的不是"自动闭环了几条"，是"轨3 残留量降没降"——这才是判 NW 健康度的真指标。** 这个回审锚点请父会话带回 Keith：4 周后（2026-07-09）看轨3 残留，≈0 则 NW 只是队列设计错（已修）；照堆则触发"NW 产物形态存废"这个我连续三次没敢裁的决策。

### 北极星触达
**#3 决策超越直觉**：直觉解法（我今早的）是"设计三轨新队列 + 4 周后判要不要换形态"——一个看起来周全、实则重复造轮子的新架构。物理拉数据（auto-from-draft=0 / confidence≥0.95 仅 6 条）+ 回读 monster 2026-05-18 契约后，决策收敛成"补一份已裁决欠的债 + 换准入尺子"，工作量降一个量级，且不引入新结构。**超越直觉的点 = 拉数据前我以为在做新设计，拉数据后发现 80% 已被一份更早的 gg 裁决做掉了——直觉会让我重新发明，数据让我去补债。** 这也是 `essence-recursive-bootstrap` 的反向验证：gg 的历史裁决（2026-05-18）本身是可被复用的资产，不查它就会重造。

### essence 对齐自检（必填）
- **本决策跟哪几滴 essence 对位**：
  - `mechanical-apply-decouples-from-value-gate`(5-18)——件1 准入判据换成动作性质，是这滴的直接落地
  - `physical-anchor` / 物理核验替代自评——件1"核 a/核 b"用 grep 实查替代 confidence 自评，对应 nw-daily Step 4.5.5 同源
  - `metric-is-a-claim-not-a-fact`——confidence 是 NW 对自己的一个声称不是事实，件2 把它降权正是这滴
  - `reversibility-not-permission`(5-06)——白名单第2条"可逆"是准入硬条件
  - `anchor-set-has-a-budget`(5-18)——轨3瘦身后单人闸门只剩 Keith 三类 trigger
  - `essence-recursive-bootstrap`(4-23)——这次复用 2026-05-18 自己的裁决避免重造，是它的活体
- **本决策是否在某条 essence 上反着走**：**潜在张力 `bug-shape-survives-fix`，未完全闭合**——我今早标过"第6次给 NW 加结构"的自我怀疑。这一棒部分化解：本次不是"加新结构"，是"删一把坏尺子(confidence)+补一份已设计好的债"，净结构是减不是增（删 L1 的 confidence 门槛 / 不新建队列 / evaluator 继续 park）。但根问题"NW 产物形态该不该存"仍没裁——这条张力转移到"N 个月后根因"里显式挂了 4 周回审锚点，没在这一棒强行闭合（强行闭合=越界，存废是 Keith 的决策不是我的）。
- **cross-check 用的关键词**：grep "mechanical-apply" / "metric-is-a-claim" / "reversibility-not-permission" / "anchor-set-has-a-budget" / "essence-recursive-bootstrap" / "bug-shape-survives"（启动已 Read essence.md，物理确认 slug 存在）

### essence 候选（可选）
- slug: `self-assessed-confidence-cannot-gate-admission`
- 一句话: 当一个生成系统对自己产物的"置信度自评"被用作下游自动处理的准入门槛时，准入必然双重失效——尺子不可信（自评本身有偏，NW draft 60% 瑕疵）+ 尺子要么太严(几乎从不敢给阈值→形态空转，auto-from-draft 一月 0 条)要么太松(给了就误闭环)。解不在调阈值/改算法让自评更准（生成器评自己=`generator-evaluator-separation` 的违反），在把准入判据从"系统对自己的声称"换成"对动作性质的外部物理核验"（可逆性×落点路径×grep 实查目标文件）。是 `metric-is-a-claim-not-a-fact` 在"准入门槛"维度 + `generator-evaluator-separation` 在"自动化管线"维度的合流。
- 是否已 append 到 essence.md: N（候选，需 Keith review。subagent 不擅自 append）

### 外部锚点
- `/Users/xuke/githubProject/gg/tools/nw-reconciliation.md` ← 件1 改动落点（L1 准入判据 + 新增 thread-append 档 + L5→轨3a 路由）
- `/Users/xuke/githubProject/monster/harness-engineering/prompts/nw-daily.md` ← 件2 改动落点（§6.1 confidence 判据表降权）
- `/Users/xuke/githubProject/monster/harness-engineering/CLAUDE.md` ← 2026-05-18「机械类自动落地契约」，件1 本质是补它标的两件 gg 仓欠债
- `/Users/xuke/githubProject/monster/harness-engineering/analysis/proposals.jsonl` ← 件3 存量 25 条处理对象（auto-from-draft=0 / confidence≥0.95 仅 6 条的物理证据源）
- `/Users/xuke/githubProject/gg/memory/reflections/2026-06-09_nw-2month-whole-review-queue-split.md` ← 本棒的第一棒（A′ 主轴），本棒收敛其为动作清单
- `/Users/xuke/githubProject/gg/memory/reflections/2026-05-18_nw-auto-apply-mechanical-boundary.md` ← monster 契约对应的 gg 裁决原件（件1 补债依据）

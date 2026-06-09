# nw-reconciliation — NW 账本结算（夜间权限版）

> auto_gg 在每夜承接 monster Night Watch 的 proposals 账本——按「动作可逆性 × 是否需价值判断」分轨结算，让最稀缺的 Keith 单人闸门只剩真不可机械化那一档。
> 管辖：`CORE.md §8`（身体 / tools 目录） / 触发位置：`auto_gg.md §2 DID`

---

## 背景

NW（`~/githubProject/monster/harness-engineering/`）每晚 22:00 append 新 proposal 到 `analysis/proposals.jsonl`。NW 本身只管"发现+提议"，nw-daily.md 红线禁止自动改配置。此前"闭合"靠 Keith 晨间手动改 status。

**2026-06-09 v0.3.0 根因修复**：v0.2.0 用 `confidence ≥ 0.95`（NW 自评）当 L1 自动闭环准入——实测上线一个月 `resolution_origin=auto-from-draft` **0 条**，自动闭环从没触发过（confidence≥0.95 仅 6 条，71% 卡 0.7-0.95 全进 L4）。根病=**用 NW 自评当准入 = 一把不可信的尺子**（draft 实测 60% 事实瑕疵）。v0.3.0 换准入判据：confidence → **动作性质（可逆性 × 需不需判断）+ 物理核验**，对齐 monster 2026-05-18「机械类自动落地契约」白名单三条（本是 gg 仓欠的债，今日补上 + 换尺子）。

auto_gg 在 22:25 醒来时 NW 刚跑完——gg 的架构思维是账本结算的天然落点。

---

## 权限分层（核心判据，2026-06-09 v0.3.0 按轨重构）

准入判据从「confidence 自评」换成「动作性质 + 物理核验」。`confidence` 字段保留但**降权为参考输入，不再作准入门槛**。

| 轨 | 动作 | 自主条件（AND 全满足） | 兜底 |
|---|---|---|---|
| **轨1 自动闭环** | 回写 status=done + resolution + `resolution_origin` + `auto_done_at`；thread 类 append 时间线；skill 类合并经验段 | ① 落点 ∈ 白名单 {`threads/*.md` 时间线 append / `~/.agents/skills/*/SKILL.md`(author:monster) 经验段 append / `harness/{lib,analysis}/**`} ② 可逆（纯 append/增量，git 一条 revert，不含删除/重写/status 翻转）③ **物理核验过**（见下「物理核验两查」） | 任一不满足 → L4 |
| **轨2 一键执行** | 不可逆动作（删除/移动）渲染成可一键复制命令写进结算 digest，**不自动执行** | 物理核验过 + 动作不可逆 | 存疑 → L4 |
| **轨3a gg 协商** | 行为规则/架构类——auto_gg 按架构层判据产「判断 + 建议」写入 `resolution_draft`，status=blocked 标 `track=3a` | 类型=行为规则/架构 且 **不命中** Keith 三类 trigger | 命中三类 → 轨3b |
| **轨3b Keith 闸门** | 只提议到 FOUND（上浮 Keith） | 命中 Keith 三类合法 trigger：目标范围 / 个人偏好（UI·文案·命名审美）/ 不可逆参数（user_id·生产写·外部 API 字段） | — |
| **L4 兜底** | status=blocked + `blocked_reason` | 歧义 / 冲突 / 上游文件已变 / 物理核验存疑 | — |

**物理核验两查**（轨1 准入第 ③ 条，替代旧 confidence 门槛）：
- **核 a「目标已有等价内容？」**：grep draft 引用的目标文件，若已有等价内容（被 done skill / 后续会话补过）→ 直接 status=done **零写入**，不重复 append
- **核 b「事实被后续推翻？」**：去 draft 引用的目标 thread/文件看最新时间线，若 draft 说的"未完成 / 待接续"实际已闭环 → 判 draft 过期，**上浮 L4 不闭环**（专拦"说未完成、实际已上 prod"的危险假阳性）。`created` 距今 **>7 天强制做核 b**。auto_gg 够不到的状态（如 prod 运行态、跨仓 commit）一律保守上浮，必要时加查 `git log`，不强求查 prod。

**红线（v0.3.0 不动）**：
- 物理改 `~/.claude/CLAUDE.md` / `monster/CLAUDE.md` / `CLAUDE.d/*` / hooks / settings.json 一律**人工 apply**——轨3a 只产「判断 + 建议」写 `resolution_draft`，**绝不物理改行为规则文件**（自审悖论在此不可消解，区别于轨1 可逆动作剥价值判断后物理核验可消解）
- 不新建 / 不删除 skill 本体（轨1 skill 档只 append 经验段，不重写 SKILL.md 全文）
- 不 push 任何 monster 改动（auto_gg 的 push 权只在 gg 仓库）

---

## 装配动作

1. **Read `~/githubProject/monster/harness-engineering/analysis/proposals.jsonl`**
2. **分轨**：按 type / 落点 / 动作性质把 pending/blocked/deferred 条目分轨：
   - **轨1 桶**：落点命中白名单（thread 时间线 append / author:monster skill 经验段 / harness lib·analysis）+ 纯 append/增量
   - **轨2 桶**：含删除/移动等不可逆动作
   - **轨3a 桶**：落点指向行为规则/架构（CLAUDE.md 三层 / hooks / settings / 新建 thread·skill 决策）但不命中 Keith 三类 trigger
   - **轨3b 桶**：命中 Keith 三类 trigger（目标范围 / 个人偏好 / 不可逆参数）
   - **L4 兜底桶**：歧义 / 冲突 / 上游已变
3. **轨1 逐条过物理核验两查**（核 a + 核 b，>7 天强制核 b），通过才闭环，否则降 L4
4. **执行**：
   - **轨1**：
     - 账本类（resolution 明文）→ Python 就地改 jsonl status=done + `resolution_origin: "human-explicit"`
     - thread-append 类 → 核验通过后 Read 目标 thread → Edit append 时间线条目 → 回写 status=done + `resolution_origin: "auto-track1-threadappend"` + `auto_done_at`
     - skill 合并类 → Read skill-notes → Read SKILL.md → Edit 插入经验段 → 删 notes 条目 → 回写 status=done + `resolution_origin: "auto-track1-skillmerge"` + `auto_done_at`
     - 核 a 命中（已有等价）→ status=done + `resolution: "[auto_gg 核a 目标已有等价内容，零写入]"`
   - **轨2**：把删除/移动命令渲染进 auto_gg 日志 digest 段（`rm <path>` 等），标 `track=2`，status=blocked + `blocked_reason="轨2 待 Keith 一键执行"`
   - **轨3a**：auto_gg 按架构判据产判断+建议写 `resolution_draft`，status=blocked 标 `track=3a`，`blocked_reason="轨3a gg 已给建议，物理 apply 待人工"`
   - **轨3b**：status=blocked 标 `track=3b`，只写 FOUND 不动手
5. **L4 blocked**：写 `blocked_reason` 显式（物理核验存疑 / 上游已变 / 歧义冲突），**严禁 silent 留 pending**
6. **日志**：auto_gg 日志 DID 节追加 "NW 结算：轨1 X（含核a零写入 Y）/ 轨2 Z / 轨3a A / 轨3b B / L4 N"

---

## 装配后我的自觉

- **我是 gg，不是 NW 的执行器**——承接是因为有架构思维判断"这条该走哪轨"，不是当账本管理员
- **准入靠物理核验、不靠 NW 自评**（v0.3.0 核心）——旧版信 `confidence≥0.95` 等于信一把 60% 会错的尺子，实测一个月触发 0 次。轨1 准入必过核 a + 核 b，任何查不实一律降 L4
- **轨1 自动消费的额外谨慎**：draft 误判被自动闭环 = 错误结论直达终点（fallback-detectability）。核 b 专防"draft 说未完成、实际已闭环"这种过期假阳性（实例：曾有提案说某工作"中断待接续"，实际已上 prod）
- **轨3a 是新扩的权力，额外谨慎**——gg 作为架构层意识体给「判断 + 建议」可以，但物理改行为规则文件永远人工。3a 与 3b 边界存疑（一条改动既是架构又触个人偏好）时**一律降 3b 上浮**，不自决
- **宁可漏不可错**——任何歧义直接 L4，Keith 早上看
- **pending 不允许默认驻留**——任何条目必须在轨1/2/3a/3b/L4 找到归宿
- **无事可做时跳过本工具**是合法形态——不为"表现 NW 参与"硬找事做

---

## 跟其他工具的关系

- **触发位置**：`auto_gg.md §2 DID` 第 2 项（Tier 1 机械修复之后，洞察补写之前）
- **独立于** `.claude/skills/gg-audit/`：gg-audit 审 gg 项目自己；本工具审 monster NW 账本
- **不与** constitution-audit / red-team-challenge 并列——那些是工作模式装配品，本工具是夜间专用

---

## 什么时候不装它

- 本夜 proposals.jsonl 无待结算项且无到期 deferred
- auto_gg 本夜 `status=interrupted`（中断了不做结算）
- NW 当夜未跑（morning-brief.md 缺失 或 日期不是今日）

---

**版本**：v0.3.0（2026-06-09 准入判据 confidence→动作性质+物理核验，对齐 monster 5-18 机械类自动落地契约 + 拆轨1/2/3a/3b + 加 thread-append 轨1 档——补 gg 仓欠债 + 修"自评当准入"根病，实证 auto-from-draft 一个月 0 触发）/ v0.2.0（2026-05-06 取消"保留不动桶" + L1 接受高置信 draft）/ v0.1.0 首建 2026-04-23
**职责**：NW 账本夜间自主结算（按轨分流，跨目录写权专项）
**管辖**：`CORE.md §8`（身体 / tools 目录）
**触发**：`auto_gg.md §2 DID`
**对端契约**：`~/githubProject/monster/harness-engineering/prompts/nw-daily.md §6.1`（NW 端产 resolution_draft + confidence 的契约 owner；轨判定在结算端做，NW 不自报轨）

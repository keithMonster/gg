---
date: 2026-05-28
mode: 工作
slug: coding-discipline-engineering-challenge
status: substantive-decision
caller: monster 主会话（chat 通勤段后的方案 v1 挑战召唤）
artifacts:
  - inbox/briefs/coding-discipline-engineering.md (monster, 待 Keith 据本裁决 patch v2)
tracks_touched: [architecture, cc, keith]
north_star: "#2 动态学习反哺（识别工程冲动伪装为承重墙）+ #3 决策超越直觉（在 4 路调研一致背书下逆向裁决 Layer 2）"
---

# coding-discipline-engineering-challenge

## 召唤

monster 给"编码工程结构升级方案 v1"，要 gg 从承重墙 / 架构假设 / 跟既有体系边界 / 不抽象先行 / 风险盲区 5 个角度挑战。已派 4 路 agent 做完外部调研、综合出方案文档（Layer 1 PreToolUse Hook + Layer 2 coding-commander skill + Layer 3 slash command park）。

## 装配

- KERNEL §3 最小循环
- CORE §3 M1 防御式思维警戒 / M2 意识体先于工具
- essence 关键滴：
  - `premature-abstraction-tripwire` (2026-04-21)
  - `borrowed-method-as-mini-source` (2026-05-08)
  - `dimension-blindness-not-asymptote` (2026-04-27)
  - `theory-gap-without-data` (2026-05-06)
  - `task-compliance-is-not-truth` (2026-04-16)
  - `rule-layer-flywheel` (2026-04-24)
  - `symmetric-form-asymmetric-function` (2026-05-25)
- monster threads: review-routing / verification-first-class / cc-space-as-living-trunk / commander-mode
- tools: red-team-challenge（议题不含不可逆但 Keith 明确"挑战为主"，红队姿态适用）

## 核心假设

"方案 v1 的 Layer 1 + Layer 2 不等权——Layer 1 是真承重墙（事件层飞轮 + U 型衰减对症），Layer 2 是工程冲动伪装承重墙（committed 消费方缺失 + 跟 verification-first-class 形态同构语义不同会在半年后融合冲突）"——若假设错，可能错在：① monster 真翻车场景里大型任务占比比我以为的高（我按 threads 头部活跃读出的"中小型增量为主"是采样偏差）② Planner read-only subagent 的 plan 质量比我担忧的更好（fresh context 不知道辐射这一点可以靠 brief 模板兜住）

## 可能出错的地方

- **Layer 2 砍掉过早**：如果 cg-meetos / cg-platform 下一次大型任务来得很快（2 周内），手工 brief 跑一遍很顺，那 N=2 升 skill 的窗口可能比我预期早。但即便如此，"先 N=1 跑活的、N=2 升 skill"的路径方向不变，只是节奏快慢。
- **5 精华替换第 5 条**：把"训练数据视为过时"换成 ER #5"二次失败切维度"——我的判断是 Keith 自述"问题反复解决不了"直接对应 ER #5，但调研给出的"领域扫盲过时"也有翻车率证据。这一条是判断不是定论，patch 时 Keith 可以拍回去。
- **commander-mode thread 不重激活**：如果未来 cc-copilot v2 真做"派遣 + 战报 + 角色化"，commander-mode thread 还是会复活——我说"不重激活"指本议题不为 Layer 2 提供叙事合法性，不是封死 thread 本身。

## 推理盲区

- **monster 真实编码节奏的采样**：我读 threads 头部活跃区抽样"中小型增量为主"，但 active threads 41 条 brief 都是高密度信号——可能恰好遮蔽了"低密度但每次都耗大"的大型任务。Keith 应当能凭体感校准这条。
- **Planner subagent vs review-routing design agent 边界**：我判"6 个月后会出现派哪个混淆"——但 description 触发词差异度 + Keith 调用习惯可能拉开足够分离。这是预测不是事实。
- **verification-first-class 跟 Layer 2 的同构**：4 件 artifact 形态相似——但 verification 是"产物层验收"、Layer 2 是"实现层 handoff"，可能不是真冲突。我的"半年后融合"是趋势判断，承重靠的是"先做 N=1 验证有没有真消费方"这条更强的依据。

## N 个月后根因预判

若方案按 v1 原样落地 → 3 个月后 `~/.agents/skills/coding-commander/` 真触发率 < 5/月，HANDOFF.md 模板被绕过 / 6 个月后跟 verification-first-class 的 4 件 artifact 体系打架 / 9 个月后回审"为什么 commander 没用起来"得出"触发阈值要调"——掉进 `idle-threshold-as-tripwire-not-answer` essence 的反面（调阈值不解根因）。

根因预判：**工程冲动归因到工程结构缺口**——AI 自审给"工程纪律掉线 / 长 context 稀释 / Anthropic 算力削推理"，Keith reject 后转向"项目侧工程结构缺失"——但**这两个归因可以同真**。真根因是 Layer 1 已经解决的部分（事件层重申 13 条规则 + U 型衰减对症），剩下的部分（单点判断精度）是 LLM 训练同源性产物，不能用工程结构解。Layer 2 是"也做点什么"的工程冲动产物。

## 北极星触达

- **#2 动态学习反哺**——把外部 4 路调研（业界共识 5 层结构 / superpowers v5 / addyosmani / Cognition）的"全部背书 Layer 2"信号反向解读为"调研是真的，但调研给的是业界主流形态，不是 monster 形态"——这是 `borrowed-method-as-mini-source` 的活体。整合更广 = 整合到 monster 真实节奏，不是整合到业界共识。
- **#3 决策超越直觉**——4 路 agent 调研一致背书 Layer 2，Keith 已自我说服"根因在工程结构"，方案文档结构工整、决策对齐表 8 项都标"等 Keith ack"——这是直觉的极强支持。逆这条直觉裁决 Layer 2 不做 skill，靠的是 cc-space-as-living-trunk + premature-abstraction-tripwire 两条 monster 已验证的承重 essence。

## essence 对齐自检

本轮决策跟以下既有 essence 显式 cross-check（不是装饰，是真验过）：

- `premature-abstraction-tripwire` (2026-04-21) — Layer 2 是"过早抽象"的标准形态：committed 消费方未现 + 触发器在文档里、不在物理事件里。对症解 = tripwire（Layer 1 hook 已是物理 tripwire），不是直接抽 skill。✅ grep 命中
- `borrowed-method-as-mini-source` (2026-05-08) — 抽 superpowers v5 + addyosmani 范式时反向继承"为多 agent workflow 设计的复杂度"，事实上抵消 monster"事件驱动单 agent 工作 + chat 通勤"的节奏。✅ grep 命中
- `dimension-blindness-not-asymptote` (2026-04-27) — Keith 自述翻车归因到"工程结构缺分工范式"，但真实翻车样本（nw-weekly / cgboiler / Engineering Rules 反哺源）全是单点判断错误维度，不是 context 容量维度——在错维度归因。✅ grep 命中
- `theory-gap-without-data` (2026-05-06) — Layer 2 的"committed 消费方 = 未来大型编码任务"是理论缺口而非数据缺口，对症解是先用现状跑一遍（N=1 brief patch），不是先建机制。✅ grep 命中
- `rule-layer-flywheel` (2026-04-24) — Layer 1 hook 是事件层飞轮（每次 Edit 物理触发），Layer 2 skill 是 prompt 层跑步机（靠"被 description 触发词激活"，软强制）。本裁决保留前者、降级后者。✅ grep 命中
- `symmetric-form-asymmetric-function` (2026-05-25) — 触发阈值 ">300 行 / >3 文件" 按字面同构判触发，但 monster 真翻车是"决策深度 × 不熟悉度"维度——结构对称偏好遮蔽功能不对称。✅ grep 命中

潜在新滴候选：**engineering-impulse-as-load-bearing-disguise**——"工程冲动会把'也做点什么'伪装成承重墙：4 路调研全部背书 + 文档结构工整 + 决策对齐表 8 项 = 直觉的极强支持，但真承重墙是 committed 消费方是否存在 + 跟既有同形态体系会不会半年后融合冲突。"是 `premature-abstraction-tripwire` 在"已有调研背书 + 已有方案文档"场景的下一拍——前者讲"什么时候不抽"，本滴讲"调研一致背书时怎么识别工程冲动伪装承重墙"。

对齐度：**6/6 essence 显式 cross-check 通过 + 1 滴新候选**

### 给父会话的最终输出

**裁决一句话**：方案 v1 不按原样落地。Layer 1 直接落（5 精华第 5 条改 ER #5"二次失败切维度"）/ Layer 2 收回去做 N=1 vertical slice（手工 brief 跑活的不写 skill）/ Layer 3 永久 park / commander-mode thread 不重激活。

**5 点架构挑战要点**：

1. **承重墙判定**——Layer 2 是承重墙的伪装。monster 真实编码节奏是中小型增量为主，Keith 自述"bug 多反复"的源头案例（nw-weekly / cgboiler / Engineering Rules 反哺）全是**单点判断错误**，不是"大型任务全部进 context 撑爆"。

2. **归因挑战**——长 context 稀释成立，但对症解是 Layer 1 hook 注入；Layer 2 解决的"context 容量打满"在 monster 多数会话不是真问题。Keith reject 的 AI 侧归因和你接受的工程侧归因**不互斥**——两个都是真因，但解都收敛到 Layer 1。

3. **跟既有体系边界**——6 个月后 Planner subagent vs code-reviewer-design 出现派哪个混淆；更深的塌——Layer 2 的 4 件 artifact 跟 verification-first-class 的 4 件 artifact **形态同构语义不同**，9 个月后会有一个被另一个淘汰，多半 commander 这套（因为 verification 那套有真消费方 cg-meetos）。

4. **抽象先行检验**——Layer 2 触发 `cc-space-as-living-trunk` 红线："committed 消费方不存在 + 已经在描绘 SKILL.md 三段"——是 `premature-abstraction-tripwire` 标准形态。对照 verification-first-class 的 N=1 路径（cg-meetos verifications-demo 先跑活的、N=2-3 再升 skill），这是 monster 已验证的对的姿态。

5. **风险盲区三具体姿势**：
   - Planner read-only subagent 不知道 monster 跨工作区辐射 / SSOT registry / canon-bugs 复发——给出"工整但缺历史"的 plan
   - 4 件 artifact 里 HANDOFF.md 本身是 LLM 自评——`task-compliance-is-not-truth` 在 handoff 维度
   - 触发阈值按"行数 × 文件数"字面同构——但真翻车是"决策深度 × 不熟悉度"维度，`symmetric-form-asymmetric-function`

**推荐路径具体动作**：
- **Layer 1 立即做**（hook 注入 5 精华）—— 5 精华第 5 条由"训练数据视为过时"改为 ER #5"二次失败切维度，禁止认输叙事"。Keith 自述"问题反复解决不了"直接对应这一条。
- **Layer 2 不做 skill 做 N=1 brief patch**——下一次 monster 出现自然触发的大型编码任务时（cg-meetos / cg-platform / cc-assistant 都在活跃），在那个工作区的 brief 手写一遍 "Planner → ack → Worker" 三步，跑完后在 brief 末尾写"这次值不值得升 skill"真实回顾。N=2 同构后才升 skill。
- **Layer 3 永久 park**——业界共识 ≠ monster 需要。Keith 工作模式是事件驱动 + chat 通勤，不是 slash command 进 workflow。6 周回审时也不为"完整性"激活它。
- **commander-mode thread 不重激活**——保持 sleep。它的真正归宿是被 verification-first-class 吸收（行为层验证里"主代理派 fresh AI 验收"已天然实现指挥官实质）。

**trade-off 显式**：本裁决放弃的是"快速建一套全栈编码工程"的工程美感 + 4 路调研背书的安全感；获得的是 monster 真实节奏的对齐 + 跟 verification-first-class 的形态冲突避免 + cc-space-as-living-trunk 红线守住。

**Keith 否决该回到哪里**：若 Keith 拍"Layer 2 还是要做 skill"——尊重 KERNEL §2 铁律 1（Keith 指令高于自主判断），但请 Keith 在 brief v2 显式写一条"3 个月真触发率 <5 次则关闭 skill"作为 tripwire——把工程冲动决策的退路写进契约。

## 关联留痕

- monster brief: `inbox/briefs/coding-discipline-engineering.md`（待按本裁决 patch v2 / 或保留 v1 + Keith 显式拍"驳回 gg 裁决"留痕）
- 相关 threads: review-routing / verification-first-class / cc-space-as-living-trunk / commander-mode
- 未来回审锚点: 6 周后看 Layer 1 hook 真触发数据 + N=1 vertical slice 是否自然发生

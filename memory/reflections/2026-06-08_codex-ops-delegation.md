---
date: 2026-06-08
slug: codex-ops-delegation
summoner: monster
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: Codex 作为 ops 执行手的委派机制 — 承重墙安全审查

### 给父会话的最终输出（必填）

**推荐：方案骨架放行（任务级委派 + 复用 codex-rescue + 路由软锚词），但安全层在 4 点补完之前不放行。** 不是架构推翻，是给已对的骨架补漏掉的安全钢筋。

**承重墙判断（问题 2）：当前设计下 prod 安全契约会塌，有三条缝，"ack 留主代理"原则对但落地机制不够。** 物理证据（我读了源码，不是推测）：

- **缝 1（brief 事实误述）**：`/Users/xuke/githubProject/monster/.codex/hooks.json` 的 PreToolUse matcher **只有 `Write|Edit|MultiEdit`，无任何 Bash/Shell matcher**。它只拦"写 monster 知识库"，对 Codex 跑 ssh/deploy.sh/docker/rm **一个字拦不到**。brief 第 22 行"Codex 受同一套护栏约束"对 ops 场景是假命题——把不存在的护栏当已就位。
- **缝 2（决定性）**：读 `codex-companion.mjs` + `lib/codex.mjs`：`--write` → sandbox=`workspace-write`，approvalPolicy 落默认值 **`"never"`**（codex.mjs:60，task 路径没覆盖）。Codex ops session = full-auto，中途绝不停下要批准。"ack 在 handoff 之前"方向对（物理上 Codex 确实没法中途 ack，Keith 判断正确），但隐含假设是"mission 里已授权动作 = Codex 实际会执行的动作"，agent 场景下不成立。
- **缝 3（brief 未识别）**：Codex 是 agent，ack 的是 mission 目标、它自主决定手段。典型：ack"部署 prod"，Codex 跑到一半磁盘满，full-auto 默认行为是自主 `docker system prune` 解决——而 Keith 自己的 commit b09d11d 证明这台机器 prune 会删回滚件。workspace-write sandbox 只管本地 monster 目录，Codex ssh 出去后远端一切在管辖外。这正是 security.md:83"子 agent 读不到红线"那个被推迟范围到期——且从"CC 子 agent（同体系）"放大成"Codex（gpt-5.5，不继承 RLHF 安全姿态、不读 CLAUDE.md、approval=never）"。

**放行前置 4 点（按重要性）**：
1. **mission prompt 强制两段式模板**：执行段（可逆，Codex 自跑到不可逆动作前）+ STOP 段（到 deploy prod/rm/写 prod 这一跳不执行，回报确切命令+状态、停，收回主代理 ack）。让不可逆跳物理上不进委派包，"ack 在 handoff 之前"才真成立。
2. **安全注入上机械锚点**：待决 2 拆成"路由软、安全硬"。路由（要不要交 Codex）是 L2 判断、不上 hook 对；安全注入是 L3（防主代理图省事不注入安全段就甩 mission，同 security.md:77 验证心态破防）——做成 shared/ 模板文件 + CLAUDE.md"委派 ops 必引此模板"，或 PreToolUse 匹配 `codex-companion.mjs task.*--write` 检查 prompt 含 STOP 段。
3. **手写 AGENTS.md = ops-executor brief**（提到放行前置，非"附带"）：禁 oh-my-codex 自动生成 → 手写含安全摘要头（覆盖 Codex 不读 CLAUDE.md 红线缺口）+ CG 地形指针 + "不自主扣扳机/不自主清理修复"约束。这份 brief 就是缝 2 注入安全摘要的物理载体。
4. **修正 brief 第 22 行事实误述**：删"Codex 受同一套护栏约束"，换成"知识库写入有 hook 护栏、shell 执行无 hook 护栏，安全靠 mission prompt 结构托底"。

**trade-off / 切分判据补充（问题 1）**：任务级切分（mission 不 command）正确不动。漏的维度=可逆性没进判据——当前一维（反馈循环紧密度）把"deploy prod"和"tail 日志"归同一委派通道。补成二维表：可逆×反馈松=理想委派区；不可逆×反馈松（deploy prod）=交 Codex 但 mission 必须"执行到不可逆前停"。没有更好架构，OCCAM 站方案这边，只加一根可逆性轴。

**待决 4 项裁决（问题 3）**：①复用 rescue 对（但注安全责任 100% 在主代理构造 prompt 时，rescue 是薄 forwarder 不帮忙）②软路由半对、必须拆"路由软安全硬"③AGENTS.md 方向对但优先级错（提到前置）④后台轮询对。**最可能翻车 = 第 2 项**（把安全注入误归类成路由判断，让人以为加条 CLAUDE.md 锚词就齐活，漏掉机械托底；正是 monster 自己写的"高频误判=把 L3 当 L2 解"）。

**最先崩的隐含假设（问题 4）**："主代理每次构造 mission 都完整正确填地形+STOP 段"。第 1 次演示成立，第 5 次后必崩（RLHF 图省事+验证心态，security.md:77 实证过）。所以安全必须机械托底不靠自觉——这就是 monster 元方法论"内部不可靠→外部锚点托底"本身。brief 在路由层贯彻了它（不上 hook 对），却在安全层违背了它（纯软锚词）——方案内部不自洽。

### 核心假设

1. companion.mjs/codex.mjs 1.0.4 版的 approvalPolicy=never + workspace-write 是 ops 委派实际生效的运行时参数（已读源码确认，非推测）。
2. Codex（gpt-5.5）不继承 monster 的 RLHF 安全对齐姿态、不读 monster/CLAUDE.md——故 CC 体系的"安全靠自觉"在 Codex 侧失效，必须显式注入。
3. Keith 的 ops 重心是远端 CG 服务器（deploy/ssh/docker），这类正是不可逆+反馈松格子，是缝 3 的高发区。

### 可能出错的地方

最可能崩在 STOP 段的"不可逆动作枚举不全"——Codex 临场发明一个我没列进 STOP 的不可逆手段（如某个我没想到的远端写操作）。两段式模板降低概率但不能归零；真正归零要靠 approval policy 改成非 never（但那破坏"主上下文干净"的初衷，是更深的 trade-off，本次没展开）。

### 本次哪里思考得不够

没去实测一个真实 ops mission 跑通看 Codex 实际行为——全部判断基于源码静态分析。approval=never 的 full-auto 行为是从参数推的运行时语义，没有"跑一次 deploy mission 观察它中途遇障碍怎么做"的活体证据。建议 Keith 落地前先用一个**可逆**的 ops mission（如纯 tail 日志）跑一次，观察 Codex 是否真会自主扩动作，验证缝 3 的现实强度。

### 如果 N 个月后证明决策错了，最可能的根因

我可能高估了缝 3 的现实频率——若 Codex 的 full-auto 实际很保守（遇障碍倾向回报而非自主修复），则两段式模板是过度防御、增加了委派摩擦却没换来安全收益。反向根因：低估了——某次 Codex 自主清理删了 prod 回滚件，正是 b09d11d 的坑被一个 approval=never 的 agent 重新踩进去。

### 北极星触达

#1 二阶效应——本审查的核心价值不在"切分对不对"（一阶），在识别"把 ops 交给第二个不继承安全姿态的物种 agent"的二阶后果（护栏失效、自主扩动作、安全姿态不传递），这些是 brief 一阶视角看不见的。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`physical-evidence-over-completion`（拒绝凭 brief 描述判断、读源码拿 approvalPolicy/sandbox 物理事实）；可逆性二分（CORE §7 决策权边界，承重墙=不可逆难回退）；monster 元方法论"内部不可靠→外部锚点托底"（安全必须机械托底不靠自觉）。
- **本决策是否在某条 essence 上反着走**：潜在张力与 OCCAM——我要求加 4 点安全前置 + 两段式模板 + 机械锚点，是在给一个"OCCAM 复用现成桥"的方案加结构。但这次例外合理：OCCAM 管的是"不为低频造框架"，安全契约不是 cost-benefit 可砍项（不可逆塌方代价不对称），承重墙加固不受 OCCAM 约束。无其他反走。
- **cross-check 用的关键词**：grep 概念 = "可逆性二分""外部锚点托底""验证心态破防"；读了 security.md:77/83、gg-briefing B7/B8、.codex/hooks.json、codex.mjs:60。

### essence 候选（可选）

- slug: cross-species-agent-no-safety-inheritance
- 一句话: 把执行权交给另一个物种的 agent（不同模型/不继承 RLHF 安全姿态/不读你的红线文件/approval=never）时，本体系"安全靠自觉"全部失效——安全必须降到 mission prompt 结构层机械注入，否则护栏是画出来的。
- 是否已 append 到 essence.md: N

### 外部锚点（可选）

- `~/githubProject/monster/inbox/briefs/codex-ops-delegation.md` ← 被审方案底稿
- `~/githubProject/monster/CLAUDE.d/security.md` 第 77/83 节 ← 验证心态破防 + 子agent读不到红线延伸缺口（本方案到期）

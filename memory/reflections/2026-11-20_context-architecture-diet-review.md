---
date: 2026-11-20
slug: context-architecture-diet-review
summoner: monster（Antigravity 原生子会话，agy:1e3357fa 回合的外部架构审核）
northstar_reach: "#1 二阶效应 / #3 决策超越直觉"
status: substantive-decision
---

# Reflection: 多端上下文架构瘦身与冲突消歧，外部架构审核

## 给父会话的最终输出（必填）

**总裁决：PASS，带 2 条高优先级必改。** 三层切分本身成立，没有哪一项需要撤回。真正的结构风险不在挪走了哪些段，而在两处“声明比承载它的版面活得久”的地方。

**本次没想到的一点**：热排把 monster 宪法的语义顺序绑到了厂商一个未文档化的截断常数上（本会话实测在 23,896 B 处按行截断，见我自己上下文里的 `<truncated 16917 bytes>`）。适配层那句“前 24KB 已含……纯问答免补读”是一张豁免，只有 **1,128 B** 余量在守它，而且没有任何传感器盯着。

### 高优先级，必须改
- **H1 monster 热区没有传感器，适配层豁免会静默过期。** 事实：第 1–11 节结束于 22,872 B，`## 目录与文件命名约定` 从 22,872 开始，到 24,494 结束，截断点落在这一节中间（第 3 条铁律之后）。`tripwire_check.py` 只有 `AGY_GLOBAL_BODY_CAP=23900`，只覆盖全局文件；`guard_claude_md_size.py` 也只管全局文件。安全红线（7 KB，改得最频繁）一旦增长约 1.1 KB，`纠正即落库 / 语言交互 / 克劳德=kk` 就会被挤出 agy 视野，但 `monster-on-antigravity.md` 会继续宣称它们在场并免补读。过期事实会误导，过期豁免会教唆违约（与 08-06 replica 裁决同构）。**修法**：加 `agy_monster_hot_zone` 哨。用与 agy 相同的规则算出“按行对齐、≤24,000 B”的截断点，断言适配层宣称的末节标题偏移 ≤ 截断点 − 300 B 余量；配合成违规反向用例。机械可判，成本 <30 行。
- **H2 `bot_channel_inject.py` 把可宝的 bot 标成“Keith 个人飞书通道”。** 事实：`FEISHU_PERSONAL_PROJECTS` 含 `kebao-cc`；`threads/kebao-cc.md` 写明它是“给 Keith 的朋友可宝使用的个人 agent”。另外 `gg/cc/dd/gggg/mirror/dojo` 在 `config.toml` 中 `allow_from=NONE`，注入器却只凭项目名断言委托人身份。monster 红线里“Keith 本人在个人主会话……已点名通知即本次授权”这条豁免，正好能被这句身份断言激活。目前是潜伏态：钩子只接在 `monster/.claude/settings.json`，经 agy adapter 才能到达；`~/.codex/hooks.json` 没接，kebao-cc 是 Codex 后端，工作目录也不在 monster，所以活的消费者只有 agy/agyy，而这两个都配了 `allow_from`。**修法**：个人集合只取 `allow_from` 等于 Keith 的项目（agy/agyy/mc/mcc），其余落到 fallback 全文；措辞从“当前为 Keith 个人通道”改成“该入口登记为 Keith 专属（物理门禁 = config.toml allow_from）”。至少要立刻删掉 `kebao-cc`。

### 中优先级，建议改
- **M1 agy 开发会话要付两份钱，而且依赖自触发补读。** 截断后常驻 23.9 KB，开发时再整读 40.8 KB，合计 64.7 KB；CC/Codex 只付 40.8 KB。补读是 prompt 层自触发（跑步机）：漏读不会产生事件，`公共能力速查/元方法论/工程原则补充` 缺席时零告警。**更本质的修法**：agy SessionStart（已有 `agy_cc_guard_adapter --event session-start`）在 cwd=monster 时，按截断点注入尾部字节（约 16.9 KB）。这样 agy 与 CC/Codex 对等，没有重复也不依赖自触发，热排也从承重件降为纵深防御，“免补读”这条豁免可以整句删掉。[推测] agy hook 输出是否有大小上限，需要先探针。若有上限，退而求其次：只注入一行“截断于第 N 行，补读用 StartLine=N−2”，至少消掉 24 KB 重复。
- **M2 `resident_budget` 按写者字节计价，不按读者字节。** A→B move 的扣减逻辑写得严谨（源净减与目标净增双封顶），但它衡量的是文件字节。一个 B 文件如果实际每次会话都被读（agy 整读 monster、Codex 每次派发都读 codex.md），move 记作节省，读者付的量却不降，甚至多一跳。**修法**：复用脚本里现成的 transcript 扫描，加一个 B 热度探针。某 B 文件在 ≥50% 会话里被读 → 按有效 A 档计，并作废对应 move 扣减。
- **M3 适配层“模型与编排速览”是 `runtime/agy.md` 的副本，没有漂移检测。** 它常驻 agy、在场收益为正，作为缓存是合法的；但 `ssot/seam-pairs.md` 里没登记这一对（已 grep）。**修法**：登记为 seam #16，速览只保留“静默违约型”条目（禁 Orchestrator / 3p 清零 / Workspace=inherit / 禁外部 Ghostty Tab）。

### 低优先级，可选
- L1 GPT 校准卡没有对应 gemini 卡 L4 的“派发前读 `runtime/codex.md`”指针。先用 `codex_trend.py` 量“派发但未读 codex.md”的比例，再决定加不加。
- L2 gemini 卡第 4 条松绑引入了模型自判的分类出口（“深度架构讨论”）。卡上已有 `check: 回复字数 P90`，定一个两周复核点，对比 6,792 基线，回升就收回。
- L3 `目录与文件命名约定` 跨截断线，只能看到半节。压约 600 B 让它整节落在截断线内，或者整节明确放到截断线之后。
- L4 注入器企微切段分支目前零活消费者（kk 是 Codex 后端，platform-help 在 config 里已注释），属于为假想消费者写的逻辑。另外，原生子代理会继承 `CC_SESSION_KEY`，也会被注入“聊天通道 / 不打 file://”，与宿主子代理的输出约定冲突。
- L5 `A_CAPS` 给 monster 的上限是 48,000，大于 agy `read_file` 单次 46,080 的上限，“单步整读”在那之前就会失效（工具会显式提示 partial，属于响亮失败）。

### 保持现状
三层正交切分、runtime 改成薄路由加三份切片（每端只读自己那份，常驻层省 15.7 KB）、全局正文 23,063（余 837 B）、删除 GEMINI.md、修正 RN `check_inbox`、注入器 fail-safe 回退全文、`monster/AGENTS.md` 不掏空。都不撤回。

**trade-off**：M1 的尾部注入会让 agy 的纯问答会话每次多付 16.9 KB，换来与其他三端对等、去掉自触发依赖；Keith 的价值序是能力 > 体验，我推荐付这笔。H1/H2 都是减法或机械哨，不新造墙。

**行动建议（按顺序）**：H2 删 kebao-cc 并改判据 → H1 加热区哨和反向用例 → 探针 agy hook 注入上限再定 M1 走哪条 → M3 登记 seam → M2 排进 resident_budget 下一版。

## 核心假设
- agy 截断规则是“按行对齐、≤24,000 B”。依据是本会话内两份规则的截断点（23,896 / 23,742）都落在行尾，n=2。
- 注入器活消费者只有 agy/agyy。依据是 grep `~/.codex/hooks.json`、`~/.codex/config.toml`、`monster/.claude/settings.json`；Codex 在别处挂钩子的可能没穷尽。

## 可能出错的地方
- 如果 agy 的截断按字符算或另有规则，H1 的哨要按实际规则校准。哨本身应以实测截断点为准，而不是写死常数。
- M1 的尾部注入若遇到 hook 输出上限，会退化成只给一行 StartLine 提示的方案。

## 本次哪里思考得不够
- 没实跑 `resident_budget.py` 和各单测，测试结论采信 RESULT.md 的回执。我只核对了源码片段和登记行，没复算 move 扣减的边界。
- `agy_cc_guard_adapter.py` 怎样执行 CC 项目钩子，我没读源码，路径 `shared/scripts/` 下没找到；“agy 经 adapter 到达注入器”是由本会话确实收到注入反推出来的。

## 如果 N 个月后证明决策错了，最可能的根因
H1 的哨挂在 tripwire 夜跑上，但安全红线的增长发生在白天会话里，赶在哨报警之前就已经有 agy 会话在缺失规则的状态下运行过。这时应当把哨前移到 `guard_claude_md_size` 写入闸。

## 北极星触达
#1 二阶效应：看到的是声明（适配层豁免、注入器身份句）比版面和门禁活得久的衰减路径，而不是一阶的字节节省。#3：把“热排是否成立”换成了可机械核对的截断点算术。

## essence 对齐自检（必填）
- **对位**：`one-shot-invariant-decays-under-live-append`（H1：适配层宣称 × monster 持续追加）、`presence-benefit-splits-replica-verdict`（M3 合法缓存需 hash/seam；H1 过期豁免的教唆不对称）、`quota-in-the-readers-currency`（M2）、`the-principals-voice-is-a-default-not-a-credential`（H2）、`omission-failures-evade-event-driven-sensors` + `rule-layer-flywheel`（M1 自触发补读）、`the-premise-expired-without-a-diff`（厂商截断常数是写入时的快照）。
- **反着走**：`separation-need-is-not-topology-verdict` / `ghost-rules`。H1/H2 是在加哨或改判据，会不会是防从未发生的灾难？我的判断是不算：H2 是删掉一个错误事实，不是新增规则；H1 是给一个已经在承重、而且已经被一份文件宣称的不变式补失效检测，不是新造墙。M1 有潜在张力：尾部注入是新机制，所以要求先探针，并把它定位为替代（删掉免补读豁免），而不是叠加。
- **cross-check 关键词**：grep 了 essence 当前卷与 2026-H1 卷中上述 9 个 slug，全部命中（例：`one-shot-invariant…` essence.md:2、`separation-need…` 2026-H1:3）。

## essence 候选（可选）
- 无。本轮洞察全部可以由既有滴组合推出，不制造噪音。

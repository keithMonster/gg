---
date: 2026-09-04
slug: skill-notes-quota-unit-and-evolution-split
summoner: monster（Claude Code 主会话，subagent 召唤）
northstar_reach: #3 决策超越直觉（把"演化块放哪"重定义为"配额计价单位错了"）
status: substantive-decision
---

# Reflection: skill-notes 载体的配额单位与演化卷下沉

### 给父会话的最终输出（必填）

**推荐**：三个问题的答案全部由一个上游决定推出——**把 skill-notes 的全部配额换成读者付账的单位（字节），行数配额整体废除**。
- Q1 → (a) `~/.agents/skill-notes/_evolution/<skill>.md`，同 basename；(c) git 历史保留为"压缩前全文"的冷层，与 (a) 互补不互斥；(b) 否决（污染「顶层一文件 = 一个 skill」不变量，被 glob 与 `ls` 误认成 skill）。
- Q2 → 升通用契约，但契约本体是**字节配额**，不是"超阈值即分离"。分离演化卷只是超额时处置菜单的第三项（压缩 / 出栈 / 下沉），26 个小文件不撞配额就零仪式，与 README L52 无张力。**禁止把 `_evolution/` 写成"超过即自动下沉"的默认泄洪口**——那会让主文件永远不必出栈。
- Q3 → (b)：主文件 = 必读区 + 各族「当前结论块」（含 n= / 出口状态 / 活触发器），演化块（被下一代证伪或吸收的中间代、逐 n 实例）下沉。硬规则：**活提案 / 活触发器只许在主文件**，这样 `[无出口提案]` 哨扫描面仍是主文件，`_evolution/` 被 glob 排除是设计而非侥幸。
- 数值：主文件 ≤ **20,480 bytes**（对齐 `skill-notes-read-guard.py` 自立的退役条件"全部 < 20KB"，同时 = 必读第 2 条的 cat 截断线；实测本文件 1.7 bytes/token，20KB ≈ 12k tokens，Read cap 一半）；必读区 **12 条 × 每条 ≤ 800 bytes**（两轴同时锁：行数配额被合行绕过、字节配额会被拆条绕过，只锁一轴必失守）；自由流水线 40 行 → 8KB 同步换单位。
- 传感器：`tripwire_check.py:1095` 改 `len(text.encode())`，加必读区逐条 800B 检查；`tripwire_selftest.py` `skill_notes_health_size` 的阳性 case 改造**一条 25KB 超长单行**（正是这次逃过哨的形态），200 短行 case 改为字节超额；docstring 里 53KB 陈旧数字更新。
- 顺手可见的漏：F2 已出栈却仍在必读 L11 占 2.3KB 且继续写 n=19——出栈动作没有从必读区撤行，配额此前没有牙的实证之一。

**理由**：README 自己的论断是"配额让留下有真实代价、自己产生方向反转"。但代价必须用读者付的币种计——读者付的是 token（∝ 字节），写者被量的是行，两次压缩把 306→149 行、53→118KB，是写者在自己控制的单位里"守约"。同一文件在 `guard_read_context.py` 被显式豁免（R2_EXEMPT），Read 直达 harness 25k cap，L66 截断（前 66 行 42,792 bytes）没有任何传感器看得见——哨的单位与读者的单位错位，哨恒绿。所以承重点不在"演化块落哪"，在配额币种。

**trade-off**：① `_evolution/` 是写多读少的冷卷，与 git 历史的差别只在可 `rg`（monster 检索充分性契约依赖 rg 面）+ 可继续追加 + 路径稳定；接受它长期不被 eager 读，不给它体积哨。② 字节仍是 token 的代理，中英混排文件比例不同（本文件 1.7 B/token）；20KB 是按最重的 done.md 标定，其他文件更宽松，可接受。③ `skill-notes-read-guard.py` 的 `SKILL_NOTES_RE = skill-notes/[^/\s]*\.md` 不匹配子目录路径——`_evolution/` 下的 cat 不会被拦；冷卷可能 >30KB，实施时扩 regex 或接受（建议扩，一行改动）。④ 未核验：20KB 下各族当前结论块是否装得下（F4/F5 现各 33/36KB，其中多少是"当前结论"要实测切分）。

**行动建议**（父会话执行，均在 harness 域自决范围）：1) 改 README 三处：形态段（三区 + 字节配额 + `_evolution/` 落点与"活提案不进冷卷"规则）、健康哨表（行→字节，加必读逐条 800B）、L100「处置不包括提高阈值」后追加"下沉不是泄洪，出栈优先级不降"；2) 改传感器 + selftest 阳性 case；3) 对 done.md 做一次切分：F4/F5 逐 n 实例与 F1/F3 演化行下沉 `_evolution/done.md`，F2 从必读撤为墓碑，切完 `wc -c` 贴回执；4) 扩 read-guard regex 覆盖子目录。

### 核心假设

- Read 工具 25k token cap 是硬边界，且 skill-notes 在 read-context guard 豁免（已实查 `R2_EXEMPT_SUBSTRINGS`）——若 harness 改 cap，20KB 数值需重标定，方向不变。
- 演化块的消费者只有"写 n+1 的那个我"和夜跑收割者，都不在开工前 30 秒——若将来有开工时读演化的需求，(b) 的切分会不够。

### 可能出错的地方

- 20KB 装不下 8 族的"当前结论块"，写者会把当前结论块也塞进必读 800B 内 → 事实上退化成 Q3(c)。这不算崩，是配额在做它该做的事。
- 字节被拆文件绕过（`done.md` + `done-extra.md`）——顶层一文件一 skill 的不变量要写进 README，哨可加"顶层文件名 ∉ skills 目录名"检查。

### 本次哪里思考得不够

- 未实跑一次切分估 F4/F5"当前结论块"真实字节数，20KB 是按物理边界（cat 截断线 / guard 退役条件）反推，不是按内容正推。
- 未读 `tripwire_selftest` 的 `w()` / `@case` 机制细节，行动建议里 selftest 改法是形态级不是行号级。

### 如果 N 个月后证明决策错了，最可能的根因

冷卷 `_evolution/` 变成第二个 write-only 堆积场且无人再读，届时会发现"演化本身有价值"（README #4）的价值只兑现在写入当下的对比动作里——那时正确的收口是把 #4 改成"写 n+1 前必须 Read 冷卷该族"这种激活机制，而不是再动载体。

### 北极星触达

#3：父会话把问题框成三选一的落点问题，裁决把它翻成配额币种问题；三问成为推论。

### essence 对齐自检（必填）

- **对位**：`gate-as-physical-fuse-not-business-metric`（配额是保险丝、按物理边界定值）、`anchor-value-in-activation-not-in-content`（冷卷价值在写 n+1 时被激活，不在内容存在）、`metric-is-a-claim-not-a-fact`（行数哨恒绿是一个声明不是事实）、`the-machine-watchers-immunity-is-purchased-by-amnesia`（哨看不见的截断）。
- **反着走**：`hardening-exemption-covers-thickness-not-existence` 潜在张力——我在加第二道配额（800B/条）而不是问"必读区该不该有 12 条"；未展开。
- **cross-check 关键词**：quota / metric / threshold / truncat / sensor / watchdog / 配额 / 恒绿 / currency（essence.md + essence/2026-H1.md + consolidation/essence-view.md，grep 实跑）。

### essence 候选（可选）

- slug: `quota-in-the-readers-currency`
- 一句话: 配额只在"写者被量的单位 = 读者付账的单位"时才产生方向反转；单位错位时写者会在自己的单位里守约而读者照付全价，哨恒绿（skill-notes 行→字节，306→149 行 / 53→118KB 活体）。
- 是否已 append 到 essence.md: **Y——2026-09-04 auto_gg 当夜补审 PASSED-WITH-EDITS 采纳入库 essence #234**。入库文本以 evaluator 修改稿为准：核心条件从「单位相等」改为「单调耦合 + 写者无便宜解耦动作」，补判别一问与前提栏。**最强反驳**：① 「哨恒绿」为假——`meta_audit_history.jsonl` 显示 `skill_notes_health` 08-21→09-02 连续 13 夜红、09-03 起绿，真实形状是「红→写者合行在自己单位达标→绿，读者账单 118KB 没动」，比原句更强地支持核心律但原句写错；② 「两次压缩把 53→118KB」归因错——`~/.agents` git 逐 commit 重算：两次压缩各减字节（08-25 −49% / 09-02 −20%），翻倍来自压缩间隙塞行式增量（09-02→09-04 +2 行 / +10.4KB）；③ 核心句「=」自反——读者付 token、本裁决处方量字节，按原判据字节闸也不合格，monster `canon.md:25` 同律措辞「成本本身或它的单调代理」才对；④ 律非首发——`canon.md:25`（09-02 guard_claude_md_size 案）已含，本滴系 essence 域移植，谱系如实计价；⑤ 证据清单 4 项里 3 项是本会话自写复印（README L67 / docstring / canon 复发段）；⑥ 对位栏引了幽灵滴 `metric-is-a-claim-not-a-fact`（两卷零命中）。真净新增 = 1 律（对 essence）+ 2 事实。派单者抽核：fc6592f 149 行/48,742B、249d792 147/107,809B、f8cabaf 149/118,160B 与 evaluator 逐字一致；`SKILL_NOTES_MAX_BYTES` 在 :1029 属实。重算侧核 transcript：tool_use = Bash×26 + Read×16，写副作用命令模式零命中

### 外部锚点（可选）

- `~/.agents/skill-notes/README.md` ← 载体契约 SSOT
- `~/githubProject/monster/auto-monster/scripts/tripwire_check.py:1067-1107` ← 传感器
- `~/githubProject/monster/shared/scripts/guard_read_context.py:83` ← skill-notes 豁免

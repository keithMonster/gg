---
date: 2026-09-02
slug: cgboiler-stage3-vs-world-model
summoner: monster / cgboiler（架构主会话，双签契约）
northstar_reach: "#3 决策超越直觉（A/B/C 三选改判为 D）/ #1 二阶效应（看门狗守空房）"
status: substantive-decision
---

# Reflection: cgboiler stage3 线 vs world_model 线——拓扑定性 + 传感器改锚

### 给父会话的最终输出（必填）

**推荐：D——stage3 线不是「被取代」也不是「暂停」，它是 `WORLD_MODEL_SCHEMA.md §2.1` 迁移状态机里的 `legacy_authoritative` 权威读层，写侧已由目标层裁定冻结。** 父会话给的 A/B/C 三选缺了这一项；「偏 A」差一层。

**理由（物理证据）**：
1. 状态机已写死关系：`legacy_authoritative`=「现有实体卡 L1 + archive；旧 append/fold/merge 继续；ledger 不能发布覆盖卡片」；`ledger_authoritative` 机械不可达（`LEDGER_AUTHORITY_ENABLED=false`，migration.json transitions=0）。**旧卡片是当前唯一被读的东西**（Atlas / `cgboiler/people/*.md`，publish「一个字都不覆盖 people/*.md」）。A「封存」= 宣告一个状态机不允许的转换，把 SSOT 关进档案。
2. 写侧没有任何合法重开条件：plist 不恢复（Keith 08-21 目标层）；Batch2 已于 08-20 我裁决时重定义为 world_model；handoff 写「恢复只能作为消费端重新开跑的自觉后果」，而 world_model 消费端是 assertion 抽取（PRINCIPLES §6 会话直读，不能无人值守）→ B「⏸ paused until X」的 X 不存在，写它 = 造一条永不到期的挂链，正是 08-11 拆掉的形状。
3. C 启动旧 Batch2：决策内参 462 条已在 world_model notes evidence 全量内（`person:cgm-888888` 1358 条，RUNBOOK §6 known limitation 明写「修之前不纳入抽取批次」）；抽取范围 status==1 由 Keith 09-01 拍。再往 legacy 层写 fact = 双轨写同一事实，且写进将被 publisher 重建掉的层。
4. inquiry layer / fold 收口的等价物（父会话未核实处）：**inquiry 有**——`adapters/assistant_chat.py` 已把 legacy inquiry dump 升级为 canonical + receipt（3 Human 终态，coverage partial dual closure）；**fold 无也不需要**——fold 是对 append-only 主卡的瘦身，assertion 模型里卡片是 read model 重建物、时态在 assertion 上（`business_time` / `supersedes` / `valid_to`），fold 这个概念随 append 通道关闭一起消失，不是缺口。

**PENDING 4 项处置清单**：
| 议题 | 处置 | 依据 |
|---|---|---|
| §4 Batch2 决策内参 | **关闭：被 world_model 吸收**。Batch3~5 按 type 分批的规模登记一并作废（evidence 全收、assertion 按覆盖增益排序，handoff #8 已降实现层）。唯一残留实质 = 888888/888886 合成账号 perspective→objective 的 normalize 来源判据，已在 RUNBOOK §6 known limitation，不另立 | RUNBOOK §6；thread L32 |
| §10 utility 固化 | **关闭：作废**。三脚本服务 note→fact→L1/L2 链；world_model 机械半边是 `extract.py prepare/mint`，L2 由 `publish.py` 重建。grep 实证 `world_model/` 零引用 `scratch_*`。scratch 两脚本留原位不删（PROGRESS/exec_reports 引为追溯锚） | grep 结果 |
| §19.3 近重复标记 | **迁移不关闭 → RUNBOOK §6 known limitation**。normalize 只处理「同 note_id 多版本」（`canonical_versions`），不处理「不同 note 重发同一周报」；A′ 判断（标记不丢弃、内容归首版、重发只留存在性）在 assertion 模型下更自然（重发 = 一条存在性断言）。触发改「周报 stratum 首次进 assertion 批次前」，不再是「Batch3 前」 | normalize.py:492；PENDING §19.3 |
| §6 memory-lab 升级 | **关闭：条件不可达，改挂 `inbox/topics.md`**。「连续 2 个 tick 周期零违规」——tick 永久停，条件永不满足 = 无时限挂链。⏰ 建议挂「world_model 首个 bounded slice 进 shadow_parity 之日」（这才是「工程实例硬通过」的物理判据）；到期动作 = 架构主会话重评路 A/B | PENDING §6 |

**PROGRESS.md 追加一条**（措辞不用「封存」不用「⏸」）：`[拓扑裁决] stage3 线定性为 legacy_authoritative 权威读层、写侧冻结：tick/fetch/extract 无合法重开条件；PENDING 4 项按 gg 清单结案；本文件自此不再是管线心跳源；读侧权威交接以 migration.json transition 为准`。STAGE3_STATE 的 `idle_complete` 不改（phase 是 tick 消费的字段，tick 不跑，改值无消费者），加一行注即可。辐射：`cgboiler/CLAUDE.md` 唤醒话术「川锅表征」行加「写侧已冻结」；`threads/cgboiler-self-model.md` 承重事实 + 关键历史各一条；`threads/cgboiler-world-model.md` 背景段「两台机器」补「那台 = legacy_authoritative 层，写侧冻结」。

**传感器判据一句话**：`cgboiler_pipeline_liveness` 改读 **world_model 三个「只在账本真长时才变」目录（`ledgers/` 铸/改断言、`interpretation_receipts/` 封批/修订、`manifests/` 新 capture）最近 git 提交日期取 max，距今 ≥14 天报警**；用 `_git("log","-1","--format=%cs","--",path)`（同文件 L187/L1609 先例）；**不读** `reports/`、`read_model/`（零新数据重跑 gate/publish 也刷 `checked_at`/`published_at`，是 mtime 同形假绿），**不读 PROGRESS.md**（legacy 层无写侧，新条目 ≠ 管线活着，且会让 legacy 空转掩盖 world_model 停摆）。三目录任一更新即活（抓证据/铸断言/封批三种进展不要求同时）。阈值 14 天不动（Keith「继续推进不设上限」下两周零进展就该报）。selftest 反向 case 改 mock `_git` 返 60 天前（`eval_version_ownership` case 已有 `tripwire._git` 注入先例）。报警文案加「先 `git status` 排除未提交」——本哨与 auto-commit 耦合，auto-commit 死则本哨也响，可接受。备选内容日期 = assertion `recorded_at`（schema 0.1 字段，drift 面更大，不作首选）。

**trade-off / 未核验**：① 我没跑 `resolve_migration_record` 实证「legacy 卡当前被 query 层消费」，判断来自 SCHEMA 状态机 + README「一个字都不覆盖」文字；② §19.3 是否在某个 amend/rejudge 路径里已被顺手处理没有全量 grep（只 grep 了 near_duplicate/canonical_version/多版本）；③ git-date 心跳假设 auto-commit 持续入库。

### 核心假设
旧线卡片仍是唯一权威读层且无人会绕状态机直接往它写——若有人以「跑 exec tick」重开写侧，本裁决的「写侧冻结」只是文字，靠 cgboiler/CLAUDE.md 话术表挡。

### 可能出错的地方
把 §6 改挂 shadow_parity 到达日——若 shadow_parity 因 query 闸 blocked-by-design 长期不可达，这条 ⏰ 会在 inbox 里再长成挂链；到期动作必须是「重评」而不是「等」。

### 本次哪里思考得不够
没有量化「传感器改锚后首个 14 天窗口内 world_model 是否有进展」——若 09-01 后本就进入等 production reconcile 授权的静默期，新哨上线即报，父会话要预判这一发是真阳性（该催 reconcile ack）而非误报。

### 如果 3 个月后证明决策错了，最可能的根因
world_model 的 publisher 迟迟不能重建卡片（roundtrip / write guard 未落地），legacy 层被迫重开写侧补新事实——那时「写侧冻结」成了阻塞业务的教条，应改为 bounded_slice 级的双轨过渡而非全局冻结。

### 北极星触达
#3：A/B/C 三选拒答改 D，状态机而非选项表定关系；#1：看门狗守空房的二阶坐标（父会话把报警读成「旧线该处理」，真相是「哨没跟着被看守物迁移」）。

### essence 对齐自检（必填）
- **对位**：`one-shot-invariant-decays-under-live-append`(08-11，本哨的出生滴)、`the-premise-expired-without-a-diff`(08-30，「PROGRESS=心跳」前提在 08-19 world_model 开工那天零 diff 失效)、`watchdog-topology-lacks-a-top`(07-03)、`omission-failures-evade-event-driven-sensors`(07-28)、`idle-threshold-as-tripwire-not-answer`(05-14，14 天不动)、`decision-execution-gap`(04-21，§4/§10 拍了 4 个月没接)、`separation-need-is-not-topology-verdict`(08-20 同案)。
- **反着走**：潜在张力 `premature-abstraction-tripwire`——候选滴暗示「传感器登记应带被看守物指针 + 迁移条款」，我把它压在 docstring 层、不建登记表字段，n=1 不造机制。
- **关键词**：watchdog / liveness / stale-observer / omission / one-shot-invariant / premise-expired / idle-threshold / decision-execution-gap / migration / legacy / paused。

### essence 候选（candidate-unverified，未 append）
- slug: `stale-watchdog-fires-true-on-the-wrong-organ`
- 一句话: 被看守物迁移而哨未迁移时，哨不会静默——它继续真阳性报警但诊断文案指向尸体（本案：报「stage3 停摆」、诱导选项 C 重启旧线），比静默更危险，因为真阳性买来了对错误病灶的处置权；哨登记须绑定被看守物指针并在其退役时翻转。【前提：哨读的是对象私有心跳（PROGRESS.md）而非域级心跳；n=1】← #227 premise-expired 的「非静默」变体：前提失效未静默降格，而是把报警复用到旧诊断上。
- 物理证据：`tripwire_check.py:1159-1203` docstring 全篇 stage3 语义；`git log` PROGRESS 08-13 vs world_model 四目录 09-01；父会话 prompt 把选项 C 列为候选。
- 是否已 append: **Y——2026-09-04 auto_gg 补审 PASSED-WITH-EDITS 采纳入库 essence #233**（原定 09-02 夜补审，该夜会话 429 塌缩顺延两天）。入库文本以 evaluator 修改稿为准，核心机制改为「私有心跳冻结 ⇒ 谓词饱和 ⇒ 读数退化为退役挂钟、诊断沿用旧文案」。**最强反驳**：① 「真阳性」措辞复犯 #223 被击穿过的前提泄漏——对哨谓词真、对诊断（「cgboiler 管线停摆」）为假阳，world_model ledgers 08-21/26/27 有提交、08-27 首响当天域活着；② 「比静默更危险」零对比证据且记录反向（静默期两月 173 条违反 vs 本案 6 天归位零误动作）；③ 「诱导选项 C」过强——`inbox/closed/2026-09.md:40` 三选一已含正确解 ③；④ 处置句「登记绑指针」已被 06-15 / 08-14 + monster `inbox/README.md:54`(08-26) 含住，且与本档「反着走」段自述「压在 docstring 层不建字段」矛盾；⑤ 证据描述失真——旧 docstring 全文零 `stage3` 字样。真净新增 = 1 律（谓词饱和）+ 1 事实。evaluator 自陈一处偏离：`git show > /tmp/twc_old.py` 落盘读旧版——派单者裁**不作废**（两仓零写入、evaluator 独立性未损），依赖该文件的反驳 ①⑤ 已由派单者管道零落盘复核（`git show b092b8d5:… | sed -n '1159,1203p'`：stage3 0 命中、:1201 文案属实）。派单者重算侧核 transcript：tool_use = Bash×19 + Read×1

### 外部锚点
- `~/githubProject/monster/cgboiler/_pipeline/world_model/WORLD_MODEL_SCHEMA.md` §2.1 迁移状态机
- `~/githubProject/monster/cgboiler/_pipeline/PENDING_DECISIONS.md` 「当前未闭议题（2026-08-13）」
- `~/githubProject/monster/auto-monster/scripts/tripwire_check.py:1159` / `tripwire_selftest.py:2126`

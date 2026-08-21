---
date: 2026-08-21
slug: cgboiler-evidence-retention-contract
summoner: monster（cgboiler 世界模型 evidence artifact 保留契约缺口，后台会话）
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: evidence 保留契约——「保留多久」是类型错误

### 给父会话的最终输出（必填）

**裁决三条：① evidence 留 git 仓内，现状转正为显式契约；② 保留期 = 永久（与 receipt 谱系同寿），「有限窗口 + 降级 attestation」在类型层出局；③ 两个传感器落 tripwire_check.py + selftest 反向 case。另有一颗冻结前必须拆的实弹：snapshot_store.py manifest 存绝对路径，换机器即全断。**

**核心 reframe**：「保留多久」这个问题本身是类型错误。在 replay 型审计系统里，artifact 的寿命不是时间参数，是 receipt 的类型属性——replay 闸之所以是 replay（昨日裁决的判别问句「它重算了哪一侧？」），前提是被重算的那一侧物理存在。删 artifact = 把该 receipt 从 replay 降级为 attestation（「当时算过」的操作者声明）= 从仓库后墙重新凿开 2026-08-20 刚封死的那扇门，且是对全部闸批量凿。所以问题 2 没有参数空间，只有一个类型正确解。

**裁决 1（存哪）：git 仓内，现状转正。** 物理证据链：

- `contracts.py:565-567` binding 已锚死仓内相对路径（`is_relative_to(root)` 越界即拒）——契约已隐含仓内。
- `load_legacy_inventory` 用 `git cat-file -e {commit}:{card_ref}` 验证冻结 commit ——**系统已经在把 git 本身当 immutable capture root 用**。git 的内容寻址与 snapshot_store 的内容寻址同构；push 到 origin（github keithMonster/monster）即天然异地副本，换机器 clone 即全量恢复。
- 既成事实：`cgboiler/_pipeline/data/` 254MB / inquiry 97 文件已 100% tracked（git ls-files 97=97）。「进不进 git」是伪问题，真问题是「要不要显式承认并守护」。
- 「进了历史删不干净」不是代价，是这个系统花七个闸想买的性质——审计链恰恰要求删除有摩擦。
- reject 仓外目录 + 仓内 manifest：准入三问②直接答不出（没有任何机制守护 `~/some/dir`，Time Machine/换机/清磁盘的首选牺牲品）；且要改 binding 契约。
- reject git LFS：LFS server 可 prune 旧对象（保留反而更弱）、换机需装 LFS、把不可变性外包给 GitHub 存储政策。
- 体积核算：pack 572MB；正式跑（794 卡/8K L1/五来源）文本增量估 1-2GB 级，JSONL 经 git zlib+delta 压缩远小于原始体积；当前最大单文件 12MB，远离 GitHub 100MB blob 硬限。契约加一条「单 artifact 落盘分片 ≤50MB」防未来单批超限。体积真爆（pack >5GB）的出口是 evidence 专用裸仓/仓分体，届时过冻结变更闸——现在不预设计。

**裁决 2（保留多久）：永久。** 「过期标记为不可重放」也 reject 作为常规出口——那是把断链合法化。唯一合法删除路径 = **整条谱系显式退役**：artifact + 引用它的 receipt + 派生 assertion 同批 tombstone，消费端对应子句降级 unverifiable 且显式展示，退役属冻结变更闸级动作。v0.1 不建退役机制（YAGNI），契约里写死「永久保留；未来退役须过冻结变更闸」一句话即可。

**裁决 3（传感器）：两个。**

- `world_model_binding_replayable`（主）：夜巡扫全部 snapshot manifest JSONL + gate report/receipt 的 `{artifact_ref|path, sha256|content_hash}`，逐条验「存在 + hash 逐字节一致」。本质 = 把消费时的惰性 replay 提前为主动巡检，正面解「只在下次消费才炸」的假绿形态。成本：sha256 全量 254MB 秒级、2GB 十几秒，夜巡可承受。
- `world_model_evidence_gitguard`（薄）：① `git check-ignore` 对 evidence 根必须非 0；② `git ls-files` 计数 vs 磁盘文件数 vs manifest 记录数三方对账（防 `git rm --cached` 静默摘除）；③ evidence 路径下 untracked 文件驻留超 N 天报警（capture 未 commit = 只活在本机，换机即断）。
- selftest 反向 case：沙箱 fixture manifest 指向已删/已改文件 → binding_replayable 必须报阳；模拟 ignore 规则命中 fixture 路径 → gitguard 必须报阳。实现细节（文件名/沙箱方式）是实现层，父会话自拍不必回来。

**附加实弹（冻结前免费修改窗口，必须本次修）**：`snapshot_store.py` 的 manifest record `path`/`source_path` 存 `resolve()` 绝对路径（`/Users/xuke/...`），`verify_snapshot` 按绝对路径读——换机器即全部快照验证断裂，与 contracts.py 相对路径契约自相矛盾。manifest 当前 0 条生产记录，改 repo-relative 零迁移成本；冻结后改就要过变更闸。同步改 `test_snapshot_store.py`。

**落点清单**：① `DATA_RUNBOOK.md` 新增「Evidence 保留契约」节（落点选它因为数据会话操作者是保留规则的读者）：落盘位置 = 仓内 capture root、入 git、永久保留、禁 gitignore/禁 git rm --cached、单 artifact ≤50MB、删除唯一路径 = 谱系退役过冻结变更闸；② `WORLD_MODEL_SCHEMA.md` 状态机段补一句互指「receipt 可重放性依赖 evidence 保留契约」；③ 两传感器进 `auto-monster/scripts/tripwire_check.py` + `tripwire_selftest.py` 反向 case；④ snapshot_store.py 相对路径修正。机制文件变更若按 handoff 判据触发异谱系审则照跑。

**边界回应**：问题 1/2 是承重墙（存储拓扑 + 审计链语义，选错难回退），受理正确不收回；问题 3 的具体落点是实现层，方向已给、细节父会话自拍。

### 核心假设

「正式数据会话的文本量级在 1-2GB 级」——由 inquiry 205MB（部分覆盖）外推，无人真算过五来源全量。若实际到 10GB+，裁决 1 的「不预设计仓分体」要提前兑现，但保留语义（裁决 2）不变。

### 可能出错的地方

git 作为 immutable store 的隐藏敌人是 **history rewrite**（filter-repo / 强推）——本裁决没有给防强推的传感器（GitHub 侧 branch protection 是外部配置，monster 是个人仓未必开）。若未来有人 rebase 掉含 evidence 的历史 commit，`git cat-file -e` 类验证会断。缓解：evidence 靠工作区文件 + hash 验证（不依赖历史 commit 存在），只有 legacy inventory 冻结 commit 验证依赖祖先链——已在其 reachable_check 中会显式报错，断了能被发现。

### 本次哪里思考得不够

未读 handoff §9 原文与 v0.1 冻结闸的精确变更判据（grep README/SCHEMA「异谱系/变更闸」零命中，判据可能在别处）；「机制文件变更是否触发重审」交由父会话按其冻结契约判。

### 如果 2 个月后证明决策错了，最可能的根因

体积外推失准：把「文本 + git 压缩」的先验套在了可能含二进制附件（图片/文件消息 dump）的来源上——若 assistant_chat 来源含媒体文件，量级和压缩率两个假设同时失效，git 仓内策略被迫提前重议。

### 北极星触达

触达 #3：没有在「永久 vs 有限窗口」参数空间里作答，而是判定问题 2 无参数空间——artifact 寿命是 receipt 的类型属性，删除即闸型降级，与前日 query 闸裁决合并为同一条类型公理的两个投影。

### essence 对齐自检（必填）

- **对位滴**（均实际 cross-check）：`attestation-has-no-fixed-point-under-self-audit`（#211，08-20——本裁决是它在存储时间轴上的推论）、`physical-anchor`（工具返回/物理存在是唯一穿透范式层的信号——evidence 物理存在即 replay 的物理锚）、`mechanical-gate-needs-machine-detectable-target`（06-24，传感器设计依据：保留契约必须有机器可检测目标才不是漂移债）、`evaluator-input-ownership`（05-19，仓外目录方案 reject 的深层：无守护者的输入端 = 无主）。
- **反着走**：无。
- **cross-check 关键词**（物理证据）：attestation / replay / gate / physical / anchor / evaluator（grep essence-view 命中）。

### 沉淀

候选滴 `replay-gate-collapses-to-attestation-when-inputs-expire`（candidate-unverified，工作模式无 Agent 开不了证伪审，交夜巡/设计模式补审）：

> replay 闸的类型不由它自己的代码决定，由它输入的保留契约决定：输入可被清理（无保留契约/有限窗口/仓外无主目录）的 replay 闸，在时间轴上必然塌缩为 attestation——重算无对象时，receipt 只剩操作者当年的声明。故审计系统的「retention policy」不是运维参数而是闸型参数；问「证据保留多久」等价于问「验证闸允许在多久后降级为自签」。#211 的时间轴推论：判别问句「它重算了哪一侧？」需补一问「那一侧十年后还在吗、谁守着？」。
>
> 物理证据：monster cgboiler world_model——七闸 replay 架构完备（contracts.py binding 逐字节重验），但仓内 retention/保留/清理零命中，254MB evidence 已 tracked 却无任何契约守护，一条 .gitignore 即可把全部闸静默降级。近邻滴 #211（attestation 无不动点）——净新增点是「闸型由输入存储契约决定、可随时间塌缩」这一时间维；若证伪员判定被 #211 + physical-anchor 组合覆盖则降级为应用实例存档。

**验证关 verdict（auto_gg 2026-08-21 夜补审）**：PASSED-WITH-EDITS 采纳入库（essence #213）。裁决：非 #212 同义反复——#211/#212 病灶全在对抗性供给轴，本滴病灶在非对抗性存续轴（无攻击者，.gitignore/换机即塌），且「retention=闸型参数」产出 #211/#212 推不出的操作性决策（永久保留类型层锁死、唯一合法删除=整谱系 tombstone）；恰落 #207「账本层看守不在射程」+ `watchdog-topology-lacks-a-top` 敞口。**最强反驳点**：核心句有被读成 #211 一步解析推论的风险（「哪侧都没重算=自签」+「对象没了没法重算」近乎定义推演）——净新增须钉死在「非对抗退化路径 + retention=闸型参数」上，否则是 #211 换皮；「必然塌缩」系 n=1 类型推演，已进前提。**3 处证据订正**（均不翻案）：① 证据路径实为 `_pipeline/world_model/contracts.py`（非 scripts/lib/）；② 「retention 零命中」是裁决时刻态——DATA_RUNBOOK §1.5 保留契约已按本裁决落地且措辞「类型层出局非参数权衡」，由缺口转为最强物理锚；③ snapshot_store.py 绝对路径实弹已修（commit 90d045ef，root-relative），入滴时标历史态。evaluator tool_use 11 次全只读（Read/grep/sed/find/git log），派单者事后核一行留此。

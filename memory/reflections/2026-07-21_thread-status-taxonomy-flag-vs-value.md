---
status: substantive-decision
slug: 2026-07-21_thread-status-taxonomy-flag-vs-value
date: 2026-07-21
mode: work
summoned_by: monster (thread-status-governance brief)
tags: [data-model, taxonomy, ssot, orthogonality, reversibility, monster-threads]
---

# thread status taxonomy：旗标 vs 升值（A）+ closed 扶正（B）

## 决策对象
monster thread 记忆的 `status` 字段 taxonomy 形状。两耦合子问：A = "live 但结构性安静"用旗标（dormant_ok）还是升成正式 status 值（maintained/dormant）；B = 成功终态 closed 扶正还是映射。

## 核心假设（可证伪）
- 假设 status 的**完整机器消费闭包只区分 `active` / 非-active 一个 bit**（sync render/staleness/count + tripwire fake_active 全部只 `== active`）。若存在某脚本对 paused/shipped/abandoned/closed 分别 branch，A/B 的迁移成本模型全变。→ 已 grep 全仓消费方物理证伪：无一处区分非-active 值。
- 假设 `active+dormant_ok ⟷ maintained` 是**信息等价的双向映射**（同一 active-bit × quiet-bit 的两种编码，非有损 schema 变更）。若 maintained 承载了 dormant_ok 之外的信息，等价性破。→ 核对：dormant_ok 唯一作用是 tripwire 豁免，不改可见性；映射是纯 relabel bijection。

## 给父会话的最终输出

**裁决：A1（dormant_ok 保持旗标）+ B1（closed 扶正，退化为文档对齐）。**

### A —— A1（旗标），但理由要从"成本"升级到"kind 错配"

父项目把 A1 当"MVP / 最小改动 / 不付 taxonomy 洁癖税"——这是**成本框架**，它低估了自己的直觉。真正的理由是**建模正确性**：A2 才是被错误建模的那个，A1 不是"便宜但不够干净"，A1 是对的模型。

判据链：
1. **status 从来不是 taxonomy，是一个机器 bit（`在 live 索引里吗？`）+ 挂在 not-active 侧的人类标签袋。** 运行时从不区分 paused/shipped/abandoned/closed（已物理核验消费闭包）。所以"旁标 vs 升值"的可见性维度是伪命题——active 和 active+dormant_ok **都可见**，dormant_ok 唯一改变的是**告警（tripwire fake_active 豁免）**，不是可见性。
2. **A 的真问题因此是：告警豁免该是 status-值还是 tag？** 而告警豁免是**传感器调参**，不是**生命周期位置**。判 flag/enum-value 的刀：这个属性**沿单调生命周期移动（active→paused→终态）→ enum 值**；还是**修饰一个会增殖的传感器集 → tag**。dormant_ok 的全部职责是修改一个 sensor 的行为，它是 tag。
3. **传感器增殖是实况不是假设**：`detect_state_staleness`（sync :297）已是第二个 per-thread、只跑 active 的传感器，将来同样可能要 per-thread 豁免。第二个豁免出现时，单轴 status 被迫枚举 `active / maintained / active-but-exempt-from-X`（cross-product 爆炸）；tag 命名空间把它吸收成又一个 flag。把第一个豁免折进 enum = 给第二个豁免关掉干净的门。对应 essence `safe-default-by-whitelist-inversion`：安全/正确来自极性方向，不来自枚举完备。
4. **可读性反而站 A1**：系统整个目的是对未来模型可读。`dormant_ok: true` 是**自证函数的命名 flag**；`maintained` 是**不透明值**，其"告警豁免"含义埋在 spec 里。命名 flag 比不透明 enum 值更可读。
5. **可逆性去升级焦虑**（essence `reversibility-not-permission` 的应用）：父项目升 gg 的理由是"选错难回退（迁 21 文件）"。但 `active+dormant_ok ⟷ maintained` 是**信息等价的双向 relabel**，一个 20 行脚本随时来回，不丢信息。这不是单向门。→ 正确 meta-move：选此刻零成本、今天就工作、且 A1→A2 永远免费可用的那个（A1），把"更干净的单轴"推迟到有 forcing function（如 v1 记忆系统重构，届时反正在动全部文件、迁移搭便车免费）。YAGNI：A2 的唯一真收益（读一个字段不读俩）边际且罕见兑现（只在人工审 dormant thread 时付，且 flag 自证），却要现在付具体迁移+回归风险。

**monster_insight 的 `dormant` 化石不构成 A2 先例**：那是 stale dashboard 的 aspirational 词汇（`{active,dormant,archived}` 既不匹配 README 也不匹配 lint，全靠 `.get(...,·)` 兜底），是**词汇未被 pin 就漂移**的证据（essence `stale-observer` / `count-legitimacy-is-tense`：stale observer 的值读作史不读作现状），恰恰反证 hazard #1，不是 A2 的半个落点。别让一段死代码的臆想词汇拉动数据模型裁决。

### B —— 确认坍缩为文档对齐（不是待裁决策）

你的辐射纠正对：lint STATUS_ENUM 2026-06-11 已机器强制含 closed，:111 真拦非枚举值。closed 早已是合法值，只有 README:70 人类注释漏同步。**B 不是"要不要加第 5 值"，是"两个已分歧的 legality-SSOT 该以谁为准 + 消除分歧"。** lint 是 enforcing SSOT，已定；README 是漏更的文档。→ 直接文档对齐。

**你问的"终态语义重叠该不该合并 closed"——我判：不合并，四终态各承独立人类-actionable 语义。** 机器四值同构，但人类叙事四值不同构：shipped=产品交付（会被当 win 引用/可能复活）/ abandoned=失败弃（含悔意，不复活）/ closed=善终了结（协议/决策/概念干净收口，非产品非失败）/ paused=暂停（会回来）。miscategorize（生日歌塞 shipped、协议了结塞 abandoned）会让 win-log 说谎、情绪/战略读错。零机器成本保留最大叙事保真 = B1 正解。B2 更糟：它得**反向撤销 06-11 的 lint 决定**（从 enum 删 closed），是主动 un-decide。

## 执行修正（注入父项目 plan 的两个盲区——这是本裁决的承重附加值）

**盲区 #1（根因未命名）：三套 taxonomy 并存 = 本次要修的 status drift 的真根因，而父 plan 的修法在制造第三份手抄枚举。**
- README:70（4 值，漏 closed）/ lint:45（5 值，enforcing）/ monster_insight（3 值 aspirational `{active,dormant,archived}`）——同一 enum 三处手抄、互相分歧。
- 父 plan「改 README 补 closed+dormant_ok」= 再造一份手维护副本 = **加 drift 面还自称治 drift**。这违反 monster 自己的外化锚点/SSOT 单源原则（对应 gg essence `ssot-as-loadable-fragment` / `runtime-state-vs-business-data-distinct-ssot-domains`）。
- **修正**：**指定 lint_thread_format.py:45 STATUS_ENUM 为 status legality 的唯一机器 SSOT**；README **不再内联复述值列表**，改写"合法集由 lint_thread_format.py 强制，见该处"（内联复述 = drift 源）。monster_insight emoji map 统一到同一真值集（你已认领）。三处收敛到一处 enforcing + 两处引用。

**盲区 #2（无约束 flag 会腐）：dormant_ok 无合法组合校验。** 没有任何东西阻止 `paused + dormant_ok`（静默无意义）。无约束 flag 的漂移正是将来有人说"flag 太乱，改单轴吧"的口实——预先堵掉。**修正**：spec 明写"dormant_ok 仅对 active 有意义"；lint 加一条 warn（dormant_ok 出现在非-active thread 上）。这让 A1 的 flag 模型自带护栏，抵消 A2 唯一的真论点（非法组合空间）。

**次要（诚实标注，非阻塞）**：阈值 30→90 后，fake_active 传感器实质变成"逾期未转 paused 检测器"（>90 天 still active 且非 dormant_ok = 该 paused 没 paused），非"假活"。考虑改名以名实相符——你自己拍，不升 gg。

## 可能出错的地方
- 若未来 monster 真长出"paused 态也要区分 quiet-by-nature"的需求（生命周期终态也要带 nature bit），则我判"终态 nature 属性 moot"会被推翻，A1 的正交论证需重估。当前物理事实：终态一律不告警，nature bit 在终态确实 moot——但这是当前传感器集的性质，非永恒。
- SSOT 指定 lint 为准，前提是 lint 一直是 status 唯一 enforcing 校验器。若将来别处新增 status 写入校验，需回到此裁决把新校验也指向 lint SSOT（辐射检查义务）。

## 推理盲区
- 我只核验了 monster 仓内 shared/scripts + auto-monster/scripts + .claude 的消费方。若有**仓外**（别的 project、cron、cc-connect）读 thread status 值，未覆盖。判据：thread status 是 monster 内部记忆字段，外部消费概率低，但未物理排除。父项目执行时应 grep 一次跨仓引用兜底。

## 根因预判
status drift（本次 3 洞）的根因不是"阈值没对齐"也不是"closed 是野值"——是**同一枚举被三处手抄、无单一 enforcing SSOT**。不指定 SSOT，修完这次、下次加值/改值照样三处分歧复发。阈值/closed 都是症状，SSOT 单源是根治。

## 北极星触达
#1 二阶洞察：把"旁标 vs 升值"（父项目的一阶成本框架）重定义为"sensor-exemption tag vs lifecycle enum-value 的 kind 错配"——A1 不是便宜妥协，A2 是错模型。Keith 看完应想"我把 A1 当次优解了，其实它是正解"。
#3 决策超越直觉：可逆性 relabel 的识别把"难回退的架构门"降级为"随时可换的表示选择"，去掉升级焦虑。

## essence 对齐自检
- `reversibility-not-permission` (05-06)：grep 确认在视图 F8。用于把迁移成本从"不可逆门"降级为"可逆 relabel"→ 选便宜-now、保 A2-later 可用。✅ 一致
- `safe-default-by-whitelist-inversion` (05-19)：视图在册。用于"正确来自极性/结构方向，不来自枚举完备"→ 支持豁免留 tag 不枚举 cross-product。✅ 一致
- `ssot-as-loadable-fragment` (05-08) / `runtime-state-vs-business-data-distinct-ssot-domains` (05-20)：视图在册。支撑盲区#1 的单-SSOT 指定。✅ 一致
- `falsification-as-structure-not-just-skepticism` (06-29)：视图在册。落地为补集采样——我枚举了 A3（把 flag 泛化成 tag 命名空间 `sensors_exempt:[...]`）并证伪为投机 YAGNI（今日只一个豁免，第二个出现才 promote），非直接接受父项目二选一。✅ 一致
- 对齐度：高。无与既有滴冲突。

## essence 候选滴（candidate-unverified —— 工作模式无 Agent，开不了 fresh 证伪审）
- **slug**: `sensor-exemption-is-a-tag-not-a-lifecycle-value`
- **候选全文**：判一个属性该做 enum 值还是旁标 tag 的刀 = 它**沿单调生命周期移动（→enum 值）**还是**修饰一个会增殖的传感器/校验集（→tag）**。传感器增殖，把第一个豁免折进 lifecycle enum 会逼后续豁免走 cross-product 枚举；tag 命名空间线性吸收。附识别帧：当一个"状态字段"的机器消费闭包只区分一个 bit、其余值全是人类标签时，围绕人类值的 taxonomy 争论是文档问题不是数据模型问题。
- **物理证据**：monster threads_sync + tripwire 消费闭包 grep（全部 `==active`，零非-active 分支）；detect_state_staleness 是已存在的第二 per-thread 传感器；dormant_ok 唯一作用是 tripwire 豁免不改可见性。
- **相关既有滴**：`safe-default-by-whitelist-inversion`（反枚举同族，但那条讲安全极性，本条讲 flag/enum 建模刀，是新维度）、`runtime-state-vs-business-data-distinct-ssot-domains`（SSOT 辖域，正交）、`reversibility-not-permission`（表示选择的可逆性，正交）。
- **入库路径**：待 auto_gg 当夜或下次设计会话补 fresh 证伪审后决定入库/驳回。**不直接 append essence.md。**
- **【已结算 2026-07-21 夜 auto_gg】**：fresh-context 证伪审（general-purpose，纯只读 grep）判 **PASSED**，已 append `memory/essence.md`（模式=工作，日期锚 07-21）+ 同步 essence-view F7 + 分配表 #180 + 反向引力核归零。最强反驳点（留档）：第二行 cross-product/线性吸收半是 `safe-default-by-whitelist-inversion`(05-19) 换域复读，重量全在第一行建模槽刀 + 单-bit 闭包识别帧——那两处经物理 grep 坐实全卷缺席。本候选不再复提。

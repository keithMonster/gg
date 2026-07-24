# parked — 挂账清单（跨夜已知项，FOUND 只报增量）

> auto_gg SCAN 每夜 Read。存量挂账项不占 FOUND 槽位——只在**新增 / 状态变化 / 出口条件满足**时上报并回写本清单。
> 建立：2026-07-02 设计会话。成因：fable5 slug 连报 13 夜、canon 死链假阳性连报 7 夜（`cadence-as-symptom`：重复上报 = 缺跨夜状态记录器的症状）。
> 出口条件满足 → 条目移入「已结」节（移动不删内容——历史可溯）。

## 在账

| id | 首报 | 内容 | 状态 / 出口条件 |
|---|---|---|---|
| P-0720-nonfire-recur | 07-20 | **07-15 / 07-16 双夜 auto_gg 全暗**（无日志、无 commit；gg-explore 槽同期同暗——explore 档 07-15 后直接跳 07-18）。物理核：`git log 07-14..07-18` 该两夜零 gg 产出；07-16 07:19 的 plist 归档 commit(c699a0a) **不是成因**（客户端 routine 自 06-12 起即唯一执行者，plist 06-12 已 bootout）。**P-0707-nonfire 于 07-13 以"一次性未复发"结案属过早**——两天后即复发且连发两夜 | §5「连续 2 次同类问题」触发：已推 agenda `[RECURRING]` 交 Keith 查客户端调度根因（定时任务配置在 gg 权力边界外，gg 不自查不自修）。**出口**：Keith 定位根因并处置 / 或此后连续 14 个日历日无 **non-fire**。**07-24 加注**：07-23 的缺日志**不是 non-fire**（该夜 fired 且 committed 8a72baf，属独立子模式 collapse-before-log → 见 P-0702-missing-log），故本条 non-fire 计数 07-17→07-24 未断（07-17~22 有日志、23 fired、24 本夜） |
| P-0702-missing-log | 07-02（重开 07-24） | **auto_gg commit 无对应日志**。首例 06-13（commit ad2cd74 产 essence+agenda+tracks 却无 memory/auto_gg/2026-06-13.md）；**07-23 复发**（commit 8a72baf 只更 substrate 传感器节、无日志，`git log --all -- .../2026-07-23.md` 证从未 commit）。同形态第 2 次 → 按原结案条"复发则重开并按 §5 [RECURRING] 处理"重开。**顺带证伪暗夜哨前提**：哨假设"缺日志⟹non-fire"，07-23 反例（fired+committed 仍无日志）= 独立子模式，与 07-15/16 non-fire 两回事 | §5 触发：已推 agenda `[RECURRING]` 交 Keith 查根因（日志物理缺失可核；"从未创建 vs 创建后丢失"会话内不可判，疑似 session 生命周期——commit 后结束于写日志前，属 gg 权力边界外）。**07-23 实况仅存于 8a72baf commit message，日志永久缺失不补造**（`铁律2` 禁伪造）。**出口**：Keith 定位根因 / 或此后连续 14 个日历日无缺日志夜 |

## 已结

| id | 首报 | 内容 | 结案 |
|---|---|---|---|
| P-0626-cadence | 06-26 | cadence 哨 3a 积压 park（善后臂停摆判定，连续 7+ 夜 <60% 告警被延续） | 07-09 NW 缩编 blocked 池取消，哨随之作废（agenda 07-09 收口记录"cadence 哨随 blocked 池取消作废"）；07-13 出口条件永不再触发，2026-07-10 全面检查补账结案 |
| P-0615-slug | 06-15 | audit 命名违规 1：fable5 中文 slug（12 夜议题） | 07-03 体检 Keith 总体授权下 ASCII 化：改名 `2026-06-15_fable5-prompt-methodology-four-candidate-verdict.md`（夜巡 06-17 备选 slug）+ frontmatter slug 同步；判据依据 = 380 文件仅此 1 例中文 slug，既有实践已投票，不开豁免口子 |
| P-0625-canonlinks | 06-25 | audit 死链 8：canon-bugs.md / canon.md 跨项目相对路径假阳性 | 07-03 体检根治：check_deadlinks 加 monster 仓根第三解析基（真验证非豁免，monster 侧文件真丢照样报）+ 裸 backtick 文件名对全仓 basename 匹配（06-17 backtick 议题一并结）；实测活跃死链 11→0 |
| P-0702-missing-log | 07-02 | 06-13 夜有 commit（ad2cd74，产出 essence+agenda+tracks）但从未写 memory/auto_gg/2026-06-13.md——SCAN"本夜日志创建"违规一次 | ~~一次性事件未复发，记录即结~~；**07-24 复发重开**（07-23 同形态），见「在账」P-0702-missing-log 行 |
| P-0702-bets-firstrun | 07-02 | bets.md 押注结算首次进 SCAN——客户端定时任务在 gg 权力边界外，接入是否生效待首巡实证 | 07-03 夜核 07-02 日志 SCAN 段含 bets 消费记录（"B1-B5 到期日全在未来，全未到期不碰"）→ 接入生效，结案 |
| P-0707-nonfire | 07-07 | 07-06 evening auto_gg 槽未触发（单次 non-fire；同源观察：explorations 侧 07-07 名文件实为 07-08 00:26 产出，同时段调度抖动第二症状，产出未丢） | 07-13 出口条件满足：07-07~07-12 连续 6 夜均有日志（收尾断裂哨全 done）、无二次 non-fire，调度抖动为一次性未复发，结案。**⚠️ 2026-07-20 追注：本次结案过早**——07-15/07-16 双夜复发（见在账 P-0720-nonfire-recur）。教训同 substrate 第四相 n=2 条款：6 夜无复发也只是"未见复现"，`bug-shape-survives-fix` 的又一实例 |

# parked — 挂账清单（跨夜已知项，FOUND 只报增量）

> auto_gg SCAN 每夜 Read。存量挂账项不占 FOUND 槽位——只在**新增 / 状态变化 / 出口条件满足**时上报并回写本清单。
> 建立：2026-07-02 设计会话。成因：fable5 slug 连报 13 夜、canon 死链假阳性连报 7 夜（`cadence-as-symptom`：重复上报 = 缺跨夜状态记录器的症状）。
> 出口条件满足 → 条目移入「已结」节（移动不删内容——历史可溯）。

## 在账

| id | 首报 | 内容 | 出口条件 | owner |
|---|---|---|---|---|
| P-0707-nonfire | 07-07 | 07-06 evening auto_gg 槽未触发（无日志/无 commit；exploration 流正常，最可能机器/客户端该时段未运行，非 gg 缺陷）。单次 non-fire 不升级，记账供复发检测。**同源观察补账（07-10）**：explorations 侧 07-07 名文件实为 07-08 00:26 产出（自名 07-07，07-08 无文件）——同时段调度抖动第二症状，产出未丢，同门出口 | 07-13 前无二次 non-fire → 结案；复发 → agenda `[RECURRING]` 查调度器 | auto_gg |

## 已结

| id | 首报 | 内容 | 结案 |
|---|---|---|---|
| P-0626-cadence | 06-26 | cadence 哨 3a 积压 park（善后臂停摆判定，连续 7+ 夜 <60% 告警被延续） | 07-09 NW 缩编 blocked 池取消，哨随之作废（agenda 07-09 收口记录"cadence 哨随 blocked 池取消作废"）；07-13 出口条件永不再触发，2026-07-10 全面检查补账结案 |
| P-0615-slug | 06-15 | audit 命名违规 1：fable5 中文 slug（12 夜议题） | 07-03 体检 Keith 总体授权下 ASCII 化：改名 `2026-06-15_fable5-prompt-methodology-four-candidate-verdict.md`（夜巡 06-17 备选 slug）+ frontmatter slug 同步；判据依据 = 380 文件仅此 1 例中文 slug，既有实践已投票，不开豁免口子 |
| P-0625-canonlinks | 06-25 | audit 死链 8：canon-bugs.md / canon.md 跨项目相对路径假阳性 | 07-03 体检根治：check_deadlinks 加 monster 仓根第三解析基（真验证非豁免，monster 侧文件真丢照样报）+ 裸 backtick 文件名对全仓 basename 匹配（06-17 backtick 议题一并结）；实测活跃死链 11→0 |
| P-0702-missing-log | 07-02 | 06-13 夜有 commit（ad2cd74，产出 essence+agenda+tracks）但从未写 memory/auto_gg/2026-06-13.md——SCAN"本夜日志创建"违规一次 | 一次性事件未复发，记录即结；复发则重开并按 §5 [RECURRING] 处理 |
| P-0702-bets-firstrun | 07-02 | bets.md 押注结算首次进 SCAN——客户端定时任务在 gg 权力边界外，接入是否生效待首巡实证 | 07-03 夜核 07-02 日志 SCAN 段含 bets 消费记录（"B1-B5 到期日全在未来，全未到期不碰"）→ 接入生效，结案 |

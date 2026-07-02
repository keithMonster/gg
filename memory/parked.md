# parked — 挂账清单（跨夜已知项，FOUND 只报增量）

> auto_gg SCAN 每夜 Read。存量挂账项不占 FOUND 槽位——只在**新增 / 状态变化 / 出口条件满足**时上报并回写本清单。
> 建立：2026-07-02 设计会话。成因：fable5 slug 连报 13 夜、canon 死链假阳性连报 7 夜（`cadence-as-symptom`：重复上报 = 缺跨夜状态记录器的症状）。
> 出口条件满足 → 条目移入「已结」节（移动不删内容——历史可溯）。

## 在账

| id | 首报 | 内容 | 出口条件 | owner |
|---|---|---|---|---|
| P-0615-slug | 06-15 | audit 命名违规 1：fable5 中文 slug（12 夜议题） | Keith 拍字（保留豁免 or 改名） | Keith |
| P-0625-canonlinks | 06-25 | audit 死链 8：canon-bugs.md / canon.md 跨项目相对路径假阳性 | check_deadlinks 加跨项目路径豁免（设计模式议题，agenda 已有根因记录） | 设计模式 |
| P-0626-cadence | 06-26 | cadence 哨 3a 积压 park（善后臂停摆判定，连续 7+ 夜 <60% 告警被延续） | 2026-07-13 阈值回审 | auto_gg（07-13 夜） |
| P-0702-bets-firstrun | 07-02 | bets.md 押注结算今夜首次进 SCAN——客户端定时任务 prompt 在 gg 权力边界外无法直核，接入是否生效待首巡实证 | 07-03 夜核昨夜日志：SCAN 段含 bets 消费记录 → 结案；缺失 → FOUND 上报 [RECURRING] 接入断点 | auto_gg（07-03 夜） |

## 已结

| id | 首报 | 内容 | 结案 |
|---|---|---|---|
| P-0702-missing-log | 07-02 | 06-13 夜有 commit（ad2cd74，产出 essence+agenda+tracks）但从未写 memory/auto_gg/2026-06-13.md——SCAN"本夜日志创建"违规一次 | 一次性事件未复发，记录即结；复发则重开并按 §5 [RECURRING] 处理 |

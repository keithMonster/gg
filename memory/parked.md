# parked — 挂账清单（跨夜已知项，FOUND 只报增量）

> auto_gg SCAN 每夜 Read。存量挂账项不占 FOUND 槽位——只在**新增 / 状态变化 / 出口条件满足**时上报并回写本清单。
> 建立：2026-07-02 设计会话。成因：fable5 slug 连报 13 夜、canon 死链假阳性连报 7 夜（`cadence-as-symptom`：重复上报 = 缺跨夜状态记录器的症状）。
> 出口条件满足 → 条目移入「已结」节（移动不删内容——历史可溯）。

## 在账

| id | 首报 | 内容 | 状态 / 出口条件 |
|---|---|---|---|

*（空——2026-08-16 P-0720 结案后暂无在账项）*

## 已结

| id | 首报 | 内容 | 结案 |
|---|---|---|---|
| P-0720-nonfire-recur | 07-20 | **07-15 / 07-16 双夜 auto_gg 全暗**（无日志、无 commit；gg-explore 槽同期同暗——explore 档 07-15 后直接跳 07-18）。物理核：`git log 07-14..07-18` 该两夜零 gg 产出；07-16 07:19 的 plist 归档 commit(c699a0a) **不是成因**（客户端 routine 自 06-12 起即唯一执行者）。**P-0707-nonfire 于 07-13 以"一次性未复发"结案属过早**——两天后即复发且连发两夜。在账期间演化史：07-28 Keith 把三条 AI 任务迁回 launchd（原根因载体客户端调度整体退役，出口第一支以调度器更换形态发生）；此后三种基础设施层瞬断三次重置计数——07-30 认证层（CC OAuth token 失效 10.5h）、08-02 网络层（办公网 WARP 网关故障，三槽全灭连告警都发不出）、launchd 三次皆无辜按时 fired | **08-16 出口第二支满足：08-03→08-16 连续 14 个日历日无 non-fire**（本夜 fired 由 2026-08-16 日志即证）。逐夜加注链（07-24→08-15 计数史全文）留 git log 本文件历史。08-15 在案「出口判据疑问（第二支是否收窄为仅调度层 non-fire）」其前提『按现判据可能永不满足』被本次满足物理证伪，疑问自然消解、不推 agenda；复发（任一层故障致 auto_gg 槽 non-fire）按原条款重开并转 agenda `[RECURRING]` |
| P-0809-explore-coauthor-trailer | 08-09 | **explore 槽 commit 作者尾注纪律连违 14 天**：07-26 起全部 gg-explore commit（10+ 条，另 ce5289d 回填）带作者尾注，违 auto_gg §1.3（explore git 权同 auto_gg）；auto_gg 槽自身全程合规。根因 = exploration.md 仅「git 权同 auto_gg」一行指针、消息纪律未显式到场，harness 系统层主动指示追加尾注——到达帧的指令压过缺席的指针。08-09 已在 exploration.md git 权行补显式禁令；历史尾注不改写（禁 rebase）。另 08-09 commit 2557fb6 的 FOUND 摘要引用被禁字样本体自犯一次（引用即在场），此后涉此条一律用「作者尾注」指代 | 08-10 出口第一支满足：修复后首个 gg-explore commit c6f23a1 物理核（`git log -1 --format=%B`）**无作者尾注**——exploration.md 显式禁令首夜即压住 harness 默认，契约层修复有效。复发则重开并转 agenda（届时按原条款交 Keith 改 plist prompt） |
| P-0702-missing-log | 07-02（重开 07-24） | **auto_gg commit 无对应日志**（collapse-before-log 子模式，≠non-fire）。首例 06-13（ad2cd74）、07-23 复发（8a72baf）；同形态第 2 次重开并推 agenda `[RECURRING]`。07-23 实况仅存 commit message，日志永久缺失不补造（铁律 2）。逐夜计数链（07-24→08-07）在 git log 本文件历史 | 08-07 出口第二支满足：07-24→08-07 **连续 14 个日历日无缺日志夜**（07-30 / 08-02 两夜为 non-fire 形态归 P-0720 不计本条；疑似根因载体客户端 session 生命周期已随 07-28 迁 launchd 退役）。agenda `[RECURRING]` 条对应撤销；复发则按原条款重开 |
| P-0801-vol-split-settle-ptr | 08-01 | essence 分卷后 B4/B5 结算 grep 对象在归档卷 7 月段（勿只 grep 近空当前卷）；跨卷双路径 `memory/essence.md memory/essence/*.md` | 08-03 出口满足：B4/B5 结算完成（✅✅，verdict 落 bets.md；原定 08-02 因该夜网络故障全暗顺延一日）——结算脚本按双卷指针执行，归档卷 185/186 滴入解析，指针尽责 |
| P-0626-cadence | 06-26 | cadence 哨 3a 积压 park（善后臂停摆判定，连续 7+ 夜 <60% 告警被延续） | 07-09 NW 缩编 blocked 池取消，哨随之作废（agenda 07-09 收口记录"cadence 哨随 blocked 池取消作废"）；07-13 出口条件永不再触发，2026-07-10 全面检查补账结案 |
| P-0615-slug | 06-15 | audit 命名违规 1：fable5 中文 slug（12 夜议题） | 07-03 体检 Keith 总体授权下 ASCII 化：改名 `2026-06-15_fable5-prompt-methodology-four-candidate-verdict.md`（夜巡 06-17 备选 slug）+ frontmatter slug 同步；判据依据 = 380 文件仅此 1 例中文 slug，既有实践已投票，不开豁免口子 |
| P-0625-canonlinks | 06-25 | audit 死链 8：canon-bugs.md / canon.md 跨项目相对路径假阳性 | 07-03 体检根治：check_deadlinks 加 monster 仓根第三解析基（真验证非豁免，monster 侧文件真丢照样报）+ 裸 backtick 文件名对全仓 basename 匹配（06-17 backtick 议题一并结）；实测活跃死链 11→0 |
| P-0702-missing-log | 07-02 | 06-13 夜有 commit（ad2cd74，产出 essence+agenda+tracks）但从未写 memory/auto_gg/2026-06-13.md——SCAN"本夜日志创建"违规一次 | ~~一次性事件未复发，记录即结~~；**07-24 复发重开**（07-23 同形态），见上方 P-0702-missing-log 重开行 |
| P-0702-bets-firstrun | 07-02 | bets.md 押注结算首次进 SCAN——客户端定时任务在 gg 权力边界外，接入是否生效待首巡实证 | 07-03 夜核 07-02 日志 SCAN 段含 bets 消费记录（"B1-B5 到期日全在未来，全未到期不碰"）→ 接入生效，结案 |
| P-0707-nonfire | 07-07 | 07-06 evening auto_gg 槽未触发（单次 non-fire；同源观察：explorations 侧 07-07 名文件实为 07-08 00:26 产出，同时段调度抖动第二症状，产出未丢） | 07-13 出口条件满足：07-07~07-12 连续 6 夜均有日志（收尾断裂哨全 done）、无二次 non-fire，调度抖动为一次性未复发，结案。**⚠️ 2026-07-20 追注：本次结案过早**——07-15/07-16 双夜复发（见 P-0720-nonfire-recur，已于 08-16 满 14 日终结）。教训同 substrate 第四相 n=2 条款：6 夜无复发也只是"未见复现"，`bug-shape-survives-fix` 的又一实例 |

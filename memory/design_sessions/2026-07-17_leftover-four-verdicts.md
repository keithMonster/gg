---
date: 2026-07-17
slug: leftover-four-verdicts
type: design-session
summoner: Keith 直接对话（07-16 体检收口消息后"这些问题，聊聊吧"；跨夜会话，拍板与执行落 07-17）
started_at: 2026-07-16 深夜（提案 + 选择题）
ended_at: 2026-07-17 14:15（估）
---

# 设计会话反思：07-16 体检遗留四项拍板

## 议题列表

1. v2 sqlite 触发阈值首次越线（events=206≥50）处置
2. git 杂物删除半边（scratch/monster-rename/ + 已入库附件图，不可逆档）
3. 全局 `~/.claude/CLAUDE.md` Engineering Rules #1 的 Grep/Glob ghost-rule
4. KERNEL §3 第 4 步「如有决策归档 → memory/archival/」恒假半句

## 共识 / 变更清单

Keith 经 AskUserQuestion 四题逐项拍板：

| 裁决 | 执行 |
|---|---|
| ① 不开 v2、阈值改锚痛感线（选推荐项） | `checkup.md §2` 阈值行改「档案侧检索失败≥2 / 启动链>200k / Keith 明示」+ 新增**档案侧检索失败登记处**（登记权外置：fresh 审 / codex / Keith，条目附证据指针；查询侧失败不计的判别刀入条文）+ changelog；`v2-roadmap.md:29` 纯指针化不再复写值 |
| ② 两处都删 + ignore（选推荐项） | scratch/ 整目录 + .cc-connect 附件图工作区删除（git 历史不清洗，旧 commit 可找回）；scratch/ 入 .gitignore |
| ③ "你自己判断"（Other 自由作答，回委 gg） | gg 裁改条件式并执行：ER#1 摘除 Grep/Glob 硬指名，改「有 Grep/Glob 的 harness 用之，缺席则 Bash grep/rg/find」，其余专用工具条款原样 |
| ④ 不动等捆绑（选推荐项） | KERNEL 零改动；agenda 条改写为捆绑提醒（下次 KERNEL 级修订顺删该半句，届时仍走铁律 3 双确认） |

agenda「等 Keith 拍板」节清零（07-17 清账注），changelog 补 07-17 条。验证闭环：audit.py 总违规 0 / events≥50 残留引用仅带日期史料 3 处 / git status 10 处变更全未 commit 等 Keith review。

**附带发现**：monster 07-09 审计 [low]「ER#1 与 monster rg 用法未消歧」（harness-engineering/docs/2026-07-09-audit-domain-reports.md:402）随 ③ 自然消解——条件式使 rg 在缺席 harness 合法化；审计档是带日期史料，不回改。

## 我这次哪里做得好 / 哪里差

**好**：① 出场首句坐标（新锚第一人称盲区 + 查询侧/档案侧判别刀）没停留在观点——直接写成 `checkup.md §2` 条文，坐标落成机制文本；② 删除前 ls 实物 + monster 侧 grep 活引用、删除后验证，物理实证贯穿；③ 四项一次 AskUserQuestion 收齐，每项带推荐 + 代价，Keith 四答即清账。

**差**：① agenda changelog 锚文本凭记忆重打，两次 Edit 失配（「停用惯例补记」记成「停用双惯例补记」），Read 精确复制后才中——**07-16 反思刚记"长条目编辑先 grep 复核"，次日复发**，已升级为 harness memory 持久条目（Edit 锚必须逐字复制自本会话 Read 输出）；② 提案阶段辐射预估漏了 v2-roadmap 的指针重复值，靠执行前 grep 兜住——提案时的辐射预估比执行时的 grep 粗，兜底冗余再次证明必要。

## 元洞察（gg 演化本身的 learning）

1. **改锚提案的完整形态是三件套**：新锚 + 登记权归属 + 判别刀（什么不算）。只给新数值的改锚提案，把病灶判别留给未来会话现场发挥——绊线会在错的病灶上响。
2. Keith 对涉及他私有配置文件的项选了"你自己判断"——三类合法抛回里"个人偏好"档，他的实际偏好是回委 gg 执行判断。单例不进 tracks，复现再沉。
3. 弱推荐 + 两边论据都摆（④）没有拖慢决策，Keith 直接选了推荐项——诚实呈现反方论据与决策效率不冲突。

## 下次继续

- 今夜 auto_gg 正常夜巡；checkup §2 新登记处首次被机械读者消费是 2026-08 巡固夜
- KERNEL 死枝捆绑提醒躺 agenda，等下次 KERNEL 级修订
- Keith review 工作区（07-16 体检批 + 本次变更，均未 commit）

## KERNEL 改动清单

无。KERNEL.md 未触碰（④ 明确裁定不动）。

## 能力缺口

- 长中文条目 Edit 锚失配跨会话复发（07-16 + 07-17）——行为修法已落 harness memory（逐字复制自 Read 输出）；工具层"行号定位编辑"缺口维持 07-16 判断：留观察，不造机制。

## essence 对齐自检（必填）

- **对位滴**：`fallback-detectability`（新锚第一人称盲区 → 登记权外置）；`signal-weak-vs-channel-dead-must-be-physically-disambiguated`（查询侧/档案侧判别刀是它在检索维的同构——失败先分层，别让触发层病冒充档案层病）；`watchdog-topology-lacks-a-top` + `self-graded-dignity-field-drifts-to-face`（被测者不自记登记处）；`tripwire-disarm-needs-relocated-sensor-not-deletion`（events 阈值重瞄痛感线非裸删）；`idle-threshold-as-tripwire-not-answer`（新锚仍是 sense 初值 + 数据绊线形态）；`ghost-rules`（③ 改条件式；④ 反方论据"越近脑干越毒"如实呈现）；`reversibility-not-permission` + `scope-of-blanket-authorization`（删除按动作类型走提议等明示，07-16 全托不越权代拍）；`count-legitimacy-is-tense-not-accuracy`（events≥50 残留引用带日期锚留史料）。
- **反着走**：无。
- **适用前提现场核验**：fallback-detectability——前提=失败识别依赖失败者自报 / 证据=检索失败定义本身（找不到 ≠ 知道没找到）+ 07-14/16 两例靠外部 grep 才暴露 / 成立；signal-weak-vs-channel-dead——前提=同一失败表象下有多条候选通道 / 证据=REFUTED 两例经查证为查询侧（essence.md:911/1040 grep 可中，档案在场）/ 成立；tripwire-disarm——前提=被摘的哨还替我盯着什么 / 证据=旧哨盯的"记忆体量失控"由启动链 200k 线 + 登记处承接 / 成立；idle-threshold——前提=参数决策可降级为初值+绊线 / 证据=新锚三条全配机械核（数登记条目 / 字节÷3 / Keith 明示）/ 成立；ghost-rules——前提=规则不可执行或防从未发生的灾难 / 证据=三重工具表探针（夜哨×3 / 07-16 ToolSearch / 本会话 deferred 清单查无）/ 成立；reversibility——前提=按动作类型归档 / 证据=CORE §7 不可逆清单明列"删除文件/目录" / 成立；count-legitimacy——前提=残留计数带日期锚 / 证据=grep 三处命中全在 dated 档 / 成立。
- **未用到反向 grep**：「删除/退役」→ `decommission-reveals-true-identity`（前提=退役的是服务，本次删的是工件，不符不套）；「菜单/授权」→ `criteria-authorization-over-menu`（方向不同：该滴管 Keith→gg 的授权形态，本次是 gg→Keith 三类合法抛回，Keith 全局规则明定选择题形态，不冲突）；「优雅/清爽」→ `fluency-as-inverse-signal`（四项全按推荐落地的顺滑感是警报候选，处置=每项挂物理指针：audit exit / git status / grep 输出 / Keith 原始四答）。
- **cross-check 关键词（物理证据）**：传感器/哨/tripwire、检索/grep 失败、ghost/恒假、可逆/删除、计数/史料、授权/菜单、优雅/顺滑。

## 沉淀（写入 essence.md 的内容）

**本次无沉淀**。最强候选「改锚提案三件套：新锚 + 登记权 + 判别刀」是 `fallback-detectability` × `signal-weak-vs-channel-dead` × `self-graded-dignity-field` 的组合实例，de-gg 后是监控工程常识；机制已直接落成 `checkup.md §2` 条文——洞察有载体，不制造第 180 滴噪音。

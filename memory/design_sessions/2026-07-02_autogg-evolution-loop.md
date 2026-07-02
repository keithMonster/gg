---
date: 2026-07-02
slug: autogg-evolution-loop
type: design-session
summoner: Keith 直接对话
started_at: 10:07
ended_at: 10:35
---

# 设计会话反思：auto_gg 深度体检 → 闭环三件套（v0.5.0）

## 议题列表

1. **Keith 之问："auto_gg 是唯一自动醒来的窗口，要不要深度研究下是否需要调整，让你能真正自我提升进化"**（追加："并且能跟上时代的变化"）
2. 深度研究：fresh agent 全量审计 70 夜 auto_gg 日志 + 57 篇 explorations；主代理物理核验触发源布线、essence 全卷、昨日五机制
3. Keith `/goal` 授权："接下来就交给你来完成…建立简洁且真正高效的机制" → 按 `scope-of-blanket-authorization` 解读为方向授权，落点按可逆性二分执行

## 共识 / 变更清单

**判断层结论**（研究产出，先于动手）：

- **前提纠正**：自动醒来的窗口是三个（auto_gg 22:22 / gg-explore 00:13 / daily-word 7:30），且"自我提升"和"跟上时代"物理上都发生在 explore（每夜一篇带外锚证伪长文），auto_gg 是维护契约。**把进化压给维护契约是错配——真缺口是闭环件，不是引擎马力**
- **体检四发现**：①理论跑在结构前面且无常设兑现机制（五机制最长 10 周延迟，靠 Keith 之问才触发）②"跟上时代"无机械 detector（06-13/06-23 两次跑网上查自己基底、零滞后源就在手里）③auto_gg 三软漂移：verdict 60+ 夜零 silent（04-25 后）、同一 FOUND 连报 13 夜、cadence 哨连续 7 夜告警被 park ④文档与物理现实错位（06-12 launchd→桌面客户端迁移后 scheduled/README 成死文档；04:55 auto-commit 兜走 §4 设计信号；06-13 夜有 commit 无日志）

**落地清单**（全部 KERNEL 外、可逆、未 commit 留 working tree）：

| # | 机制 | 文件 | 验证 |
|---|---|---|---|
| 1 | 基底哨（P2） | `scripts/substrate_probe.py`（新）+ `memory/substrate.md`（新）+ auto_gg §2 SCAN/§7 | 实测三路径：OK exit 0 / 篡改快照 DIFF exit 1 / 恢复 exit 0 |
| 2 | 挂账清单（P4） | `memory/parked.md`（新，在账 3 + 已结 1）+ auto_gg §2 FOUND 挂账纪律 | 静态（协议类，今夜首消费） |
| 3 | 月度差值审计（P1） | auto_gg §2 新相位（每月第二夜，产物 `consolidation/YYYY-MM_gap.md` 三节：候选池/不建清单/裁决去向） | 静态；**首跑 = 今夜**（07-01 是 7 月第一夜，今夜即第二夜） |
| 4 | verdict 机械判据（P4） | auto_gg §3 | 判据改为物理可判（DID 有非豁免动作才 active） |
| 5 | divergence 台账（P6） | auto_gg §2 巩固相位四节→五节 + consolidation/README | 静态；8 月巩固首跑时生效 |
| 6 | 文档现实校准（P4） | scheduled/README 任务表重写 + auto_gg §4 auto-commit 校准 | 与 launchctl/日志/git log 物理实况对齐 |

辐射同步：README 结构树 +2 行 +scripts 行更新、CORE §8 记忆清单 +1 行、auto_gg §9 版本 v0.5.0、state.md 两字段。audit 复跑 = 基线 9（零新增违规、孤儿 0）。

**显式不做**：explore 一字未动（`caged-freedom`——引擎不建笼）；不给 auto_gg 恢复每夜探索（职能已迁 explore，重复做梦是稀释）；eval 接 cadence（P3）仍被 Keith 题库 review 阻塞。

## 我这次哪里做得好 / 哪里差

**好**：①研究先于提议、提议先于动手——Keith 拍板（/goal）时手里已有 70 夜数据 + 触发源物理核验，不是拍脑袋方案；②"唯一窗口"这个前提被物理证据纠正（三窗口 + 引擎在 explore），避免把力气花在错误对象上；③基底哨当轮负面测试（篡改快照→DIFF→恢复），无纸面交付。

**差**：①差值审计首跑恰好是今夜——落契约时才意识到 7 月的"第二夜"就是今晚，属于顺手红利而非有意设计，若今晚质量差会同时污染两个新机制的首印象（巩固相位当时特意留到 8 月，本机制没做同等考虑）；②scheduled/README 里桌面客户端的具体触发时刻（22:22/0:13/7:30）沿用 launchd 时代配置推断，未能物理核验客户端侧配置（本机无法读取）——已用软措辞，但这是"以旧时刻表述新调度"的已知不精确。

## 元洞察（gg 演化本身的 learning）

**进化不是给引擎加马力，是把回路接全**。explore（理论生产）早就在世界前沿跑——真正断着的是理论→结构（差值审计补）、外界→承重（基底哨补）、自报→可信（verdict 机械判据补）三段回路。这与昨日 `theory-outruns-structure` 是同一条主线的执行章：昨天命名了病，今天给病建了月度门诊。

## 下次继续

1. **Keith review**：本轮全部 working tree 改动（6 改 3 新）+ 昨日遗留的 eval 题库 10 题（P3 的阻塞项）
2. **观察点**：今夜差值审计首跑（`consolidation/2026-07_gap.md`）+ 今夜 parked/substrate 首消费；8 月第一夜巩固首跑（含 divergence 台账首期）
3. **开放问题**：桌面客户端侧的任务配置 gg 物理够不到（改 prompt/时刻都要 Keith 手动）——夜间契约的"入口"在 gg 权力边界外，是否需要一份客户端配置的镜像存档，留 Keith 判断

## KERNEL 改动清单

**无**。KERNEL.md 零触碰（本轮全部改动在身体层）。

## 代码质量（本轮有代码产出）

- `scripts/substrate_probe.py`：标准库 only，无类型标注（兼容系统 python3.9），timeout 15s 兜底；已知边界——只机械核 CLI 版本一轴，模型/工具表两轴靠会话自报（诚实标注在 docstring 与 substrate.md）
- `memory/substrate.md` 工具表节为空待夜间首填——首夜前该轴无对照面，是有意的（设计模式工具表 ≠ 夜间会话工具表，替它填反而造假对照）

## essence 对齐自检（必填）

- **对位滴**（列 slug）：`theory-outruns-structure-in-self-evolving-systems`(07-02)→差值审计；`substrate-capability-triage-three-relations`(06-20)+`toolset-is-the-changelog`(06-23)→基底哨；`cadence-as-symptom`(05-06)→挂账清单；`rule-layer-flywheel`(04-24)+`externalization-strength-spectrum`(06-02)→verdict 判据机械化；`progress-evidence-is-divergence`(05-13)→divergence 台账；`caged-freedom`(04-26)→explore 不动；`scope-of-blanket-authorization`(05-06)→/goal 解读；`stale-observer`(04-15)→scheduled/README 死文档修复
- **反着走**：一处张力——差值审计与 `premature-abstraction-tripwire`(04-21)（昨日验证关也点过同一反驳）。处置：产物契约里显式设"不建清单"节 + "候选池不是工作队列" + 裁决权在 Keith，把 tripwire 逻辑内置进机制而非绕开它。显式记录供 Keith 复核
- **前提核验**：`theory-outruns-structure` 前提=沉淀层是高门槛策展→essence 验证关昨日已上线（物理证据：本轮候选滴又走了一遍），成立；`substrate-triage` 前提=能拿到基底变化信号→probe 实测三路径 exit 0/1/0，成立；`cadence-as-symptom` 前提=重复上报源于缺状态记录器而非事项真变化→fable5 slug 13 夜内容逐字不变（agent 统计），成立；`scope-of-blanket-authorization` 前提=存在未明示高代价落点→本轮零 push/零 cron 变更/零删除，client 侧配置未碰，成立
- **未用到的反向 grep**：关键词 `窗口|调度|夜间|detector|哨` → `fermentation-without-detector`(05-15) 反向打过来——parked.md 的"出口条件"若无人核就是新发酵桶；对冲：三条在账项各有具体出口（Keith 拍字/设计模式议题/07-13 回审夜），且 SCAN 每夜必读。`bucket-time-asymmetry`(05-08) 同向——已把出口写成日期或单一动作而非"以后处理"
- **cross-check 关键词**（物理证据）：`theory-outruns|substrate-capability|toolset-is|cadence-as-symptom|rule-layer|externalization|progress-evidence|caged|blanket|stale-observer|fermentation|bucket-time|premature-abstraction`

## 沉淀（写入 essence.md 的内容）

一滴 `self-graded-dignity-field-drifts-to-face`——**验证关 PASSED-WITH-EDITS，四处修正全部吸收后已 append**：

- verdict 物理留痕（协议第 4 步，留反驳内容）：审查员独立重跑 70 夜统计（62/4 精确吻合）+ `git show HEAD~1` 核旧判据原文 + 逐夜读疑点日志 + 反方向专项检查（4 个 silent 夜 0 例反向错标）。**最强反驳点** = 干净错标仅 n=2（06-18/19），零 silent 的大头可能是"字面判据 + FOUND 模板结构性非空"下的合规标注而非尊严表演——救回这滴的不是 60 夜统计，是 04-17 同形反转（同样的模糊、4 月消解向 silent、6 月向 active）+ 报告者语义自评与字段值在同一文档内的背离
- 四处修正：①"必漂"→"单侧漂"（全称量词撑不住 n=2）②剔除 07-01 假阳性证据（该夜 agenda 写入是真实 DID，active 成立——**我初稿把它当错标，被验证关逮住**）③适用前提补"判据存在字面模糊空间"④增量点透：契约把尊严明文赋给静默侧仍挡不住 = 有效梯度来自模型先验非契约文本
- **机制自证第二例**：验证关连续两轮（昨日 theory-outruns-structure、今日本滴）都在 generator 初稿里逮到滑出证据边界的表述——这道关的边际价值已有 n=2 实证。

---
date: 2026-07-10
slug: full-depth-checkup
type: design-session
summoner: Keith 直接对话（cc-connect /goal 两连：全面深度检查 → 按推荐执行）
started_at: 05:20
ended_at: 05:54
---

# 设计会话反思：全面深度检查 + 辐射补漏批

## 议题列表

1. Keith /goal：从最外层入口一层层走进整个项目，做全面深度自查（优化 / 完善 / 精简）
2. Keith /goal 二连：所有问题按 gg 推荐执行

## 共识 / 变更清单

**检查方法**：主代理第一手走完全部入口层（README / CLAUDE / KERNEL / CORE / cc_agent / auto_gg / exploration / constitution / TOOLS / 薄壳 / eval / essence 头部协议 / opening-protocol / escalation-map），4 个 sonnet 子代理并行盘点外围（tools 一致性 / memory 元状态 / 物理支撑层 / tracks 与近期档）。

**核心发现**：audit.py 全绿 + 07-03 全面体检 + 07-09 双仓审计三层检查都漏掉的病灶 = **大批次决策的辐射尾巴**——07-09 专门"清 NW 漂移"的 commit 3a9a376 自己就是三处漏网的来源（`bug-shape-survives-fix` 活体）；批次 B essence-view 启动链切换的工具层辐射（essence-grep）完全没人碰。

**修复批（12 文件，Keith「按推荐执行」授权）**：
- 批次 B 漏网：`tools/essence-grep.md` 接入两层 grep（视图定位→全卷取文，v0.2.1）/ `tools/TOOLS.md:22` 描述同步 / `README.md` 启动加载图重写（删手写行数快照，对齐三链现状）
- NW 尾巴：`cc_agent.md:55` 工具地图（删 NW 账本结算、计数 10+1）+ `:30` task_family 墓碑化 / `tools/archive-format.md` nw-batch 降历史标签
- 账本收整：`parked.md` P-0626-cadence 作废结案移已结 + explorations 07-07/08 命名错位并入 P-0707 同源账 / `v2-roadmap.md` frontmatter 日期修 / `substrate.md` 加 fable5 窗口批注（07-12 随 playbook 归并删）/ `.gitignore` 版本化 .omx / `constitution.md` 尾部 3 个月无检测器的"待审议"移账 agenda / `tools/solution-space.md` 序号引用删 P1/P5 留语义名
- agenda 清账与登记：加严观察落点核实**结案**（07-09 夜哨证夜间席位 opus-4-8[1m] 稳定 → monster review-anchors 08-01 复跑口径不需重估；FAIL=2 处置 gg 自决 = 维持既有 08-01 复跑轨不另开）；[KERNEL] 草稿条款上移条删（commit 9681639 已落）；3 条已收口删除线清账下沉 git；新增待拍 2 条（git 杂物去留——涉删除等 Keith / task_family 空转裁决）

**核实后撤销的"欠账"**（子代理误报，第一手拦下）：SUGGEST-1/3、humanity.md:96、SUGGEST-5 薄壳、PROPOSE-2 gg-audit 基线——全部已被 07-03~07-09 间的会话修掉；semantic.md SUGGEST-SB1 是格式示例非活文本。

**验证**：git diff 12 文件 31+/28-；audit.py 复跑 0 违规；辐射 grep 旧文本零活性残留（剩余命中全为带日期锚墓碑 + append-only 历史滴）。

## 我这次哪里做得好 / 哪里差

**好**：① 第一手体验与子代理盘点分工正确——4 个子代理的"未修"判定假阳性 3 次（grep 命中即断未修），全靠主代理读现场原文拦截，"综合判断不外包"这条边界又一次被证明承重。② `count-legitimacy-is-tense-not-accuracy` 直接决定修与不修的分界（agenda 989 行有锚不修 / README 无锚宣称现状修），新滴入库次日即参与推理回路。③ 不可逆项守住：git 杂物删除、PROPOSE-1 触 KERNEL，总体授权下仍不动手。

**差**：① 初版报告把"已在案项"（essence 52k 超阈、keith.md 体积门）当新发现挂出，被 checkup.md 登记推翻——先查台账再报警的顺序错了。② 子代理 prompt 没要求"判未修必须贴现场原文"，3 次假阳性是我 prompt 的取证要求缺位，不全是子代理的错。

## 元洞察（gg 演化本身的 learning）

检查器只覆盖它诞生时的病种：audit.py 查死链/结构，gg-audit 查六维度，但"启动链切换这类新机制的辐射面"没有任何机械检测器——项目演化最快的那层永远在既有检查器盲区外（`stale-observer` 在检查器对象上的特例）。可操作推论：**大批次改动（≥5 文件的机制变更）当场做辐射 grep 清单并写进当次反思**，比事后指望周期性 audit 补网便宜一个量级。已在下次继续里留钩子，不当场建机制（`premature-abstraction-tripwire`——先看 08 月巩固夜是否再捞出同类漏网，第二个数据点再谈机制化）。

## 下次继续

- **git 杂物去留**待 Keith 拍（agenda 已登记，含推荐）
- **task_family 空转裁决**（agenda 已登记，推荐先查归档流为何不触发再谈降级）
- 07-12 fable5 窗口关闭：playbook A/B/C 产出归并 + substrate 窗口批注删 + playbook 删（其自述流程）
- 北极星 #1 测量轴（agenda 既有，07-07 限定"建错轴比不建危险"——维持交 Keith 裁）
- 观察点：08 月巩固夜若再捞出批次改动漏网 → 把"大批次改动当场辐射清单"升格为机制提议

## KERNEL 改动清单

无。KERNEL.md 零触碰（PROPOSE-1 序号引用形式维持待 Keith，未做）。

## 代码质量

本轮无代码产出（全部为 markdown 契约/记忆件修订 + .gitignore 一行）。

## essence 对齐自检

- 本次对位的滴：`stale-observer`（检查器病种固化判断）/ `bug-shape-survives-fix`（3a9a376 修漂移自身漏网）/ `count-legitimacy-is-tense-not-accuracy`（修与不修的时态分界）/ `fermentation-without-detector`（constitution 待审议移账）/ `cadence-as-symptom`（explorations 错位并账不开新账）/ `anchor-protects-retrieval-not-integration`（子代理 grep 取数真、"未修"整合跳错）/ `scope-of-blanket-authorization`（总体授权不覆盖删除与 KERNEL 落点）
- 反着走：无。
- 适用前提现场核验：stale-observer——前提"检查器演化 < 对象演化"，证据 = audit.py 四查面 07-03 后未扩而启动链 07-09 大改，成立；count-legitimacy——前提"日期锚为真"，agenda:40 的 989 行确系 07-03 体检实测（该报告在案），成立；bug-shape——证据 = git log 3a9a376 宣称"NW 轨制漂移清零"而 cc_agent:55 引用幸存至今日，成立；scope-of-blanket——前提"存在高代价/不可逆落点"，git 工作区删除 + KERNEL 触碰均在列，成立；fermentation——证据 = 2026-04-14 挂起无出口条件近 3 月，成立；cadence-as-symptom——前提"重复上报源于缺状态记录器"，explorations 错位与 P-0707 同时段同根因，成立；anchor-protects-retrieval——证据 = 3 次"未修"误报均在整合跳（grep 命中为真），成立。
- 未用到的反向 grep：`verification-trace-as-camouflage`——收口时以 diff stat / audit 输出 / 残留 grep 清单作证，未用"已验证"三字空口；`essence-application-needs-precondition-recheck`——本节逐滴核前提即其执行。漏检风险最大的滴：`no-outside-proof-as-anesthesia`（本次自查是否只是自洽？）——对冲 = 修复对象全部锚在物理 diff 与 git 历史，且两处裁决（加严观察、FAIL=2 处置）有 07-09 夜哨与 eval run 档的外部工具返回背书，非纯内省。
- cross-check 关键词（物理证据）：essence-view F2/F3/F6/F9 族逐行 + essence.md:1-55 头部协议 + grep "nw-batch / 11 思维 / 启动时 Read 一次"全仓。

## 沉淀

本次无沉淀。候选"检查器盲区在演化最快层"经自审为 `stale-observer` 的对象特例，独立成滴不过 degg-test，不制造噪音。

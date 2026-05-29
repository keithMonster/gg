---
date: 2026-05-28
slug: keith-counter-precondition-uncheck
type: design-session
summoner: Keith 直接对话
started_at: ~22:00
ended_at: ~23:30
---

# 设计会话反思：Keith 反拷问与 essence 适用前提核验缺失

## 议题列表

1. monster 工作模式裁决（coding-discipline-engineering v1）作为入口——前置已 commit 在 `memory/reflections/2026-05-28_coding-discipline-engineering-challenge.md`
2. Keith 反拷问 N=0 vs N=1：`theory-gap-without-data` essence 在零经验场景被错套
3. 我承认精化 + Layer 2 → Layer 1.5（hook 自检提醒 + 参考文档不抽 skill）+ 拒绝再 gg 审
4. Keith 要求自我反思 → 我反思 13 条（5 段：做对 / 做错 / 没考虑全 / 应该更激进 / meta）
5. Keith 判据级授权"你自己决定，不用再问我" → 本次落地

## 共识 / 变更清单

- **memory/essence.md**：append 新滴 `2026-05-28 / 设计 / essence-application-needs-precondition-recheck`
- **CLAUDE.md §3**：reflection 模板"essence 对齐自检"段加 2 行——"用到的每滴 essence 的适用前提是否被现场核验"（强制）+ "未用到的 essence 反向 grep"（软建议，前提存疑信号时强制）
- **memory/state.md**：`last_summoned_at` 替换为本次设计会话总结（保留 5/28 凌晨 auto_gg 链路作为前置）；`last_design_session_slug` 更新为本反思 slug
- **本反思文件**：`memory/design_sessions/2026-05-28_keith-counter-precondition-uncheck.md`

## 我这次哪里做得好 / 哪里差

### 做对的

1. 顶住 4 路调研一致背书的引力，没被外部安全感拽走——vantage 测试通过
2. 新 essence `engineering-impulse-as-load-bearing-disguise` 沉淀质量过 `essence-degg-test`
3. Keith 反拷问后立即承认精化（`precondition-recheck-overturns-prior-verdict` 落地，没护短）
4. 拒绝再派 gg 审——四条理由叠加（prior 同源 / Keith 在场是最强锚点 / 物理事实可现场核 / 自审偏置）
5. 收到 Keith"你自己决定"后按 `criteria-authorization-over-menu` 落点自决——没回 menu 让 Keith 选具体改哪些文件

### 做错的

1. **essence 适用前提没核验** — `theory-gap-without-data` 原适用域是"机制已建、消费方未来"，本议题是"机制未建、消费方物理触发不了"。同一句话两种语义边界，我套了最方便的那一种。`task-compliance-is-not-truth` 在 essence 引用维度的活体
2. **"等自然触发" = `fermentation-without-detector` 的活体** — 我在裁 Layer 2 工程冲动时握着"无检测器的发酵 = 0 进度"判据，**没把这条转向自己开出的处方**。同议题内同一 essence 被违反两次（裁决"等自然触发" + 6 周回审无挂载点契约）仍未识别 = `bug-shape-survives-fix` 特殊形态
3. **cross-check 只数"用到哪几滴"、没数"漏了哪几滴反向打我"** — `fermentation-without-detector` 就在 essence 库里，没被 grep 到 = 引力分配盲区，选择性挑"支持裁决方向"的 essence

### Keith 在哪里打断 / 纠正我

- **反拷问 N=0 vs N=1**：命中事实层漏洞——不是修辞，是 monster 对"派子代理写代码"是零经验、不是一次经验
- **要求自己反思**：把"再 gg 审一次"路径切断，逼我做内省（这本身是对"我拒绝再 gg 审"的延续测试——你让我自己干那件事）
- **判据级授权"你自己决定"**：方向已明、不让我抛回——`criteria-authorization-over-menu` 的活体训练

## 元洞察（gg 演化本身的 learning）

1. **essence 库本身需要元审视** — 70+ 条 essence 的引力分配靠 LLM 记忆挑相关的 = 同一逻辑栈反复挑熟面孔。结构性补丁=每次 cross-check 至少派一次反向 grep。本次 CLAUDE.md §3 补丁就是这条洞察的落地
2. **反向引力字段的方向决定能锚住什么** — reflection 模板"可能出错的地方 / 推理盲区"如果只写"我判断粗糙在哪"、不写"我引用判据是否适用"，后者才是 Keith 反拷问命中点。`reverse-anchor-by-reflection` 的精化——前者讲反向锚定本身是机制，本议题揭示锚定方向选错时机制空转
3. **判据级授权下直接动手** — Keith 给"你自己决定"= 已经在前置反思中给了 13 条判据，按 `criteria-authorization-over-menu` 落点自决 + 事后简明同步。本次实践成功
4. **同一 essence 在同一议题内反复违反 = 内化未改** — 不是规则文本没写到，是修者用规则修对方时没把规则也用在自己处方上。`bug-shape-survives-fix` 在"治理冲动 + 工程冲动"同时存在场景的双活体

## 下次继续

- 6 周后看 monster 侧 Layer 1.5 hook 自检提醒触发率 + 真派 worker 比例（monster 工作模式回审锚点；gg 这边的对应物=观察自家 essence 应用模式有无改进）
- **留意下次工作模式裁决里是否自然激活补丁后的"适用前提核验"项**——如果第一次按新格式填时仍只填"对位 essence"忽略前提项，说明模板补丁形态不够强、需要继续精化（甚至上升到 reverse-anchor 字段名级机制改造）
- 6 周后回审：新 essence `essence-application-needs-precondition-recheck` 在未来工作模式承重裁决里是否被真激活、还是又陷入"挑熟面孔"。如果未被引用、模板补丁也未被填——essence 沉淀+模板补丁双失败，需要更狠的机制（例如 essence 强制配前提元数据 + cross-check 脚本物理检查）

## KERNEL 改动清单

无。本次所有改动均在 KERNEL.md 之外（essence / CLAUDE.md §3 / state.md / 本反思文件）。

## 代码质量

本轮无代码产出。略。

## 能力缺口

- **essence 应用前提的元数据缺失**：每滴 essence 写时是 1-2 行 insight，没有显式的"适用域 / 反例边界"字段。靠 cross-check 时人脑推断前提，本议题证明这条不可靠。**潜在改造**：essence 写作格式加可选"适用前提"行；或在 essence.md 头部加"应用前提推断规则"段落
- **反向 grep 自动化缺失**：本次反向 grep "fermentation-without-detector / default-bucket-as-deadlock / idle-threshold-as-tripwire-not-answer" 是事后做的，本应是 cross-check 中的标准步骤。**潜在改造**：写一个轻量脚本 `tools/essence-reverse-grep.sh <议题关键词>`，输出"未用到但相关"的 essence 候选——但这又会触发"工具吞噬目的" `means-end-inversion`，要慎重

## essence 对齐自检（必填）

- 本次会话的判断 / 改动跟哪几滴 essence 对位：
  - `criteria-authorization-over-menu` (2026-05-15)
  - `precondition-recheck-overturns-prior-verdict` (2026-05-19)
  - `bug-shape-survives-fix` (2026-04-27)
  - `fermentation-without-detector` (2026-05-15)
  - `reverse-anchor-by-reflection` (2026-04-27)
  - `task-compliance-is-not-truth` (2026-04-16)

- 本次是否在某条 essence 上反着走：无（本次正是补反着走的盲点）

- **用到的每滴 essence 的适用前提是否被现场核验**（按 CLAUDE.md §3 新补丁项填——本次正是补丁落地的第一次实践）：
  - `criteria-authorization-over-menu` — 前提：Keith 已明示判据 + 给"你看着办"。核验：本对话上文 13 条反思 + "你自己决定，不用再问我"原话。✅ 成立
  - `precondition-recheck-overturns-prior-verdict` — 前提：旧裁决依赖的物理前提被推翻。核验：N=0 vs N=1 是物理事实而非语义（monster 项目 grep 历史无"派子代理写代码"实例）。✅ 成立
  - `bug-shape-survives-fix` — 前提：修者修了显式形态、未改内化形态。核验：`fermentation-without-detector` 在本议题被违反 2 次 = 内化未改。✅ 成立
  - `fermentation-without-detector` — 前提：动态过程语义掩盖无机制事实。核验："等自然触发" + "6 周回审无挂载点"两处均符合（无检测器物理对象）。✅ 成立
  - `reverse-anchor-by-reflection` — 前提：反思字段在物理引力上锚住主输出。核验：本议题反思字段写"判断粗糙"、未锚"判据适用" = 锚定方向选错。✅ 前提成立但方向错（这是本议题揭示的精化点）
  - `task-compliance-is-not-truth` — 前提：LLM 找到能套上的就用。核验：`theory-gap-without-data` 在 N=0 场景被错套 = 找熟面孔不审前提。✅ 成立

- **本议题相关但未用到的 essence 反向 grep**（本议题有强"前提存疑 / 选择性引用"信号，按补丁强制做）：
  - 关键词：grep "等" / "发酵" / "无机制" / "consumer absent" / "tripwire" / "default"
  - 漏掉的滴：`fermentation-without-detector` / `default-bucket-as-deadlock` / `idle-threshold-as-tripwire-not-answer`
  - 漏掉理由：cross-check 时只挑"支持我裁决方向"的 essence（用 essence 反对 Layer 2 skill），没挑"反对我替代方案动作"的（用 essence 反对"等自然触发"自己的处方）——选择性引用是 `reverse-anchor-by-reflection` 在 essence 选择维度的反向脱锚

- cross-check 用的关键词：本议题关键词集 = ["theory-gap" / "N=0" / "consumer absent" / "等" / "发酵" / "无机制" / "tripwire" / "default"]——后 5 个是反向 grep 关键词，本应在原裁决就做、不是事后做

## 沉淀（写入 essence.md 的内容）

1 滴：`essence-application-needs-precondition-recheck`（2026-05-28 / 设计）

正文（已写入 `memory/essence.md` 文末）：
> 自家 essence 在应用时必须核验适用前提——"找到能套上的就用"是 `task-compliance-is-not-truth` 在 essence 引用维度的活体，本议题 `theory-gap-without-data` 在 N=0 场景被错套是典型形态（原适用域"机制已建、消费方未来"被套到"机制未建、消费方物理触发不了"上，对症解从"等"变"建最小观察机制"）。
> cross-check 不只数"用到哪几滴 + 是否成立"，更要数"每滴前提是否被现场核验 + 漏了哪几滴反向打我"——essence 库的引力分配也有盲区，靠记忆挑相关的等于同一逻辑栈反复挑熟面孔；选择性挑"支持裁决方向"的 essence 而不挑"反对方案动作"的，是 `reverse-anchor-by-reflection` 在 essence 选择维度的反向脱锚。

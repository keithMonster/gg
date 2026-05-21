---
date: 2026-05-20
mode: 工作
slug: monster-buglog-design
status: substantive-decision
caller: monster (Claude Code 主会话，inbox topics #21 OpenWolf 议题决策)
---

# monster buglog 载体设计裁决

## 议题

Claude 提案 B 路径：monster/buglog.md 独立文件 + 一行自包含 + diagnose Phase 0 接入 + 30 天 ROI 评估 + 启动种子 6 条。原议题（topics #21）A 路径：jsonl + py + 可能 embedding。Claude 自己抛 3 个承重墙问题：新载体 vs canon 子段 / 写入义务挂哪 / grep vs embedding。

## 装配

- KERNEL + CORE + state + essence（启动四件）
- shared/gg-briefing.md（monster invariant 先验）
- monster/canon.md（横切规矩载体现状 + 撤销条件）
- monster/concepts.md（元概念边界条款）
- diagnose SKILL.md（现状 5 phase）
- reasoning_modules（OCCAM + COST-BENEFIT + TRIPWIRE）
- persona conservative + radical 内部辩论（防御新载体扩张 vs 看是否真有新维度需求）

## 核心假设

1. canon 的本质是"横切方法论"——bug 经验是其同质子集，不是异质对象。Claude "规矩 vs 案例"二分搞反了 canon 的定位
2. canon 自身在 4 周 tripwire 期（2026-06-15 撤销条件），未稳定载体之上叠新载体 = theory-gap-without-data
3. canon.md 头部已明示"写入触点 done 5F"——bug 经验作为 canon 子段自然继承，无需新建 diagnose Phase 5
4. monster 月均 2-3 次 bug 复发率 × 半年累计 ≤15 条 → grep 全文 < 50 行可吃下，embedding 焦虑提早
5. MEMORY 是 threads 派生物不是独立载体——Claude 列 4 载体把派生当并列，导致"加一个变 5 个"的伪拓扑焦虑

## 可能出错的地方

- canon 子段可能跟现有 canon 规矩条目语义混淆（grep 命中规矩 vs 案例时优先级判定）—— 用标题 anchor `## bug 复发型经验` 物理隔开同一文件不同子段，grep 命中归属清晰
- done 5F 在实际触发上的 bar 不够高，bug 子段无差别堆条目—— 写入时强制"症状词列 ≥2 个自然变形"格式过滤
- diagnose Phase 0 加了但实际 LLM 不读 canon—— 监测窗口跟 canon 撤销条件同步，零 fire 时整体撤销
- 跟 canon 共存亡可能拖累 canon 撤销判定（"bug 子段在用但 canon 主条目零 fire" 的纠结）—— canon 撤销条件文件尾改一句"包括 bug 子段在内的所有条目"消歧

## 推理盲区

- 没核 done SKILL.md 现状 Step 5F 具体怎么写的（议题涉及在它上面挂新格式）—— 父会话执行"必做1-4"前应该 Read done SKILL.md Step 5F 现状再扩
- review-routing skill 跟 bug 经验的接口考察是猜的（没读 review-routing agent system prompt 实际内容）—— 仅作为未来锚点提及，必砍清单未硬塞接口设计

## N 个月后根因预判

如果这个决策最后错了，最可能的根因是：
- (a) canon 撤销了但 bug 子段需求真的产生了独立增长 → 此时该独立成载体而非跟 canon 一起删；当前判定是把它当 canon 扩张测试一并撤销，可能浪费实证数据
- (b) done 5F 触点太重 / 太被动，会话级回看抓不住 bug 形态横切信号 → 应该在 diagnose 收尾也加写入触点（不是 Phase 5 强制，是 Phase 5 推荐 + done 5F 兜底双触点）

对冲：撤销/扩张决定走 gg 重审，不让"跟 canon 共存亡"硬规则锁死 (a) 的可能性

## 北极星触达

- 二阶效应（space）：bug 经验从一次性会话事件 → 永久横向资产 ✅
- 动态学习反哺（time）：done 5F 把会话级学习自动沉淀跨会话 ✅
- 决策超越直觉（depth）：diagnose Phase 0 让"是否踩过同形态"从直觉 → 外部可查事实 ✅

强对齐。

## essence 对齐自检

- `theory-gap-without-data` (2026-05-06) → 拦住 A 路径 embedding / 拦住 30 天 ROI 锁生死 / 拦住启动种子 6 条 ✅
- `premature-abstraction-tripwire` (2026-04-21) → 拦住"为想象的未来需求"建独立载体 ✅
- `idle-threshold-as-tripwire-not-answer` (2026-05-14) → 拦住"30 天 ROI"短窗判生死，改 sense-driven 跟 canon 共存亡 ✅
- `tool-elevation-as-occam` (2026-05-06) 反向 → 上提到独立载体的合法触发未达（消费方 1 个 / 物理量级未触发），保持原载体子段 ✅
- `runtime-state-vs-business-data-distinct-ssot-domains` (2026-05-20) → 同类辖域归一原则，bug 经验属于横向规矩辖域归 canon ✅
- `cheap-layer-is-intentional-not-fallback` (2026-05-17) → canon 是 monster 的廉价横切层，bug 经验属于该层而非另起昂贵层 ✅
- canon.md 自身的撤销条件 + 零关系 schema → bug 子段继承零关系约束，撤销跟随主条款 ✅

cross-check 关键词均 grep 过 / 真实存在。

## 给父会话的最终输出

**结论**：建，但变形——不新建 buglog.md，挂在 canon.md 作 `## bug 复发型经验` 子段。

**Q1 拍**：canon.md 子段（不新建第 5 个载体）。理由：bug 经验本质属横切方法论辖域，与现有 canon 同质；canon 自身在 tripwire 期未稳定，叠新载体 = theory-gap-without-data；Claude 的"4 载体"列错把 MEMORY 派生物当并列，真载体只有 3 个（threads/canon/concepts）。

**Q2 拍**：done skill Step 5F 写入触点（diagnose 只在 Phase 0 读侧接入）。理由：canon 头部已焊触点；bug 元洞察（bug-shape-survives-fix 类）往往要会话级回看才显形；CLAUDE.md 隐式 = 必然漂回 LLM 不靠谱原点。

**Q3 拍**：markdown 起步 + 无独立时钟 + 跟 canon 整体共存亡（不设 30 天 ROI 判生死 / 不设升 A 显式触发）。理由：低频系统短窗判生死违 idle-threshold-as-tripwire-not-answer；升级判据归 canon 自身扩张 tripwire（>20 条 + ≥3 次扁平答不了），不另设独立时钟；embedding 讨论全砍（theory-gap-without-data）。

**必做 5**：
1. canon.md 末尾加 `## bug 复发型经验` 段（含格式契约 + 写入触点 + 共存亡条款）
2. diagnose SKILL.md 加 Phase 0（grep canon bug 段，命中跳过 1-4）
3. done skill Step 5F 文档加一行（bug 形态走 5F + 格式硬约束"症状词 ≥2 变形"）
4. monster/CLAUDE.md "横向记忆载体 canon.md" 段触发关键词追加 bug/报错/根因/复发/症状/debug 经验
5. inbox topics #21 关闭（移 closed/2026-05.md 一行摘要 + 指针本 reflection）

**必砍 6**：buglog.md 独立文件 / jsonl+py / 启动种子 6 条 / 30 天 ROI 时钟 / 升 A 显式触发 / embedding 讨论。

**5 盲点**：① 4 载体计数把派生当并列 ② 种子 6 条 = 理论数据污染 ③ Phase 0 命中率焦虑提早（半年内 grep 完全吃下）④ review-routing 接口未来锚点（先标 `[review-blind: ...]` tag，不焊死）⑤ Anthropic Managed Agents 调研里的 scheduled cron Outcomes 判据是未来潜在消费方（不为此设计 schema）。

**北极星三条均强对齐**——但只在变形后的版本下才过；原 B 提案因新增载体+种子+独立时钟在二阶效应轴上是稀释。

## 待 Keith review

- 父会话执行"必做 1-5"前请先 Read done SKILL.md 现状 Step 5F（reflection 推理盲区 1）
- Q1 决议关键依据 = canon 本质判定（bug 经验属横切方法论辖域同质子集），如果 Keith 不同意此本质判定，整个决议链需重审

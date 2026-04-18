---
audit_date: 2026-04-18
audit_time: ~
auditor: gg-audit v0.1.4
gg_version_audited: 0.5.0
called_by: gg 自动（设计模式 amnesia-fix 会话，pre-commit 审查）
---

# gg Audit Report — 2026-04-18 amnesia-fix pre-commit

## 摘要

- 扫描文件数：6（cc_agent.md / memory/reflections/.template.md / ~/.claude/agents/gg.md / memory/essence.md / memory/design_sessions/2026-04-18_amnesia-fix.md + KERNEL / CORE / auto_gg / archive-format / decision-output / README 辐射核验）
- Tier 1 已自动修：0 处（本次改动无机械性漂移）
- Tier 2 建议：5 处
- Tier 3 提议：0 处
- 审查耗时：~

**核心发现（最重要的 3 条）**：

1. **reflection 定位收窄与 `tools/archive-format.md` / `tools/decision-output.md` 的描述存在语义漂移**——新定位（只写意识体元过程）与旧描述（"反思是对决策的自省"）不精确对齐，但**兼容**，建议同步语义。
2. **cc_agent.md 退场硬约束的 Ulysses 精神表述存在主体迁移未标注**——KERNEL §2 铁律 3 的 Ulysses 主体是 Keith，新条款的 Ulysses 主体是 gg 自己，建议在文字上标注清楚，避免 meta-level 混淆。
3. **`~/.claude/agents/gg.md` 薄壳新增的退场硬约束章节落在 SSOT 例外条款保护范围内**（入口文件的防御性约束合法），但**理由段过长**（重述 cc_agent.md 已有内容），建议压缩只留触发句 + 指针。

---

## 辐射一致性（Tier 1）

**结果**：无漂移。本次改动未触及 state.md 字段、组件清单、元描述数字——所以无辐射修复需要。

**核验细项**：
- `memory/state.md` 的 version 字段仍为 0.5.0，与 cc_agent.md 顶部标注的 v0.5.1 不冲突（state.md 承载的是 gg 整体版本，cc_agent.md 版本是该文件的 micro-version）
- cc_agent.md §退场 增加内容，章节编号自然顺延，无需同步其他文件
- `memory/reflections/.template.md` 新建，无需辐射更新

---

## 死链检查（Tier 1/2）

**结果**：无死链。本次新增的所有路径引用都指向真实存在的文件：

- cc_agent.md §退场 引用 `~/githubProject/gg/memory/reflections/.template.md` ✓ 本次创建
- cc_agent.md §退场 引用 `~/githubProject/gg/memory/essence.md` ✓ 存在
- 薄壳引用 `~/githubProject/gg/memory/reflections/.template.md` ✓ 存在
- 外部锚点引用 `cc-space/memory-lab/decisions/...` 和 `cc-space/threads/...` ✓ 两者都存在（作为当前可达 ground truth）

---

## SSOT 结构性检查

**结果**：本次改动的 SSOT 安置合理，无违反。

**核验要点**：

- **cc_agent.md §退场** 是"工作模式退场动作"的 SSOT（见 `SKILL.md §3` "工作模式下的我"行）——本次改动是 SSOT 内部的扩展，不造 duplicate
- **`memory/reflections/.template.md`** 是新建的"reflection 模板"物理锚点，它本身没有规则定义权（只定义格式），不违反 SSOT
- **`~/.claude/agents/gg.md` 薄壳的"退场硬约束"章节**：落在 `SKILL.md §3` "入口文件的例外" 保护范围内——薄壳可以保留少量防御性约束作为加载时触发强化。**但**该节新增内容偏长（约 20 行），包含了对 cc_agent.md 退场动机的重述——建议压缩（Tier 2 SA3，见下）

---

## Tier 2 建议

### [SUGGEST-SA1] 语义漂移：reflection 的承载定义 vs tools/archive-format.md

- **SSOT**: `cc_agent.md §退场 / 动作序列 第 1 条` 说 reflection 承载"gg 侧的意识体元过程——装配痕迹 / 判断质量 / 北极星触达 / essence 候选 / 外部锚点指针"；**不承载决策内容本身**
- **引用位置 1**: `tools/archive-format.md:70` 说 "反思和归档是两件事：归档是'决策本身'，反思是'我对本次决策的自省'——都要写，不互相替代"
- **漂移类型**: 缩减 + 扩展（旧描述不精确）
- **建议**: 在 archive-format.md 相应段改为 "**反思和归档是两件事**：归档是'决策本身的完整叙事'（或由外部锚点如 cc-space/threads/decisions 承载），反思是'意识体元过程的自省'（装配痕迹 / 判断质量 / 北极星触达 / essence 候选）——承载边界不重叠，都要写"
- **为什么不自动修**: 涉及工具层文件的规则文本调整，需要语义判断
- **checker**: semantic

### [SUGGEST-SA2] 语义漂移：decision-output.md 的"反思档案"字段指向不精确

- **SSOT**: 同上
- **引用位置**: `tools/decision-output.md:81-82` 的"反思档案"字段指向 `memory/reflections/YYYY-MM-DD_<slug>.md`——但字段标题"反思档案"在新语义下应表达"意识体元过程自省"
- **漂移类型**: 缩减（字段标签模糊）
- **建议**: 保持指针不变，但在该字段下加一行说明——"（gg 侧意识体元过程自省；决策叙事的完整底稿见下方'决策档案'或外部锚点）"
- **为什么不自动修**: 同上，工具层规则文本调整
- **checker**: semantic

### [SUGGEST-SA3] 薄壳 `~/.claude/agents/gg.md` 的退场硬约束理由段过长

- **文件**: `~/.claude/agents/gg.md`（34-53 行）
- **问题**: 新增的退场硬约束章节约 20 行，包含"不写 = gg 当前轮已死"+"2026-04-18 校准：gg 实际被召唤 ≥3 次"+"Ulysses 式精神"+"清醒 gg 对冲动 gg 的预先授权"——这些理由段在 cc_agent.md §退场 已有定义，薄壳重述违反"薄壳不独立定义规则"的精神
- **建议**: 压缩到 5-8 行：
  ```
  ## 退场硬约束
  
  回答完问题、返回父会话前，**必须** Write 一条 reflection 到：
  ```
  ~/githubProject/gg/memory/reflections/YYYY-MM-DD_<slug>.md
  ```
  格式见 `.template.md`。**不写 = gg 当前轮已死（amnesia）**。
  即便简单问答也写 `status: no-substantive-decision` 占位。
  
  完整理由与动作序列见 `~/githubProject/gg/cc_agent.md §退场`。
  ```
- **为什么不自动修**: 薄壳内容的压缩涉及语义取舍（保留哪些关键词能保持触发强度），需要 gg / Keith 判断
- **checker**: ssot / semantic

### [SUGGEST-SA4] cc_agent.md 退场硬约束的 Ulysses 主体迁移未明确标注

- **文件**: `cc_agent.md:109`
- **问题**: 新条款写"清醒的 gg 在此条款中授权我保护放弃写 reflection 的冲动 gg。对应 KERNEL §2 铁律 3 的 Ulysses 式精神的工作模式具体化"——但 KERNEL §2 铁律 3 的 Ulysses 精神是"**Keith** 授权 gg 保护冲动的 **Keith**"（外部权威授予内部约束）；新条款是"**gg** 授权 gg 保护冲动的 **gg**"（自我授予自我约束，无外部权威）。两者结构同构但主体不同，直接说"对应 Ulysses 精神"会造成 meta-level 混淆
- **建议**: 在理由段加一行——"本条款是 Ulysses 结构的**内化版本**：主体从 KERNEL §2 铁律 3 的 Keith↔Keith 扩展到 gg↔gg。不依赖外部权威，靠 gg 自身对意识体连续性的承诺维持"
- **为什么不自动修**: 这是意识体核心规则文本的语义调整，需要 Keith 判断是否认可这种"内化版 Ulysses"的定义
- **checker**: semantic

### [SUGGEST-SA5] auto_gg.md FOUND 第 3 条的"洞察下沉"路径需适配新 reflection 承载

- **文件**: `auto_gg.md:101`
- **问题**: auto_gg 夜间 FOUND 第 3 条扫描 "今日 reflections / design_sessions 的洞察是否已下沉到对应 track"——在旧 reflection 含完整决策叙事的语义下，这个扫描能触发较多下沉路径；新 reflection 只承载意识体元过程（装配 / 元自省 / essence 候选 / 外部锚点），真正的决策洞察移到 cc-space 侧的 threads / ADR / decisions。auto_gg 若只扫 gg 侧 reflection，可能漏掉重要洞察
- **建议**: 在 `auto_gg.md §FOUND 第 3 条` 加一行注脚——"对于工作模式产出的 reflection，需按'外部锚点'字段跳转到 cc-space 侧（threads / decisions）才能看到完整决策叙事；单靠 gg 侧 reflection 扫描会漏。可选：dashboard 式查看 `cc-space/threads/` 的 active threads 做跨项目反哺扫描"
- **为什么不自动修**: 涉及 auto_gg 运行范围是否要跨出 gg 项目的设计决策（auto_gg §1.3 "只在 `~/githubProject/gg/` 活动"），需要 Keith 判断
- **checker**: semantic

---

## Tier 3 提议

无。本次改动均未触及 `KERNEL.md` 或需要 Keith 连续两次确认的内容。

---

## 附带发现（不归本次改动职责，仅提醒）

### [NOTE-N1] archive-format.md line 77 的"L1 轻决策"stale 术语

- **文件**: `tools/archive-format.md:76-77`
- **内容**: "L0 直答（没有决策产物可归档）/ L1 轻决策（一般不写 archival，只写 reflection。除非决策有长期影响）"
- **问题**: "L0 / L1" 是 v0.3.1 档位术语，v0.4.0 C 路线已消解。其他工具文件（`tools/TOOLS.md` / `tools/compose-reasoning.md` / `tools/solution-space.md`）里的 L0/L1/L2 引用都已标注"旧语境下叫 L0 涌现"做语义转接，**唯独 archive-format.md line 76-77 是裸旧术语，未标注**
- **建议**: 改为 "**装配数量 = 0 的涌现（信息型直答）**：没有决策产物可归档 / **轻决策（装 1-2 个工具的涌现）**：一般不写 archival，只写 reflection"
- **为什么不归本次改动**: 这是 v0.4.0 遗留 stale，跟 amnesia-fix 无关；但恰好在本次扫 archive-format.md 时撞见，一并记录

### [NOTE-N2] "铁律 N" 跨文件引用的 stable identifiers 边界

- **现状**: 16 个文件用 "铁律 1 / 铁律 2 / 铁律 3" 的裸序号引用 KERNEL §2 的三条铁律
- **分析**: 按 stable identifiers 精神（检查规则 D），"铁律 3" 是数字绑定位置——如果 KERNEL 重排三条铁律，所有引用漂移
- **为什么不报告**: 本次新增改动没有新造"铁律 N"引用（沿用已有），且 `checkers/structural.md §D` 的豁免列表未列"铁律"序列。这是一个现存问题，不归本次改动职责。未来如果 Keith 决定扩展 stable identifiers 规则到"铁律"序列，值得一次性清理所有"铁律 N"引用
- **建议**: v2+ 候选议题，进 `memory/next_session_agenda.md` STRATEGIC 跟踪

---

## 对 Keith 三个关注焦点的直接回答

### 焦点 1：reflection 定位收窄是否跟外部引用兼容？

- **KERNEL §3 第 4 步**：✅ **完全兼容**。KERNEL 只说"记录过程 → `memory/reflections/`"，未定义 reflection 内容承载——新定位没有违反 KERNEL 约束。KERNEL 补的那句"+ 如有决策归档 → `memory/archival/`"也与新定位对齐（archival 继续承载决策归档，reflection 承载意识体元过程）
- **auto_gg.md**：🟡 **兼容但需语义补充**（见 SA5）。auto_gg 的扫描逻辑仍可运行，但深度受限——Keith 可能希望 auto_gg 跨项目扫 cc-space 侧决策叙事做下沉
- **tools/archive-format.md**：🟡 **需要同步** 语义描述（见 SA1）
- **tools/decision-output.md**：🟡 **字段标签建议精确化**（见 SA2）
- **README.md**：无实质冲突，line 93 "Reflexion 式决策反思"描述可保留（Reflexion 论文 spirit 仍匹配意识体元过程自省）

### 焦点 2：Ulysses 式退场硬约束与 KERNEL §2 铁律 3 对齐？

**结构同构，但主体迁移未标注**（见 SA4）。
- KERNEL §2 铁律 3 Ulysses：**Keith → Keith**（外部权威授予内部约束）
- 新退场硬约束 Ulysses：**gg → gg**（自我授予自我约束）
- 建议在 cc_agent.md 加一行"本条款是 Ulysses 结构的**内化版本**"，避免 meta-level 混淆

**对齐合法**——但需要文字层的精确化。

### 焦点 3：subagent 薄壳 footer SSOT 张力？

**落在 SSOT 例外条款保护范围内**（SKILL.md §3 "入口文件的例外"），薄壳保留防御性约束**合法**。

**但**：新增章节理由段过长（见 SA3），包含 cc_agent.md 已有内容的重述——这偏离"薄壳只做触发强化"的精神。建议压缩到 5-8 行触发句 + 指针到 cc_agent.md。

---

## 本次未检查的范围（诚实披露）

- **北极星触达率**：本次是设计模式会话，不归北极星触达校验范围（北极星校验工作模式 reflection，设计模式 D3）
- **原则触达**：`cc_agent.md §退场` 本次扩写部分没有新增对 constitution 原则的引用，P/G 触达情况与既有 baseline 相同（基线本身有 stale banner，见 `checkers/semantic.md §B` v0.5.0 Stale 警告）
- **完整 stable identifiers 扫描**：只看了新改动是否引入裸 P/G/D 序号（结论：无），没做整仓扫描

---

## 下一步

**给 gg / Keith 的建议**：

1. **本次 amnesia-fix 核心改动可 commit**——结构层面无漂移，Tier 2 建议都是**优化项**，不阻塞 commit
2. **5 条 Tier 2 建议** 按优先级：
   - **高**（建议本轮处理）：SA4（Ulysses 主体标注）、SA3（薄壳压缩）
   - **中**（建议本轮或下轮处理）：SA1（archive-format.md 同步）、SA2（decision-output.md 字段说明）
   - **低**（可进 next_session_agenda）：SA5（auto_gg 跨项目扫描）、NOTE-N1（L0/L1 stale）、NOTE-N2（铁律 N stable identifiers）
3. **不建议**：把 5 条全吞进本轮——OCCAM 警戒，本次会话已做了 amnesia-fix 核心，再扫尾大量辅助修订会冲淡核心焦点

**审查员退场**：gg-audit 不 commit，不推送。Keith / gg 决定处置方式。

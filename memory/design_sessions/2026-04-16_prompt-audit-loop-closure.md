---
date: 2026-04-16
slug: prompt-audit-loop-closure
type: design-session
summoner: Keith 直接对话
started_at: 09:30
ended_at: 10:25
---

# 设计会话反思：提示词工程内核 → skill-auditor rubric 的刀链闭合

## 议题列表

按出现顺序：

1. **2026 提示词工程内核总结**——Keith 要我讲清楚当前提示词工程的范式、真正有效的杠杆、已死技巧、深层本质
2. **审核 prompt-writer skill**——用内核对照现有的自研 skill 打分
3. **子代理二次审核我的审核**——Keith 要求独立视角 critique
4. **接受反驳 + 修正后 P0 改 prompt-writer**——body 大重构（加已死表述清单 / 目标模型字段 / 修复路径 / 输入变量设计）
5. **审核 skill-auditor 自身**——用刚磨好的刀审核 meta 工具
6. **修 skill-auditor**（description 精简 + PLAN 动态化 + tags）
7. **触发 skill-auditor 审核其他 9 个自研 skill**——产出 reports/2026-04-16.md（v1）
8. **Keith 追问"skill-auditor 有没有审核 prompt 内容质量"**——决定扩展 rubric
9. **rubric v2 扩展**——新增 §4.13 Prompt 内容质量维度 + 权重重分配
10. **重审一次（v2）**——产出 reports/2026-04-16-v2.md
11. **全线修 4 个 description 的触发短板**——最后收尾，平均分到 98.67

## 共识 / 变更清单

### 变更文件清单（全部在 `~/.agents/skills/` 内，gg 本身未动）

**prompt-writer**：
- `SKILL.md`：body 从 86 行重构到 131 行——新增"已死表述主动剔除清单"、"目标模型"字段、"修复路径"、"输入变量设计"模块、"反向重叠检查"自检项。description 两次升级（含 tags）

**skill-auditor**：
- `SKILL.md`：description 从 ~250 字精简到 ~150 字（去掉 body 重复的行为约束枚举），加 tags，Step 3 加 "Prompt 内容质量" 维度说明
- `PLAN.md`：首批审核对象静态表改为动态扫描声明
- `references/rubric.md`：§3 权重表调整（B/C 新增 Prompt 内容质量 10 分，从 Desc 触发/Pushy/代码化匀出）、§2 代表 skill 列表更新、新增 §4.13 完整细则
- `reports/2026-04-16.md`：v1 审核报告（9 及格 / 0 警戒，平均 95.3）
- `reports/2026-04-16-v2.md`：v2 含 Prompt 内容质量维度（平均 96.7）

**其他 skill description 升级**：
- `fastgpt/SKILL.md`、`search-skill/SKILL.md`：加防漏触发兜底句
- `wecom-smart-table/SKILL.md`：搬 body 触发场景到 description

### 核心共识

1. **Skills body 本质就是 prompt**——结构合规不等于内容合规。prompt 工程内核应当从 prompt-writer 的私有信条升级为 skill-auditor 的共享审核标准
2. **"只审不改"原则强化**：skill-auditor 检测 prompt 内容问题但只报告，绝不改语义。审核权和修改权分离是认知独立性的基础
3. **刀链闭合**：prompt-writer（产出规约）↔ skill-auditor（审核规约）↔ skill 生态 body（被审核对象）——三者共享同一套 prompt 工程原则，形成一条流动的认知标准传播链

### 数据结果

| 阶段 | 平均分 | 最低分 |
|---|---|---|
| v1（旧 rubric） | 95.3 | 86 (prompt-writer) |
| v2（+Prompt 内容质量） | 96.7 | 90 (loop) |
| 全线 description 修复后 | **98.67** | **90 (loop)** |

7 个 B 档 skill 中 6 个满分，prompt-writer 98，loop 90（手动调用型天然上限）。

## 我这次哪里做得好 / 哪里差

### 做得好

1. **主动开子代理二次审核**——没等 Keith 提就是我自己没做的，但 Keith 提出后我直接给了一份自包含的高质量 briefing，子代理的反驳锋利且有价值
2. **诚实接受反驳**——尤其 persona 自相矛盾那一刀我直接承认（审核报告里夸"角色要匹配产物"是亮点，但内核里又说"persona 近乎零效果"）。没护短
3. **刀磨好再砍别人**——Keith 说"刀磨好再去砍其他的"，我按这个顺序做。先改 skill-auditor 自己，再用它审其他 skill。避免了"用没校准的尺子量别人"
4. **扩展 rubric 时的体系化思考**——不是简单加一条，而是重新分配了权重（description 从偏重下调、新增维度 10 分）、考虑了 A 档豁免、明确了豁免规则（具象角色锚定/创作型豁免样例等）。不是"加"而是"重构"
5. **description 并行修复**——4 个文件并行 Edit，1 个 message 搞定
6. **批量采集用脚本**——第一步扫所有 skill 时用了 bash 一行处理 9 个文件，没有逐个 Read

### 做得差

1. **初次内核总结的三个绝对化**——"CoT 已死" / "persona 零效果" / "few-shot 最高 ROI" 全都省了前置条件。需要子代理指出才发现。这是我顺着往下写的惯性
2. **范式霸权**——Gap #2 我用 Context Engineering 大叙事去压一个定位清晰的 86 行元工具。子代理正确地反驳："克制本身是它的设计，不是它的缺陷"
3. **冤枉 3 个 gap（#5/#6/#7）**——有"希望 skill 更长更全"的本能冲动，违背我自己讲的 OCCAM
4. **漏掉 3 个真 gap**——input slot 设计 / debug 已有 prompt 的路径 / 反向重叠警告。子代理抓到的这三条比我列的很多 gap 都更重要
5. **自相矛盾未自检**——内核总结和审核报告里的 persona 判断是冲突的，这在 D2 心算 INVERSION 时应该抓到但我没抓
6. **没显式标注任务性质**——按 CLAUDE.md §5，这次任务从性质上更接近"用 gg 做工作"（改 skill 生态）而不是"演化 gg 本身"。虽然边界模糊（建立跨 skill 共享的 prompt 工程标准也算 gg 能力扩展），但我没做这个说明

## 元洞察（gg 演化本身的 learning）

### 1. 双端生态的刀链闭合

这是本次最大的元发现——**prompt-writer 是"写 prompt 的规约"，skill-auditor 是"审 skill 的规约"，而 skill 的 body 就是 prompt**。所以 prompt-writer 建立的 prompt 工程内核，应该沉淀到 skill-auditor 的 rubric 里——内核就成了可复用的共享标准。

这提示了一种 gg 也可以借鉴的模式：**任何"规约-产出-审核"三元组，规约部分应该同时成为审核器的标准库**。比如 gg 的 constitution 就应该是 gg-audit 的 rubric 源，而不是两条平行的规则链。现在部分如此但不完全。

### 2. 审核者必须能被审核

skill-auditor 自己定义了"自审递归例外"（自己不审自己），但必须有**外部视角**审核它——这次就是我用 prompt 工程视角独立审核了它。没有这一步，skill-auditor 的标准就是"皇帝的新衣"。gg 同理：gg-audit 独立审 gg 结构，但 gg 本身还需要 Keith 审核 gg-audit 的判断合理性。

### 3. 子代理 CRITIQUE 是不可放弃的工具

我自己顺着往下写容易"绝对化 / 范式霸权 / 冤枉对象"。二次审核不是仪式，是必须——尤其当我做评估性输出（审核 / 评分 / 判断优劣）时。gg 的 constitution §CRITIQUE 是这条规则的形式化。设计模式下我应该默认高级别议题都触发 CRITIQUE，而不是"感觉需要的时候才做"。

### 4. "改了里子没改面子"是一种典型 failure mode

prompt-writer 在本轮 body 重大重构后，description 只做了微调——这导致它在 v1 审核里拿了最低分。身份/能力更新但对外接口没同步，这在 skill 生态里是个常见陷阱。推广到 gg：如果我改了 KERNEL / constitution / CORE，对应的"对外接口文件"（README / CLAUDE.md / auto_gg 入口）必须同步检查，否则能力有但外界触达不到。

### 5. "只审不改"是认知独立性的结构保障

审核者一旦获得修改权，就丧失了独立判断。skill-auditor 的核心纪律是正确的。推广：gg-audit 也应该坚持只审不改（Tier 3 KERNEL 改动甚至需要 Keith 两次确认），这不是谨慎，是结构必要。

### 是否写进 tracks？

tracks/ai.md 已经有"prompt 工程 / skill 生态"相关的开放问题吗？（这次没去读 tracks）。元洞察 1-5 里至少 1 和 3 值得作为 gg 认知的扩展候选，留待后续触达 tracks 时合并。

## 下次继续

### 遗留问题（skill 生态）

1. **search-skill vs Vercel find-skills 决策**——延续两次报告了，Keith 尚未决策
2. **skill-auditor Phase 3 脚本化**——scripts/collect.sh（扫描 + 分类采集）落地后可大幅降低审核成本
3. **loop 的天然上限**——90 分是手动调用型 skill 的结构上限，不需要再推

### 遗留问题（gg 本身）

- 本次没动 gg 文件。但元洞察 1（constitution 应作为 gg-audit 的 rubric 源）和元洞察 3（CRITIQUE 应默认触发而非感觉需要）是两条值得在下次设计会话中讨论的候选议题

### 是否合并进 tracks

本次元洞察暂未写入 tracks/。如果下次 Keith 在 gg 目录讨论"审核机制 / skill 生态 / 认知独立性"话题，可以把这份反思作为背景材料引用。

## KERNEL 改动清单（如有）

**无。** 本次未修改 `KERNEL.md`。

## 沉淀（写入 essence.md 的内容）

本次产出一滴值得沉淀的洞察：

### slug: `audit-loop-closure`

**摘要**：规约、产出、审核是认知体系的三元组。规约部分（prompt-writer / constitution）应当同时成为审核器的标准库（skill-auditor / gg-audit），而不是平行的两条规则链。审核者必须能被外部审核，且必须保持"只审不改"——修改权和审核权合流会摧毁判断独立性。

**完整形态见下**（追加到 essence.md 时的格式）。

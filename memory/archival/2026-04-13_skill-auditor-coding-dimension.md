---
date: 2026-04-13
slug: skill-auditor-coding-dimension
summoner: Claude Code 主会话 (cc-space 工作区)
tracks_touched: [cc, architecture]
reasoning_modules: [IDENTIFY_QUALITY_ATTRIBUTES, COMPARE_TRADEOFFS, INVERSION_DESIGN, RED_TEAM_CHALLENGE]
reversibility: fully_reversible
confidence: 4/5
---

# 决策：skill-auditor 新增"代码化合理性"维度的审查

## 问题陈述

父会话在 skill-auditor 新增第 10 个评分维度"代码化合理性"，改动涉及 3 个文件（SKILL.md Step 3 / rubric.md §3 权重表 + §4.10 + §4.11/4.12 序号 / refactor-playbook.md §10）。

需 gg 从架构师视角回答 5 个问题：
- Q1 维度独立性（vs Progressive Disclosure 边界）
- Q2 权重分配合理性
- Q3 判定可操作性（三分类稳定性）
- Q4 豁免条款抗滥用
- Q5 skill-auditor 自身的反身一致性

硬约束：rubric 必须可追溯 / 三档总分 100 / 只审不改 / 不引入 O(n²) / A 档不加维度。

## 输入文件

- `/Users/xuke/.agents/skills/skill-auditor/SKILL.md`
- `/Users/xuke/.agents/skills/skill-auditor/references/rubric.md`
- `/Users/xuke/.agents/skills/skill-auditor/references/refactor-playbook.md`
- `/Users/xuke/.agents/skills/skill-creator/SKILL.md`（权威底本）

## 推理结构

4 个原子模块按以下顺序组合：

1. **IDENTIFY_QUALITY_ATTRIBUTES** — 把 rubric 当作"评分装置"识别其质量属性（主导：判定稳定性 + 可追溯性）
2. **COMPARE_TRADEOFFS** — Q1 的"独立维度 vs PD 子项 vs 不加"三方案对比
3. **INVERSION_DESIGN** — 逆向枚举最糟设计选择（6 条），命中 4 条并修正
4. **RED_TEAM_CHALLENGE** — 针对 Q5 的反身一致性漏洞做正面处置

未选 LIST_FAILURE_MODES（和 INVERSION 重叠）、SKETCH_MINIMAL_MVP（本次是结构级选型不是 MVP）、RADIATION_CHECK（辐射面极小）。

## 辩论记录

### 激进派主张
- 代码化维度太保守，权重应提到 B 档 15 / C 档 20
- 废除"早期 skill"豁免
- 强制 auditor 自审生成缺陷清单
- 从 First Principles 看 skill 本质是"把行为硬固化为可复用资产"，文本指引是软固化

### 保守派主张
- 权重维持 10/15，先跑数据再调
- 豁免条款加硬约束（而非废除）
- 反身一致性是漏洞但可温和处置（self-audit.md + 提示而非强制完整自审）
- Imp+Why 是防长期腐烂主力，B 档应保持 12 而非 10
- 判定稳定性是最大风险，canonical 例子必须加

### 分歧与决议
| 分歧 | 决议 |
|---|---|
| 权重大小 | 采纳保守派维持 10/15，但微调 Imp+Why 10→12 |
| 早期 skill 豁免 | 采纳保守派加硬条件而非废除 |
| 反身自审 | 中间方案：立即 self-audit.md，Phase 3 后常规自审 |

## 最终方案

### 必做修正（5 项）

1. **Rubric §4.7 和 §4.10 加扣分路径分隔声明**（4.7 只查 references/ / 4.10 只查 scripts/）
2. **Rubric §4.10 新增 8 条判定锚点 + 判例库机制**（半确定性区间不硬化，争议案例沉淀到末尾）
3. **Rubric §4.10 豁免条款加硬条件**
   - 纯指引型：必须同时满足"无 Step N / 无执行动词 / 输出为开放内容"3 条
   - 早期 skill：必须满足"<30 天 且 metadata.version 未迭代过"
4. **Rubric §4.10 扣分梯度线性化**（1/2/3/≥5 → -20%/-40%/-60%/-80%，移除 -100% 档）
5. **新建 `~/.agents/skills/skill-auditor/self-audit.md`**（一次性反身违规声明）+ SKILL.md Step 4 报告结构加"代码化维度自审"一行

### 可选微调

B 档 Imp+Why 10→12，代码化 10→8（总分差 4.5%，不改变分档）

### 修改后的 B/C 档权重表

| 维度 | B 权重 | C 权重 |
|---|---|---|
| Frontmatter 完整 | 10 | 10 |
| Description 触发条件 | 20 | 15 |
| Description pushy 度 | 10 | 5 |
| 命名一致性 | 10 | 5 |
| 体量合规 | 10 | 15 |
| Imperative + Why | 12 | 10 |
| Progressive Disclosure | 10 | 15 |
| 代码化合理性 | 8 | 15 |
| 职责边界 | 10 | 10 |
| **总计** | **100** | **100** |

## Trade-off

5 条代价，见反思档。核心：
- 判定稳定性仍有飘忽空间（靠判例库机制兜底）
- 双标技术债（靠 self-audit.md 显式定价）
- Imp+Why 威慑力微损（1.5 总分级别）
- rubric 复杂度增加（多读 80 行）
- 长期威慑力依赖 Phase 3 真的发生

## 可逆性

**完全可逆**。所有改动都是 markdown 文字级，git revert 即可回滚，5 分钟成本。不触发 G4。

## 置信度

**4/5**

- 修正 1/2/3/5：5/5 信心
- 修正 4（梯度线性化）：4/5 信心（阈值偏主观）
- 可选微调：3/5 信心（对最终分档影响极小）
- 未到 5 的原因：判定锚点需实测验证 / 豁免条件仍有规避路径 / 双标技术债无法根治

## Q1-Q5 结论

- **Q1** 独立维度正确 + rubric 明文分隔扣分路径
- **Q2** 权重基本合理 + 微调 Imp+Why 保持更高威慑力
- **Q3** 必须加 8 条判定锚点 + 判例库机制
- **Q4** 豁免必须配硬条件
- **Q5** 设计漏洞但可显式定价，不撤回维度

## 二阶效应

1. **rubric 从"演绎规则"向"判例积累"的演化 precedent**——本次判例库机制可能是 rubric 整体演化方式的转折点，未来主观维度（Desc pushy / 职责边界）都应考虑引入
2. **self-audit.md 是"技术债显式定价"模板**——可复用到 gg 自己（候选 reasoning_module: EXPLICIT_DEBT_PRICING）
3. **代码化维度暴露 skill 生态的"文本固化瘾"**——5/10 自研 skill 会同时掉进警戒区，这是文化级预期管理问题

## 来自我的学习

1. **skill-creator 规范性语气分布**：Anatomy 小节是描述性，Improving/Writing Style 小节才是规范性。拉权威支撑要去后者而非前者
2. **判定锚点 = 规则的锚点化模式**：把抽象规则退化成 if-then 决策表是提升稳定性的技巧
3. **yellow flag 是弱规范词汇的典型**：官方用弱规范词时 rubric 扣分应渐进，强规范词才用硬门槛

## 执行方

父会话（Claude Code 主会话）。所有改动都是 Edit 操作，不需要 skill 调用。不 commit（按 gg 硬约束）。

## 反思链接

`memory/reflections/2026-04-13_skill-auditor-coding-dimension.md`

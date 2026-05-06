---
date: 2026-05-06
slug: audit-cleanup-nw-noise
type: design-session
summoner: Keith 直接对话（hourly-scan 14:18 alert 触发）
started_at: 14:20
ended_at: 17:10
---

# 设计会话反思：audit 21→0 清扫 + NW 推送噪音归属辨析

## 议题列表

1. hourly-scan 14:18 alert：gg audit exit=21（20 死链 + 1 命名违规）的拆解
2. Keith 提"我需要做什么判断"——简化为单一决策点
3. gg-audit skill 内引用的 path style：A（全 ROOT 相对路径）vs B（语义引用）vs 混合
4. Keith 拍板选 A（理由：gg-audit 是 gg 专属，跨项目自然性不构成约束）
5. 10 处编辑落地，audit 21 → 0
6. 16:25 第二条 alert：NW 未产出 + audit 残留快照
7. NW 推送的定义、原意图、设计弱点（60 min dedup 不匹配占位符 24h 锁定状态）
8. Keith 反问"这推送不是 gg 推的吗"——归属辨析时刻
9. Keith 决定"今天不用推"——dedup mtime 推到明天 09:00 静默今日

## 共识 / 变更清单

**path style 决策（已结）**：
- 选 A——gg-audit 内文档引用 gg 内部文件一律用 ROOT 相对路径（`memory/state.md` / `tools/persona-debate.md`）
- 理由：gg-audit 是 gg 专属 skill，不会装到其他项目

**修复落地（10 处）**：
- `.claude/skills/gg-audit/SKILL.md` ×2（L112、L125 工具名加 `tools/` 前缀）
- `.claude/skills/gg-audit/checkers/structural.md` ×2（L60-62 + L199 加 `memory/` 前缀）
- `.claude/skills/gg-audit/checkers/semantic.md` ×1（L30 加 `memory/`）
- `auto_gg.md` ×1（morning-brief 加 `cc-space/harness-engineering/analysis/` 跨项目前缀）
- `exploration.md` ×1（"（拟）"未归档会话改为文字描述，去 .md 反引号）
- `tracks/architecture.md` ×2（L245 personas/evaluator 候选去反引号 + L257 .template.md 补完整路径）
- `memory/next_session_agenda.md` ×2（L34 候选 evaluator 同上 + L67-76 批 B 标"已结 2026-05-06，选 A"）
- `scripts/check_structure.py` ×1（豁免 .template.md，与 README.md 同级例外）

**audit 验证**：21 → 0（exit=0，全绿）

**NW 推送今日静默**：
- `~/.agents/skills/notify/dedup/warning_morning-brief-nw-unproduced.last` mtime → 2026-05-07 09:00
- 行为：今日剩余 hourly-scan 推送被 dedup 跳过；明日若 NW 自愈则触发条件消失，若再失败则正常推一次

## 我这次哪里做得好 / 哪里差

**好**：
- 21 条违规分 6 类（A 设计决策待定 / B 真死链 / C 候选未来文件 / D path 残缺 / E 元噪音 / F 命名豁免缺失），辨识出 8 条早登记在 next_session_agenda L67-76 等 Keith 拍板，没盲扫
- 第一轮先输出方案分类等同意（D1 触发——超 3 文件），未盲修
- Keith 问"我需要做什么判断"时压缩到一个决策点（A/B/混合），尊重对方的认知带宽
- OCCAM 体现：personas/evaluator 候选用"去反引号"局部编辑而非动 audit 脚本噪音规则——少改比多改优

**差**：
- 第一次回应 NW 时把"修 NW 根因"和"修推送噪音"含糊化，一句"NW 是 cc-space 的事"把两件事捆在一起。Keith 反问"这推送不是 gg 推的吗"才厘清。**应一开始就拆开**：修复端在 cc-space，推送端在 gg。归属错位是真实的方法论盲点

## 元洞察（gg 演化本身的 learning）

**归属按"面"切分，不按"系统"切分**。NW 失败这一个信号同时涉及：
- 产出端（cc-space NW 子系统）
- 消费端（gg hourly-scan）
- 推送端（gg notify skill 链）
- 修复端（cc-space）
- 接收端（Keith）

我前一轮把"修复"这一面的归属（在 cc-space）当成了整个信号的归属，遮蔽了"推送策略全在 gg"这一面。Keith 反问 = 检测到我把多面合并成一面的含糊。

这是 gg 在跨系统治理问题上的一个隐性失败模式——值得沉淀。

**hourly-scan dedup 设计弱点**（次级洞察）：固定 60 min dedup 假设事件状态在窗口内可能变化；但"占位符已写入"型事件状态是 24h 锁定的，60 min dedup 必然违反 hourly-scan §0 自己的"静默是合法产出"哲学。修法 ABC 提出但 Keith 选了一次性静默，未做结构修——登记到下次议题。

## 下次继续

- **hourly-scan dedup 升级**：从"固定时长"升级为"按事件特性区分窗口"（候选选项 B：状态机识别"已锁定的失败态"，指纹加日期）。Keith 今天选了一次性静默，结构修登记 next_session_agenda 等主动触发
- **候选 evaluator persona**（Generator-Evaluator 分离）继续在 STRATEGIC Tier 3 等 Keith 拍

## KERNEL 改动清单

无。本次未触及 KERNEL.md。

## 代码质量

本轮代码产出：`scripts/check_structure.py` 加 `.template.md` 豁免（1 行修改）。豁免方式与 README.md 同形式（`fn == "X" or fn == "Y"`）保持一致，无技术债 / 安全隐患 / 死代码。

其余编辑都是文档 prose 改动，无代码层风险。

## 能力缺口

无新发现的能力缺口。本次工作流程顺畅，工具组合（Read / Edit / Write / Bash）已足够。

## 沉淀（写入 essence.md 的内容）

**ownership-by-facet**：跨系统信号的归属应按"面"切分（产出端 / 消费端 / 推送端 / 修复端 / 接收端），不是按"系统"整块归。"X 是 Y 的事"式裁决多半在合并多面——我前一轮把 NW 推送噪音含糊归给 cc-space，被 Keith 反问后才显形。产消错位是 LLM 在跨系统治理上的高发盲点。

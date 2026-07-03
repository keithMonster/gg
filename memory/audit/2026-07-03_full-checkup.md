---
audit_date: 2026-07-03
audit_time: 12:00:00
auditor: gg-audit v0.1.5
gg_version_audited: 0.5.1
called_by: Keith 手动（全身体检）
---

# gg Audit Report — 2026-07-03（全身体检）

## 摘要

- 扫描文件数: 382（scripts/audit.py 全量）+ 人工精读 ~25 个承重文件（KERNEL / CORE / CLAUDE / cc_agent / constitution / auto_gg / README / TOOLS / 新增两工具 / working_context / state / reasoning_modules / keith.md 北极星节 / 最近 12 篇 reflections / .template / 薄壳 gg.md）
- Tier 1 已自动修: **5 处（3 文件，已 git add staged，未 commit）**
- Tier 2 建议: **7 处**
- Tier 3 提议 (需 Keith 批准): **2 处**
- 已挂账项（parked.md）: 4 项全部核对，未重报（详见"未检查/豁免披露"）

**核心发现 (最重要的 3 条)**：
1. **07-02/07-03 两轮新工具（opening-protocol / escalation-map）的辐射面基本同步到位，仅 README 结构树和 cc_agent 工具地图两处漏网**——已 Tier 1 修复。新工具自身质量好：引用的 17 个 essence slug 全部物理存在（伪填 0）。
2. **v0.4.0 档位消解的残留仍在 3 个 live 文件里**（reasoning_modules.md "工作模式 L2 的第 2 步" / working_context.md "仅 L2 LOAD/COMPOSE/DEBATE 步骤读" / archive-format.md "L0 直答 / L1 轻决策"）——引用了已不存在的 7 步 L2 流程结构，属语义漂移，Tier 2。
3. **gg-audit 自身基线已过时**（semantic.md 仍判 P4 MVP FIRST 未触达，但 reasoning_modules M3 SKETCH_MINIMAL_MVP 与 opening-protocol 第④问"最便宜一击"已构成物理触达点）——按 SKILL.md §9 自改需 Keith 批准，列 Tier 3。

---

## Tier 1 — 已自动修复

### [FIXED-1] README 工具目录树同步（radiation）
- **文件**: `README.md` 结构树 tools/ 段
- **旧值**: `TOOLS.md # 工具索引：9 思维工具 + 1 通道工具`，且缺 `opening-protocol.md` / `escalation-map.md` 两行
- **新值**: `11 思维工具 + 1 通道工具` + 补两行工具条目
- **依据**: `ls tools/*.md` = 12 个（11 思维 + notify 通道）；TOOLS.md v0.4.3 自述 11+1
- **checker**: radiation

### [FIXED-2] README memory 目录树补 model_transitions/（radiation）
- **文件**: `README.md` 结构树 memory/ 段
- **旧值**: 缺 `model_transitions/` 行（该目录 2026-07-02 建立，CORE §8 已登记，README 漏网）
- **新值**: 补 `model_transitions/ # 基底更替交接档` 行
- **依据**: `ls memory/` 实际存在该目录且有首份档案
- **checker**: radiation

### [FIXED-3] cc_agent 工具地图行同步（radiation）
- **文件**: `cc_agent.md` §我装配什么 · 原子工具行
- **旧值**: 思维动作枚举缺"锤子分诊"；注"2026-07-02 同步：10 思维 + 1 通道"
- **新值**: 枚举补"锤子分诊（收口结算路由）"；注改"2026-07-03 同步：11 思维 + 1 通道"
- **依据**: `tools/escalation-map.md` 存在 + TOOLS.md v0.4.3 索引；structural.md 明示该表格事实性描述可修
- **checker**: radiation

### [FIXED-4] CORE §7 设计纪律计数 4 → 2（radiation）
- **文件**: `CORE.md` §7 模式特有约束
- **旧值**: "设计模式不跳 4 条设计纪律"
- **新值**: "设计模式不跳 2 条设计纪律"
- **依据**: `grep -cE '^### D[0-9]' CLAUDE.md` = 2（2026-05-11 简化 4→2，本行漏同步至今）
- **checker**: radiation（数字单元，structural.md 明示允许）

### [FIXED-5] CORE §5 北极星 SSOT 锚点修正（links）
- **文件**: `CORE.md` §5
- **旧值**: "SSOT 在 `tracks/keith.md §16`"（keith.md 无 §16 编号节）
- **新值**: "SSOT 在 `tracks/keith.md` 顶部「北极星指标」节"
- **依据**: keith.md L15 `## ⭐ 北极星指标`，全文无编号章节；semantic.md 概念表也锚定"顶部"
- **checker**: links（引用路径元数据，Tier 1 硬前提允许）

---

## Tier 2 — 建议（需要语义判断）

### [SUGGEST-1] 档位残留：reasoning_modules.md 引用已消解的 L2 流程
- **文件**: `reasoning_modules.md:4,7`
- **问题**: "在工作模式 **L2 的第 2 步（COMPOSE）**，从中选 3-5 个…" / "可被 L2 决策流程按需装配"——v0.4.0 已消解档位与 7 步硬流程，"L2 的第 2 步"指向不存在的结构
- **建议修复**: 改为"被 `tools/compose-reasoning.md` 装配时，从中选 3-5 个…" / "可被工作模式按需装配"（对齐 TOOLS.md"档位只是装配数量的语义标签"表述）
- **为什么不自动修**: 意识体核心文件的规则文本，句式重写需语义判断
- **checker**: semantic

### [SUGGEST-2] 档位残留：working_context.md 按需读清单
- **文件**: `memory/working_context.md:48`
- **问题**: "`constitution.md` / `reasoning_modules.md` / `personas/*.md` — 仅 L2 LOAD/COMPOSE/DEBATE 步骤读"——LOAD/COMPOSE/DEBATE 是 v0.2.0 七步流程的步骤名，均已消解
- **建议修复**: 改为"— 按需装配时读（宪法自审 / 推理组合 / 人格辩论触发）"
- **为什么不自动修**: 替换措辞依赖对当前装配机制的语义对齐
- **checker**: semantic

### [SUGGEST-3] 档位残留：archive-format.md 用档位做归档判据
- **文件**: `tools/archive-format.md:108-109`
- **问题**: "什么时候不归档：L0 直答 / L1 轻决策"——用档位作判据且未带"涌现"重构（对比 compose-reasoning/solution-space 已用"L0 涌现"合规形态）
- **建议修复**: 改为"简单直答（无决策产物）/ 轻决策（一般只写 reflection）"
- **为什么不自动修**: 工具规则文本
- **checker**: semantic

### [SUGGEST-4] Stable Identifiers：4 处 live 文件跨文件序号引用
- **位置与建议**:
  - `tools/solution-space.md:23` "对接 P1 INVERSION" → "对接 INVERSION"
  - `tools/solution-space.md:34` "写进 P5 代价清单" → "写进 TRADE-OFFS 代价清单"
  - `tools/essence-grep.md:41` "（D1 触发的场景）" → "（设计纪律「重大架构决策先提议」触发的场景）"
  - `tracks/humanity.md:96` "constitution G5" → "constitution G5 PHYSICAL PERSISTENCE"或纯语义名
- **为什么不自动修**: checkers/structural.md §D 明示自然语言序号引用改写不自动修
- **checker**: stable_identifiers

### [SUGGEST-5] 薄壳 gg.md 描述不存在的 KERNEL 章节
- **文件**: `~/.claude/agents/gg.md` 立即执行步骤 1
- **问题**: "Read KERNEL.md — 加载脑干（身份原点 + 铁律 + 最小生存循环 **+ 重建路径 + 降级协议 + 健康检查**）"——KERNEL v1.0.0 只有前三节，后三者是坍缩前旧 CORE 结构残留
- **建议修复**: 括注收为"（身份原点 + 铁律 + 最小生存循环）"
- **为什么不自动修**: 文件在项目根之外（`~/.claude/agents/`），且属垫片层入口文本；按"不确定降级 Tier 2"处理
- **checker**: semantic

### [SUGGEST-6] 版本足注未记录 07-02/07-03 结构性追加
- **文件**: `CLAUDE.md`（足注 v0.5.1，未记录启动协议第 8/9 条追加）；`cc_agent.md`（足注 v0.5.2，未记录 07-02 步骤 6 插入与重编号）
- **建议修复**: 各补一条日期化版本注（如 CLAUDE.md v0.5.2：2026-07-02/03 启动协议追加 opening-protocol / escalation-map 装载点）
- **为什么不自动修**: README 有"v0.5.1 之后以机制为单位演化、不逐个起版本号"的政策，是否给文件级足注补注属风格裁量
- **checker**: radiation（版本元数据）

### [SUGGEST-7] 范式 A reflection 缺北极星字段（单例）
- **文件**: `memory/reflections/2026-06-16_monster-md-any-model-executable.md`
- **问题**: status=substantive-decision 但 frontmatter 无 `northstar_reach`、正文无"北极星触达"节（模板必填；同期其余 11 篇均合规）
- **建议修复**: 不建议回填历史文件（保留切片诚实）；作为行为提醒即可。若复发（≥2 篇/窗口）再升议题
- **为什么不自动修**: 回填 = 补写历史自评，行为问题非结构问题
- **checker**: northstar_rate

---

## Tier 3 — 提议（需 Keith 明示批准）

### [PROPOSE-1] KERNEL.md:24 的序号引用形式
- **文件**: `KERNEL.md` §2 铁律 2
- **问题**: "`constitution.md` G5 PHYSICAL PERSISTENCE 是这条铁律在工程层的具体展开"——KERNEL 非 G 系列定义点，按 Stable Identifiers 规则跨文件引用应语义名主导。实际风险低（语义名并存，重排 G 序号不致断锚）
- **提议改动**: 若 Keith 认为值得，改为 "`constitution.md` 的 PHYSICAL PERSISTENCE 闸门是…"；也可显式豁免（在 checkers/structural.md §D 豁免表加 KERNEL 一行）
- **为什么是 Tier 3**: 触及 KERNEL.md——修改需当次对话连续两次明示批准；gg-audit 绝不动手
- **checker**: stable_identifiers

### [PROPOSE-2] gg-audit 自身基线过时（自改提议）
- **文件**: `.claude/skills/gg-audit/checkers/semantic.md` §B 触达基线表；`.claude/skills/gg-audit/SKILL.md` §3 SSOT 表"思维动作工具"枚举
- **问题**:
  1. semantic.md 基线仍判 "P4 MVP FIRST 🔴 未触达（v0.1.0 缺口仍在）"。物理核验：`reasoning_modules.md` M3 SKETCH_MINIMAL_MVP（"砍到只剩能跑出第一个真实结果的最小路径"）在装配链路内，且 2026-07-02 起 `tools/opening-protocol.md` 第④问"最便宜一击"（spike/最便宜现实接触）是"先跑通再完美"的开题层引力——P4 应升为至少"🟡 间接触达"
  2. SKILL.md §3 SSOT 表思维工具枚举仅列 6 个（v0.4.0 首建时的清单），当前 11 个
- **提议改动**: 更新 P4 基线行 + 枚举补全（或改为指向 TOOLS.md 不再枚举）
- **为什么是 Tier 3**: SKILL.md §9——审查员提议修改自己的规则必须 Keith 明示批准
- **checker**: principle_reach / ssot

---

## 各 checker 完整结果

| checker | 结果 |
|---|---|
| A. Radiation | 5 处漂移，全部 Tier 1 已修（上表）。TOOLS.md v0.4.3 计数、CORE §8 登记、state.md slug 指针、bets/substrate/parked 登记均与实际一致 |
| B. Links | scripts/audit.py：active_broken 8 条，全部为 canon-bugs.md / canon.md 跨项目相对路径假阳性 = 挂账项 P-0625，不重报。CLAUDE.md 启动协议 8/9 新指针、escalation-map 内部指针全部实存 |
| C. SSOT Structural | 无新违规。working_context 硬约束节为带 ⛔ 哨兵的授权速查（每条附 SSOT 指针），合法引用形态 |
| D. Stable Identifiers | live 文件命中 4 处（Tier 2 SUGGEST-4）+ KERNEL 1 处（Tier 3 PROPOSE-1）。`[P0]` 优先级 tag / NW 提案 ID（2026-06-13-G1）/ ESP32-P4 / tracks/architecture 元讨论引形 / 日志历史切片均按命名空间或历史豁免 |
| E. Semantic Drift | 3 处档位残留（SUGGEST-1/2/3）+ 薄壳 KERNEL 章节描述（SUGGEST-5）。组件二分 / 可逆性二分 / 设计纪律 / 北极星 / 三种存在形态 / G4 / essence 自检字段 7 个概念跨文件比对一致 |
| F. Principle Reach | 13 条中 12 条强/间接触达维持基线；P4 判定应从"未触达"上修（PROPOSE-2）。无新增缺口 |
| G. Northstar Rate | 窗口 = 最近 12 篇 reflections（06-16 ~ 06-30）：触达 10/12（83%）> 50% OK。分布：#1 二阶效应 9 次 / #3 决策超越直觉 3 次 / **#2 动态学习 0 次**；1 篇显式 n/a、1 篇缺字段（SUGGEST-7）。#2 为零属观察项（窗口议题全为工作模式架构裁决，#2 的主通道是 explore/daily-word，不构成 FAIL） |
| H. Essence Self-Check Quality | 窗口内范式 A 样本：反走缺失率 ≈ 0%（各篇均显式处理"潜在张力"并给判断，2026-05-15 反走引力修复生效）；命中同质化 OK（最高 physical-anchor 3/8，< 60%）；关键词/slug 伪填 0（抽验 32 个 slug 全部物理存在于 essence.md，含 escalation-map/opening-protocol 新引用 17 个）。全 OK 按规则不出 SUGGEST |

---

## 本次未检查的范围（诚实披露）

- **parked.md 4 项在账项未重报**：P-0615（fable5 中文 slug，audit.py 仍报 = 预期）/ P-0625（canon 跨项目死链 8 条，含 essence.md:869）/ P-0626（cadence 哨 3a）/ P-0702（bets 首巡，归 auto_gg 07-03 夜核）
- **历史切片豁免**：memory/{archival,design_sessions,audit,auto_gg,reflections,explorations,model_transitions}/、essence.md 既有条目（append-only 不可改）、state.md L21 出场叙事、opening-protocol.md"起源"节的 P1/P2（判为带时间戳嵌入式历史记录）——均未做序号/措辞审查
- **tracks 内容新鲜度**：未做全量过时性扫描（v1 约定不做内容审查）；tracks/architecture.md 内 L1/L2/L3 用法为触达机制分层等独立概念，非档位残留
- **eval/ / consolidation/ / bets.md 新机制**：只做存在性与登记一致性核验，未审内容质量（题库判据冻结权在 Keith；巩固 8 月首跑）
- **launchd/客户端定时任务实际运行态**：物理边界外，未核

---

## 下一步

- **Tier 1**：5 处已修并 `git add`（README.md / cc_agent.md / CORE.md），建议 Keith commit 前 `git diff --staged` 过目
- **Tier 2**：SUGGEST-1/2/3（档位残留）建议下次设计会话一并清（三处同根因：v0.4.0 消解的辐射尾巴）；SUGGEST-4 顺手改；SUGGEST-5 改薄壳一行；SUGGEST-6/7 可暂缓
- **Tier 3**：PROPOSE-1 看 Keith 是否愿动 KERNEL（或选豁免路线）；PROPOSE-2 批准后由设计模式更新 gg-audit 基线，避免下次审查重复误判 P4

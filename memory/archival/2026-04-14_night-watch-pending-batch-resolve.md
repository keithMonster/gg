---
date: 2026-04-14
slug: night-watch-pending-batch-resolve
summoner: cc-space 父会话（cc-space 工作台）
task_type: 批量决策（Night Watch pending 清算）
---

# Night Watch 11 条 pending 提案批量处置决策

## 召唤背景

cc-space 的 Night Watch 机制 pending 队列积压 11 条（最早 5 天），需要批量决断。父会话给出了初步判断，要求 gg 做反驳/支撑 + 决策矩阵 + 执行顺序。

## 核心反驳点（vs 父会话初步判断）

| 父会话倾向 | gg 反驳 | 证据 |
|---|---|---|
| G1 + G5 + G3-0409 三合一 MERGE | 反对。G1 是工具调用粒度（Edit vs Write），G5/G3-0409 是任务规划粒度。强合并两头不精确。**正确是二合一**（G5+G3-0409），G1 单独落 Code First | 04-09 日报明示"G5 是 G3 的超集"，无日报把 G1 与 Plan Mode 关联 |
| 2026-04-10-G1 REJECT（memory 够用） | 反对。04-10 日报明写"今日连续两次违反，memory 约束力不足"。应 EXECUTE，**但用扩写 Rule #5 方式**避免规则数膨胀 | 04-10 日报 [3b2f9450-2, 3b2f9450-6] |
| 2026-04-09-G2 "含义模糊可能 REJECT" | 反对（事实纠正）。具体场景是 01f85354 Turn 6，示例命令 `python3 test_api_call.py 300860` 被用户误解为真实执行。诉求明确，P2 归宿是一行字 MERGE 入 Communication Style | 04-09 日报 corrected 表第一行 |
| 2026-04-09-G4 REJECT（重复） | 同意方向，修辞修正：实质是 **CLOSE-AS-DONE**。04-10 日报已写"已写入，确认闭环"，是 jsonl 状态未同步导致的假 pending | harness-engineering/CLAUDE.md 顶部已有第一性原理段 |
| G4-0413 haiku DEFER | 同意，**加硬升级条件**。不带升级条件的 DEFER 是永久遗忘垃圾桶，违反 P8。建议 21 天硬闸，到期自动转 REJECT | 父会话自己说"P2 合理归宿是 REJECT" |

## 决策矩阵（11 条）

| ID | 处置 | 落地位置 | 置信度 |
|---|---|---|---|
| 2026-04-13-G3 (P0 Keychain) | EXECUTE | `~/.claude/CLAUDE.md` 新增 `## Security Red Lines` 段 | 5/5 |
| 2026-04-13-G1 (P1 串行 Edit) | EXECUTE | `~/.claude/CLAUDE.md` `## Code First` 段末追加一行 | 5/5 |
| 2026-04-13-G2 (P1 gg 误路由) | EXECUTE | `~/.claude/agents/gg.md` description 首句加强触发词 | 5/5 |
| 2026-04-13-S1 (P1 web-access 合并) | EXECUTE | `~/.agents/skills/web-access/SKILL.md` + 删 skill-notes | 5/5 |
| 2026-04-13-G4 (P2 haiku) | DEFER 21d | 硬升级条件：2026-05-04 截止，到期若无观测支撑自动 REJECT | 4/5 |
| 2026-04-10-G1 (P1 先搜 skill) | EXECUTE（扩写）| `~/.claude/CLAUDE.md` Engineering Rules **#5 扩写**，不新增 #9 | 5/5 |
| 2026-04-10-G2 (P2 subagent 限制) | EXECUTE | `cc-space/harness-engineering/CLAUDE.md` 新增"已知平台限制"段 | 5/5 |
| 2026-04-09-G3 + G5 | MERGE-EXECUTE | `~/.claude/CLAUDE.md` `## Workflow` 段完全重写为硬判定清单 | 5/5 |
| 2026-04-09-G2 (P2 示例代码) | EXECUTE | `~/.claude/CLAUDE.md` `## Communication Style` 段追加一行 | 4/5 |
| 2026-04-09-G4 (P2 第一性原理) | CLOSE-AS-DONE | 仅改 jsonl 状态，resolution: "已于 2026-04-10 写入，04-09 日报状态未同步" | 5/5 |

## 执行批次顺序

**第一批（立即，低风险）**：G3 → S1 → G2-0413 → 2026-04-10-G2 → 2026-04-09-G4 CLOSE
**第二批（Plan Mode 对齐，一次性改完全局 CLAUDE.md 三处小改动）**：G1-0413 + 2026-04-10-G1 + 2026-04-09-G2
**第三批（单独改动，最大一笔）**：G3-0409 + G5 MERGE 重写 Workflow 段
**第四批（延迟决策）**：G4-0413 DEFER 入 NW 观测队列

执行完后批量更新 proposals.jsonl status 字段。

## 规则膨胀核算

- 全局 CLAUDE.md 净增：~12 行（约 360 tokens 入场费）
- 项目 CLAUDE.md：0
- 工作区 CLAUDE.md（harness）：+3 行
- 规则条数净增：1 条（Workflow 清单，替代原 2 行模糊版）
- Keith 新信息点：~6 条

相较 11 条全 EXECUTE（11 个新信息点），**阅读成本节省约 45%**。

## 置信度 + 可逆性

- 整体置信度：4.9/5
- 所有处置全部可逆（markdown + jsonl 改动）
- **G4 IRREVERSIBILITY Gate**：不触发，无不可逆项

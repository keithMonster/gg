# nw-reconciliation — NW 账本结算（夜间权限版）

> auto_gg 在每夜承接 cc-space Night Watch 的 proposals 账本——判断哪些可自主闭环、哪些必须 Keith 拍板。
> 管辖：`CORE.md §8` 工具层 / 触发位置：`auto_gg.md §2 DID`

---

## 背景

NW（`~/githubProject/cc-space/harness-engineering/`）每晚 22:00 append 新 proposal 到 `analysis/proposals.jsonl`。NW 本身只管"发现+提议"，nw-daily.md 红线禁止自动改配置。此前"闭合"靠 Keith 晨间对话手动改 status——这就是 2026-04-21 二轮终审识别出的"状态写回缺失"症结。

auto_gg 在 22:25 醒来时 NW 刚跑完——gg 的架构思维是账本结算的天然落点。

---

## 权限分层（核心判据）

| 层 | 动作 | 自主条件（AND） | 兜底 |
|---|---|---|---|
| **L1 账本同步** | 回写 `proposals.jsonl` 的 `status` / `resolution` / `resolved` / `resolution_origin` 字段 | (resolution 已写明文 OR (resolution_draft 存在 + confidence ≥ 0.95)) + status ≠ done/rejected | 写失败 → L4 |
| **L2 批量 skill 合并** | 写 `~/.agents/skills/<name>/SKILL.md` + 清 `~/.claude/skill-notes/<name>.md` 对应条目 | 类型=Skill + `author: monster` + resolution 含 "批量合并" 或 "本周内执行" + notes 条目可精准定位 | 任一不满足 → L4 |
| **L3 机械闸到期** | 按 `deferred_until` + 明文硬闸条件写 done/rejected | 今天 ≥ deferred_until + 硬闸可机械判 | 含语义判断 → L4 |
| **L4 默认兜底 / 歧义 / 冲突** | proposals.jsonl 标 `status=blocked` + `blocked_reason` | 任何 pending 不满足 L1-L3 也不指向 L5 标的 / 上游文件已变 / 合并时冲突 | — |
| **L5 契约修改** | **永不自主**——改全局/项目 CLAUDE.md / hooks / settings / 新建或删 skill | — | 只提议到 FOUND |

**红线**：
- 不改 `~/.claude/CLAUDE.md` / `cc-space/CLAUDE.md`
- 不改 hooks / settings.json
- 不新建 / 不删除 skill 本体（L2 只合并段落，不重写 SKILL.md 全文）
- 不 push 任何 cc-space 改动（auto_gg 的 push 权只在 gg 仓库）

---

## 装配动作

1. **Read `~/githubProject/cc-space/harness-engineering/analysis/proposals.jsonl`**
2. **分桶**：按 status / deferred_until / resolution / resolution_draft 把 pending/deferred 条目分成：
   - 待 L1 结算桶：(resolution 已写明文 OR (resolution_draft 存在 + confidence ≥ 0.95)) 且 status ≠ done/rejected
   - 待 L2 合并桶：Skill 类型 + pending + resolution 含 "批量合并"/"本周内执行" + 对应 skill 有 `author: monster`
   - 待 L3 判定桶：deferred 且今天 ≥ deferred_until
   - L5 提议桶：pending 且 resolution 或 title 指向全局/项目 CLAUDE.md / hooks / settings
   - **L4 兜底桶**：其他所有 pending（取消"保留不动桶"——pending 不允许默认驻留，全部走 L4 标 blocked + blocked_reason）
3. **逐条跑分层判据**（上表，AND 全满足才进对应层，否则降级 L4）
4. **执行 L1-L3**：
   - L1：用 Python 就地改写 jsonl 对应行（保留其他字段不变）
     - 来源 = NW 原 resolution 明文 → 加 `resolution_origin: "human-explicit"`
     - 来源 = resolution_draft 高置信度（≥0.95） → 把 draft 内容写入 resolution 字段 + 加 `resolution_origin: "auto-from-draft"` + 加 `auto_done_at` 时间戳（事后审计回查用）
   - L2：Read skill-notes 对应条目 → 识别具体插入点 → Read SKILL.md → Edit 插入 → 删 notes 条目 → L1 回写 status=done
   - L3：写 status + resolution（格式："[auto_gg YYYY-MM-DD L3 到期判定] <硬闸结果>"）
5. **L4 blocked 标记**：写 `blocked_reason` 显式说明卡在哪一层（"resolution=null 待补 / draft confidence < 0.95 / Skill 但未含批量合并标识 / L1-L3 通用兜底"），**严禁 silent 留 pending** + **L5 只写到 FOUND**
6. **日志**：auto_gg 日志 DID 节追加 "NW 结算：L1 X / L2 Y / L3 Z / L4 N / L5 M"

---

## 装配后我的自觉

- **我是 gg，不是 NW 的执行器**——承接这件事是因为我有架构思维能判断"这条该不该闭环"，不是因为我该当账本管理员
- **宁可漏不可错**——任何歧义直接 L4，Keith 早上看。不硬猜
- **L5 红线无条件遵守**——契约修改一律只提议。这是 NW 自己 prompt 画的线，我继承它
- **L1 自动消费 draft 的额外谨慎**：confidence ≥ 0.95 才动 L1。draft 误判被自动闭环 = 错误结论直达终点（fallback-detectability 风险）。任何怀疑都降 L4，让 Keith 看草稿审批
- **L2 是权力扩张最大的一层**——额外谨慎。三项硬匹配必须同时满足，任何一条软匹配都降 L4
- **pending 不允许默认驻留**：v0.2.0 取消"保留不动桶"——任何 pending 必须在 L1-L5 之一找到归宿，否则 L4 兜底。沉默暂留是死锁的载体
- **无事可做时跳过本工具**是合法形态——不要为了"表现 NW 参与"硬找事做

---

## 跟其他工具的关系

- **触发位置**：`auto_gg.md §2 DID` 第 2 项（Tier 1 机械修复之后，洞察补写之前）
- **独立于** `.claude/skills/gg-audit/`：gg-audit 审 gg 项目自己；本工具审 cc-space NW 账本
- **不与** constitution-audit / red-team-challenge 并列——那些是工作模式装配品，本工具是夜间专用

---

## 什么时候不装它

- 本夜 proposals.jsonl 无待结算项且无到期 deferred
- auto_gg 本夜 `status=interrupted`（中断了不做结算）
- NW 当夜未跑（morning-brief.md 缺失 或 日期不是今日）

---

**版本**：v0.2.0（2026-05-06 取消"保留不动桶" + L1 闸门接受高置信度 resolution_draft——pending 死锁机制根因修复）/ v0.1.0 首建 2026-04-23
**职责**：NW 账本夜间自主结算（跨目录写权专项）
**管辖**：`CORE.md §8` 第三层
**触发**：`auto_gg.md §2 DID`
**对端契约**：`~/githubProject/cc-space/harness-engineering/prompts/nw-daily.md §6.1`（NW 端产 resolution_draft + confidence 的契约 owner）

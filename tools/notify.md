# notify — gg 主动外推通道

> **物理实现已上提为全局 skill**：`~/.agents/skills/notify/`
> 本文件是 gg 视角的薄壳，记录 gg 任务（hourly-scan / auto_gg / 被召唤的 gg）何时调用全局通道。

---

## 调用入口

```bash
~/.agents/skills/notify/bin/notify.sh <severity> <source> <message> [--context f1,f2] [--task-id ID]
```

完整文档：`~/.agents/skills/notify/SKILL.md`。

---

## gg 项目内的使用约定

| 场景 | source | severity | 关联 |
|---|---|---|---|
| hourly-scan 异常 | `hourly-scan` | warning / critical | 出问题的文件路径 |
| auto_gg 夜间 P0 | `auto_gg` | warning | 议题相关文件 |
| 被召唤的 gg 在 Keith 离开后完成长跑 | `gg-summoned` | info | 决策档案 / 新写文件 |

**默认不调用**：
- 工作模式 / 设计模式下 Keith 在场 → 直接对话，不外推
- auto_gg 静默夜（无 FOUND 无 DID）→ 不外推
- 重复同类异常（< 60 min）→ 走去重，跳过

---

## 何时这个工具被装配

**通道工具，不参与思考装配**。在 `tools/TOOLS.md` 的"通道工具"区段——执行时调用，不进会话上下文。

只有在 gg 任务**已经决定要外推**时才调用一次 `notify.sh`，不需要"装配 notify.md 来思考"。

---

## 安全边界

跟着 `CORE.md §7` 可逆性二分框架：

| 操作 | 类别 |
|---|---|
| 调用 notify.sh | 可逆（自主调用，trace 自动留痕） |
| 修改全局 .env / webhook URL | 不可逆（仅 Keith 明示授权） |
| 删除 sent/ 历史 trace | 不可逆（事件账本，永不自主清） |

完整规则在 `~/.agents/skills/notify/SKILL.md`。

---

## 版本

- v0.2.0（2026-05-06）— 物理实现上提为全局 skill；本文件改为薄壳
- v0.1.0（2026-05-06）— 首版（gg 内部 notify.sh）

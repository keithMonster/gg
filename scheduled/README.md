# gg scheduled — gg 项目的 launchd 定时任务

> 全局技能 `~/.agents/skills/scheduled/SKILL.md` 是这套机制的总入口。本文件只记录 gg 项目特有的东西。

## gg 已有任务

| Label | 触发 | 职责 | prompt 入口 |
|---|---|---|---|
| `com.gg.hourly-scan` | 每小时 :23 | 轻量状态扫描 + 异常告警 | `HOURLY_SCAN.md` |

## 命名约定

- Label：`com.gg.<task>`
- 文件：`plists/<label>.plist`
- 日志：`logs/<label>.YYYY-MM.log`（月度滚动，run-task.sh 自动产出）
- 告警：`alerts/YYYY-MM-DD-HHmm.md`（hourly-scan 异常时写入）

## 跟 cc-space 的分工

- `com.cc-space.*` → cc-space 自己的工作流（cgboiler tick / NW 等）
- `com.gg.*` → gg 作为系统管理员的横切监控
- gg 的任务可读 cc-space 的产出，但不修 cc-space（修复留给 auto_gg 夜间或被召唤的 gg）

## 工作流速查

详见 `~/.agents/skills/scheduled/SKILL.md`。常用命令：

```sh
# 列出 gg 任务
launchctl list | grep com.gg

# 看任务详情
launchctl print gui/$UID/com.gg.hourly-scan

# 立即触发一次（调试用）
launchctl kickstart -k gui/$UID/com.gg.hourly-scan

# 装 / 改 / 删
scheduled/bin/install.sh   plists/com.gg.<task>.plist
scheduled/bin/uninstall.sh com.gg.<task>

# 看日志
scheduled/bin/logs.sh com.gg.hourly-scan
scheduled/bin/logs.sh com.gg.hourly-scan -f
```

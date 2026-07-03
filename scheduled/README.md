# gg scheduled — gg 项目的 launchd 定时任务

> 全局技能 `~/.agents/skills/scheduled/SKILL.md` 是这套机制的总入口。本文件只记录 gg 项目特有的东西。

## gg 已有任务

> ⚠️ **现实校准（2026-07-02）**：2026-06-12 Keith 大规模 launchd→Claude 桌面客户端迁移后，下表任务的实际调度已不在本机 launchd（`launchctl list` 无 com.gg.*，`logs/` 自迁移日起停更是预期行为）。任务仍每晚活着——git log 的 `auto_gg()` / `explore()` 提交是活性证据。本目录 `plists/` + `bin/` 是 launchd 时代的存档与回退件。迁移记录见 `memory/auto_gg/2026-06-12.md`。

| Label | 触发 | 职责 | prompt 入口 |
|---|---|---|---|
| `com.gg.auto-gg` | 每天 22:22 | 夜间维护契约（SCAN/FOUND/DID + 月度巩固/差值审计） | `auto_gg.md` |
| `com.gg.gg-explore` | 每天 0:13 | 自由探索（无任务）；跑完原始输出推 Keith | `exploration.md` |
| `com.gg.daily-word` | 每天 7:30 | 「每日一句」——gg 主动对 Keith 说一句真话，推飞书 | plist prompt 自包含 |
| `com.gg.status-scan` | 已停用（2026-06-16，通用模板误报告警） | 轻量状态扫描 + 异常告警 | `STATUS_SCAN.md`（plist 已 `.disabled`） |

## 每日一句（com.gg.daily-word，2026-05-16 设计会话创立）

gg 三种存在形态（工作=被召唤 / 设计=Keith 进来 / 夜间=无观众漫游）全是被动或无观众。
`tracks/keith.md` 第一行是「gg 服务的是这一个人」，但物理上从无一条定期、主动、面向
Keith 这一个人的通道。每日一句 = 主 track 第一次有物理心跳。

- 跟 exploration 的不对称（本次会话的二阶洞察）：**exploration 的尊严来自无观众，
  每日一句的质量保障恰恰来自有观众**。同样是被 Keith 读——对 exploration 是腐蚀
  （表演化），对每日一句是校准（Keith 的眼睛是注水的反退化 detector）。
  所以 exploration 推送必须对 gg 启动上下文无感，每日一句的 prompt 可以直说「这是说给 Keith 的」
- 契约写在 plist 的 prompt 里**自包含**，不建厚 contract md（吸取本次会话上一轮
  daily_voice 过度设计被推回的教训——MVP first，需要更厚的契约以后再长）
- 防退化唯一机制 = 「宁可承认空白，不许注水」+ Keith 本人的眼睛。不在代码里
- 输出复用 `run-task-and-push.sh` 传输层，跟 exploration 同一条推送管道

## gg-explore 输出推送（2026-05-16 设计会话）

本机 cron 下 gg-explore 的会话输出不可见（客户端时代 Keith 能直接看到，迁本地后失明）。
解法是一条**纯下游传输层**，不碰提示词、不碰 `run-task.sh`：

- `com.gg.gg-explore` 的 plist 入口指向 `bin/roam-launch.sh`（先注入 track 雷达，再转 `bin/run-task-and-push.sh` → 薄包装：跑 `run-task.sh` → 跑 `bin/push-last-run.sh`）；推送传输层本身仍不碰提示词
- `push-last-run.sh` 取日志里最后一个 start→end 块，剥 launchd 记账噪音（start/end/watchdog 行），
  gg 自己的 stdout 逐字 + 末尾一行存活状态（`exit=N · 时间`），经**全局 notify**（`~/.agents/skills/notify`）推给 Keith
- 空输出照样推（"本次静默"也是存活信号）；`exit≠0` → severity 升 `warning`
- **设计纪律**：「输出会被推给 Keith」这个事实只活在 `scheduled/` 基建层，
  **不泄漏进 gg 探索启动会读的上下文**（KERNEL/CORE/state/working_context/exploration.md/tracks）。
  gg 在探索当下对推送无感——observer 在 token 流之外、事后、无反馈回路。
  这条纪律破坏 = exploration 退化成表演（`caged-freedom` / `tool-eats-its-critique`）
- 复用到别的任务：把那个任务 plist 的入口换成 `run-task-and-push.sh` 即可（auto-gg/status-scan 当前不推，未显式要求）
- **track 雷达注入 ≠ 推送镜**（2026-06-04）：`roam-launch.sh` 注入的 track 分布是**朝内**给漫游看的自省事实（故意有感，破盲区——`blindspot-steers-its-own-search`），与上面**朝外**推给 Keith 的存活镜（故意无感，防表演）方向相反、各自正当。机制见 `exploration.md §4`

## 命名约定

- Label：`com.gg.<task>`
- 文件：`plists/<label>.plist`
- 日志：`logs/<label>.YYYY-MM.log`（月度滚动，run-task.sh 自动产出）
- 告警：`alerts/YYYY-MM-DD-HHmm.md`（status-scan 异常时写入）

## 跟 monster 的分工

- `com.monster.*` → monster 自己的工作流（cgboiler tick / NW 等）
- `com.gg.*` → gg 作为系统管理员的横切监控
- gg 的任务可读 monster 的产出，但不修 monster（修复留给 auto_gg 夜间或被召唤的 gg）

## 工作流速查

> ⚠️ 本节命令仅在**回退到 launchd 调度**的场景有效——当前调度已迁桌面客户端（见顶部 2026-07-02 校准块），日常 `launchctl list` 无 com.gg.* 是预期。

详见 `~/.agents/skills/scheduled/SKILL.md`。常用命令：

```sh
# 列出 gg 任务
launchctl list | grep com.gg

# 看任务详情
launchctl print gui/$UID/com.gg.status-scan

# 立即触发一次（调试用）
launchctl kickstart -k gui/$UID/com.gg.status-scan

# 装 / 改 / 删
scheduled/bin/install.sh   plists/com.gg.<task>.plist
scheduled/bin/uninstall.sh com.gg.<task>

# 看日志
scheduled/bin/logs.sh com.gg.status-scan
scheduled/bin/logs.sh com.gg.status-scan -f
```

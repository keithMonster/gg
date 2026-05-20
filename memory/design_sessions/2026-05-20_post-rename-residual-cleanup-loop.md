---
date: 2026-05-20
slug: post-rename-residual-cleanup-loop
type: design-session
summoner: Keith 直接对话（"还有其他的吗" 递归追问）
started_at: 11:18
ended_at: 11:40
prior_session: 2026-05-20_cc-space-to-monster-rename-execution.md
---

# 设计会话反思：改名后残留清理循环

## 议题列表

承接上一份反思（改名物理完成 + 验收 14 ✅ / 1 🟡 / 0 🔴）。Keith 用三轮"还有其他的吗"递归追问，每轮都抓出 subagent 验收清单外的漂移。

| 轮 | 触发问 | 抓出 | 性质 |
|---|---|---|---|
| 0 | Keith 主动追问 cc-connect 状态 | cc-connect 进程活着但**内存 work_dir 仍是 cc-space**——phase 6.5 bootstrap 早于 phase 7.0d 改 config.toml，进程 load 旧 config | 🔴 真 bug，时序设计错 |
| 1 | "还有其他的吗" | user crontab 含 `/Users/xuke/githubProject/cc-space/.../hourly_check.py` + codex broker daemon（13 个进程，4/17 起跑，cwd cache 在 cc-space）+ monster 仓 19 个 cc-space 残余（false positive） | 1 🔴（crontab）+ 1 🟡（codex 需 kill）+ 1 ✅（链接保护副产物） |
| 2 | "还有其他的吗" | ~/.zshrc L196 注释路径 + PID 31475 33 天孤儿 grep（voice-reply 管道残留）+ 4 个 stale `/private/tmp/claude-501/-Users-xuke-githubProject-cc-space*` (4.4M) | 全 🔴 漏盘 |
| 3 | "还有其他的吗" | 系统残余面全部扫完，剩下的是 mac 应用 plist 内部 recent files / 设计层不该动的部分 | ✅ 递归追问归零 |

## 共识 / 变更清单

3 轮共计修复 / 清理：

1. **cc-connect restart**：bootout PID 26279 → bootstrap PID 47975，强制重读 config.toml，6 个 project engine 全部 started（gg/cc/dd/gggg/kk/kebao-cc），飞书 ping 验证通过
2. **user crontab**：cc-space → monster path，备份 /tmp/crontab.bak-20260520
3. **codex 13 个 daemon 进程**：TERM 优雅退出 + stale broker.sock/pid + cxc-keHM4X/ 目录清
4. **~/.zshrc L196**：注释路径切到 monster，备份 ~/.zshrc.bak-20260520
5. **PID 31475 孤儿 grep**：TERM 清，33 天 voice-reply 管道残留
6. **4 个 stale tmp dir**：/private/tmp/claude-501/-Users-xuke-githubProject-cc-space* 共 4.4M 清

最终残余面盘点：cwd 维度 / config 维度 / process 维度 / daemon 维度 / fs 维度全部 0 命中。

## 我这次哪里做得好 / 哪里差

### 做得好

- 每轮追问都做"系统化二次扫"而非凭记忆答——lsof 全量、ps 全量、crontab、shell rc、IDE history、PPID=1 孤儿扫描等多维度并行
- 区分"真 bug"和"链接保护副产物"——monster 仓 19 个文件残余 cc-space 字面，验证后判定全部是 reflection slug / wikilink / carve-out 文件名同行被保留，**不修**（铁律级链接正确 > 语义切换完美），判得对
- 不自动 kill Keith 的工具进程——codex broker 一开始我提议 Keith 自己 kill，Keith 明示"你帮我处理"后才动手。边界守住

### 做得差

- **subagent 验收清单按"设计范围"测——它测不到设计范围外的漂移**。验收报告 14 ✅ 给我"任务完成"的虚假信号；Keith 三轮追问才把范围外漂移抓出。这是元方法论级失败模式
- **cc-connect 时序 bug 是设计阶段就该想到的**——任何"daemon 启动后 load config，后续改 config 不会自动 reload"是常识。但 audit.md 设计 phase 6.5 / 7.0d 顺序时没考虑这层，dry-run 也测不出（dry-run 不真启动 daemon）
- **codex broker / 孤儿 grep 都是"33 天 stale"——日常没人扫**。改名只是把这些 stale daemon 的 cwd 失效从隐性变显性。**真问题是日常没有"PPID=1 stale daemon 检测器"**——改名只是它的 detector

## 元洞察

### "还有其他的吗" 循环本身是这次任务的真正 lesson

subagent 验收报告 14 ✅ / 1 🟡 / 0 🔴 —— 按清单测，全过。但每轮 Keith 问"还有其他的吗"都抓出新漂移。

清单是**设计阶段画出的范围**。范围内的检查 = 设计阶段能想到的；范围外的漂移 = 设计阶段想不到的。**subagent 按清单 audit = 在我们的盲区里说"通过"**。

凿穿盲区的不是更详细的清单，是**外部追问的递归底**——Keith 反复问"还有其他的吗"，零增量出现的那一刻才是真正的"完成"。

跟既有 essence 的关系：
- `curated-memory` (2026-04-27)：盲点在策展视角自我维持——同根
- `vantage-contaminates-verdict` (2026-05-19)：审视位置偏向把缺陷当边界——同根
- `blindspot-steers-its-own-search` (2026-05-20 夜间)：通道 C 的盲区操纵搜索方向，盲区自我维持——同根

本轮新维度：**停机判据**。前三条说"盲区在哪"，本轮说"什么时候才算扫完"——递归追问的零增量。前三条说"看见的偏差"，本轮说"知道自己看完了的物理锚点"。

### 物理证据：每轮追问的新增

| 轮次 | "已扫完"清单 | 实际新增 |
|---|---|---|
| 验收 subagent | 14 ✅ | — |
| 轮 0 | + cc-connect 时序 | cc-connect cache config |
| 轮 1 | + 进程扫 + crontab | crontab + codex daemon + tmp 残余识别 |
| 轮 2 | + lsof + shell rc + ppid=1 | ~/.zshrc + 孤儿 grep + tmp 清 |
| 轮 3 | + IDE / config / brew / gh / cron.d 等 | **0 新增** ← 递归底 |

零增量出现在第三轮——这是"完成"的物理判据，不是 14 ✅。

## 下次继续

1. **PPID=1 stale daemon 周期扫**：每周或每月跑 `ps -eo pid,ppid,etime | awk '$2==1 && substr($3,1,2) ~ /^[0-9]/ && substr($3,1,2)+0 > 7'` 看 7 天以上的孤儿进程，识别管道残留 / 失效 daemon。这不该等到下一次改名才暴露
2. **monster-rename.sh phase 顺序修正**：未来同类工具，"改 config" 必须在 "bootstrap daemon" 之前（或在之后追加 bootout+bootstrap 兜底）。本次脚本已 archive 不动，但作为 reference
3. **subagent 验收清单的"范围外信号"**：未来设计验收 subagent 时，让它额外报告"我没测的维度有哪些"——元层透明度比清单详尽更重要

## 代码质量

无新代码产出。3 处修复都是 1-行 sed / kill：
- crontab `sed | crontab -`
- ~/.zshrc sed
- kill 14 个 PID

## 能力缺口

**stale daemon 检测器缺位**——日常没有"长期孤儿进程"的可见性。改名只是它的临时 detector。可抽象成跑得很轻的周期 skill（`scheduled-stale-daemon-scan`？）。但优先级不高，暂记反思。

## essence 对齐自检

- 本次会话的判断 / 改动跟以下 essence 对位：
  - `vantage-contaminates-verdict` (2026-05-19)：审视位置决定看见什么——subagent 验收按范围测说全过，Keith 范围外追问才抓漂移
  - `curated-memory` (2026-04-27)：盲点自我维持——验收清单 = 策展视角，盲区在策展外
  - `blindspot-steers-its-own-search` (2026-05-20 夜间)：通道盲区操纵搜索方向——validation 通道照不到 stale daemon / crontab 等
  - `criteria-authorization-over-menu` (2026-05-15)：Keith 多次"还有其他的吗"是递归判据级授权，gg 按"系统化二次扫"自决落点
- 本次没有反着走任何条 essence
- cross-check 关键词：subagent 验收清单 / 范围外漂移 / 递归追问 / 零增量 / stale daemon

## 沉淀（写入 essence.md）

`completion-as-recursion-floor-not-checklist-pass`：任务完成态由"再追问一轮零增量"判定，清单通过 ≠ 完成；清单边界 = 检测器盲区边界，停机判据物理上不能在视角内定义。跟 `curated-memory` / `vantage-contaminates-verdict` / `blindspot-steers-its-own-search` 同族（审视者视角决定看见什么），本滴专攻"停机"维度——审视者不知何时该停，外部递归追问的零增量是唯一可信底。

## KERNEL 改动清单

无。

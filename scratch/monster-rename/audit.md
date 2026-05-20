---
date: 2026-05-20
slug: monster-rename-audit
type: rename-execution-audit
auditor: gg-design-mode
executor: same gg session
---

# monster-rename 审核 + 决策记录

> 原文档：`brief.md`（cp 自 cc-space/inbox/briefs/）
> 原脚本：`monster-rename.sh`（已修过，见 §修改清单）
> 单行回滚：`bash rollback.sh`
> 回滚使用说明：`ROLLBACK.md`

---

## §1. 文档原始覆盖度审计

cc-space 内会话写的 brief 是从 cc-space 视角盘点的。gg 这一侧（执行端）做了二次扫描，发现以下漏点：

### 1.1 cc-connect 整条链路漏盘（Keith 在审核第 2 轮主动指出）

| 漏点 | 影响 | 处理 |
|---|---|---|
| `com.cc-connect` 是**第 14 个 launchd label**（活跃 PID 91598） | 文档 §3 验证基线说 "13 个 com.cc-space"——漏第 14 个独立 label | 新增 phase 2.5 / 6.5 |
| `~/.cc-connect/config.toml` 4 处 `work_dir = ".../cc-space"`（项目 gg/cc/dd/kk） | mv 后 4 个飞书 bot + 1 个企微 bot 死循环（launchd KeepAlive） | phase 7 增 sed |
| `~/Library/LaunchAgents/com.cc-connect.plist` | 内容不含 cc-space，不需改；但 bootout/bootstrap 时序必须正确 | 见 phase 2.5/6.5 时序 |
| cc-connect 服务的 attachments 目录 `cc-space/.cc-connect/attachments/` | 随仓 mv，work_dir 改对即自动接管 | 无需独立处理 |

### 1.2 gg 自身辐射漏盘

文档 phase 7.5 只改 `gg/CLAUDE.md`，但 gg 活文件清单**13 个**（实测 grep 后排历史档/essence 得出）：

```
./auto_gg.md
./cc_agent.md
./CLAUDE.md
./memory/next_session_agenda.md
./memory/state.md
./scheduled/README.md
./scheduled/STATUS_SCAN.md
./tools/nw-reconciliation.md
./tools/TOOLS.md
./tracks/architecture.md
./tracks/cc.md
./tracks/humanity.md
./tracks/keith.md
```

**显式 NOT IN 清单（绝对不动）**：
- `memory/essence.md`（KERNEL §2 append-only 铁律——改既有条目违反脑干）
- `memory/{reflections,design_sessions,archival,audit,auto_gg,explorations}/*`（历史档，essence `fast-slow-divide`：修归档 = 篡改快照）

### 1.3 ~/.claude/ + ~/.agents/ 全量盘漏

| 漏点 | 实证 |
|---|---|
| **E** `~/.claude/agents/gg.md` | gg subagent 入口，L26 含 "cc-space" |
| **F** `~/.agents/skills/` 11 处 | 文档只盘 3 个（done/notify/text-to-podcast），实际还有 `rtk-curl / voice-reply / scan-knowledge / diagnose / skill-auditor / multi-agent-docs / scheduled / product-design-prelude`，含 `notify/bin/notify.sh` |
| **G** `~/.agents/skill-notes/done.md` | skill 反哺笔记 |
| **H** `~/.claude/scheduled-tasks/auto_cc_space/` | 目录名 + 内部 SKILL.md 含 cc_space（下划线） |
| **I** `~/.claude.json` (583K) | 6 处 cc-space：CC 顶层状态库（project 注册 + worktree + GitHub identifier + task history prompt） |
| **J** `~/.gk/repoMapping.json` | gk 仓映射（github/keithMonster/cc-space + path） |
| **K** `~/Library/Caches/claude-cli-nodejs/-Users-xuke-githubProject-cc-space*` | 8 个 CC CLI cache 目录（cwd-hash 命名，cc-space session resume 依赖） |

### 1.4 carve-out 链接断裂（最严重 bug）

cc-space 内 **19 个活文件**含对 3 个 historical 文件的 cross-reference（`cc-space-as-living-trunk` / `cc-space-memory-decommission` / `cc-space-design-system`）。原脚本 sed_in_repo 排除规则只覆盖**文件自身**，不覆盖**活文件里指向这些文件的字符串**——一跑就把活文件里的引用改成 `monster-as-...`，目标文件按 carve-out 保留原名 = 19 个文件 N 处链接全部 404。

---

## §2. 决策表（Keith 批准）

| Q | 决策 | 落点 |
|---|---|---|
| Q1 | **A 彻底改**：`com.cc-space.auto-cc-space` → `com.monster.auto-monster`；`~/.claude/scheduled-tasks/auto_cc_space/` → `auto_monster/` | phase_3 plist rename 用全量替换；新增 phase 7.8 mv scheduled-tasks 目录 |
| Q2 | **b 只改绝对路径**：~/.claude.json 用 `sed s\|/Users/xuke/githubProject/cc-space\|/Users/xuke/githubProject/monster\|g`，不改单词 cc-space（保留 GitHub identifier + task history prompt 字面） | phase 7.1 增补 |
| 整体 | 留好退路——失败时单行回滚 | 见 `rollback.sh` |

---

## §3. 脚本修改清单（原 → 改后）

| # | 原 | 改后 | 理由 |
|---|---|---|---|
| **M1** | `sed_in_repo` 排除规则只覆盖历史叙事文件**自身** | 增加 `EXCLUDE_HISTORICAL_TOKENS` 数组，sed 前用 `awk` 跳过含这些 slug 的整行 | 修 carve-out 链接断裂 bug（§1.4） |
| **M2** | `LAUNCHD_LABELS` 含 `auto-cc-space` | 拆分：`SUFFIX_RENAME_MAP` 映射 `auto-cc-space → auto-monster`，其他末段不变 | Q1 决策落点 |
| **M3** | phase_3 plist rename 用 `${var/find/replace}`（单次替换） | 改 `${var//find/replace}` 全量替换 + 套用 SUFFIX_RENAME_MAP | Q1 决策落点 |
| **M4** | phase_0 备份缺 ~/.claude.json / ~/.cc-connect/ / ~/.gk/ / ~/.claude/agents/gg.md / Library/Caches / ~/.claude/scheduled-tasks/auto_cc_space/ + 跨仓未基线 | 增加 phase 0 备份项 + 跨仓 git commit 基线（cc-copilot/Voca/kebao-cc/voca-mic）+ gg 自身 git commit 基线 | 单行回滚保底 |
| **M5** | 无 phase 2.5 / 6.5 | 新增 phase 2.5 bootout com.cc-connect / phase 6.5 bootstrap | cc-connect 链路 |
| **M6** | phase 7.5 只改 gg/CLAUDE.md | 改 phase 7.5 调用 sed 处理 gg 13 个活文件（清单硬编码），essence.md 在 sed_in_repo 排除字典里显式 NOT IN | gg 自身覆盖度 |
| **M7** | phase 7 缺 ~/.claude.json / ~/.cc-connect/config.toml / ~/.gk/repoMapping.json / ~/.claude/agents/gg.md / ~/.agents/skills 全量 / ~/.agents/skill-notes/done.md | 新增 phase 7.0a-7.0d 处理各项；7.2-7.4 改为对 ~/.agents/skills 全量 sed | E-J 漏点 |
| **M8** | 无 phase 7.8 | 新增 phase 7.8 mv ~/.claude/scheduled-tasks/auto_cc_space → auto_monster + 内部 sed | H 漏点 + Q1 |
| **M9** | phase 10 只盘 ~/.claude/projects/ 12 目录 | phase 10 同步处理 ~/Library/Caches/claude-cli-nodejs/ 8 目录（mv 前缀 + 不需要 jsonl 改写——cache 内容是 CC 自管） | K 漏点 |
| **M10** | phase 7.7 跨仓盲 sed 无 ack | 跨仓 sed 前打印命中清单 + ack 一次（防御未来类似 Voca Swift 源码场景） | B 风险防御 |
| **M11** | 无统一 dry-run 选项 | 增加 `bash monster-rename.sh dry-run`，跑完所有 phase 但不实际 mv/sed，输出预计改动清单 | 跑前看一眼 |
| **M12** | 无 cwd 安全检查回滚自封装 | 主入口的 cwd 检查保留；新增 `MONSTER_RENAME_DIR` 环境变量，rollback.sh 读取以定位备份 | rollback 自定位 |

---

## §4. 单行回滚机制

`rollback.sh` 可逆点：

| 类别 | 回滚动作 |
|---|---|
| **仓** | rm -rf ~/githubProject/monster && tar xzf ~/Downloads/cc-space-backup-20260520.tar.gz -C ~/githubProject/ |
| **CC projects (jsonl)** | rm -rf ~/.claude/projects/-Users-xuke-githubProject-monster* && tar xzf ~/Downloads/cc-projects-backup-20260520.tar.gz -C ~/.claude/projects/ |
| **CC CLI cache** | rm -rf ~/Library/Caches/claude-cli-nodejs/-Users-xuke-githubProject-monster* && tar xzf ~/Downloads/cc-cli-cache-backup-20260520.tar.gz -C ~/Library/Caches/claude-cli-nodejs/ |
| **scheduled-tasks** | rm -rf ~/.claude/scheduled-tasks/auto_monster && cp -r ~/.claude/scheduled-tasks-bak-20260520/auto_cc_space ~/.claude/scheduled-tasks/ |
| **launchd com.monster.*** | bootout 全部 com.monster.* → 反向 mv plist → bootstrap com.cc-space.* (13 个) + bootstrap com.cc-connect |
| **小项备份** | cp ~/.claude.json.bak-20260520 ~/.claude.json; cp ~/.cc-connect/config.toml.bak-20260520 ~/.cc-connect/config.toml; cp ~/.gk/repoMapping.json.bak-20260520 ~/.gk/repoMapping.json; cp ~/.claude/settings.json.bak-20260520 ~/.claude/settings.json; cp ~/.claude/agents/gg.md.bak-20260520 ~/.claude/agents/gg.md |
| **~/.agents** | rm -rf ~/.agents && cp -r ~/.agents-backup-20260520 ~/.agents |
| **gg 自身** | cd ~/githubProject/gg && git reset --hard HEAD@{rename-baseline}（baseline tag） |
| **跨仓 cc-copilot / Voca / kebao-cc / voca-mic** | cd $repo && git reset --hard HEAD@{rename-baseline}（每个仓打 baseline tag） |
| **GitHub repo name** | 若 phase 8 已跑：gh repo rename cc-space --repo keithMonster/monster（手工 ack） |

**rollback.sh 自身可幂等重跑**——任意 phase 中断后跑回滚都安全。

---

## §5. 验收（脚本跑完后追加）

- [ ] git log --oneline -5（基线 + rename commit + 不丢 commit）
- [ ] launchctl list | grep monster = 13 + cc-connect = 1（PID 非 0）
- [ ] CC statusline 正常
- [ ] threads_sync.py 派生 MEMORY.md 通
- [ ] notify.sh 推消息成功
- [ ] gg auto_gg 跑通（手工 kickstart 一次 com.monster.auto-monster）
- [ ] 飞书 bot ping（gg/cc/dd/kk 任一 + kebao-cc）
- [ ] 跨仓引用更新（cc-copilot / Voca / kebao-cc / voca-mic）
- [ ] CC --resume 老 sessionId 识别历史 transcript（D2 实测）
- [ ] 回滚演练（可选——cp 一份备份 + 手动测一次 rollback.sh 流程，确认能跑通）

---

## §6. 改动记录

- 2026-05-20 10:18 cp brief + script 到 gg/scratch/monster-rename/
- 2026-05-20 10:25 写本 audit.md
- 2026-05-20 后续：脚本改造 + rollback.sh 落地

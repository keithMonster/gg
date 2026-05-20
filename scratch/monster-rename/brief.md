---
slug: cc-space-to-monster-rename
title: cc-space → monster 仓库改名执行说明书（gg 会话版）
status: ready-to-execute
created: 2026-05-20
executor: gg-session
---

# cc-space → monster 仓库改名执行说明书

> **执行端**：从 `~/githubProject/gg/` 目录起的 fresh CC 会话。
> **本会话**：cc-space 内会话，只写文档，不执行。
> **理由**：cc-space 自己改自己时 cwd 失效 + jsonl 写入冲突，需中立 cwd。
>
> Keith 拍板「monster」于 2026-05-20——理由：cc-space (Claude Code Space) 命名当时太窄，现在它是「超级个体把『如何与不可靠 AI 协作』外化成的活文件系统」（见 `threads/cc-space-as-living-trunk.md`），跟 gg（大佬/军师）形成对子：gg 后方军师，monster 前线巨兽。

---

## §0. gg 会话开头必读

你（gg 会话的 CC）从 `~/githubProject/gg/` 起，fresh context，没有 cc-space 上下文。本文档自包含，按 §5 顺序执行即可。

**关键约束**：
- 你的 cwd **必须**在 `gg/` 或其他 cc-space 外目录，**绝不能 cd 到 cc-space**——否则 Phase 5 `mv` 时 cwd 失效，操作中断
- 改名期间 Keith 必须暂停其他活 CC 会话（kebao-cc / hermes / 其他 bg agent）——开干前他会确认
- Phase 8（`gh repo rename`）必须人工 ack 才执行——这是对外身份变更
- 所有破坏性操作前先备份，回滚链见 §6

**你拿到的资产**：
- 本文档（执行说明书）：`~/githubProject/cc-space/inbox/briefs/cc-space-to-monster-rename.md`
- 改名脚本：`~/githubProject/cc-space/scratch/monster-rename.sh`（self-contained，分 phase 独立可执行）
- worktree-cleanup skill：`~/githubProject/cc-space/.claude/skills/worktree-cleanup/`（已审计完，留档在 `scratch/worktree-cleanup-20260520-092235/`）

**总估算**：~75 分钟一次性收完。

---

## §1. 已锁决策（D1-D6 + 历史叙事 carve-out）

| # | 决策 | 锁定 |
|---|---|---|
| **D1** | threads/*.md cross-ref | **全量 sed 替换** `cc-space/threads/X.md` → `monster/threads/X.md` |
| **D2** | CC 旧 transcript 处理 | **全部迁移**（12 目录 + 1027 jsonl 全替换 cwd 字段 + 备份保底） |
| **D3** | 改名时机 | 等 Keith 叫，本说明书 ready 等触发 |
| **D4** | 4 worktree 处置 | **全删**（已审计 4/4 ✅ CAN_DELETE 噪音豁免，留档已 dump） |
| **D5** | scratch/ spike 改不改 | **改**（跟仓名一致） |
| **D6** | GitHub rename 时机 | 本地全改 + commit + 验证后再 `gh repo rename`（避免半状态） |

---

## §2. 历史叙事 carve-out（**保留 `cc-space` 字面**的清单）

按 Keith 拍："我们可以有历史叙事，就是知道我们改过名字。"

**绝对保留**（文件名 + 内容都不改 `cc-space` 字面）：

- `threads/cc-space-as-living-trunk.md`（"cc-space 这个概念的活载体本质"纪念碑）
- `threads/cc-space-memory-decommission.md`（cc-space 原生 memory 废弃事件记录）
- `threads/cc-space-design-system.md`（视觉契约整合事件记录）
- `threads/cc-space-memory-decommission.md` 关联快照 `auto-maintenance/memory-decommissioned-snapshot/`（如存在）
- 本 brief 本身：`inbox/briefs/cc-space-to-monster-rename.md`（改名事件本身的文档；改完后归档不删）
- `inbox/closed/*`（历史归档区，按 mtime 自然冻结）
- **git commit history**（commit message 不改写，按惯例）
- `chat/log.jsonl` / `chat/history/*`（历史会话日志，含 cc-space 是事实）

**改名脚本必须排除这些路径**（见 `scratch/monster-rename.sh` `EXCLUDE_HISTORICAL_PATHS` 段）。

---

## §3. 已验证基线事实

- **launchctl 活跃 label 13 个**：`usage-monitor` / `nw-weekly` / `cgboiler-sync` / `mirror-n` / `kebao-cc-sync` / `cgboiler-tick` / `chat-prep` / `mirror-h` / `mirror-o` / `cgboiler-inquiry-fetch` / `cgboiler-inquiry-extract` / `auto-cc-space` / `nw-daily`（前缀全 `com.cc-space.`）
- **git worktree 4 个**：全部 ✅ CAN_DELETE 噪音豁免（Phase 0 跑 audit.py --clean 删）
- **GitHub 仓**：`keithMonster/cc-space` PRIVATE，main 分支，无 Actions / Pages / webhook
- **本地 dirty 13 文件**：执行前先 commit 作基线（脚本 Phase 0 处理）
- **CC projects/ 目录数**：12 个 `-Users-xuke-githubProject-cc-space*`（主 + 11 个 worktree 子目录）
- **transcript jsonl 数**：主目录 1027 个，每个 jsonl 内部 `cwd` 字段含 cc-space 字面
- **gg 仓**：`~/githubProject/gg/CLAUDE.md` 关键 ~5 处引用需改（你跑改名同时顺手改自己仓）
- **跨仓**：`~/CGProject/cg-platform-template/AGENTS.md`(2) + `ENGINEERING-STANDARD.md`(4) + 其他 githubProject 仓零星
- **不影响项已验证**：
  - ✅ summon-deck Bundle ID = `com.keith.summondeck`（不含 cc-space，但 Models.swift 路径硬编码改）
  - ✅ cg-skills 仓无 cc-space 引用
  - ✅ FastGPT app prompt（跳过 V1，预期无引用，风险低）

---

## §4. 执行前置（gg 会话起手 5 分钟）

按这个顺序：

```bash
# 1. cwd 是 gg
pwd  # 应该是 /Users/xuke/githubProject/gg

# 2. Keith 确认无其他活 CC 会话
claude agents  # 让 Keith 看一眼，确认无其他活动 bg agent

# 3. 读说明书
cat ~/githubProject/cc-space/inbox/briefs/cc-space-to-monster-rename.md

# 4. 读改名脚本
cat ~/githubProject/cc-space/scratch/monster-rename.sh

# 5. 跑脚本（脚本 Phase 0 会自动备份所有项 + 逐 phase 显示进度 + Phase 8 暂停 ack）
#    备份产物：
#      - ~/Downloads/cc-space-backup-20260520.tar.gz （cc-space 仓含 .git，排 worktrees）
#      - ~/Downloads/cc-projects-backup-20260520.tar.gz （CC projects 内所有 cc-space 相关目录）
#      - ~/.claude/settings.json.bak-20260520
#      - ~/.agents-backup-20260520
bash ~/githubProject/cc-space/scratch/monster-rename.sh
```

---

## §5. Phase 执行清单（脚本会按这个跑）

> 完整脚本：`scratch/monster-rename.sh`（self-contained，分 phase 函数化）。
> 每 phase 跑完打印 [OK] / [FAIL]，失败立即停。

### Phase 0：前置清理（5 分钟）

- 0.1 **worktree 清理**：`cd ~/githubProject/cc-space && python3 .claude/skills/worktree-cleanup/scripts/audit.py --clean agent-a4b2f324907e57fc1 agent-a98a0a22ecafc84a3 done-noise-exemption-dogfood nw-clear-mechanical`
- 0.2 **commit dirty 13 文件作基线**：拆 3 个主题 commit（cc-assistant Step 1 收尾 / thread cc-space-as-living-trunk 落地 / 自动派生 jsonl 维护）
- 0.3 验证 `git worktree list` 仅剩主 worktree + `git status` 干净

### Phase 1：本机准备（5 分钟）

- 1.1 全仓 `grep -rln "cc-space"` 收集命中（排除 §2 历史叙事路径 + `__pycache__/` + `.git/` + 二进制）→ `/tmp/monster-targets.txt`
- 1.2 全仓 `grep -rln "/Users/xuke/githubProject/cc-space"` 路径命中 → `/tmp/monster-paths.txt`
- 1.3 打印两个清单总数，让 Keith 一眼看 sanity check

### Phase 2：launchd 安全卸载（5 分钟，**不可跳过**）

- 2.1 `launchctl bootout gui/$(id -u)/com.cc-space.<each>` × 13
- 2.2 验证 `launchctl list | grep cc-space` 空输出
- 2.3 留档当前 13 个 plist 文件路径到 `/tmp/monster-launchd-bak.txt`

### Phase 3：仓内 P0 必改（15 分钟）

- 3.1 Python 硬编码绝对路径（7 文件）批量 sed
- 3.2 launchd plist × 13：`<Label>` + `<WorkingDirectory>` + `<ProgramArguments>` + `StandardOut/ErrorPath`
- 3.3 prompt 文档绝对路径（chat/PREP_TICK.md / huasheng/TICK.md / plist 内嵌）
- 3.4 threads_sync.py / inbox 自动化派生工具自身
- 3.5 summon-deck Models.swift cc-space 路径硬编码

### Phase 4：仓内 P1 文档级（10 分钟）

- 4.1 主文档：CLAUDE.md / concepts.md / mirror/CLAUDE.md / chat/CLAUDE.md / profile.md / scheduled/README.md
- 4.2 **threads/*.md cross-ref 全量替换**（D1，排除 §2 历史叙事文件）
- 4.3 MEMORY.md 索引（threads_sync.py 派生不动）
- 4.4 shell / json 注释
- 4.5 scratch/ spike 脚本（D5，排除 __pycache__/）

### Phase 5：git mv 仓路径（1 分钟）

- 5.1 提交 Phase 3+4 改动作为「rename: cc-space → monster」commit
- 5.2 `cd ~/githubProject && mv cc-space monster`
- 5.3 `cd monster && git status` 干净

### Phase 6：launchd 重新装载（5 分钟）

- 6.1 `launchctl bootstrap gui/$(id -u) ~/githubProject/monster/scheduled/plists/com.monster.<each>.plist` × 13
- 6.2 验证 `launchctl list | grep monster` = 13
- 6.3 抽 `chat-prep` 跑一次 `launchctl kickstart` 验证

### Phase 7：本机仓外（10 分钟）

- 7.1 `~/.claude/settings.json:46` statusline hook 路径（**P0**）
- 7.2 `~/.agents/skills/done/SKILL.md`（6 处 `cc-space/threads/`）
- 7.3 `~/.agents/skills/notify/SKILL.md` 示例 task-id
- 7.4 `~/.agents/skills/text-to-podcast/SKILL.md`
- 7.5 `~/githubProject/gg/CLAUDE.md`（关键 ~5 处）—— **你顺手改自己仓**
- 7.6 `~/CGProject/cg-platform-template/AGENTS.md` + `ENGINEERING-STANDARD.md`
- 7.7 其他 githubProject 仓零星：`kebao-cc` / `cc-copilot` / `Voca` / `voca-mic` / `cookie-arcade`

### Phase 8：GitHub 远端改名（2 分钟，**🚨 暂停等 Keith ack**）

脚本会在这一步停下，打印：

```
[ACK] 准备执行 GitHub 远端改名：
  gh repo rename monster --repo keithMonster/cc-space
  git remote set-url origin git@github.com:keithMonster/monster.git
这是对外身份变更（GitHub 自动 301 但仓名公开变了）。Keith 输入 yes 继续：
```

Keith 输入 yes 后才执行 8.1-8.4。

- 8.1 `gh repo rename monster`（在 `~/githubProject/monster/` 内）
- 8.2 `git remote set-url origin git@github.com:keithMonster/monster.git`
- 8.3 `git remote -v` + `git fetch` 验证
- 8.4 `git push` 验证基线 commit + rename commit

### Phase 9：验证收尾（10 分钟）

- 9.1 CC statusline 正常显示（看终端 status bar）
- 9.2 `threads_sync.py` 派生 MEMORY.md 正常
- 9.3 抽 1-2 个核心 launchd 任务 `launchctl kickstart` 验证
- 9.4 `notify.sh` 推一条测试消息
- 9.5 done skill 触发一次会话复盘验证 Glob
- 9.6 `git status` 干净 + `git log --oneline -5`

### Phase 10：CC transcript 迁移（D2，独立 phase，10 分钟）

> 隔离 phase——Phase 0-9 完成后单独跑，万一 CC resume 不接受可 fallback 到原始备份。

- 10.1 mv 12 个目录前缀：`for d in ~/.claude/projects/-Users-xuke-githubProject-cc-space*; do mv "$d" "${d/cc-space/monster}"; done`
- 10.2 sed 替换所有 jsonl 内部 cwd 字段：`find ~/.claude/projects/-Users-xuke-githubProject-monster* -name "*.jsonl" -exec sed -i.bak 's|/Users/xuke/githubProject/cc-space|/Users/xuke/githubProject/monster|g' {} \;`
- 10.3 清理 .bak 文件：`find ~/.claude/projects/-Users-xuke-githubProject-monster* -name "*.jsonl.bak" -delete`
- 10.4 **实测**：`claude --resume <一个老 sessionId>`——看 CC 是否识别历史 transcript
- 10.5 如果实测失败：回滚 `mv` + 还原 backup，按原 D2(a) "不管"走

---

## §6. 风险 + 回滚预案

| 风险 | 概率 | 影响 | 回滚 |
|---|---|---|---|
| launchd bootstrap 失败 | 低 | cron 全断 | `/tmp/monster-launchd-bak.txt` 留档，反向 mv plist 名字 + 重 bootstrap 旧 label |
| Phase 5 `mv` 期间 cwd 失效 | **已消解** | — | gg 会话在 cc-space 外，不受影响 |
| GitHub rename 后 SSH 缓存滞后 | 低 | push 失败 | `git remote set-url` + `git fetch` 重试 |
| 跨仓引用有漏改 | 中 | 文档语义错位 | Phase 9 后 grep 一遍 `/Users/xuke/` 整树复查 |
| skill Glob 失败 | 中 | skill 行为异常 | Phase 9.4-9.5 触发测试，失败回查 sed |
| Phase 10 D2 CC resume 不认 | 中 | 历史 transcript 找不到 | 回滚 mv，按原 D2(a) "不管"走，历史孤悬不影响新工作 |
| `__pycache__/*.pyc` 被 sed 损坏 | 已防 | 编译产物损坏 | 脚本显式排除 `__pycache__` + 二进制 |
| 历史叙事文件被误改 | 已防 | 纪念碑被改 | §2 carve-out 清单 + 脚本 `EXCLUDE_HISTORICAL_PATHS` |

**总回滚链**（最坏情况）：
1. 仓本身：`tar xzf ~/Downloads/cc-space-backup-20260520.tar.gz -C ~/githubProject/`（含 .git）
2. CC projects：`tar xzf ~/Downloads/cc-projects-backup-20260520.tar.gz -C ~/.claude/projects/`
3. CC settings/agents：`~/.claude/settings.json.bak-20260520` / `~/.agents-backup-20260520`
4. launchd：`/tmp/monster-launchd-bak.txt` 留档清单反向 bootstrap

---

## §7. 验收清单（Phase 9 跑完报给 Keith）

- [ ] `git log --oneline -5` 显示基线 commit + rename commit + push 成功
- [ ] `launchctl list | grep monster` = 13 / `grep cc-space` = 0
- [ ] CC statusline 正常（hook 路径已改 settings.json）
- [ ] `threads_sync.py` 跑通，MEMORY.md 派生正常
- [ ] `notify.sh info monster-rename-test "改名验收测试"` 推送成功
- [ ] done skill 跑一次，Glob `monster/threads/*.md` 不报错
- [ ] gg/CLAUDE.md 已改，召唤 gg 时无 "cc-space" 字面出现（当下指向类）
- [ ] cg-platform-template AGENTS.md / ENGINEERING-STANDARD.md 引用更新
- [ ] Phase 10 D2 迁移实测：`claude --resume <老 sessionId>` 能识别历史（如果识别不了，记录降级 D2(a)）

---

## §8. 改完后归档

- 本 brief 文件名保留 `cc-space-to-monster-rename.md`（事件描述非仓状态，留作历史叙事）
- 内容保留 `cc-space` 字面（事件文档本身就是历史叙事）
- 关闭后移到 `inbox/closed/2026-05.md` 一行摘要："改名 cc-space → monster 实施完成 [→] briefs/cc-space-to-monster-rename.md"
- 改名脚本 `scratch/monster-rename.sh` 不删（spike 入库原则，决策可追溯锚点）

---

## 附：gg 会话起手 prompt 模板（Keith copy 用）

新会话从 `~/githubProject/gg/` 起，第一条消息发：

```
执行 monster 改名包。

执行说明书：~/githubProject/cc-space/inbox/briefs/cc-space-to-monster-rename.md
改名脚本：~/githubProject/cc-space/scratch/monster-rename.sh

按说明书 §4 执行前置（5 分钟）→ §5 Phase 0-10 顺序跑。

约束：
- cwd 必须在 gg/ 不能进 cc-space
- Phase 8 (gh rename) 暂停等我 ack
- Phase 10 (D2 迁移) 独立跑

我已暂停其他活 CC 会话，可以开干。
```

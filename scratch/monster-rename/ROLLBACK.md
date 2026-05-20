---
date: 2026-05-20
slug: monster-rename-rollback
type: rollback-runbook
companion_script: rollback.sh
companion_audit: audit.md
---

# monster-rename 单行回滚使用说明

> Keith 原话："留好退路就行，失败了我们能一行代码回滚回去就行。"
> 本文配 `rollback.sh` 使用。决策契约见 `audit.md §4`。

---

## 1. 快速使用

```bash
bash ~/githubProject/gg/scratch/monster-rename/rollback.sh
```

执行后系统状态等价于 `monster-rename.sh` 运行前的备份点（`20260520` 时间戳）。

**预期输出形态**：

```
================================================================================
  monster-rename 单行回滚脚本
  时间戳: 20260520
================================================================================

将依次回滚以下 11 项：
   1) 仓本身  ...
   2) CC projects jsonl ...
   ...
  11) GitHub rename     仅提示（不自动执行）

── 备份存在性检查 ──
  [PRESENT] ~/Downloads/cc-space-backup-20260520.tar.gz
  [PRESENT] ~/Downloads/cc-projects-backup-20260520.tar.gz
  [PRESENT] ~/Downloads/cc-cli-cache-backup-20260520.tar.gz
  [PRESENT] ~/.claude/scheduled-tasks-bak-20260520
  [PRESENT] ~/.agents-backup-20260520

确认开始回滚？(输入 yes 继续): yes

开始回滚……

── 步骤 1 / 11 — 仓本身 ──
  [OK]   rm -rf ~/githubProject/monster
  [OK]   tar xzf cc-space-backup → ~/githubProject/

── 步骤 2 / 11 — CC projects jsonl 目录 ──
  [OK]   rm -rf ~/.claude/projects/-Users-xuke-githubProject-monster*
  [OK]   tar xzf cc-projects-backup → ~/.claude/projects/

...

================================================================================
  回滚报告
================================================================================
  OK   : 35
  SKIP : 2
  WARN : 0

  退出码: 0（完全 OK）
```

**退出码语义**：

| 码 | 含义 |
|---|---|
| 0 | 完全 OK（所有步骤 OK 或幂等 SKIP） |
| 1 | 部分失败（至少一项 [WARN]——见明细 + 本文 §5 失败兜底） |
| 2 | 关键备份缺失（核心 tarball / agents / scheduled 备份目录缺一即拒绝执行） |

---

## 2. 回滚 11 项一览

| # | 维度 | 回滚动作 | 备份源 |
|---|---|---|---|
| 1 | 仓本身 | `rm -rf ~/githubProject/monster && tar xzf cc-space-backup-20260520.tar.gz -C ~/githubProject/` | `~/Downloads/cc-space-backup-20260520.tar.gz` |
| 2 | CC projects jsonl | `rm -rf ~/.claude/projects/-Users-xuke-githubProject-monster* && tar xzf cc-projects-backup-20260520.tar.gz -C ~/.claude/projects/` | `~/Downloads/cc-projects-backup-20260520.tar.gz` |
| 3 | CC CLI cache | `rm -rf ~/Library/Caches/claude-cli-nodejs/-Users-xuke-githubProject-monster* && tar xzf cc-cli-cache-backup-20260520.tar.gz -C ~/Library/Caches/claude-cli-nodejs/` | `~/Downloads/cc-cli-cache-backup-20260520.tar.gz` |
| 4 | scheduled-tasks | `rm -rf ~/.claude/scheduled-tasks && cp -r ~/.claude/scheduled-tasks-bak-20260520 ~/.claude/scheduled-tasks` | `~/.claude/scheduled-tasks-bak-20260520/` |
| 5 | launchd monster 系列 | `bootout` 全部 `com.monster.*` → `bootstrap` 全部 `com.cc-space.*`（13 个） | `/tmp/monster-launchd-bak.txt` 留档清单 |
| 6 | cc-connect launchd | `bootout com.cc-connect` → 还原 `config.toml`（步骤 7）→ `bootstrap com.cc-connect` | `~/Library/LaunchAgents/com.cc-connect.plist`（plist 本身不变） |
| 7 | 小项 .bak 还原 | `cp` 5 个 `.bak-20260520` 文件回原位 | 各文件同目录下的 `.bak-20260520` |
| 8 | `~/.agents` | `rm -rf ~/.agents && cp -r ~/.agents-backup-20260520 ~/.agents` | `~/.agents-backup-20260520/` |
| 9 | gg 自身 | `cd ~/githubProject/gg && git reset --hard rename-baseline-20260520` | git tag `rename-baseline-20260520` |
| 10 | 跨仓（5 个） | 各 `git reset --hard rename-baseline-20260520`：`cc-copilot / Voca / kebao-cc / voca-mic / cookie-arcade` | 各仓 git tag |
| 11 | GitHub rename | **仅提示，不自动执行**（gh repo rename 是 GitHub 端不可逆动作） | — |

**小项 .bak 清单（步骤 7）**：

- `~/.claude.json.bak-20260520`
- `~/.cc-connect/config.toml.bak-20260520`
- `~/.gk/repoMapping.json.bak-20260520`
- `~/.claude/settings.json.bak-20260520`
- `~/.claude/agents/gg.md.bak-20260520`

---

## 3. 设计要点（为什么要这样写）

| 设计 | 理由 |
|---|---|
| **`set -uo pipefail`，不用 `set -e`** | 回滚要尽量跑完所有可逆步骤，单步失败不该 abort 后续 |
| **每步独立 try-catch** | 任一步失败 → 打印 `[WARN]` → 继续下一步 |
| **幂等性** | 第二次跑基本 no-op：已删则 SKIP、已 load 的 launchd 跳过、cc-space 仓存在则不覆盖（防吃掉新提交） |
| **单次 ack** | 启动一次 `yes` 确认，中途不打断 |
| **关键安全闸** | 三个 tarball + 两个备份目录任一缺失就 `exit 2`，禁止"半还原"；脚本内**禁止任何 `sed`/`find` 全文跑** |
| **essence.md 不动** | 改名脚本就没动它。rollback 也不修，只检测：若 `essence.md` 含 `monster` 字面 → 提示 Keith（这是改名脚本 bug） |
| **GitHub rename 不自动** | `gh repo rename` 是 GitHub 端显式不可逆动作，必须人工触发 |

---

## 4. 场景化 SOP

### 场景 A：改名脚本跑到 phase 5 失败（仓已 mv 但还没改 cc-connect）

**症状**：`~/githubProject/monster` 已存在，但 cc-connect 飞书 bot 死循环、CC statusline 不正常。

**动作**：

```bash
bash ~/githubProject/gg/scratch/monster-rename/rollback.sh
```

输入 `yes`。rollback.sh 会：

- 删 `~/githubProject/monster` → 还原 `cc-space`
- 还原 CC projects + CLI cache + scheduled-tasks
- bootout monster launchd → bootstrap cc-space launchd
- 还原 `cc-connect/config.toml` + bootstrap `com.cc-connect`
- gg + 跨仓 git reset 到 baseline tag

**验收**：

```bash
launchctl list | grep cc-space | wc -l      # 应 = 13
launchctl list | grep cc-connect             # 应有 1 条且 PID 非 0
ls ~/githubProject/cc-space                  # 应存在
ls ~/githubProject/monster                   # 应不存在
```

---

### 场景 B：phase 8 GitHub rename 已跑后回滚

**症状**：本地已全改 + push + `gh repo rename monster` 已跑，GitHub 端仓名是 `keithMonster/monster`。

**动作**：

```bash
# 1. 本地回滚
bash ~/githubProject/gg/scratch/monster-rename/rollback.sh

# 2. 手工还原 GitHub 端（rollback.sh 步骤 11 会打印提示）
gh repo rename cc-space --repo keithMonster/monster
cd ~/githubProject/cc-space
git remote set-url origin git@github.com:keithMonster/cc-space.git
git fetch && git remote -v   # 验证
```

**验收**：

```bash
gh repo view keithMonster/cc-space --json name,url    # name = cc-space
git -C ~/githubProject/cc-space remote -v             # origin = ...cc-space.git
```

---

### 场景 C：完整跑完才发现问题（一周后回滚）

**症状**：改名一切正常，但一周后 Keith 反悔——这期间 monster 仓有新 commit、CC 有新 session、scheduled-tasks 有新产物。

**风险**：`git reset --hard rename-baseline-20260520` 会**丢掉**这一周的新 commit；rollback.sh 会**吃掉** monster 期间产生的新 jsonl/cache。

**动作**（必须先保护新工作）：

```bash
# 1. 保护新 commit（gg + 跨仓 + monster 本身）
for repo in ~/githubProject/gg ~/githubProject/monster ~/githubProject/cc-copilot \
            ~/githubProject/Voca ~/githubProject/kebao-cc ~/githubProject/voca-mic \
            ~/githubProject/cookie-arcade; do
  [[ -d "${repo}/.git" ]] && git -C "${repo}" branch backup-pre-rollback-$(date +%Y%m%d) HEAD
done

# 2. 备份这一周新增的 CC transcript（避免被吃掉）
tar czf ~/Downloads/monster-week-transcripts.tar.gz \
  ~/.claude/projects/-Users-xuke-githubProject-monster* 2>/dev/null

# 3. 跑回滚
bash ~/githubProject/gg/scratch/monster-rename/rollback.sh

# 4. （可选）把 monster 期间的 commit cherry-pick 到 cc-space
cd ~/githubProject/cc-space
git log backup-pre-rollback-<date> --oneline   # 看一周内新 commit
# 按需 git cherry-pick <sha>
```

**判断要点**：场景 C 的核心是"baseline 之后有产出值得保留"——如果都是噪音，直接跑 rollback 即可；如果有真东西，先建 backup-branch + 备份 transcript 再回滚。

---

## 5. 失败兜底 — rollback.sh 自己失败时的手工 SOP

如果 `rollback.sh` 退出码 = 2（关键备份缺失）或 = 1（多项 WARN），按下表手工恢复：

### 5.1 关键备份位置清单

| 备份 | 位置 | 关键性 |
|---|---|---|
| 仓 tarball | `~/Downloads/cc-space-backup-20260520.tar.gz` | **致命**（缺则无法还原仓） |
| CC projects tarball | `~/Downloads/cc-projects-backup-20260520.tar.gz` | **致命**（缺则 CC session 历史全丢） |
| CC CLI cache tarball | `~/Downloads/cc-cli-cache-backup-20260520.tar.gz` | 高（缺则 resume 行为异常） |
| scheduled-tasks 备份 | `~/.claude/scheduled-tasks-bak-20260520/` | 高 |
| ~/.agents 备份 | `~/.agents-backup-20260520/` | 高 |
| launchd 留档清单 | `/tmp/monster-launchd-bak.txt` | 中（缺则需手工 bootstrap） |
| 小项 .bak | 见 §2 步骤 7 | 中（每项独立，缺一损一） |
| git tag | 各仓 `rename-baseline-20260520` | **致命**（缺则跨仓改动无法精确还原） |

### 5.2 手工恢复命令（按步骤）

```bash
# 步骤 1：仓本身
rm -rf ~/githubProject/monster
tar xzf ~/Downloads/cc-space-backup-20260520.tar.gz -C ~/githubProject/

# 步骤 2：CC projects
rm -rf ~/.claude/projects/-Users-xuke-githubProject-monster*
tar xzf ~/Downloads/cc-projects-backup-20260520.tar.gz -C ~/.claude/projects/

# 步骤 3：CC CLI cache
rm -rf ~/Library/Caches/claude-cli-nodejs/-Users-xuke-githubProject-monster*
tar xzf ~/Downloads/cc-cli-cache-backup-20260520.tar.gz -C ~/Library/Caches/claude-cli-nodejs/

# 步骤 4：scheduled-tasks
rm -rf ~/.claude/scheduled-tasks
cp -r ~/.claude/scheduled-tasks-bak-20260520 ~/.claude/scheduled-tasks

# 步骤 5：launchd monster → cc-space
# 5a. bootout monster
launchctl list | awk '$3 ~ /^com\.monster\./ {print $3}' | while read l; do
  launchctl bootout gui/$(id -u)/$l
done
# 5b. bootstrap cc-space（从留档清单读 plist 路径）
while read plist; do
  [[ "$plist" =~ cc-connect ]] && continue
  launchctl bootstrap gui/$(id -u) "$plist"
done < /tmp/monster-launchd-bak.txt

# 步骤 7：小项备份还原
cp ~/.claude.json.bak-20260520 ~/.claude.json
cp ~/.cc-connect/config.toml.bak-20260520 ~/.cc-connect/config.toml
cp ~/.gk/repoMapping.json.bak-20260520 ~/.gk/repoMapping.json
cp ~/.claude/settings.json.bak-20260520 ~/.claude/settings.json
cp ~/.claude/agents/gg.md.bak-20260520 ~/.claude/agents/gg.md

# 步骤 6：cc-connect bootstrap（步骤 7 之后做）
launchctl bootout gui/$(id -u)/com.cc-connect 2>/dev/null
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cc-connect.plist

# 步骤 8：~/.agents
rm -rf ~/.agents
cp -r ~/.agents-backup-20260520 ~/.agents

# 步骤 9：gg 自身
cd ~/githubProject/gg && git reset --hard rename-baseline-20260520

# 步骤 10：跨仓
for repo in cc-copilot Voca kebao-cc voca-mic cookie-arcade; do
  cd ~/githubProject/$repo && git reset --hard rename-baseline-20260520
done

# 步骤 11：GitHub rename（仅当 phase 8 已跑过）
gh repo rename cc-space --repo keithMonster/monster
cd ~/githubProject/cc-space
git remote set-url origin git@github.com:keithMonster/cc-space.git
```

### 5.3 备份缺失时的降级

| 缺失项 | 降级方案 |
|---|---|
| **仓 tarball 缺** | 无路可走——尝试从 `~/githubProject/monster/.git` 用 `git log` 查找 baseline commit 并 `git checkout` |
| **CC projects tarball 缺** | 牺牲历史 transcript，按原 brief D2(a)"不管"走；新 session 不受影响 |
| **CC CLI cache 缺** | 无关键影响——CC 会重建 cache |
| **scheduled-tasks 备份缺** | 从 `~/githubProject/cc-space/scheduled/plists/`（还原后的仓内）反推重建任务 |
| **~/.agents 备份缺** | 从 git 仓库（如有）或 skill-creator 重建关键 skill |
| **launchd 留档清单缺** | 手工列：从 `~/githubProject/cc-space/scheduled/plists/*.plist` 逐个 `launchctl bootstrap` |
| **小项 .bak 单项缺** | 该项保持 monster 状态——影响有限可后续手工修正 |
| **git tag 缺** | `git reflog` 查找 baseline 时间点的 HEAD，手工 `git reset --hard <sha>` |

---

## 6. 不可逆点说明

### GitHub repo rename

`gh repo rename` 修改的是 GitHub 端仓库实体名称——这是 GitHub 服务器侧的状态变更，**rollback.sh 无法物理回滚**。

**rollback.sh 的处理**：

- 不自动执行 `gh repo rename`
- 步骤 11 检测当前 `git remote get-url origin`，若指向 `keithMonster/monster` → 打印 `[MANUAL]` 提示
- 把这一项计入 `WARN` 总数，让最终退出码反映"有手工动作待办"

**为什么不自动**：

- `gh repo rename` 影响所有协作者 / CI / webhook（虽然 GitHub 自动 301 redirect 一段时间，但仍是对外身份变更）
- 用户决策权——不该被脚本悄悄改回
- 自动跑可能在凭据 / 权限 / 二次确认上失败，反而留下半状态

**手工执行**：见场景 B + §5.2 步骤 11。

---

## 7. 自检快速命令

跑完 rollback 后用以下命令快速验收：

```bash
# 仓
ls ~/githubProject/cc-space >/dev/null && echo "[OK] cc-space 仓还原"
ls ~/githubProject/monster 2>/dev/null && echo "[WARN] monster 仓还在"

# launchd
echo "cc-space labels: $(launchctl list | grep com.cc-space | wc -l)（应 = 13）"
echo "monster labels:  $(launchctl list | grep com.monster | wc -l)（应 = 0）"
echo "cc-connect:      $(launchctl list | grep com.cc-connect | wc -l)（应 = 1）"

# CC projects
ls ~/.claude/projects/-Users-xuke-githubProject-cc-space* >/dev/null 2>&1 && echo "[OK] CC projects 还原"

# 小项
for f in ~/.claude.json ~/.cc-connect/config.toml ~/.gk/repoMapping.json \
         ~/.claude/settings.json ~/.claude/agents/gg.md; do
  [[ -f "$f" ]] && grep -q cc-space "$f" 2>/dev/null && echo "[OK] $f 含 cc-space 字面"
done

# gg
git -C ~/githubProject/gg log --oneline -1
```

---

## 附：rollback.sh 设计契约速查

- **入口**：`bash ~/githubProject/gg/scratch/monster-rename/rollback.sh`
- **前置闸**：5 项关键备份存在性检查 → 任一缺失 `exit 2`
- **确认**：单次 `yes` 输入 → 进入执行
- **执行**：11 步顺序，每步独立兜底（`||` + log_warn）
- **后置自检**：`essence.md` 含 `monster` 字面检测（情况性 WARN）
- **总报告**：聚合 OK / SKIP / WARN 数 + 逐步明细 + 退出码
- **配套**：`audit.md §4`（决策契约 SSOT）


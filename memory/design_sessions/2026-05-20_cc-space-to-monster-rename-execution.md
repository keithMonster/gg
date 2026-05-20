---
date: 2026-05-20
slug: cc-space-to-monster-rename-execution
type: design-session
summoner: Keith 直接对话（执行端）
started_at: 10:15
ended_at: 11:00
---

# 设计会话反思：cc-space → monster 改名执行端

## 议题列表

1. Keith brief：cc-space → monster 改名包从 cc-space 内会话写好交执行（gg 这边）
2. 文档+脚本审计：发现 4 类问题（链接断裂、跨仓盲 sed、gg 覆盖度缺口、phase 10 路径失效）
3. Keith 主动指出 cc-connect 漏盘（gg 漏盘的）→ 二次扫确证 com.cc-connect 是第 14 个独立 label + ~/.cc-connect/config.toml 4 处 work_dir + .claude.json + .gk + 多个 skill
4. 单行回滚保底设计 → audit.md §4 + rollback.sh + ROLLBACK.md
5. 派 2 个 subagent 分头改造 monster-rename.sh v2 + 写 rollback.sh + ROLLBACK.md
6. Dry-run 实测抓出 4 个 subagent 漏的（notify/sent + done/logs 历史档 / Voca .build 二进制 / gg HISTORICAL_TOKENS 扩展）→ 派第三个 subagent 修补
7. Keith 全权接管授权 → 真跑 phase 0-10
8. 跑时再抓 3 个 bug：BSD ls `-` 开头当 option（0.0b 失败）/ BSD tar 同病（0.0b 再失败）/ launchctl bootout 异步导致 phase 2.5 false fail
9. Phase 7.5 后发现链接保护残留漏洞——HISTORICAL_TOKENS 用文件名形式（`2026-05-08_cc-space-design-asset-integration`），但活文件叙事用空格分隔（`2026-05-08 cc-space-design-asset-integration`），token 不命中→ keith.md / architecture.md 里 3 处 reflection slug 被误改成 `monster-X` → 手工修复

## 共识 / 变更清单

物理改名全部完成：

- `~/githubProject/cc-space` → `~/githubProject/monster`
- GitHub `keithMonster/cc-space` → `keithMonster/monster`（301 重定向 + push）
- 14 个 launchd label：13 个 `com.cc-space.*` → `com.monster.*`（含 `auto-cc-space` → `auto-monster`）+ `com.cc-connect` 重启 PID 26279
- `~/.claude/projects/-Users-xuke-githubProject-monster*` × 12 + `~/Library/Caches/.../monster*` × 8
- `~/.cc-connect/config.toml` 4 处 work_dir 切到 monster
- `~/.claude.json` 5 处绝对路径切到 monster
- `~/.gk/repoMapping.json` 含 path + GitHub identifier
- `~/.claude/agents/gg.md` + `~/.claude/scheduled-tasks/auto_monster/`
- gg 自身 13 个活文件 + 3 处误改回滚（`monster-<slug>` → `cc-space-<slug>` 恢复历史 reflection 引用真名）
- 跨仓 sed：kebao-cc / cc-copilot / Voca / voca-mic / cookie-arcade

历史档保护（铁律级）100% 守住：
- `essence.md` monster 字面 = 0（KERNEL §2 append-only 铁律）
- 4 个 carve-out 文件（`cc-space-as-living-trunk` / `cc-space-memory-decommission` / `cc-space-design-system` / `cc-space-to-monster-rename`）原名保留
- gg 历史档（reflections 74 / design_sessions 16）保留 cc-space 字面
- `~/.agents/skills/notify/sent` 45 个 trace + `done/logs` 231 个复盘历史档未被改

回滚保底就位：3 个 tarball (550M) + 5 个 .bak-20260520 + 2 个备份目录 + 6 个 git baseline tag。

## 我这次哪里做得好 / 哪里差

### 做得好

- **二次扫漏点**：Keith 给 brief 后我没直接跑——做了 gg 侧二次 grep 扫，抓出 cc-connect / .claude.json / .gk / scheduled-tasks/auto_cc_space / Library/Caches 等 brief 完全没盘的辐射面。Keith 一句"cc-connect 想过吗"是关键提示，没我也会自查到（已经在盘）
- **铁律级保护**：essence.md 显式 NOT IN + 跑完验证 monster 字面 = 0 + carve-out 行级保护——这层从 audit.md 设计到 dry-run 验证到真跑后核对，三道闸全部生效
- **回滚先于执行**：rollback.sh 跟 monster-rename.sh 同时落地。Keith 一句"留好退路就行"被翻译成 11 项可逆维度 + 单行入口
- **subagent 复用**：4 个 subagent（脚本改造 v1 / rollback / 4 处修补 / 验收清单），自己做的是 review + 决策。这是 Keith 中途明示要的形态

### 做得差（每条 Keith 没直接打断，是 dry-run 或真跑暴露的）

- **dry-run 没覆盖真跑特有的两类问题**：(1) BSD `ls -d *X*` 在以 `-` 开头的文件名展开时被当 option 解析（dry-run 时跳过整段 `ls + tar` 没触发）；(2) `launchctl bootout` 异步导致立即 `launchctl list` 还看到——dry-run 也跳过了。**教训**：dry-run 是必要不充分的——它验证逻辑路径，但 OS 异步动作 + glob 解析 corner case 必须真跑才暴露
- **HISTORICAL_TOKENS 字面形式跟自然语言变体的失配**：keith.md 里写"2026-05-08 cc-space-design-asset-integration"（空格分隔），但 HISTORICAL_TOKENS 数组定义 `2026-05-08_cc-space-design-asset-integration`（下划线分隔，文件名形式）。**字符级 token 保护对自然语言中的 slug 引用变体盲**——指向 historical 文件的方式不止文件路径，还有"散文叙事中的 slug 引用"。这层在 audit.md 漏盘了。所幸只 3 处误改，跑完后扫出来手工修。但思路上是个新的失败模式
- **跨仓 git commit 副作用**：phase 0.0f 跨仓打 baseline tag 时顺手 `git add -A + commit`，把 Voca 仓的 30 个 dirty 文件（之前累积的 unrelated 工作）一并 commit 了。这不是预期——baseline 应该是"这一刻的快照"，但 Voca 实际有未完成工作被强制收尾。**教训**：跨仓 baseline 应该用 `git stash` 而非 `git commit` —— stash 是可还原的暂存，commit 是改 git 历史

## 元洞察（gg 演化本身的 learning）

### 字面 vs 引用形态的不对称（候选 essence）

**链接保护机制按"字面 token"判别一行是否含 historical 引用，但活文件里同一个 historical entity 可以以多种字符串形态出现**：

- 文件名形式：`2026-05-08_cc-space-design-asset-integration.md`（带下划线 + .md）
- 路径形式：`memory/reflections/2026-05-08_cc-space-design-asset-integration.md`
- 自然语言引用：`从 2026-05-08 cc-space-design-asset-integration reflection 获得`（空格 + 无 .md）
- 缩写：`design-asset-integration reflection`

字面 token 数组覆盖一种形态，但 sed 影响的是所有形态。第二种保护是不对等的——保护机制只盯**注册过的形态**，但被保护对象在自然语言中**变体涌现**。

跟 essence `bug-shape-survives-fix` 同根反向：那条说"修了一处，自己以同形态做下一个动作"——本条说"保护了一种字面形态，被保护对象以另一种形态溜走"。是"保护机制的 dimension blindness"。

待沉淀（见下"沉淀"节）。

### dry-run 的边界

Dry-run 验证的是**纸面逻辑**——脚本 control flow + 命中清单。**OS 异步动作（launchctl bootout）+ glob 解析 corner case（BSD ls/tar `-` 开头）+ 文件系统真实状态**这三类必须真跑才暴露。

跟 essence `theory-gap-without-data` 同维：理论分析（dry-run）找不到的问题，只有数据（真跑）才能证伪。

不算新 essence——是已有 essence 在"dry-run vs 真跑"边界的具体落点。

### 跨仓 baseline = stash 而非 commit

为另一个项目的改名"顺手"在其他仓 commit dirty 是越界。baseline 的语义是"可回到的快照"，stash 满足；commit 改了项目历史。如果 Voca 这些 dirty 是用户 in-progress 的工作，commit 会破坏他自己的回滚意图。

不算 essence——是 cross-project ops 的工程约定。

## 下次继续

1. **rollback.sh fall-back 路径补**：subagent 写的 rollback 期望 `~/.claude/projects-backup-*` + `claude-cli-nodejs-backup-*` 目录，但实际备份在 ~/Downloads/*.tar.gz。需要加"目录缺失则解压 tarball 到目标路径"的 fall back（验收 §E 的 🟡 项）
2. **HISTORICAL_TOKENS 的"形态展开"机制**：未来类似改名/迁移任务，token 数组要自动展开多种形态（下划线/空格/路径前缀/带后缀），不是逐 token 字面匹配
3. **跨仓 baseline 改用 stash**：脚本里 phase 0.0f 现在用 `git commit + tag`，下次同类工具应改用 `git stash save baseline-<stamp>` + `git stash` 索引追踪
4. **Voca 仓本次"被动 commit"的 30 个文件**：Keith 可能想看下是不是他想要的状态，或者 reset 回去重新整理（baseline tag 是 reset 锚点）
5. **跨仓 sed 完成度复核**：voca-mic 非 git 仓，本次 sed 跑了但无法用 git diff 验证。需要 Keith 手工 diff 或我后续派 subagent 对照基线 .bak 验证

## 代码质量

本轮主要代码产出：
- `monster-rename.sh` 1057 行 → 1080 行（4 处真跑 fix）
- `rollback.sh` 502 行
- `ROLLBACK.md` 14K
- `audit.md` 9K

技术债：
- monster-rename.sh 里 `sed_file_line_safe` 的 HISTORICAL_TOKENS 是字面 token 数组——未来类似工具应抽象成"token + 形态展开器"
- rollback.sh 的备份目录 fall-back 缺失（subagent 写时按 audit.md §4 直接 cp 目录，但实际备份是 tarball）

死代码 / 遗留 TODO：无

## 能力缺口

本轮没明显缺口。subagent 协作 + dry-run + 真跑反馈循环的组合工作得不错。**唯一暴露的能力维度**：跨抽象层的"字面保护机制 vs 自然语言变体引用"的不对称——这是认知层的，不是工具层。

## essence 对齐自检

- 本次会话的判断/改动跟以下 essence 对位：
  - `physical-anchor`（2026-04-16）— dry-run 验证后还是必须真跑，物理工具返回才是锚点。落点：跑时再抓 3 个 dry-run 没暴露的 bug
  - `bug-shape-survives-fix`（2026-04-27）— 修了 carve-out 文件自身，没意识到活文件里的"形态变体"引用仍以同结构被改。落点：HISTORICAL_TOKENS 失配漏洞
  - `reverse-anchor-by-reflection`（2026-04-27）— 本次反思暴露的"字面 vs 引用形态不对称"就是它的活体
  - `theory-gap-without-data`（2026-05-06）— dry-run 是理论分析，OS 异步 + glob 解析必须数据（真跑）证伪
  - `fast-slow-divide`（2026-04-16）— 历史档（notify/sent / done/logs / gg reflections）的保护是"历史是只写的"在 cross-project sed 场景的落点
  - `criteria-authorization-over-menu`（2026-05-15）— Keith 多次给"按推荐来 / 全权接管"的判据级授权，gg 不回 menu，按判据自决落点
- 本次没有反着走任何条 essence
- cross-check 关键词：HISTORICAL_TOKENS / carve-out / dry-run / baseline / rollback

## 沉淀（写入 essence.md）

候选 essence — **`literal-token-blind-to-variant-form`**（字面 token 对引用变体盲）：

> 按字面 token 做的保护机制，对被保护对象在自然语言中以变体形态出现的引用全盲。
> 文件名 token 数组只能保护"这一种字面"，但同一对象在散文叙事里有空格分隔/缩写/路径前缀等变体——保护机制盯注册形态，被保护对象在变体中溜走。
> `bug-shape-survives-fix` 在"保护机制 vs 被保护引用"维度的镜像反转：前者保护者（人）以同形态复犯，本条被保护者（引用）以异形态被改。

写入 essence.md（append）。

## KERNEL 改动清单

无（本轮未触 KERNEL.md）。

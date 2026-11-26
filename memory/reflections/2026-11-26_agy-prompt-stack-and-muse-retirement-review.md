---
date: 2026-11-26
slug: agy-prompt-stack-and-muse-retirement-review
summoner: monster（agy 无头 `agy -p` claude-opus-5-5-high，父进程 82545；提示词体系联合审查 + Muse Code 退役边界）
northstar_reach: "#1 二阶效应 / #3 决策超越直觉"
status: substantive-decision
---

# Reflection: agy/monster 提示词加载体系联合审查与 Muse Code 退役清理

## 给父会话的最终输出（必填）

**本次没想到的一点**：简报基线说"子代理与无头会话只收 Gemini 校准卡"，这一条被本次召唤本身证伪。我就是无头 `agy -p`（`ps` 85827，etime 与本会话吻合），`conversation_summaries` 里本会话 parent=''、depth=0，但上下文里收到了 `<runtime-md-preload>` 和 `<monster-memory-preload>`，共 37 KB。原因在 `is_personal_main_session_agy`：它没有 `is_closeout_eligible_agy` 里的 `_parent_agy_is_headless()` 判断。所以在 monster cwd 下跑的 Carbon、gg、neon-high 无头审查，每次都要多付 37 KB。Q2 的分层权衡也不能再以"无头不收预注"为前提。

**P0 必须改**
1. 预注判定补上无头排除：`is_personal_main_session_agy` 增加 `_parent_agy_is_headless()`，但 `CC_SESSION_KEY` 已实核的个人 bot 通道要豁免（先核飞书 `cc_agy_wrapper` 是否走 `-p`，`cc_agy_wrapper.py` 里没 grep 到 `-p`，未证）。补一个反向用例：无头 + 无 CC_SESSION_KEY → False。
2. cmd/commander 下发口径漂移，共 4 处（简报漏了第 4 处 `cmd/SKILL.md:78`，它仍写"首选 rn-agy-worker"）。修法：副本里**删掉排序**，只留不变式"严禁外部 Ghostty Tab，口径见 runtime/agy.md §cmd"。涉及 `monster-on-antigravity.md:11`、`runtime.md:23`、`cmd/SKILL.md:78`。理由：seam #16/#17 只核锚词在不在，排序变化查不出来，副本保留排序就会继续漂。
3. `/compact` 回水增加 MEMORY 失效声明，约 150 B：`<monster-memory-preload> 已随压缩失效，查主体前重读 MEMORY.md 或按冷启动 rg`。原因：预注文案里"无需重复 read_file"这句豁免会被压缩摘要保留，正文却没了，等于教模型漏查（与 11-20 H1 同形）。不回水全文 27 KB，因为强制触发①（先查再答）本来就存在，只需撤掉"已加载"这个错误信念。
4. `monster/AGENTS.md:18` 改成与 harness 无关的写法：`（未见 <monster-memory-preload> 时须工具读取）`，替换"Codex/agy 须工具读取"，消掉与 `monster-on-antigravity.md:10` 的字面矛盾。
5. Muse 活入口清理，**立刻做**：
   - `runtime.md:9` 删"/ Muse"，`:10` 整行删；`reason-network.md:3/12/21/22` 删 Muse 字样，Codex 保留。
   - `muse-guard-review`、`muse-sensitive-data` 移到 `~/.agents/skills/_archive/<name>-20261126/`，同时删掉 `~/.claude/skills/muse-guard-review` 软链。这样做不止为省字节：`muse-sensitive-data` 的触发描述"任务需要读原文、凭据、个人标识或公司内容时使用"覆盖面很宽，在 agy 和 CC 每个会话都可能误触发，把任务引到一个已死的 Muse 流程。
   - `he-AGENTS.md:128` 删掉；`harness-map.md:61` 的 Muse 项改成一行墓碑"已停用 2026-11-26"；`toolbox.md:53` 标停用或迁到 toolbox-history；`calibration/README.md:22` 删 Muse 行；`monster-on-muse.md` 顶部加停用头。
   - `threads/muse-code.md`：status 改为非 active，"关键历史"记"2026-11-26 Keith：Muse code 不会使用了"。MEMORY 自动派生。
   - **不动**：`muse_*.py` 及测试、`shared/data/muse-guard/`、`transcript_indexer` 的 muse 来源（历史检索还要用）、fleet/model_eval/agent_thread/cc_binary_grep 的 muse 参数支持、`aliases.toml`/`calibrationctl.py` 注释、`~/.config/muse`、`~/.local/bin/muse`（卸载由 Keith 决定）、个人代理路由。改完跑一遍断链/skill 组合类传感器，确认软链删除后没有误报。

**P1 建议改**
6. `runtime.md` 删掉 agy 专属括注：第 8 行双号长括注收成"→ runtime/agy.md（含 agy2 双号联动）"；第 17 行删"agy 禁 /browser…"括注。runtime.md 也给 CC/Codex 读，这两条已由 `monster-on-antigravity` 送到所有 agy 会话（含子代理），这是唯一能到达子代理的载体。
7. `monster-on-antigravity.md:16`：删 10 项路径枚举，保留语义类"受 Write/Edit 守卫、写后契约或 closeout 写计数覆盖的路径不借脚本/batch_exec 绕过"，加指针"清单以 batch_exec 工具说明为准"。batch_exec 自身会物理拒收，失败是显式的；规则里真正有承重的是"也不借 run_command python 绕过"这层语义。
8. `codex-with-chatgpt` 迁到 `~/.codex/skills/`。前置：核 author、核 `~/.codex` 与 `~/.codex-cli` 两个 HOME 都能发现它、删 `~/.claude/skills` 软链。收益主要是去掉 agy 里的误触发入口，字节可以忽略。
9. gg 召唤拓扑（属 review-routing，可暂缓）：无头 gg 在 monster cwd 下会加载 monster AGENTS，其中"monster 内 commit 直接执行不问"与 gg"不 commit"冲突，还会加载 MEMORY 预注，与 gg-briefing"❌ MEMORY narrative"冲突。P0-1 修好后预注这半自然消失；规则这半，可评估把单轮召唤的 workspace 改到 `~/githubProject/gg`（RN 路径已经用 `--cwd gg`）。

**观察不动**
- `file://` 两处不算重复：`monster-on-antigravity:14` 与模型无关，本会话是 Claude-in-agy，没收到 Gemini 卡，它就是唯一载体；gemini 卡第 5 条是模型偏差补偿，带指标。
- runtime.md 全文预注（8.2 KB）去掉 Muse 后保持。MEMORY 保持预注，依据 rounds 11-02 不动清单"保留 MEMORY 完整索引"。
- 宿主三处摩擦都**不加字**：`&&` 已由 `monster-on-antigravity:16` 用 batch_exec 化解；`invoke_subagent` 默认 inherit 已被 gemini 卡第 4 条、agy.md 分档表和 `monster-on-antigravity:11` 三处覆盖；`<artifacts>` 与 `output/` 的冲突先量一下，看 transcript 里有没有本应落 `output/` 却落在 `brain/` 的持久交付，第二次被证实再加一行。
- fleet 的 muse Tab 代码与 `agy.md:41` 文案：代码在，文案就如实；以后 fleet 去掉 muse 时再一起改。
- 华昇两个 skill 放在 `monster/.agents/skills` 是正确的作用域；项目是否结束由 Keith 判断。

**反对改动**
- 在探针 agy2 的 skill 索引之前拆 `~/.gemini/config/skills` 软链层。agy2 的 HOME 是 `~/.agy2-home`，它扫的 `~/.agents/skills` 可能不是同一棵树，软链层可能正是 agy2 的发现来源。先在 agy2 新会话里数一下 skill 条数再定。另外，agy 直扫 `~/.agents/skills`，说明软链层**不能当过滤器用**：要对 agy 隐藏某个 skill，只能把它移出 `~/.agents/skills`。
- 动 `frontend-design`/`microinteractions`/`storyteller`：rounds 不动清单（"不把设计执行器'可见'直接判误触发"）还在，本轮没有新证据。
- MEMORY 改成按需读；为宿主三摩擦逐条写覆盖条款。

**trade-off**：P0-3 选了撤销声明，没选全文回水，赌的是强制触发①会被执行（跑步机层）；如果之后发现压缩后漏查 thread 复发，就升级为回水 🔥 段或全文。P0-1 每次无头审查省 37 KB，代价是要先核 bot 路径，否则可能误伤个人飞书 bot 的预注。

**执行顺序**：P0-1（附反向用例）→ P0-5 Muse → P0-2/4 文案 → P0-3 回水 → P1-6/7 → 传感器全跑（`claude_d_reference_check --all`、`seam_check`、`resident_budget`）→ P1-8/9 按余力做。

## 核心假设
- 本会话收到的两段预注来自 SessionStart 或首轮补注，经 `is_personal_main_session_agy` 放行。依据是代码 + DB 行 + 进程参数，三者一致（n=1）；adapter 日志没读。
- agy 直扫 `~/.agents/skills` 采信简报，我没在 agy 新会话里独立数过。

## 可能出错的地方
- 如果飞书 bot 走 `agy -p`，P0-1 不加 bot 豁免会剥掉 bot 的预注。
- 如果 `muse-sensitive-data` 被某个非 Muse 流程暗中依赖（grep 只扫了 monster 和 `~/.agents`，没扫 cg 仓），归档会断掉它；但 consumer 列表里全是 muse 文件。

## 本次哪里思考得不够
- 没读 `monster-on-muse.md` 全文和 `commander/SKILL.md` 全文，只 grep 了口径行。
- 没验证 11-20 H1（热区哨）是否落地；monster AGENTS 现为 20.5 KB，tail 注入已是 no-op，那条风险暂时被 3.5 KB 余量覆盖。

## 如果 N 个月后证明决策错了，最可能的根因
撤销声明那一行没能阻止压缩后的漏查，因为摘要里的"已加载"信念比我那行声明更强。应改成回水 🔥 近 3 天段。

## 北极星触达
#1：看到的是"注入面的受众闭包"与"文案宣称的受众"之间的错位（无头被当主会话，gg 被 monster 规则覆盖），而不只是字节重复。#3：用进程参数和 DB 行，把一条基线假设换成了可核的事实。

## essence 对齐自检（必填）
- **对位**：`presence-benefit-splits-replica-verdict`（P1-6/7 按在场收益与受众判副本去留）、`one-shot-invariant-decays-under-live-append`（P0-2 排序漂移）、`perimeter-derives-from-load-path-not-self-model`（P0-1：受众要从实际加载路径推出来，不能从"无头不收"这个自我模型推）、`retiring-a-dead-mechanism-orphans-no-one-who-lives-elsewhere`（P0-5：Muse 拆除没有孤儿，代码保留）、`recurrence-defense-pays-on-second-occurrence`（artifacts 冲突先量、P0-3 先轻）、`evaluator-input-ownership`（P1-9 gg 视野被启动拓扑策展）。
- **反着走**：`ghost-rules`。P0-3 新增的一行是在防一个还没观测到的漏查吗？我的判断是不算：它撤销的是一张已经在场的错误豁免，属于减法性质。
- **cross-check 关键词**：上述 7 个 slug 全部 grep 命中（essence.md:110/161/43/189/318/209/323）。

## essence 候选（可选）
- 无。"启动拓扑回收外部锚独立性"可由 `evaluator-input-ownership` + `perimeter-derives-from-load-path` 组合推出。

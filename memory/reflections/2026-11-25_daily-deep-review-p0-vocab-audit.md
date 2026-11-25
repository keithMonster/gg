---
date: 2026-11-25
slug: daily-deep-review-p0-vocab-audit
summoner: monster（Antigravity 原生子会话；Keith 点名 call gg，审 harness-engineering/work/daily-deep-review-2026-11-25/REPORT.md + concepts.md + agent-memory-vocabulary.md）
northstar_reach: "#1 二阶效应 / #3 决策超越直觉"
status: substantive-decision
---

# Reflection: 11-25 全日复盘 P0/P1 与词表扩充独立审查

## 给父会话的最终输出（必填）

**Keith 没想到的一点**：`edit_exact.py` 全天 0 次调用，说明的其实是问题已经解决了。近 24h agy 共 207 个手写 str.replace 写回脚本，其中 200 个带命中断言（97%）；codex 115 个中 107 个带断言。这个工具当初要治的就是“11 月初约 2000/4100 次无断言”。批改规则本身写了“或逐处断言 count==1”，Agent 选了这条，因为不用记脚本路径。报告要做的 `--multi`，另一个会话已经以 `shared/scripts/code_mode_mcp.py` 做出来了（未提交，19:53 写入，带受保护路径拦截）。

**总裁决**：诊断方向对，P0 排序错。报告把三种原因不同的“0 调用”当成一种病，统一开了“改进工具”：edit_exact 是有合规替代且目标已达成，colab 是能力缺口，agent_thread/cc_binary_grep 原因未查。P0-1 砍；P0-3 砍新模块，只留两件小事；P0-2 做，但收口点要换、交给短剧会话；P0-4 本轮做，但范围要换：报告漏了一个真 bug，又把一个按设计如此的行为当成了 bug。词表中度膨胀。concepts.md 两条新 A 类要压缩，其中一条引用了 gg 尚未入库的候选 slug。

**P0-1 砍**。证据：写入 ≥2 次的脚本只占 agy 62/207、codex 18/115；单文件多块本来就支持（parse_blocks）；多个文件用 `&&` 串成一条 run_command，就只过一次云审，规则也允许这样做。动作：不改 edit_exact；词表 #13 的落点改指 code_mode_mcp。把 code-mode 写进批改规则之前，先核一条边界：MCP `batch_exec` 调用（内含 `cm.run` 任意命令）是否还经过 agy 云审？如果不经过，就是从“N 次审→1 次”变成“→0 次”，属于安全边界变更，按 review-routing 送审。顺带发现（宽匹配）：207 个脚本里有 30 个提到受守卫覆盖的路径，其中至少 5 个能看到字面写入目标（cg-platform/*.py、*.sh）。也就是说内联脚本通道已经在绕开 Write/Edit 守卫，而且目前没有传感器。

**P0-2 做，交短剧会话在下次换声时做**。证据：Agent 已经自己收敛了，今天的 v6/v61 是经 sys.path 从带日期的 work 目录 `from run_v5_batch_seedvc_colab import REMOTE_WORKER` 导入的。这个 worker 被原样复用两次，说明已经稳定，那个 work 文件事实上成了未登记的库。`colab_audio_tools.py` 只有 tts|lipsync 两个子命令，0 调用是能力缺口。`video-production/GUIDE.md` 第 92 行写着 colab_audio_tools 能做“声纹替换”，实际不存在：Agent 照这句去找工具，找不到，就退回拷贝。最小切面：新增 `voice-convert <spec.json>` 子命令，沿用现有 spec/recipe/--account 模式；worker 原样搬入；bigvgan 补丁和模型版本钉进 colab-recipes.json；补一条 dry-run 单测；改正 GUIDE 第 92 行和 toolbox 第 56 行。承印人那份 338 行变体等下次用到时再迁，不预先合并两份。防复发：在 woshizhimao/chengyinren 的工作区 AGENTS.md 各加一行“换声走 voice-convert”，那是会话开工时一定会读到的位置。

**P0-3 砍新模块**。报告说“4–5 处”，实际横跨 3 个根目录、2 种语言：清洗环境变量在 agy2_launcher.build_exec_env（py）和 monsterd agy_profile.ts（TS）；读取在 ~/.agents/hooks（另一个仓）；real home 在 harness-engineering/lib/agy_transcript.get_real_home 已有实现（12 处导入），launcher 另有一份语义不同的（认 AGY2_REAL_HOME）。monster 里的 py 模块服务不了 TS；hooks 反向 import monster，会把每个会话的 hook 绑在 monster 的导入健康上。正确的抽象是收口点，不是共享库：所有 agy2 子进程一律经 launcher 拉起；monsterd 侧靠 profile_lock_diff.test.ts 守护，补齐 agy→agy2 反向用例（目前只看到 agy2→agy）。inode 防护和 DB 有界等待各自只在一个点上，就地加回归测试，不抽。

**P0-4 本轮先做，因为报告的排序就建在这台扫描器上**。①“990 RUNNING 计入 errors”不是 bug：docstring L9-11 写明旧口径 errors 保留 RUNNING，供历史对比；新口径 error_clusters 已在 L449-451 排除。要改的是报告不再引用旧列。是否删列，先看 tripwire_check.py 是否消费它。②报告漏掉的真 bug：agy 的 reads/writes 计数（L437-440）只认旧工具名 view_file/AbsolutePath、write_to_file/TargetFile；现在的 agy 记录的是 read_file/Path、write_file、edit_file（本会话 transcript_full 实测：read_file 12 次，view_file 0 次）。所以 agy 的热读和写文件两个维度一直是空的，“canon-bugs 被整读 6 次”只统计到了 shell 的 cat/sed。③EXIT_RE 只扫 run_command/exec 的输出，不扫读文件的正文。④按 FIFO 对齐回执先不动，等观察到标错再改。另加一条自洽检查：tools[read_file]>0 而 reads==0 时告警（防被观察对象改了 schema、观察者没跟上），按准入三问② 在 tripwire_selftest 注册反向用例。

**5. 词表与 concepts**
- 出口闭环原则：保留，压成一行理论 + 主载体。必须改两处。第一，定义里引用了 `gate-leaks-at-exit-not-at-detection`：这是 gg 今早 reflection 里的候选滴，未过验证关，不是 essence。引用它就是让待批文本经旁路被消费，应删掉，或标“gg 候选未入库”。第二，删掉“1–2 轮断路器”：那是可调策略，不是概念。今早实测 8 次 design 里有 7 次在第 4–6 轮才拿到 PASS，轮次上限之所以安全，全靠 close 存在。概念应写不变量（非 PASS 结束必须登记处置），不写参数。
- 逆风三试 + 禁止冒充：条目自己说是“工程化「反逢迎/事实推进」”，按“演化只改一处”，应并作反逢迎条下的演化行，主载体指向 GUIDE §二；删掉枚举的例子（它们会与 GUIDE 漂移）。
- 调取失活“演化”：内容是一个实例，不是 reframe。改标“实例”，删掉 34.9KB 这个数字。低优先级。
- 词表（零常驻，每次被读才付成本，但每条“Monster 落点”都会漂移；#13 写入不到一小时就过期了）：#21/#22/#23 是教科书概念，裸模型能再生，唯一的增量是 canon-bugs 指针，压成一张“元模式 → canon-bugs 锚点”表；#16 与现有运行规则（禁 sleep 轮询）重复，删掉或压成一行；#17/#18/#19 都出自同一份研究报告，且多为“规划”，退回报告或标“未落地”；#20 只按一个原因解读 72.61%，另一种可能是修复引入了真的新问题，在 stats 把新问题分成域内/越界之前，只写“多轮新增问题占比高”；含糊的引文（"Goodhart's Law in Agentic Coding Loops"、“长上下文 Agent Loop 退化工程实践”、“多 Agent 审阅台设计模式”）要么补上实际出处，要么标“工程归纳，无单一出处”。
- tripwire：14 天后统计三端读取 agent-memory-vocabulary.md 的次数。≈0 就说明扩到 24 条什么也没换来，不再扩。调取失活同样适用于这份词表本身。

**P1 三分**
- 本轮立做：P1-4 的一部分。M8 用今天的读数（23.1%，基线 49.5%）收口，前提是判据口径一致。2 个已知红的单测，修好，或标 xfail 并写明理由和日期。codex_gate 的 24 条 unclosed_leaks 不要批量关闭：close 是 2026-11-25 08:10（29c92a89c）才上线的，11-23/24 的 21 条早于机制，stats 加机制截止线，标 pre-mechanism，不计入闭合率；11-25 的 3 条逐条处置。批量关闭正是今早预判的失败形态：处置字段漂向体面侧，指标被洗成 0。M2/M3/M12/M16 如果各是一条现成命令就当场跑，否则拆出去。
- 拆给专门任务：P0-2（短剧，触发条件 = 下次换声）；P1-1（短剧；只下沉已被跨目录导入的部分，wzm_cinema_qc → chengyinren/scripts/quality_probe 这条反向依赖是最强信号；slice ×3 等第 4 次出现或并发会话结束；cinematography 等并发会话提交后再合）；P1-3 tsconfig 对齐（Koi 任务；多人仓，先 git pull，单行高价值改动）；monsterd state.sqlite 诊断子命令（34 次手写，确实没有 CLI，交 monsterd 负责人）。
- 直接砍：agy_env.py；edit_exact --multi；P1-2 整包加 flag（先抽 5 例手写扫描，问“agent_thread 能不能做”，能做就是发现问题，改路由，不加功能）；“分层测试写进验收习惯”（prompt 层习惯是跑步机）；canon-bugs grep 提示（同理；6 次整读这个数还来自盲区扫描器）；platform-help 发布脚本抽常青（等第二次用到）。

**本轮执行顺序**：①concepts/词表修正 → ②efficiency_scan 最小修 + 自洽检查 → ③P1-4 部分 → ④给 code_mode_mcp 的作者带一句 MCP 云审边界的问题。其余拆出去。

## 核心假设
- 内联样本口径 = 近 24h 本机 agy 双号 + codex 四个 home，判据沿用 efficiency_scan 的 CATS/UNASSERTED（宽匹配，断言率偏高估）。97% 是上界，方向不受影响。
- code_mode_mcp 是在建中的合法产物，作者会接着把它接入规则。

## 可能出错的地方
- UNASSERTED 正则很宽（`count(` 任意命中），真实断言率可能低于 97%。不过即使降到 80%，`--multi` 也不是解药。
- 30 个受保护路径命中多为变量路径，没有逐个核实是否真的写入。
- 没读 colab worker 正文，也没 diff 承印人变体；M 项的复测命令没核；没核 MCP 是否过云审。

## 本次哪里思考得不够
- 没有逐条读 167 个 Turn≥3 新问题去判是域内还是越界，对 #20 的批评停在“不能单因解读”。
- 没用 transcript 统计词表的历史读取次数，只给了 tripwire。

## 如果 N 个月后证明决策错了，最可能的根因
- code_mode_mcp 没接上，或被判不安全而撤掉，“砍 --multi”就会留下多文件批改的空档。届时回退的代价很低：在 edit_exact 上加 `=== FILE` 块，约 30 行。

## 北极星触达
#1：把“0 调用 = 造了没用”拆成三种病因，其中一种的读法正好反过来（目标行为已达成）。#3：用原件否掉三个顺手的直觉（扩工具、抽公共模块、批量关账）。

## essence 对齐自检（必填）
- 对位：`means-end-inversion`（工具调用量被当成主战场）、`standing-instructions-do-not-produce-standing-behavior`（零读数不携带死因）、`signal-weak-vs-channel-dead-must-be-physically-disambiguated`、`stale-observer` / `one-shot-invariant-decays-under-live-append`（扫描器工具名漂移、词表落点过期）、`approval-gate-gates-status-not-consumption`（候选 slug 被 concepts 消费）、`self-graded-dignity-field-drifts-to-face`（批量关账）、`anchor-value-in-activation-not-in-content`（防复发挂在工作区 AGENTS.md）、`mechanism-relocation-has-its-own-precondition`（code-mode 承接的前提 = 云审边界）、`external-anchor-is-corroboration-not-foundation`（含糊引文）、`recurrence-defense-pays-on-second-occurrence`（发布脚本、slice）。
- 反着走：`omission-failures-evade-event-driven-sensors` 支持“共享函数会被新调用方漏调”，我据此选了收口点而不是共享库；但如果 monsterd 绕开 launcher 直接拉起，收口点也会漏，所以保留合约测试。
- 关键词：以上 13 个 slug 已 grep 原卷与索引，全部命中（3–17 次）。

## essence 候选（candidate-unverified，未 append）
- slug: `remediation-tool-is-graded-by-the-behavior-not-its-calls`
- 一句话：为纠正某种行为而造的工具，KPI 是那个行为的发生率，不是工具的调用量。行为被另一条合规路径纠正后，工具零调用是成功读数；按“造了没人用”去扩工具，等于给已经治好的病加药，同时漏掉真正有缺口的那几个。零调用至少有三种病因（替代路径已达标 / 能力缺口 / 发现失败），处置方向互相冲突。
- 证据：edit_exact 0 调用 vs 200/207 断言（目的原为治 2000/4100 无断言）；colab 0 调用 = 缺 seedvc 子命令且 GUIDE 虚报；agent_thread 2 vs 79 原因未查。相关滴：`means-end-inversion`、`standing-instructions-do-not-produce-standing-behavior`（“零读数不携带死因”在工具域的处方侧）。待验证关补审。

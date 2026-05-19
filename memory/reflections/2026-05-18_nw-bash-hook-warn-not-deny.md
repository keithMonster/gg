---
date: 2026-05-18
slug: nw-bash-hook-warn-not-deny
summoner: cc-space
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: NW 第 1 批 Bash 拦截 hook（G1+R1 合并）裁定

### 给父会话的最终输出（必填）

**推荐**：做这个 hook，但**改建模——做 PostToolUse 软提示注入（warn 档），不做 PreToolUse deny 硬阻断**。R1 提的 "exit 2 + permissionDecision deny" 建模错误：Bash cat 一个文件是**可逆动作**（代价=token 浪费+协作记忆污染，非数据损毁），不是 user_id/prod-push 那种不可逆红线，不配套 deny 闸。实施细节决策权在 Keith（落点 hooks/settings.json = nw-auto-apply 承重墙物理排除的行为规则类，永远走 Keith 闸门），gg 给架构推荐 + 标偏好位。

**理由**：
1. **该不该做=做，但重新归类**：76-82% 滥用率证明 prompt 软规则（全局 Engineering Rule #1）是跑步机失效（essence `rule-layer-flywheel`），值得上事件层飞轮。但事件层升级形态是**反馈注入**不是**硬阻断**——deny hook 要在"该拦的滥用"和合法 Bash（`ls -la`/管道里 grep/heredoc/`git log --grep`/装依赖）之间做语义判别，shell pattern match 做不准，误伤面（每次合法管道 Bash 被 exit 2 打断 → 协作摩擦）> 治理收益。essence `transparent-rewrite-breaks-contract` 直接适用：stdout 在 bash 是神圣契约，硬 deny 碰契约。
2. **边界**：拦截集 = `cat/head/tail/grep/rg/find/sed/awk` 八个；**不含** `ls`（`ls -la` 查 mtime/size 是 Glob 无法替代的合法用途，全局规则明示例外）、`curl/wget`（本会话已确认 rtk exclude）、`echo`（heredoc/管道赋值依赖）。放过规则（hook 内短路）：① 命令含 `|`/`>`/`>>`/`$(`/反引号（stdout 契约消费场景）② `git/npm/pip/docker/make` 子命令里的 pattern ③ heredoc `<<`。剩"裸 `cat file`/裸 `grep pat file`/裸 `find . -name`"才命中——恰好是滥用主体且无歧义。
3. **三档**：deny 否（误伤>收益+本体论错位）；ask 否（高频动作中断+subagent 无效）；**warn（PostToolUse 软提示注入）= 架构推荐档**——命中后不阻断执行，工具结果后注入 system-reminder 矫正提示，把信号物理钉进 transcript（飞轮），零误伤，持续矫正 LLM 的工具选择 prior。
4. **实现路径**：自写 ~50 行 `~/.claude/hooks/bash-tool-route-guard.sh`，**不 fork liberzon/claude-hooks 整仓**（essence `borrowed-method-as-mini-source`：fork 整仓=引入只用 10% 的外部依赖；它的复合命令 decompose 是 deny 多 sub-command 才需要的精度，warn 形态用不上——宁可对 `a && cat b` 整条提示也不漏 < decompose 复杂度）。借设计思想（pipe/子命令短路判别），不借代码仓。R1 的"dry-run 一周后切 hard-deny" **不执行**——warn 是终态。
5. **subagent 盲区**：接受部分覆盖（hook 对 subagent 结构性无效是平台事实 #22665/#27661，试图补全=造假锚点，违 `physical-anchor`）。结构=承认 hook 部分覆盖 + nw-daily 统计侧把 Bash 滥用率拆 `main_session`/`subagent` 双指标（否则 hook 真实效果被 subagent 噪声淹没，同 `extraction-rate-not-density` 不控浓度读不出真信号）。不为 subagent 盲区否决整 hook（主会话覆盖 ≠ 0 收益）。
6. **与今日两份 reflection 一致性=完全自洽**：本提案落点 `~/.claude/hooks/`+`settings.json` 正是 nw-auto-apply 承重墙物理排除的行为规则类——gg 不自主裁定实施、给推荐+标偏好位让 Keith 拍，跟 G1 原 resolution + nw-auto-apply 裁定严格一致；它落地后不进 NW 自动落地通道（落点白名单外），后续调 pattern/档位仍走 Keith，不会变"又一个绕过 Keith 的自动机制"。warn 形态=识别+提示≠判定+阻断，与 gg-review"识别停货架不自动判决"同构（deny 档反而会与 gg-review 克制原则冲突）。

**trade-off**：
- 代价 1：新建 1 hook 脚本 ~50 行 + settings.json 加 PostToolUse 配置 + nw-daily 统计侧双指标拆分（hook/settings 改动需 Keith 闸门，统计侧拆分在 nw-auto-apply 白名单内可机械落地）
- 代价 2：warn 不阻断 = 滥用仍会发生，只是每次留矫正信号——强制力弱于 deny，赌的是"持续 prior 矫正 > 单次硬拦"，若 Keith 要立竿见影压制率可能不满意（故留 ask-on-bare-subset 偏好位）
- 代价 3：subagent 路径滥用 hook 完全不覆盖，只能靠 subagent prompt 文本重述（harness CLAUDE.md:96 已写明），本提案不解决这部分
- 未核验假设：(a) PostToolUse hook 的 `hookSpecificOutput` 注入提示能进主会话 transcript 并形成下一轮 prior 矫正——基于官方 hooks reference 推断，未物理验证注入文本是否真被模型后续读到；(b) 八 pattern + 放过规则的边界在实跑中切得干净，未跑样本验证误命中率

**行动建议（父会话执行）**：
1. 采纳 warn 档，自写 `~/.claude/hooks/bash-tool-route-guard.sh`（放过规则按理由 2），settings.json 加 PostToolUse 配置——**此步 Keith 闸门**（落点行为规则类）
2. G1+R1 在 proposals.jsonl 合并：R1 标 superseded-by 指向本裁定；G1 resolution 更新为"gg 2026-05-18 裁定：warn 档非 deny，实施 Keith 拍偏好位"，status 保持 pending 等 Keith 对偏好位点头
3. **偏好位待 Keith 决**：warn（gg 推荐）vs ask-on-bare-subset（强力档，对裸命令无管道子集返回 permissionDecision=ask）——协作摩擦容忍度的个人偏好，gg 不替拍
4. nw-daily 统计侧 Bash 滥用率拆 `main_session`/`subagent` 双指标（落点 harness-engineering/analysis/，nw-auto-apply 白名单内，机械落地不占 Keith 闸门）
5. R1 "dry-run 一周后切 hard-deny" 不执行；liberzon/claude-hooks 不 fork

### 核心假设

- Bash cat/grep 类滥用的本质是可逆的协作偏好违反（token 浪费），不是不可逆红线——故配可逆软矫正（warn）而非 deny 闸；这个可逆性分类是整个裁定的承重墙
- PostToolUse 注入的矫正提示能进 transcript 并对 LLM 后续工具选择形成 prior 矫正（事件层飞轮假设成立）
- 滥用大头在主会话（R1 估 ~90%），即便高估，主会话部分覆盖仍有正收益，不必因 subagent 盲区否决

### 可能出错的地方

- **最大风险（概率 35%）**：warn 软矫正对 76-82% 这么高的滥用率压制力不足——LLM 的 Bash cat 是强训练 prior，一条 PostToolUse 提示可能矫正力衰减太快，跑几个月滥用率没明显下降，Keith 回头要 deny。缓解=已显式留 ask-on-bare-subset 偏好位给 Keith，且 nw-daily 双指标能实测主会话压制率，不是盲赌
- **次风险（概率 25%）**：八 pattern + 放过规则边界切不干净——`find` 在 `find . -name x -exec cat {}` 这种复合里、或路径含 pattern 字面量的边缘 case 误命中/漏命中，warn 形态下误命中只是多一条无害提示（不阻断），但漏命中=治理无效。warn 选型让误命中代价≈0 是这个风险可接受的关键
- **小风险**：subagent 滥用占比若实际远高于 R1 估的 10%，hook 整体收益被高估——需 nw-daily 双指标上线后用真数据校准，不在本裁定能解决

### 本次哪里思考得不够

- 没物理读 PostToolUse hook 的 `hookSpecificOutput` schema 和官方文档确认"注入文本是否真被模型下一轮读到、以何种 role 进 context"——warn 档整个有效性押在这个机制上，但我是基于 nw-auto-apply reflection 提到的"May 2026 hookSpecificOutput.updatedToolOutput 能力"+ 官方 hooks reference 的推断，未拉文档逐字核
- 没读 liberzon/claude-hooks 源码确认它的 decompose 逻辑具体形态——"warn 不需要 decompose"是基于"warn 不阻断所以不需精确到 sub-command"的推断，若它的 pipe 短路逻辑有可直接抄的 50 行，自写 vs 抽取的边界需父会话实施时再核
- 没展开 warn 注入文本的具体措辞设计——矫正 prior 的提示文本本身有 prompt engineering 空间（参考 PreToolUse hook 反例注入的现有实践），本裁定只定档位未定文本

### 如果 N 个月后证明决策错了，最可能的根因

最可能：**warn 的"软矫正能压住强训练 prior"假设证伪**——PostToolUse 注入提示对 LLM 是 context 里一条弱信号，而"看到文件就 cat"是预训练+海量 SFT 固化的强 prior，几个月后 nw-daily 双指标显示主会话滥用率纹丝不动，证明事件层飞轮在"对抗深层训练 prior"这个特定战场上力度不够，warn 和 prompt 软规则没有本质差别（都是 context 里一条字，只是一个在 CLAUDE.md 一个在 transcript）。根因：我把"事件层 vs prompt 层"的 essence `rule-layer-flywheel` 当成万能升级，但那条 essence 的飞轮性来自"物理触发+留锚点"，对"改变 LLM 即时行为"这个目标，留锚点 ≠ 改行为——锚点是给下一轮 gg/统计看的，不是给当前这一轮模型行为施力的。真正能施力的只有 deny（物理阻断改变本轮行为）或 prompt 反例注入到 PreToolUse（在动作前施力）。我选 warn 是为了避免 deny 误伤，但可能用"零误伤"换掉了"有效性"——fallback-detectability 的变体：warn 永远"看起来在工作"（每次都注入了提示），但它是否真改变行为无法从它自身判断，只能靠双指标证伪，而证伪要几个月。

次可能：偏好位留给 Keith 后 Keith 选了 ask-on-bare-subset，但裸命令子集的判别在实跑中频繁误判（把合法裸 `cat .env` 查配置也 ask），摩擦超预期，回退到无 hook，整个提案 40+ 天 pending 后归零。

### 北极星触达

**#1 二阶效应（space 方向）**：Keith 一阶诉求是"76-82% Bash 滥用率太高，上个 hook 拦住"。二阶结构是——这条提案从 5/1 起就被建模成"红线托底"（套 deny），但它治理的对象（工具选择偏好）是**可逆动作**，跟它套的强制档（deny=不可逆红线才配的闸）本体论错位。这跟同日 nw-auto-apply 揭示的"机械可逆落地 vs 行为规则变更被强行同池"是**同一个本体论错位的第三次显现**（第一次=2026-04-21 NW 治理档位，第二次=nw-auto-apply 同池同闸，第三次=本提案可逆动作套不可逆强制档）。更远一层：识别出"事件层飞轮"在"对抗 LLM 深层训练 prior"这个特定战场上可能力度不足（根因预判第一条），这对 cc-space 元方法论"内部不可靠→外部锚点托底"划了一条边界——锚点能给下一轮看、能给统计看，但不一定能给"当前这一轮模型行为"施力。这条边界对 5 年维度的 cc-space hook/治理设计有复利：不是所有"软规则失效"都能靠"升级到事件层"解决，要分清锚点的受力对象是谁。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `transparent-rewrite-breaks-contract` (2026-04-21)——deny 否决核心理由：stdout/pipe 是 bash 神圣契约，硬 deny 在合法管道处误伤=改写契约
  - `rule-layer-flywheel` (2026-04-24)——该不该做的核心：prompt 软规则=跑步机失效（76-82%），值得升事件层；但本裁定同时给这条 essence 划了边界（根因预判）——事件层飞轮的受力对象是下一轮/统计，不一定是当前轮行为
  - `action-type-over-aggressiveness` (2026-04-21)——三档不是激进度线性分级，是动作性质分流：可逆协作偏好配 warn，不可逆红线才配 deny；与 nw-auto-apply 同承重墙
  - `physical-anchor` (2026-04-16)——subagent 盲区处理：hook 对 subagent 结构性无效是平台事实，试图补全=造假锚点
  - `borrowed-method-as-mini-source` (2026-05-08)——实现路径否决 fork liberzon 整仓
  - `mechanical-apply-decouples-from-value-gate` (2026-05-18 今日 append)——本提案是其判别试金石在工具治理维度的第三个独立印证：剥掉价值判断后剩可逆软矫正，配 warn 不配 Keith 闸门外的自动 deny
  - `extraction-rate-not-density` (2026-05-07)——subagent/main 双指标拆分理由：不控浓度的合并指标读不出 hook 真信号
- **本决策是否在某条 essence 上反着走**：潜在张力，已展开——`rule-layer-flywheel` 主张"prompt 层=跑步机，事件层=飞轮"，本裁定选了事件层（warn hook）似乎完全顺着它走。但根因预判第一条恰恰论证了**本决策可能在这条 essence 上半反着走**：warn 虽在事件层，但它对"当前轮 LLM 行为"的施力可能跟 prompt 软规则无本质差别（都是 context 一条字）——飞轮性来自"留锚点给下一轮"，不来自"改本轮行为"。我没有因此改决策（warn 仍是推荐档，因为它零误伤且双指标可证伪），但显式标注了这条 essence 在"对抗深层训练 prior"战场上可能不适用——这是对该 essence 适用域的边界发现，非简单顺从或反走
- **cross-check 用的关键词**：grep "transparent-rewrite" / "rule-layer-flywheel" / "action-type-over-aggressiveness" / "physical-anchor" / "borrowed-method" / "mechanical-apply-decouples" / "extraction-rate"（启动时 essence.md 已 Read 全文加载 L1-L475，记忆中检索 + 物理确认 mechanical-apply-decouples-from-value-gate 在 essence.md 末条 L471-474 为今日 nw-auto-apply 已 append）

### essence 候选

- slug: `anchor-receives-next-round-not-this-round`
- 一句话：外部锚点（事件层 hook 注入/留痕）的受力对象是下一轮实例与统计观测，不必然是当前这一轮的模型行为——"软规则失效→升级到事件层"不是万能解，对抗 LLM 深层训练 prior 需要的是动作前物理施力（deny/PreToolUse 注入）而非动作后留锚点；判别试金石：问"这个锚点是给谁施力的——下一轮 gg、统计、还是此刻这个正在跑的模型"
- 是否已 append 到 essence.md: N（工作模式不擅自 append 新洞察候选，交设计模式判定；这是对 `rule-layer-flywheel` 适用域的边界精化，候选性质，需 Keith review）

### 外部锚点

- `~/githubProject/cc-space/harness-engineering/analysis/proposals.jsonl` ← G1/R1 合并落点（待父会话处理）
- `~/.claude/hooks/bash-tool-route-guard.sh` ← warn hook 落地点（待建，Keith 闸门）
- `~/.claude/settings.json` ← PostToolUse 配置（待改，Keith 闸门）
- `~/githubProject/cc-space/harness-engineering/CLAUDE.md` ← :50 nw-auto-apply 承重墙 + :96 subagent 平台限制（本裁定一致性依据）
- `~/githubProject/gg/memory/reflections/2026-05-18_nw-auto-apply-mechanical-boundary.md` ← 承重墙同源裁定（一致性检验对照基准）
- `~/githubProject/gg/memory/reflections/2026-05-18_gg-review-mechanism-placement.md` ← warn≠deny 与 gg-review 克制原则同构性对照

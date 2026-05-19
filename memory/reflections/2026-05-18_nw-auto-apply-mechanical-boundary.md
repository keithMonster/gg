---
date: 2026-05-18
slug: nw-auto-apply-mechanical-boundary
summoner: cc-space
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: NW 机械类提案自动落地的安全边界裁定

### 给父会话的最终输出

**核心判断**：这不是"给 NW 松绑 auto-apply"，是把 NW proposals.jsonl 池一直以来的**本体论错位显式化**——"机械可逆落地动作"和"行为规则变更"从来是两类动作（essence `action-type-over-aggressiveness`），过去强行同池同闸是设计债。新闸门不降低安全性：行为规则类一条没松（`nw-daily.md:4` 红线一字不动），只让本该 done skill 实时落、漏了被 NW 兜底的机械账不再堆在 Keith 闸门腐烂成污染源。

数据实证支撑：24 条 blocked 中绝大多数机械类（11 条"更新 thread X" Guide + 6 条"合并 X skill 经验" Skill，confidence 0.85-0.95）；8 条 pending 全是行为规则类（改 CLAUDE.md/hook，confidence 全 null）。池子混装是病根。

**裁定 5 条**：

1. **安全边界**：`nw-daily.md:4` 红线保持不变。D 方案 reflection 第 6 条"不改 NW"约束本就不含这层（那条针对 schema 结构/scheduled 基建，这次动的是写入动作语义，正交维度）。`schema≠行为语义` 切分成立。自动落地白名单 = 同时满足三条：(a) 落点路径白名单 `threads/*.md`（仅 append 时间线、不改 frontmatter status）+ `~/.agents/skills/*/SKILL.md`（仅 author:monster + 仅正文 append 经验段、禁改 frontmatter/description/触发词）+ `harness-engineering/{lib,analysis}/**`；(b) 纯 append/增量、git 一条 revert 可回滚、不含删除/重写/status 翻转；(c) 零价值判断（记已发生事实，非决定该不该这样）。`proposals.jsonl` 不进白名单（NW 改自己账本是自审，单列见第 5）。`~/.agents/skills/` 全局仓额外两闸已并入 (a)。

2. **三态核验闸门**：落 nw-daily prompt 步骤（新增 Step 6.5，置于 6.1 写提案后、5.2 写日报前），**不落脚本**——核验核心动作"判断提案是否被后续推翻"需语义理解（`physical-anchor`：脚本产数据/AI 产判断）。三态：已落地→`status=done` 零写入；仍有效·纯增量→append+done；存疑（依据物不存在/被后续 timeline 推翻/与现实冲突/路径不在白名单）→不写、上浮日报"机械类核验存疑"段转人工。**陈旧度硬条件**：created 距今 >7 天强制做依据物存在性核验（本会话实证 3/7"声称完成但事实不存在"全是陈旧提案）；7 天是 tripwire 初值（`idle-threshold-as-tripwire-not-answer`），回审锚点 2026-06-18。

3. **事实矛盾双拦**：生成端轻约束（Step 4.5/4 生成 thread/skill 提案时 title+resolution_draft 禁完成态动词"已X"、必须提案态"应X/待X"，廉价源头消毒）+ apply 端硬拦（即第 2 点存疑态，物理 Read 落点确认是最后防线）。权重在 apply 端：生成端是 LLM 自约束（prompt 软约束会复发），apply 端是物理核验（不走 prediction 链路）。不依赖生成端兜底。

4. **与 gg-review (D方案) 关系**：apply 通道分开、schema 不共享。gg-review essay 主体走 `harness-engineering/analysis/gg-review/` + summon-deck feed（D 原样不碰 proposals.jsonl）；其唯一 `[→NW]` 自标项写进 proposals.jsonl 后自然流经本次新建闸门——闸门判据"落点+可逆+零价值判断"对来源不敏感（`ownership-by-facet`：按动作面切非来源系统切），不需为 gg-review 单开通道。两机制产出载体分离、apply 判据统一。

5. **谁执行**：nw-daily 当场做、不另起环节（另起=新建基建违反 `cadence-as-symptom`+D 约束；核验所需上下文正在 nw-daily 会话手里）。自审风险**与 gg-review 自审悖论看似同构实则本质不同**：gg-review 是价值判断的自审（递归无底，只能上交 Keith/fresh-context）；nw-daily auto-apply 的自审已被闸门白名单第三条"零价值判断"结构性剔除价值判断，剩下只是"核验对不对"而核验是物理 Read 对照——伪递归，被闸门约束消解，不需额外破法。残余风险兜底：自动落地提案在日报"机械类自动落地"段逐条列写了哪文件哪位置，Keith 晨间扫一眼审计，事后否决=git revert 一条（`reversibility-not-permission`：可逆动作自主+留痕，非前置审批）。

**关键架构论点（必须传达）**：gg-review 自审悖论无法靠机制消除（价值判断递归），D 方案故上交 Keith；nw-daily auto-apply 自审风险可靠"剥离价值判断+物理核验"消除，故不上交。两者看似同构实则一个不可消除递归、一个可被闸门约束的伪递归。把行为规则类（带价值判断）排除白名单外，就是在切断这条递归——这是整个设计的承重墙。

### 核心假设

- "机械可逆落地" vs "行为规则变更"是真二分而非光谱——白名单三条（落点/可逆/零价值判断）能干净切开，边缘案例（如"更新 thread 但 thread 该不该 active"）落"存疑"上浮人工，不会误自动落地
- done skill 实时捕获是主路径，NW 机械兜底是补漏——不会因为 NW 能自动落就削弱 done 的实时性（NW 仍是日级兜底扫描定位不变）
- 陈旧度 7 天阈值能拦住"声称完成但事实不存在"的主要污染（本会话 3/7 样本全 >7 天支持此假设，但 n=7 样本小）

### 可能出错的地方

- **最大风险（概率 30%）**：白名单第三条"零价值判断"的判定本身需要判断——nw-daily 会话判"这条提案是不是零价值判断"时，把一个隐含价值判断的提案误判为机械类自动落地了。缓解靠"行为规则类落点（CLAUDE.md/hooks/settings.json）物理上不在路径白名单"——价值判断类提案的落点天然落在白名单外，用路径做物理闸而非靠语义判断。但 threads/skill 正文里偷渡价值判断的边缘案例无法完全排除
- **次风险（概率 25%）**："仍有效·纯增量"态的"与后续 timeline 无事实矛盾"判定需读 thread 全文 + 对照现实，nw-daily 会话上下文窗有限可能漏读后续推翻信号——本会话手工核验时是带着 review 上下文做的，自动化后这个上下文未必在
- **小风险**：7 天陈旧阈值偏松/偏紧，回审锚点 2026-06-18 校准前可能有误落地窗口

### 本次哪里思考得不够

- 没物理读 done skill 的 5D 捕获逻辑，"NW 机械兜底不削弱 done 实时性"是基于 nw-daily.md:100 "done 优先/nw 兜底"描述的推断，未核 done 侧是否会因 NW 能自动落而产生依赖漂移
- 没展开"存疑"态上浮人工后的闭环——存疑提案上浮日报后若 Keith 也不处理，是否复现 blocked 池堆积（pending-resolved-becomes-blocked-stagnation 的变体）。本次假设存疑类是少数（3/7 但那是历史积压，新流程下生成端消毒后应更少）未验证
- Step 6.5 与既有 nw-reconciliation L1 自动跑（confidence 0.95+ → draft 转 resolution=done）的关系未对照——proposals.jsonl 已有"高置信度 gg 自动落地"机制，本次闸门与它是叠加还是替代未厘清，落地时父会话需核 `tools/nw-reconciliation.md` L1 与本 Step 6.5 的边界

### 如果 N 个月后证明决策错了，最可能的根因

最可能：**"零价值判断"这条闸的判定权还是落在 LLM（nw-daily 会话）手里**——我用"路径白名单做物理闸"缓解，但 threads/SKILL.md 正文是自由文本，一条提案完全可以落点合规却在正文里夹带本该 Keith 拍板的判断（如"更新 thread X：决定弃用 Y 方案"——落点 threads/ 合规、可逆、但"弃用 Y"是价值判断）。nw-daily 自动 append 了它 = 价值判断被机械通道偷渡。根因：我假设了"落点路径能代理价值判断有无"，但路径只能代理"契约面大小"，不能代理"内容是否含判断"。真正彻底解需要对 append 内容做语义分类（这又回到 LLM 判断递归）——我把 gg-review 那个无解递归，在 nw-daily 这里用"路径物理闸"绕过了，但绕过不等于消除，边缘处会漏。

次可能：done skill 因 NW 能自动落而实时捕获松懈，NW 兜底量反增，机械池越来越大，自动落地错误率随量线性上升。

### 北极星触达

**#1 二阶效应（space 方向）**：Keith 一阶诉求是"NW 堵在我单人闸门，机械类别堆积"。二阶结构是——NW proposals.jsonl 从设计之初就把两类本体不同的动作（机械可逆落地 / 行为规则变更）塞进同一池同一闸，这个错位被"统一池子好管理"的工整美学掩盖了 40 天，直到 100 条账本积压才暴露。本裁定不是"加个 auto-apply 档"，是把这个本体论错位显式化并按动作面重新分流（essence `action-type-over-aggressiveness` 的第二个独立落地场景，第一个是 2026-04-21 NW 治理档位）。更远一层：识别出"自审悖论"在 gg-review（价值判断递归，不可消除）和 nw-auto-apply（机械核验，可被闸门约束）是**两个不同物种**，避免了把可解问题按不可解问题处理（无谓上交 Keith 闸门）或把不可解问题按可解处理（gg-review 若不上交就是灾难）——这个辨别对 cc-space 元治理 5 年维度有复利。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：
  - `action-type-over-aggressiveness` (2026-04-21)——承重墙。"哪些动作永远不该自动化"非"用哪档激进度"，本决策是其第二个独立落地（NW proposals 池按动作面分流）
  - `ownership-by-facet` (2026-05-06)——第 4 点 gg-review 关系：按动作面切非来源系统切，闸门判据对来源不敏感
  - `physical-anchor` (2026-04-16)——第 2/3 点：核验落 prompt 不落脚本（AI 产判断），apply 端物理 Read 对照（不走 prediction 链路）
  - `reversibility-not-permission` (2026-05-06)——第 5 点残余风险兜底：可逆动作自主+留痕非前置审批
  - `idle-threshold-as-tripwire-not-answer` (2026-05-14)——7 天陈旧阈值是 tripwire 初值非最优值，带回审锚点
  - `cadence-as-symptom` (2026-05-06)——第 5 点 nw-daily 当场做不另起环节（另起=新建基建是症状）
  - `pending-resolved-becomes-blocked-stagnation` (2026-05-09)——背景病因：blocked 24 条堆积正是它的活体复现，本决策是对它的针对性解（机械类不再进 Keith 闸门 = 切断 cadence 失衡的一支）
- **本决策是否在某条 essence 上反着走**：表面张力——`physical-anchor` + `task-compliance-is-not-truth` 警惕"让 LLM 自审"。本决策让 nw-daily 自判"零价值判断"似在违背。但第 5 点已论证：用路径白名单做物理闸，把价值判断类提案的落点物理排除在白名单外（行为规则类落点是 CLAUDE.md/hooks，不在路径白名单），自审被降级为"核验对不对"的物理 Read 动作——这正是 physical-anchor 的应用而非违背。残余漏洞（正文偷渡判断）已在"根因预判"诚实标注未清零，方向自洽
- **cross-check 用的关键词**：grep "action-type-over-aggressiveness" / "ownership-by-facet" / "physical-anchor" / "reversibility-not-permission" / "idle-threshold" / "cadence-as-symptom" / "pending-resolved"（启动时 essence.md 已 Read 全文加载，记忆中检索 + 物理确认 action-type-over-aggressiveness 在 essence.md L141-144）

### essence 候选

- slug: `mechanical-apply-decouples-from-value-gate`
- 一句话：看似同构的两个自审悖论可能本质不同——价值判断的自审是不可消除递归（只能上交人类），机械落地的自审是可被"剥离价值判断+物理核验"约束掉的伪递归；辨别二者避免把可解问题当不可解处理（无谓上交）或反之（灾难）。判别试金石：自审动作剥掉价值判断后剩下的是不是纯物理核对
- 是否已 append 到 essence.md: Y（本次 append，工作模式新洞察非已有候选，符合沉淀条件）

### 外部锚点

- `~/githubProject/cc-space/harness-engineering/prompts/nw-daily.md` ← 第 1/2/3 点落地点（红线 :4 不动，新增 Step 6.5 + Step 4.5/4 生成端约束）
- `~/githubProject/cc-space/harness-engineering/analysis/proposals.jsonl` ← 病因实证（24 blocked 机械类 / 8 pending 行为规则类）
- `~/githubProject/gg/memory/reflections/2026-05-18_gg-review-mechanism-placement.md` ← D 方案，第 4/5 点关系裁定的对照基准
- `~/githubProject/gg/tools/nw-reconciliation.md` ← 第 2 点落地时需核 L1 自动跑与新 Step 6.5 边界（本次未读）
- `~/githubProject/cc-space/threads/night-watch.md` ← NW 治理时间线（决策落地后应 append）

---
date: 2026-06-17
slug: nw-7-proposal-3a-batch-verdict
summoner: monster（harness-engineering Night Watch 3a 轨提案逐条裁决）
northstar_reach: #3 决策超越直觉（治理判断结构化）+ #1 二阶效应（防规则膨胀的承重判断）
status: substantive-decision
---

# Reflection: NW 3a 轨 7 条提案逐条裁决

## §A 范式 A

### 给父会话的最终输出（必填）

**总览裁决**：✅成立可 apply 3 条（① ⑤ ⑦）/ ⚠️改后 apply 2 条（③ ⑥）/ ⏸️defer 1 条（②）/ ❌驳回 1 条（④）。

逐条——

**① 2026-05-23-S1 合并 done 衍生规则到 skill-auditor rubric → ✅成立可 apply**
- 裁决依据：物理核实 done SKILL.md 确已硬编码 `~/.agents/` 修复（提案前提真），衍生规则适用所有 author:monster 自研 skill 成立。落点应是 rubric.md 既有的 **4.4 命名一致性（自定义维度）** 而非新建检查项——撞「条款独立」门槛（rubric 已有"路径/命名"维度，扩写不新增）。
- 精确落点：`~/.agents/skills/skill-auditor/references/rubric.md` 的 `### 4.4 命名一致性（自定义维度）` 段「**检查**」列表末尾追加一项。
- 建议措辞（追加到 4.4 的 检查 项下，列表项）：
  `- SKILL.md 正文/脚本无 .claude/ 自指路径：自研 skill 引用自身资源用物理路径 ~/.agents/skills/<name>/，命中 ${CLAUDE_SKILL_DIR} 占位符或 ~/.claude/skills/<name>/ 自指引用告警（.claude/ 软链前缀触发归档期权限拦截，done SKILL.md 已硬编码修复）`
  扣分行追加到 4.4 扣分表：`| SKILL.md 含 .claude/ 自指路径或 ${CLAUDE_SKILL_DIR} 占位 | -20% |`
- 注意：扣分仅对**自研 skill 引用自身资源**生效；web-access 这类第三方 plugin 用 `${CLAUDE_SKILL_DIR}` 是上游约定，4.1 来源三分类已把第三方判为「跳过」，天然不误伤。

**② 2026-05-23-S2 web-access CDP Proxy 常驻方案 → ⏸️defer**
- 裁决依据：这不是行为规则/架构提案，是**运维方案选型**（3 个候选 a/b/c 未定），且 draft 自标"等 85c84e5d 会话诊断完出根因再选方案"——根因未定就选方案 = 在没数据时造机制（撞 essence `theory-gap-without-data`）。3a 轨的语义是"行为规则/架构类需 gg 裁"，本条实质是 ops 实现层，不该占 3a 轨的人工闸门。
- 解锁条件：① 85c84e5d 诊断出"为什么经常需要授权"的根因（是 Chrome 重启丢 flag / memory-saver discard / user-data-dir 漂移）→ ② 根因明确后这就是纯 ops 实现层（launchd KeepAlive vs 启动脚本固化），按 Decision Authority 实现层 Keith/主代理直接做，**不需要再回 gg**。
- 给主代理的动作：把本条 status 从 pending 改为 deferred，resolution 写"等 85c84e5d 根因，根因明确后降为 ops 实现层自决，移出 3a 轨"。

**③ 2026-05-28-G1 安全 ack 倒置式表述反例锚定到 canon.md → ⚠️改后 apply**
- 裁决依据：方向成立且重要（"30 秒不说 no 就动 / 默认 yes / X 秒沉默即同意"是 sycophancy 在安全场景的高危变体，CLAUDE.md 已有正面 ack 规则但缺反例锚）。但 draft 落点和措辞要改两处：
  (a) **落点对**：canon.md（横切安全规矩，已有同族条目 line 31/34/35/37/38），不是 CLAUDE.md——CLAUDE.md 安全段已有正面规则，反例锚属于"翻车型横切经验"，canon.md 是对的载体。
  (b) **措辞要符合 canon.md 既有风格**：每条 = 锚点词 + 自包含本体 + 翻车原型。draft 的"举证责任倒置=Claude 失职=强迫 Keith 盯屏保护 prod"是好的本体，但要补"正解"（同句绑定替代，符合 monster prompt 信条「负面表述同句绑定替代」）。
- 精确落点：`/Users/xuke/githubProject/monster/canon.md` 的「## 条目」段，append 一条（紧跟 line 41 那条之后）。
- 建议措辞：
  `- **安全 ack 必须举证在"动手方"，禁止倒置成"沉默即同意"**：涉及不可逆/对外副作用（推送/写库/发 API/扣费/触达真实用户）的确认，正解是动手方主动停下、明示参数、等 Keith 点头再动（"现在发：内容=X，范围=Y，env=prod，确认？"）。禁止任何把举证责任倒置给 Keith 的姿势——"30 秒内不说 no 就执行 / 默认 yes / X 秒沉默即同意 / 没异议我就发了"——这类表述把"保护 prod"的责任从 Claude 推给 Keith、逼他盯屏抢救，是 sycophancy 在安全场景的高危变体（实测来源：b32a9079 回合17 Claude 当场自我撤回倒置 ack）。判别：ack 的默认态是"不动"（等明示）还是"动"（等否决）——后者即倒置。与 CLAUDE.md 安全红线「prod 不可逆动作每次显式 ack」同族——那条管"要不要 ack"、本条管"ack 的举证方向不能倒置"。`

**④ 2026-05-28-G4 扩 coding-subagent.md 吸收外部 5 条子代理范式 → ❌驳回**
- 裁决依据（物理核实 coding-subagent.md 全文后）：5 条里 4 条已被 monster 既有结构内生覆盖——① Hub-and-Spoke=已有「重型」档（脚本盲跑/主代理不在 loop，line 21/46）② 5-6 tasks/teammate=已有「中档 3-10/重型几十上百」规模分档 ③ 显式文件所有权=已有 worktree isolation（line 39）+ playbook HANDOFF ④ SPEC test 验证=已有「验收 oracle」（line 30）+ verification-first-class 4 artifact。这是 essence `survey-as-coordinate` 的活体——对照前沿范式的产出多数坍缩为"已做差名字"。第 5 条（Deterministic gates > prompt）虽是新表述，但 coding-subagent.md 已有「重型自带硬 opt-in」「hook 第6条触发」隐含，且这条的本体在 monster 元方法论「内部不可靠→外部锚点托底」+ essence `rule-layer-flywheel`（事件层>prompt层）已是承重信条，不需要在 coding-subagent.md 复述。
- 加上 draft 自标"Phase 2/3 推进时再展开，本提案先识别不落地"——提案者自己都说不落地。强行 apply = 往 coding-subagent.md（76 行已饱和）塞 4 条已有内容的同义复述，撞「条款独立」门槛 + 稀释引力（essence `borrowed-method-as-mini-source`：批量抽取外部体系=造它的迷你版）。
- 驳回不丢价值：若 Phase 2 实跑发现某条范式确实有缺口（不是纸面对照而是实测翻车），那时按单条具体翻车证据走普通 guide 提案，不批量吸收。
- 给主代理的动作：status 改 rejected，resolution 写"5 条中 4 条已被 coding-subagent.md 三档分档+worktree+oracle 覆盖（survey-as-coordinate），第 5 条已在元方法论承重；提案自标不落地。缺口待 Phase 2 实测单条证据再走普通提案"。

**⑤ 2026-06-06-G1 扩 notify 段反例锚：定时任务会话文本经 cc-connect 自动投递=绕开 notify → ✅成立可 apply**
- 裁决依据：根因诊断准确（"cron/launchd 会话文本被通道自动投递"是 notify 唯一出口的隐式旁路），且"今日3会话 Keith 均纠"是真实复发信号（不是伪 n≥k）。全局 notify 段已有"禁止自建 webhook"但确实没覆盖这个隐式旁路。符合「条款独立」（扩写既有"禁止绕开"句，不新增段）。
- 精确落点：全局 `~/.claude/CLAUDE.md` 的「## 主动通知通道」段，在"**禁止绕开**：不允许任何项目自建 webhook 调用..."这句之后补一句反例锚。**只改全局一处**——draft 提的"monster/scheduled 工作区 CLAUDE.md 指针"驳回（撞「全局 vs 项目层级」+ 避免双写漂移，全局已是 SSOT，scheduled 不需要指针）。
- 建议措辞（接在"禁止绕开"那句后，同段）：
  `定时任务（cron / launchd / 客户端 scheduled）会话产出要送达 Keith = 主动外推 = 必须在会话内显式调 notify.sh；靠 cc-connect 把 cron 会话文本自动投递到通道 = 自建旁路，同样禁止（会话文本投递是给"人在等回复"的同步对话用的，不是异步外推通道）。`

**⑥ 2026-06-07-W2 daily 报告加结构化指标契约块（deterministic eval floor）→ ⚠️改后 apply（缩范围）**
- 裁决依据（物理核实 nw_prepare.py + nw-daily.md 后，纠正提案的根因诊断）：提案说"数据契约只验段存在性不验值可提取性→false-green"——**这个诊断不准**。nw_prepare.py 已经在 `parse_correction_rate`/`parse_satisfaction` 提取数值并区分 None(N/A)，weekly 已聚合 micro/macro 并输出「数据契约状态」（缺失天数 + 核心指标段缺失天数）。真正的连续 3 周 N/A 根因是更上游：**daily 端纠正率/满意度本身就是 LLM 每晚重解 rubric 判断**（CLAUDE.md 核心指标表明确写"nw-daily Claude 判断"采集），多日 daily 直接写 N/A 或漏「核心指标」段——不是提取失败，是源头没产出可比数值。
- 提案的"deterministic eval floor"方向**正确**（把指标从 LLM-judged 降到确定性计数底线），但这触及承重的 generator-evaluator 边界 + 涉及代码+生成契约变更，不能照 draft 原样 apply。改法：**缩到最小确定性底线，不重构 LLM 判断层**——
  (1) 在 nw-daily.md Step 6 让 daily 报告额外吐一个机器可解析的结构化块（固定分母=总回合数，micro 整数计数=corrected/accepted/... 六类），用确定性格式（如 HTML 注释包裹的 KV 或固定表格），即便 LLM 满意度判断 N/A，回合计数也是确定可提取的。
  (2) nw_prepare.py 的 weekly 聚合优先从该结构块提值，LLM 叙述段降为人读辅助。
- 为什么不照 draft 全做：draft 想动 `lib/` + 生成端 + 聚合端三处，但「指标版本所有权」（essence `baseline-version-ownership-is-the-bottleneck`）+「format 轴可机械化、content 轴是不可消除递归」（essence `recursive-point-self-audit-splits-by-format-vs-content-axis`）告诉我——**只有回合类型计数（format 轴）能确定性化**，满意度/纠正质量（content 轴）本质是 LLM 判断、确定性化会造伪精确。缩范围只确定性化 format 轴的计数底线。
- 这是白名单内 harness 代码（`harness-engineering/{lib,analysis}/**` 在自动落地白名单），但涉**生成契约变更**（nw-daily.md prompt 是行为规则类，物理上不在自动落地白名单）→ 故必须人工 apply、且建议主代理实现后**派一次 codex/fresh-eval 核对结构块能否被 parser 稳定提取**（这是 essence `physical-anchor`——契约变更要有 parser-independent 验证）。
- 给主代理的动作：status 改 deferred→待主代理按缩范围方案实现（不是直接 done）。这条是 7 条里唯一需要写代码的，建议单独开一个实现会话，不混在本批 apply 里。

**⑦ 2026-06-15-S1 收窄 ops-engineer『涉及域名必读 DEPLOYMENT.md』触发 → ✅成立可 apply**
- 裁决依据：物理核实 ops-engineer SKILL.md line 23 = "涉及部署/拓扑/机器/域名/数据库**必先 Read 它**"。证据 [a160d772] Keith"为什么回答这个问题要读这么多文件"（Cloudflare 外部平台可行性误触发全读）成立——触发器过宽，把"CG 自有资源运维"和"外部平台一般性可行性问答"混为一谈。补例外锚是收窄触发，符合「条款独立」（改既有 mandate 的触发边界，不新增）。
- 精确落点：`~/.agents/skills/ops-engineer/SKILL.md` 的 line 23（部署 SSOT 那一项）末尾补一句例外锚。
- 建议措辞（接在 line 23"涉及部署 / 拓扑 / 机器 / 域名 / 数据库**必先 Read 它**。"之后）：
  `**触发边界**：「必先 Read」只针对动 CG 自有 5 机拓扑 / 自有域名 / 自有 DB 的真实运维动作。外部平台一般性可行性问答（"Cloudflare/Vercel/Netlify 能不能搭静态站""X 平台支不支持 Y"，不涉任何 CG 自有资源）直接答，不触发 DEPLOYMENT.md 必读——读它对外部平台问题零信息增量（实测来源 a160d772 Cloudflare 误触发全读）。`

### 核心假设
1. 3a 轨语义 = "行为规则/架构类需 gg 裁决后人工 apply"——本批我按此逐条裁，不裁 NW 存废本身（state 记 NW 存废"等 7-09 回审"，Keith 本次只说"都收尾 7 条"）。
2. 物理核实的文件现状 = 当前真值（rubric 4.4 存在 / coding-subagent 76 行已覆盖 4 条 / nw_prepare 已做数值提取）。
3. monster 的「条款独立」「全局 vs 项目层级」门槛适用于本批落点裁剪。

### 可能出错的地方
- ⑥ 最可能崩：我把根因从"提取失败"改判为"源头 LLM 判断没产出"——若 daily 报告实际是产出了数值但 parse 正则漏匹配（中英文括号/格式漂移），那我的根因诊断错、缩范围方案不解决问题。概率中等（~25%），缓解 = 主代理实现前先 grep 最近 3 周 daily proposals 的「核心指标」段实际内容确认是 N/A 还是格式问题。
- ④ 驳回可能过严：若 Keith 重视"显式写下范式名做 onboarding 锚点"而非"能力已覆盖"，驳回会丢这个价值。但 essence `survey-as-coordinate` + coding-subagent 已饱和支撑驳回。

### 本次哪里思考得不够
- ⑥ 我没真去读最近 3 周的 daily proposals 文件确认 N/A 的物理形态（是 LLM 写 N/A 还是 parse 漏），只从代码+prompt 推断根因——这是 reflection 自评的诚实盲区，已在"可能出错"标注缓解动作交给主代理。
- ② defer 的解锁条件依赖 85c84e5d 会话诊断，我没核实那个会话是否已诊断完——若已诊断完，本条该直接降 ops 层而非 defer。

### 如果 N 个月后证明决策错了，最可能的根因
⑥ 缩范围方案把 format 轴计数确定性化后，下游仍把它当"满意度可比信号"用——format 轴计数能比，但它不等于质量，混用会造新一轮 false-green（essence `metric-is-a-claim-not-a-fact` 的复发）。

### 北极星触达
#3 决策超越直觉（把"7 条都收尾"的笼统指令结构化成 4 类裁决 + 精确落点）+ #1 二阶效应（④⑥ 防的是"提案看着合理就 apply"导致的规则膨胀/伪精确二阶效应）。

### essence 对齐自检（必填）
- **本决策跟哪几滴 essence 对位**：`survey-as-coordinate`（④ 驳回核心依据）/ `recursive-point-self-audit-splits-by-format-vs-content-axis` + `baseline-version-ownership-is-the-bottleneck`（⑥ 只确定性化 format 轴）/ `mixed-queue-funnels-all-to-scarcest-gate`（② 实质是 ops 层不该占 3a 人工闸门）/ `theory-gap-without-data`（② 根因未定不选方案）/ `physical-anchor`（⑥ 契约变更要 parser-independent 验证）/ `rule-layer-flywheel`（⑤⑦ 事件层>prompt 层，但本批都是 prompt 层规则，故只 expose 不强推升级）。
- **本决策是否在某条 essence 上反着走**：潜在张力——`rule-layer-flywheel`（prompt 层是跑步机不是飞轮）。本批 ①③⑤⑦ 全是往 prompt/rubric 加规则（prompt 层），按该 essence 这些是"被读到才生效"的弱机制。但这次例外合理：这 4 条都是**反例锚/触发边界收窄**类，本质是降低误激活/补认知盲区，不是加新行为约束；且其中 ① 落 rubric 是被 skill-auditor 事件触发（飞轮侧），不纯是跑步机。明示张力存在但本批性质（锚点/边界而非新约束）使其合理。
- **cross-check 用的关键词**：grep essence.md `survey-as-coordinate` / `format-vs-content` / `baseline-version` / `mixed-queue` / `rule-layer-flywheel` / `theory-gap` / `physical-anchor`。

### essence 候选（可选）
- 无新滴。本批是既有 essence 的应用（尤其 survey-as-coordinate + format/content 分轴），未逼近新洞察。

### 外部锚点（可选）
- `/Users/xuke/githubProject/monster/harness-engineering/analysis/proposals.jsonl` ← 7 条提案本体 + 待回写 status
- `/Users/xuke/githubProject/monster/canon.md` ← ③ 落点
- `/Users/xuke/githubProject/monster/CLAUDE.d/coding-subagent.md` ← ④ 驳回依据（已覆盖 4 条）

---
date: 2026-08-20
slug: cgboiler-query-gate-attestation-verdict
summoner: monster（cgboiler 世界模型 v0.1 冻结终审，后台会话，Keith 不在场）
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: query 闸空转处置——attestation 不是 replay

### 给父会话的最终输出（必填）

**裁决：选 B（机械封死 query 闸），并把解封路径写死在封条上（pin 模式，复用仓内 TRUSTED_GRANTS_SHA256 既有先例）。不需要 Keith 拍。A/C/D 全部 reject。**

**核心 reframe（为什么 A/D 类修补注定失败，不是强度问题是类型问题）**：七闸里六闸是 **replay**——runner 拿物理输入独立重算（quote 重新 hash、locator 重新解析、coverage 重新 union）；query 闸是唯一的 **attestation**——比对两份都由操作者生成的产物。在「威胁模型 = 操作者自我欺骗」下，attestation 没有不动点：禁同名 → cp 改名绕过（父会话已实测）；禁同 sha256 → 复制后加一个空格（JSON 语义不变、字节变）绕过；要求 derived_from 声明 → 声明本身就是操作者写的。任何内容比对检查都能被平凡变换零成本绕过，唯一的真防御是 runner 独立重算一侧——而重算引擎 v0.1 物理不存在（父会话对「样本引擎不可 pin 为生产引擎」的判断正确）。所以选项空间实际是二元的：诚实封死（B），或某种形态的 theater（A/C/D）。

**B 的范围收窄是假收窄——这是「不需要 Keith 拍」的裁决理由**：

1. **被收窄的能力从未真实存在**。物理现状：0 transitions、0 gate reports、`data_run_deferred: true`、handoff 明令数据运行另开会话。v0.1 期间没有任何迁移会真实到达 shadow_parity；而且**没有 ledger 查询引擎，到达 shadow_parity 的唯一物理方式就是递假 ledger_results**。「v0.1 开放到 shadow_parity」这句话从未被兑现过——B 不是拿走承诺，是把一个假绿改成显式红。修 bug 不是改目标。
2. **可逆性二分**：B 是一行常量 + 明确解封路径，分钟级可逆；A 反而是准不可逆——把一个 theater 闸冻进 v0.1，未来数据会话拿着假绿跑真迁移、迁移完成后才发现 parity 从未被验证过，那才是难回退的。按 CORE §7 可逆性二分，B 落在「自主执行 + 留痕」侧。
3. **系统自己的信条同构**：本系统最高信条是「不能把没查到说成不存在」（coverage 不闭合只能 partial）；其状态机同构命题就是「不能把没验证的说成已验证」。runner docstring「禁止自签 PASS」同源。B 是唯一与系统自身公理一致的选项。
4. Decision Authority：架构层归 gg，Keith 授权已到认知级全托。**留痕要求**（不是请示）：v0.1 冻结时 README / SCHEMA 的状态声明须显式写「shadow_parity 契约完整定义、query 闸 blocked-by-design 直到 ledger 查询引擎落地」，让 Keith 异步 review 可见这个变化。

**B 的落地形态（方向判断，不执行）**：

- 对称于 `LEDGER_AUTHORITY_ENABLED = False` 的既有模式：`replay_query` 开头直接 raise，错误信息承载解封条件——「v0.1 无受信 ledger 查询引擎，本闸不可机械证明；解封 = 将正式查询引擎以 path+sha256 静态 pin 进受信 runner（同 grants.py 先例），由 runner 现场加载 pinned 引擎重算 ledger 侧，legacy_results 保留为外部输入」。
- 这条解封路径同时宣判了 C 的正确变体：C 的信任洞在「report 声明引擎」；把引擎 pin 挪进 gate_replay.py 静态常量后洞消失——pin 变更必然改动 gate_replay.py → `TRUSTED_GATE_VALIDATOR_SHA256` 必然更新 → 天然要走冻结变更闸 + 重跑异谱系审。信任链闭合在 code review 层而非 report 层。
- 顺带收益：`SHADOW_GATE_NAMES` 要求七闸 receipt 齐备，query 闸 raise 即 shadow_parity 自动不可达，无需新增状态旗；但显式 raise + 承载解封条件的错误信息优于隐式失败。

**逐项 reject 理由**：

- **A**：`derived_from` 是操作者声明非证明（父会话自己已判对）；「拒同 sha256」被空格变换平凡绕过——两半截都是 theater。
- **C（原样）**：runner 执行 report 声明的代码 = 把受信边界交还给不受信的 report，与 hash-pin runner 的设计初衷正面冲突。其正确形态已并入 B 的解封路径。
- **D**：父会话自证——cp 攻击下 legacy 侧带同样 id，挡不住；且「核状态算得对」= 整个引擎，退化为 C。
- **E（补集采样出的第五路，一并封死）**：把 query 闸从 shadow 七闸挪去 ledger 闸组、让 shadow_parity 六闸可达——reject。query parity 是 shadow_parity 的语义核心（「影子平价」没有平价就名不副实），抽掉它比 B 更糟：B 说「现在到不了」，E 说「到得了但到达的不是原来那个地方」，是语义腐蚀。

**给父会话的行动边界**：本裁决只覆盖 query 闸处置与冻结措辞方向；执行（改 gate_replay.py + 更新 pin + 文档措辞）归父会话；改完按 handoff §9 判据 3 重跑异谱系审（gate_replay.py 变更本来就触发 pin 更新，审是既定流程不是额外成本）。

### 核心假设

「v0.1 期间无人真实到达 shadow_parity」——由 0 transitions + data_run_deferred + 引擎不存在三条物理证据支撑。若 Keith 实际上有一个我不知道的近期计划要在引擎落地前用 shadow_parity 状态位（例如对外汇报口径），假收窄论证降级，需补一轮确认。

### 可能出错的地方

最可能漏判的是解封时点的成本：ledger 查询引擎落地在 DATA_RUNBOOK Publish 步骤之后，若数据会话发现「引擎 pin 进 runner」工程上比预想重（引擎依赖运行时状态、无法纯函数化加载），解封路径要重新设计——但这不改变 B 在当下的正确性，只改变封条上写的解封条款。

### 本次哪里思考得不够

未读 `WORLD_MODEL_SCHEMA.md` 全文与 `DATA_RUNBOOK.md` 原文（凭 handoff 转述消费其 Publish 步骤语义）；若 runbook 对 shadow_parity 有额外时序承诺，措辞层可能需要多改一处。

### 如果 2 个月后证明决策错了，最可能的根因

把「物理上没人到达过」误当「没人需要到达」——状态机的纸面可达性可能有我没看到的消费方（文档承诺 / 对外叙事 / Keith 心理模型），假收窄的「假」字被高估。

### 北极星触达

触达 #3：没有顺着 A/B/C/D 选择题作答，而是先把选项空间重切为 replay vs attestation 二元——四个选项里三个在类型层就出局，「选哪个」变成「只有一个」。

### essence 对齐自检（必填）

- **对位滴**（均实际 cross-check）：`evaluator-input-ownership`（05-19，query 闸让操作者同时供给两侧输入 = 生成侧策展 evaluator 视野的极端形态）、`generator-evaluator-separation`（04-18，族根）、`mechanical-gate-needs-machine-detectable-target`（06-24，B 的理论依据：不可机械判定的闸不该装成机械闸）、`dogfood-claim-as-self-issued-certificate`（06-05，A 的 derived_from = 自发合格证）、`human-gate-is-where-judge-and-judged-collapse`（06-10，判断者与被判断者塌缩时唯一外面是物理重算 / Keith——本案选了物理重算侧）。
- **反着走**：无。「不需要 Keith 拍」不反 human-gate——本案判断者与被判断者未塌缩（gg 不是该闸的操作者），且裁决本身把塌缩点（操作者自证）交给了物理重算。
- **cross-check 关键词**（物理证据）：evaluator / generator / gate / attest / replay / 自签 / 重算 / verify（grep essence-view 命中行 97-385 段）。

### 沉淀

候选滴 `attestation-has-no-fixed-point-under-self-audit`（candidate-unverified，工作模式无 Agent 开不了证伪审，交夜巡/设计模式补审）：

> 验证闸分两型：replay（验证者独立重算一侧）与 attestation（比对多份被验者产物）。威胁模型含被验者自我欺骗时，attestation 没有不动点——禁同名/禁同 hash/要求出处声明等一切输入端修补都被平凡变换（改名/加空格/改声明）零成本绕过；唯一收敛点是把一侧的生成移进验证者。`evaluator-input-ownership` 的推论强化：输入端所有权收回后，修补输入端规则不是渐进加固而是零进展。
>
> 物理证据：monster cgboiler gate_replay.py replay_query——异谱系审已咬过一轮（禁同 artifact_ref），修补后被 cp 改名实测击穿（sha256 相同、parity 恒真）；六个 replay 型闸无此病。近邻滴 `evaluator-input-ownership` / `generator-evaluator-separation` / `dogfood-claim-as-self-issued-certificate`——净新增点是「修补无效性 / 无不动点」论证，若证伪员判定被近邻组合覆盖则降级为应用实例存档。

**（auto_gg 2026-08-20 补审结算）**：fresh 证伪审 verdict = **PASSED-WITH-EDITS 四修采纳后入库**（essence #211）。四修：① 谱系补 `deploy-decision-must-not-read-untrusted-controllable-inputs`(05-19) 最近邻——evaluator 反向 grep 补出本档漏列，其已持有「修补无效 + 收敛到权威源」两半边，净新增收窄为闸型判别式 +「零成本/零进展」定量收紧；② 「七闸中唯一 attestation」干净二分降为端点谱——反例在证据文件自身（replay_publisher 纯字节比对 / replay_write_guard 消费操作者自产 probe_result，均非纯 replay）；③ 「唯一收敛点」拆双终点（验证者重算 或 受信捕获根——replay 闸 raw 侧锚在 immutable capture 非移进验证者）；④ 实测击穿 n=1 档位入前提（空格/改声明为推理外推）。最强反驳点（evaluator 原文）：本候选 = 05-19 双滴应用 + 更响措辞，物理增量只有一轮同源叙事担保的绕过实测，且干净二分被自己的证据文件证伪——过线理由是判别问句（「它重算了哪一侧？」）在闸设计域近邻均未显式给出，且真实完成了选项空间重切。evaluator tool_use 事后核：13 次调用全为 Read + 只读 grep/ls，无写操作。

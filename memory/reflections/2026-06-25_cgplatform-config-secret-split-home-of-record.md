---
date: 2026-06-25
slug: cgplatform-config-secret-split-home-of-record
summoner: monster (cg-platform)
northstar_reach: "#1 二阶效应（config/secret 分治是结构性解，非补值流程优化）"
status: substantive-decision
---

# Reflection: cg-platform 非密配置归位应用仓 — config/secret 真分治

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**裁决：采纳 Keith 候选方案的核心（非密配置归位应用仓、进 git、Keith 退出补值环路），但落点修正为单文件 `server/config.<env>.env`（不是 `server/config/<env>.env` 子目录）+ 一条新硬不变量「config-file 进 git 前必须全非密，由 deploy 期 secret-leak 闸门机械保证」。5 个架构选择逐条裁如下。**

**选择 1 — 契约 §2/§7「env-file 不进 git」改不改？改，但精确改：拆成两类载体、红线只收紧不放松。**

- 红线本意（你的取证事实 2 已证）从来是「**secret 不进 git**」，不是「**所有 env 值不进 git**」。当前契约把 config 和 secret 焊死在同一个 `<slug>.env` 文件里，于是「secret 不进 git」被过度泛化成「整个 env-file 不进 git」——**这是载体耦合导致的红线过包覆**，连非密 user_id 白名单都被一起锁进 Keith 经手环路。
- 正确动作：**契约 §2 显式拆成两个不变量**——`I-config:非密环境配置进应用仓 git`（user_id 白名单 / provider / URL / path / 超时数）+ `I-secret:secret 永不进任何 git，集中 map 注入`（DB_PASSWORD / *_API_KEY / *_SECRET / *_PAT / *_PASS）。§7「不进 git」从「env-file 整体」收窄绑定到「secret 类」。
- **非密 user_id 白名单进 git 可接受**——它本就是业务授权配置不是凭据，GitLab 仓已是 private（`cg-platform/<slug>`，企微登录态 + deploy-key 控制），user_id 在仓里的暴露面 = 它在应用源码 / PRD / registry.json `pm_user_id` 里本就存在的暴露面，没有新增攻击面。registry.json 早就明文存 `pm_user_id` 进 git——同构先例已成立。

**选择 2 — 配置落点：`server/config.<env>.env` 单文件，进 git。否决 registry 加元数据，否决 config/ 子目录。**

- **否决 registry 加字段**（你倾向否，我确认）：会造第二 SSOT（值同时在 registry 和应用仓）+ 违反 B5「别建平行知识结构」。registry.json 是平台资产账本，不是应用配置仓——配置归应用自己。
- **落点选 `server/config.<env>.env`**（平铺单文件，非 `config/` 子目录）：① 与 `.env.example` 同级、同 `server/` 根，PM/AI 一眼对照声明 vs 取值 ② OCCAM——9 应用没一个有「多文件配置树」需求，先别造目录层级 ③ `.env.example` 退回纯字段声明模板（你的方案对，保留）。命名用 `config.<env>.env` 不是 `<env>.env`，避免和根 `.env`（dev 本地）混淆。
- **`.env.example` 角色不变**：仍是字段 SSOT（闸门 presence parity 的左集）、仍 zod fail-fast 的声明源。它和 `config.<env>.env` 的关系 = 「声明 vs 取值」，parity 在同一个仓内自动成立——这正是你三词里「完善」的物理兑现（同 PR 同仓，闸门不再跨 monster/GitLab 两地查）。

**选择 3 — 平台耦合字段（ENV_NAME / DB_* / BUILD_COMMIT / PORT / CC_GATEWAY_URL）怎么分界？三类注入源，常迪一律不写。**

分界判据 = **「谁拥有这个值的真相」**：

| 字段类 | 真相拥有者 | 注入路径 | 进应用 config.env？ |
|---|---|---|---|
| `ENV_NAME` / `BUILD_COMMIT`(`CI_COMMIT_SHA`) / `PORT` / `CC_GATEWAY_URL` | 平台（部署期才知道） | deploy.sh `-e` 直注 | **否**（常迪写了也被覆盖，且语义错位） |
| `DB_*` | 平台（per-app 凭据） | datasources.json 字典注入 | **否**（已是 §2 现状） |
| secret（自声明账密 / API key） | 应用负责人，但值是密 | secrets.json map 注入 | **否**（red line I-secret） |
| 非密 config（白名单 / provider / URL / path / 超时） | 应用（常迪） | **应用仓 config.env，git** | **是** |

- ENV_NAME 必须平台注入不能进 config.env：否则 `config.prod.env` 里写 `ENV_NAME=prod`、`config.test.env` 写 `ENV_NAME=test` 看似合理，但它是平台的「我现在把你部署到哪」的自描述（§2 已立 ENV_NAME 是唯一合法环境锚点、禁应用自填反推），让应用文件名 `.<env>.` 和文件内 `ENV_NAME=` 双源声明环境 = 漂移风险。**deploy.sh 已经在注 ENV_NAME**（现 env-file 里那行 `ENV_NAME=prod` 同 DB_PASSWORD 一样是冗余、被部署期覆盖）——保持平台注入，config.env 不含它。
- BUILD_COMMIT / CI_COMMIT_SHA 当前 env-file 里是空值（L27/L33）——本就该 CI 注入，迁移时直接从 config.env 剔除，归 deploy `-e`。

**选择 4 — 迁移：渐迁，不一刀切。新应用模板即新范式 + 闸门双认（config.env 或 monster env-file 都放行），9 个在册按「下次该应用加字段时」自然迁。**

- 一刀切 9 个应用 = 9 次 test+prod 重新验证 + 9 次潜在 fail-loud，无收益堆风险（B3 cost-benefit：迁移本身不产生价值，只在「下次有人要加字段」时才兑现「Keith 退环路」收益）。
- **闸门改造一次到位**（这是真正的承重改动）：deploy.sh 字段闸门的「左集来源」从「monster `<slug>.env` ∪ map ∪ ignore」扩成「**应用仓 `config.<env>.env` ∪ monster `<slug>.env`(legacy) ∪ map ∪ ignore**」。即 config.env 提供的字段视为「已提供」。这样新旧两范式在同一个闸门下共存，迁移是 per-app 渐进的、不是 big-bang。
- 模板仓（`cg-platform/template`）改 `.env.example` 为纯声明 + 加 `config.test.env`/`config.prod.env` 骨架——新 fork 的应用天然新范式。
- runtime 合并顺序（deploy.sh L240-242 区）：`config.<env>.env`（应用非密，git）→ 叠加 monster `<slug>.env`（legacy 残留，存在才叠，优先级高于 config 兜迁移期）→ 叠加 map 注入 secret/DB（最高优先级）。**secret 永远最后注入、永远赢**——保证即使应用仓 config.env 误填了某 secret 字段，也被 map 覆盖（纵深防御，但不替代闸门）。

**选择 5 — 「活的主干 fork 不回写」不变量：不违反，你判断对，我确认。**

- 不变量本意 = 「fork 拿冻结快照，不回写模板仓 / 不建 fork↔template 同步协商通道」。应用自带 `config.<env>.env` 是**应用往自己仓里写自己的配置**，不碰模板仓、不碰 monster、不建任何反向同步通道——方向完全相反。
- 反而更合规：现状「配置值在 monster 侧 env-file」才是隐性的「平台持有应用的配置真相」耦合；归位应用仓后，应用配置真相归应用自己，**降低了 monster↔应用的耦合**，是 fork 自治的强化不是破坏。

**新增一条硬不变量（这是放 config 进 git 的安全前提，必须配套落）：**

> **`I-config-leak-gate`：deploy.sh 在读取应用仓 `config.<env>.env` 后、build 前，跑 secret-leak 闸门——扫该文件所有 KEY 命中 secret 命名模式（`*PASSWORD*` / `*SECRET*` / `*_KEY` 非空值 / `*_PAT` / `*TOKEN*` / `*PASS`）且值非空 → fail-loud 拒绝部署，提示「该字段属 secret，请移入 secrets.json map，勿写进进-git 的 config.env」。**

理由：放 config 进 git 的全部安全性，押在「进 git 的那个文件保证全非密」这一条上。Keith 约束里写的「这次进 git 的须**保证**全非密」——「保证」二字在 monster 元方法论里只有一个合法形态：**机械传感器**，不是人/AI 的自觉（B1「内部不可靠→外部锚点托底」+ 准入三问②「谁检验它持续成立」）。没有这道闸门，半年后某个 PM/AI 把 `WECHAT_SECRET=xxx` 直接写进 config.prod.env push 上 git，红线静默破防且无人知。这道闸门就是该约定的检验传感器，答得出准入三问②。

**行动建议（父会话执行，按序）：**
1. 改 `integration-contract.md §2`：拆 `I-config` / `I-secret` 两不变量；config schema 段加 `config.<env>.env`（进 git）；env-file schema 段标注「legacy 渐迁、新应用不用」。§7 红线措辞从「env-file 不进 git」收窄为「secret 不进 git」。
2. 改 `cg-platform-deploy.sh`：① 字段闸门左集加 `config.<env>.env` ② 加 `I-config-leak-gate` secret-leak 扫描（build 前）③ runtime 合并加 config.env 为最底层、map 最高层。改完跑 `sync-deploy-tooling.sh both`（CLAUDE.md 现状指针硬约束：runner 宿主人肉同步副本）。
3. 改模板仓 `cg-platform/template`：`.env.example` 退纯声明 + 加 `config.{test,prod}.env` 骨架（非密字段示例值）。注意 tripwire `cgplatform_scaffold_drift`——改模板要同步 scaffold 脚本认知。
4. 新增传感器候选：`config_leak_gate` 注册 `auto-monster/scripts/tripwire_check.py`（准入三问②的物理兑现）。
5. cg-patent-agent 作首个迁移样本（它正是触发本次的实例）：把 L9-58 非密字段搬进应用仓 `config.{test,prod}.env`，monster `cg-patent-agent.env` 保留 DB_*（实为冗余、可一并删走字典）+ 清空。验证 test 部署绿后再迁下一个。
6. **这是改上游契约（§2/§7）+ deploy.sh（契约 3 锚点）的承重改动，全局 Workflow #1 触发**——父会话落地前应把上述 5 步整理成方案文档给 Keith 异步过目（User Profile：信号词「把方案写好就行」语境下停在 plan，不主动张罗施工），尤其第 1 步红线措辞改动需 Keith 确认。我已做架构裁决，措辞落地是实现层。

### 核心假设

1. **GitLab 仓 private 且访问控制等价于「不增加 user_id 暴露面」**——基于契约里 `cg-platform/<slug>` 是 private group + deploy-key + 企微登录态的描述。若某应用仓被设为 internal/public 则假设破，但那本身违反平台默认。
2. **secret 命名模式可机械枚举覆盖**——`*PASSWORD*`/`*SECRET*`/`*_KEY`/`*_PAT`/`*TOKEN*`/`*PASS` 能 cover 川锅现有 secret 字段（取证已见 CGM_PASSWORD/MQTT_PASS/GITLAB_PAT/WECHAT_SECRET/*_API_KEY 全命中）。新型 secret 命名不符模式是残余风险（见下）。
3. **取证事实 1 物理成立**——我已亲读 cg-patent-agent.env 45 字段 + deploy.sh L181-259 字典注入逻辑，确认删 DB_* 后 40 字段全非密，唯一 secret 是被字典覆盖的冗余 DB_PASSWORD。非转述。

### 可能出错的地方

- **最可能崩点：secret-leak 闸门的命名模式漏判**（概率中）。某个 secret 字段命名不含上述模式词（如 `LLM_API_KEY` 命中 `*_KEY` 但假设有个 `CALLBACK_SIGN` 这种），机械扫漏 → secret 进 git。缓解：闸门 + map-最后注入纵深双层，且漏判的代价是「需手动从 git 历史清掉一个值」非「持续静默泄漏」（闸门会在该字段下次非空时报，只要值非空）。但 git 历史不可变是真实代价——这条残余风险须在方案里对 Keith 显式标注。
- 次可能：渐迁期「双载体」让某应用同一字段在 config.env 和 monster env-file 都有、取值不一致 → 合并优先级决定哪个赢。我定的「legacy env-file 优先于 config」是迁移期兜底（防迁移半途值丢），但若 PM 以为改了 config.env 生效、实际被残留 env-file 覆盖 → 困惑。缓解：迁移某应用时必须同步清空其 monster env-file 非密行（迁移动作的一部分，非可选）。

### 本次哪里思考得不够

- 没有展开 `dev_ro` / `.dev-ro.env` 这条线是否也该归位——它也是 monster 侧文件、也含 user 名（但含 `DEVRO_*` 密码，属 secret，不在本次 config 归位范围）。判断是 dev_ro 不动（它是 secret + 人工调研用、不是应用 runtime config），但没穷尽验证。
- 没核实模板仓 `.env.example` 当前结构（是否已有注释/分段），改成纯声明的具体 diff 留给实现层，可能有我没看到的格式约束。

### 如果 N 个月后证明决策错了，最可能的根因

secret-leak 闸门的命名模式被某个新型 secret 字段绕过，且 map-最后注入纵深防御因该字段不在 map（应用直接写进了 config.env）而失效——secret 静默进 git 公开历史。根因会是「机械传感器的覆盖完备性假设」过强。对冲：方案落地时把闸门做成「白名单式」更稳（只有显式标注 `# non-secret` 或匹配已知非密前缀的字段才放行进 git，其余一律疑似 secret 拦截）——但这会增加 PM 标注负担，是 trade-off，留给 Keith 在方案阶段定松紧。

### 北极星触达

**#1 二阶效应**：本裁决不是「优化 Keith 补值的操作」（一阶），是识别出「config/secret 载体耦合 → 红线过包覆 → Keith 被焊进非密配置环路」的结构因，用「拆载体 + 机械闸门保证」根除。Keith 退环路是结果，结构分治是因。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`reversibility-not-permission`（判据是动作可逆性——config 进 private git 可逆、secret 进 git 不可逆，二分决定载体）；`physical-anchor`（「保证全非密」只认机械传感器不认自觉）；monster 侧 `attribute-failure-layer-before-restructure`（红线过包覆是 L2 载体设计问题，不是加规则能治——拆载体是结构动作）。
- **本决策是否在某条 essence 上反着走**：潜在张力——`occams-razor`/防御式思维警戒（CORE M1）会问「加一道 secret-leak 闸门是不是又一条外加栏杆」。判断不是：它不是「禁止 X」的自觉栏杆，是把「config 进 git」这个新开口的安全性外化成传感器——开口是 Keith 拍的目标，闸门是开口的承重托底，符合准入三问②「谁检验它持续成立」。无栏杆则开口本身不该开。
- **cross-check 用的关键词**：grep 概念 `reversibility-not-permission` / `physical-anchor` / `external anchor` / `占包覆 红线`（凭 CORE §7 可逆性二分 + gg-briefing B1/B7 + monster 元方法论准入三问内化判断，未单独 grep essence.md 全文——议题判据已由 CORE §7 二分 + briefing invariant 充分覆盖）。

### essence 候选（可选）

- slug: `red-line-overcoverage-from-carrier-coupling`
- 一句话: 红线被过度泛化，常因「该红线」和「不该红线」的东西被焊在同一个载体里——拆载体比加豁免规则更根治。
- 是否已 append 到 essence.md: N（留 Keith review 后定，避免噪音）

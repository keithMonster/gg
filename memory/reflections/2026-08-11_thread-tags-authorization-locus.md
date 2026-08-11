---
date: 2026-08-11
slug: thread-tags-authorization-locus
summoner: monster / platform-help 读取面白名单
northstar_reach: "#1 二阶效应"
status: substantive-decision
---

# Reflection: thread frontmatter 语义标签 vs 集中白名单 —— 授权意图的落点

### 给父会话的最终输出（必填）

**推荐：不做 tags（第一版也不做）。改做三件小的：① 堵住 registry 派生的自授权路径 ② 把"最不该放"负面点名移出通道可读面 ③ 给"会忘"配提名式传感器（人拍放行）。**

**两条物理发现（本次实查，非估）**

1. **今天的白名单不是"一处集中文件"——第三个源在这条通道自己的写权里。** `cc_codex_wrapper.derive_app_threads()` 从 `cg-platform/registry.json` 派生 `read threads/<slug>.md`（存在即放行），而 `cg-platform` 在 `BASE_ALLOW` 里是 **write**，`guard_platform_mechanism` 只比对 registry 的**字段名集合**、不管新增 slug key（`platform-help/CLAUDE.md` 明写"三个 JSON 里加应用条目"属应用层照常做）。实测：构造一条 slug=`fund-balance`、复用既有字段名的条目，`_content_text_verdict` 返回 `blocked=False`；`threads/fund-balance.md` 存在 → 下一轮 session 编译 profile 时即被放行。即**这条对外通道能给自己开读权，落点恰好是"最不该放"清单里的组织财务 thread**。触发不需要恶意 PM，一次 prompt injection 或一次 slug 撞名的 onboard 就够。essence `deploy-decision-must-not-read-untrusted-controllable-inputs`（05-19）逐字命中：决策函数的事实输入不得有任何一个是不可信方物理可写的。
2. **`read-allowlist.txt` 第 124-137 行把 20+ 条最敏感 thread 的 slug 按类点名列出，而这个文件对通道可读**（`read platform-help`）。`platform-help/CLAUDE.md` 明写"不描述边界形状"，这段注释是它的直接反例：文件读不到，但"monster 里有 `salary-slip-archive` / `fund-balance` / `neican-memory` / `tencent-wecom-relations`，分组织人事财务、对外话术策略、别人的机器、通道拓扑四类"全给出去了。**这与做不做 tags 无关，独立成立、独立要修。**

**裁 Q1（值不值得做）：不值得，且第一版的价值是负的。**
- `cgboiler AND NOT confidential` 是**一个 bit**，和"这行在不在 allowlist 里"完全同构。第一版 tags = 把同一个 bit 从 1 个带守卫的文件重编码到 ~70 个 frontmatter，不新增任何表达力。
- 它自动化的恰好是**已经 fail-safe 的那半**：漏标 → 拒读 → PM 少一段背景（服务质量降级）。没自动化的是危险那半：错标 `cgboiler` → 静默泄露，无告警、无检验者。monster 自己的准入三问②「谁检验它持续成立」在这里答不出来。
- 「两条 todo 共用一个机制」不成立：暴露安全性与参考相关性是两个**面**（essence `ownership-by-facet`）。`cg-infra` 对 PM 暴露安全但作参考语料未必相关；monster 元基建 thread 可能是好参考却绝不能对 PM 暴露。两个集合不重合，共用一个 tag 是典型产消错位。
- 每月 1~2 条的痛点体量，配不上 183 文件的本体论级变更（`ontology-expansion-velocity-needs-cap`：本体论级变更须先立封顶原则与新增标准）。

**裁 Q2（集中 → 分散是不是架构级退步）：命题的前提不成立，但结论方向对，理由要换。**
- 不是"集中 vs 分散"，是"含自授权路径的三源 vs 无自授权路径的源"。按可审计性算，tags（threads/ 对通道不可写）反而比今天的 registry 派生**更干净**。
- 真正搬不动的代价不是可审计性（`--dump-profile` 确实能补），是**写入时的帧**。allowlist 文件头那句「改本文件 = 改这条通道能看见的世界，属信任根」在下笔的那一刻就在眼前；thread frontmatter 的写入帧是「记一个主体」，安全判断在那一刻根本不在视野里——这是 L3b 召回失效，不是文档问题，注入器也救不了（写 thread 的会话不会被提示"你正在配置一条对外通道的读权"）。
- 所以判据是：**授权决定必须留在带帧的落点**。分散本身不是罪，剥掉帧才是。

**裁 Q3（两个口子）**
- **① `monster` 标签：不存在。** 消费闭包只判 1 bit 时，人类值的 taxonomy 之争是文档问题不是数据模型问题（essence `sensor-exemption-is-a-tag-not-a-lifecycle-value` 07-21）。同一把刀往回切一格，`cgboiler`/`confidential` 二值本身也过不了这条——它们合起来还是那 1 个 bit。
- **② `confidential` 语义不纯：不是洁癖问题，是判定者不同。** (a) 真机密 = **内容属性**，thread 自己知道；(b) 不该让 bot 谈自己（通道与认人拓扑）= **通道属性**，thread 不知道、通道知道。(b) 写进 thread frontmatter = 让被保护对象记录保护它的拓扑，归属错位。**(b) 永远留在消费端**（wrapper 硬编码排除），这条独立于做不做 tags 都成立。

**裁 Q4（最小切面）—— 替代方案三件，总量约 30 行改动**
1. **堵自授权路径**（二选一，推荐 B）：**A** 删 `derive_app_threads`（实测今日派生集 25 条 ⊆ 显式列表，删是当日 no-op，`cg-dev-console`→`dev-console` 的静默漏口一并消失）；**B** 保留派生，把 `guard_platform_mechanism` 的 registry 判据从"字段名集合"扩到"**新增 slug key 也算机制层**"——这与 `platform-help/CLAUDE.md` 已写的「新建应用的 slug/pm/db-mode 三项要 Keith 拍」对齐，只是把那条 L2 规则机械化。B 保住 Keith 要的自动化方向，故推荐 B。
2. **把 124-137 行那段负面点名移出可读面**（`platform-help/**` 整目录 read），落 `CLAUDE.d/`（对通道 deny）。allowlist 里只留一句「显式不放行清单见 CLAUDE.d/，本文件不列」。
3. **"会忘"配提名式传感器**：夜跑列出「近 30 天新建 / 更新、语义疑似川锅项目、但不在 allowlist」的 thread 候选，**只提名不放行**，Keith 一句话过。机械那半（提名）自动化、价值那半（放行）留人 —— essence `mechanical-apply-decouples-from-value-gate`（05-18）。缺席型漏报不产生事件，故必须周期抽样而非事件驱动（`omission-failures-evade-event-driven-sensors`）。

**如果 Keith 仍要 tags（他拍板高于本裁决）：唯一硬条件 = 别让安全边界当新本体论的第一个消费方。** 先接「应用参考哪些 thread」那个 todo（失败模式无害：多一份少一份参考文档），跑够样本、错标率有实测后，再谈要不要让 seatbelt profile 读它。且无论何时，`confidential` 的 (b) 类不进 thread。

**行动建议（父会话下一步）**：先修 1 和 2（安全性，与 tags 决策解耦，今天就能做）；3 作为「白名单派生」这条 todo 的收口写法；tags 本身回 `inbox/topics.md` 挂着，等第一个无害消费方出现。

### 核心假设

- 假设 platform-help 会话对 `cg-platform/registry.json` 的写权在真实运行路径上可达（BASE_ALLOW write + guard 放行两条已实测；未实测端到端跑一次真实写入——那属外部副作用，不做）。
- 假设「每月 1~2 条手工行」的增长率测量为真（父会话给的，未复核 `started` 分布）。
- 假设 threads/ 对该通道不可写（seatbelt default-deny，未列 write）。

### 可能出错的地方

最可能崩在「tags 只值 1 个 bit」这个论断上：如果 Keith 的真实意图不是喂白名单，而是给 183 个主体建**领域本体**（他说的"或者其他"），那我按第一消费方定价就低估了。缓解是我没否掉本体论本身，只否掉「让安全边界当第一消费方」。

### 本次哪里思考得不够

没量化发现 1 的可利用性——prompt injection 经 PM 文本进入 platform-help 会话的真实概率没有本地实证，我按"结构性存在即需修"处理，可能对 Keith 的威胁模型（防手滑 vs 防恶意，essence `security-invariant-encodes-an-owner-set-threat-model`：这是 owner 参数）过度加权。修法 B 成本极低（~5 行）故这个过度加权不贵，但判断本身没上交 Keith。

### 如果 N 个月后证明决策错了，最可能的根因

第二、第三个消费方真的出现（给建龙的通道 / app-context-kit / 公开子集），届时手工白名单要复制三份，而 tags 恰好是那时该有的东西——我这次按"第一消费方"定价，等于把一个本体论投资推迟到它已经痛的时候才建。反向预判：那时重建的成本仍只是给 ~70 条 thread 加一行 frontmatter，不比现在贵——这条是我判它可推迟的依据。

### 北极星触达

**#1 二阶效应**：父会话问的是"契约变更值不值得"，实查后发现要裁的前提（授权集中在一处）本身不成立，且集中处正在被绕过。二阶点 = 授权机制的风险不在"意图存在哪里"，在"意图的输入源谁能写"。

### essence 对齐自检（必填）

- **对位**：`deploy-decision-must-not-read-untrusted-controllable-inputs`（05-19，逐字命中发现 1）/ `ownership-by-facet`（05-06，两 todo 共用 tag 的产消错位）/ `sensor-exemption-is-a-tag-not-a-lifecycle-value`（07-21，1-bit 闭包 → taxonomy 是文档问题）/ `mechanical-apply-decouples-from-value-gate`（05-18，提名自动化 + 放行留人）/ `ontology-expansion-velocity-needs-cap`（05-07）/ `omission-failures-evade-event-driven-sensors`（07-28）/ `security-invariant-encodes-an-owner-set-threat-model`（06-17）
- **反着走**：`safe-default-by-whitelist-inversion`（05-19「安全性来自极性方向非枚举完备性」）对我有张力——我这次恰恰在为"枚举"辩护、反对把极性下放。解释：tags 方案的极性其实**没变**（fail-closed 照旧），它换的是**枚举的落点**；那滴管极性、不管落点，故不构成真反例，但张力提醒我别把"手工枚举"本身当成美德。另有 `separation-need-is-not-topology-verdict`（06-10）轻度反向：我建议"先试最轻治理形态"，与它同向；但我拒绝新建 tag 本体论时用的是同一把刀，方向一致不算反走。
- **cross-check 关键词**（物理证据）：`grep -o` 于 `memory/essence/2026-H1.md` + `memory/essence.md`，命中计数 deploy-decision×1 / safe-default×4 / sensor-exemption×2+1 / ownership-by-facet×1 / ontology-expansion×2 / mechanical-apply×4 / separation-need×3 / isolation-key×1

### essence 候选（可选）

- slug: `authorization-intent-must-stay-in-a-framed-locus`
- 一句话: 授权意图搬家的代价不在可审计性（可用 dump 补），在**写入时的帧**——集中文件把「你正在改一条对外通道能看见的世界」放在下笔那一刻的视野里，搬进被授权对象自身的元数据后帧被剥掉，写的人以为在记录属性、实际在配权限；故授权决定的落点判据是「写它的那一刻，写的人知不知道自己在授权」，不是「读它的人能不能审计」。
- 物理证据：`platform-help/read-allowlist.txt` 头 24-26 行（信任根自述）vs `threads/README.md` frontmatter 字段契约（无任何安全语义）；`guard_platform_mechanism.is_trust_root` 按路径前缀守 `platform-help/**`，183 个 threads/ 文件在守卫外。
- 相关既有滴: `frame-grammar`(04-29) / `security-claim-as-physical-fact-not-injectable-grant`(05-19) / `deploy-decision-must-not-read-untrusted-controllable-inputs`(05-19) / `anchor-value-in-activation-not-in-content`(06-01)
- 是否已 append 到 essence.md: **N — candidate-unverified**（工作模式无 Agent 工具，开不了 fresh 证伪审；待 auto_gg 夜巡或设计会话补审）

### 外部锚点

- `/Users/xuke/githubProject/monster/platform-help/read-allowlist.txt`
- `/Users/xuke/githubProject/monster/shared/scripts/cc_codex_wrapper.py`（`derive_app_threads` / `BASE_ALLOW`）
- `/Users/xuke/githubProject/monster/shared/scripts/guard_platform_mechanism.py`（`_content_text_verdict` / `is_trust_root`）

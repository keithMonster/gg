---
date: 2026-05-22
slug: cg-platform-template-context
summoner: monster
northstar_reach: n/a 非北极星触发（架构层文档形态裁决）
status: substantive-decision
---

# Reflection: cg-platform 模板仓上下文补全方案裁决

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**裁决汇总：**

| 问题 | 裁决 | 关键修改 |
|---|---|---|
| 1 横向系统目录进模板仓 | 修改后接受 | 不违反 living-trunk 不变量——管辖域错配（见下）。但 brief 托底论证瞄错靶子，换机制：每条系统记录加 `verified: YYYY-MM-DD` 字段 + 文件头写死快照契约（"字段与指针冲突以 canonical 源为准，接入前核实关键契约"）+ brief §4 列的 4 个未落地缺口单独切 `## 未落地/不可 copy-as-is` 区，与"不要碰"反例区**并列分开**（反例=永远绕开，缺口=将来会通，AI 处理动作不同） |
| 2 指针策略 | 接受 | "指针只指 fork 环境可达目标"完全正确——是本方案最扎实一处。补一条：monster 侧 `cg-platform/docs/capability-map.md` 加各条目的 monster 侧事实来源映射（哪个 thread / DEPLOYMENT.md 段），给维护者用；fork 应用读不到 monster 不受影响。两类读者各有指针网络互不污染。零额外成本（§6 辐射本来就动 capability-map §3） |
| 3 独立文件 vs 并入 §0 | 接受独立 `docs/PLATFORM-SERVICES.md` | 判据=漂移源不同必须物理隔离。ENGINEERING-STANDARD 描述模板仓内部研发约束（SSOT 在自己、慢变量），PLATFORM-SERVICES 描述外部系统接入契约（SSOT 在 cg-proxy/cc-gateway 各自的仓、模板仓不控制、快变量）。快变量塞进慢变量文档=污染。`§0.3/§0.6` 现有对 cg-proxy/cg-api 的提及改为指向 PLATFORM-SERVICES 的指针，禁双写 |
| 4 纵向扩 §10 + skeleton 内联 | 接受，无修改 | 与问题 3 同一原则（不矛盾）：看内容 SSOT 在哪、漂移源是谁。纵向内容（文档地图/阅读顺序/填写指引）SSOT=模板仓自己，与 §10 已有"内容归属表"同源同漂移频率→同源合一。横向异源→分离。skeleton 内联 `<!-- 填写指引 -->` 是正确形态——指引放在使用现场，零检索成本 |

**额外两点 brief 没问到、架构上更该担心：**

- **A. 双源漂移**：PLATFORM-SERVICES.md（fork 消费视角）与 capability-map.md（平台自审视角）描述对象高度重叠（都讲 cg-proxy/cc-gateway 能干什么），必然 drift。必须现在划清：两份文档文件头各写交叉声明（视角不同、不互为副本、各自 canonical 边界），否则三个月后没人记得为什么有两份讲 cg-proxy 的文档。
- **B. 环境前提隐式假设**：PLATFORM-SERVICES.md 所有契约（`*.cgboiler.com` 域名 / 内网 VPC 段 / `db.cgboiler.com:9033`）隐含"应用跑在川锅 VPC 内"前提，模板仓没一处把它写成显式约束。错误网络环境 fork 会写出连不通的代码、陷入根因不在视野的调试黑洞。文件头加一句环境前提断言（"本文件所有契约前提=应用部署在川锅生产网络内可访问 `*.cgboiler.com` 及内网 VPC；前提不满足时本文件全部失效"）。零成本，挡掉一类最难 debug 的环境假设故障。符合 monster「内部不可靠→外部锚点托底」元方法论。

**核心架构判断（裁决的真正切入点）**：brief §3 把两个不同的耦合轴混成一个。living-trunk 不变量约束 **trunk↔fork** 关系（剥离物=冻结快照、不回写、不建同步通道）。`PLATFORM-SERVICES.md` 不是剥离物，是主干内部一份文档，它与外部系统的关系是 **主干↔同级依赖系统** 关系——这个耦合一直存在（`§0.3` 现已"一句带过 cg-proxy"）、且不在 living-trunk 不变量管辖域内。所以问题 1 真问题不是"违不违反不变量"（不违反，错配），而是"fork 应用 AI 会拿过时快照写错代码、且读不到主干永不知情"——这才是 living-trunk thread §4「留一行账」要解的 Context Asymmetry，brief 误当成"主干维护负担"，没看到危害落在 fork 侧。修改项 1 的 `verified` 字段 = 把"留一行账"下沉到每条记录粒度。

**行动建议（给父会话）**：方案整体可落地，按上表 4 条修改 + 2 条额外约束补进 brief 再实施。push GitLab 是外部不可逆，按 monster 安全红线逐次 ack（brief §8 两条已识别，属实现层）。

### 核心假设

- living-trunk 不变量的文本边界确实只管 trunk↔fork（thread §3「剥离绝不能做成维护中的包/引擎」「剥离仪式」全在讲剥离物）——已 Read 全文核实，trunk↔同级系统的耦合 thread 未涉及。
- fork 应用 AI 物理上读不到 monster——brief §2 断言，与 cg-platform"fork=独立 GitLab 仓"形态一致，成立。
- cg-proxy / cc-gateway 各自仓有可被 fork 应用 AI 读到的 API 文档——brief §3.2 假设，我未物理核实这些文档是否真存在、是否足够。若不存在，问题 2 的指针策略会指向空目标。

### 可能出错的地方

- 最可能崩在"指针指向的 GitLab 文档实际不存在或不够详细"——brief §3.2 假设 cg-proxy 仓有 API.md，我没核实。若空，PLATFORM-SERVICES.md 的"易变细节指针化"会把 fork 应用 AI 引到死链，比写在文档里更糟。概率中等——建议父会话实施前先核实指针目标真实存在。
- `verified` 字段可能流于形式——AI 维护时机械改日期不真对账。但比 brief 原"只写稳定契约层"（无任何客观判据）强，是改善不是完美解。

### 本次哪里思考得不够

- 没核实 cg-proxy/cc-gateway 仓的 API 文档现状（问题 2 指针落点的物理前提）——这是实现层核查，但它直接决定问题 2 裁决能否落地，本该在 final message 里标成父会话必做的前置核查项。已在行动建议补。
- 未展开 `PLATFORM-SERVICES.md` 的具体节级骨架——brief §4 给了表格结构，我接受了但没逐字审"每条字段：职责/何时用/契约/指针/闭环状态"是否最优，只补了 verified + 缺口区分离。属软层，留实现自决。

### 如果 N 个月后证明决策错了，最可能的根因

最可能：`verified` 字段 + 文件头快照契约都没能阻止 fork 应用 AI 用过时契约写错代码——因为 AI 读文档时不会主动按日期触发"该核实了"的动作，除非有更硬的机制（如 fork 仪式里强制走一遍指针核实）。即根因=把"防 drift"寄望于 AI 的自觉而非流程闸门。若如此，下一步该把"核实 PLATFORM-SERVICES 关键契约"做成 TEMPLATE.md fork 仪式的一个 checklist 步骤。

### 北极星触达

n/a——本次是文档形态/耦合边界的架构裁决，不涉及北极星三条（二阶效应/动态学习/决策超越直觉）的推进。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：grep `memory/essence.md` 关键词 `SSOT` / `coupling` / `drift` / `living-trunk` / `OCCAM` —— 命中精神对位的有：单一漂移源原则（问题 3/4 裁决核心 = "一份文档一个漂移源"）、外化锚点托底（额外点 B 的环境前提断言 = 把隐式假设外化成显式契约，monster B1 元方法论）。未 grep 出字面同 slug 的精确条目，以上为精神对位。
- **本决策是否在某条 essence 上反着走**：无 + 议题性质决定——本次是对"耦合边界/文档同源性"的判断，与 essence 各条无张力。唯一需警惕的是 OCCAM：我给问题 1 加了 3 条修改、额外补 2 条约束，是否过度工程？自审——5 条全是"零成本/低成本的显式化"（加日期字段/加文件头一句话/分区），没有一条是新建机制或新建文档，与 OCCAM 不冲突；问题 4 我还主动接受了"不加独立文档"的减法。无反走。
- **cross-check 用的关键词**：`SSOT` / `coupling` / `drift` / `living-trunk` / `OCCAM` / `anchor`（grep `~/githubProject/gg/memory/essence.md`）。

### essence 候选（可选）

- slug: coupling-axis-misidentification
- 一句话: 一个不变量约束的是某一类耦合关系（如 trunk↔fork）；评判一个新结构是否违反它，先确认该结构产生的耦合在不在那个不变量的管辖轴上——管辖域错配会让"违不违反"变成假问题。
- 是否已 append 到 essence.md: N（候选，等 Keith review 决定是否沉淀——本条是本次裁决最核心的方法论增量）

### 外部锚点

- `~/githubProject/monster/inbox/briefs/cg-platform-template-context.md` ← 被裁方案 brief
- `~/githubProject/monster/threads/cc-space-as-living-trunk.md` ← living-trunk 不变量来源
- `~/githubProject/monster/threads/cg-platform.md` ← cg-platform 主时间线（裁决落地后应留时间线条）

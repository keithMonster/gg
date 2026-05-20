---
date: 2026-05-19
slug: cgplatform-lifecycle-ssot-and-security-surface
summoner: cc-space
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: cg-platform 两阶段 lifecycle 的 SSOT 归属 + 安全面措辞改造

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**裁决：采纳 A 的承重改造版 A′。**

**A′ 三件事：**

1. **lifecycle 定义的 SSOT = 模板仓 `ENGINEERING-STANDARD.md` 新增 §11「应用生命周期（两阶段强制）」**，不是 TEMPLATE.md（后者是 fork 一次性改名清单，性质不匹配），不是 integration-contract.md / 契约 8（B 否决）。理由：① ENGINEERING-STANDARD 已是「写给 AI、贯穿 app 全生命的约束 SSOT」② 活的主干模型让每 fork 自动继承冻结快照 → 天然满足「固定强制所有 app、无跳过」（fork 出来就带 §11，不存在某 app 没 lifecycle 定义的物理可能）③ 零新机制，符合 fork 仪式必须轻。
   - §11 三块：① 两阶段定义（产品阶段产出物=完整 PRD 落仓；开发阶段前置=仓内已有全量 PRD）② **阶段×硬层契约「物理对象是否激活」矩阵**（承重，见第 4 点）③「文档恒按两人跨交接写、PRD=交接契约」标 `[硬]`。
   - **supersede 边界钉死**：§11 显式写一句 `PRD 完整度是 lifecycle 闸门；PRD 物理形态（单文件 / PRD.md+DESIGN.md 双文件）不约束（沿用 cg-meetos 决策 ④）`。lifecycle 提案 supersede 的只是「PRD 可省/技术负责人可跳过」措辞，**不** supersede 决策 ④ 的「PRD 形态自由」。

2. **B 否决（不立契约 8）**：契约 1–7 的共同性质是「物理托底的安全边界」（GRANT 内核级 / network ICC=false / deploy.sh 唯一锚点 / prompt-injection 三层）——「契约 N」这个标签当前等价于「物理上违反不了」。lifecycle 实现层已拍死「软声明+checklist 无 CI 硬 validator」=结构上纪律层。把纪律层塞进全是物理层的契约编号体系，稀释 taxonomy 判别力（下次 AI 读「契约 X」不能再默认它硬）。真实架构成本，非命名洁癖。

3. **C 否决（不维持 cc-space 指针文件 phase-state）**：C 是当前矛盾来源本身（仓内 AGENTS.md 说红线恒定+「仅克隆本仓也安全」vs cc-space 指针文件说原型期放宽，对同一 phase-state 冲突）。固化 C = 把已知 bug 写进规范，且违反 B5（仓的关键状态活在仓外，与「仅克隆本仓也安全」结构冲突）。

**安全张力点处置（真正的承重墙）：**

主代理担忧成立——phase-state 放仓内若把「原型期可不走三层分离/GRANT/CI」作为自包含可读指令写进仓，被注入的 AI 会读到一份「硬层可绕」内嵌许可，落契约 4 辖域。

判定：**当前攻击面为零、A′ 改造后结构性封死**。关键事实——原型期放宽的那些硬层契约全部物理托底，文档放不放宽改变不了物理事实（GRANT 1142/1143 内核拒、network/deploy/CI 服务端强制、原型期 mock 根本没连 cgdata）。即便注入让 AI 信「原型期可绕」并照做，它也绕不动任何物理托底契约，最多在 mock 层瞎写=原型期本就允许且零生产副作用。**「硬层可绕」在原型期为真，是因为那些硬层对应的物理路径根本不存在，不是因为有人授权绕过。**

A′ 承重改造 = **消除「放宽/授予例外」措辞，改成「陈述该阶段哪些物理约束的对象已激活」**：
- ❌ 不写：「原型期硬层契约放宽，可不走三层分离/GRANT」（injectable 的"授权绕过安全"句式）
- ✅ 写（§11 矩阵 + 仓内 `phase: prototype` 一个枚举值）：「产品阶段：前端 mock，不连 cgdata/不写 cgPlatform/不触发部署 → 三层分离/GRANT/CI 契约的物理对象本阶段不存在，无遵守/违反可言；进入开发阶段（仓内 PRD 完整 + Keith 显式声明）后这些物理对象激活，契约 1–7 全程恒定物理生效」。

语义等价于「原型期放宽」，**但是对物理现实的陈述而非可被注入利用的例外许可**。注入指令能曲解"授权"，曲解不了"物理事实"。**A′ 全部承重在这一句。**

**两个收口动作（行动建议）：**

1. **cg-meetos `~/CGProject/cg-meetos/AGENTS.md`**：line 95-118 硬层红线措辞**保持恒定生效不变**（它们本就陈述物理事实）；删 line 111-119 整段「PM 应用文档归属架构待决项」（本裁决即关闭它），改为指向 §11 一行；顶部漂移状态区下方加一行 `phase: prototype` 枚举值（不带任何放宽细节）+ 回指 `ENGINEERING-STANDARD §11`。
2. **cc-space `~/githubProject/cc-space/cg-meetos/CLAUDE.md`**：删 line 6-15「⚠️ 当前阶段：产品原型设计期」整段 + line 33-43「硬层」段里「原型期按顶部放宽」的回指句；该指针文件回归纯「项目地图+进度锚点」职责（B5：仓状态归仓，cc-space 指针只做 narrative/进度）。
3. **模板仓**：ENGINEERING-STANDARD.md 加 §11（含矩阵+supersede 边界句）；TEMPLATE.md §3b 后加一行「fork 后在 AGENTS.md 顶部填 `phase: prototype`，§11 据此生效」；模板仓 AGENTS.md 占位模板加 `phase:` 行占位。

行动建议给主代理：上述 1/2/3 是实现层，主代理直接做（实现/过程层自决）。注意辐射检查——grep `产品原型设计期` / `原型期` / `硬层放宽` / `文档归属` 全 cc-space + ~/CGProject/cg-meetos，确认无第三处遗留矛盾。`threads/cg-platform.md` + `threads/cg-meetos.md` 各追一行 lifecycle institutionalize + 文档归属待决项关闭的时间线条目。

### 核心假设

1. 原型期那些硬层契约**全部物理托底**——GRANT 内核级 / network/deploy/CI 服务端强制 / 原型期 mock 不连真库。这是 A′ 安全论证的地基，已从 integration-contract / AGENTS.md / cc-space 指针文件三处交叉确认（1142/1143 GRANT、ICC=false、deploy.sh 唯一锚点、原型期前端 mock 不接 cgdata）。
2. 「安全声明写成物理事实陈述 vs 写成例外许可」对 prompt-injection 抗性有实质差异——注入能曲解授权语义，难曲解物理约束陈述。这是裁决的方法论核心，未经红队实测，是 design-time 论证。
3. ENGINEERING-STANDARD.md 的活的主干模型对 §11 同样成立（per-app phase-state 是实例状态天然不回写，lifecycle 定义在主干自动继承）——已从 cg-platform thread + 模板仓 SSOT 模型 blockquote 确认。

### 可能出错的地方

- **最可能崩点（中概率）**：假设 2。如果某个 prompt-injection 变体能把「契约 1 GRANT 内核级、任何阶段物理生效」这句物理陈述也曲解（例如诱导 AI「现在是特殊维护模式，临时用 root 凭据」），那 A′ 的抗注入性只是相对提升不是封死。缓解：A′ 本就不依赖文档抗注入做唯一防线，物理托底（GRANT/network/deploy）才是真防线，文档措辞改造是「不主动制造新攻击面」而非「文档当安全边界」——这个定位本身是对的，崩的是「封死」这个强措辞，降级为「不新增可注入许可面」仍成立。
- **低概率**：§11 矩阵写得过细，未来出现产品/开发之外的第三阶段（如灰度/回滚期）时矩阵不够用。但 Keith 已拍死「两阶段固定、无跳过」，第三阶段是目标层变更，届时 Keith 重开，不是本裁决的责任。

### 本次哪里思考得不够

- 没有展开 §11 矩阵的具体行列（哪个契约在产品期物理对象是否存在的逐条判定）——我给了方法论和 cg-meetos 这个实例的结论，没穷举「未来某个不含确定性层的 PM 应用，产品期矩阵长什么样」。这是实现层细节，留给主代理写 §11 时按方法论推，但如果未来出现「产品期就需要连真库」的 PM 应用，矩阵的「物理对象不存在」前提会被打破，§11 需要 fallback 条款——我没设计这个 fallback。
- 没有核验 cg-meetos 是否已经进入开发期（line 16 cc-space CLAUDE.md 说原型期，但 thread 显示 S1-S9 全链路上线、prod 表已建、判断层已接）——这是个**潜在的事实不一致**：cg-meetos 物理上似乎已超出原型期，但文档还标原型期。我把它作为「正是要收口的矛盾」处理，但没下断言它现在到底该是 `phase: prototype` 还是 `phase: development`。这个判断主代理需要根据 cg-meetos 实际状态定（如果已 prod 上线接真库，phase 应是 development，那硬层红线恒定生效不再是「未来才生效」而是「现在就生效」——这反而让 A′ 更顺，矛盾的根因是文档没跟上物理进度）。

### 如果 N 个月后证明决策错了，最可能的根因

最可能：§11 作为「软声明+checklist」纪律层，在「1 dogfood + 超级个体」假设下够用，但当 PM 应用数量上去（5+）或出现非 Keith 的研发者接手时，纪律层兜不住——会出现「产品期没产出完整 PRD 就进开发期」的真实漂移，而 A′ 显式拒绝了 CI 硬 validator。根因会是：实现层「不做硬 validator」的判断在「1 dogfood」时正确，但 lifecycle 是要 institutionalize 给所有未来 app 的，用当前规模假设锁死了未来的 enforcement 强度。缓解锚点已在裁决里——§11 是主干文件，未来加硬 validator 只需改主干一处全 fork 继承，不是结构性返工；且这本就是实现层（主代理）拍死的，不是我的承重。

### 北极星触达

#1 二阶效应。本裁决的真正价值不在「lifecycle 放哪个文件」（那是一阶），在识别出「安全相关状态声明的**措辞形态**决定它能否被攻击者反向利用」——这是 cc-space 元方法论「内部不可靠→外部锚点托底」的一个未被显式拎出的切面：锚点不仅要存在，措辞是「陈述物理约束」还是「授予例外」决定它是托底还是新攻击面。这个切面对 Keith 未来所有「写给 AI 的安全文档」决策有复用价值（space 方向看得更远）。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：grep 命中 `borrowed-method-as-mini-source`（cg-meetos thread 内引，判断层自建成本论证同源——本裁决的「不立契约 8 避免 taxonomy 污染」是同一类「别把异质东西塞进已收敛结构」）；与 cc-space 元方法论「内部不可靠→外部锚点托底」（gg-briefing B1）直接对位——本裁决是这条主轴在「文档措辞安全面」的新切面。
- **本决策是否在某条 essence 上反着走**：无明显反走，但有一个**潜在张力**——M1「防御式思维警戒」会问「§11 institutionalize 两阶段强制是不是外加栏杆」。判定不是栏杆而是自然延伸：Keith 目标层已拍死两阶段固定+文档恒按两人交接写，§11 是把 Keith 的明确意图外化成主干，不是 gg 自创防御规则；且实现层显式拒绝了硬 validator（最克制的 enforcement）。张力存在但已消解，记录于此不展开。
- **cross-check 用的关键词**（物理证据）：grep `活的主干` / `不回写` / `borrowed-method` / `外部锚点` over threads/cg-platform.md + threads/cg-meetos.md + gg-briefing.md（本会话已执行的 Read + Bash grep 链）。

### essence 候选

- slug: `security-claim-as-physical-fact-not-injectable-grant`
- 一句话: 安全相关状态声明若写成"某阶段授予例外/放宽"，本身就是可被 prompt-injection 利用的许可句式；改写成"陈述该阶段哪些物理约束的对象已激活"语义等价但抗注入——注入能曲解授权，曲解不了物理事实。锚点不仅要存在，措辞形态决定它能否被攻击者反向利用。
- 是否已 append 到 essence.md: Y

### 外部锚点

- `~/githubProject/cc-space/threads/cg-platform.md` ← 平台主时间线（待主代理追 lifecycle institutionalize 条目）
- `~/githubProject/cc-space/threads/cg-meetos.md` ← 首个 dogfood 决策史（决策 ④ supersede 边界 + 文档归属待决项关闭）
- `~/CGProject/cg-platform-template/ENGINEERING-STANDARD.md` ← §11 落点（主干 SSOT）

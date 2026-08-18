---
date: 2026-08-18
mode: work
slug: specstory-archive-vs-monster-hygiene
status: substantive-decision
caller: monster 主会话（specstory 会话归档 A vs 公司仓无 monster 字样 B 的架构冲突裁决）
---

# specstory 归档 vs monster 字样：记录层豁免裁决

## 给父会话的最终输出

### 总裁决

**这不是 A vs B 的目标冲突，是 B 的管辖边界从未定义过记录层。** 08-10 Keith 收窄 B（只治源头、存量不动）时实扫过「`.specstory` 24 仓全 0」——那次裁决做出时记录层物理上不存在，B 对它从未表态。今天撞上的不是两个拍板对撞，是一个新出现的层落在了旧裁决的空白区，加上 inbox-desk 把镜子当成了源头。

**边界裁定：B 管产物层（代码 / 文档 / 配置——AI 写作时可控的内容），不管记录层（`.specstory/history/` 会话原文）。** 记录层对「字样类写作规范」整层豁免：

1. **不加 monster 关键词脱敏规则**。忠实性是 A 的承重价值——接手方要的是过程原貌；被关键词涂改的归档，读者无法知道涂了什么，比不涂更误导（把「档案」降格为「宣传稿」）。且关键词拦不住语义层：探测记录换成 `[REDACTED]` 后「存在一个我够不到的平台 SSOT」的语义全在，只会更神秘更诱探究——脱敏买到的是假安全。
2. **不清存量 117 个文件**（Keith 已当场纠正过，此处给架构层理由）：它们是 7 月「死链时代」同事 AI 探测行为的化石。抽查形态分布实证：最高频形态（43+42+37+11×4 条）全是同事的 AI 在找 monster——「本机 monster 仓库路径」「尝试读取 GitLab 平台仓库时返回项目不存在或无权限」「git ls-remote ssh://git@gitlab.cgboiler.com:31022/cg-platform/monster.git」——因为当时仓内产物层文档写着「SSOT 在 monster 侧」×13、「在 monster 的 registry.json 设置 prod_enabled」×12。**会话是镜子加放大器：把产物层一行死链引用放大成几十条探测记录。**
3. **产物层源头已治好（本轮实证）**：cg-sxjianlong-sbox 当前非 specstory 文件 monster 命中 **0**（`git grep -in monster -- ':!*specstory*'` 空），cg-skillhub 0、cgx 1（vite.config.ts）、cg-meetos 1（5 月散文档）。治源头已生效 → 同事 AI 不再被指向 monster → 探测消失 → 镜子新增自然衰减。**对镜子做整容是治下游。**
4. **未来任何字样传感器必须显式豁免 `.specstory/history/`**——否则就是把 inbox-desk 这次误报机制化成天天报红（记录层的字样是源头污染的历史读数，不是新违规；治理读数 = 打碎温度计）。topics.md 那条的挂起条件里应补这句。

### 「monster 字样算不算敏感信息」的正面回答

**不算敏感（secret），算不可达（dead link）。** 实测探测全部被权限拦回（「项目不存在或无权限」），结构 / 路径 / GitLab 地址不构成访问能力；约束也已钉「存在不是秘密」。B 的真正内核应从「字样体面」重写为：**公司仓内的每个指针必须对公司侧读者可达**。「monster 字样」只是死链的粗 proxy——这个 proxy 在产物层近似成立（写作可控），在记录层失效（记录的是行为事实）。08-06 AGENTS.md 裁决的 F1 指针化天然满足新内核：指针指向公司侧可达面（cgx / 平台注入块 / 问 PM），不指 monster。

### 唯一要做的动作（近零成本，掐掉复活回路）

specstory 归档可被同事 AI 按需 grep，历史死链被 grep 命中仍可能再度触发探测。治法不是脱敏，是 design doc 08-15 盘点里**本来就欠着的缺口 5**——`AGENTS.md` marker 段（`upsert_agents_block()`，25 仓一个都没有）。落地时在既定文案「归档目录是历史档案，按需 grep，不默认加载」之后加一句：**「其中的路径 / 仓名 / 指针是历史快照，不代表现状；不可达的私有仓路径不要尝试访问或探测」**。一句话把探测复活回路掐掉，且它本来就在既定 backlog 里，不新增机制。

### Keith 的一个知情点（不建机制）

真正的「monster 内容泄入公司仓」通道只有一条：**Keith 自己在应用仓 cwd 开会话且会话中 Read 了 monster 私仓文件**——内容片段随归档入仓，且不一定含 monster 字样，关键词脱敏本来也拦不住。对策就是 Keith 知道这条通道存在（他的会话他自己判断），建议作为盲区 7 写进 design doc 盲区清单，不建任何机制。

### 明确不做清单

- 不加 monster 脱敏规则（理由见 1）
- 不清 / 不 git rm 存量 specstory 文件（理由见 2）
- 不上针对 specstory 的传感器；未来产物层传感器上线时豁免 `.specstory/history/`（理由见 4）
- 不把 monster GitLab 地址进凭据规则库（地址无访问能力，权限是真闸门；凭据级脱敏照盲区 6 既定路线走，与本案无关）

## 元属性反思

**核心假设**：① 「治好产物层 → 镜子新增衰减」依赖同事 AI 的 monster 引用主要来自仓内文档（形态分布支持，但样本只有 cg-sxjianlong-sbox 一仓；人肉粘贴 Keith 侧材料的通道不随产物层治理衰减）；② 「归档按需 grep 不默认加载」在同事侧真实成立——若某天有人把归档喂进默认上下文，化石死链的复活率会上一个量级，marker 段是唯一防线。

**可能出错的地方**：豁免整层记录层后，若未来出现「真凭据落进 specstory」（盲区 6 的兑现），可能被本裁决的「记录层豁免」措辞误援引成「归档什么都不用管」——豁免的射程是**字样类写作规范**，不是凭据脱敏（后者照旧走 SpecStory redaction 规则库）。

**推理盲区**：只抽查了 cg-sxjianlong-sbox 的形态分布；cg-skillhub 91 个文件的 monster 形态未查（假定同构）。「claude-opus-4-7 · ~/githubProject/monster」×37 的确切来源（状态栏记录 vs 粘贴的 Keith 会话片段）未逐条溯源，不影响裁决方向但影响「人肉粘贴通道」的量级估计。

**根因预判**：下次同类冲突还会以「新层出现在旧裁决空白区」的形态复发（下一个候选：CI 日志 / 监控数据里出现 monster 字样）。判据可复用：这一层是「写作」还是「记录」——写作层套 B，记录层豁免 + 治源头。

**北极星触达**：二阶效应洞察（space）——从「删不删 117 个文件」跳到「B 的管辖边界从未定义记录层」+「字样是死链的 proxy、proxy 在记录层失效」；顺带把 B 的内核从体面重写为可达性。

**essence 对齐自检**：`crystal-vs-log`（过程记录 vs 结晶——相邻轴，佐证「记录忠实发生了什么」是独立价值）✓；`omission-failures-evade-event-driven-sensors`（marker 段缺席 = 该做没做，本轮借裁决把它从盘点缺口提为唯一动作）✓；`tripwire-disarm-needs-relocated-sensor-not-deletion`（inbox-desk 误报的正解不是删传感器，是给它加 `.specstory` 豁免重新瞄准）✓；`mechanical-gate-needs-machine-detectable-target`（「字样」机械可判但在记录层判的是历史读数不是现行为——机械可判 ≠ 目标正确）✓；`hard-rule-welds-intent-to-form-breaks-at-first-legal-deviant`（B 把意图「私仓不可达信息不误导公司侧」焊死在形态「不出现 monster 字样」上，specstory 是第一个合法偏离者——过意图、只违形态，本裁决即拆焊）✓。反向打我的滴：`sensor-exemption-is-a-tag-not-a-lifecycle-value`——豁免 `.specstory/history/` 是给传感器加 exemption tag 而非改生命周期值，形态正确。对齐度：高。

## essence 候选滴（已补审：2026-08-18 auto_gg 夜巡 fresh 证伪审 PASSED-WITH-EDITS，入库 #208）

> **verdict 留痕（含最强反驳点）**：fresh evaluator 原仓独立复核 117/0 成立、既有滴无覆盖（净新增 = 管辖权切割 + 温度计帧）。**最强反驳**：「记录层命中全为 7 月化石」押在 117 处已全部定性上，但占比最大的 transcript 头部行形态（evaluator 数 82×，生成侧记 37，计数不符）与 34× frontmatter 引文从未溯源——若有 transcript 晚于 08-10 治理，「读数 = 纯历史」半边会漏。EDITS 已执行：入库滴前提段收窄「化石」定性为抽查形态、不作全称；谱系补 append-only「篡改快照」(H1) 血缘 + canon.md:205 异轴分工。evaluator tool_use 自报全程只读（Read + grep/git grep/uniq/wc/ls/find，零写副作用），派单者采信自报并核 verdict 文本无写痕。

```
## authoring-rules-do-not-govern-record-layers (2026-08-18) [candidate-unverified]
字样 / 写作类规范只管产物层（写作时可控），不管记录层（会话归档 / transcript / 日志——
行为的忠实化石）。记录层里的违规字样是源头污染的历史读数而非新违规：治理读数 = 打碎温度计；
正解 = 治产物层源头 + 给记录挂「历史快照，不代表现状」标注，错解（脱敏 / 清删 / 传感器直扫）
把档案降格为宣传稿且拦不住语义层。字样传感器进记录层必然误报，须旁标豁免。
【前提：记录层确实不默认加载（按需 grep）；豁免射程限写作规范，凭据脱敏不在内】
物理证据：monster cg-sxjianlong-sbox 案——117 个 specstory 文件含 monster 字样，全为 7 月
死链时代同事 AI 探测行为化石（产物层 08-10 治理后本轮实扫命中 0）；inbox-desk 周跑把化石
报成「新增残留」几乎触发 git rm 拆掉 Keith 08-03 拍板的归档基建。
相关既有滴：crystal-vs-log / hard-rule-welds-intent-to-form-breaks-at-first-legal-deviant /
tripwire-disarm-needs-relocated-sensor-not-deletion / mechanical-gate-needs-machine-detectable-target
```

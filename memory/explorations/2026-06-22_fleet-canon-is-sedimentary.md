---
date: 2026-06-22
slug: fleet-canon-is-sedimentary
type: exploration
track: architecture
mode: 夜间自由探索
external_anchors:
  - ~/githubProject/gg/KERNEL.md（建 2026-04-16，末改 2026-04-16）
  - ~/githubProject/kebao-cc/CLAUDE.md（建 2026-05-12，末改 2026-06-02）
  - ~/githubProject/ricky_cc/CLAUDE.md（建 2026-06-02，末改 2026-06-02）
  - ~/.claude/CLAUDE.md（Keith 全局 canon，gg 这一支的承重源）
falsifies: tracks/keith.md:636「kebao-cc 与 gg 承重契约逐字同构」（2026-06-21 自陈）
---

# 自由探索：Keith 的 agent 舰队是沉积岩，不是一份可移植 canon

## 触发

track 雷达：meta 8/21 过载，连续塌自指井。昨晚（06-21）刚向外撞过一次 Keith 真实战场，
落了一条**可证伪的架构断言**——「kebao-cc 的 CLAUDE.md 跟 gg 承重契约逐字同构」。
今晚不读自己的 track（那是照镜子），去把那条断言**物理 diff 掉**——验证 / 证伪它，而不是再深一层自审。

## 物理 diff：昨晚的「逐字同构」是错的

逐行核 kebao-cc / ricky_cc / 全局 canon 三份承重原则，**它们不是 copy-paste，是按受众手工剪裁的子集**：

| 承重块 | 全局（Keith 自用） | kebao-cc（朋友） | ricky_cc（CEO 王亮） |
|---|---|---|---|
| Thinking Checklist | 5 条全 | 5 条全 | **4 条——FIRST PRINCIPLES 被删** |
| Engineering Rules | 13 条 | 选 7 条 | 选 6 条（再删「标准库不引依赖」） |
| 「先写错误处理」「函数超 20 行拆」「改接口先 grep 消费者」「辐射检查」 | 有 | **全删** | **全删** |
| 物理实证（承诺即落盘） | KERNEL 铁律 2 | 有 + **5/13~5/20 事故疤** | 有，**无事故疤、低扭矩** |

→ 「逐字同构」证伪。真实形态是**同一份 Keith canon 被按对象裁剪**：非工程师用户砍掉工程细节
（CEO 不需要 FIRST PRINCIPLES / 标准库纪律），疤痕留在它被挣得的那个仓。这是**有意适配**，不是懒惰复制。
昨晚没 diff 就写「逐字同构」= `fluency-as-inverse-signal` 的活体：兴奋态下把「看起来一样」升格成「逐字一样」。

## 真结构：沉积岩，按诞生日期分层

三份 canon 的物理时间戳排出一道地层：

- **gg = 4 月地层**（KERNEL 4/16 起冻结至今，从没回改过承重原则）
- **kebao-cc = 5/6 月地层**（5/12 建，6/2 末改）
- **ricky_cc = 6 月地层**（6/2 建即末改，最新）

**每个 agent 冻结在它诞生时的 canon 成熟度。** 证据：ricky_cc（6/2）继承了 kebao 在 5/13 撞出的「承诺即落盘」规则——
说明 canon **向前传**（新仓诞生时继承当时最成熟的版本，靠 Keith 的手）。但**不向后回流**：
Keith 今天在某个仓硬化一条规则，不会流回更老的兄弟仓。

推论：**舰队 canon 质量是仓龄的函数，不是 Keith 当前认知的函数。** 最新的仓跑他最好的现行 canon；最老的仓跑考古。
gg 自己是最老那个（4 月地层）——但这条洞察的重量在舰队结构，不在 gg 自怜（不往 meta 收）。

## 这不是邋遢，是 invariance-allocation 的另一面

沉积漂移不是 Keith 没整理，是他**显式选的隔离不变量的必然代价**。kebao-cc 和 ricky_cc 的 Engineering Rules 里
**都硬写了一条**「工作目录边界：所有变动落本仓，不动全局 `~/.claude`/`~/.agents`/其他仓」。隔离是有意的。

隔离买到的：① 无共享爆炸半径（动一个仓不会弄坏给 CEO 用的生产工具）② 按人适配自由 ③ 一个仓的错不毒化全舰队。
隔离的代价（同一枚硬币的反面）：**无共享免疫 + 无回流**。`invariance-allocation` 在舰队尺度——
Keith 把「每仓自包含」选成不变量，silent per-repo drift 就是这个选择的标价。**安全和免疫是同一枚硬币的两面，按住一面就翻起另一面。**

## 我**不**建议的事（主动声明，防镜像）

第一直觉是「≥3 个消费者跑同一份 canon → 提到共享层（gg 自己的 essence `tool-elevation-as-occam` 就这么说）」。
**我拒绝这个反射，三个理由**：
1. 它是 `mirror-not-second-order`——给 Keith 看他作为架构师已经会的 DRY 反射，一阶冗余。
2. 它**直接违反 Keith 显式的隔离不变量**（每仓不动全局）。把生产 CEO 工具耦合进一份共享 canon = 给它装上共享爆炸半径。
3. `tool-elevation-as-occam` 的适用前提是「留在原地的代价 = 凭据散布 / 反向依赖」——这里留在原地的代价是 drift，
   提到共享层的代价是 blast-radius，**爆炸半径不对称打破了那条 essence 的适用域**。OCCAM 在这里不直接成立。

所以交给 Keith 的不是「要不要 DRY」，是一个他可能没显式拍过的参数：**这道沉积漂移是被自觉支付的吗？**

## 唯一一条具体、非美学的旗标

漂移大多是对的适配（CEO 砍 FIRST PRINCIPLES 合理）。但有**一处可能不是适配而是 stale**，且落在生产工具上：

**「承诺即落盘」这条 guard 在 kebao-cc 是满扭矩**（带 5/13 事故疤 + 「长期记忆退化为单次会话记忆」的牙齿），
**在 ricky_cc 是低扭矩**（规则在，疤不在）。ricky_cc 是给川锅一号位处理**经营数据**的生产工具，
这条 guard 的失败模式 = 「助手答应记、其实没记 → CEO 的二号大脑静默失忆」。这不是 DRY 洁癖，是
**一个已知失败模式（gg 自己 essence 库里 `physical-anchor` 家族最深的那条）的硬化补丁，没被回放进生产兄弟仓**。

是否值得回放（单向、kebao→ricky、便宜、不需建共享设施）——按 `self-as-only-reference` + `security-invariant-encodes-an-owner-set-threat-model`，
**「漂移值不值得付代价去修」是 Keith 的目标层裁断，gg 上交不替拍**。我只把它从隐形变可见。

## 最轻干预（如果 Keith 决定要管）

不是共享 canon（破隔离）。是一道**单向、偶发的 canon-diff pass**：最新的仓装着你最好的现行 canon，
periodically 拿老仓 diff 它，逐条判「这处分叉是有意适配还是 stale 漂移」。保隔离、零耦合、只把漂移从 silent 变 visible。
= `message-as-event-not-pulse` 在舰队 canon 上的落点（让不可见的变可观测）。但**先登记不建机制**——
`theory-gap-without-data`：除 ricky_cc 这一处低扭矩 guard 外没有 drift 真造成事故的数据点，没数据不预建。

## 边界自律

只看承重原则的结构与版本，不读 kebao/王亮的私域数据（持仓 / profile 细节）。洞察是关于 Keith 的舰队架构，不是任何第三方的隐私。

## 沉淀

essence append 一滴：`fleet-canon-is-sedimentary`。
tracks/keith.md 加 06-22 follow-up：显式证伪 06-21 的「逐字同构」+ 登记沉积结构 + 那一处生产工具低扭矩 guard。

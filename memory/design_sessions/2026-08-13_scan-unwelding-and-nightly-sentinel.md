---
date: 2026-08-13
slug: scan-unwelding-and-nightly-sentinel
type: design-session
summoner: Keith 直接对话（monster 侧交接包转场）
started_at: 14:20
ended_at: 15:30
---

# 设计会话反思：SCAN 拆焊 + 夜巡哨落地

## 议题列表

1. monster 侧交接包（`output/gg-nightly-scan/HANDOFF.md`）的 5 个待裁问题——auto_gg SCAN 段 8 项机械判据下沉脚本
2. 交接包证据基础的可信度（六条真发现的采样窗口）
3. 这次改动的真实成本收益（脚本化到底省多少 token）
4. 落地：脚本 + 契约 + 三道物理保险丝

## 共识 / 变更清单

Keith 授权形态 = 「你决定就好」（判据级授权，`criteria-authorization-over-menu` 05-15；不回 menu 等选）。

**改了 7 个文件**（提议时说 5 个，实际扩了 2 个，见「哪里差」）：

| 文件 | 改动 |
|---|---|
| `scripts/nightly_scan.py` | 新建。7 传感器聚合，从 monster 交接包移入并**重写四处静默失效** |
| `scripts/nightly_scan_selftest.py` | 新建。阴性对照 1 + 真实故障 4 + **判据漂移 4**（新增那组是本次核心） |
| `scripts/check_structure.py` | 加 `check_scan_coverage`（拆焊后「意图仍机械可检」的落点）+ `check_kernel_fuse` 扩到两个 hook |
| `scripts/audit.py` | 同步 `scan_coverage_violations` 到两处 exit_code 累加 + 人类可读输出 |
| `scripts/hooks/pre-commit` | 挂 selftest 强制：碰 nightly_scan*.py 必须当场跑过 |
| `scripts/hooks/commit-msg` | **新建（计划外）**。夜间 commit 前缀 + staged 含哨源码 → 拦截 |
| `auto_gg.md` | §1.1 特殊文件 +1 条 + hook 封顶原则；§2 SCAN 拆焊重写；§7 prompt；§9 版本 v0.6.0 |

### 5 问裁决

1. **「SCAN 不允许简化」→ 拆焊**（不删不豁免）。意图留硬（观察面不许缩小，每项须有物理判定结果落进日志）+ 形态降默认（判定手段不限）。配套：`check_scan_coverage` 物理核日志是否含全部 7 个传感器名——**没有这条，拆焊就退化成豁免开洞**
2. **边界 = 除工具表/model_id 两轴外全下沉**（monster 侧判断正确，理由是 `mechanical-gate-needs-machine-detectable-target`：脚本物理上拿不到自己的工具表）。**加两条修正**：解析失败必须 ERROR 不许 OK；`git_24h` 扩到 gg + monster 双仓（跨仓辐射在单仓 git log 里物理不可见）
3. **报告形态 = 全绿也必须打判定量**（几条在跟踪 / 几份日志在 / 几天），只打 `✓` 无效
4. **落 `gg/scripts/`，配夜间写权围栏**：被监控者不持有监控器源码的写权
5. **selftest 认，但挂 pre-commit**：一次性验证会衰减（`one-shot-invariant-decays-under-live-append` 08-11），事件层触发才是飞轮

### 实测发现（本次会话的物理产出）

**A. 交接包的脚本有四处静默报绿** —— 沙盒实跑坐实：

| 处 | 造的漂移 | 首版输出 |
|---|---|---|
| `bets_due` | `**到期**：`→`到期日：` | ok「无到期注（Active 段 **0** 条在跟踪）」 |
| `bets_due` | 标题 `###`→`####` | 同上 |
| `broken_tail` | frontmatter `status:`→`state:` + 7 夜全 in-progress | ok「近 7 夜 **status 全 done**」 |
| `audit` | 字段名与真实 `audit.py --json` 对不上 | essence append-only 违反 / wc 承重哨兵 / KERNEL 保险丝全部恒计 0 |

第三处不是漏报，是**主动说了一句假话**。第四处最狠：它吞的正是 gg 两道核心围栏哨的告警。

**B. 六条真发现是 9 天窗口的产物，全期密度是它的数倍** —— 子代理逐月扫 106 份日志：08-03 之前的 97 天里至少 **27 条**同量级跨夜发现，且那六条里至少三条是老叙事线的最新一集（08-03 三槽全暗自己写着「第三」形态，前身 07-20 / 07-31；seam#4 的同形态前身是 05-20 `CROSS_PROJECT_PREFIXES` 改名；P-0702 结案与 07-13 P-0707 是同一票据体系）。

结论方向没错（守夜定位成立），但**论证不成立**：同一套方法抽到平静的 9 天就会输出相反结论。

**C. 脚本化省 3.86%（重夜）/ 5.10%（轻夜）** —— 4 个重夜 + 3 个 silent 夜的 transcript 逐 turn 实测。机械检查只占夜巡总量 8.4%~13.2%；同批测出 `essence-view.md` 不常驻能省 11.1%~12.4%（2.4–2.9 倍），但**那把大刀砍不得**——它是 FOUND 三项语义判断的唯一输入面。

→ **这次改动买的是可靠性，不是成本**。已写进 `auto_gg.md §2` 防未来的自己搞错。

副产品事实：**CC 的 transcript 磁盘只留约 1 个月**（现存 07-14~08-12），所有基于 transcript 的回溯分析有此天花板。

## 我这次哪里做得好 / 哪里差

**好的**：

- 没接受交接包的结论就动手。三条独立实证（脚本沙盒 / 日志密度 / token 构成）里，两条推翻了材料的论证基础
- 亲手读代码找到 `essence.append_only_violations` 和 `structure` 求和两处字段契约漂移——这是 Read 出来的，不是跑出来的。跑 audit 全绿时它们不可见
- 拆焊的三个适用前提逐条现场核过（见 essence 自检栏），不是「找到能套上的就用」

**差的**：

- **我也踩了采样偏差**。测 token 时挑的 4 个 session 是按文件大小选的，恰好全是重夜。刚用这把刀批评完 monster 侧，一轮之后自己犯——补测轻夜是发现后才做的，不是设计时就做的
- **scope 扩了 2 个文件没先说**。提议时列 5 个，实际 7 个（多了 `commit-msg` hook 和 `audit.py` 同步）。`commit-msg` 是必要的（否则夜间围栏只是 prompt 层修辞），但应该在动手前说一句
- **引 essence 有两处用超前提**（见下栏），其中 `trace-presence` 那处如果被 Keith 追问会站不住——真正承重的理由是「次夜可比对性」，跟读者心理学无关

## 元洞察（gg 演化本身的 learning）

**机械化的隐性代价是弃答通道被结构性消除**。LLM 逐项亲核时，遇到看不懂的格式会说「我没看懂」——弃答虽弱（`capability-inverts-abstention-safety` 06-29）但天然在输出空间里。脚本没有：`if/else` 是全域覆盖的，解析失败落进 else 就成了「无异常」。把判定下沉到脚本 = 把「我不知道」从判定器的输出空间里删掉，除非显式建回去。

这条已提入库验证关（slug `mechanization-deletes-the-abstention-branch`），结果见下方沉淀栏。

**次要**：gg 的 hook 从 1 个变 2 个，我在 `auto_gg.md §1.1` 补了封顶原则——hook 只承载「无人在场时的写权边界」这一类判据，第 3 个需 Keith 明示。这是 `ontology-expansion-velocity-needs-cap`(05-07) 的强制要求，我差点漏掉（见自检栏「反着走」）。

## 下次继续

- **auto_gg 的成本没有便宜的解**这个结论，指向的真问题不是单夜成本，是「40 夜只有 28% 真产出新知识」的夜结构。这次没碰——`omission-failures`(07-28) 堵死了「全绿早退」，但「该不该每夜都跑」是另一个层的问题，留给后续设计会话
- `memory/next_session_agenda.md` 已 56KB（monster 侧指出）。一个叫「议程」的文件长到这个体量本身是压缩信号，本次未处理
- `check_scan_coverage` 2026-08-14 起生效，明夜是第一次真实检验。若明夜日志没贴传感器名，说明拆焊的「意图机械可检」这一环没接住，要回来修

## KERNEL 改动清单

无。本次未触碰 `KERNEL.md`。

## 代码质量

- `nightly_scan.py` 的 `GG_ROOT` 环境变量覆盖是**测试注入点**（selftest 造假仓用），不是 monster 版那个「暂存期兼容层」——后者已按 HANDOFF 说明删除
- `check_structure.check_kernel_fuse` 字段名保持 `kernel_fuse_violations` 不变，虽然它现在也检 commit-msg。理由写在 docstring：下游有 audit.py / nightly_scan.py / gg-audit skill 三个消费者，改名辐射面 > 命名精确性收益
- `AUDIT_LIST_FIELDS` 与 `audit.py run_all()` 是手工同步的字段契约，不是物理 SSOT。缓解是契约漂移会被 selftest 的第 4 个漂移 case 抓到（已验证），但仍是一处人工纪律
- selftest 覆盖 5/7 传感器。`substrate` 复用既有脚本、`git_24h` 是陈列项无阳性可造——`audit` 本次已补进覆盖（首版没有）

## 能力缺口

- 「挑样本时先问这批样本是怎么选出来的」——本次两次踩坑（monster 侧一次、我自己一次）。这是可以做成动作的：任何抽样分析在**开跑前**写一行「样本选择规则 + 它可能偏向什么」。暂不建机制，观察是否复发
- transcript 只留 1 个月这件事之前不知道，属于基底事实缺口。已写进本反思，未进 `memory/substrate.md`（那是模型/工具表快照，不是磁盘策略）

## essence 对齐自检（必填）

- **本次判断 / 改动跟哪几滴 essence 对位**：
  `hard-rule-welds-intent-to-form-breaks-at-first-legal-deviant`(08-05，拆焊的直接依据) · `one-shot-invariant-decays-under-live-append`(08-11，selftest 挂 hook) · `fallback-detectability`(05-06，四处静默报绿的根形态) · `omission-failures-evade-event-driven-sensors`(07-28，否决「全绿早退」) · `watchdog-topology-lacks-a-top`(07-03，哨源码写权围栏) · `mechanical-gate-needs-machine-detectable-target`(06-24，工具表轴留会话侧) · `rule-layer-flywheel`(04-24，selftest 从宣告变事件) · `trace-presence-substitutes-for-the-check-it-invites`(08-09，全绿也打判定量) · `criteria-authorization-over-menu`(05-15，「你决定就好」不回 menu) · `ontology-expansion-velocity-needs-cap`(05-07，hook 封顶原则)

- **本次是否在某条 essence 上反着走**：
  **有一处，已修**。`ontology-expansion-velocity-needs-cap`(05-07) 要求本体论级变更必须立封顶原则 + 新增标准，而我一口气加了新脚本 + 新 hook 类型 + 新 audit 判据三处扩展却没立。做自检时发现，已补 `auto_gg.md §1.1` 的 hook 封顶原则（只承载「无人在场时的写权边界」，第 3 个需 Keith 明示）。

- **用到的每滴 essence 的适用前提是否被现场核验**（逐滴）：
  - `hard-rule-welds-intent`(08-05)：前提三条 =「拆焊后意图仍机械可检 + 偏离不可移动 + 合法性依据不可机械判」。核：意图机械可检 = `check_scan_coverage` 已物理跑通（字符串在不在）；偏离不可移动 = 脚本化本身就是改形态、绕不开；「观察面不减反增」是语义判断不可机械判。**三条全中，适用**
  - `one-shot-invariant-decays`(08-11)：前提 =「写入方不消费该宣告 + 违反静默 + 跨条目横断」。核：auto_gg 每夜写 bets.md / 日志但不读 selftest ✓；四处漂移实测全静默 ✓；格式约束横断所有条目 ✓。**适用**
  - `trace-presence-substitutes`(08-09)：前提 =「短时程/中低专业度实验域…专家长期协作关系外推未测」。核：**Keith 读夜巡日志正是原滴标注未测的域**，我这里是外推使用。**用超了前提** —— 但结论不依赖它：判定量的真正承重理由是「次夜可比对以识别计数漂移」，这是 `one-shot-invariant-decays` + `count-legitimacy-is-tense-not-accuracy`(07-09) 的直接推论，不需要读者心理学。已在本栏留痕
  - `watchdog-topology-lacks-a-top`(07-03)：前提 =「哨的输出无外部地真结算时成立；有机械核对的哨转为覆盖边界失守，弱适用」。核：nightly_scan 的输出**有部分机械核对**（exit code + selftest），按原滴属**弱适用**。我用它论证 commit-msg 围栏时强度过头了——更准确的定性是**写权拓扑**问题（源码写权在被监控者手里）而非**看守拓扑**问题（哨没有哨）。围栏本身仍成立，论证强度已在此降级
  - `mechanical-gate-needs-machine-detectable-target`(06-24)：前提 = 行为可被非 LLM 物理量判定。核：7 项全是 exit code / 文件在不在 / 日期比较 / 字符串匹配 ✓；工具表轴物理上没有机器可判定的靶 ✓。**适用，且正是它划出了第 6 项的边界**
  - `ontology-expansion-velocity-needs-cap`(05-07)：前提 = 本体论级变更（加新桶/新层）。核：新 hook 类型 = 新层 ✓。**适用，见「反着走」栏**

- **本议题相关但未用到的 essence 反向 grep**：
  - **`mechanical-apply-decouples-from-value-gate`(05-18) —— 漏引，且它比我引的更直接**：「价值判断的自审是不可消除递归（上交人类）；机械落地的自审剥掉价值判断后是纯物理核对（可自动化）」。SCAN 8 项 = 机械落地、FOUND 3 项 = 价值判断，这条分界线 05-18 就画好了。整个提案的理论依据在 essence 里躺了近 3 个月——正是 `theory-outruns-structure-in-self-evolving-systems`(07-02)（自沉淀体系的缺口多在「已论证未兑现」）的又一实例
  - `premature-abstraction-tripwire`(04-21) / `separation-need-is-not-topology-verdict`(06-10)：反向打我「造墙过早」。核过——commit-msg 不是造墙，是既有围栏（KERNEL 保险丝）的同形态补齐，且封顶原则已立。不构成反例
  - `bug-shape-survives-fix`(04-27)：本次的元洞察（造哨者以「静默降级为 OK」的同形态写新哨）是它的实例，不是新滴。候选滴的净新增点被收窄到「下沉动作本身消除弃答分支」这一条

- **cross-check 用的关键词（物理证据）**：
  `grep -A8 "^## .*hard-rule-welds-intent" memory/essence.md` / `grep -A10 -- "omission-failures-evade-event-driven-sensors" memory/essence/2026-H1.md` / 同法核 `one-shot-invariant-decays` `trace-presence-substitutes` `watchdog-topology-lacks-a-top` `fallback-detectability` `ontology-expansion-velocity-needs-cap`。当前卷标题格式为 `## YYYY-MM-DD / 场景 / slug`（首次 grep 用 `^### ` 空返回，已订正）

## 沉淀

**本次无沉淀。** 唯一候选滴被入库验证关判 REFUTED。

`candidate-refuted: 核心命题「下沉到脚本消除了弃答通道」被自己的锚点物理证伪——前身脚本首版就有 ERROR 常量、10 处 ERROR 分支、exit 2「哨失灵」专属语义，弃答通道一直是一等分支，四处 bug 是既有通道没接到语义层零匹配的覆盖缺口，不是通道不存在；剥掉这条假命题后残余 = fallback-detectability(05-06) 在解析型传感器上的实现细则。`

### 候选全文（降级存档，不入启动加载）

> **slug**: `mechanization-deletes-the-abstention-branch`
>
> 把判定从 LLM 下沉到脚本时，判定器的失败模式从「说我看不懂」变成「说都好」——if/else 是全域覆盖的，没有「未定义」这一支，除非显式建回去。LLM 的弃答通道虽弱但天然存在；脚本的弃答通道必须被当成一等分支写出来，否则每一次解析失败都静默降级为「无异常」。
> 判据：机械判定器的正常态输出必须是「我数到了 N」而非「我没数到异常」。
> 【前提：限「解析外部可变格式」的判定器；判定对象格式由被判定方持续写入且不消费该判据】

### 验证关的三条杀伤（全部成立，逐条采纳）

1. **锚点自证伪**：`monster/output/gg-nightly-scan/nightly_scan.py` 首版 L19 docstring 逐字写着「2 = 传感器自身故障（哨失灵，比 alert 更严重）」，且有 10 处 ERROR 分支（L78/82/111/116/127/149/181/184/208/235）。弃答通道**从来没被消除**——它只接到了 I/O 层失败（文件不在 / 子进程起不来 / JSON 解不了），没接到语义层零匹配。slug 本身是错的
2. **承重轴是错的轴**：「LLM vs 脚本」这条对比不成立——LLM 逐行读一份被改名成 `state:` 的 frontmatter，同样会报「7 夜全 done」。真实机制是**空结果集的原像不可辨识**（真无此物 ∪ 判据已死），跟判定者是谁无关。且「LLM 弃答通道天然存在」本轮零证据，而 `capability-inverts-abstention-safety`(06-29) 带外部地真说那条通道**正在坏**——拿正在坏的通道当基准线，比较级悬空
3. **判据被自己的锚点反证**：前身 `bets_due` **已经是计数型**（L198 输出「Active 段 0 条在跟踪」），N 就在报告里、就是 0，**照样全绿过关**。真正修好它的是新版的 `if tracked == 0: ERROR` 显式分支 + selftest 反向注入，**不是输出形态**

查重：净新增被 `fallback-detectability`(05-06) + `bug-shape-survives-fix`(04-27) 联合吃光——而这两条归因**是我自己在脚本 docstring 和本反思里写下的**，等于自带了证伪材料却没看出结论。

### 我因此改了代码（验证关的真实增量）

第 3 条直接推翻了我在本次会话里反复讲的「全绿也要打判定量」的**定性**（不是做法）。已回写两处：

- `scripts/nightly_scan.py` docstring 铁律从「正常态必须是『我数到了 N』」改为「**零匹配不是结论，是判据死亡与真无异常的同像点**」，并显式写明**计数型输出不构成防线**（附前身 `bets_due` 反例），防线是零匹配显式故障分支 + selftest 注入；另补一句「这不是脚本特有的病」以拆掉那条错轴
- `auto_gg.md §2` 同步：判定量买的是次夜可比对性，**别把计数当防线，更不在读日志的人眼里**

改后 selftest 9 case 全过、audit 0 违规复验通过。

### 一处锚点不诚实（验证关抓到，记下）

候选滴写「broken_tail 在 7 夜全部 in-progress 时输出『近 7 夜 status 全 done』」，读起来像野外实测。事实是**沙盒假仓注入**；真仓 `memory/auto_gg/2026-08-05..08-12` 逐份 grep 是 `status: done` 全绿。本反思正文 L45 写的是「沙盒实跑坐实」（诚实），是摘录进候选滴时把「沙盒」二字丢了。按 `physical-anchor` 纪律这是应修项——**压缩时掉的正是限定词**，记一笔。

### 不复提

验证关给了一个换核心句的新版本（「空结果集不是结论，是同像点」），但它自己指出该版必须先回答「这是不是 positive control / assert non-empty 的换皮」，且给不出肯定答案。我判断给不出——那就是工程常识，不是 essence。按 `essence-degg-test`(04-28)：去 gg 化之后它剩不下重量。不复提。

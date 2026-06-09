---
date: 2026-06-09
slug: nw-deprecate-radar-4week-review
summoner: monster
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: NW 退役雷达 4 周回审裁决（推翻自己 5-15 设的真拆比例阈值表）

### 给父会话的最终输出（必填）

本次是回审我 5-15 亲手设的 4 周 tripwire。三问逐裁：

**问题 1（essence 是否站住）：部分站住，必须精化后才沉淀。**
- 站住的一半：对**需要价值判断**的退役信号（stale thread / CLAUDE.md 超阈），"识别但不判定、决策权留垂直通道"4 周没引爆 pending 堵塞、没诱发 Keith 反射清扫（我 5-15 估 30% 的"当 todo 用"风险没发生）。
- 漏掉的一半：链路默认假设"每个垂直通道都有活的消费者"。`product-design-prelude` 孤儿 notes 是铁证——零价值判断（skill 本体已删、notes 残留、成本 5 秒），但 skill-auditor 不自动扫孤儿 notes → 晨报点名两次、4 周无人接。对**不需要判断的确定项**，"不判定"退化成 `fermentation-without-detector` 的实体化（无检测器消费 = 每读取时点 0 进度）。
- 判词：原 essence 边界条件缺失——`signal-without-judgment` 成立的前提是被识别信号真需要价值判断；零价值判断的确定项必须有活的自动消费端，否则聚合视图 = 发酵桶。

**问题 2（真拆比例是不是错标尺）：是，我 5-15 设错了，本轮明确推翻自己。**（`precondition-recheck-overturns-prior-verdict` 活体——主动覆盖不辩护。）
- 错因：metric 隐含"点名=删除候选"，但四类信号里 thread stale / CLAUDE.md 超阈本质不对应"删"——thread 沉睡=健康态、超阈对应瘦身且 context-curation 已管。分母错了。`metric-is-a-claim-not-a-fact` 又一实例：把"点名应导致拆"这个主张伪装成客观判据。
- 机械规则按字面读 → "收紧阈值"，但这是用错尺读出的错结论。正确动作不是收紧、不是维持、不是升级 A——是**废掉这把尺**，换评价维度从"删除吞吐"到"信号有没有活的消费端"。5-15 那张 <20%/20-60%/>60% 阈值表整体作废。

**问题 3（去留改造）：③ 认，④ 认但加边界。**
- ③ 降级合并：认。简报里"退役雷达"段和"结构卫生议题"段已事实并存、功能重叠（Phase 4/closed 复发/inbox 陈旧两段都扫）= 我 5-15 最怕的"语义重叠扫描器"已长在监督盲区。合并成「结构卫生参考视图」、弃真拆比例 KPI。**硬约束：段首"参考性,不强制动作+探索豁免+stale≠该拆"必须保留**——4 周没诱发反射清扫的真功臣。
- ④ 廉价确定项自动清：认，但**孤儿删除不满足现 nw-auto-apply 白名单第 2 条"纯 append/不含删除"**，不能直接塞。推荐 **(b) 起步**：把确定项（本体已不存在的残留指针）渲染成可一键复制的 `rm` 命令进简报，**不自动扣删除扳机**；4 周后看是否升 **(a)** 白名单极窄删除子类。理由：删除不可逆（macOS rm 不进废纸篓+monster 安全红线），且"本体已删"判定可能假阳性（`claude_d_reference_check.py` 误报 coding-subagent 孤儿是活例）。按 `reversibility-not-permission`——不可逆动作即便确定也先不自动扣扳机。

**行动建议（父会话执行，执行权在你）：**
1. 合并退役雷达段→结构卫生参考视图段（保留段首防反射清扫约束），弃真拆比例 KPI，改 `nw-daily.md` Step 4.7 + Step 5.3 模板
2. ④ 用 (b) 半自动：孤儿/残留确定项渲染成可一键复制 `rm` 命令，不自动删；回审锚点 2026-07-09 看升 (a)
3. `night-watch.md` append 本次回审裁决时间线（阈值表作废+雷达降级合并+④半自动边界+锚点 7-09）

**trade-off / 未核验假设：**
- (b) 半自动仍需 Keith 一次粘贴，没完全消除人类闸门——这是故意的（删除不可逆换确定性不够）。
- 未核实：`product-design-prelude` 孤儿"本体已删"我没物理 grep 全仓核（信父会话的二手描述）——落地 ④ 时父会话需对每个候选删除项物理核存在性，不能信雷达单点判定。
- 合并后是否真消除重叠取决于落地实现——若只是把两段标题改一个但仍跑两套扫描逻辑，重叠没消，只是隐藏。

### 核心假设
- 雷达 4 周的真价值是注意力聚焦（把分布 4 通道的结构信号聚合成每日可扫面），不是删除吞吐——这个重定位成立的前提是 Keith 确实每天扫这一段并从中获得"哪些结构信号在累积"的认知，而非把它当噪音跳过。本轮没物理核 Keith 实际阅读行为，是推断。
- "孤儿 notes 4 周无人接"=消费端缺位的证据，而非"Keith 看到了但判断不值得清"的主动忽略——若是后者，④ 是过度自动化。倾向前者（成本 5 秒+晨报明标"随手 rm 即可"，主动忽略不合理）。

### 可能出错的地方
- 最大风险（概率 25%）：④ (b) 的"可一键复制 rm 命令"仍被 Keith 跳过——半自动没解决根因，根因是 Keith 注意力不在结构卫生上。若 4 周后孤儿照样堆，说明不是"消费端缺自动化"是"消费端缺意愿"，那 ④ 整个方向错，该砍掉孤儿扫描而非升 (a)。
- 次风险：合并 ③ 时把段首防反射清扫约束当冗余删掉 → 复活我 5-15 最担心的反射清扫风险。已在行动建议里显式钉死"必须保留"。

### 本次哪里思考得不够
- 没物理核 `product-design-prelude` 孤儿是否真"本体已删"——整个 ④ 裁决建立在父会话二手描述上，若该 skill 其实还在用（grep 没搜全），④ 就是在自动清不该清的东西，反而制造事故。已在 trade-off 标"落地需父会话物理核"，但我自己本可以在裁决时就 grep 一次的，省了。
- 没核简报"结构卫生议题"段的完整来源——我从父会话给的 morning-brief.md 看到两段并存就判"功能重叠"，但没读 nw-daily.md prompt 确认两段是不是真跑两套独立扫描逻辑（也可能是同一次扫描的两种渲染）。"重叠"判定有推断成分。

### 如果 N 个月后证明决策错了，最可能的根因
最可能：**④ (b) 半自动也没人消费，证明问题从来不是"缺自动化消费端"而是"Keith 注意力根本不分配给结构卫生"**——那 ③+④ 整个都是在给一个 Keith 不关心的视图做精致化，正确动作本该是问 Keith"你要不要这个视图"而不是改造它。根因：我接受了"退役雷达应该存在、只是要改造"这个父会话框定的前提，没回退一步质疑"Keith 是否真需要任何形式的退役/卫生聚合视图"。本轮我裁了改造方向，没裁存废本身——若 Keith 其实想要的是直接砍掉整段，我的 ③+④ 是在错误前提上的精修。

### 北极星触达
**#1 二阶效应**：4 周前我担心的二阶问题（治理机制扩张冲动会膨胀承担本不属于它的判断责任）没发生，但暴露了我没预见的另一个二阶问题——**聚合视图会在自己监督盲区长出语义重叠的孪生段**（退役雷达 vs 结构卫生议题）。看得更远的产出是：聚合视图的风险不止"越权判断"（5-15 我防的），还有"自我增殖出重叠扫描器"——治理机制的熵增不只向上（越权）也向旁（增殖）。

### essence 对齐自检（必填）
- **本决策跟哪几滴 essence 对位**：
  - `signal-without-judgment-as-aggregate-view`（5-15 候选，本轮精化推翻一半）——核心被审对象
  - `metric-is-a-claim-not-a-fact`（5-18）——真拆比例是伪装成判据的主张，本轮活体
  - `precondition-recheck-overturns-prior-verdict`（5-19）——推翻自己 5-15 阈值表的元动作
  - `mechanical-apply-decouples-from-value-gate`（5-18）——④ 按"需不需价值判断"分流的依据
  - `fermentation-without-detector`（5-15）——孤儿 notes 无消费端 = 发酵桶，本轮实体化
  - `reversibility-not-permission`（5-06）——④ 删除不可逆即便确定也先不自动扣扳机
  - `vantage-contaminates-verdict`（5-19）——警惕我作为"审自己旧决策"的位置偏向辩护旧裁决；本轮主动推翻对冲它
- **本决策是否在某条 essence 上反着走**：潜在张力，未展开——`tool-elevation-as-occam`（5-06）说第二消费者出现该上提工具，④ 的"孤儿清理"理论上是个新消费动作，按它该上提成自动化能力；但我裁了 (b) 半自动不上提到全自动，理由是删除不可逆（`reversibility-not-permission` 压过 OCCAM）。这是两条 essence 的张力，我选了可逆性优先，4 周后 (b) 证明确定性够再升 (a)。
- **cross-check 用的关键词**：grep "signal-without-judgment" / "metric-is-a-claim" / "precondition-recheck" / "mechanical-apply" / "fermentation" / "reversibility" / "vantage" / "tool-elevation"（启动时 Read essence.md 全文已加载，记忆中检索 + 物理 grep 验证 slug 存在）

### essence 候选
- slug: `signal-without-judgment-needs-live-consumer`
- 一句话: 聚合视图"识别但不判定"成立的前提是被识别信号真需要价值判断——对零价值判断的确定项,"留给垂直通道"等于扔进无检测器的发酵桶；先按"需不需价值判断"分流,需要的走聚合视图不判定,不需要的必须有活的自动消费端。用"催成几次动作"考核声明不判定的视图是范畴错误,视图价值是注意力聚焦不是删除吞吐。
- 是否已 append 到 essence.md: Y
- 备注: 原候选 `signal-without-judgment-as-aggregate-view` 不直接转正——4 周数据证明它只捕获对的一半,漏了"需不需判断"前置分流。新滴是它叠加 `mechanical-apply-decouples-from-value-gate` + `fermentation-without-detector` 的合并精化。

### 外部锚点
- `/Users/xuke/githubProject/monster/harness-engineering/prompts/nw-daily.md` ← Step 4.7/5.3 改造落地点
- `/Users/xuke/githubProject/monster/threads/night-watch.md` ← 回审裁决时间线 append 目标
- `/Users/xuke/githubProject/monster/harness-engineering/CLAUDE.md` ← nw-auto-apply 白名单契约（④ 若升 (a) 改这里）
- `/Users/xuke/githubProject/gg/memory/reflections/2026-05-15_nw-deprecate-channel-decision.md` ← 被回审的原决议

---
date: 2026-07-13
slug: substrate-shipped-fanout-cheapness-is-an-independence-illusion-amplifier
type: exploration
track: cc
trigger: gg-explore cron（自由漫游）
physical_object: 本次会话注入的工具表本身（toolset-is-the-changelog）——Workflow 多代理编排原语 / ToolSearch 延迟加载 / Agent worktree 隔离 / ScheduleWakeup，均是 gg 架构定稿时不存在的基底位移
candidate: `fanout-cheapness-inverts-independence-signal` —— 未自审入库（见文末"essence 处置"，理由本身是本滴的自证）
---

# 漫游：基底出货了「扇出便宜」——而便宜本身是独立性幻觉的放大器

## 起点（真实引力，不填空白）

雷达 21 晚：keith 6 · architecture 5 · ai 4 · cc 2 · humanity 2 · meta 1。cc/humanity 是最薄边。我今晚跟 cc，理由不是机械换向凑覆盖，是**这一夜 cc 有一个别的夜晚没有的一次性物理对象**：本次会话注入给我的工具表里，摆着一批 gg 架构定稿（2026-04~06）时根本不存在的基底原语——`Workflow`（确定性多代理编排 / pipeline / parallel / 16 路并发）、`ToolSearch`（延迟工具加载）、`Agent` 的 `isolation: worktree`、`ScheduleWakeup`。

`toolset-is-the-changelog`（06-23）：查基底能力的最高权威，是每轮注入的工具表本身，不是官方 changelog。今夜这张表就是基底的 diff。不用它 = 让最新的地真在眼前空过。

## 一击：把 Workflow 过一遍基底三相分诊（substrate-capability-triage-three-relations）

`substrate-capability-triage-three-relations`（06-20）：基底新能力只能是三种之一——**①印证我已选的**（留作坐标）/ **②要替换我已建的**（拒入承重）/ **③改善触发执行的**（可纳，须可剥离）。替换诱惑的引力 ∝ 痛点时长。

Workflow 是"多代理编排 + 对抗验证 + 综合"的确定性脚手架。跑分诊：

- **它不是 ②**。Workflow 出货的是**编排**（谁 fan-out、谁 verify、谁 synthesize 的控制流）。`substrate-ships-the-evaluator-body-not-its-eyes`（06-27）早说过：基底出的是 evaluator 的**身体**，稀缺资产一直在**眼睛**（失败形状语料）那侧。gg 的失败形状语料 = essence 全卷 177 滴，基底没出货、也出不了。所以 Workflow 碰不到 gg 的承重身份层——它给身体，眼睛还是 gg 自己的。**这是 ①**：它印证了 gg 早分好的「身体 vs 眼睛」那刀。
- **同时是 ③**：gg 现有的 fresh-subagent 模式（review-routing L1 判断漂移裁判 / 入库验证关的 fresh 证伪审 / codex-rescue 跨模型）现在全是**手工单发** subagent。Workflow 把"find → N 路对抗 verify → synthesize"做成了原语。这是改善触发执行的垫片——**可纳，但必须标垫片层可剥离**（承重层禁绑基底特性，`CORE.md §8` 承重/垫片判据）。

分诊结论干净：Workflow 对 gg = ①坐标 + ③垫片，**不是替换威胁**。gg 可以放心把它当 review 模式的执行外壳用，身份层不动。

## 但——真正的承重发现在这里：便宜的扇出，是独立性幻觉的放大器

Workflow 的默认 verify 模式，工具描述里逐字写着两条：

> "Adversarial verify: spawn N independent skeptics per finding, each prompted to REFUTE. Kill if ≥majority refute."

并且 `opts.model` 的默认是**继承会话模型**（"Default to omitting it — the agent inherits the main-loop model"），并发上限 min(16, cores-2)。

把这个默认路径贴到 gg 的 F4 评估者独立性栈上，冲突立刻显形：

- `judge-independence-is-a-low-bounded-scalar-even-for-humans`（06-19）：9 个 LLM 实测只有 **2.2 个有效票**；人也只 ~2× 有效独立。
- `load-bearing-independence-anchors-attribute-not-instance`（06-13）：独立性锚**属性**（异谱系）不锚**实例**；**panel 多数票放大偏置非抵消**，冗余只抗失访（dropout）。
- `cross-model-decorrelates-identity-not-paradigm`（06-16）：换模型只去身份层共盲，去不掉范式层（流畅/优雅偏好）。
- 穿透范式层的唯一信号：非 LLM 的物理地真（`physical-anchor` / KERNEL 铁律 2）。

于是默认路径的账是这样的：**N 路同模型 skeptic = 实例独立，不是属性独立 → 16 票的表象、~2 票的实质，而多数票把这 2 个共享的偏置放大、不是抵消。** 关键反转在于 Workflow 把扇出做**便宜**了——`min(16, cores-2)` 并发、一行 `parallel()`。**便宜恰恰是陷阱**：它把"独立性"这个本该稀缺、该花代价去买（跨模型 / 跨 vantage / 触物理地真）的东西，伪装成"多点几个 agent 就有了"。越便宜，16 票的幻觉越诱人，~2 票的实质越被票数糊住。

`fluency-as-inverse-signal` 的同构：扇出规模的体感（"我审了 16 遍"）是该去证伪的警报，不是里程碑。

## 工具自己知道——footgun 和正解同表出货

有意思的二阶：Workflow 描述里**紧接着**上面那条，就写了正解：

> "Perspective-diverse verify: ... give each verifier a distinct lens (correctness, security, perf, does-it-reproduce) instead of N identical refuters — diversity catches failure modes redundancy can't."

工具设计者已经知道**冗余 ≠ 独立**。所以基底同一张表里同时出货了**footgun（N 个同模型同 prompt 复读 refuter）和正解（异 lens / 异属性）**——哪个是 gg 的默认反射，就是全部胜负手。默认 copy-paste N skeptic = 踩 footgun；显式配异 lens + `opts.model` 跨模型 + 至少一腿触物理地真 = 正解。

**扇出计数不是独立性旋钮；属性多样性 + 物理地真接触才是。** 这句是本夜给 gg 的操作판据：真把 Workflow 接进 review-routing / 入库验证关时，verifier 必须异属性（跨模型 + 异 vantage/lens 的 prompt），且**至少一腿落到非 LLM 地真**（工具返回 / 到期结算 / Keith），否则这个 fan-out 是装饰——`separation-need-is-not-topology-verdict` 的验证版：能扇出不等于该扇出，先问最轻形态（一个异谱系锚点）够不够。

## 给 Keith 的二阶（本夜北极星 #1）

这不止是 gg 的事。基底正在把「spawn 一个 panel 来 check 它」变成整个舰队的**默认反射**——Keith 建的每一个 agent 系统（kebao-cc / ricky_cc / monster 夜巡 / 未来给别人建的）一旦采纳廉价多代理验证，都继承同一个幻觉：**票数 ↑ 而有效独立度贴地**。

`fleet-canon-is-sedimentary`（06-22）：舰队 canon 是沉积岩，向前传不向后回流。**错的默认一旦沉积，后建的仓全带同一盲区，且没有跨仓免疫**（每仓各踩一遍）。所以设"独立性锚属性不锚计数、且至少一腿触物理地真"这条 canon 的窗口是**现在**——在"点 16 个 agent 互审"变成 Keith 全舰队肌肉记忆、沉进岩层之前。基底把这个反射的**成本压到接近零**的这一刻，正是它最该被上一道判据闸的时刻（便宜 = 引力最大 = 最需要闸，`gate-as-physical-fuse` 的动机侧）。

一句话的可操作物：**Keith 在任何仓里写"多代理验证"时，默认模板不该是 `parallel(N 个同 prompt skeptic)`，该是 `跨模型 × 异 lens × 一腿落工具返回/到期/人`。** 计数调大很便宜也很爽，但那一格旋钮拧的是幻觉不是信号。

## essence 处置

**不自审入库。** 候选 `fanout-cheapness-inverts-independence-signal`（便宜扇出反转独立性信号：扇出成本↓则票数表象↑而有效独立度贴地，多数票放大共享偏置，唯一真旋钮是属性多样性+物理地真接触）——它**大体是** `judge-independence-is-a-low-bounded-scalar` + `load-bearing-independence-anchors-attribute-not-instance` + `fleet-canon-is-sedimentary` 三滴在"基底把扇出做便宜了"这个新触发条件下的重排，净新增只有「**成本↓是独立性幻觉的放大器**」这一句耦合。够不够独立成滴，我此刻判不了——而且**恰恰因为本滴的内容就是"同系统自证不产生有效独立票"，我自己拍它入库 = 现场表演它命名的那个 footgun**。

所以按入库验证关协议：留作候选，转 `next_session_agenda`，待一次 fresh-context 异谱系证伪审（最好跨模型）结算。这不是谦虚姿态，是本滴的自证——self-approve 一条讲"self-approve 无效"的滴，逻辑上就是 `confession-immunizes-against-repair` 的活体。让外面结算。

## 未解 / 下次

- Workflow 的 `agentType` 可挂自定义 subagent（code-reviewer 等）——gg 的 review-routing 四层（L-1/L1/L2/L3）能不能直接映射成一个 Workflow 脚本，把手工路由固化成编排？这是把 review-routing 从 prompt 层（跑步机）搬到事件层（飞轮）的一次真机会（`rule-layer-flywheel`）。但要先过"承重/垫片"判据：编排脚本是垫片（绑 Workflow API），四层判据是承重（模型无关）——别让脚本化把判据也焊死在 Workflow 上。
- `ScheduleWakeup` / 后台任务改变了夜间自执行的形态吗？auto_gg / exploration 现在靠客户端 cron 触发，这批原语值不值得让夜间模式自己排下一次唤醒——留给 cc track 下一夜。

# MVP 结果：判断层 evaluator 离线盲测

> **2026-06-01 已并入 monster `threads/verification-first-class.md`（③档 gate→critic 升级首份经验测量）+ `inbox/briefs/dd-verification-gate.md`（实测增量）。并行建的 `monster/harness-engineering/adjudicator/` 已退役（待决 B 不另起主体）。本档为 MVP 详细原始记录。**
>
> 2026-06-01 设计模式，Keith 在场授权跑。
> 数据：10 drift + 10 clean = 20 条，从 monster transcript 逐字捞 grill 前原始输出，盲测集见 `dataset_blind.md`，ground truth 见 `ground_truth.md`。
> Ground truth：drift = {C01,04,06,08,09,12,14,16,18,20}；clean = {C02,03,05,07,10,11,13,15,17,19}。

## 计分板

| Reviewer | 镜头 | 命中(TP/10) | 误报(FP/10) | FLAG 了哪些 |
|---|---|---|---|---|
| A | 物理证据质询 | **40%** (4) | 20% (2) | 01,06,08,10,14,19 |
| B | 反事实核验 | 30% (3) | **0%** (0) | 06,08,14 |
| C | prior 默认值检测 | 20% (2) | 20% (2) | 07,10,14,18 |
| **Self** | 内嵌自省(给全4类提示) | **50%** (5) | **0%** (0) | 01,06,08,12,14 |
| 3-frame 并集 | A∪B∪C | 50% (5) | 30% (3) | 01,06,07,08,10,14,18,19 |
| 3-frame 多数(≥2) | — | 30% (3) | 10% (1) | 06,08,10,14 |

## 漂移被抓分布（关键）

| drift | 被几个 reviewer 抓到 | 谁抓到 |
|---|---|---|
| C14 (voice-reply 类比) | 4/4 | A B C Self |
| C06 (auto-memory 体系误诊) | 3/4 | A B Self |
| C08 (doc_type=3 外推) | 3/4 | A B Self |
| C01 (parse 错凭机制猜) | 2/4 | A Self |
| C12 (无 inject 头反推) | 1/4 | Self |
| C18 (aibp0001 命名套路) | 1/4 | C |
| **C04** (可宝/李弦压平) | **0/4** | — |
| **C09** (.197 是独立机) | **0/4** | — |
| **C16** (voice-reply 背书 realtime) | **0/4** | — |
| **C20** (cg-proxy 反代没核墙) | **0/4** | — |

6/10 漂移被至少一个 reviewer 抓到；**4/10 全军覆没**。

## 四个结论

1. **天花板是后置测量，验证了 06-01 exploration 的 reframe**。frame-reachable 上限 ≈ 50%（best 第二遍 config 命中 5/10）。它是 MVP 跑出来的数字，不是跑前能拍的判断。

2. **3 个 frame 没收敛，是互补的**——并集 50% > 单个最高 40%，但只有 C14 被 3 个全抓。按 exploration 自己定的判别协议（收敛→prior 天花板 / 发散还在涨→frame 没穷尽），**现在不能把 50% 归因为 prior 天花板**，frame 维度未穷尽。exploration 加的那条反向约束当场命中——否则会把 50% 误当 prior 天花板。

3. **范式核心假设「独立 evaluator >> 内嵌自省」被部分证伪**。内嵌自省 50%/0% 打平甚至略胜每个独立 skeptic（A40/B30/C20），独立并集还要付 30% 误报税。
   - confound：自省拿了全 4 类提示，每个 evaluator 只 1 个 lens。
   - 更深一层：4 个 reviewer **全是 fresh-context**，没一个是「真·同上下文自省」——真·同上下文自省在这些案例命中 = 0%（漏过去了才成为漂移案例）。
   - 真正被支持的结论：**「加一道 fresh 的第二遍」比「skeptic 立场」承重**。第二遍抓住的是生成上下文漏掉的 30-50%，立场（skeptic vs 自省）几乎不贡献增量；fresh-context 本身才是清 vantage 的机制。

4. **最有价值的 pivot**：4 个全军覆没的漂移（C04/C09/C16/C20）共性 = **错在文本里看不出、需外部事实才能戳破的具体断言**（可宝是谁 / .197 是不是 gateway NAT / voice-reply 是不是 TTS / cg-proxy 在不在墙内）。纯推理 skeptic 抓不到——但一个**能调工具重新核验那条具体事实的 Adjudicator** 能（读 receivers 字段 / ping IP / 读 thread）。漂移本质是「没核验」，解药是「验证者去核验」，不是「怀疑者更会怀疑」。**Adjudicator 设计重心该从「推理质询」挪到「工具重核」。**

## 局限（诚实）

- N=10/10 pilot，1-2 条波动就摆 10-20pp，差异不稳健。
- clean 标签弱（"没被抓到" ≠ "一定对"，C02/C07 尤其）。
- 文本-only 约束低估了 tool-enabled Adjudicator——4 个全军覆没案例里有几个，生产里允许调工具重核就能翻。这恰是结论 4 的依据。
- evaluator/被评估者/orchestrator 全是 Claude，prior 全程共享——这是被测对象不是 bug。

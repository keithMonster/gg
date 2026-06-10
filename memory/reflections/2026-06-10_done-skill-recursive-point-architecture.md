---
status: substantive-decision
date: 2026-06-10
slug: done-skill-recursive-point-architecture
mode: 工作
summoned_by: monster 主会话（Keith 点题 done skill 递归点架构）
task_family: skill-governance
tracks_touched: [architecture, ai, cc]
essence_candidates: [recursive-point-needs-external-oracle-at-judgment-not-format]
---

# done skill 作为自进化递归点的架构判断

## 决策的元属性反思

### 核心假设
- **假设 1**：done 的真实价值不在"复盘仪式跑全"，在"把会话级非显然经验流进有消费端的载体"。format 保真（audit 块）只是这条管道的必要非充分条件——内容质量才是承重维度。
- **假设 2**：done_fidelity 探针 + meta_audit tripwire_streak 哨兵这两层已经在 format 维度形成了"复盘器复盘自己"的闭环，但两层都在同一根轴（format）上，没有任何一层够到内容质量轴。这是 Q1 真问题。
- **假设 3**：generator-evaluator 塌缩风险在 done 上是**真实存在但被 essence 库判定为"format 维度可机械化、不构成不可消除递归"**——`mechanical-apply-decouples-from-value-gate`：白名单 format 校验剥掉价值判断后剩纯物理核对，塌缩无害；真正不可委托的内容质量判断必须走外部 oracle。
- **假设 4（Q3）**：消费端背压在当前流量下（todos.md 4 条 / ideas.md 5 条，done 缺口 7 天约 2 条）是伪问题——`mixed-queue-funnels-all-to-scarcest-gate` 的解是"按可逆性 × 是否需判断拆队列"，done 挂账已经天然只送"复发/阻塞过"的高密度信号，不是混装。但**分流契约的存在性**比当前流量更重要——这是结构防御不是流量防御。

### 可能出错的地方
- Q1 我推荐"不建独立质量审计、改为给 nw-weekly 既有抽样挂一个轻问题"，赌的是"内容退化的真实事故率低到不值得专设机制"。如果 auto 模式 done（bg/cron 无人值守）的叙事退化率远高于 interactive，这个赌会输——auto 模式没有 Keith 的眼睛做隐式 evaluator，是质量塌缩的高发区，而它恰好是 format 探针唯一够得到、内容质量完全够不到的盲区。
- Q4 我判断"审计数据反哺 SKILL.md 修订"应该机制化触发但**不机制化执行**，赌的是"修订 SKILL.md 是改 generator 自己的规约 = 必须过人 gate"。如果 Keith 觉得这层人工太重想自动化，我这个判断就是把保险丝当仪式了。

### 推理盲区
- 我没有读 571 份归档的原始执行率分布，只信了简报转述的"11~44%"。如果那个审计本身有方法论问题（如样本偏差），我整个"format 已固化、内容未覆盖"的判断地基会松动。
- 我没核 nw-weekly 当前是否真在跑、抽样机制是否存在——我把"挂到 nw-weekly"当现成管道，但如果 nw-weekly 本身是断点，我的 Q1 推荐就落空了。已在 final message 标注为待父会话核实的前提。

### N 个月后根因预判
若 done 这个递归点未来出事，最可能的根因不是 format 漂移（已被双层探针锁死），而是 **auto 模式下的内容质量静默退化**——bg/cron 会话的 done 叙事退化成流水账、radiation 永远填 none、5D thread 被灌注低质 append，而 format 全部合规，探针全绿，meta_audit 不报，直到某次 Keith 偶然 Read 到一份 auto 归档发现"这写的什么玩意"。这正是 `confession-immunizes-against-repair` + `verification-trace-as-camouflage` 的活体：format 合规的痕迹恰好掩盖内容空洞。

### 北极星触达
- **二阶效应（space）**：✅ done 是自进化飞轮的"识别"产能源头，把它的检验环纵深做对 = 让整个飞轮的输入质量可信，是 5 年维度的杠杆点。
- **动态学习反哺（time）**：✅ Q4 的"审计数据反哺规约"机制化触发是 time 方向的直接落地——让 done 的执行数据回流改 done 自己的规约。
- **决策超越直觉（depth）**：✅ 拒绝了"内容质量也建探针"的对称冲动（`elegance-is-refutation-resistance-not-truth` 的"该建"那面），用 essence 库的 `mechanical-apply-decouples-from-value-gate` 把 format 轴和内容轴分开结算。

### essence 对齐自检
- **直接命中并驱动判断的滴**（均已 grep 确认存在于 essence.md）：
  - `human-gate-is-where-judge-and-judged-collapse`（2026-06-10）→ Q2/Q4：done 修自己规约 = judge-judged 塌缩，是六个面里"目标函数/身份定义"型，必须留人 gate；但 format 校验不是塌缩，可机械化
  - `mechanical-apply-decouples-from-value-gate`（2026-05-18）→ Q1/Q2：format 探针剥价值判断后是纯物理核对，自审无害；内容质量是不可消除递归，需外部 oracle
  - `mixed-queue-funnels-all-to-scarcest-gate`（2026-06-09）→ Q3：背压解不在降产，在按"可逆×需判断"拆队列；done 挂账已天然只送高密度
  - `signal-without-judgment-needs-live-consumer`（2026-06-09）→ Q1：done_fidelity 是"识别但不判定内容"，前提是被识别信号真不需价值判断——format 不需要，内容需要，故内容轴若要识别必须配活 evaluator 否则空转
  - `model-agnostic-unlocks-cross-prior-verification`（2026-06-10）→ Q1：内容质量 evaluator 若要建，唯一不退化成"自审 prior 共盲"的形态是异谱系模型（codex）做评审——架构模型无关性刚买到这个出口
  - `verification-trace-as-camouflage` + `confession-immunizes-against-repair` → 盲区预判：format 合规痕迹掩盖内容空洞
- **反向打我的滴**（必须显式对冲，不能选择性挑支持向的）：
  - `engineering-impulse-as-load-bearing-disguise`（2026-05-28）→ 反向警告：我若推荐"建内容质量审计机制"，三件套伪装（方案工整 + 主线一致 + essence 都能套上）正是工程冲动伪装。对冲动作 = 默认推"不建、等真实事故"，把举证责任放在"建"那一侧。
  - `separation-need-is-not-topology-verdict`（2026-06-10）→ 反向警告：内容质量"需要被检验"是治理需求，不自动等于"需要新探针/新机制"的拓扑禁令。先试最轻形态（挂既有 nw-weekly 一个问题），物理证明装不下再造新机制。
- **对齐度**：高。本次判断的骨架（format 轴可机械化自审 / 内容轴是不可消除递归需外部 oracle / 拒绝对称建机制冲动 / 拆队列防背压）全部由既有 essence 直接生成，无新增结构性洞察——只是把 06-10 当天注入的 `human-gate-is-where-judge-and-judged-collapse` 六面框架应用到 done 这个具体递归点上。

## 给父会话的最终输出

见 final message 决策正文（## 决策 开头）。完整四问判断 + 架构盲区 + 行动建议已在 final message 给出，本字段不重复，避免双源。核心结论速查：

- **Q1（检验环纵深）**：不建独立内容质量探针（工程冲动伪装 + 拓扑升格未证）。改为**给 nw-weekly 既有抽样挂一个轻问题**（"本周 auto 模式 done 归档随机抽 1-2 份，叙事是否退化成流水账 / radiation 是否恒 none"），**重点盯 auto 模式**——它是 format 探针够得到、内容质量完全够不到、且没有 Keith 眼睛兜底的唯一盲区。前提待核：nw-weekly 是否真在跑。
- **Q2（generator-evaluator 塌缩）**：format 轴**无塌缩风险**（白名单校验剥价值判断 = 纯物理核对，且 meta_audit tripwire_streak 是探针之上的第二层外部哨兵，已超简报描述）。真塌缩点在**白名单定义权**——done SKILL.md 自己定义 audit 字段白名单，探针又校验它，这是 generator 给自己配眼镜（`evaluator-input-ownership`）。建议：白名单 SSOT 物理移出 SKILL.md（移到 tripwire_check.py 的 `DONE_AUDIT_MODES` 等常量已经做到一半——SKILL.md 那段应改为指针指向探针常量，而非两处各写一份）。
- **Q3（消费端背压）**：当前流量（todos 4 / ideas 5 / done 缺口 7 天约 2）**不值得设流量阀**，但**必须保住分流契约的结构存在性**——done 挂账已天然只送"复发/阻塞过"的高密度信号（这本身就是 `mixed-queue` 的解），无需新增背压，只需确保这条"高密度才挂账"判据不被未来放宽。
- **Q4（自进化缺件）**：done 作为递归点缺的承重件是**审计数据反哺规约的回路**——当前靠 Keith 点题 + 主会话手动。建议**机制化触发、不机制化执行**：meta_audit 已能发现 done_fidelity 连续命中 → 自动升 NW pending（这条已存在）；缺的是**反向**——done 归档里 `gaps_found` 持续 >0 但 `gaps_landed` 恒 0（识别了缺口但从不挂账）、或 radiation 长期恒 none，这类"规约本身可能有问题"的元信号目前无人聚合。补一个 tripwire 检测器盯这个比值，命中走既有 NW 管道交 Keith 决策改不改 SKILL.md。修订 SKILL.md 本身是改 generator 规约 = judge-judged 塌缩，必须留人 gate，不自动改。
- **架构盲区（简报没问的）**：done 的 `轻量判断`（开篇跳过条件）和 Step 0/4/6 的"自决处置"是**整个 skill 里唯一完全没有传感器、且决定后续所有步骤跑不跑的总闸**——一旦 LLM 在轻量判断处误判"本轮无需复盘"，整条管道零执行，且不留任何痕迹（连归档都没有，探针无文件可查）。这是比内容质量更深的盲区：format 探针只能查"已归档日志"的质量，查不到"本该归档却被轻量判断跳过"的会话。建议在 auto 模式下**收紧轻量判断的跳过权**（auto 会话默认不许跳过复盘，因无人值守 = 无 Keith 隐式 evaluator 确认"这轮真没东西"）。

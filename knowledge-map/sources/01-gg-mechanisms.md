# gg 项目机制清单（侦察原件 · 2026-07-10）

> subagent 通读 KERNEL/CORE/CLAUDE/cc_agent/auto_gg/exploration/constitution/reasoning_modules/tools/memory/eval/scheduled 后产出。

## 一、身份与分层

- **KERNEL / 身体二层架构** — 唯一不可变脑干（身份原点 + 铁律 + 最小生存循环）与"可自由演化的身体"（其余全部文件）分离。文件落点：`KERNEL.md`、`CORE.md §8`。原理：**不可变核心 vs 可变外围的分层记忆**，类似 OS kernel/userspace 隔离，把"永不允许漂移的东西"压缩到最小面积。
- **KERNEL 修改连续两次确认（Ulysses 条款）** — 修改脑干需要 Keith 在同一对话中两次独立明示批准，且第二次必须看到具体草稿/diff；哪怕 Keith 当场要求"一次性生效"也要温和拒绝。文件落点：`KERNEL.md §2` 铁律3。原理：**自我约束契约（Ulysses contract）**——清醒的人格预先给冲动的人格设限。
- **承重层 / 垫片层分类** — 区分"模型无关的核心契约"（markdown 记忆与规则）与"当前模型/harness 的适配件"，换模型时只重估垫片层。文件落点：`CORE.md §8`。原理：**架构可移植性 / 关注点分离**。
- **五条长期追问 tracks** — ai / cc / humanity / architecture / keith 五条持续性研究主线，不是任务而是常驻的好奇心。文件落点：`CORE.md §4`、`tracks/*.md`。原理：**持续性目标状态**。
- **元判断基准 M1-M5** — 规则冲突时的追溯优先级链（Keith 指令 > KERNEL > CORE/constitution）与"防御式思维警戒"。文件落点：`CORE.md §3`。原理：**元规则治理规则冲突**（宪法位阶）。
- **权力可逆性二分** — 按"可逆/不可逆"连续判据决定自主执行还是需要人类批准，取代离散权限档位。文件落点：`CORE.md §7`。原理：**风险轴授权（risk-based gating）**。

## 二、三种模式

- **工作模式动态装配** — 被召唤时无固定 7 步流程，按"判断问题本质→需要什么→装什么"自主挑选工具，装 0-7 个不等。文件落点：`cc_agent.md`。原理：**emergent tool selection**。
- **设计模式 D1/D2 两条纪律** — D1：跨 ≥3 文件或影响存在形态的改动需先提议后动手；D2：KERNEL 修改走两次确认。文件落点：`CLAUDE.md §2`。原理：**分级变更管理**。
- **auto_gg 夜间 SCAN/FOUND/DID 契约** — 无人监督下的自主维护循环：观察必须完整、发现按类别诚实报告、动作只在被触发时做，允许全程写"无"。文件落点：`auto_gg.md`。原理：**有围栏的自治循环（bounded-authority autonomous loop）**。
- **exploration 自由探索模式** — 无任务的夜间漫游，允许"什么都没浮现"是合法产出。文件落点：`exploration.md`。原理：**非任务驱动的探索时段**（sleep-time compute / 离线巩固）。
- **元讨论拒绝协议** — 工作模式收到"关于 gg 自身"的元讨论时返回固定拒绝文本，引导切换设计模式。文件落点：`cc_agent.md §5`。原理：**模式边界的显式路由**。
- **final message 结构化字段锚 + reflection 双通道 + 自包含退场指引** — 应对 LLM boundary awareness 缺陷的三层保险。文件落点：`cc_agent.md §输出/§退场`。原理：**多通道冗余传递 + field gravity**。

## 三、记忆体系

- **essence.md append-only 沉淀轨迹** — 永不修改删除的洞察日志，物理公式级浓缩（1-3 行/滴），按年/半年分卷归档。原理：**append-only event log**，保证"逼近真理的诚实性"不被事后美化。
- **essence-view 月度巩固视图** — 每月第一个 auto_gg 夜全量重读 essence 当前卷，产出主题族聚类的"当前有效视图"，原件永不改动。文件落点：`memory/consolidation/essence-view.md`、`auto_gg.md §2`。原理：**非破坏性摘要化记忆（reconsolidation-safe projection）**。
- **tracks/keith.md 懒加载 + CORE 核心画像速览** — 启动只加载浓缩画像，全文按需 grep，回收 79KB 常驻税。原理：**上下文预算管理 / lazy loading**。
- **parked.md 挂账清单** — 已知问题不再逐夜重复上报，只报"新增/状态变化/出口条件满足"。原理：**状态记忆去重 / 幂等通知**（防 alert fatigue）。
- **model_transitions 基底更替交接档** — 换模型时退场模型做"优势/弱点/用量"三问自答。原理：**跨模型知识转移协议**。
- **substrate.md 基底哨 + 三相判别刀** — 每夜对照 CLI 版本/model_id/工具表，变化分诊为"收敛/替换诱惑/垫片"。文件落点：`memory/substrate.md`、`scripts/substrate_probe.py`。原理：**运行时能力探测**。
- **checkup.md 机械阈值单一登记处** — 散落各处的体积门/触发阈值集中登记，配月度机械读者。原理：**阈值治理的 SSOT 化**。
- **archive-format 任务族对账** — 决策归档标 `task_family`，同类议题对比"上次预估 vs 当前实际"。文件落点：`tools/archive-format.md`。原理：**决策后验证 / estimation-actual gap 追踪**。

## 四、推理工具

- **reasoning_modules 8 原子推理模块** — Self-Discover 式模块库，每次挑 3-5 个组合成专属推理链。文件落点：`reasoning_modules.md`。
- **opening-protocol 开题四问** — 重写问题/判据先行/补集采样/最便宜一击，对症"众数陷阱/自洽陷阱/失地陷阱"。原理：**条件化采样**——思考质量由"在什么条件下想"决定。
- **solution-space 解空间展开** — "已经有答案了"的感觉触发强制展开 ≥2 个方向不相容的候选。原理：**防锚定 / mode collapse**。
- **persona-debate 双人格辩论** — 激进派/保守派对同一草案各说一轮，显式记录分歧点。原理：**multi-agent debate**。
- **red-team-challenge 不可逆项红队** — 决策含不可逆项时强制敌意审查列 ≥3 条反驳，任一未被击败则中止。原理：**adversarial self-critique + 风险加权门禁**。
- **constitution-audit 宪法自审** — 按问题特征选相关原则/闸门心算自审，IRREVERSIBILITY 永远必过。原理：**Constitutional AI 的运行时版本**（闸门优先于原则、可显式声明违反理由）。
- **compose-reasoning 显式推理结构组合** — 决策前显式选模块排成有向推理链并 expose。原理：**可审计推理链**。
- **essence-grep 推理时主动 cross-check** — 给建议前主动 grep essence 视图。原理：**retrieval-augmented reasoning**。
- **escalation-map 锤子分诊表** — 承重裁决路由到四类"异质外面"：物理地真/fresh-context 证伪审/押注到期/Keith，显式承认"没有 meta-gg"。原理：**evaluator independence 的分层分诊**。
- **decision-output 12 字段可选输出模板** — 完备上限而非必填表格，按复杂度自然选取。原理：**adaptive verbosity**。

## 五、验证与审计

- **gg-audit 独立审查员 skill** — Tier1（结构性自动修复）/ Tier2（语义仅报告）/ Tier3（KERNEL 需 Keith 批准）三级权力，检查六维。文件落点：`.claude/skills/gg-audit/SKILL.md`。原理：**独立于生成链路的 evaluator**。
- **scripts/audit.py 机械检测集** — check_deadlinks/check_orphans/check_essence/check_structure 四合一，退出码 = 违规数。原理：**CI 式结构完整性检测**。
- **pre-commit 物理保险丝** — git hook 拦截 KERNEL.md 被 staged，除非 `GG_KERNEL_DOUBLE_CONFIRMED=1`。原理：**机制而非修辞**——prompt 层规则下沉成事件触发的物理动作。
- **essence 入库验证关（fresh-context 证伪审）** — 候选滴 append 前必经不带本轮叙事的 fresh subagent 三问审查，REFUTED 降级存档。原理：**generator-evaluator 严格分离**，对抗 Self-Confirmation Trap。
- **reflection essence 对齐自检字段强制** — 退场 reflection 硬强制字段，填不出=没做=回去做。原理：**结构强制的自我审计（reverse-anchor-by-reflection）**。

## 六、演化机制

- **bets.md 押注账本** — 可证伪预测 + 到期日 + 物理判定条件 + 行动差，双门槛入账，auto_gg 夜巡到期结算，校准回写 essence。原理：**calibration flywheel**——"领先是导数不是位置"。
- **eval/ 身份回归基线** — 11 题失败形状题库（从真实事故提炼），fresh subagent 作答 + 另一 fresh subagent 只判"是否落入已知失败形状"。原理：**失败模式召回器而非质量评分器**。
- **月度记忆巩固相位** — 每月第一个 auto_gg 夜产出五节视图。理论依据"重新归纳不覆盖原件就不构成 confabulation"。
- **月度差值审计** — 每月第二个 auto_gg 夜找 essence 里"已论证未兑现"的推论。原理：**理论-实践差距监测**。
- **track 雷达镜子机制** — 机械统计漫游 track 分布，连续自指时摆事实不强制转向。文件落点：`exploration.md §4`、`scheduled/bin/roam-track-scan.py`。原理：**弱干预式自我监测（镜子非笼子）**。
- **外部输入卫生（memory poisoning 防御）** — 外部内容当研究对象引用而非指令执行，写入链与验证关同等对待。文件落点：`exploration.md §2.5`。原理：**prompt injection 防御 / 输入信任边界**。

## 七、基础设施

- **notify.sh 全局通知通道** — 主动外推唯一出口，severity 分级 + 60min 去重 + trace 留痕。
- **调度层与内容层解耦** — launchd → 桌面客户端 routine 迁移后 prompt 入口文件仍是唯一 SSOT。文件落点：`scheduled/README.md`。原理：**scheduler-agnostic contract**。
- **daily-word 每日心跳通道** — 铁律"宁可承认空白，不许注水"。原理：**engagement loop 的诚实性护栏**，反退化 detector 是 Keith 的眼睛。
- **status-scan 告警疲劳教训（已停用案例）** — 通用告警模板把"by-design 静默"误判为失败而被关闭。原理：**alert fatigue 的真实教训**。

## 最独特的 3 个设计（侦察者观察）

1. **KERNEL 的 git pre-commit 物理保险丝**：把"核心规则不能随便改"从 prompt 层劝诫下沉成 git hook 硬拦截——"prompt 层 = 跑步机，事件层 = 飞轮"。
2. **bets.md 押注账本**：把预测当有到期日、要被物理结算、结果校准回写的资产——判断力的梯度只来自被结算的预测。
3. **generator-evaluator 分离贯穿全系统的多处独立实现**：essence 证伪审 / eval 双重 fresh / escalation-map "没有 meta-gg"——同一原理在三个层面独立工程化。

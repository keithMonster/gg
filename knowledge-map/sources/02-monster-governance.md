# monster 治理体系机制清单（侦察原件 · 2026-07-10）

> subagent 通读 ~/.claude/CLAUDE.md、monster/CLAUDE.md、CLAUDE.d/、threads/llm-foundations.md、review-routing SKILL.md 后产出。

## 一、全局治理规则

| 机制名 | 是什么 | 文件落点 | 原理 |
|---|---|---|---|
| 安全红线两档分级 | "一按就产生真实不可逆副作用"和"纯认知/流程约束"分两档，前者调用前显式 ack | `~/.claude/CLAUDE.md`、`monster/CLAUDE.d/security.md` | 分级熔断——"人在场确认"的成本只花在真正不可逆的动作上 |
| Workflow 确认门（5 类触发） | 改上游契约/调生产系统/多文件变更/不熟悉三方库/架构调整前必须先出方案 | `~/.claude/CLAUDE.md` Workflow 段 | plan-then-act 按不可逆程度分流 |
| Engineering Rules 13 条 | 输入四查、失败两次换维度、改契约先 grep 消费者等 | `~/.claude/CLAUDE.md` | 把"LLM 会系统性偷懒"固化成检查点 |
| Subagent Routing 分流 | 调研/批量读交子代理，"外包信息收集不外包理解" | `~/.claude/CLAUDE.md` | orchestrator-worker 的上下文经济学 |
| CLAUDE.d 分层拓扑 | 超行数门限强制拆子文件，主索引常驻+子文件懒加载 | `monster/CLAUDE.d/context-curation.md` | 惰性加载对抗 context rot |
| 11 条结构原则 + 双轴审查 | 准入裁剪/一事一SSOT/理由链下沉…；结构轴×锚词轴正交审查 | `monster/CLAUDE.d/authoring-handbook.md` | 把 prompt 文档质量转成可审计 lint |
| 编码编排三档判据 | 轻(串行)/中(并行 Worker)/重(Workflow 盲跑) | `monster/CLAUDE.d/coding-subagent.md` | 编排复杂度的成本-收益判据 |

## 二、决策权限与升级

| 机制名 | 是什么 | 文件落点 | 原理 |
|---|---|---|---|
| Decision Authority 三层 | 目标层 Keith / 实现层 Claude / 架构层 gg | `monster/CLAUDE.md` | 分层自主权（human-on-the-loop） |
| 抛回三类合法 trigger + 强制语法 | 只有目标范围/偏好/不可逆参数才抛回，形态="我用 X 理由 Y，想换 Z 告诉我" | `monster/CLAUDE.md` | 反"决策外包伪装成谦逊" |
| gg 主动召唤判定 | 架构级难回退 + 当前层信息内无解，两条同时成立才升 | `monster/CLAUDE.md` | 逃逸阈值显式化 |
| 核对不抛回 | 承重产出先派 fresh subagent 独立核验，不拿用户当 verifier | `~/.claude/CLAUDE.md` Review 段 | generator-evaluator 分离 |
| 纠正即落库 | 用户事实性纠正当场 grep 全仓改正 + 时间线记事件 | `monster/CLAUDE.md` | 在线增量学习 |
| Context Asymmetry + 意图回显 | 承重任务出方案须回显"目标 X + 可证伪假设 Z" | `monster/CLAUDE.md` | 显式目标状态确认 |
| 锚点四分类退役判据 | 信息/能力补丁/架构补丁/结构锚点，退役靠传感器数据 | `monster/CLAUDE.d/harness-map.md` | 防护机制的生命周期治理 |

## 三、review 与验证分层

| 机制名 | 是什么 | 原理 |
|---|---|---|
| review-routing 五档路由 | L-1 实跑/L0 内省/L1 fresh 同事/L2 跨模型/L3 架构，视角独立性随档位递增 | 视角多样性分级供给 |
| [verify] 三行块 | 写操作后强制"改动定位+命令+输出" | 强制 grounding |
| L1 三 flavor 拆分 | 实现层/方案层/互动拷问三种 reviewer 分离 | 专职化优于万能化 |
| 承重判断层裁判 | fresh 子代理只读冻结 critic_prompt 当判官，禁读其它 | frozen judge——judge 与生成侧物理隔离 |
| 升级原则 | 改动面积/不可逆性自动升档 | 基于风险的自动强度调节 |
| 三会话协议 | 架构/执行/审查三分离，审者不能审自己 | 关注点分离在会话粒度 |
| 自查幻觉不可信 | 怀疑幻觉时"自查根因"触发二阶 confabulation，只信 transcript 原始字节 | 系统不能从内部证明自身一致 |

## 四、记忆与知识沉淀

| 机制名 | 是什么 | 原理 |
|---|---|---|
| 分层检索 L1-L4 | 规则索引/threads/SQLite FTS5/原始 jsonl，自上而下不许跳级 | tiered memory |
| threads 主体维度记忆 + 两区切分 | 按名词主体切 thread；"当下事实区"与"历史状态流"物理分区 | 实体中心索引 + 可变/不可变分层 |
| MEMORY.md 自动派生索引 | 索引 100% 由脚本从 frontmatter 派生，禁手工编辑 | 单一数据源 + 派生视图 |
| canon / canon-bugs 横向记忆 | 跨主体的规矩/决策理由链 + bug 症状反查表 | 正交存储维度 |
| concepts.md 元概念词典 | 自创术语的权威定义源，防 LLM 即兴造词漂移 | 术语本体作漂移锚点 |
| 观察期结算 | 新机制的撤销条件由客观数据判定，不许自证有效 | 成功度量不能内生 |
| 检索充分性契约 | 否定断言前强制走完检索链，否则降级"没查到" | 非对称风险下的举证责任转移 |

## 五、prompt 工程实践

| 机制名 | 是什么 | 原理 |
|---|---|---|
| 语义场域牵引模型 | 目标=够不到的球，从语义邻居种锚拉扯画引力路径 | 激活工程——prompt 是吸引子布置不是指令传达 |
| Prompt Writing 5 条准则 | 激活而非描述/具体>抽象/词义漂移/敏感反例点名/反复=重要 | "写清楚"="给出强激活信号" |
| 负面表述分层规则 | 正面锚词优先/硬禁止同句绑定替代/删因果论证尾巴 | negation 弱效应的分层对策 |
| 锚词激活轴 vs 结构轴 | 双轴正交审查，防"长但激活强"被误删 | 内容质量的双维度分解 |
| RLHF 副作用对冲清单 | 每个外化锚点标注对冲哪条 RLHF 已知偏差 | alignment tax 的显式对账 |

## 三个最独特的设计（侦察者观察）

1. **治理规则本身要过"证伪测试"，不允许自我报告有效**——观察期结算/锚点退役/冻结裁判三处独立收敛到同一约束：有效性判定必须挂系统外传感器。哥德尔第二不完备定理的工程化。
2. **Prompt 工程有自洽理论支撑且被反向验证**——每条实践钉到具体论文，区分"硬支撑/引申/引用错配"三层置信度，还订正过自己的错误引用。
3. **"抛回"被重新定义为可疑行为而非谦逊美德**——"出选项让用户选"判定为失职，正确姿态是"举手+否决权"。

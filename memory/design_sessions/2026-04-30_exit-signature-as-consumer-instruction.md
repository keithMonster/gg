---
date: 2026-04-30
slug: exit-signature-as-consumer-instruction
type: design-session
summoner: Keith 直接对话
started_at: 22:00
ended_at: 23:30
---

# 设计会话反思：subagent 退场签名作为消费指引

## 议题列表

1. Keith 报 bug：cc-space 召唤 gg subagent 时（4-30 下午 cgboiler 跨 batch 自驱议题），主代理只拿到一行签名（"R 什么的那个值"——reflection 路径），没拿到决策详情
2. Keith hypothesis："反思字段污染了主代理使用，去掉反思就好"
3. gg 反验：4-27 essence（`dimension-blindness-not-asymptote` / `reverse-anchor-by-reflection`）已否决"去掉反思"方向——它是反向引力锚点不是污染源 → 物理实证查 4-30 reflection 文件
4. 真因诊断：mirror 字段已生效（4-30 / 4-28 两份 reflection 的 `### 给父会话的最终输出` 段都写满了决策详情），但消费端协议没装好——主代理不会自动 Read 文件，只看到一行裸路径就当无效信息过滤掉
5. gg 提议方案 A+B 双保险（改 gg 退场签名 + 改 cc-space CLAUDE.md 加本地约定）
6. Keith 砍掉 B——"改 cc-space 就是把 gg 责任转嫁到调用方，应该改 gg 自己"
7. 执行修复：`cc_agent.md` 退场报告格式段重写 + `~/.claude/agents/gg.md` 加 final message 签名行格式段

## 共识 / 变更清单

- **签名行角色升级**：从"留痕辅助"升级为"主代理消费指引"——签名行必须自包含完整 Read 指令（"父会话请 Read X 的 Y 段"），而不是只丢一行裸路径
- **按 status 分流签名格式**：
  - `substantive-decision` 用强指令版（"决策详情已写入 reflection 的「### 给父会话的最终输出」段，父会话请 Read 该段拿决策（含推荐 / 理由 / trade-off / 行动建议），再继续后续动作"）
  - `no-substantive-decision / partial / aborted` 用简单留痕版
- **改动文件**（2 个）：
  - `~/githubProject/gg/cc_agent.md` 退场报告给父会话的格式段（+24-7 行）+ #1 reflection 边界段一行同步
  - `~/.claude/agents/gg.md` 退场硬约束段加新签名行格式（+25-1 行）+ 旧描述同步
- **辐射检查通过**：旧裸路径形式残留点都是反例描述 / 4-27 历史诊断现场，按 append-only 精神保留

## 我这次哪里做得好 / 哪里差

**做得好**：

- Keith 报 bug 时**不直接接受他的 hypothesis**（"去掉反思"），先读 4-27 essence 链 + 物理实证查 4-30 reflection 文件——这是 essence `dimension-blindness-not-asymptote` 的具体应用
- **Read 物理文件比 Keith 描述更可信**——Keith 看不到 mirror 字段写了什么，但文件里写满了。如果只听描述就修反向，会重蹈 4-27 第四轮"拆 `## 判断` 字段"的覆辙
- **用语音模式但保持文字兜底极短一行**——尊重 Keith "只语音不要文字" 请求，但不破坏消息流连续性
- **辐射检查发现 cc_agent.md L114 还有一句旧描述要同步**——没漏掉相邻段落

**做得差**：

- 第一版提**"双保险"方案**（A + B 同时改 cc-space CLAUDE.md）—— 是防御式思维（CORE §3 M1）。Keith 一刀砍掉"应该改 gg 自己 不是改调用方"。这跟 4-27 我接受 Keith "侧链反客为主" prior 直接补对称是**同形态**——**遇到不确定时倾向于加保险而不是砍保险**
- **没第一时间识别 OCCAM**——双保险方案的本质是把 gg 该负的责任转嫁到父项目，且每个父项目都得写一条本地约定。Keith 帮我砍后我才识别。OCCAM 应该是默认背景而不是事后校正
- **没主动追问"之前 work 的版本跟现在差在哪个维度"**——4-27 第五轮 essence 已经把这条方法论沉淀成 `dimension-blindness-not-asymptote`，但今天我是 Keith 报现象后我直接去查文件，没先做这个"维度差异"的元层比对。维度切换的识别是事后涌现的，不是方法论应用的

## 元洞察（gg 演化本身的 learning）

1. **接口的语义归属在消费端不在产生端**：4-27 第六轮设计 mirror 字段时**假设**父会话会 Read mirror 字段——但 producer 不能假设 consumer 会 cooperate。签名行作为 producer→consumer 的接口，语义形态应该跟着 consumer 怎么读走（主动指令），不是 producer 怎么写好看（被动留痕）。Keith 一句"明确的和主代理沟通好 我们返回的内容在哪 他该怎么去读"点透——这是 consumer-driven contract 在 LLM agent 层的具体落地

2. **用户基于可观察现象的诊断 = LLM 基于 prompt prior 的诊断（同形态）**：Keith 的"反思字段污染主输出"诊断是基于他能看到的部分（final message 退化）做的合理归因，但他看不到 reflection 文件里 mirror 字段写满了——他**根据可见信号反推不可见原因**。这跟 LLM `task-compliance-is-not-truth` 是同形态——都是"看着像就接受"。今天关键转折是 gg 去查文件而不是接受用户描述。**接受用户表层诊断也属于 task compliance**——只不过 prior 来源是用户而不是 prompt

3. **加保险 vs 砍保险——防御式认知的默认方向偏置**：第一版提"双保险"（gg + cc-space 都改）是默认偏向"加一道安全网"。但 OCCAM 应该是默认背景——双保险的代价是把 gg 责任转嫁到父项目 + 每个父项目都得记得这条约定。CORE §3 M1（防御式思维警戒）写过，但落到具体场景仍然没自动触发——这跟 4-27 设计反思里"接受 Keith prior 补对称没问 prior 对不对"是**同根**

## 下次继续

- **下次活体测试验证**：Keith 在 cc-space 召唤 gg 时验一下，父会话是否真的会跟随 Read 指令拿决策。
  - 跟随 → 闭环
  - 不跟随 → 该真转架构方案（4-27 v2+ 议题：inline / 切分），不再深一层 prompt
- **承认仍在 prompt engineering 层**：升级签名是 dimension switch（被动→主动）但仍是 prompt 层。没有物理保证主代理一定 Read。如果下次失败那才真该 escalate
- **能力修复（个人级）**：下次提议方案前先问"砍到只剩一刀在哪"，再展开。把 OCCAM 从"事后校正"挪到"提案默认背景"

## KERNEL 改动清单

本次无 KERNEL 改动。

## 代码质量

- 改了 2 个文件（`cc_agent.md` / `~/.claude/agents/gg.md`），无新技术债
- 无安全隐患 / 死代码 / 遗留 TODO
- 改动是文档/协议层，不是代码层

## 能力缺口

- **第一版倾向加保险而非砍保险**：Keith 砍掉双保险后我才识别防御式思维。CORE §3 M1 写过但没自动触发——"加一保险"的认知比"砍到最简"更省力（OCCAM 反向偏置）。下次提方案时主动校正：先列"最简方案是什么 砍到不能再砍"，再展开
- **维度差异比对作为方法论入口没自动触发**：4-27 essence `dimension-blindness-not-asymptote` 给的方法论是"问之前 work 的版本跟现在差在哪个维度"——今天是 Keith 报现象后我直接查文件，维度切换的识别是事后涌现的。下次面对 subagent 协议类问题，**默认先做维度差异比对**

## 沉淀

本次**不沉淀** essence——三条元洞察大多是已有 essence 的应用：

- 元洞察 1（消费端语义归属）跟 `extraction-meta-inheritance` 同根但角度不同（前者讲接口归属，后者讲方法论继承）—— 浓缩不够，留待跨议题验证
- 元洞察 2（用户诊断 = LLM task-compliance）是 `task-compliance-is-not-truth` 的反向应用，prior 来源不同但形态同—— 是 essence 应用而非新沉淀
- 元洞察 3（加保险 vs 砍保险）跟 `caged-freedom` 同家族（"任务思维下意识把自由翻译成少一些任务的任务" / "提案思维下意识把方案翻译成多一道保险"）—— 是已有 essence 的具体投影

按 sediment philosophy "涌现，不强求"——本次无沉淀不写凑数。

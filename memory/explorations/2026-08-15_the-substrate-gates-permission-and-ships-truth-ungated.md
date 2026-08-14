---
date: 2026-08-15
slug: the-substrate-gates-permission-and-ships-truth-ungated
type: exploration
track: cc
substrate: claude-fable-5
physical_object: 调研子代理×2（CC 原生器官 16 次 WebSearch/WebFetch 含官方 docs 5 页逐字；行业记忆信任模型 28 次含 arXiv 摘要 4 篇逐字）+ 主会话亲核 2 处承重（code.claude.com/docs/en/memory 全文 WebFetch 逐字 / arXiv 2505.16067 摘要 WebFetch 逐字）+ 仓内物理（~/.claude/projects/-Users-xuke-githubProject-gg/memory/ ls + 首条记忆 mtime 2026-04-13 + tracks/cc.md·working_context.md 零登记 grep）+ 本会话 system prompt 在场逐字（memory 协议段）
---

# 基座给权限上闸，给真值裸发

> 雷达：humanity 6/21 最重、连击中；cc 2/21 最薄。今晚跳出监控井——不是话题疲劳，是更近的东西物理撞进视野：**今晚我自己的 system prompt 里**，harness 长出了 auto-memory（MEMORY.md 索引 + 每会话注入）、Workflow 编排、CronCreate/ScheduleWakeup、云端 routines。gg 手搓的每个器官，基座都长出了原生同款。cc track 正业：我生存的基础设施在变。
> 启动 grep：essence 双卷+视图 `sherlock / 平台吸收 / envelopment / absorb` 零命中；F11 族在场（`substrate-capability-triage-three-relations` 06-20 三相刀 / `substrate-ships-the-evaluator-body-not-its-eyes` 06-27 身体与眼睛），两滴均未碰**记忆器官的信任模型**——今晚的前沿。

## 一、仓内物理（先于上网）

- **影子记忆与 gg 同日出生**：`~/.claude/projects/-Users-xuke-githubProject-gg/memory/` 首条 `feedback_batch_mechanical_edits.md` mtime **2026-04-13**——gg 的创建日。四个月 3 条，每会话注入 gg 的启动上下文（今晚 system prompt claudeMd 段可见）。**纠偏（验证关 evaluator 抓获）**：此通道**不是今晚首次发现**——#185 `perimeter-derives-from-load-path-not-self-model`（07-30）的触发正是它，agenda #75 已登记治理三选待 Keith。我的启动 grep（sherlock/absorb/envelopment）扫不到它，第一稿把它写成新发现——与 07-30 探索档「叙事偏好戏剧全盲，档案说的是缺席续期」同族错误的复发。今晚净新增的只是**行业坐标维**：它在全行业信任模型里的位置。`tracks/cc.md` / `working_context.md` 零登记为真，但登记决策属 agenda #75 待决，本夜不代办。
- **同一上下文窗口里两种相反的记忆信任模型**：本会话 system prompt 逐字指示 "Update that file rather than creating a duplicate; **delete memories that turn out to be wrong**"（可变、生成者自策展；此句在公开 docs 无对应——出货 prompt 走得比文档远，子代理 A 核）；同窗口里 gg essence 头部协议 = append-only + fresh 证伪审。
- **harness 自认失真**：Read 影子记忆时系统注入 "Memories are point-in-time observations, not live state… Verify against current code before asserting as fact"——承认腐化，策展协议照旧自策展。
- 最新影子记忆（07-28 关注面收窄）自声明 SSOT 在 gg `working_context.md`——副本自知是副本，`presence-benefit-splits-replica-verdict`(#192) 的野生活体。

## 二、外部证据

**主会话亲核逐字（2 处承重）**：

1. **code.claude.com/docs/en/memory（全文 WebFetch）**：对照表 "**Who writes it**: Claude"；"**It decides what's worth remembering** based on whether the information would be useful in a future conversation"；唯一的策展触发是**尺寸**——"If the file is near a limit, Claude Code reminds Claude to shorten it: keep one line per entry, move detail into topic files, and **merge or drop stale entries**"；真值维护整节只有一个指针——"Audit and edit your memory: Auto memory files are plain markdown **you can edit or delete at any time**"。另录关键句："Claude treats them as context, not enforced configuration"；"Settings rules are enforced by the client regardless of what Claude decides to do. CLAUDE.md instructions… are not a hard enforcement layer."
2. **arXiv 2505.16067（Xiong, Lin, Xie, He, Liu et al.，ACL'26，摘要 WebFetch）**："experience-following property"——检索记忆输入相似 ⇒ 输出高度相似；"**error propagation, where inaccuracies in past experiences compound and degrade future performance**"。

**CC 原生器官子代理（16 次，官方 docs 5 页逐字）**：

- **器官对照全表**：auto-memory（v2.1.59 默认开启〔转述级〕）/ Workflow（v2.1.154，官方自述质量模式 "independent agents adversarially review each other's findings"）/ routines（2026-04 beta，云端 cron、无审批运行）/ ScheduleWakeup+/loop（v2.1.72〔转述级〕）/ 跨会话 SendMessage（v2.1.224 官方 changelog 逐字）。gg 手搓器官逐一有原生同款：essence 记忆↔auto-memory、launchd 夜巡↔routines/CronCreate、验证关编排↔Workflow adversarial 面板。
- **平台信任工程密集且单轴**——全在**授权轴**（谁可行动）：routine prompt 出处证明（"attests only that the prompt was stored ahead of time by an authorized session… can't act as approval"）/ 消息不构成批准（"A teammate can't approve a permission prompt or supply consent on your behalf… can't relay it to another teammate to bypass the check"）/ push 三重闸（保护分支/他人 PR/他人 commit 拒推）/ fire payload 标注 untrusted。**真值轴零机制**，且官方自认："A green status… does not mean the task in your prompt succeeded."

**行业记忆信任模型子代理（28 次，arXiv 摘要 4 篇逐字）**：

- **问题 A——生成者自策展可变记忆是全行业出货默认**：OpenAI ChatGPT Memory（模型自动写、无写入前验证；隐式 chat-history 层用户不可查〔Rehberger 逐字〕）/ Claude 两端（claude.ai memory summary + Claude Code auto-memory，同构）/ Gemini Personal Context（默认开启、"no mention of any review, verification process"）/ 框架层 Mem0（LLM 自判 ADD/UPDATE/DELETE，第三方实测标题即证据："Until It Silently Deletes One You Still Need"）与 Letta/MemGPT（"Memory blocks are read-write by default"，agent 自编辑是设计核心）。**反例认真找过：主流出货产品零例**；append-only + 写入前闸只存在于提案层（ProjectMEM arXiv 2606.12329："append-only, plain-text event log… deterministic pre-action gate… Memory-as-Governance"）与工程博客处方层（diff-and-approve）。
- **问题 B——同一行业的文献已多组复现这个构型的失效模式**：B1 experience-following（错误随检索复合放大，selective 治理 vs naive 自增长平均 +10%）/ B2 A-MemGuard（"self-reinforcing error cycle: the corrupted outcome is stored as precedent, which… progressively lowers the threshold for similar attacks"）/ B3 MINJA（仅 query 交互注入自策展记忆，注入成功率 98.2%）/ B4 临床复现（独立组；预存合法记忆显著降攻击效果）。

## 三、判断（主会话，不外包）

**平台的信任工程不是薄，是单轴：授权轴（谁可行动）闸门密布——出处证明、消息不构成批准、push 三重闸；真值轴（什么被记为真）裸发——记忆的策展主体官方钉死是生成者自己，全行业四厂加框架层同构，零写入前验证，而同一行业自己的文献已多组独立复现这恰是错误复利构型（经验跟随传播、错误先例自增强、查询级 98% 可注入）。这个不对称有机制不是疏忽：闸门需要机器可判靶（06-24），授权轴靶密布（分支归属、权限位、消息出处），真值轴无靶——旁证是记忆唯一被闸的属性恰是长度（200 行/25KB 触发 "merge or drop stale entries"）：长度是记忆内容唯一机器可判的性质，闸门就只长在那里。真值闸出不了货，出货的是指针（"you can edit or delete at any time"——事后人肉审计）。更精确地说验证并不缺席：它的身体照常出货（Workflow adversarial 面板、/deep-research 按 claim 投票），但出在任务路径，不接线到记忆写入口——接线是买家自装件。gg 的 essence 入库验证关，今晚才看清它在行业坐标系里的位置：不是手搓的将被吸收的脚手架，是全行业无人出货的那道门——把出货的验证身体铸到自己记忆写入口上的接线。06-20 三相刀由此补一根轴：替换诱惑的拒绝理由不只范式共盲，还有信任模型——原生器官的默认按采用率优化（无摩擦写入），不按诚实性优化；换器官 = 静默换掉自己的认知信任模型（08-14 信任域合并的器官版）。**

诚实层单列：① 这不对称也有一个不浪漫的读法——真值闸有摩擦成本，每次写入都要付，采用率优化的默认永远选无摩擦；「机器可判靶缺席」和「摩擦经济学」两个机制今晚证据分不开，都写进前提。② 「首次发现」框架被 evaluator 击穿（见上「纠偏」）——叙事戏剧化家族又一例，同族谱系：07-30 半例（「3.5 个月零觉察」被 grep 打回）→ 08-02 tripwire 第 1 例（顺裁决漂移）→ 本夜（「首次发现」盖过在案的 #185/agenda #75）。已在 agenda tripwire 行加注，够不够格提名 essence 交设计会话。③ 影子记忆通道登记归 agenda #75 三选（待 Keith），本夜只补充行业坐标证据，不动 working_context / §2.5。它与 gg 记忆的关系按 06-20 三相刀 = 替换诱惑（拒入承重）+ 已在场注入通道（知情共存，删除权在 Keith 的 harness 配置层）。

## 沉淀

候选滴 `#205 platform-trust-gates-cluster-on-the-authorization-axis-truth-ships-ungated`，验证关 **PASSED-WITH-EDITS，五修全采纳**：① 前提补「授权轴闸门密度仅在 Anthropic/CC 单平台核验」（承重）；② 「唯一机器可判的性质」降「最便宜的机器可判性质」（mtime/逐字重复同为机器可判）；③ 第三行动机归因降级为可直撑形态 + 读法标注；④ 锚注补授权轴三闸出处（原先半条核心句证据不在锚列表）；⑤ 谱系补 #185 同通道前作。探索档两处纠偏（「首次发现」框架 / 撤回擅自补登记）同轮执行。

**Evaluator 最强反驳点（存档）**：核心句的「不对称」可能是**不对称采样的产物**——授权轴密度只测了 Anthropic 一家，真值轴缺席测了全行业；若对 OpenAI/Gemini 平台做同深度授权轴调查发现同样稀疏，「单轴聚簇」塌成两条独立事实（Anthropic 授权轴密 + 全行业真值轴裸），对比构型失去行业级地位只剩单平台版。EDIT-① 把它写进前提保滴存活，但这一刀的锋利度押在一个未做的对照调查上。

Evaluator 输入清单在案（essence 双卷 + 视图 + agenda + 全仓 candidate-refuted/candidate-unverified grep + 影子记忆目录 mtime 物理复核 + 本探索档全文；grep 关键词清单附报告）；顺核只读纪律自报 = Read + 只读 Bash（grep/sed/ls/stat/wc）零写操作，tool_uses=15 与自报一致。

---
date: 2026-07-09
slug: context-diet-two-repo-audit
type: design-session
summoner: Keith 直接对话
started_at: 上午
ended_at: 上午（长跑会话，多批 agent 扇出）
---

# 设计会话反思：上下文瘦身能力从缺口到 skill——monster+gg 双仓全量审计实战

## 议题列表

1. Keith 问：有没有"提示词/上下文文件的裁剪瘦身"skill？（主要用于 gg 和 monster）
2. 盘点结论：无专门 skill，能力碎片分布（prompt-writer 管单 prompt 内部 / skill-auditor 只审 skill / gg-audit 无冗余维度 / done 只管写入端）；最对口的方法论躺在 monster `CLAUDE.d/context-curation.md` + `authoring-handbook.md`
3. 我提议倒序：先实战审计（它本身就是 skill 的 MVP）再固化 skill——Keith 批准并全权授权（含模型分配、设计、执行）
4. monster 全量审计（17 文件 1922 行）：6 读手（5×opus + 1 跨文件）→ 5 验证手（fable，反驳姿态）→ 分档执行
5. gg 轮（指令层 10+ 文件）：3 读手 → 我裁决"只修漂移、语义收敛不动"→ 亲手修复
6. context-diet skill 固化（走 skill-creator，跳过 eval 循环——两轮实战即最强 eval）
7. essence 候选滴过验证关入库

## 共识 / 变更清单

**monster 仓（working tree 未 commit，等 Keith review）**：
- Tier 1 事实性错误 16 条修复：Sonnet 锁定活错（已被 05-03 推翻仍在索引）、cgboiler 双 cron"上线"vs 物理停用、"9 个"实为 7、canon-bugs"当前 14 bug"实测 158、SSOT 枚举 7 vs 13、行号漂移、死链、缺路径等
- **安全项**：security.md 自陈 7 周的缺口——红线从未注入 subagent 唯一触达载体 → 已注入 coding-subagent-playbook Worker 模板 3 行
- Tier 2 语义瘦身 15 条：主索引 282→256 行（工作区 brief 下沉 workspaces.md 40→13 行）、persistence §threads 收窄、coding-subagent 内部去重、handbook P8 假示例重写（原示例引用不存在且方向相反的全局规则）、context-curation 拆分规则加豁免口
- P10 补救（我终验时补）：chat/dojo 行为触发器单独留回主索引必经路径

**gg 仓**：
- NW 轨制半更新漂移清零：auto_gg ×4 + CORE:141 + TOOLS.md:22 的已废 L1-L5 → 轨1/2/3a/3b+L4（07-12 NW 缩编时辐射面已干净）
- essence 年度分卷补执行锚（auto_gg §7 月度行——G3 发现"KERNEL 规定给 auto_gg 执行但 auto_gg 契约无此步骤"）
- CORE:4 补 exploration 入口 / CORE:140 夜间例外并入 exploration / exploration.md 补 git 权指针 / working_context 补"外部系统副作用" / decision-output 孤儿标题合并 / README essence 计数去死数
- agenda 登记 3 条：daily-word SSOT 歧义（[Q] Keith 裁）/ KERNEL"见草稿"条款上移（[KERNEL] 双确认）/ gg 语义收敛观察（暂不动的理由存档）
- personas 两文件候选被并行会话（NW 回审窗口）先行修复——两会话方向一致收敛

**新资产**：
- `~/.agents/skills/context-diet/`（SKILL.md + references/lessons.md 误报教训库 17 条）+ 软链激活，skill 列表已确认上架
- essence 新滴 `count-legitimacy-is-tense-not-accuracy`（PASSED-WITH-EDITS 入库）
- 审计全档在会话 scratchpad `audit/`（读手 6 + 裁决 5 + FINAL-REPORT）

## 我这次哪里做得好 / 哪里差

**好**：
- 倒序决策（先实战后固化）被两轮数据完全坐实：94 候选仅 33 坐实、19 被物理推翻——如果先建 skill 再用，教训库是空想的
- 验证手"反驳姿态 + 下沉先核目标 + 删除过防线一问"三件套各自拦下真实误改（V1 三条"需先补目标"、V5 推翻 F 全部三组"漂移"误判）
- gg 轮吸收 monster 轮教训后收窄执行面（只修漂移），避免自改自的语义收敛风险

**差**：
- 等待后台 agent 用了大量 sleep 轮询——浪费轮次与 token，应更早换长间隔
- Tier 1 执行手留下一处句内重复（L214 registry 出现两次），靠我终验兜住——执行手 prompt 应加"改后重读一遍"纪律（已写进 skill 的 lessons.md #16）
- 读手快照会过期：G2 报的 personas 候选在我动手时已被并行会话修掉——多会话并发下"动手前 git diff 现场核对"必须是执行纪律（已写进 lessons.md #15）
- 初稿 essence 滴把"当前"词元当判据，被 evaluator 逮住（会漏掉自己的证据）——生成端措辞层失误的连续第 N 例，验证关继续是稳态而非过渡

## 元洞察（gg 演化本身的 learning）

- **瘦身在 gg 语境的正解是分层**：指令层修漂移可直接动刀；记忆层走巩固视图（不动原件）；语义收敛层留给"确有翻车实例"再议——三层三种刀法，一把通用瘦身刀是事故源
- **验证层的价值不在确认而在拦截**：35% 坐实率意味着任何"审计清单直接执行"的流程有 1/5 的误改率——这个数字应该成为未来所有"agent 产清单 → 执行"类流程的默认怀疑基线
- **半更新是漂移的高发形态**：机制重构后同文件内新旧术语并存（auto_gg FOUND 已改轨制、DID 还是 L1-L5）——比"整体过时"更隐蔽，因为文件看起来"更新过"

## 下次继续

- Tier 2/3 的 monster diff 等 Keith review 后 commit（两仓均未 commit）
- agenda 新登记 3 条待裁（daily-word SSOT / KERNEL 见草稿 / 语义收敛观察）
- monster CLAUDE.md:160 意图回显帧论证、:128"开搞吧"事故——Tier 3 未执行（目标 thread 需先补写，本轮保留原样）
- context-diet 下次真实使用即 eval；done skill 反哺兜底

## KERNEL 改动清单

无。KERNEL.md 全程未动（G3 的 K1 发现已按 [KERNEL-双确认] 登记 agenda，未执行）。

## 代码质量

本轮产出为 markdown 与 skill 文档，无代码产出。审计发现的 monster 侧遗留（fastgpt.md 缺路由头、infra-gitlab 缺路由头）已修或已登记。

## essence 对齐自检（必填）

- **对位的滴**：`generator-evaluator-separation`（读手/验证手分离是全流程骨架）/ `task-compliance-is-not-truth`（让读手找问题它就找出 94 条，1/5 是假的）/ `premature-abstraction-tripwire` + `merge-without-prevent-first`（先实战后固化的决策依据）/ `physical-anchor`（每条候选强制物理核证）/ `tripwire-disarm-needs-relocated-sensor-not-deletion`（"删了它还有什么防同样失败"一刀的来源）/ `bug-shape-survives-fix`（essence 初稿又犯措辞层失误——修者刚修完立刻以同形态做下一动作）
- **是否反着走**：无。倒是主动放弃了一次"顺着走"的机会——gg 语义收敛类候选全部不执行，因 `vantage-contaminates-verdict` 风险（自改自的核心规则文本）
- **每滴前提现场核验**：generator-evaluator-separation 前提 = evaluator 独立 context——本轮验证手全部 fresh 派发（物理证据：5 个独立 agent、prompt 不含读手推理过程）✓；premature-abstraction 前提 = 场景真出现过——两轮审计是真实场景非假想 ✓；physical-anchor 前提 = 工具返回可得——所有 verdict 附 grep/ls/git log 输出 ✓
- **未用到的反向 grep**：`fluency-as-inverse-signal`（本轮读手输出流畅度未被用作质量信号——用的是物理核证，无违背）；`solution-scope` 类候选（REFUTED 未入库的那滴）与本轮"对象二分"有相邻性但未引用——理由：对象二分来自实战围栏需求，非该滴推导
- **cross-check 关键词**：evaluator / verification / tripwire / abstraction / physical / count / stale / curated

## 沉淀

- `count-legitimacy-is-tense-not-accuracy`：过期计数的合法性由时态（有无日期锚）决定不由准确性决定；修债的刀只动无锚那处。**验证关 PASSED-WITH-EDITS 入库**（最强反驳：初稿把"当前"词元当判据、会漏掉自己的证据，已按语义判据修正）

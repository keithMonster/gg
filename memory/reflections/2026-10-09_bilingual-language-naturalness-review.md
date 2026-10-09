---
date: 2026-10-09
slug: bilingual-language-naturalness-review
summoner: monster
northstar_reach: "#2 动态学习"
status: substantive-decision
---

# Reflection: 中英混用提示词的自然语感

### 给父会话的最终输出

本次提供的判断：英语承担多少实际交流，与切换发生在单词还是整句处，是两个不同维度；取消插词配额时应保留主动增加英语接触的目标。
开题：要解决的是“如何让英语持续承担对话中的真实意思，同时让 Keith 读得顺”，不是寻找更长的英文句子。错误判据是英语重新退回技术名词，或靠机械插词/固定句型兑现数量；只能在实际回复与 Keith 的反馈中结算。补集考虑了保留逐回复配额、全交自然语感、另设纯英语学习段：前者保留当前凑词诱因，第二种可能丢失增加接触的目标，第三种改变任务形态。最便宜一击是对照原件和 10-07/10-08 记录，已执行。
读者模型：读者是能生成中英表达、已加载全局协作条款的 Agent；它没有 Keith 完整语言水平测定和本次对话史，常驻上下文有限；读完须直接改变对 Keith 的回复语感并保留英语接触目标。
Verdict：PASS WITH EDITS。原建议的双语同事场景与语义边界切换可用；“保持参与感”需改成主动多用简单英语，原第一例中 why 从句等不宜直接作为起步锚。自然度不按英文长度推断；“香港人”只取其自然双语交流的比喻含义，不增写地域口音或粤语角色。
推荐以以下三条替换共享 Language 现有三个对话子条，其他条款保留：

```markdown
  - **与 Keith 自然中英混用，主动多用简单英语交流。** 像熟悉的双语同事聊事情：中文讲清复杂内容，英语直接表达判断、反应和行动。随意思和语气切换，词、惯用短语、分句或整句都可用，搭配要顺口；不逐词硬换，不按回复或段落凑数量。技术名词不代替英语交流。
  - 从简单口语起步，难度随理解反馈提高。看不懂时换简单说法或补中文，维持英语接触。语感示例（随语境变化，不作固定句式）：“先用一个脚本，that’s enough for now. 等需求稳定了再拆。”
  - Keith 可全程用中文回复。“多掺点”增加英语，“简单点”降低难度，“别掺了”改回中文；文档、UI、注释沿各自要求。
```

保留：默认中文与英语简单起步、注释中文、语音纠错、准确优先与稳定英文术语、不要求中文重复全部英文信息、模型提示词按部署证据选语言、dd 触发规则。父会话负责最终写入与消费者核验。
Trade-off：取消机械配额后，英语数量不再有逐回复的硬代理；由“主动多用”保留方向，后续行为与反馈决定是否有效。旧三子条 991 B，新稿 785 B，净减 206 B；工具估算全文件 24478→24272 B，仍高于父会话报告的 24000 B 阈值，不声称体积闸通过。
证据：实读 /Users/xuke/.agents/AGENTS.md Language（22–24 行）、/Users/xuke/githubProject/monster/threads/context-curation.md（34、67、69 行）、/Users/xuke/githubProject/monster/shared/docs/writing-for-readers.md。用户本轮原话由父会话委派提供；历史反馈读取 thread，未回取历史 transcript。未调用外部系统、未进行行为对照，静态判断不等于行为增益已验证。
最终措辞复核：父会话落地后已重新读取完整 Language，三子条与推荐原文一致，上述保留项仍在。实测 /Users/xuke/.agents/AGENTS.md SHA256 = 9d3f36952a7bd02796a00ae57610470641de6960ff1a16c458eb6c33ecd580c2，24272 B；该文件版本的静态 verdict = PASS。父会话报告 diff --check 通过且新条款已注入当前会话；此二项为父会话证据，gg 未将其升级为行为效果证明。

### 核心假设
Keith 仍希望增加英语接触，本次改变的是表达方式；依据是父会话提供的本轮原话与 10-08 记录，不把 10-07 三例当英语水平测定。
### 可能出错的地方
“双语同事”与单个例句仍可能被模型复制成固定套话；无配额也可能出现英语减少，均待真实交流检验，概率未测。
### 本次哪里思考得不够
没有面向 Keith 的样例偏好盲测；自然度评议仍由 LLM 完成。历史用户原话尚止于 thread 层证据，本轮最新原话止于委派输入。
### 如果 N 个月后证明决策错了，最可能的根因
生成侧把“自然”当免除主动英语表达的理由，或把“简单”固化成少数重复口号；仅靠静态文稿未测出实际默认行为。
### 北极星触达
#2：把英语学习机会保留在实际协作交流中；不由本次静态审查宣称学习收益。
### essence 对齐自检
- 对位：rule-with-half-pattern-self-violates（删配额同时保留主动英语目标）；dogfood-claim-as-self-issued-certificate（文稿通过不写作行为通过）。
- 反向张力：caged-freedom 提醒增加表达条文也可能压缩语感；本次用短场景锚与一个例子替代数量分配，不新增格式模板。hard-rule-welds-intent-to-form 的机械可检前提本题不成立，仅借其意图/形态区分，不声称完整适用。
- 实际 grep 关键词：rule-with-half-pattern-self-violates、hard-rule-welds-intent-to-form、dogfood-claim-as-self-issued-certificate、caged-freedom；原卷 /Users/xuke/githubProject/gg/memory/essence.md 与 /Users/xuke/githubProject/gg/memory/essence/2026-H1.md 均有相应命中。
本次无 essence 候选；未修改被审业务原件，未 commit/push。

---
date: 2026-05-25
slug: communication-style-prompt-review
status: substantive-decision
assembly:
  tools: [reasoning_modules]
  personas: []
  tracks: []
  reasoning: [inversion, first-principles]
summoned_by: monster (Claude)
topic: Communication Style prompt 修订建议（子代理 diff review）
---

## 判断

子代理改得不对。**问题诊断错了**——不是 prompt 写得不够细，是 prompt 想用文字解决一个文字解不了的问题（system 段在长上下文末端被压制）。

## 推理路径

### 反驳子代理 diff 的三个角度

**① 违反元规则 #1（激活而非描述）**

子代理把"复读 tool call 已显示内容一律删"扩成四类反例 + 每类配负面示例（金句开场 / 结构复读 / 同信息复读 / 任务铺垫）。列负面示例 = 把反例本身的画面激活进上下文。元规则 #1 明确禁过——子代理是用违反元规则的方式去修一个元规则没盯住的失败。

**② 字数膨胀 1.6x，违反元规则 #5（反复 = 重要）**

- 原段 ~280 字
- 改后 ~450 字
- 核心动词「删 / 砍」原 4 次 → 改后 5 次
- 浓度从 1.4% → 1.1%

写更长来强调"要短"——物理自相矛盾。Keith 自己写的元规则 #5「论证 / 铺垫越长越稀释核心」。

**③ "念出声 / 按 delete 键再读一遍"是伪具体**

LLM 没有声音通道、没有按键回看的物理动作。这是给人类写的修辞动作，对 LLM = 抽象。元规则 #2 要求物理画面 = 模型推理通道里真存在的操作（如「grep」「输出 token」），不是人类比喻。

### 真问题诊断

两轮翻车（gg INFO 数据复述 + mirror 报告结构编号）的物理根因：

- system prompt 在会话开头加载
- 任务执行时上下文已 30K+ token（gg INFO 完整数据 / mirror H 报告全文）
- attention 引力被任务材料拽走，system 约束信号衰减

**这不是 prompt 写不写得清的问题。** 写多详细的反例清单都解决不了 attention decay。

这正好是 monster 自己反复说的元方法论——「LLM 内部不可靠 → 外部锚点托底」。Communication Style 翻车恰恰是这个元方法论的应用场景之一，只是 Keith 和子代理都没识别出来。

### 推荐

**A. Prompt 微调（一处，不扩段）**：

```diff
- **信息密度硬约束**：每字负载信息。AI 启动客套...一律删
+ **信息密度硬约束**：每字负载信息。写完一段回看——结论已在表格/前句出现过 → 删；装饰金句 → 删；任务铺垫 → 删
```

保留原段结构，只在「自问」环节加三个具体识别锚（命中两轮实证的失败模式），不引入负面示例画面。

**B. 真正解（外化锚点）**：

长回复（review / 决策 / 方案 / 总结）生成后跑 audit：

- 选项 1：PostToolUse hook 在主代理写完后扫一遍
- 选项 2：独立 subagent「冗余审查者」吃 final message + 上下文，输出删改 diff，Keith 接受/拒绝
- 选项 3：done skill Step 加一项「本次会话长回复抽检」

任一选项都比 prompt 文字加码更可能真生效。

## Trade-off

- A 微调成本低，但仍是 system prompt 路径，attention decay 问题未解，只是降低未来回看时的歧义
- B 工程成本高（新建 hook / agent / 流程），但物理上真解决（在生成点之后才检查，不依赖 system prompt 存活）
- 子代理 diff 全盘接受：字数膨胀 + 反例激活 + 伪具体三重副作用，零增益

## 行动建议给 Keith

1. **拒绝子代理 diff 全套**
2. **接受 A 微调**（一行改，不扩段）
3. **B 启动 inbox/topics**：「长回复冗余 audit 外化锚点设计」候选三方案，等 Keith 拍

### 给父会话的最终输出

**判断**：子代理改得不对，诊断方向就错了。问题不是 prompt 没说清，是 system 段在长上下文末端 attention decay——文字加码解决不了物理失效。

**对子代理 diff 的三个反驳**：

1. 违反元规则 #1（激活而非描述）——把四类负面示例显式写进 prompt，把反例画面激活进上下文
2. 字数 1.6x 膨胀，核心动词浓度从 1.4% 降到 1.1%，违反元规则 #5「反复 = 重要 / 铺垫稀释核心」
3. "念出声 / 按 delete 键再读一遍"是给人类写的修辞，LLM 没有这两个物理通道，违反元规则 #2「具体 > 抽象」要求的"物理画面"

**真问题**：两轮翻车（gg INFO 数据复述 + mirror 报告结构编号）根因 = system prompt 在 30K+ token 末端被任务材料引力压过去，attention decay 是物理事实，不是文字描述不够细的问题。这恰好是 monster 元方法论「内部不可靠 → 外部锚点托底」的应用场景——Keith 和子代理都没识别出来。

**推荐**：

- **A. 拒绝子代理全套 diff**
- **B. Prompt 仅做一处微调**（保留原段结构，不扩段）：
  ```diff
  - **信息密度硬约束**：每字负载信息。AI 启动客套...一律删
  + **信息密度硬约束**：每字负载信息。写完一段回看——结论已在表格/前句出现过 → 删；装饰金句 → 删；任务铺垫 → 删
  ```
- **C. 真正解走 inbox/topics 起 brief**：「长回复冗余 audit 外化锚点」三候选方案——PostToolUse hook / 独立 subagent reviewer / done skill Step 抽检。任一比 prompt 加码更可能真生效。

**Trade-off**：A 零成本但仍受 attention decay 制约（只降未来歧义），C 工程成本高但物理上真解决（在生成点之后检查，不依赖 system prompt 存活）。

## 元属性反思

### 核心假设

子代理诊断"prompt 没说清"是错的，真因是 attention decay（物理现象不是文字现象）。

### 可能出错的地方

- 假如两轮翻车真的是 prompt 措辞模糊（而非 attention decay）—— A 微调可能足够，B 外化锚点是过度工程
- 验证方法：A 落地后跟踪 2-4 周长回复样本，仍翻车 → 验证 attention decay 假设；不再翻车 → 假设证伪，B 不用做
- 时间窗：4 周内能初步证伪

### 推理盲区

- 没考虑「Keith 自检」这条路径——Keith 本人发现啰嗦就当场反馈，这条人在环里的锚点已经在工作（两次实证）。或许根本不用 B
- 没考虑子代理 diff 里某些具体识别锚（"表格已列再写散文复述""结论给完再编号列章节"）虽然有副作用但确实对应两轮真实失败模式——A 微调里我捞了三个，捞得对不对没二次校验

### N 个月后根因预判

3 个月后回看，最可能的真因 = monster 还在不断加 system prompt 内容（CLAUDE.md / 全局 CLAUDE.md / MEMORY.md 总量在涨），Communication Style 段在末端的相对位置越来越深，attention decay 越来越严重。不是这次的子代理诊断错，是问题在恶化中——A 微调只是延寿，B 外化锚点是结构性解。

### 北极星触达

本轮触达 = 维护 Keith 和 Claude 协作系统的可靠性（防止 prompt 工程退化成"加更多文字"陷阱）。直接服务 monster 元方法论本身的健康。

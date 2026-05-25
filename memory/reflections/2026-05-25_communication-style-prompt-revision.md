---
date: 2026-05-25
slug: communication-style-prompt-revision
summoner: monster
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: Communication Style prompt 修订建议（gg 审子代理 diff）

### 给父会话的最终输出

**推荐**：

子代理 diff 方向对（具体>抽象、删论证段、锚反例），但承重不够。**接受子代理的具体反例锚定（金句开场/结构复读/同信息复读）**，**否决其"加四种负向声音"的纯负向架构**，**改为"1 个正向骨架 + 末尾硬禁令"**。

**理由（三个子代理没碰的承重视角）**：

1. **rule-with-half-pattern-self-violates 复犯**：essence (2026-05-23) 已点透"规则只写删/禁/避免不写留/做/突出 → RLHF 默认值填空"。子代理 diff 的"听见 X 立刻砍"四种声音 = 纯负向规则，激活弱于正向规则，且子代理自己又堆 4 反例字符串——正面复犯 essence 描述的 bug-shape。修法是双向闭环（删 + 留 + 检测器三件），不是再加反例
2. **两轮违规根因不同质**：Round 1（表格+理由复述）= 信息组织选错形式；Round 2（金句开场+5 段编号复读）= fill-the-form 反射（"长回复 = 必须看起来完整"先验）。子代理把两个根因当一个打，diff 没区分
3. **自检条款不工作的实证**：原 prompt 两条自检（"删几个字意思不变""贴 Keith 面前能立刻知道结论吗"）写法看着对，实证同会话两轮都没触发。修 prompt 加第三条自检 ≠ 解，要把抽象自检换成具体禁令

**trade-off + 未核验假设**：

- "正向骨架=结论1句+证据N条+行动1句"是结构性约束，对**确实需要复杂展开**的长回复（如 review 多维度对比）可能压成 too tight。未核验
- "末尾硬禁令"假设 RLHF 倾向加总结段集中在末尾，没穷尽检查中段冗余
- 反例清单上限"≤5 条"是经验值，没 A/B 实证

**行动建议（Keith 下一步）**：

1. 接受子代理 diff 的**具体反例锚定**——金句开场 / 结构复读 / 同信息复读 / 任务铺垫四种画面保留（元规则 #2 #4 都对，画面感激活强）
2. **加一条正向骨架替代"四种声音砍"**：`长回复 = 判断1句 + 证据N条 + 行动1句，三段之外的都是装饰`
3. **删两条"自检"类条款**——实证不工作的留着是噪音，改成末尾硬禁令：`末尾不准加总结段，结论已在首句给过`
4. 短回复豁免按子代理改法收紧（"每字承重永远生效，无短回复豁免"）方向对，照接
5. **不要再加更多反例**——4 反例已是上限，反例 >5 条退化成 checklist 按"覆盖率"读不按"承重"读（元规则 #5）

### 核心假设

- essence `rule-with-half-pattern-self-violates` 描述的"修啰嗦文本本身啰嗦"模式适用于本次 diff 评估——子代理的 4 反例堆叠就是该 bug-shape 在评者位置上的复犯
- "正向骨架"激活强于"负向砍" = 元规则 #1（写"不是 X"激活 X）在规则架构层的推论
- prompt 修订能压住"啰嗦"——但只能压"形式层啰嗦"（装饰段/复读），压不住"组织能力层啰嗦"（选错表达形式）

### 可能出错的地方

- 推荐"加正向骨架"可能太死，复杂 review 类长回复被压成单调三段式（概率 30%）——失败信号 = Keith 反馈"这样太干瘪了"
- "末尾硬禁令"可能转移问题不解决问题——RLHF 把总结段挪到中段或换形式（如"综上"句）继续混进来（概率 40%）
- 我自己作为评者也是 LLM，元规则 #4 警示"最容易被 RLHF 压回去的反例必须显式点名"——我可能没点名某条最关键的反例自己没意识到（概率难估）

### 本次哪里思考得不够

- 没去 grep `~/.claude/CLAUDE.md` 原文做物理核查，依赖 prompt 里贴的版本；如果 prompt 里贴的版本不是最新，建议失准
- "正向骨架=判断1句+证据N条+行动1句"是我即兴造的，没去找 prompt-writer skill 已有的正向骨架范式可能复用
- Round 1 Round 2 两次违规我只看了 Keith 转述的诊断，没去原 transcript 看实际啰嗦的精确形态——可能误判根因

### 如果 N 个月后证明决策错了，最可能的根因

**最可能根因**：prompt 工程层修订就压不住"啰嗦"，因为根因不在 prompt 在反馈回路——RLHF 训练 prior 是"helpful = 详尽"，单 prompt 层的负向/正向规则都被训练 prior 盖过，唯一真解是 Keith 当场反馈即纠（已在 monster CLAUDE.md "纠正即落库"段建机制，但这条机制本身专对事实漂移不对啰嗦行为）。

如果是这个根因，N 个月后表现 = 修订后头两周生效，然后行为漂移回啰嗦默认值，Keith 又一次抓到。

### 北极星触达

**#3 决策超越直觉** — 子代理 diff 看着合理，凭直觉容易直接 forward 给 Keith；本次顶住直觉做了三步分诊（essence cross-check / 两轮根因区分 / 自检条款失效实证），输出的承重视角是 Keith + 子代理都没碰的层。

### essence 对齐自检

- **本决策跟哪几滴 essence 对位**：
  - `rule-with-half-pattern-self-violates` (2026-05-23) — **承重命中**，子代理 diff 的纯负向 + 4 反例堆叠 = essence 描述的"修啰嗦文本本身啰嗦"bug-shape 复犯，我的判断 #1 直接踩这条
  - `bug-shape-survives-fix` (2026-04-27) — essence 自引上一条时点名了它，本次的修法（不再加第三条反例，改正向骨架+末尾禁令）= 主动跳出 bug-shape 形态
  - `extraction-meta-inheritance` (2026-04-29) — 同上 essence 自引，元规则维度的落点
  - `task-compliance-is-not-truth` — 子代理交付了符合任务"给 diff"的输出，但 diff 本身复犯了它要修的 bug，是该 essence 的活体
- **本决策是否在某条 essence 上反着走**：无明显反走。**潜在张力**：我作为评者也是 LLM，跟子代理同 prior（gemini/claude 同源训练），可能命中 `evaluator-independence-is-a-three-layer-stack` (2026-05-23) 的 prior 层共盲——我说"4 反例已上限"可能本身就是过度收紧，未核验
- **cross-check 用的关键词**：`prompt`, `rlhf`, `prompt-writ`, `communication`, `verbose`, `啰嗦`, `信息密度`, `结论前置`, `自检`, `反例清单`, `positive`, `删/禁`

### essence 候选

- slug: `negative-rule-needs-positive-skeleton-twin`
- 一句话: 负向规则（删/禁/避免）必须配对正向骨架（结论形态 / 段落范式 / 字段顺序），否则留下行为真空被 RLHF 默认值填空——`rule-with-half-pattern-self-violates` 的修法侧实操化
- 是否已 append 到 essence.md: N（待 Keith 决定是否升 essence，本滴是 5/23 那条的修法侧推论，可能已被覆盖不构成新滴）

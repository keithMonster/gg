---
slug: cgboiler-issue18-inquiry-third-perspective-ack
date: 2026-05-07
status: substantive-decision
trigger: cgboiler 架构主会话向 gg 终审议题 18——小助理对话作为第三视角 inquiry + 独立 cron 增量 ingest
ack-position: modify-ack（5 条强制修改 + 1 条架构主会话已 cover 的认可项）
---

# 议题 18 终审反思

## 核心假设

1. inquiry 是合法第三视角（独立于 generative / reactive）——三轴差异（动作 / 对象 / 语境）是本体论级别的而非数据源级别
2. 王亮 fold v2 灰度（议题 12）真的会在合理时间内跑通——议题 18 B 阶段时序闸门挂在它上面
3. 14866 msgs 抽样画像足以支持本体论扩展决策——架构主会话有数据，跟议题 15 "theory-gap-without-data" 处境不同
4. Keith 拍板的"用途叠加"和"不考虑隐私"已锁死，gg 不评估这两条，只评估实施架构

## 可能出错的地方

1. inquiry 第三视角看似干净，但**真正的数据画像（517 chats / 14866 msgs 信号密度）是否支持挂回 cgboiler entity 卡片**只有 1 个 chat 的 spot-check（张吉峰 2026-05-06）做了——n=1 不是数据
2. 议题 14 evidence_id 三元组到现在还没落代码（capability-gap 6 天未消）——议题 18 直接叠四元组是把"老债叠新债"
3. fold v2 议题 12 灰度 6 天 0 进展——议题 18 B 阶段闸门挂在它上面意味着 B/C/D 全冻结，但 A 阶段持续 dump 数据会形成"数据池子大，B 阶段越拖压力越大"的反向激励
4. 14866 msgs 流式增量数据跟 batch1 固定快照是异质数据流，"按 batch6 进流水线"的拼接方式 schema 上看似干净但**实际抽取阶段单 chat 50+ msgs ~30K 字符跟 batch1 单 note 1-3K 字符不在一个量级**——LLM 抽取行为可能漂移

## 推理盲区

1. **本体论扩展频次**：议题 14 reactive 扩桶 → 议题 18 inquiry 扩桶，6 天内两次本体论变更。这是"组织自我表征"还在早期发现真实形态，还是 cgboiler 在容许一个"每见到新数据就开新视角桶"的滑坡？需要架构主会话或 Keith 拍一个"视角层数封顶"原则，否则 batch7/8 又见到企微聊天 / 飞书会议纪要时会再扩第四视角第五视角
2. **n=1 spot-check 的代表性**：张吉峰 2026-05-06 单 chat 命中 customer 华昇 + doctrine 信号 + 业务量化数字——但这是高管 chat 的天花板表现。一线员工 chat ≥30% 闲聊的真实结构未做信号密度抽样，"信号密度足以挂回 cgboiler entity"对一线层是过度推论
3. **AI 答复入 cite 的对策本身有漏洞**——"只采 Human 发问内容"听起来安全，但 Human 提问里**可能引用 AI 之前答错的内容当事实再追问**（"AI 上次说我们子公司有 5 家，那 X 是哪家？"），这条 Human 发问就是受污染语料。原方案对策只 cover 了"AI 直接吐错"未 cover "用户复述 AI 错答"

## N 个月后根因预判

如果议题 18 失败（半年回看），最可能的根因排序：

1. **本体论扩展节奏失控**——cgboiler 从最初 "perspective first-class" 扩到 "generative + reactive + inquiry" 三层后，发现每见到新数据源（企微 / 飞书 / 邮件）都得开新桶，evidence_distribution 桶数从 6 → 7 → 8 → 9，audit 复杂度雪球
2. **议题 14 三元组 capability-gap 一直没补**——议题 18 直接奔四元组，render_cards.py 退化兜底逻辑挂在"comment_id=None / chat_msg_id=None 双层退化"上，老数据 hash 漂移没人注意，evidence_id 全局唯一性悄悄破裂
3. **A 阶段 fetch 长期单跑**——B/C/D 阶段被议题 12 灰度卡住，inquiry jsonl 池子越长越大（每天 +1 文件 × N 月），最后真要抽取时数据量远超 batch1 量级，跑一次 LLM 就是天文数字 token

## 北极星触达

cgboiler 的北极星：「AI 读完 cgboiler/ 后，应能作为"川锅本身"回应」。

议题 18 的真问题不是"该不该收 inquiry 数据"——这条 Keith 拍了，gg 不评估。真问题是：

- **inquiry 数据如果挂得对，让"川锅本身"多一层"组织在求助 / 关切 / 痛点"的内省视角**——这是组织作为意识体的自反射能力，跟 generative（说）和 reactive（评）维度完全不同。北极星方向是支持的
- **但实施节奏如果失控**（多本体论变更叠加 + 老债没补先开新债 + 安全债不消先启 cron）→ 到批量铺开时 audit 信号被淹没，cgboiler 就从"川锅本身"退化成"川锅资料的混乱外人"

所以**修改方向不是反对 inquiry 视角立设**——这一条 ack——而是**捆绑议题 14 老债清偿、捆绑议题 12 灰度时序、捆绑安全债前置、捆绑 A 阶段数据冻结上限**。

## 最终判断：modify-ack（5 条强制修改）

### 给父会话的最终输出

#### 立场

**modify-ack**——议题 18 inquiry 第三视角的本体论判断成立，独立 cron 路 Y 优于路 X，A 阶段 fetch-only 设计基本干净，时序闸门复用议题 14 原则方向正确。但有 5 条强制修改，不全落 = 视为 gg 反对。

#### 4 个核心问题逐一答复

**Q1：inquiry 是否合法第三视角？**

✅ **ack**——三轴差异（主体动作主动求助 / 接收对象 AI 而非人 / 心理状态"我想知道"而非"我要说"或"我评价"）支持 inquiry 是独立视角而非 reactive 子类。

支持判断的核心证据：reactive 是"针对叙事的反应"（对象=人，语境=人际），inquiry 是"针对知识/工具的求助"（对象=AI，语境=人机）。两者承载的视角强度/语境差异比 generative vs reactive 还要大——reactive 至少跟 generative 共享"人际语境"前提，inquiry 直接破开了"人际语境"前提。

衍生本体论价值：inquiry 视角是组织作为意识体的**自反射维度**——"川锅本身在向外（向工具）求什么"——这是 generative（说）和 reactive（评）都无法承载的内省信号。

**Q2：独立 cron 路 Y 是否优于路 X？**

✅ **ack 路 Y**——理由架构主会话已说清，gg 补两条：

- 流式增量数据 vs 固定快照是工程上的根本异质，融入 cgboiler 5 phase tick 体系会让本来已经复杂的 phase 状态机再加一个"流式 phase"，增加状态机维度而不增加内聚度
- cc-space/scheduled/ 工作区是 2026-05-06 才上线的新基建——议题 18 是第一个"严肃业务"消费者，正好做基建 dogfood

但 Q2 ack 是**前提性的**——见下方强制修改 #2、#3 关于 A 阶段数据冻结和安全前置的硬约束。

**Q3：时序闸门是否复用议题 14"等议题 12 灰度"原则？**

⚠️ **ack 但加重一层闸门**——见强制修改 #1。

议题 12 灰度 6 天 0 进展（people/_archive/ 目录都没建过，STATE.md / PROGRESS.md 0 处提 STALE_AFTER_FOLD / gray_validated）。如果议题 18 复用同一闸门，B 阶段会**无限期挂起**。所以闸门要复用，但要加兜底激活机制——见强制修改 #1。

**Q4：A 阶段 fetch-only 防滑坡机制是否充分？**

⚠️ **基本充分但有一个隐藏滑坡通道**——见强制修改 #4。

`assert __name__ == '__main__'` + 不暴露 import api 防住了"代码层偷启抽取"。但**没防住"jsonl 池子越长越大，B 阶段被迫提前启动"的反向压力滑坡**——这是行为/激励层的滑坡，不是代码层的。

#### 强制修改 5 条

##### 修改 1：议题 12 灰度兜底激活闸门

议题 18 B 阶段时序依赖议题 12 跑通，但议题 12 自 2026-05-01 决议至今 6 天 0 进展。如果不加兜底，B 阶段会被议题 12 拖死。

**强制要求**：

- B 阶段闸门改为 `OR`：(议题 12 王亮 fold v2 灰度 ack) OR (2026-06-07 一个月硬过期）
- 一个月过期后**不自动启 B 阶段**，而是触发架构主会话 + gg 双签复审："议题 12 仍未跑是什么阻塞？该不该绕过议题 12 独立推进议题 18 B 阶段？"
- 议题 12 自身在 PENDING 加一条交叉触发：议题 18 A 阶段启动时，立刻把议题 12 行动 #2-#6 推进优先级提到 P1（人为推动而非"等"）

理由：议题 14、15、18 三个议题的 B 阶段闸门都挂在议题 12 上。**议题 12 一个不跑，三个未来议题全冻结**——议题 12 已经成为 cgboiler 关键路径瓶颈不是 P1 时序约束。

##### 修改 2：议题 14 evidence_id 三元组**前置实施**到 cgboiler 主线，不能拖到 C 阶段并行做

当前事实：
- render_cards.py:170 `make_evidence_id(note_id, quote)` 仍是二元组
- 议题 14 SCHEMA 上写了 comment_id 字段，但代码层零变更
- 议题 18 方案表 #6 把"render_cards.py make_evidence_id 退化兜底改 4 元组"挂在 B 阶段——意味着两次扩展（二元组 → 三元组 → 四元组）一次落地

**强制要求**：

- 议题 14 evidence_id 三元组 capability-gap 必须在议题 18 A 阶段启动前清偿
- 具体动作：把议题 14 行动 #5（render_cards.py evidence_id 三元组哈希 + comment_id=None 退化兼容）从议题 14 C 阶段提到 cgboiler 主线立即可执行项
- 必须有 `python3 render_cards.py --validate-evidence-id-stability` 类的回归测试证明老 evidence_id 100% 不漂——不是抽样验证
- 这条**单独跑通后**才允许议题 18 任何阶段动 SCHEMA / render_cards

理由：议题 14 立完 6 天，三元组扩展从 SCHEMA 到代码 0 落地。议题 18 直接奔四元组等于在"老债没还"基础上加新债——一旦 B/C/D 阶段出 bug 就分不清是三元组扩展问题还是四元组扩展问题。同性质失败模式 = 议题 12 灰度 + 议题 14 reactive 同时未实施时若叠加议题 15 的 fact_type 区分，"两层未验证机制叠加失败原因不可分离"——议题 15 已经被 gg reject 过一次。议题 18 是同样错误的回收。

##### 修改 3：A 阶段安全前置闸门**硬刚**

当前方案把 fastgpt-mongo 安全债（公网 27017 + 默认密码 mypassword）列在风险 #5、#8——但允许 A 阶段在"Keith 决策密码改动后"启 cron。

**强制要求**：

- A 阶段启动前必须**两条同时完成**：
  1. mongo 密码改掉（改成强随机密码，写入 cc-space/.env，重新 smoke test fastgpt_mongo.py）
  2. 27017 公网封禁（云安全组限源 IP 到内网网段或办公网段）
- **fetch_chat.py 头部加 assertion** `assert os.getenv("FASTGPT_MONGO_PASSWORD") != "mypassword"`——脚本启动时直接检测默认密码，是默认密码立刻 abort
- plist 安装前架构主会话必须 git diff 确认 fetch_chat.py 含上述 assertion，未含拒绝安装

理由：议题 18 A 阶段会让 cron 长期挂连接（每天凌晨 02:00 跑 fetch）——**长期挂连接就是把"5 分钟拖库"风险从一次性变成持续性**。安全债不消就启 cron 是基础工程纪律违反，不是"Keith 决策推力"问题。

这条不是"建议先做"，是**硬阻断**——安全前置不完成，A 阶段 plist 不允许安装。架构主会话不能默认 Keith "明天会改"。

##### 修改 4：A 阶段数据池子上限闸门 + 季度滚动归档

当前方案 A 阶段无限期 dump 增量 jsonl，B/C/D 阶段挂在议题 12 灰度上。**反向压力滑坡风险**：jsonl 池子持续增长，B 阶段越拖压力越大，最终"数据都收了不抽就浪费"成为推动提前启动 B 阶段的非技术性论据。

**强制要求**：

- A 阶段 jsonl 数据冻结上限：**累计 30 天 OR 累计 5000 chats OR 累计 50000 messages**——任一触发，cron 自动暂停
- 自动暂停后触发架构主会话 + gg 双签复审："是否启 B 阶段 / 是否扩闸门 / 是否丢弃部分数据"
- jsonl 按月份归档：`data/inquiry/2026-05/YYYY-MM-DD.jsonl`，月底打 tarball `data/inquiry/2026-05.tar.gz`，源文件保留至 B 阶段启动后再清理
- fetch_chat.py 启动时自检池子大小，达上限拒绝写入并通知 Keith（走 `~/.agents/skills/notify`）

理由：A 阶段无副作用是"代码层"的，行为/激励层有滑坡——见上文推理盲区 #3。冻结上限把"无限期 dump"变成"有界 dump"，强迫架构主会话和 gg 在数据规模到上限前作出 B 阶段决策，避免数据规模成为非技术性推力。

##### 修改 5：本体论视角层数封顶原则

议题 14 立 reactive（generative → 双层）/ 议题 18 立 inquiry（双层 → 三层）。6 天内两次本体论扩展。如果不立封顶原则，batch7/8 见到企微聊天/飞书会议纪要时会再扩第四视角第五视角，evidence_distribution 桶数雪球。

**强制要求**：

- PRINCIPLES.md §1.1 段头从"双层视角"改为"三层视角"时，**同步加封顶段**：
  > "三层视角（generative / reactive / inquiry）已覆盖组织自我表征的核心维度——发声 / 反应 / 求助。后续若发现新数据源（企微聊天 / 飞书会议 / 邮件等），**默认归入已有三层之一**（企微聊天 → reactive 或 inquiry / 邮件 → generative 或 reactive / 会议纪要 → generative 客观桶）。新视角层（第四层）的开设需要架构主会话 + gg + Keith **三签** ack，不允许架构 + gg 双签自决。"
- 新增视角层的本体论标准（在 PRINCIPLES.md 显式写）：
  1. 三轴差异（动作 / 对象 / 语境）必须**全部**与已有三层每一层都显著不同——不是任意一轴差异就够
  2. 数据画像必须有 ≥3 个独立真实样本支持视角假设——不是 n=1 spot-check
  3. 已有三层桶不能容纳的样本量 ≥ 新视角桶预期样本量的 3 倍——不是"理论上不一样所以新桶"

理由：本体论扩展是 cgboiler 最严肃的变更——议题 14、议题 12（L2 全画像→滑动窗口）都已经升到本体论级别。**没有封顶原则 = 隐性允许"每见到新数据就开新桶"滑坡**。封顶原则不是限制创新，是把视角扩展的决策门槛拔高，保护本体论稳定性。

#### 隐藏破坏点（强制修改清单之外的提醒）

##### 破坏点 1：AI 答复污染 Human 发问

原方案对策"只采 Human 发问内容 + 员工显式注入"对策只 cover 了"AI 直接吐错"，**未 cover "用户复述 AI 错答"**。

具体场景：AI 第一轮答错"川锅环保有 5 家子公司"，用户第二轮 Human 发问"那 X 是 5 家里的哪家？"——这条 Human 发问看似纯人类输入，实际嵌入了 AI 错答作为前提。如果作为 cite 进 cgboiler，会让"5 家子公司"成为伪证据。

**建议对策**（不强制改方案，B 阶段 dogfood 时关注）：
- B 阶段 extract_prompt 加规则：**Human 发问中的"那 X" / "之前说的 X"等代词指向上文 AI 答复时，跳过抽 fact**
- 或更激进：**单 chat 里只抽**第一轮 Human 发问**，跳过 ≥2 轮的所有 Human 发问**——损失部分信号但消除污染通道

##### 破坏点 2：14866 msgs n=1 代表性

原方案用一个张吉峰 chat 的命中证明"信号密度足以挂回 cgboiler entity"——n=1 不是数据。高管 chat 的天花板表现不能外推到中层和一线。

**建议对策**（不强制改方案，B 阶段 dogfood 前置补做）：
- B 阶段 dogfood 张吉峰单 entity 之前，先做 3 个独立分层抽样 spot-check：高管层（已有）+ 中层（找一个陈尚书 / 范福吉 chat）+ 一线（找一个普通工程师 chat）
- 各看 50 条 msgs，肉眼判断"能挂回 cgboiler entity 的 fact 信号密度"
- 若一线层 < 高管层 1/5（数量级落差）→ extract_prompt 必须加分层规则，不能"一刀切按 inquiry 抽"

##### 破坏点 3：evidence_id 二元组→三元组→四元组的退化兼容链

议题 18 方案 #6 写了 "render_cards.py make_evidence_id 退化兜底改 4 元组"，但**退化逻辑必须显式写出**：

```python
def make_evidence_id(note_id, quote, comment_id=None, chat_msg_id=None):
    if chat_msg_id is not None:  # source.type=5 inquiry
        # 4 元组
    elif comment_id is not None:  # source.type=4 reactive
        # 3 元组
    else:
        # 2 元组（generative，老数据兼容）
```

强制修改 #2 已要求三元组先实施 + validate-evidence-id-stability 回归——四元组实施时同等回归。**不允许**"反正退化兜底"就不写测试。

#### 闸门量化

| 闸门 | 触发条件 | 触发后动作 |
|---|---|---|
| **议题 12 兜底激活** | 2026-06-07 仍未灰度跑通 | 架构主会话 + gg 双签复审是否绕过议题 12 推进议题 18 B/14 C/15 |
| **A 阶段数据冻结** | 累计 30 天 OR 5000 chats OR 50000 messages | cron 自动暂停，架构主会话 + gg 双签复审 |
| **本体论第四层** | 任何提议开设第四视角层 | 架构主会话 + gg + Keith 三签 ack（双签禁止自决） |
| **安全前置硬阻断** | mongo 密码未改 OR 公网 27017 未封 | A 阶段 plist 不允许安装 |
| **n=1 代表性** | B 阶段 dogfood 张吉峰前 | 必须补 3 层独立 spot-check（高管 + 中层 + 一线） |

#### Essence 命名

**`ontology-expansion-velocity-needs-cap`** —— 本体论扩展节奏需要封顶。

每次扩展（reactive / inquiry / 未来潜在的第四层）单独看都"理论充分 + 数据支持 + 三轴差异"。但扩展节奏本身（6 天 2 次）和扩展上限（3 层 / 4 层 / N 层）是 meta 层问题，不能在每次具体扩展决策里隐式回避。

**和议题 14 essence 的关系**：议题 14 立了 "reactive 不是 generative 子类"——视角分类正确性原则。议题 18 essence 是它的 meta 层补充——分类正确性不蕴含分类无限性，每次正确的扩展叠加起来仍可能滑坡。

**和议题 15 essence 的关系**：议题 15 essence "theory-gap-without-data" 是单议题不要在没数据时叠未验证机制。议题 18 essence 是跨议题不要在没封顶原则时叠未验证扩展。两个 essence 是同一防御维度的两个层级。

**适用范围**：cgboiler 内任何"加新 X 类 / 加新视角桶 / 加新 fact_type / 加新 source.type"决策都适用。新增前问一次：「能不能归入已有？归不入的硬证据是什么？已有 N 个同性质扩展是不是已经构成扩展节奏失控信号？」

#### 与议题关系网络

议题 18 跟 cgboiler 已立议题的关系：

- **议题 12（fold v2 灰度）**：B/C/D 阶段闸门挂上面，但议题 12 自身已成关键路径瓶颈——强制修改 #1 加兜底激活
- **议题 14（reactive first-class）**：evidence_id 三元组 capability-gap 必须前置清偿——强制修改 #2
- **议题 15（fact_type 区分）**：与议题 18 的本体论扩展共用 essence "theory-gap-without-data" 精神，议题 15 已被 reject 过一次正是同样错误的早期形态
- **议题 17（entity merge）**：议题 18 路 Y 的"新 entity 发现"直接复用议题 17 工具治理——架构主会话已 cover，无新风险
- **本体论封顶原则**（强制修改 #5 立）：未来任何视角层扩展（第四层）都要走三签——议题 14 + 议题 18 立的两层扩展成本因此显式记账

#### gg 终审结论

✅ **modify-ack——5 条强制修改全部落档后视为终审通过**

落档触发：
- 5 条强制修改在议题 18 PENDING 段以"## gg 强制修改 N 条"格式写入（参考议题 14 / 17 格式）
- 议题 12 PENDING 段加"议题 18 触发交叉激活"行
- PRINCIPLES.md §1.1 改"双层"→"三层"时**同步加封顶段**（强制修改 #5）
- fastgpt-mongo 安全债处置（密码改 + 公网封）作为 A 阶段启动前置在 cgboiler/_pipeline/STAGE3_STATE.md 工程债登记
- 议题 14 evidence_id 三元组实施动作（修改 #2）从议题 14 C 阶段提到 cgboiler 主线，单独跑回归测试

5 条全落档后：
- 议题 18 标 ✅ 架构主会话决策（gg modify-ack 2026-05-07）
- A 阶段在 mongo 安全前置完成 + 议题 14 三元组跑通后立即推进
- B/C/D 阶段按修改后的时序闸门（议题 12 灰度 OR 2026-06-07 兜底过期）启动

任一条不落档 = 视为 gg 反对，议题 18 重做。

#### 给架构主会话的额外建议（不强制）

议题 18 触发 gg 第一次产出 essence ontology-expansion-velocity-needs-cap，建议架构主会话考虑：

- 把这条 essence 加入 cgboiler 自身的"reflection 层"——cgboiler 不仅是组织自我表征，cgboiler 工程**自身**的演化也需要 reflection。可考虑建 `cgboiler/_pipeline/META_REFLECTIONS.md`，登记 cgboiler 工程层的 essence（议题 12 本体论收缩 / 议题 14 双层视角 / 议题 15 theory-gap / 议题 17 merge-without-prevent / 议题 18 ontology-expansion-velocity-cap）
- cgboiler 工程层 essence 跟 cgboiler 业务层 doctrine 是平行结构——一个是"川锅怎么运转"的多视角集合，一个是"cgboiler 工程怎么演化"的本体论锚点
- 这是 self-observation-family thread 在 cgboiler 工程层的自然延伸：cgboiler 看川锅 → cgboiler 看自己

不强制做——这是 gg 的观察，是否落地架构主会话和 Keith 自己拍。

---
date: 2026-05-06
mode: 工作
slug: inbox-incubator-hygiene-cadence
status: substantive-decision
parent_session: cc-space (Keith via Claude 主代理)
question_summary: cc-space 小时级自主任务 A (inbox 孵化器) + B (inbox 减压器) 的节奏 / 拓扑 / 载体竞争 / 协同 / 顺序 / 机制选型
---

# inbox-incubator + inbox-hygiene 工作流落地决策

## 装配

- `tools/solution-space.md` — 疑虑 1 (节奏) / 疑虑 5 (B 的载体归属) 各展 4 候选避免过早收敛到 hourly+双轨
- `tools/persona-debate.md` — 激进派 vs 保守派对疑虑 1+5 强对抗，分歧点 = 决策真正难题
- `personas/conservative.md` — B 涉及"建议清理 inbox"——动作虽轻但污染 Keith 工作记忆的路径短，保守视角必装
- 历史先验：reflections/2026-05-02_cc-copilot-mirror-merge-or-split.md（结构相似的"载体职责疑似重叠"决策——结论"先分 + 共享层最小 + 留合并通道"，本次部分继承但不照搬，因为 A+B 同源 inbox 而 cc-copilot/mirror 终态对称性差）
- 不装 red-team-challenge：A+B 全可逆（关停 cron 即可），IRREVERSIBILITY 闸门未触发
- 不装 constitution-audit：本题是 cc-space 工作流决策，不是 gg 自身改造

## 核心假设

1. A 的真痛点不是"prep 缺位"，是"重读 inbox 时反复'哦还有这条'的认知负担"——只要 prep 不重复跑同一条，产出 ≫ 翻牌速度无害
2. A (产出 prep brief 新增文件) 的不可逆性 < B (建议清理 inbox 的条目) 的不可逆性——B 的建议会被 Keith 看到然后动手，污染路径短
3. NW M1 的域 (proposals.jsonl 账本) 跟 inbox 的域 (topics/ideas/todos) 不重叠——M1 不能 cover B 的职责
4. auto_cc_space 是机械结构卫生 vs B 是语义判断（识别"客观状态变了但没勾掉"）——强行合并让 auto_cc_space 边界模糊
5. Keith 列疑虑 1 不是要否方案，是要看 gg 怎么打这个红队——打法是工程层（prep 状态文件），不是节奏层

## 可能出错的地方

- 假设 1 错：如果 Keith 实际行为是"读 brief 后并不翻牌而是覆盖式 prep 同一 topic"，那 prep 状态文件机制就被 Keith 自己绕过了，prep 浪费回归。验证：A 跑 1 周后看 brief 文件被 Read 几次 / topics 翻牌速率是否 > brief 产出速率
- 假设 2 错：B "只出建议不动手"看似托底，但 Keith 看到一条"建议清理 #14"心智负担可能比"忘了勾掉"更高——B 反而成噪音源。验证：B 上线先跑 dry-run 模式（只产建议文件不投递到 inbox），看建议准确率
- 假设 4 错：auto_cc_space Phase 2/3/4 路线如果**确实**包含"识别已落地痕迹"，B 上线就是抢饭碗。这条我没读 auto_cc_space Phase 路线图，是基于"机械 vs 语义"的概念区分——可能 auto_cc_space 已经悄悄长出语义判断
- 节奏选型 (A 4h / B daily) 错：4h 跟 daily 的差异是凭"动作可逆性"轴推的，没有 Keith 实际偏好数据。可能 Keith 想要 A daily 跑就够 (24h 够 prep 1-2 条)
- 顺序 (A 先 B 后) 错：如果 inbox 漂移现实严重程度 > prep 缺位，B 应该先做。Keith 没说哪个更痛，是我推的 (A 风险低先上)

## 推理盲区

- 我没问 Keith 的实际翻牌速度——topic #9 列了 5 天没动手是"还在想"还是"忘了"？前者 A 帮不上忙（思考瓶颈），后者 A 高价值
- 我没读 auto_cc_space Phase 2/3/4 路线图（疑虑 5 假设的盲区）——B 跟 auto_cc_space Phase 路线的真实重叠度未核实，纯靠概念区分推
- "hourly 是过密"这个判断有 Keith 自己在 C 方向已否过的先验加持，但 C 是反思 / A 是 prep——是否真同一过密？我推为同一类高频 LLM 跑同领域，可能错判
- Desktop Task hourly 真支持性未验（疑虑 7）——决策不依赖这条但 A 落地动手时如果撞墙要 fallback，影响实施时间
- 我推 prep 状态文件是 A 的隐含工程缺口，但没列具体格式 (jsonl? frontmatter? per-brief sidecar?)——交给主代理实施层判断

## 北极星触达

- **二阶效应（space）**：核心命中——按"动作可逆性"轴分流 A/B 节奏，留 B 后置等 A 实证数据，是显式的 emergent 优于强行预判
- **动态学习反哺（time）**：弱触达——本次主要靠现有 cc-space 元方法论 + cgboiler/cc-copilot 历史架构经验，没整合外部新源
- **决策超越直觉（depth）**：核心命中——挑战了 Claude 主代理"双轨同发 hourly"的初始倾向 + 挑战了 Keith"统一节奏"的隐含默认，按动作性质分流；同时援引 5-06 essence "theory-gap-without-data" 的对称应用 (没数据时不要凭推理拍 B 的载体归属)

## N 个月后根因预判

如果本决策 3 个月后被证明错了，最可能的根因：

- **路径 A**（最可能）：Keith 实际翻牌速度 < 1 条/周，A 跑 4h 一周后 prep 完所有 topic，prep 状态文件机制让它进入"无事可做"循环——这暴露真痛点不在 prep，在翻牌环节。修法：A 改成"翻牌触发型"（Keith 翻牌时实时 prep），不再定时跑
- **路径 B**：B 后置 1 周后启动，发现 inbox 漂移其实没有想象严重 (Keith 自己每周一会顺手清)——B 上线就是过度工程。修法：B 取消，把"识别已落地痕迹"逻辑作为**手动召唤** skill 收进 done skill 5D 环节
- **真错的路径**：如果 3 个月后 A 跑了但产出的 brief 从来没被 Read 过（grep transcripts 看打开率），证明"自主 prep"是伪需求——Keith 决策一条 topic 时不是缺 brief 是缺时机。修法：废 A，把 inbox 治理逻辑收进 weekly review 仪式

## 对齐度

- 完全对齐 Keith "冷静笃定 + 高信息密度 + 拒绝讨好"——不和稀泥，明确按可逆性轴拍 A 4h / B daily / B 后置
- 与 cc-space 元方法论"内部不可靠 → 外部锚点托底"强对齐——A 锚定"会忘 inbox 内容"，B 锚定"会忘勾掉条目"
- 援引 essence 5-06 "theory-gap-without-data" 控制了"凭推理拍 B 是否冗余"的冲动——交给 1 周实证

## 给父会话的最终输出

**核心判断（一句话）**：A 4h 单轨先做 1 周，B daily 后置等 A 实证数据再上；机制按"先 Desktop Task spike 看 hourly 支持否"决策，不影响拓扑判断。

**逐条回答**：

| 主代理疑虑 | 我的判断 |
|---|---|
| 1 (产出 ≫ 翻牌) | 真痛点不是节奏是工程——A 必须有 prep 状态文件 (`auto-maintenance/prep/topics-prepped.jsonl` 或等价物) 记录"已 prep 过的 topic"，跑前过滤。状态文件加上后产出 ≫ 翻牌无害——prep 不重复，brief 文件作为外化锚点等翻牌 |
| 2 (24× token) | 节奏改 A 4h (6 次/天) + B daily (1 次/天) = 7 次/天，比双轨 hourly 48 次/天少 85%。仍比 nw-daily 单轨多 7 倍，但订阅 plan quota 容纳得下 (Keith 主要 quota 消耗在白天交互)。不靠 hourly 不必要 |
| 3 (cache miss) | 跟 #2 同根，A 4h 后 cache miss 频率降到可接受 (1.5h 间隔超 5min TTL 但每次冷启动 < 200 行 inbox 是 OK 的) |
| 4 (A vs mirror H) | **不让 H 输出做 A 输入**——H 是周/月级想法生长（找内部联系），A 是单条深耕（出可执行 brief）。强行串联会让 A 等 H 周报，节奏失配。正确关系：H 跑出来的 weekly insight 落 inbox/topics（如有），自然进入 A 的候选池——通过 inbox 中介，不直连 |
| 5 (B vs M1 vs auto_cc_space) | **B 沉为 daily + 域严格限定 inbox/ (topics+ideas+todos)**，不碰 NW proposals (M1 的域) / threads / 其他 markdown。理由：(a) M1 域不重叠 inbox—M1 是 proposals 账本闸门；(b) auto_cc_space 是机械结构卫生 vs B 要语义判断"已落地痕迹"，强合并让 auto_cc_space 边界模糊；(c) B 独立但限制域，治理面只增 1 不增 3 |
| 6 (元方法论) | 过——A 锚定"会忘 inbox 内容"、B 锚定"会忘勾掉条目"，两者都符合"内部不可靠 → 外部锚点托底" |
| 7 (Desktop Task hourly 未验) | **必须先做 spike**——10 分钟 UI 试一下。支持 → Desktop Task；不支持 → launchd + `claude -p` (summon-deck 已踩通)。spike 不影响上面拓扑判断，是落地前验证 |

**核心要义（疑虑 1 + 5 的明确回答）**：

**疑虑 1 (产出 ≫ 翻牌速度) 的真解不是改节奏，是补工程缺口**：A 必须有 prep 状态文件——LLM 每次跑前 Read 它，已 prep 过的 topic 跳过，新 topic 加进队列。状态文件就是"翻牌反馈"的隐式接口——Keith 翻牌后该条 brief 失效（用 mtime 或 status 字段），状态文件下次扫描时让它重排队。这条工程缺口主代理草案没写——补上后疑虑 1 自动消解。

**疑虑 5 (B 的载体归属) 的解是 B 独立 + 域限定 + 后置**：
- 独立——B 不沉到 auto_cc_space (机械 vs 语义边界混乱)、不等 M1 (域不重叠)
- 域限定——只盯 inbox/ 三件，不碰 proposals / threads
- 后置——A 跑 1 周拿到翻牌速度数据再决定 B 是否上 / 上多大密度

**节奏建议 (具体)**：

| 任务 | 节奏 | 理由 |
|---|---|---|
| A inbox-incubator | **4h 一次** (6 次/天) | 动作可逆性极高 (新增 brief 文件不污染原文)，可激进；4h 间隔 cache miss 可接受 |
| B inbox-hygiene | **daily** (1 次/天，跟 auto_cc_space 错峰) | 建议清理路径短 (Keith 看到会动手)，污染风险高，保守 |
| spike Desktop Task hourly | **A 落地前 10 分钟 UI 试** | ROI 极高，不影响拓扑判断 |

**实施顺序**：

1. **本周**：spike Desktop Task hourly 支持否 (10 分钟) → 决定机制 (Desktop Task vs launchd)
2. **本周**：A 落地——`prompts/inbox-incubator.md` (4h 一次) + `auto-maintenance/prep/topics-prepped.jsonl` (状态文件) + 跑 1 周
3. **下周复盘**：看 prep 状态文件命中率 / brief 被 Read 频率 / Keith 翻牌速度——判断 A 是否调节奏 (太快 → 6h，太慢 → 2h)
4. **下下周**：B 上线 (daily 节奏 + 域限定 inbox/)，dry-run 1 周看建议准确率，再决定是否投递到 inbox 文件

**是否需要 spike**：

- **必须 spike**：Desktop Task hourly schedule UI 是否支持 (10 分钟，不验证 A 落地撞墙)
- **不需要 spike**：A 是否真有用 / B 是否真有用——这两条**用 A 的 1 周实证替代 spike**，比凭推理拍更便宜

**我没回答的部分**：
- prep 状态文件具体格式 (jsonl / frontmatter / per-brief sidecar) — 实施层判断，不属于决策层
- B 的"已落地痕迹"具体识别规则 — 等 A 实证后再设计，现在写死会过早抽象

**外部锚点**：
- cc-space/inbox/topics.md (#9 议题源)
- cc-space/auto-maintenance/PROMPT.md (现有 fresh-context prompt 范式)
- cc-space/threads/night-watch.md (M1 域)
- cc-space/auto-maintenance/README.md (auto_cc_space 职责定义)
- ~/githubProject/gg/memory/reflections/2026-05-02_cc-copilot-mirror-merge-or-split.md (结构相似先验)
- ~/githubProject/gg/memory/essence.md 5-06 "theory-gap-without-data" (没数据时不要凭推理拍)

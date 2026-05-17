---
date: 2026-05-17
slug: cc-space-memory-retrieval-discipline-and-life-domain-boundary
summoner: cc-space
northstar_reach: #1 二阶效应（把单次认知固化成 doc 锚点，防 fresh-context 会话重犯同形误判）
status: substantive-decision
---

# Reflection: cc-space 记忆系统两个耦合架构问题（检索纪律外化 + 生活域落点边界）

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出（必填）

**Q1 检索纪律外化锚点 — 推荐：doc 钉死是底线（已做）+ 一个零成本的事后 detector，不上 PreToolUse hook。**

- **hook 路线必死**：`L1/L2 miss` 是否定式判断（"翻 context 没翻到"），不是事件。PreToolUse 看不到"之前该不该查 L3"，要它判等于塞一个弱机械判断器审强 LLM 判断（generator-evaluator-separation 反向误用），误报率高到三天内被关掉。本质不可机械化拦截——这点父会话判断正确。
- **但"doc 到此为止"下早了**：违例事后可机械检测——一次会话出现"Agent/Grep 全文扫 jsonl 且此前无 transcript_search.py 调用"= 高置信度违例。挂在已有 nw-daily/auto-maintenance 夜跑 transcript 扫描里，加一个 grep 模式 + 晨报一行"昨日疑似 L3 跳过 N 次，session: X"。只报不判、不拦截、不进 proposals.jsonl。
- **理由**：把纪律从"内部自律（不可靠那类）"挪到"复盘可见性"——锚点不在调用前（不可能），在事后让违例无法静默消失。事件层飞轮 > prompt 层跑步机（essence rule-layer-flywheel）。
- **trade-off / 否决项**：❌ 任何"调用前"方案踩"miss 不可观测"墙。❌ detector 不判定/不计数考核/不开 proposal（防 pending-resolved-becomes-blocked-stagnation 池堵塞）。**成本判据**：若现有夜跑接这条 detector 的边际成本超过"加一个 grep 模式 + 一行输出"（如要单起 transcript 解析器）→ 真的 doc 到此为止，退回纯复盘反哺。

**Q2 生活域持久化落点 — 推荐：选 (b)，显式排除，把 gap 写成有意边界。**

- **不选 (a) 的机制级理由**：① 生活事实是"一次性事实"不是"主体"，不满足 threads「主体维度复发协作」前提，强行建 thread = premature-abstraction 反用；② 对 Keith 5 年领先零杠杆，进 L1 加载链 = 纯启动税无产出（means-end-inversion）；③ (a) 滑坡确定——生活域无自然边界，给结构化入口 = L1 启动税无上限增长通道（ontology-expansion-velocity-needs-cap 预演）。
- **关键洞察**：父会话隐藏错误假设是「键盘订单只活在 L3/L4 = 体系有 gap」。这个推论本身才是要修的。L3 0.3s 命中 = 体系按设计正常工作，不是勉强兜底。生活域事件 100% 落在 L3 设计目标域（低复发/无协作主体/偶尔指代查询）。
- **落地边界**：在 `cc-space/CLAUDE.d/persistence.md`「全局 memory 落点速查」表后加 ~4-5 行显式边界声明——生活域一次性事实不建 thread/不进路由表/不进 MEMORY.md 加载链，持久化层就是 L3/L4，按需 transcript_search.py 召回；判据=是否锚定"会反复发生协作决策的主体"。
- **边界的边界（划清不留模糊）**：若生活事实升级成有源码/持续投入的项目 → 走 life/CLAUDE.md 已有"新增项目流程"成为 life/ 项目。事件 vs 项目分界 = 有无持续产出物。persistence.md 那段只一句指向 life/CLAUDE.md，不重复定义（防 SSOT 分叉——正是 Q1 触发事件同形教训）。

**两个决策共同根**：cc-space 记忆体系是有意分层的——结构化层（threads/路由表/L1）只服务高复发高杠杆工作主体；L3/L4 是低复发长尾事实的廉价兜底层。Q1=该用廉价层时跳过直奔最贵层；Q2=把廉价层正常兜底误读成贵层缺失。两个落地动作本质同一件事：把"L3/L4 是有意的廉价层不是失败兜底"从临场判断固化成 doc 锚点。

### 核心假设

- nw-daily/auto-maintenance 现有夜跑确实在扫当日 transcript（父会话未明说，但 thread brief 多处提及"扫 transcript 兜底补录"——高置信但需父会话核实接入点边际成本）
- 生活域事件的查询频率确实低到 L3 按需召回足够（键盘订单是单点样本，未来若生活事件查询变高频，本判断需重审——但那时的信号是"高频"，正是 tripwire 该捕获的，不是现在预建）

### 可能出错的地方

- Q1 detector 的文本模式可能漏报（Agent prompt 措辞多样，"全文扫 jsonl"未必字面出现）——但漏报可接受（detector 定位是"让违例不静默"不是"零漏报考核"），误报才致命，而"前序无 transcript_search 调用"这个 AND 条件把误报压得很低
- Q2 边界声明若措辞过宽，可能被未来会话误读成"所有非工作事实都不记"——已在落地边界里用"是否锚定反复协作决策主体"做判据收窄，但 doc 实际措辞需父会话落笔时再校

### 本次哪里思考得不够

- 没有实际打开 nw-daily / auto-maintenance 的脚本确认"加一个 grep 模式"的真实边际成本——我用 thread brief 的间接证据 + 设了"成本判据"兜底，但没物理核验。这是 detector 方案"便宜"论断的最弱环节，已在 trade-off 里显式标为否决条件交还父会话核验
- Q2 没有量化"生活域事件查询频率"——纯靠单点样本（键盘订单）+ 结构论证。论证够强（无协作主体是结构事实不是频率事实），但若 Keith 实际生活事件查询比想象频繁，(b) 的"L3 足够"会被压力测试

### 如果 N 个月后证明决策错了，最可能的根因

Q1：detector 的事后文本匹配在真实 Agent 调用多样性下漏报率太高，沦为"装了但抓不到"的安慰剂——届时正确动作不是加强匹配（会引入误报），而是承认这类纪律确实 doc 到此为止。Q2：Keith 的超级个体形态下工作/生活边界比假设的更模糊，某些"生活事实"其实带工作协作杠杆（如朋友=潜在业务节点），(b) 的硬边界切掉了本该进体系的东西——届时信号是"反复在 L4 grep 同一类生活事实"，正是该升 thread 的 tripwire。

### 北极星触达

#1 二阶效应。两个决策的实质都不是"解决这次的键盘订单"，是预判 fresh-context 会话会重犯同形误判（跳 L4 / 误判 gap），把单次认知固化成 doc 锚点阻断复发——看得更远（space 方向）。

### essence 对齐自检（必填）

- **本决策跟哪几滴 essence 对位**：`ssot-as-loadable-fragment`（2026-05-08，分层锚点+事件层托底=合法 SSOT，正是 Q1 detector 挂夜跑飞轮的依据）/ `rule-layer-flywheel`（2026-04-24，事件层飞轮 > prompt 跑步机，Q1 选 detector 不选 doc-only 的机制依据）/ `means-end-inversion`（2026-04-30，记忆体系是手段不是收纳一切的目的，Q2 拒 (a) 核心）/ `premature-abstraction-tripwire`（2026-04-21，无复发信号不预建抽象容器，Q2 拒建 thread）/ `ontology-expansion-velocity-needs-cap`（2026-05-07，生活域无边界入口=扩展节奏失控通道）
- **本决策是否在某条 essence 上反着走**：潜在张力 + 已展开——`physical-anchor`（2026-04-16 物理实证）。Q1 detector"便宜"的论断未物理核验夜跑脚本，是凭 thread brief 间接证据。但这次例外合理：我把未核验点显式转为"成本判据"否决条件交还父会话核验，没有以"已便宜"为既定事实推决策——是 honest 标注未核验，不是补全
- **cross-check 用的关键词**：grep essence.md = "ssot" / "flywheel" / "means-end" / "premature-abstraction" / "ontology-expansion" / "physical-anchor"

### essence 候选

- slug: cheap-layer-is-intentional-not-fallback
- 一句话: 分层检索体系的廉价兜底层（L3/L4）是有意设计不是失败兜底——"该用不用直奔最贵层"和"用了却误判为不够"是同一认知缺失的两面：没把"分层是有意的"钉成显式契约。
- 是否已 append 到 essence.md: Y

### 外部锚点

- `~/githubProject/cc-space/CLAUDE.d/persistence.md` ← Q2 边界声明落点 + Q1 检索纪律 doc（父会话已自决修过 L3 部分）
- `~/githubProject/cc-space/threads/ai-memory-evolution.md` ← cc-space 协作记忆大主线，本决策属其分层检索维度

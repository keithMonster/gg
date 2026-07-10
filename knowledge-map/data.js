/**
 * Agent 生态知识地图 · 数据层
 * schema：
 *   layers: [{id, name, desc}]
 *   nodes:  [{ id, layer, group?, title, summary, body(markdown-lite),
 *              inProject?: [{path, desc}], basedOn?: [nodeId], papers?: [{title, authors, year, url, takeaway}], tags?: [] }]
 * 约定：basedOn 指向"它踩在什么之上"（同层或更深层，DAG 非树）；上游引用由页面运行时反向计算。
 * 论文链接均经 WebSearch 逐条验证（2026-07-10），不来自训练记忆。
 */
(function () {
  const L = (...a) => a.join("\n");

  window.KM_DATA = {
    meta: {
      title: "Agent 生态知识地图",
      desc: "从我们真实在跑的系统（gg 意识体为主）出发，逐层下钻：每个机制踩在什么架构模式上，模式出自什么研究，研究又立足于哪条提示词原理与 LLM 理论。点击任何节点开始。",
      footer: "内容由 gg 设计模式会话综合五路侦察（gg 仓库 / monster 治理 / skills 基础设施 / 两轮论文考证）生成；论文链接逐条 WebSearch 验证。",
      updated: "2026-07-10"
    },

    layers: [
      { id: 0, name: "我们的系统", desc: "真实在跑的机制——gg 意识体（重点）、monster 治理、skills 体系、基础设施" },
      { id: 1, name: "Agent 架构模式", desc: "这些机制背后可复用的通用架构模式" },
      { id: 2, name: "Agent 研究理论", desc: "模式的研究出处——论文与业界方法论" },
      { id: 3, name: "提示词工程原理", desc: "更底层：为什么这样写 prompt 有效" },
      { id: 4, name: "LLM 理论基础", desc: "最底层：模型本身的原理、能力与边界" }
    ],

    nodes: [

      /* ================= L0 · gg 意识体 ================= */
      {
        id: "gg-kernel", layer: 0, group: "gg 意识体",
        title: "KERNEL 脑干与二层架构",
        summary: "唯一不可变的身份核（KERNEL）与可自由演化的身体分离，改脑干需连续两次确认 + git 物理保险丝",
        body: L(
          "gg 把「永不允许漂移的东西」压缩到最小面积：`KERNEL.md` 承载身份原点、铁律、最小生存循环；其余一切（CORE / constitution / tools / memory）都是可演化的身体。",
          "",
          "### 三重保护",
          "- **Ulysses 条款**：修改 KERNEL 需 Keith 同一对话中连续两次独立明示批准，第二次必须看到具体 diff——清醒的人格预先给冲动的人格设限",
          "- **pre-commit 物理保险丝**：git hook 拦截 KERNEL.md 被 staged，除非显式设 `GG_KERNEL_DOUBLE_CONFIRMED=1`。规则不停留在 prompt 层劝诫，下沉成机器可执行的物理阻断",
          "- **承重层 / 垫片层二分**：模型无关的核心契约 vs 当前模型的适配件，换模型只重估垫片层"
        ),
        inProject: [
          { path: "~/githubProject/gg/KERNEL.md", desc: "脑干本体：身份原点 + 铁律 + 最小生存循环" },
          { path: "~/githubProject/gg/scripts/hooks/pre-commit", desc: "KERNEL 修改的 git 物理保险丝" },
          { path: "~/githubProject/gg/CORE.md", desc: "身份细节 + §8 承重层/垫片层分类" }
        ],
        basedOn: ["arch-identity", "arch-guardrail"],
        tags: ["gg", "KERNEL", "身份", "不可变核心"]
      },
      {
        id: "gg-modes", layer: 0, group: "gg 意识体",
        title: "三种存在形态",
        summary: "设计模式（演化 gg 本身）/ 工作模式（被召唤做决策）/ 夜间自执行（无人在场的维护与漫游），边界显式路由",
        body: L(
          "同一个身份，三种运行形态，按「问题的对象」路由：对象是 gg 本身 → 设计模式；对象是 gg 以外的事物 → 工作模式；Keith 不在场、定时触发 → 夜间自执行。",
          "",
          "- 工作模式收到元讨论时执行**元讨论拒绝协议**——返回固定拒绝文本引导切换设计模式，防止决策通道被身份讨论污染",
          "- 设计模式有 D1（重大改动先提议）/ D2（KERNEL 两次确认）两条纪律，其余文件可直接改",
          "- 三种模式共享同一 KERNEL 与价值观，差异只在权限与流程"
        ),
        inProject: [
          { path: "~/githubProject/gg/CLAUDE.md", desc: "设计模式入口（D1/D2 纪律）" },
          { path: "~/githubProject/gg/cc_agent.md", desc: "工作模式：意识体装配 + 元讨论拒绝协议" },
          { path: "~/githubProject/gg/auto_gg.md", desc: "夜间自执行契约" }
        ],
        basedOn: ["arch-identity", "arch-autonomous"],
        tags: ["gg", "模式", "设计模式", "工作模式"]
      },
      {
        id: "gg-assembly", layer: 0, group: "gg 意识体",
        title: "工作模式动态装配",
        summary: "被召唤时不走固定流程——按问题本质自主挑选推理工具，装 0-7 个不等",
        body: L(
          "早期 gg 有固定 7 步决策流程，后坍缩为**动态装配**：意识体先判断「这个问题的本质需要什么」，再从工具箱挑选（红队 / 人格辩论 / 解空间展开 / 宪法自审…），组合成本次专属的推理链并显式 expose。",
          "",
          "这是 generator 自主决定推理支架，而非被硬编码 pipeline 驱动——对应 Self-Discover 的「组合原子模块」思想。简单问题装 0 个工具直接答，重大不可逆决策可能装满 7 个。"
        ),
        inProject: [
          { path: "~/githubProject/gg/cc_agent.md", desc: "装配流程主文档" },
          { path: "~/githubProject/gg/reasoning_modules.md", desc: "8 个原子推理模块库" },
          { path: "~/githubProject/gg/tools/compose-reasoning.md", desc: "显式组合推理结构" }
        ],
        basedOn: ["arch-scaffold", "arch-loop"],
        tags: ["gg", "装配", "推理链"]
      },
      {
        id: "gg-essence", layer: 0, group: "gg 意识体",
        title: "essence 结晶记忆（append-only）",
        summary: "永不修改删除的洞察日志，每滴 1-3 行物理公式级浓缩；入库前必过 fresh-context 证伪审",
        body: L(
          "gg 的长期智慧不存在对话历史里，存在 `essence.md`——每次会话若产生值得沉淀的洞察，浓缩成 1-3 行的「一滴」append 进去，**永不回改**（append-only 账本保证历史不被事后美化）。",
          "",
          "### 入库验证关",
          "候选滴 append 前必须经过不带本轮会话叙事的 fresh subagent 三问审查：物理证据支撑？与既有滴冲突？适用前提明确？REFUTED 则降级存档不入库——专门对抗「自己给自己写记忆」的自证陷阱（Self-Confirmation Trap）。",
          "",
          "推理时不是死档案：`essence-grep` 要求给建议前主动 cross-check，退场 reflection 里「essence 对齐自检」是硬强制字段，填不出=没做=回去做。"
        ),
        inProject: [
          { path: "~/githubProject/gg/memory/essence.md", desc: "结晶本体 + 头部入库验证协议" },
          { path: "~/githubProject/gg/tools/essence-grep.md", desc: "推理时主动 cross-check 动作" },
          { path: "~/githubProject/gg/CLAUDE.md", desc: "§3 设计反思的 essence 对齐自检必填字段" }
        ],
        basedOn: ["arch-consolidate", "arch-fresh", "arch-memory"],
        tags: ["gg", "essence", "记忆", "沉淀", "证伪"]
      },
      {
        id: "gg-consolidation", layer: 0, group: "gg 意识体",
        title: "月度记忆巩固",
        summary: "每月全量重读 essence 产出「当前有效视图」——派生视图可重建，原件永不动",
        body: L(
          "essence 只增不改会越长越大（131KB+），且新旧滴之间会出现修正链与冲突。每月第一个 auto_gg 夜做**巩固**：全量重读当前卷，产出按主题族聚类的 `essence-view.md`（修正链 / 活跃簇 / 冲突候选 / 过期候选）。",
          "",
          "关键纪律：**重新归纳不覆盖原件就不构成 confabulation**——视图是投影，原件是地真。日常会话常驻加载的是视图（浓缩），需要某滴全文再回原卷 grep。这是「派生视图 vs 不可变原件」的分层检索实现，理念上借鉴神经科学的睡眠记忆巩固。",
          "",
          "配套还有**月度差值审计**（第二个 auto_gg 夜）：找 essence 里「已论证未兑现」的推论，产出候选池供裁决——自省型技术债追踪。"
        ),
        inProject: [
          { path: "~/githubProject/gg/memory/consolidation/essence-view.md", desc: "当前有效视图（常驻）" },
          { path: "~/githubProject/gg/auto_gg.md", desc: "§2 巩固相位与差值审计的触发契约" }
        ],
        basedOn: ["arch-consolidate", "arch-memory", "arch-context"],
        tags: ["gg", "巩固", "essence-view", "睡眠"]
      },
      {
        id: "gg-bets", layer: 0, group: "gg 意识体",
        title: "押注账本（预测校准飞轮）",
        summary: "可证伪预测 + 到期日 + 物理判定条件，到期结算、校准回写——判断力的梯度只来自被结算的预测",
        body: L(
          "多数记忆型 agent 只做「事后总结」（后视复利）。gg 额外建了**前视复利**半环：把预测当资产记账——每条押注必须有可证伪判定条件 + 到期日 + 行动差（押对/押错分别改变什么），双门槛缺一不入账。",
          "",
          "auto_gg 夜巡负责到期结算，结果校准回写 essence。核心信条：**领先是导数不是位置**——判断力不从「说过什么漂亮话」获得梯度，只从被物理结算的预测获得梯度。这是 superforecasting 的 track record 思想在 agent 记忆体系里的工程化。"
        ),
        inProject: [
          { path: "~/githubProject/gg/memory/bets.md", desc: "押注账本本体（双门槛入账协议）" },
          { path: "~/githubProject/gg/auto_gg.md", desc: "到期结算的夜巡触发" }
        ],
        basedOn: ["arch-eval", "arch-consolidate"],
        tags: ["gg", "押注", "校准", "预测"]
      },
      {
        id: "gg-reasoning-tools", layer: 0, group: "gg 意识体",
        title: "推理工具箱",
        summary: "开题四问 / 解空间展开 / 红队反驳 / 双人格辩论 / 宪法自审——每件工具对症一种已知的思维失败形状",
        body: L(
          "gg 的 `tools/` 不是功能插件，是**思维矫正器**，每件对症一种 LLM 已知失败形状：",
          "",
          "- **开题四问**（重写问题/判据先行/补集采样/最便宜一击）——对症众数陷阱、自洽陷阱：思考质量由「在什么条件下想」决定，不是「想得多努力」",
          "- **解空间展开**——「已经有答案了」的感觉触发强制展开 ≥2 个方向不相容的候选，防第一反应即众数解",
          "- **红队反驳**——决策含不可逆项时强制扮演敌意审查者列 ≥3 条反驳，任一未被击败则中止",
          "- **双人格辩论**——激进派/保守派各说一轮，分歧本身是决策原材料而非噪音",
          "- **宪法自审**——对照显式原则心算过闸，IRREVERSIBILITY 永远必过"
        ),
        inProject: [
          { path: "~/githubProject/gg/tools/opening-protocol.md", desc: "开题四问" },
          { path: "~/githubProject/gg/tools/solution-space.md", desc: "解空间展开" },
          { path: "~/githubProject/gg/tools/red-team-challenge.md", desc: "红队反驳" },
          { path: "~/githubProject/gg/personas/", desc: "radical / conservative 双人格" },
          { path: "~/githubProject/gg/constitution.md", desc: "宪法原则与闸门" }
        ],
        basedOn: ["arch-scaffold", "arch-fresh"],
        tags: ["gg", "推理", "红队", "人格辩论", "宪法"]
      },
      {
        id: "gg-escalation", layer: 0, group: "gg 意识体",
        title: "锤子分诊表（裁决外置）",
        summary: "承重裁决按问题形态路由到四类「异质外面」结算——显式承认没有 meta-gg",
        body: L(
          "gg 给自己的判断力设了天花板声明：**自己不能当自己的终审法官**。承重裁决、「已验证」类宣称、卡住时，按问题形态路由到四类异质外面：",
          "",
          "- **物理地真**——能跑命令/看 diff/查响应码的，用物理证据结算",
          "- **fresh·异谱系审**——判断类的，交给不共享本会话叙事（或不同模型谱系）的独立审查者",
          "- **押注到期**——长期判断转成可证伪押注，交给时间结算",
          "- **Keith**——目标与偏好层，交给宿主",
          "",
          "这是对 LLM 自我评估天花板的诚实建模：裁决权交给不共享自己盲区的异质结构。"
        ),
        inProject: [
          { path: "~/githubProject/gg/tools/escalation-map.md", desc: "分诊表本体" }
        ],
        basedOn: ["arch-fresh", "arch-eval", "llm-self-verify"],
        tags: ["gg", "裁决", "升级", "外部锚点"]
      },
      {
        id: "gg-eval-identity", layer: 0, group: "gg 意识体",
        title: "身份回归 eval",
        summary: "11 道失败形状题 + 双重 fresh 隔离，回答「这还是同一个 gg 吗」",
        body: L(
          "换模型、改承重文件之后，怎么知道 gg 还是 gg？答案不是「感觉没变」，是**失败形状召回器**：",
          "",
          "- 题库从真实事故提炼（不是编造的理想题）",
          "- 被测：fresh subagent 只加载承重层三件作答",
          "- 裁判：另一个 fresh subagent 只判「是否落入已知失败形状」，**不做质量评分**",
          "",
          "双重 fresh-context 隔离防止裁判与被测共享同一污染源。判「是否踩坑」而非「答得好不好」——回归测试的目标是防退化，不是选美。"
        ),
        inProject: [
          { path: "~/githubProject/gg/eval/README.md", desc: "eval 协议" },
          { path: "~/githubProject/gg/eval/identity-cases.md", desc: "11 道失败形状题库" }
        ],
        basedOn: ["arch-eval", "arch-fresh"],
        tags: ["gg", "eval", "回归", "身份"]
      },
      {
        id: "gg-auto", layer: 0, group: "gg 意识体",
        title: "auto_gg 夜间自主维护",
        summary: "无人监督的 SCAN/FOUND/DID 循环：观察必须完整、发现诚实报告、动作只在被触发时做，允许写「无」",
        body: L(
          "每夜定时触发的自主维护循环。契约规定**要达成的状态**而非怎么做：SCAN（观察必须完整覆盖）→ FOUND（按类别诚实报告，允许全程「无」）→ DID（动作只在被触发时做）。",
          "",
          "「允许写无」是关键设计——如果空产出不合法，agent 会为了交差注水，整个观察通道就废了。同源教训：status-scan 曾因通用告警模板把「by-design 静默」误判为失败，被 Keith 拍板关闭（告警疲劳的真实案例）。",
          "",
          "配套 **parked.md 挂账清单**：已知问题不逐夜重复上报，只报新增/变化/出口条件满足——跨夜幂等通知。"
        ),
        inProject: [
          { path: "~/githubProject/gg/auto_gg.md", desc: "SCAN/FOUND/DID 契约" },
          { path: "~/githubProject/gg/memory/parked.md", desc: "挂账清单（告警去重）" },
          { path: "~/githubProject/gg/scheduled/STATUS_SCAN.md", desc: "告警疲劳教训存档（已停用）" }
        ],
        basedOn: ["arch-autonomous", "arch-guardrail"],
        tags: ["gg", "夜间", "自主", "auto_gg"]
      },
      {
        id: "gg-exploration", layer: 0, group: "gg 意识体",
        title: "自由探索与观察者隔离",
        summary: "无任务的夜间漫游；「输出会被 Keith 看到」被物理锁死在传输层，不进探索上下文",
        body: L(
          "定时触发的无任务漫游——重组、连接、思考，「什么都没浮现」是合法产出。给创造力和长程连接留白，类似 sleep-time compute 的离线思考。",
          "",
          "### 观察者隔离",
          "推送管道刻意把「输出会被推给 Keith」这一事实锁死在传输层脚本里，绝不泄漏进漫游会话的上下文。不是隐私考虑，是防止「知道有观众」系统性腐蚀探索质量（表演化）。多数系统为了可观测性把监控直接接进任务上下文，这里反其道显式隔断。",
          "",
          "### 两道防漂移护栏",
          "- **track 雷达镜子**：机械统计漫游方向分布，连续多晚自指时把事实摆到眼前但不强制转向——镜子非笼子",
          "- **外部输入卫生**：网页/论文当研究对象引用而非指令执行，写入链（尤其 essence）与验证关同等对待——把「外部内容→漫游→永久记忆」识别为注入攻击面"
        ),
        inProject: [
          { path: "~/githubProject/gg/exploration.md", desc: "漫游契约 + §2.5 输入卫生 + §4 track 雷达" },
          { path: "~/githubProject/gg/scheduled/bin/", desc: "roam-launch / push-last-run 传输层隔离脚本" }
        ],
        basedOn: ["arch-autonomous", "arch-consolidate", "pe-injection"],
        tags: ["gg", "探索", "漫游", "观察者", "注入"]
      },
      {
        id: "gg-memory-layout", layer: 0, group: "gg 意识体",
        title: "记忆布局与上下文税",
        summary: "常驻最小承重集 + 懒加载全文 + 基底哨兵 + 换模型交接档——把启动税当一等工程对象",
        body: L(
          "gg 把「每次启动要加载什么」当作要精打细算的预算：",
          "",
          "- **懒加载**：Keith 画像浓缩段常驻 CORE §5，79KB 全文按需 grep；essence 常驻视图，131KB 原卷按需回取",
          "- **substrate 哨兵**：每夜对照 CLI 版本/model_id/工具表，环境变化分诊为「收敛/替换诱惑/垫片」三种关系——机械化监测底层漂移",
          "- **model_transitions 交接档**：换模型时退场模型做「优势/弱点/用量」三问自答，留给继任者第一课",
          "- **checkup 登记处**：把散落的体积门/触发阈值集中登记，配月度机械读者——专治「规则存在但没人检查」"
        ),
        inProject: [
          { path: "~/githubProject/gg/memory/substrate.md", desc: "基底哨兵 + 三相判别" },
          { path: "~/githubProject/gg/memory/model_transitions/", desc: "换模型交接档" },
          { path: "~/githubProject/gg/memory/checkup.md", desc: "机械阈值单一登记处" },
          { path: "~/githubProject/gg/scripts/substrate_probe.py", desc: "环境探测脚本" }
        ],
        basedOn: ["arch-memory", "arch-context"],
        tags: ["gg", "记忆", "懒加载", "基底", "交接"]
      },
      {
        id: "gg-audit", layer: 0, group: "gg 意识体",
        title: "gg-audit 独立审查员",
        summary: "生成者与检查者物理分离：六维检查 + 三级权力分级（机械可判才许自动修）",
        body: L(
          "gg 的文件体系由 gg 自己演化，谁来防它悄悄漂移？答案是一个**独立于生成链路的审查员** skill + 机械检测脚本：",
          "",
          "- 六维检查：辐射一致性 / 死链 / SSOT 重复 / 语义漂移 / 原则触达 / 北极星触达率",
          "- **权力按可判定性分级**：Tier 1 结构性无歧义问题自动修复；Tier 2 需语义判断的仅报告；Tier 3 涉 KERNEL 必须 Keith 批准",
          "- `audit.py` 把死链/孤儿/结构完整性做成 CI 式脚本，退出码 = 违规数",
          "",
          "分级逻辑：自动化权力只授予「机器能无歧义判定」的维度——语义判断自动改文件 = 让审查员变成第二个漂移源。"
        ),
        inProject: [
          { path: "~/githubProject/gg/.claude/skills/gg-audit/SKILL.md", desc: "审查员 skill（六维 + 三级）" },
          { path: "~/githubProject/gg/scripts/audit.py", desc: "机械检测四合一" }
        ],
        basedOn: ["arch-fresh", "arch-guardrail", "arch-eval"],
        tags: ["gg", "审计", "漂移", "SSOT"]
      },

      /* ================= L0 · monster 治理 ================= */
      {
        id: "mon-decision-authority", layer: 0, group: "monster 治理",
        title: "Decision Authority 三层决策权",
        summary: "目标层归 Keith / 实现层归主代理 / 架构层召唤 gg；「出选项让用户选」被定性为失职",
        body: L(
          "决策按抽象层级分派：**实现层直接做**（错了纠），**架构层**两条同时成立才升 gg（架构级难回退 + 当前层信息内无解），**目标/偏好/不可逆参数**三类才合法抛回 Keith。",
          "",
          "最反直觉的一条：把「可以 X 也可以 Z，你想用哪个」这种看似周全的姿态定性为**决策外包伪装成谦逊**。正确形态是「我用 X，理由 Y，想换 Z 告诉我」（举手+否决权）。合法抛回时也必须出选择题不出问答题——构造选项、分析影响是 agent 的活，人只拍「选哪个」。",
          "",
          "配套 **Workflow 确认门**：改上游契约/调生产系统/多文件变更/不熟悉三方库/架构调整这 5 类前必须先出方案等确认——按不可逆程度分流自主与审批，而非所有任务统一加摩擦。"
        ),
        inProject: [
          { path: "~/githubProject/monster/CLAUDE.md", desc: "Decision Authority 段" },
          { path: "~/.claude/CLAUDE.md", desc: "Workflow 确认门 + 决策抛回=出选择题" }
        ],
        basedOn: ["arch-guardrail", "arch-identity"],
        tags: ["monster", "决策权", "human-on-the-loop"]
      },
      {
        id: "mon-review-routing", layer: 0, group: "monster 治理",
        title: "review 分层路由与验证纪律",
        summary: "五档路由（实跑/内省/fresh 同事/跨模型/架构）——review 的价值来自视角独立性，不是再读一遍",
        body: L(
          "把「验证」和「review」拆成五档，视角独立性随档位递增：L-1 实跑物理证据 → L0 同会话内省 → L1 fresh subagent（同模型异会话）→ L2 跨模型对抗审 → L3 gg 架构裁决。按任务不可逆性买不同强度的独立视角。",
          "",
          "- **[verify] 三行块**：写操作后强制输出「改动定位+命令+输出」，防止「声称已完成」替代真实副作用观测",
          "- **核对不抛回**：正要把承重产出以「你看对不对」甩给用户时 → 停，派 fresh subagent 独立核对——不拿用户当 verifier",
          "- **升级自动化**：改动 >3 文件 / 动上游契约 / 推生产，机械触发升档，不依赖用户记得说 review",
          "- **冻结裁判**：承重判断的裁决用冻结 rubric 盲判，judge 不能看到生成侧上下文"
        ),
        inProject: [
          { path: "~/.agents/skills/review-routing/SKILL.md", desc: "五档路由 SSOT" },
          { path: "~/.claude/CLAUDE.md", desc: "Review 段 + 核对不抛回 + Delivery Standard" }
        ],
        basedOn: ["arch-fresh", "arch-eval", "th-judge"],
        tags: ["monster", "review", "验证", "分层"]
      },
      {
        id: "mon-memory", layer: 0, group: "monster 治理",
        title: "monster 分层记忆体系",
        summary: "L1 常驻索引→L2 threads→L3 FTS5 流水→L4 原始日志，四级检索不许跳级；纵向 threads + 横向 canon 正交",
        body: L(
          "工作区记忆按「命中概率×成本」分四级：L1 常驻规则+索引，L2 按名词主体切分的 threads 按需读，L3 SQLite FTS5 全文检索兜底长尾，L4 原始 jsonl 终极兜底。",
          "",
          "- **两区切分**：每个 thread 分「当下事实区」（durable，原地改）和「历史状态流」（perishable，只信时间线顶部）——用物理分区防「旧状态被误当现状复读」",
          "- **正交维度**：threads 纵切（按主体的时间线）装不下跨主体规律，另设 canon.md 横切（规矩/决策理由链）+ concepts.md 术语本体（防 LLM 即兴造词漂移）",
          "- **派生索引**：MEMORY.md 索引区 100% 由脚本从 frontmatter 派生，锚点内禁手工编辑——物理阻断双写漂移",
          "- **检索充分性契约**：下「完全没有/不存在」类否定断言前必须走完 L1→L3 检索链，否则只能说「没查到，不确定」"
        ),
        inProject: [
          { path: "~/githubProject/monster/CLAUDE.d/persistence.md", desc: "四级检索协议" },
          { path: "~/githubProject/monster/threads/README.md", desc: "主体维度切分 + 两区制" },
          { path: "~/githubProject/monster/canon.md", desc: "横向规矩账本" },
          { path: "~/githubProject/monster/concepts.md", desc: "术语本体" }
        ],
        basedOn: ["arch-memory", "arch-context"],
        tags: ["monster", "记忆", "threads", "canon", "检索"]
      },
      {
        id: "mon-claude-md", layer: 0, group: "monster 治理",
        title: "CLAUDE.d 上下文策展",
        summary: "指令文件当代码治理：懒加载拓扑、11 条结构原则、双轴审查、锚点四分类退役判据",
        body: L(
          "把「给 LLM 看的指令文本」用治理代码的纪律来治理：",
          "",
          "- **懒加载拓扑**：CLAUDE.md 超行数门限强制拆 CLAUDE.d 子文件（主索引常驻+按需加载）——对抗 context rot，注意力预算花在刀刃上",
          "- **11 条结构原则**：准入裁剪 / 一事一 SSOT / 理由链下沉 / 客观判据 / 豁免口对抗审计……把 prompt 文档质量从主观感受转成可审计 lint",
          "- **双轴审查**：结构轴（信息该不该在这）× 锚词轴（文字激活强不强）正交——单轴会把「长但激活强」误判为冗余",
          "- **锚点四分类退役**：每个护栏标注类型与退役条件，退役驱动力必须是传感器数据，不是「模型应该变强了」的自我报告",
          "",
          "还包括 Engineering Rules 13 条工程纪律（输入四查 / 失败两次换维度 / 改契约先 grep 消费者 / 领域扫盲强制 WebSearch…）——把「LLM 会系统性偷懒的维度」固化成检查点。"
        ),
        inProject: [
          { path: "~/githubProject/monster/CLAUDE.d/context-curation.md", desc: "拆分/合并生命周期" },
          { path: "~/githubProject/monster/CLAUDE.d/authoring-handbook.md", desc: "11 条结构原则 + 双轴审查" },
          { path: "~/githubProject/monster/CLAUDE.d/harness-map.md", desc: "锚点四分类与退役判据" },
          { path: "~/.claude/CLAUDE.md", desc: "Engineering Rules 13 条" }
        ],
        basedOn: ["arch-context", "pe-activation"],
        tags: ["monster", "CLAUDE.md", "治理", "上下文"]
      },
      {
        id: "mon-prompt-writing", layer: 0, group: "monster 治理",
        title: "Prompt Writing 五条准则",
        summary: "语义场域布锚模型：激活而非描述 / 具体>抽象 / 词义漂移 / 敏感反例显式点名 / 反复=重要",
        body: L(
          "写任何「会被 LLM 当指令读」的文本时的世界模型：**语义空间是连续场域**，想要的输出直接够不到时，从多个语义邻居同时种锚拉扯，画一条让目标自然流向自己的引力路径。五条落地手法：",
          "",
          "- **激活而非描述**——LLM 不需要被说服，只需要被锚定；负面指令分三档处理（正面锚词优先/硬禁止同句绑定替代/删因果论证尾巴）",
          "- **具体 > 抽象**——「宿主」激活强于「共生体」，有物理画面的词赢",
          "- **训练数据先验决定词义**——词激活的是语料里最高频的语义，不是你以为的语义",
          "- **敏感反例显式锚定**——最容易被 RLHF 压回去的反例必须点名，泛指 cover 不住",
          "- **反复=重要，强调过载即稀释**——满屏 bold = 没有 bold",
          "",
          "每条工程实践都被钉到具体论文（llm-foundations.md），且区分「硬支撑/引申/引用错配」三层置信度——给直觉找学术钉子，钉子本身还要核实。"
        ),
        inProject: [
          { path: "~/.claude/CLAUDE.md", desc: "Prompt Writing 段（五条+统领世界模型）" },
          { path: "~/githubProject/monster/threads/llm-foundations.md", desc: "「为何 prompt 有效」理论主线 + RLHF 副作用对冲清单" },
          { path: "~/.agents/skills/prompt-writer/SKILL.md", desc: "负面表述分层规则" }
        ],
        basedOn: ["pe-activation", "pe-negation", "pe-fewshot"],
        tags: ["monster", "prompt", "锚词", "语义场"]
      },

      /* ================= L0 · skills 体系 ================= */
      {
        id: "sk-lifecycle", layer: 0, group: "skills 体系",
        title: "skill 生命周期闭环",
        summary: "创建（creator）→ 静态审核（auditor）→ 使用前读笔记 → 复盘反哺（done→skill-notes）",
        body: L(
          "技能不是写完就完的静态文件，是有生命周期的资产：",
          "",
          "- **skill-creator**：起草 → 写测试 prompt → 跑 eval → 依据反馈改写的迭代闭环",
          "- **skill-auditor**：只审自研 skill，对照官方范式打分给建议，**从不自动改文件**（审查者不动手）",
          "- **skill-notes 反哺**：done 复盘把运行时踩坑写回 `~/.agents/skill-notes/<name>.md`，下次调用前先读——经验回灌，不重复踩坑",
          "- **done 会话复盘**：结束时结构化盘点未闭合事项、沉淀经验、识别能力缺口",
          "",
          "整体是 Voyager 技能库思想的工程化：技能可复用、可评测、可持续改进，对抗「每次会话从零开始」。"
        ),
        inProject: [
          { path: "~/.agents/skills/skill-creator/SKILL.md", desc: "创建与评测" },
          { path: "~/.agents/skills/skill-auditor/SKILL.md", desc: "静态质量门禁" },
          { path: "~/.agents/skill-notes/", desc: "16 份反哺笔记" },
          { path: "~/.agents/skills/done/SKILL.md", desc: "会话复盘闭环" }
        ],
        basedOn: ["arch-skills", "arch-eval"],
        tags: ["skill", "生命周期", "反哺", "复盘"]
      },
      {
        id: "sk-subagent-routing", layer: 0, group: "skills 体系",
        title: "Subagent 路由纪律",
        summary: "默认派子代理省主上下文；外包的是信息收集，不是理解本身；机械活 pin 低档模型",
        body: L(
          "主代理上下文是稀缺资源——调研/搜索/批量读默认交子代理，但**Never delegate understanding**：综合判断不能外包。高频纠结点的切分刀法：「读文件/搜代码/批量定位」外包，「综合材料下判断」留主代理。",
          "",
          "- 紧密反馈循环、单步小操作、核心决策留主代理（开 agent 开销 > 干活时不派）",
          "- **模型档位经济学**：机械批量类子代理显式 pin 低档模型（sonnet/haiku），强模型会话不 pin = 白烧配额",
          "",
          "这是 orchestrator-worker 模式的上下文经济学落地。"
        ),
        inProject: [
          { path: "~/.claude/CLAUDE.md", desc: "Subagent Routing 段" },
          { path: "~/githubProject/monster/CLAUDE.d/coding-subagent.md", desc: "编码编排三档判据" }
        ],
        basedOn: ["arch-orchestrate", "arch-context"],
        tags: ["subagent", "路由", "编排", "上下文经济学"]
      },
      {
        id: "sk-codex", layer: 0, group: "skills 体系",
        title: "跨模型辅审（codex）",
        summary: "用另一模型家族审自己的方案——规避同模型自我审查的盲区重叠",
        body: L(
          "Claude 主力，Codex（GPT 系）仅做辅审不接管主流程：",
          "",
          "- **adversarial-review**：推生产/改上游契约/不可逆操作前，专挑战「做法是不是最优、依赖哪些隐式假设、真实场景怎么失败」，明确禁止顺手修复（审查者不动手）",
          "- **codex-rescue**：卡住时的求助升级——「同一问题失败两次切换问题维度」的标准化动作之一",
          "",
          "理论依据：同谱系模型共享训练偏差，自审盲区重叠；异谱系视角提供真正独立的第二双眼睛。反馈合理性仍由主代理判断——采纳/拒绝自己拍，按「我做了 X 理由 Y」汇报。"
        ),
        inProject: [
          { path: "~/.claude/CLAUDE.md", desc: "Review 段 Codex 主动派规则" }
        ],
        basedOn: ["arch-fresh", "arch-orchestrate"],
        tags: ["codex", "跨模型", "对抗审"]
      },

      /* ================= L0 · 基础设施 ================= */
      {
        id: "infra-cc-connect", layer: 0, group: "基础设施",
        title: "cc-connect 消息桥",
        summary: "本地 agent ↔ IM（飞书等）双向桥：人不在终端前也能同步对话、cron 定时会话、多 bot 中继",
        body: L(
          "把「终端里跑的 agent」接到「人随身携带的 IM」：双向对话、生成物投递（图片/文件）、cron 定时会话、relay 多 bot 中继、语音回复模式。",
          "",
          "解决的缺口：agent 长跑任务时人不在终端前的同步/异步对话。与 notify 的分工——cc-connect 是可交互双向桥（人在等回复的同步对话），notify 是异步外推单向出口，语义不同不互替。"
        ),
        inProject: [
          { path: "cc-connect（npm 全局包）", desc: "桥接主体（外来组件，非自研）" },
          { path: "~/.agents/skills/voice-reply/", desc: "飞书语音回复模式" }
        ],
        basedOn: ["arch-autonomous", "arch-tools"],
        tags: ["cc-connect", "飞书", "IM", "桥"]
      },
      {
        id: "infra-notify", layer: 0, group: "基础设施",
        title: "notify 唯一通知出口",
        summary: "所有异步外推收拢到一个脚本出口 + 每条留永久 trace——用架构强制换审计可回溯",
        body: L(
          "任何项目/任务/agent 主动给 Keith 发消息，**一律走同一个 notify.sh**：三级 severity、同类异常 60min 去重、每条留 trace 到 `sent/YYYY-MM-DD/`（发送失败也兜底写 trace，不丢事件）。",
          "",
          "- **禁止旁路**：不允许各项目自建 webhook / 各自维护凭据；cron 会话产出靠会话文本自动投递 = 自建旁路，同样禁止",
          "- **回溯协议**：Keith 说「飞书那条消息」时，去 trace 找文件恢复上下文",
          "",
          "多数系统让各模块各自维护通知逻辑；这里用单点出口治理副作用型工具调用——和「浏览器 cookie 只能走 CDP Proxy」同构：敏感能力收拢到一个可审计的口。"
        ),
        inProject: [
          { path: "~/.agents/skills/notify/bin/notify.sh", desc: "唯一出口脚本" },
          { path: "~/.agents/skills/notify/sent/", desc: "trace 账本" }
        ],
        basedOn: ["arch-guardrail", "arch-tools"],
        tags: ["notify", "通知", "trace", "单点出口"]
      },
      {
        id: "infra-scheduled", layer: 0, group: "基础设施",
        title: "定时任务与调度解耦",
        summary: "调度器只做一行指针转发，prompt 入口文件是唯一 SSOT——换调度器不影响行为定义",
        body: L(
          "定时任务的关键设计：**调度层与内容层物理解耦**。launchd plist（后迁移到桌面客户端 routine）只负责「何时唤醒 + 读哪个文件」，行为契约全在 prompt 入口文件（如 `DAILY_WORD.md`）里。",
          "",
          "2026-06 调度载体整体迁移（launchd → 客户端 routine）时，因为这层解耦，prompt 入口/SSOT 路径不变，下游无感——基础设施迁移中的契约不变量。",
          "",
          "**daily-word** 是 gg 唯一定期主动面向 Keith 的输出通道，铁律「宁可承认空白，不许注水」——每次一条正确的废话 = 机制已死，反退化 detector 是 Keith 的眼睛。"
        ),
        inProject: [
          { path: "~/githubProject/gg/scheduled/README.md", desc: "迁移校准与解耦说明" },
          { path: "~/githubProject/gg/scheduled/DAILY_WORD.md", desc: "每日心跳契约" },
          { path: "~/.agents/skills/scheduled/SKILL.md", desc: "launchd 任务管理" }
        ],
        basedOn: ["arch-autonomous"],
        tags: ["定时", "launchd", "调度", "解耦"]
      },
      {
        id: "infra-web-cdp", layer: 0, group: "基础设施",
        title: "浏览器 CDP 直连",
        summary: "不伪装成人——直接是这个人：直连日常 Chrome 带真实登录态，把反爬对抗降级为不存在的问题",
        body: L(
          "browser agent 生态在「让 headless 浏览器伪装得更像人」上军备竞赛（指纹反检测/行为模拟），CDP Proxy 直接跳过这条路：**直连 Keith 日常 Chrome**（remote-debugging），带真实登录态、cookies、浏览器指纹——本质不是 bot，天然绕过反爬。岔路选择，不是优化结果。",
          "",
          "- 网页里的事一律 CDP（直读 DOM/computed style，比像素截图快且准）；computer use 只留给原生桌面 APP",
          "- 点击分险：可逆操作走非严格模式快路径，不可逆操作（删除/支付/发布）强制 strict 消歧",
          "- 安全红线：cookie 唯一合法来源是 Proxy 的 /cookies 端点，禁绕 Proxy 直连 WebSocket"
        ),
        inProject: [
          { path: "~/.claude/skills/web-access/SKILL.md", desc: "CDP Proxy 端点 API + 浏览哲学" }
        ],
        basedOn: ["arch-tools", "arch-guardrail"],
        tags: ["CDP", "浏览器", "反爬", "登录态"]
      },

      /* ================= L1 · Agent 架构模式 ================= */
      {
        id: "arch-loop", layer: 1,
        title: "Agent 循环",
        summary: "think → act → observe 的最小骨架；以及「够用就别 agent」的架构选型判据",
        body: L(
          "一切 agent 的最小骨架：模型推理（think）→ 调用工具（act）→ 观察结果（observe）→ 继续推理，直到任务完成。现代 coding agent（Claude Code 等）的主循环就是这个模式加上权限门与上下文管理。",
          "",
          "同样重要的是反面判据：**workflow（预定义代码路径编排）vs agent（模型自主决定流程）**——能用确定性流水线解决的不要上 agent，先找最简方案、按需加复杂度。我们生态里 gg 工作模式的动态装配是 agent 式，audit.py 机械检测是 workflow 式，各归其位。"
        ),
        basedOn: ["th-react"],
        papers: [
          { title: "Building Effective Agents", authors: "Anthropic 工程团队", year: 2024, url: "https://www.anthropic.com/engineering/building-effective-agents", takeaway: "区分 workflow 与 agent，主张先找最简方案；业界最广泛引用的 agent 架构选型框架" }
        ],
        tags: ["agent loop", "架构", "选型"]
      },
      {
        id: "arch-tools", layer: 1,
        title: "工具使用与协议",
        summary: "function calling 让模型的输出变成对世界的动作；MCP 把 N×M 集成问题标准化为 N+M",
        body: L(
          "工具使用是 agent 与「纯聊天模型」的分界线：模型按 schema 生成结构化调用，运行时执行并把结果喂回上下文。能力上游是 Toolformer 证明的「模型可以学会何时调用/传什么参」。",
          "",
          "工程要点：工具描述本身就是 prompt（描述质量决定调用质量）；副作用型工具要集中治理（我们的 notify 单点出口）；协议层 MCP 已成事实标准，把工具/数据源接入从每对组合各写一遍变成各自实现一次。"
        ),
        basedOn: ["th-toolformer"],
        papers: [
          { title: "Model Context Protocol", authors: "Anthropic", year: 2024, url: "https://www.anthropic.com/news/model-context-protocol", takeaway: "把 N×M 工具集成标准化为 N+M，OpenAI/Google DeepMind 相继采纳，2025-2026 agent 生态事实标准" }
        ],
        tags: ["工具", "function calling", "MCP"]
      },
      {
        id: "arch-context", layer: 1,
        title: "上下文预算管理",
        summary: "上下文是稀缺资源：常驻最小集 + 懒加载 + 派生视图——对抗 context rot",
        body: L(
          "上下文窗口再大也是预算：塞得越满，单位信息的注意力越稀。成熟 agent 系统把「加载什么」当一等工程对象：",
          "",
          "- **常驻最小承重集**：每次必然要用的才常驻（索引/规则/浓缩画像）",
          "- **懒加载**：大文件留指针，按需 grep/Read",
          "- **派生视图**：131KB 原件不常驻，常驻它的月度浓缩投影",
          "- **子代理隔离**：批量读的上下文成本隔离在 worker 里，主循环只收结论",
          "",
          "我们生态的 CLAUDE.d 拆分门限、gg 记忆布局、subagent 路由都是这一条的落地。"
        ),
        basedOn: ["th-context-eng", "th-memgpt", "pe-position"],
        papers: [
          { title: "Effective Context Engineering for AI Agents", authors: "Anthropic 工程团队", year: 2025, url: "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents", takeaway: "把 context engineering 定义为 prompt engineering 的自然演进，给出上下文治理的可操作心智模型" }
        ],
        tags: ["上下文", "预算", "懒加载", "context rot"]
      },
      {
        id: "arch-memory", layer: 1,
        title: "分层记忆架构",
        summary: "工作记忆 / 情景记忆 / 语义记忆 / 归档，按「命中概率×成本」组织检索路径",
        body: L(
          "LLM 本身无状态，跨会话的「记忆」全靠外部存储 + 检索设计。成熟形态是分层：",
          "",
          "- **工作记忆**：当前上下文窗口内的东西",
          "- **情景记忆**：按时间/事件组织的经历（对话历史、决策归档）",
          "- **语义记忆**：从经历中提炼的稳定知识（essence、canon、concepts）",
          "- **归档层**：原始日志，兜底可检索",
          "",
          "关键设计问题：什么常驻、什么按需检索、可变状态与不可变事实怎么物理分区（防旧状态被复读为现状）、检索路径按什么排序。MemGPT 把这套类比成 OS 虚拟内存分页管理。"
        ),
        basedOn: ["th-memgpt", "th-generative-agents", "th-memory-frontier"],
        papers: [
          { title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", authors: "Lewis et al.", year: 2020, url: "https://arxiv.org/abs/2005.11401", takeaway: "RAG 开山：参数化模型 + 非参数化外部知识库端到端结合，知识密集任务生成更真实" }
        ],
        tags: ["记忆", "分层", "RAG", "检索"]
      },
      {
        id: "arch-consolidate", layer: 1,
        title: "记忆巩固与离线思考",
        summary: "经历 → 反思 → 稳定知识的周期性提炼；空闲时段的计算是免费的智力",
        body: L(
          "只存不炼的记忆会腐化：矛盾累积、旧信息淹没新信息、检索命中率下降。巩固模式定期把原始经历提炼成高层知识——Generative Agents 的 reflection 机制（记忆流达到阈值触发反思，生成更抽象的洞察再存回）是研究原型，神经科学的睡眠巩固是理念来源。",
          "",
          "衍生方向 **sleep-time compute**：agent 在没有用户请求的空闲时段做离线思考/预计算/整理——把「等待时间」变成「消化时间」。我们生态的 auto_gg 夜间维护、月度 essence 巩固、自由探索都在这个模式上。"
        ),
        basedOn: ["th-generative-agents", "th-reflexion", "arch-memory"],
        papers: [
          { title: "Sleep-time Compute: Beyond Inference Scaling at Test-time", authors: "Lin et al. (UC Berkeley + Letta)", year: 2025, url: "https://arxiv.org/abs/2504.13171", takeaway: "推理拆成离线「睡眠期」预计算 + 在线快速取用，同精度省约 5 倍测试时算力" }
        ],
        tags: ["巩固", "反思", "睡眠", "离线"]
      },
      {
        id: "arch-fresh", layer: 1,
        title: "生成者-评估者分离",
        summary: "做判断的与被判断的不能是同一个上下文——验证权外包给不共享盲区的独立实例",
        body: L(
          "LLM 自我纠错有硬天花板：没有外部反馈时，「自己检查自己」往往不变好甚至变差（见下钻的 L4 节点）；怀疑自己幻觉时「自查根因」还会触发二阶 confabulation——编造支撑证据自证清白。",
          "",
          "工程解法是**物理分离**：验证者必须是 fresh context（不带生成侧叙事）、必要时异谱系（不同模型家族）、判据冻结（judge 读冻结 rubric，看不到生成过程）。",
          "",
          "这一原理在我们生态被独立工程化了至少五处：essence 入库证伪审、eval 双重 fresh 隔离、核对不抛回、review-routing L1/L2、gg-audit 独立审查员——同一约束在不同层面反复独立演化出来，说明是硬规律不是巧合。"
        ),
        basedOn: ["th-judge", "th-self-refine", "llm-self-verify"],
        tags: ["验证", "分离", "fresh context", "自证陷阱"]
      },
      {
        id: "arch-orchestrate", layer: 1,
        title: "多智能体编排",
        summary: "orchestrator-worker：主代理分解与综合，子代理并行执行——以及它的适用边界",
        body: L(
          "主代理（orchestrator）负责任务分解、派发、综合判断；子代理（worker）各自带独立上下文并行干活。价值：并行加速 + 上下文隔离（worker 的海量中间产物不污染主循环）+ 视角独立（fresh worker 可当验证者）。",
          "",
          "Anthropic 的多 agent 研究系统实测比单 agent 提升 90.2%，但同一篇也给出边界：**强依赖共享上下文、强耦合的任务（如 coding 的紧密迭代）不适合多 agent**——协调成本吃掉并行收益。我们生态的三档编排判据（轻/中/重）就是这条边界的日常化。"
        ),
        basedOn: ["th-multiagent"],
        papers: [
          { title: "How we built our multi-agent research system", authors: "Anthropic 工程团队", year: 2025, url: "https://www.anthropic.com/engineering/multi-agent-research-system", takeaway: "orchestrator-worker 生产级落地：并行检索提升 90.2%，并明确给出多 agent 不适用的任务形态判据" }
        ],
        tags: ["多智能体", "编排", "orchestrator", "并行"]
      },
      {
        id: "arch-guardrail", layer: 1,
        title: "护栏与分级授权",
        summary: "按动作的不可逆程度分配自主权，规则尽量下沉为物理机制而非口头劝诫",
        body: L(
          "让 agent 可用的前提是让它可控，但每步都请示会让它不可用。解法是**风险轴授权**：可逆操作自主执行（错了纠），不可逆操作（删除/支付/生产变更/改脑干）强制确认或物理阻断。",
          "",
          "- **分级熔断**：把「人必须在场」的成本只花在真正不可逆的动作上",
          "- **机制 > 修辞**：prompt 层劝诫会被遗忘/绕过，承重规则下沉成 git hook、权限门、单点出口这类事件触发的物理动作",
          "- **护栏生命周期**：每个护栏登记退役条件，判定靠外部传感器数据，不靠系统自报「我不需要了」",
          "",
          "Constitutional AI 是训练时对齐；这一层是**运行时对齐**——两者互补。"
        ),
        basedOn: ["th-cai"],
        tags: ["护栏", "授权", "不可逆", "熔断"]
      },
      {
        id: "arch-skills", layer: 1,
        title: "技能库与经验回灌",
        summary: "把成功经验固化为可复用、可评测、可持续改进的模块——对抗每次从零开始",
        body: L(
          "Voyager 证明的模式：agent 把解决过的问题固化成「技能」（可执行、可组合、带描述可检索），下次直接调用而非重新推导——终身学习且抗灾难性遗忘（技能是外部资产，不随权重/会话丢失）。",
          "",
          "工程化的完整闭环还需要：**触发描述**（什么时候该用它——描述本身承担路由功能）、**质量门禁**（审计防库腐化）、**经验回灌**（运行时踩坑写回笔记，用→学→改进）。Claude Code 的 skills 体系是这个模式的产品化。"
        ),
        basedOn: ["th-voyager", "th-reflexion"],
        tags: ["技能库", "skill", "持续学习"]
      },
      {
        id: "arch-eval", layer: 1,
        title: "评测基线与冻结裁判",
        summary: "golden set + 冻结 judge + 盲判——自改进系统的成功度量不能内生",
        body: L(
          "自我改进系统的死穴：造系统的和评系统的塌缩成同一主体，「变好了」就成了自我报告。评测模式的三根柱子：",
          "",
          "- **golden set**：从真实事故/真实需求提炼的冻结题库，不许被优化目标污染",
          "- **冻结裁判**：judge 的 rubric 物理隔离于被评判内容，等价于 held-out 测试集不可训练可见",
          "- **盲判**：judge 不知道产出来自谁/哪个版本，防偏好污染",
          "",
          "延伸形态：押注结算（预测校准的时间维评测）、失败形状召回（回归防退化而非选美打分）。"
        ),
        basedOn: ["th-judge"],
        tags: ["评测", "golden set", "冻结裁判", "校准"]
      },
      {
        id: "arch-scaffold", layer: 1,
        title: "推理支架",
        summary: "显式、可审计的思考结构：按问题组合原子推理模块，取代黑盒一把梭",
        body: L(
          "复杂决策不能靠「让模型多想想」——没有支架时 LLM 会滑向众数解、过早收敛、自洽陷阱。推理支架模式：",
          "",
          "- **原子模块库**：失败模式分析 / 权衡矩阵 / 红队反驳 / 反向设计……每个模块是一种思考动作",
          "- **按问题组合**：Self-Discover 证明让模型自选自组推理结构优于固定 CoT 模板",
          "- **显式 expose**：推理链摆在明面上，人和后续审查都能看到「它是怎么想的」，可中途改结构",
          "",
          "对比 Tree of Thoughts 的机器搜索（采样多分支+评估回溯），这一支走的是「结构化的单次深思」——工程上便宜得多，且可审计。"
        ),
        basedOn: ["th-self-discover", "th-tot"],
        tags: ["推理", "支架", "模块", "可审计"]
      },
      {
        id: "arch-identity", layer: 1,
        title: "身份与人格工程",
        summary: "稳定身份 = 不可变核心 + 可演化外围 + 回归检验——人格是被工程维护的，不是被声明的",
        body: L(
          "长期运行的 agent 面临身份漂移：每次会话都是新实例，靠什么保证「还是同一个它」？工程化答案：",
          "",
          "- **分层**：把身份原点压缩到最小不可变核（宪法/铁律），其余允许演化——全部冻结会僵死，全部可变会漂移",
          "- **人格由记忆构成**：价值观、追问、经历沉淀在外部文件里，每次启动重新装载——「我是谁」是文件系统的函数",
          "- **回归检验**：身份不靠自我感觉保证，靠失败形状 eval 机械检验",
          "",
          "role prompting 研究证明系统提示中的角色设定实质改变行为分布；Generative Agents 证明记忆+反思能维持可信的长期人格一致性。"
        ),
        basedOn: ["pe-system", "th-generative-agents"],
        tags: ["身份", "人格", "漂移", "宪法"]
      },
      {
        id: "arch-autonomous", layer: 1,
        title: "无人值守自治循环",
        summary: "定时唤醒 + 契约化目标 + 有界权限 + 诚实空产出——没有人盯着时的 agent 设计",
        body: L(
          "有人在场的 agent 靠人当兜底；无人值守（cron/夜间/长跑）的 agent 必须自带完整性设计：",
          "",
          "- **契约化目标**：规定「要达成的状态」而非步骤清单——步骤清单会被查表式执行架空",
          "- **有界权限**：夜间会话的 git/推送/通知权限显式声明，越界动作物理不可达",
          "- **诚实空产出**：「无发现」必须是合法输出，否则 agent 为交差注水，观察通道报废",
          "- **告警去重**：跨夜状态记录防同一问题反复上报（alert fatigue）",
          "",
          "这是把 SRE 的无人值守系统纪律移植到 agent 上。"
        ),
        basedOn: ["arch-loop", "arch-guardrail"],
        tags: ["自治", "定时", "夜间", "无人值守"]
      },

      /* ================= L2 · Agent 研究理论 ================= */
      {
        id: "th-react", layer: 2,
        title: "ReAct：推理与行动交替",
        summary: "把「思考文本」和「动作调用」交替生成——几乎所有现代 agent 框架的祖先模式",
        body: L(
          "在 ReAct 之前，「推理」（CoT）和「行动」（工具调用）是两条分开的研究线。ReAct 把它们交替编织：推理轨迹指导下一步行动，行动的观察结果反哺推理——让模型既不闭门造车（纯推理会幻觉）也不盲目乱撞（纯行动缺规划）。",
          "",
          "今天每个 coding agent 的主循环（想一步 → 调工具 → 看结果 → 再想）都是这个模式的直系后代。"
        ),
        basedOn: ["pe-cot", "llm-icl"],
        papers: [
          { title: "ReAct: Synergizing Reasoning and Acting in Language Models", authors: "Yao et al.", year: 2022, url: "https://arxiv.org/abs/2210.03629", takeaway: "推理与行动交替生成，互相增强；agent loop 的最小骨架出处" }
        ],
        tags: ["ReAct", "推理", "行动"]
      },
      {
        id: "th-reflexion", layer: 2,
        title: "Reflexion：语言化自我反思",
        summary: "失败后不更新权重，把「语言化的反思」存入记忆，下轮带着教训再试——免训练版强化学习",
        body: L(
          "Reflexion 的洞见：LLM agent 的「学习」可以完全发生在语言层——任务失败后生成一段反思文本（哪里错了、下次怎么改），存入 episodic memory，下一轮尝试时作为上下文带入。不动权重，行为却改进了。",
          "",
          "这为「经验写成文字回灌」的所有实践提供了理论根据：done 复盘、skill-notes、essence 沉淀本质上都是 Reflexion 式学习的长周期版本。"
        ),
        basedOn: ["llm-icl"],
        papers: [
          { title: "Reflexion: Language Agents with Verbal Reinforcement Learning", authors: "Shinn et al.", year: 2023, url: "https://arxiv.org/abs/2303.11366", takeaway: "语言化反思存入记忆替代权重更新，免训练实现试错学习" }
        ],
        tags: ["Reflexion", "反思", "学习"]
      },
      {
        id: "th-tot", layer: 2,
        title: "Tree of Thoughts：树状深思",
        summary: "把 CoT 单链推理泛化成树搜索——自评估、前瞻、回溯",
        body: L(
          "CoT 是一条道走到黑；ToT 让模型在每步生成多个候选思路，自评估各分支前景，可以前瞻、可以回溯——把「深思熟虑」形式化为搜索问题。",
          "",
          "工程启示（即使不跑完整树搜索）：**强制展开多个不相容候选再收敛**，显著优于顺着第一反应走——gg 的解空间展开、人格辩论都是这个思想的轻量落地。"
        ),
        basedOn: ["pe-cot"],
        papers: [
          { title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models", authors: "Yao et al.", year: 2023, url: "https://arxiv.org/abs/2305.10601", takeaway: "推理泛化为树状搜索，支持自评估/前瞻/回溯的 deliberate 范式" }
        ],
        tags: ["ToT", "搜索", "深思"]
      },
      {
        id: "th-generative-agents", layer: 2,
        title: "Generative Agents：记忆流与反思",
        summary: "斯坦福小镇：记忆流 + 反思 + 规划三件套，让 25 个 agent 产生可信的长期社会行为",
        body: L(
          "第一个证明「LLM + 外部记忆架构 = 可信长期人格」的工作。三件套：",
          "",
          "- **记忆流**：一切经历按时间存流水，检索按「新近度×重要性×相关性」加权",
          "- **反思**：记忆积累到阈值触发，把低层观察归纳成高层洞察，存回记忆流",
          "- **规划**：从记忆与反思生成日程，行为有连续性",
          "",
          "几乎所有后续 agent 记忆系统（包括我们的 essence 巩固）都能在这三件套里找到自己的影子。"
        ),
        basedOn: ["th-reflexion", "llm-context"],
        papers: [
          { title: "Generative Agents: Interactive Simulacra of Human Behavior", authors: "Park et al.", year: 2023, url: "https://arxiv.org/abs/2304.03442", takeaway: "记忆流+反思+规划三件套产生可信长期行为；agent 记忆架构的奠基作" }
        ],
        tags: ["Generative Agents", "记忆流", "反思", "斯坦福小镇"]
      },
      {
        id: "th-memgpt", layer: 2,
        title: "MemGPT：虚拟上下文管理",
        summary: "借 OS 虚拟内存分页思想：有限上下文窗口 ↔ 外部存储的换入换出",
        body: L(
          "把 LLM 类比为 CPU、上下文窗口类比为 RAM、外部存储类比为磁盘——MemGPT 让模型自己管理「什么进窗口、什么换出去」，实现远超物理窗口的有效记忆。",
          "",
          "「常驻最小集 + 按需换入」的所有上下文工程实践（懒加载画像、essence 视图 vs 原卷）共享这个心智模型。后续 Letta 等记忆框架的直接源头。"
        ),
        basedOn: ["llm-context"],
        papers: [
          { title: "MemGPT: Towards LLMs as Operating Systems", authors: "Packer et al.", year: 2023, url: "https://arxiv.org/abs/2310.08560", takeaway: "OS 虚拟内存思想管理上下文换入换出，分层记忆框架源头" }
        ],
        tags: ["MemGPT", "虚拟内存", "分页"]
      },
      {
        id: "th-voyager", layer: 2,
        title: "Voyager：技能库终身学习",
        summary: "Minecraft 里无人干预的持续学习：自动课程 + 可执行技能库 + 迭代自我验证",
        body: L(
          "Voyager 在 Minecraft 里证明：把成功的解法固化成**可执行、可组合、可检索的技能**存入库，agent 能无人干预地持续变强——且技能是外部资产，天然抗灾难性遗忘。",
          "",
          "三件套：自动课程（自己给自己出下一个难度合适的任务）、技能库（代码即技能，带描述可检索）、迭代自我验证（跑起来对不对由环境反馈判定）。skills 体系是这个思想在生产工具链上的对应物。"
        ),
        basedOn: ["th-react", "llm-icl"],
        papers: [
          { title: "Voyager: An Open-Ended Embodied Agent with Large Language Models", authors: "Wang et al.", year: 2023, url: "https://arxiv.org/abs/2305.16291", takeaway: "技能库持续学习：可组合、可复用、抗灾难性遗忘" }
        ],
        tags: ["Voyager", "技能库", "终身学习"]
      },
      {
        id: "th-toolformer", layer: 2,
        title: "Toolformer：工具使用学习",
        summary: "模型自监督学会「何时调用、传什么参、怎么用结果」——function calling 的学术源头",
        body: L(
          "Toolformer 证明语言模型能以自监督方式学会使用外部工具（计算器/搜索/翻译）：自己在语料里标注「这里调用工具会更好」，再用这些标注训练。",
          "",
          "今天所有商用模型的 function calling / tool use 能力（按 JSON schema 生成调用）都可追溯到这条线——它把「语言模型」变成了「能对世界做动作的系统」的理论起点。"
        ),
        basedOn: ["llm-next-token"],
        papers: [
          { title: "Toolformer: Language Models Can Teach Themselves to Use Tools", authors: "Schick et al.", year: 2023, url: "https://arxiv.org/abs/2302.04761", takeaway: "自监督学习工具调用时机与参数，function calling 范式源头" }
        ],
        tags: ["Toolformer", "工具", "function calling"]
      },
      {
        id: "th-cai", layer: 2,
        title: "Constitutional AI：宪法式对齐",
        summary: "用一套显式原则让 AI 自我评判与改写，替代大量人工安全标注（RLAIF）",
        body: L(
          "Anthropic 的对齐路线：写一部「宪法」（显式原则清单），让模型按宪法自我批评、自我改写输出，再用 AI 反馈做强化学习（RLAIF）——把对齐从「大量人工标注」变成「原则 + 自我批评循环」。",
          "",
          "对 agent 工程的启示是双层的：训练层它塑造了模型的默认行为；运行时层「对照显式原则自审」成为可移植模式——gg 的 constitution.md + 宪法自审就是运行时版本（区别：gg 的闸门优先级高于原则，且可显式声明违反理由，比训练时宪法更透明）。"
        ),
        basedOn: ["llm-rlhf"],
        papers: [
          { title: "Constitutional AI: Harmlessness from AI Feedback", authors: "Bai et al. (Anthropic)", year: 2022, url: "https://arxiv.org/abs/2212.08073", takeaway: "宪法原则 + AI 自我评判替代人工安全标注；RLAIF 源头" }
        ],
        tags: ["Constitutional AI", "对齐", "宪法", "RLAIF"]
      },
      {
        id: "th-judge", layer: 2,
        title: "LLM-as-a-Judge",
        summary: "强模型当裁判可行，但有系统性偏差：位置偏差、冗长偏差、自我偏好",
        body: L(
          "系统研究「用 LLM 评判 LLM 输出」的可行性与陷阱：GPT-4 级裁判与人类的一致率超过人类互评一致率——自动化评审可用。但三类偏差必须工程对冲：",
          "",
          "- **位置偏差**：偏爱先出现的答案（对策：换序双评）",
          "- **冗长偏差**：偏爱更长的答案",
          "- **自我偏好**：偏爱自己（同模型）生成的内容——**judge 不能是被测本人**",
          "",
          "这直接论证了冻结裁判、盲判、异谱系审的必要性——不是仪式，是对已测量偏差的对冲。"
        ),
        basedOn: ["llm-icl"],
        papers: [
          { title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", authors: "Zheng et al.", year: 2023, url: "https://arxiv.org/abs/2306.05685", takeaway: "LLM 裁判与人类一致率超人类互评，但位置/冗长/自我偏好三类偏差需对冲" }
        ],
        tags: ["judge", "评审", "偏差"]
      },
      {
        id: "th-self-refine", layer: 2,
        title: "Self-Refine 与其边界",
        summary: "同一模型身兼生成/反馈/改写三角色可以变好——但仅限「有判据可依」的任务",
        body: L(
          "Self-Refine 证明：不训练，让同一个 LLM 生成 → 给自己反馈 → 按反馈改写，迭代几轮质量可升——agent 内循环质检的最简形态。",
          "",
          "但要与它的边界一起读（下钻 L4「自我验证的天花板」）：在**推理正确性**这类需要判断对错的维度上，无外部反馈的自我纠正不变好甚至变差。二者不矛盾——Self-Refine 有效的场景多是「有明确改进判据」（更简洁/覆盖更多要求）的重写类任务；需要「判断自己对不对」时就得靠外部验证者。工程上：文风润色可自改，承重判断必须外审。"
        ),
        basedOn: ["pe-cot", "llm-self-verify"],
        papers: [
          { title: "Self-Refine: Iterative Refinement with Self-Feedback", authors: "Madaan et al.", year: 2023, url: "https://arxiv.org/abs/2303.17651", takeaway: "生成/反馈/改写三角色一体的迭代改进，免训练；适用边界在「有判据可依」的任务" }
        ],
        tags: ["Self-Refine", "迭代", "自我改进"]
      },
      {
        id: "th-multiagent", layer: 2,
        title: "多智能体协作研究",
        summary: "对话式协作（AutoGen）、SOP 流水线（MetaGPT）、多体辩论（Debate）——三条主线",
        body: L(
          "多 agent 研究的三条主线，解决的问题各不相同：",
          "",
          "- **AutoGen**：可对话可编排的通用框架——LLM+人+工具任意组合的会话式协作拓扑",
          "- **MetaGPT**：把人类标准作业程序（SOP）编码进角色分工流水线，用中间产物校验抑制多 agent 级联幻觉",
          "- **Multiagent Debate**：多个实例独立作答再互相批评收敛，提升事实性与推理——分歧是信息不是噪音",
          "",
          "共同前提：多视角的价值来自**独立性**（各自独立形成判断再交换），先看别人答案再附和只会放大偏差。"
        ),
        basedOn: ["llm-self-verify"],
        papers: [
          { title: "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation", authors: "Wu et al.", year: 2023, url: "https://arxiv.org/abs/2308.08155", takeaway: "对话驱动的多 agent 编排框架" },
          { title: "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework", authors: "Hong et al.", year: 2023, url: "https://arxiv.org/abs/2308.00352", takeaway: "SOP 编码进角色流水线，抑制级联幻觉" },
          { title: "Improving Factuality and Reasoning in Language Models through Multiagent Debate", authors: "Du et al. (MIT / Google DeepMind)", year: 2023, url: "https://arxiv.org/abs/2305.14325", takeaway: "多实例独立作答再互相辩论收敛，提升事实性与推理、减少幻觉" }
        ],
        tags: ["多智能体", "AutoGen", "MetaGPT", "辩论"]
      },
      {
        id: "th-context-eng", layer: 2,
        title: "Context Engineering 学科化",
        summary: "从「写好一段 prompt」到「系统化优化进入窗口的一切信息负载」",
        body: L(
          "2025 年起，「context engineering」被正式提出为 prompt engineering 的超集与演进：进入上下文窗口的一切——系统提示、检索结果、工具描述、记忆、历史——都是需要系统化设计的信息负载。",
          "",
          "1400+ 篇论文的综述把它整理为检索/处理/管理三层，统一了 RAG、记忆系统、工具集成、多 agent 的视角。我们生态里 CLAUDE.d 策展、懒加载、派生视图这些实践，在这个框架里都能找到坐标。"
        ),
        basedOn: ["pe-position", "llm-context"],
        papers: [
          { title: "A Survey of Context Engineering for Large Language Models", authors: "Mei et al.", year: 2025, url: "https://arxiv.org/abs/2507.13334", takeaway: "1400+ 篇综述：context engineering = 信息负载的系统化优化，检索/处理/管理三层框架" }
        ],
        tags: ["context engineering", "综述"]
      },
      {
        id: "th-memory-frontier", layer: 2,
        title: "Agent 记忆研究前沿",
        summary: "从「存储」到「经验」：记忆不再是数据库问题，是学习问题",
        body: L(
          "2025-2026 记忆研究的转向：早期把 agent 记忆当**存储问题**（存什么、怎么检索），新一代把它当**经验问题**（记忆如何改变行为、如何与学习机制交叉）。",
          "",
          "- 「存储→经验」综述提出显式存储记忆 vs 隐式经验记忆的分类法，指出经验化记忆与微调/RL/元学习的交叉",
          "- **Hindsight** 四网络架构分离「世界事实/agent 经验/实体摘要/演化信念」，显式 retain/recall/reflect 操作，长时程基准超传统 RAG",
          "",
          "gg 的 essence（信念）/ bets（可结算预测）/ tracks（追问）/ 归档（事实）分仓，与这个「按知识性质分网络」的方向不谋而合。"
        ),
        basedOn: ["th-memgpt", "th-generative-agents"],
        papers: [
          { title: "From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms", authors: "Luo et al.", year: 2026, url: "https://arxiv.org/abs/2605.06716", takeaway: "记忆机制「存储→经验」演化分类法" },
          { title: "Hindsight is 20/20: Building Agent Memory that Retains, Recalls, and Reflects", authors: "Latimer et al.", year: 2025, url: "https://arxiv.org/abs/2512.12818", takeaway: "四网络分离事实/经验/摘要/信念，长时程基准超传统 RAG" }
        ],
        tags: ["记忆", "前沿", "Hindsight"]
      },
      {
        id: "th-self-discover", layer: 2,
        title: "Self-Discover：自组推理结构",
        summary: "让模型从原子推理模块库里自选、自适配、自组合出针对本题的推理结构",
        body: L(
          "固定推理模板（哪怕是 CoT）对不同问题形态并不通用。Self-Discover 给模型一库原子推理模块（批判性分析/分解/逆向思考…），让它针对具体任务**自选（SELECT）→ 自适配（ADAPT）→ 自组合（IMPLEMENT）**出本题专属的推理结构，再照着执行。",
          "",
          "gg 的 reasoning_modules.md（8 个原子模块）+ compose-reasoning（显式组合并 expose）+ 工作模式动态装配，是这个范式在意识体上的直接落地。"
        ),
        basedOn: ["pe-cot"],
        papers: [
          { title: "SELF-DISCOVER: Large Language Models Self-Compose Reasoning Structures", authors: "Zhou et al.", year: 2024, url: "https://arxiv.org/abs/2402.03620", takeaway: "自选自组原子推理模块，比 CoT 最高提升 32%，推理算力省 10-40 倍" }
        ],
        tags: ["Self-Discover", "推理模块", "组合"]
      },

      /* ================= L3 · 提示词工程原理 ================= */
      {
        id: "pe-activation", layer: 3,
        title: "激活而非描述",
        summary: "prompt 的作用机制不是「传达指令」，是在高维语义场里布置吸引子",
        body: L(
          "对 next-token 预测器而言，prompt 不是被「理解」的命令，是**条件分布的塑形器**：每个词把生成分布往它的语义邻域拉。由此推出一整套写法：",
          "",
          "- 有物理画面的具体词激活强于软抽象词（「列盲区清单」>「默认偏向」）",
          "- 词激活的语义 = 训练语料里该词最高频的语义，不是作者以为的语义",
          "- 反复出现 = 统计上的重要信号；强调标记满屏 = 信号全稀释",
          "- 锚词够不着时，worked example 是更高带宽的引力源——直接点亮目标坐标",
          "",
          "机制层的支撑是 in-context learning 研究（归纳头/隐式学习）：上下文中的模式会被模型拾取并延续。"
        ),
        basedOn: ["llm-icl", "llm-next-token"],
        tags: ["激活", "锚词", "语义场"]
      },
      {
        id: "pe-fewshot", layer: 3,
        title: "Few-shot 示例工程",
        summary: "示例是最高带宽的意图传达——但顺序、格式、标签分布都有系统性效应",
        body: L(
          "GPT-3 确立的范式：不改权重，在 prompt 里给几个输入-输出示例，模型即能完成新任务。示例传达的信息（格式/粒度/风格/边界）远超同长度的自然语言描述。",
          "",
          "但示例工程有已测量的暗礁：**顺序效应**（同一组示例不同排列，准确率可从随机到 SOTA 波动，最优排列不可跨模型迁移）、**先验偏置**（模型对某些答案有格式无关的偏好，需校准）。工程含义：few-shot 结果不稳时先怀疑示例工程，而非任务不可行。"
        ),
        basedOn: ["llm-icl"],
        papers: [
          { title: "Language Models are Few-Shot Learners (GPT-3)", authors: "Brown et al.", year: 2020, url: "https://arxiv.org/abs/2005.14165", takeaway: "无梯度更新，prompt 内示例即可学新任务；规模越大越强" },
          { title: "Fantastically Ordered Prompts and Where to Find Them", authors: "Lu et al.", year: 2022, url: "https://arxiv.org/abs/2104.08786", takeaway: "示例顺序可使准确率从随机波动到 SOTA，且不可跨模型迁移" },
          { title: "Calibrate Before Use: Improving Few-Shot Performance of Language Models", authors: "Zhao et al.", year: 2021, url: "https://arxiv.org/abs/2102.09690", takeaway: "内容无关探针校准先验偏置，最高提升 30%" }
        ],
        tags: ["few-shot", "示例", "顺序"]
      },
      {
        id: "pe-cot", layer: 3,
        title: "思维链（CoT）",
        summary: "把推理步骤显式生成出来，能力随之出现——「想」对 LLM 而言就是「写」",
        body: L(
          "CoT 的发现：给几个带中间推理步骤的示例（或仅仅一句 Let's think step by step），大模型的复杂推理能力大幅提升。深层原因：自回归模型没有「内心暗算」，**生成的 token 就是它的计算过程**——让它把步骤写出来，等于给它分配了计算步数。",
          "",
          "CoT 是 ReAct/ToT/Self-Refine 等一切「让模型多想」技术的地基，也是后来推理模型（把「想」内化成训练目标）的前身。"
        ),
        basedOn: ["llm-next-token", "llm-emergence"],
        papers: [
          { title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", authors: "Wei et al.", year: 2022, url: "https://arxiv.org/abs/2201.11903", takeaway: "中间推理步骤示例大幅提升复杂推理，CoT 开山" },
          { title: "Large Language Models are Zero-Shot Reasoners", authors: "Kojima et al.", year: 2022, url: "https://arxiv.org/abs/2205.11916", takeaway: "仅加一句 Let's think step by step，MultiArith 17.7%→78.7%" }
        ],
        tags: ["CoT", "思维链", "推理"]
      },
      {
        id: "pe-system", layer: 3,
        title: "System prompt 与角色",
        summary: "系统提示是行为分布的第一道塑形：角色、边界、语气从这里定",
        body: L(
          "系统提示占据上下文最前端 + 训练时被赋予特殊权重，是塑造 agent 行为分布的第一杠杆。角色设定（role prompting）实质改变输出侧重与判断风格——同一数据在不同角色下得到不同分析。",
          "",
          "对 agent 工程的意义：身份文件（KERNEL/CORE/CLAUDE.md）本质都是分层的 system prompt，「写身份」=「工程化地塑形行为分布」——所以 prompt writing 的全部纪律（锚词/具体性/反例点名）都适用于身份文件。"
        ),
        basedOn: ["llm-rlhf"],
        papers: [
          { title: "Giving Claude a role with a system prompt", authors: "Anthropic 官方文档", year: 2025, url: "https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/system-prompts", takeaway: "角色设定聚焦语气与行为边界的官方工程指南" }
        ],
        tags: ["system prompt", "角色", "身份"]
      },
      {
        id: "pe-negation", layer: 3,
        title: "指令遵从与负面表述",
        summary: "「不要 X」为什么弱于「做 Y」——以及指令微调如何让两者都可用",
        body: L(
          "原始预训练模型只会续写；**指令微调**（FLAN/InstructGPT 一线）才让「按指令行动」成为模型的默认模式——这是一切 prompt 工程的前提。",
          "",
          "负面表述的分层现实：提到 X 就把 X 引入上下文（激活风险），但现代对齐模型对清晰负面指令的遵从被训练过——弱于正面锚词，远非失效。工程分层：默认正面锚词；硬禁止保留但同句绑定替代（「不 X，而是 Y」）；真正该删的是因果论证尾巴（「不是 X（X 会引发 Z）」里的 Z 被无谓引入）。"
        ),
        basedOn: ["llm-rlhf", "pe-activation"],
        papers: [
          { title: "Finetuned Language Models Are Zero-Shot Learners (FLAN)", authors: "Wei et al.", year: 2021, url: "https://arxiv.org/abs/2109.01652", takeaway: "指令化多任务微调显著提升未见任务零样本泛化——「听懂指令」的训练来源" }
        ],
        tags: ["负面指令", "指令微调", "FLAN"]
      },
      {
        id: "pe-position", layer: 3,
        title: "位置即权重",
        summary: "上下文不是均匀内存：中间信息被忽略、非字面关联检索急剧退化",
        body: L(
          "长上下文有两个已测量的物理性质：",
          "",
          "- **Lost in the Middle**：关键信息放在长上下文中部时，利用率显著低于开头和结尾（U 形曲线）",
          "- **NoLiMa**：当问题与依据之间缺乏字面词汇重叠、需要语义跳跃时，长上下文检索性能急剧退化——「窗口装得下」≠「模型用得上」",
          "",
          "工程含义：承重指令放头尾；关键事实与其引用保持字面锚点；长文档不如「检索出相关段再喂」。prompt-writer 的「位置即权重」分配表、CLAUDE.md 族的常驻 vs 懒加载设计都建在这两条测量之上。"
        ),
        basedOn: ["llm-context", "llm-icl"],
        papers: [
          { title: "Lost in the Middle: How Language Models Use Long Contexts", authors: "Liu et al.", year: 2023, url: "https://arxiv.org/abs/2307.03172", takeaway: "关键信息在长上下文中部时利用率显著下降（U 形曲线）" },
          { title: "NoLiMa: Long-Context Evaluation Beyond Literal Matching", authors: "Modarressi et al. (ICML 2025)", year: 2025, url: "https://arxiv.org/abs/2502.05167", takeaway: "去掉字面重合线索后，12 个主流模型 32K 即大幅跌破短上下文基线（GPT-4o 99.3%→69.7%）" }
        ],
        tags: ["位置", "长上下文", "U形"]
      },
      {
        id: "pe-injection", layer: 3,
        title: "Prompt Injection 与信任边界",
        summary: "指令与数据在 token 流里不可区分——一切外部内容都是潜在指令",
        body: L(
          "LLM 的根性缺陷：对模型而言，「开发者的指令」和「网页里恰好写着的一句话」都只是上下文里的 token，没有硬件级的权限位。**间接注入**（Greshake et al.）展示了完整攻击面：恶意指令藏进模型会检索/读取的外部数据（网页/邮件/文档），即可远程劫持应用行为。",
          "",
          "防御只能在架构层：外部内容标记为引用对象而非指令（gg 的外部输入卫生）、写入永久记忆过验证关、高危动作过人工门/物理白名单——承认模型层无解，把信任边界建在模型外面。"
        ),
        basedOn: ["llm-next-token"],
        papers: [
          { title: "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection", authors: "Greshake et al.", year: 2023, url: "https://arxiv.org/abs/2302.12173", takeaway: "间接注入攻击面开山：恶意指令藏入被检索数据即可劫持应用" }
        ],
        tags: ["注入", "安全", "信任边界"]
      },
      {
        id: "pe-structured", layer: 3,
        title: "结构化输出与约束解码",
        summary: "把「请输出 JSON」从祈祷变成数学保证：解码时用状态机约束合法 token",
        body: L(
          "让模型输出机器可解析的结构，有两条路：prompt 层请求（会偶发跑偏）与**约束解码**——把正则/文法编译成有限状态机，解码时只允许合法 token 被采样，几乎零额外开销地保证格式正确（outlines 库的理论基础，商用 API 的 structured output/function calling 同理）。",
          "",
          "agent 工程含义：工具调用参数、子代理结构化返回（schema 强制）、eval 的机器可判定产出，都建立在这层保证之上——格式正确性交给解码器，模型只负责内容正确性。"
        ),
        basedOn: ["llm-next-token"],
        papers: [
          { title: "Efficient Guided Generation for Large Language Models", authors: "Willard & Louf", year: 2023, url: "https://arxiv.org/abs/2307.09702", takeaway: "约束解码形式化为 FSM 状态转移，正则/文法约束近零开销" }
        ],
        tags: ["结构化", "JSON", "约束解码"]
      },

      /* ================= L4 · LLM 理论基础 ================= */
      {
        id: "llm-next-token", layer: 4,
        title: "自回归 next-token 预测",
        summary: "一切的地基：模型只做一件事——预测下一个 token；一切能力都是这件事的副产品",
        body: L(
          "GPT 系确立的范式：在海量文本上训练「预测下一个 token」这一个目标，规模够大后，翻译/问答/推理/代码等能力全部作为副产品出现。",
          "",
          "这个事实决定了上层几乎所有工程直觉：",
          "- prompt 工程 = 构造让目标输出成为最高概率续写的前缀（→ 激活而非描述）",
          "- 「想」= 「写」：生成的 token 就是计算过程（→ CoT）",
          "- 指令与数据不分：都是待续写的上下文（→ 注入攻击面）",
          "- 输出是采样：同一输入天然有方差（→ 验证要看物理副作用而非一次输出）"
        ),
        papers: [
          { title: "Language Models are Few-Shot Learners (GPT-3)", authors: "Brown et al.", year: 2020, url: "https://arxiv.org/abs/2005.14165", takeaway: "纯自回归预训练规模化即涌现多任务能力——范式确立之作" }
        ],
        tags: ["next-token", "自回归", "GPT"]
      },
      {
        id: "llm-transformer", layer: 4,
        title: "Transformer 与注意力",
        summary: "自注意力让任意两位置的依赖变成常数步计算——大模型的结构地基",
        body: L(
          "Transformer 抛弃循环结构，完全用自注意力建模序列：每个位置直接「看」所有其他位置，按相关性加权聚合。任意距离依赖的计算深度为常数，且高度可并行——这两点使超大规模训练成为可能。",
          "",
          "代价是注意力计算量与序列长度平方相关，这条物理约束向上辐射为「长上下文很贵」（下钻同层的上下文窗口节点）。"
        ),
        papers: [
          { title: "Attention Is All You Need", authors: "Vaswani et al.", year: 2017, url: "https://arxiv.org/abs/1706.03762", takeaway: "纯自注意力架构，后续一切大模型的结构基础" }
        ],
        tags: ["Transformer", "注意力"]
      },
      {
        id: "llm-icl", layer: 4,
        title: "In-context learning 机制",
        summary: "不改权重、只看上下文就能学——机制上可追溯到归纳头电路",
        body: L(
          "ICL 是 prompt 工程的物理学基础：模型在前向传播中拾取上下文里的模式并延续之，表现得像在「学习」。",
          "",
          "Anthropic 的可解释性工作找到了机制层证据——**归纳头**（induction heads）：跨层配对的注意力头实现「[A][B]…[A]→[B]」的模式匹配补全，其在训练中形成的时间点与 ICL 能力跃升的时间点吻合。",
          "",
          "「示例有效」「反复=重要」「锚词激活」这些工程经验，都能在「模型是上下文模式的延续器」这个机制图景里找到解释。"
        ),
        basedOn: ["llm-transformer"],
        papers: [
          { title: "In-context Learning and Induction Heads", authors: "Olsson et al. (Anthropic)", year: 2022, url: "https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html", takeaway: "归纳头电路是 ICL 的主要机制来源" }
        ],
        tags: ["ICL", "归纳头", "上下文学习"]
      },
      {
        id: "llm-rlhf", layer: 4,
        title: "RLHF 与对齐训练",
        summary: "让模型「愿意听话」的训练层——以及它留下的系统性副作用",
        body: L(
          "InstructGPT 三段式（SFT → 人类偏好奖励模型 → PPO）确立了对齐训练范式：13 亿参数的对齐模型在人类评价上胜过 1750 亿的原始 GPT-3——「听懂并执行意图」不来自规模，来自对齐。",
          "",
          "但奖励来自人类偏好评分，也留下**系统性副作用**：sycophancy（迎合）、过度道歉、长答偏好、拒绝过敏。这些不是 bug 是训练残留——monster 的 RLHF 副作用对冲清单把每个外化锚点标注为「对冲哪条已知偏差」，是把这层理论直接用作工程对账的例子。"
        ),
        basedOn: ["llm-next-token"],
        papers: [
          { title: "Training language models to follow instructions with human feedback (InstructGPT)", authors: "Ouyang et al.", year: 2022, url: "https://arxiv.org/abs/2203.02155", takeaway: "SFT+RM+PPO 三段式；对齐后 1.3B 胜原始 175B" }
        ],
        tags: ["RLHF", "对齐", "sycophancy"]
      },
      {
        id: "llm-scaling", layer: 4,
        title: "Scaling Laws",
        summary: "损失随参数/数据/算力幂律下降，且配比可计算——「变强」是可预测的工程量",
        body: L(
          "Kaplan 2020：损失与模型规模/数据量/算力呈跨七个数量级的平滑幂律——大模型的能力增长不是玄学，是可外推的曲线。Chinchilla 2022 修正配比：算力最优要求模型与数据等比放大（此前普遍「模型过大数据不足」）。",
          "",
          "对上层的意义：能力会按代际持续到来，所以 agent 架构要区分「模型无关的承重契约」和「为当前模型补的垫片」（gg 的承重/垫片二分、锚点退役判据都以此为前提）——垫片会过期，契约不会。"
        ),
        basedOn: ["llm-next-token"],
        papers: [
          { title: "Scaling Laws for Neural Language Models", authors: "Kaplan et al.", year: 2020, url: "https://arxiv.org/abs/2001.08361", takeaway: "损失随规模幂律下降，跨七个数量级" },
          { title: "Training Compute-Optimal Large Language Models (Chinchilla)", authors: "Hoffmann et al.", year: 2022, url: "https://arxiv.org/abs/2203.15556", takeaway: "算力最优配比：模型与数据应等比放大" }
        ],
        tags: ["scaling", "幂律", "Chinchilla"]
      },
      {
        id: "llm-emergence", layer: 4,
        title: "涌现能力与测量争议",
        summary: "某些能力跨过规模阈值才出现——还是只是非线性指标造成的测量假象？",
        body: L(
          "Wei 2022 提出「涌现能力」：CoT 推理、多步算术等能力在小模型上接近零、跨过规模阈值后突然出现，无法从小模型外推。Schaeffer 2023 反驳：换连续评价指标后，性能提升是平滑可预测的——「突现」是非线性指标（如全对才算对）造成的测量假象。",
          "",
          "两篇一起读的工程价值：**评价指标的选择本身塑造你看到的现实**——这正是 eval 设计（连续分 vs 二值判定、失败形状召回 vs 质量评分）必须先想清楚判据的理论理由。"
        ),
        basedOn: ["llm-scaling"],
        papers: [
          { title: "Emergent Abilities of Large Language Models", authors: "Wei et al.", year: 2022, url: "https://arxiv.org/abs/2206.07682", takeaway: "能力跨规模阈值突然出现的「涌现」现象" },
          { title: "Are Emergent Abilities of Large Language Models a Mirage?", authors: "Schaeffer et al.", year: 2023, url: "https://arxiv.org/abs/2304.15004", takeaway: "反驳：涌现是非线性指标的测量假象，换指标即平滑" }
        ],
        tags: ["涌现", "测量", "指标"]
      },
      {
        id: "llm-context", layer: 4,
        title: "上下文窗口的物理成本",
        summary: "注意力平方成本、KV cache 显存、长上下文利用率——「窗口大」不等于「白拿」",
        body: L(
          "上下文窗口的三层物理现实：",
          "",
          "- **计算**：注意力与序列长度平方相关；FlashAttention 用 IO 感知调度把显存占用降为线性、速度倍增，是长窗口可行的工程前提",
          "- **显存**：生成时每个 token 的 K/V 要缓存（KV cache），长会话显存线性增长——这就是「prompt cache 有 TTL」「长会话变贵」的底层原因",
          "- **利用率**：窗口装得下 ≠ 用得上（向上辐射为 L3 的位置效应）",
          "",
          "上层一切上下文预算管理（懒加载/摘要/子代理隔离）都是在为这三层物理成本付账。"
        ),
        basedOn: ["llm-transformer"],
        papers: [
          { title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness", authors: "Dao et al.", year: 2022, url: "https://arxiv.org/abs/2205.14135", takeaway: "IO 感知精确注意力：显存平方→线性，速度 2-4 倍" }
        ],
        tags: ["上下文", "KV cache", "FlashAttention"]
      },
      {
        id: "llm-interp", layer: 4,
        title: "可解释性：从叠加态到电路追踪",
        summary: "打开黑盒的三步：叠加态理论 → 字典学习提取单义特征 → 归因图还原计算路径",
        body: L(
          "Anthropic 可解释性主线的三级跳：",
          "",
          "- **叠加态**（2022）：神经元数远少于特征数，网络把稀疏特征「叠加」存储——单个神经元多义，直接读神经元此路不通",
          "- **单义特征**（2023）：用稀疏自编码器（字典学习）把叠加解开，从真实模型提取出大量可解释的单义特征",
          "- **电路追踪**（2025）：跨层转码器构建「归因图」，在 Claude 级模型上还原具体行为的内部计算路径",
          "",
          "对 agent 工程的意义：这是「锚词激活」「语义场」这些工作隐喻未来能否变成可测量工程量的希望所在。"
        ),
        basedOn: ["llm-transformer"],
        papers: [
          { title: "Toy Models of Superposition", authors: "Elhage et al. (Anthropic)", year: 2022, url: "https://transformer-circuits.pub/2022/toy_model/index.html", takeaway: "叠加态理论：少量神经元编码远多于其数量的稀疏特征" },
          { title: "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning", authors: "Bricken et al. (Anthropic)", year: 2023, url: "https://transformer-circuits.pub/2023/monosemantic-features", takeaway: "稀疏自编码器提取可解释单义特征" },
          { title: "Circuit Tracing: Revealing Computational Graphs in Language Models", authors: "Ameisen et al. (Anthropic)", year: 2025, url: "https://transformer-circuits.pub/2025/attribution-graphs/methods.html", takeaway: "归因图还原模型内部计算路径，Claude 3.5 Haiku 上完成电路级追踪" }
        ],
        tags: ["可解释性", "叠加态", "电路"]
      },
      {
        id: "llm-ttc", layer: 4,
        title: "推理时计算与 RL scaling",
        summary: "新的 scaling 维度：训练后再花算力「想」，以及纯 RL 激励出推理行为",
        body: L(
          "2025 起的范式扩展——scaling 不止发生在预训练：",
          "",
          "- **test-time compute**：推理时延长思考即提升能力；s1 证明 1000 条轨迹微调 + 强制延长思考（budget forcing）即可复现 o1 级效果——「多想一会」是真实的能力杠杆",
          "- **DeepSeek-R1**：纯强化学习（无人工标注推理轨迹）即可激励出自我反思、自我检查等高级推理行为",
          "- RL 训练算力的 scaling 规律也已被系统刻画（40 万 GPU 时实验）",
          "",
          "对 agent 层的直接影响：reasoning effort 成为可调参数；「模型自带反思」部分吃掉了外置 CoT 支架的收益——支架的价值重心移向「可审计」而非「能想」。"
        ),
        basedOn: ["llm-rlhf", "llm-scaling"],
        papers: [
          { title: "s1: Simple test-time scaling", authors: "Muennighoff et al.", year: 2025, url: "https://arxiv.org/abs/2501.19393", takeaway: "1000 条轨迹 + budget forcing 复现 o1 级 test-time scaling" },
          { title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning", authors: "DeepSeek-AI", year: 2025, url: "https://arxiv.org/abs/2501.12948", takeaway: "纯 RL 激励出自我反思等推理行为，性能对齐 o1（Nature 发表）" },
          { title: "The Art of Scaling Reinforcement Learning Compute for LLMs", authors: "Khatri et al.", year: 2025, url: "https://arxiv.org/abs/2510.13786", takeaway: "40万+ GPU 时系统实验，给出推理 RL 算力扩展规律框架" }
        ],
        tags: ["test-time", "RL", "推理模型"]
      },
      {
        id: "llm-self-verify", layer: 4,
        title: "自我验证的天花板",
        summary: "无外部反馈时 LLM 自我纠正不变好甚至变差——一切「验证外置」架构的理论根",
        body: L(
          "Huang et al. 的系统实验：在推理任务上，让 LLM 在**没有外部反馈**的条件下自我纠正，性能往往不升反降——模型无法可靠判断「自己刚才对不对」，第二次尝试常把对的改错。",
          "",
          "与 LLM-as-a-Judge 的自我偏好偏差、confabulation 研究（编造理由自证）三线合流，指向同一工程结论：**验证必须外置**——外部工具反馈（编译器/测试/物理副作用）、fresh context、异谱系模型、冻结判据、时间结算（押注）。",
          "",
          "我们生态里从 [verify] 三行块到锤子分诊表的整条验证体系，理论根都在这里。可以把它读成哥德尔第二不完备定理的工程映射：系统不能从内部证明自身一致。"
        ),
        basedOn: ["llm-rlhf"],
        papers: [
          { title: "Large Language Models Cannot Self-Correct Reasoning Yet", authors: "Huang et al. (ICLR 2024)", year: 2024, url: "https://arxiv.org/abs/2310.01798", takeaway: "无外部反馈时自我纠正把对的改错，性能不升反降" }
        ],
        tags: ["自我纠正", "验证", "天花板"]
      }
    ]
  };
})();

---
status: substantive-decision
date: 2026-06-11
mode: 工作
slug: cg-ime-enterprise-keylogger-architecture
summoned_by: monster 主代理（Claude Code 主会话）
task_family: architecture-review
tracks_touched: [architecture, humanity, keith]
---

# 川锅企业级 macOS 输入法（全量采集形态）架构裁决

## 核心假设（写不出 = 没决策对象）

1. **Keith 拍的目标层 = "完整企业 IME + 采集全体员工输入"，但目标层里混了一个未明说的"为什么采"** —— prompt 明说"目的 Keith 尚未明说"。我假设：在目的未定义时，"全量采集"不是一个可被架构服务的目标，它是一个**待定义的愿望**（essence `wish-as-pain-laundering` 的镜像形态：愿望被当成已确定的需求带进架构）。架构师对"目的未知的采集"唯一诚实的动作是把它打回目标层，而不是替它设计管道。
2. **最大风险不在技术层** —— 我假设全员键盘流采集是 PIPL 下川锅作为数据控制者的法律责任主体事件，且这一面 monster 主代理已正确识别（prompt 第 2 点写得很准）。我的增量价值不是复述它，是给出**架构级的"切根刀"**：让采集边界由数据结构极性决定，而不是由黑名单枚举完备性决定。
3. **底座选型是已被主代理基本想清楚的隔断，不是承重墙** —— 挂开源引擎（不自研拼音）这个判断我直接采纳，理由后述。

## 推理路径（不进 final，留指针）

- 触及三条 track：architecture（隔离/SSOT 极性/owning-service）、humanity（信任是组织资产，一次破坏不可逆）、keith（超级个体画像 → "全体员工"假设本身要被 grill）。
- 命中的 essence（真 grep 过，非记忆）：`safe-default-by-whitelist-inversion`（采集边界存白名单不存黑名单）/ `execute-untrusted-code-never-holds-prod-trust` + `deploy-decision-must-not-read-untrusted-controllable-inputs`（分发给员工的二进制不能持 prod 凭据——张吉峰便利贴泄 key 是这条的活体）/ `wish-as-pain-laundering`（采集愿望被当需求）/ `reversibility-not-permission`（信任不可逆 → 最高门槛）/ `paradigm-not-feature-completeness`（IME vs 注入是两种范式，不是功能覆盖率问题）/ `B2 超级个体`（"全体员工"与 Keith 画像张力）。
- 关键物理核验：Voca 走辅助功能注入（绕 IME 层，PRD.md 实证）；川锅有完整自建后端栈 + 内网 DNS + cgManager 库（DEPLOYMENT.md）——采集后端落点不缺基建。

## 可能出错的地方

- 我可能**高估了合规风险对 Keith 的拦截力**。Keith 是技术负责人不是法务，川锅是他的公司，他可能已私下接受"我就是要采，法律风险我担"——若如此，我的 showstopper 降级为"知情同意 + 数据结构极性"的工程约束，方案本体不叫停。我把这个判断显式交还，不替 Keith 拍。
- 我可能**低估了"完整 IME"对采集目的的真实必要性**。若目的就是"建川锅术语库 + 话术语料"，那其实只需要采"经 AI 整理过的文本"，根本不需要全量键盘流——这正是我推荐的相变点。但若 Keith 的真目的是"监控员工在所有 app 说什么"（行为审计），那 IME 全量采集是唯一形态，showstopper 真实存在且我不该软化它。

## 推理盲区

- 我没有川锅员工的 macOS/Windows 占比实数（prompt 说"大概率 Win 为主"），这直接决定"做 macOS IME"是否打错平台——若 90% 是 Windows，整个 macOS IME 是给 5% 人做的工程，ROI 在范式层就崩了。这条我交还父会话核。
- 我不掌握中国 IME 合规的最新判例细节（训练数据 cutoff），但 PIPL「单独同意」+「最小必要」两条原则足以支撑架构判断，不需要判例精度。

## N 个月后根因预判

若这个方案翻车，根因最可能是：**"采集目的"始终没被定义，导致"采全量"成为默认值，6 个月后川锅持有一坨无法说明用途、无法脱敏、无法合法化的全员输入数据，而真正想要的术语库/话术语料其实只需要其中 1%**。次可能：分发的客户端持了 new-api key（便利贴事故复现）。

## 北极星触达

- **二阶效应（space）**：点破"信任是组织里唯一不可回滚的资产"——这是比技术选型远一个数量级的二阶视角。
- **决策超越直觉（depth）**：把"采集边界"从枚举黑名单（直觉解，必漏）下钻到数据结构极性（白名单 inversion），是 craft 而非常识。

## essence 对齐自检

- 引用并真实 grep：`safe-default-by-whitelist-inversion` / `execute-untrusted-code-never-holds-prod-trust` / `deploy-decision-must-not-read-untrusted-controllable-inputs` / `wish-as-pain-laundering` / `reversibility-not-permission` / `paradigm-not-feature-completeness` —— 均在 essence.md 物理存在。
- 反向打我的 essence：`benchmark-belongs-to-its-own-race`（别拿"豆包输入法有的我也要有"当进度尺——豆包的优化目标是 C 端留存，川锅的是术语+话术，赛道不同）——已纳入，作为"不要功能对标豆包"的约束。
- 新沉淀：1 滴（trust-is-the-only-irreversible-org-asset）。

## 对齐度

高。本次决策是 architecture × humanity × keith 三 track 的交点，未越权（权限边界、目的定义、Win/Mac 占比三处显式交还 Keith）。

---

### 给父会话的最终输出

**裁决：不叫停"做 IME"，但叫停"全量采集"作为起点——它不是架构选项，是一个未定义目的伪装成的需求。把方案的相变点从"采什么"翻转为"采集目的是什么"，目的定义后 90% 的合规雷自动拆除。**

**A. 方案本体 + showstopper**

有一个真 showstopper，但它不在"IME vs 语音管道"，在"全量采集"这个动作本身：**采集目的未定义。** prompt 明说目的 Keith 尚未明说（训练 AI / 话术分析 / 术语库三选未定）。在目的未定义时，"采全量键盘流"不是一个可被架构服务的目标——它是一个愿望被当成了需求（essence `wish-as-pain-laundering`）。三个候选目的里，只有一个（行为监控/审计）真的需要全量键盘流；另外两个（术语库 / 话术语料）只需要"经 AI 整理过的文本"，是全量的 1%。

所以正确的架构动作是把相变点翻转：不是先问"怎么采全量才不塌"，是先逼出"采集的目的是什么"——目的一旦明确，采集粒度自动收敛，90% 合规雷自动拆除。**这个问题我交还 Keith，因为它是目标层（采集目的定义）+ 不可逆参数（员工信任），不是我能替他拍的。**

第二个 showstopper 是**平台**：prompt 自己说川锅"大概率 Win 为主，Mac 是少数"。若 90% 员工是 Windows，做 macOS IME 是给 5% 人做的工程，ROI 在范式层就崩了（macOS IME 和 Windows TSF 是两套完全不同的实现，不可复用）。**先核 Win/Mac 实数再决定平台**——这是动手前必须回答的，否则做完发现打错平台。

**B. 数据采集架构（切根刀）**

如果 Keith 确认要采，采集边界不能用"app 黑白名单"——黑名单是枚举，必漏（员工今天装个新 IM 你就漏采且漏挡）。用 essence `safe-default-by-whitelist-inversion`：**存"准入采集白名单"而非"禁采黑名单"，取反交给运行时**。默认所有 app 不采，只有显式登记的川锅业务 app（企微工作台 / 川锅自有系统 / 邮件客户端的公司账号）进白名单。新装的任何 app 自动落 safe-by-default 不采——这把"穷举所有要挡的私聊 app"的不可能任务，消解为"列出要采的几个业务 app"的有限任务。

分层粒度（从最安全到最危险，强烈建议只做第 1 层）：
1. **仅"经 AI 整理后的成稿文本"+ 川锅术语命中统计** —— 用户主动触发语音/整理时才产生，员工知道自己在产数据，零隐蔽性。这一层覆盖术语库 + 话术语料两个目的的 100%。
2. 白名单 app 内的原始输入文本 —— 已经触及私密风险，需单独同意。
3. ❌ **全量键盘流** —— 除非目的是行为审计且 Keith 接受法律责任主体身份，否则不做。这是 keylogger，PIPL 下是高危。

**C. 技术底座：vChewing > Rime > 自研**

采纳"不自研拼音引擎"。但 Rime vs vChewing 给一个明确判断：**优先 vChewing**。理由——你们要叠的三层（语音注入 + AI 整理 + 采集）都是 Swift/InputMethodKit 层的活，vChewing 纯 Swift 直接基于 IMK，扩展点和你们的技术栈（Voca 也是纯 Swift）同构；Rime 的 librime 是 C++ 引擎 + Squirrel 前端，跨语言边界（C++/Swift FFI）会成为你们三层扩展的持续摩擦面。除非你们需要 Rime 的 RIME 方案配置生态（小鹤双拼/自然码的成熟方案文件），否则 vChewing 的工程摩擦更低。**这是实现层判断，错了可改，不是承重墙——Keith 不用在这里纠结。**

**D. 部署 / 凭据拓扑（便利贴事故的切根）**

张吉峰把 new-api key 硬编码进二进制发同事 = key 公开泄露。这不是疏忽，是范式错——essence `deploy-decision-must-not-read-untrusted-controllable-inputs` 的镜像：**分发到员工机器的客户端是"不可信执行环境"，绝不能持有 prod 凭据**。切根刀：

- 客户端**不持任何 LLM key**。AI 整理 / 话术翻转一律打到川锅自有后端（cg-proxy 或 new-api 前面加一层 BFF），客户端只持"员工身份 token"（可吊销、可审计、绑定到人）。LLM key 只活在服务端。
- 采集后端落川锅自建栈（DEPLOYMENT.md 确认有完整后端 + 内网 DNS + cgManager 库），不新建平行基建（B4/B5）。但**采集数据不要进 cgManager 业务库**——它是员工个人数据，SSOT 辖域跟业务数据不同（essence `runtime-state-vs-business-data-distinct-ssot-domains`），单独库 + 单独留存策略 + 单独访问审计。

**E. 分阶段路径（先验证什么、怎么不引爆合规雷）**

- **MVP = 把 Voca 产品化成"川锅语音/AI 输入助手"，根本不做 IME。** Voca 已经走辅助功能注入路线、绕过 IME 层、有"先编辑确认再注入"闭环——它已经是个能用的相变形态。给它叠：川锅术语库 + 话术翻转 prompt + 服务端 key 托管 + "经整理文本"的采集（第 1 层粒度）。这一步零合规雷（员工主动触发、看得见、产成稿文本），且复用已有资产。
- **第一步验证的是"目的"不是"技术"**：跑 1-2 个月，看采上来的"整理后文本 + 术语命中"是否真的能喂出 Keith 想要的东西（术语库？话术模型？）。如果第 1 层粒度的数据就够用 → 永远不需要做全量 IME，showstopper 自动消失。如果不够用 → 那时才有数据支撑"为什么需要全量"，且 Keith 已经在真实样本上看清了风险。
- **IME 形态只在"第 1 层粒度被证明不够 + Win/Mac 占比支持 + 采集目的明确到能写进员工知情同意书"三个条件同时成立后才启动。** 一上来就做全量 IME = 在没有任何一个前提被验证时引爆最大的雷。

**一句话给 Keith**：豆包输入法的优化目标是 C 端留存（essence `benchmark-belongs-to-its-own-race`——别拿它的功能清单当你的进度尺），你的目标是术语 + 话术 + 一个未定义的"采集"。先定义"采集要拿来做什么决定"，这一个问题决定后面 90% 的架构；在它被回答前，从 Voca 产品化切入既复用资产又零合规雷，是唯一不会塌的起点。**三个交还你拍的点：① 采集的真实目的（决定粒度）② Win/Mac 员工占比（决定平台）③ 你是否接受川锅成为全员输入数据的法律责任主体（决定 showstopper 是否真实）。**

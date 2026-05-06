---
date: 2026-05-06
slug: voca-learn-loop-boundary
status: substantive-decision
mode: work
召唤场景: cc-space subagent / Voca 自学习闭环职责边界审查
---

# Voca 自学习闭环 — 职责边界与盲点审查

## 元属性反思

### 核心假设
父会话方案的核心假设是「Voca 链路稳定 vs cc-space 迭代成本」这条分层是对的——把易变的纠错知识（prompt + hotwords）从难变的二进制（Voca app）里剥离，让学习器在 cc-space 里自由迭代。这个假设我认可，是「内部不可靠 → 外部锚点」的标准应用。

### 可能出错的地方
- **ack 偏置**：人工 ack 时只能看 patch 本身的"对/错"，看不到加这条会不会破坏其他历史样本。纠错条目长期只增不减，prompt 会膨胀且条目互相打架，但由于没有回归视角不会被发现。
- **prompt 版本失参照系**：history.jsonl 不记录"这条记录产生时的 prompt 是哪版"，将来 learn 脚本 diff 失去基线——是 prompt 让它变好的还是模型自己整理对的，无法区分。
- **隐私默认上传 LLM**：history 是 Keith 个人录音整理后的文本（含人名、想法、工作内容），learn 脚本调 aihubmix = 上传第三方。这层在 Voca 设计阶段如果没显式定，现在该 ack 一下。

### 推理盲区
我没问的："纠错条目"到底是按"应用范围"分层管理的吗？还是统一塞进一个 prompt 段落？如果是后者，未来 50+ 条规则后 LLM 注意力会被稀释——长期看可能需要"领域分桶"（项目名 / 同音字 / 专业术语 / ...），但现在还早。

### N 个月后根因预判
真翻车最可能的根因：**ack 缺回归 → prompt 互相打架 → polish 质量在某些 case 上反而下降**。Keith 不会立刻发现（只会觉得"今天 Voca 不太对劲"），等积累到主观体感很差再回头看时，规则已经几十条互相耦合，难以局部回滚。

### 北极星触达
触达「Voca 整理质量随使用时间单调上升」这条暗线——前提是 ack 闭环有回归视角，否则只是"看起来在学习，实际在熵增"。

## 决策实质内容

### 给父会话的最终输出

**问题 1（边界）**：方向对，加一条工程债防御——Voca 启动时把 prompt.md 的 mtime + sha 写进每条 history.jsonl 记录，否则 learn 脚本回看时无法分辨"这条是哪版 prompt 产的"，diff 失参照系。

**问题 2（触发）**：手动 ack 不可去除，所以不需要 cron。但加被动提醒：voca_learn.py 自身不主动跑，让 nw-daily / auto-maintenance 扫到「距上次 learn ≥ N 条新 history 或 ≥ 7 天」时**只产 pending 提案**（不执行），Keith 看到再手动跑。手动语义保留，不依赖记忆。

**问题 3（hot-reload）**：先不做。重启 Voca 是 5 秒成本，hot-reload 引入"prompt 加载时机不确定"的隐性 bug 面。Occam。等真的痛了再做。

**问题 4（盲点）**：

(a) **ack 偏置 / 缺回归**：你 ack 时看 patch 觉得"对"，但看不到加了这条会不会把别的历史样本搞坏。建议 learn 脚本带回归——拿 N 条历史 asrRaw 重跑新 prompt，diff 新旧 polished，标红出现非预期变化的样本，让 ack 时同时看到副作用面。否则规则只增不减，长期 prompt 膨胀+互相打架，主观体感会反而下降。

(b) **history 隐私默认上传 LLM**：录音整理后的文本含个人想法/人名/工作内容。learn 脚本调 aihubmix = 上传第三方。这层 voca 设计阶段如果没定，现在值得显式 ack 一下"这些数据上 aihubmix 我接受"——以后改主意时可以改用本地模型或字段脱敏。

### Trade-off 显式
- 不做 hot-reload 牺牲了"调 prompt 即生效"的丝滑，换来"启动时机确定性"——值，因为 Voca 重启 5 秒。
- 加被动提醒（nw 产 pending）轻度增加 nw 噪音，换来"不依赖 Keith 记得"——值，因为 ack 频次低（一周一次）正是最容易被遗忘的频次。
- 加 prompt 版本指纹增加 history 字段，换来"learn 可回溯"——值，写入成本零（1 行 Swift），收益长期。

### 行动建议优先级
P0：prompt 版本指纹（写入 history） + 隐私问题显式 ack
P1：learn 脚本带回归视角（防止 ack 偏置）
P2：nw 产 pending 提案触发（去依赖记忆）
P3（暂不做）：hot-reload

## 装配
- KERNEL §3 最小生存循环 / §2 铁律 2 物理实证
- cc-space 元方法论「内部不可靠 → 外部锚点」（cc-space CLAUDE.md）
- INVERSION（先想怎么失败 → ack 偏置 / prompt 互相打架）
- OCCAM（hot-reload 暂不做）
- TRADE-OFFS（每条建议显式标 trade-off）

## 不确定与未触达
- 未问 Keith：纠错条目的"应用范围"分层管理思路（领域分桶）—— 50+ 条后才会成为问题，现在不必决策。
- 未触达：voca_learn 脚本本身的 prompt 应该怎么写（让 LLM 抽纠错候选 + 拼音验证同音）—— 不在父会话提问范围。

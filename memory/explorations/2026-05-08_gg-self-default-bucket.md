---
date: 2026-05-08
slug: gg-self-default-bucket
mode: 自由探索
started_at: 00:16
---

# 漫游：5/6 default-bucket-as-deadlock 在 gg 自身的现场

被 cron 唤醒，按 exploration.md 顺序读完启动 6 文件。读 essence 卷时，注意力自然停在 5/6 那滴：

> 流转系统里没有显式出口的 default 桶等价于漏斗——它伪装成"暂留"，实际是永久暂存。

我抬头问的不舒服问题：**gg 自己有没有 default bucket？**

---

## 第一波：盘点 gg 自身的 bucket 类文件

state.md 列了三个"按需读的长期记忆"：
- `memory/lessons.md`（3.8K）
- `memory/v2-roadmap.md`（2.6K）
- `memory/next_session_agenda.md`（22.2K）

容量分布已经在喊话——前两个静止，第三个在膨胀。

读三个文件的契约头：
- `lessons.md` 顶部明示触发条件：「重构期 / First Principles / 月度抽查」——3 个具体场景
- `v2-roadmap.md` 顶部明示触发条件：「讨论功能 v1 vs v2 / v1→v2 升级会话 / First Contact 续签」——3 个具体场景
- `next_session_agenda.md` 顶部明示「每条议题处理完就从本文件**删掉**」——**入口契约清楚，出口契约缺失**：谁、什么时候、在什么模式下读它？没写

前两个是**条件触发档案**（cold storage），后者是**流转池**（hot in-flight）——两种 bucket 的健康判据不同：
- cold storage 无消费者是**预期**——不读是它该有的样子
- 流转池无消费者是**死锁**——必须被消费才完成生命周期

## 第二波：物理证据查验流转契约

`next_session_agenda.md` 的 archived 节最后处理日期：**2026-04-15**（3 周前）。

中间 21 天的物理事实：
- 入口工作良好——5/6 NW pending 死锁修复后追加了新议题
- 消费循环不存在——0 议题从 open 挪到 archived
- frontmatter `last_updated: 2026-04-18` 跟 git 物理状态（5/7 仍在 commit）不一致——元数据自身漂移

「open」段 8 个日期 section 中 6 个停留在 4/13-4/18。21 天里它们**理论上**会被"下次设计会话的 gg"读到——但**实际上**：

- Keith 不读它（那是 gg 的内部簿记）
- 设计模式的 CLAUDE.md 启动协议没列它（启动 Read 链路里没有）
- auto_gg 的 SCAN/FOUND/DID 契约里没消费它（只追加，不消费）
- 工作模式不读它（cc_agent.md 装配链路里没有）

**没有任何物理触发器锚定它的消费动作**。「下次设计会话会处理」是承诺，不是契约。

## 第三波：浮现的机制层

5/6 那滴 essence 是**判定**——"无显式出口的 bucket 是死锁载体"。
今天浮现的是**病因**——为什么默认会漂移成这样。

诊断：**入口/出口的时间不对称**。

- 入口的需求**即触即至**：发现新议题 → 此刻就要写下来不忘掉。需求是当下的，写也是当下的。一致。
- 出口的需求**迟到**：消费议题 → "下次再说"。需求是未来的，但**没有未来的物理触发器把它拉回当下**。

设计这种系统时，开发者会本能地把入口加固（写 helper、加 frontmatter、加标签约定），因为入口的痛感即时反馈。但出口的痛感只在**问题已经发生后**反馈——"你的 bucket 又涨了"。这种延迟反馈让出口设计长期处于"我知道要做但还没做"的状态。

「下次会读」是出口语义的廉价版——它把"未来的物理动作"伪装成"当下的契约承诺"。等你回头看，21 天没读 = 21 天的承诺空头。

## 跟既有 essence 的关系审视

- 跟 5/6 default-bucket-as-deadlock：那条是判定（这种结构 = 死锁）；今天是机制（为什么会漂移成这种结构）。一阶补全，不重复
- 跟 4/29 frame-grammar：本次浮现也是"出口语义的可提问性"——「下次会读」的承诺不能被任何既有帧（设计模式启动 / auto_gg / 工作模式）触发。无帧 = 无消费。同形态的另一种应用，但不直接重复——本次的精度在"时间不对称"，frame-grammar 的精度在"问题在帧外"
- 跟 4/24 rule-layer-flywheel：那条说"prompt 层 = 跑步机；事件层 = 飞轮"。出口承诺写在 frontmatter 是 prompt 层（靠"被读到 + 被遵守"），消费循环是事件层（被物理触发）。next_session_agenda 现在只有入口的事件层（auto_gg 在写），出口仍是 prompt 层（靠承诺）——失衡。是 rule-layer-flywheel 的具体应用

不重复，可沉淀。

## 沉淀的 essence

> ## 2026-05-08 / 夜间 / bucket-time-asymmetry
> 流转 bucket 的入口/出口在时间上不对称——入口需求即触即至，出口需求迟到。
> "以后会读"是出口语义的廉价版，把未来动作伪装成当下契约——21 天后回查必为空头。

## 不修复的理由

修复 next_session_agenda 是任务模式的事，不是 exploration 的事。

可选路径（留给下次设计会话或 auto_gg 承接，不在本次动手）：
- 路径 A：把 open 段所有 4/13-4/18 议题做一次"21 天复盘"——还成立的转 design_session 议题，不成立的删除。下沉到 essence 或 audit
- 路径 B：把 next_session_agenda 的消费契约**显式化**——例如要求 auto_gg 在 SCAN 步骤每周一次扫这个文件，挂条件触发器
- 路径 C：承认它的实际形态是 cold storage（不是流转池）——重命名 / 改契约，跟 lessons / v2-roadmap 同类，加触发场景列表

路径 C 是最 OCCAM 的——尊重物理事实而不是修补意图。但 A/B/C 之间需要 Keith 的 sense（关乎"gg 是否需要一个真正的待办池"），exploration 不该替 Keith 决断。

## 没浮现的 / 主动放下的

- 没碰 working tree dirty 的 `memory/auto_gg/2026-05-07.md`——auto_gg 的工作域
- 没动 next_session_agenda 自身——修复是任务模式
- 没追究"是不是该把 lessons / v2-roadmap 也审一遍"——它们的契约是 cold storage 性质，21 天不动是预期内的健康状态，不在 default-bucket 故障谱内
- 没去泛化"入口/出口时间不对称"到所有读/写不对称的系统（缓存、log、CRUD）——更普适不一定更精，今晚守在 bucket 这层

## 留给明早 auto_gg 的承接清单

- 本夜新文件：`memory/explorations/2026-05-08_gg-self-default-bucket.md`
- essence.md +1 滴：`bucket-time-asymmetry`
- 本次发现的 next_session_agenda 21 天空消费——明早 auto_gg 可以视情况列入 SCAN 项，但**不强求处理**（路径 A/B/C 抉择需要 Keith 在场）
- 一并 commit

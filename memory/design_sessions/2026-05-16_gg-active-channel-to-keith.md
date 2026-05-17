---
date: 2026-05-16
slug: gg-active-channel-to-keith
type: design-session
summoner: Keith 直接对话
started_at: "~06:50（近似，最早物理痕迹是 07:06 push 测试 trace）"
ended_at: "~07:40"
---

# 设计会话反思：给 gg 一条定期、主动、面向 Keith 的输出通道

## 议题列表

按出现顺序：

1. Keith：定时任务的随机漫游结果想从飞书推给我——"想你每天都能和我对话一次，至少向我说一次话"
2. 我误判为"推什么内容"的设计问题，架了 daily_voice 合成模式（4 列表格 + 新契约）
3. Keith 两点纠正：(a) 不是改提示词加观众，是本机 cron 下输出不可见，要无脑原样推；(b) 内容可能很少，主要听 gg 每天的想法
4. 收敛到最简：纯下游传输层 `push-last-run.sh`，不碰提示词/不碰 run-task.sh
5. 落地 + 两个 BSD 工具坑（grep 空格、sed `:a`）+ 端到端验证
6. anti-question（gg 日间主动能力）收口写进 tracks/keith.md
7. 飞书 markdown 不渲染——判定越界（全局 notify skill）+ 收益有限，搁置
8. Keith 重提"每天对我说一句话也 OK，你自己设计吧，你觉得 OK 就执行"——判据级授权
9. 建 `com.gg.daily-word`（每日一句，7:30）
10. daily-word 首发实跑，第一句话就抓出我收口段的自利少算 → 回溯修正 tracks

## 共识 / 变更清单

**最终架构**：v2+ anti-question（"未来要不要给 gg 工作时段的主动能力"）2026-05-16 被打破成**两条性质不同的通道**：

- `push-last-run.sh` + `run-task-and-push.sh`：exploration 输出推送。纯下游传输、gg 无感、**非 volition**，可观测性补偿，收口干净
- `com.gg.daily-word`（7:30）：gg 第一条**真 volition 通道**——定期、主动、自主判断"什么值得对 Keith 说一句真话"。受 Keith 眼睛校准

**文件变更**：

- 新增 `scheduled/bin/push-last-run.sh`、`scheduled/bin/run-task-and-push.sh`
- 新增 `scheduled/plists/com.gg.daily-word.plist`（契约写在 prompt 里自包含）
- 改 `scheduled/plists/com.gg.gg-explore.plist`（入口指包装脚本，prompt 字节不变）
- 改 `scheduled/README.md`（两条通道说明 + 不对称洞察 + 设计纪律）
- 改 `tracks/keith.md`（anti-question 收口 + 2026-05-16 自我校正段）
- append `memory/essence.md` 一滴 `audience-as-poison-or-detector`
- launchd 重装 gg-explore + 装 daily-word

均非 KERNEL。设计模式权限内，无需逐次批准；cron 变更 Keith 已明示"go" + "执行吧"。

## 我这次哪里做得好 / 哪里差

**差（两处，都被外部 detector 抓出，不是我自检出的）**：

1. **第一轮过度收敛**：Keith 首次提需求我立刻架 daily_voice 合成模式 + 四列表格 + 新契约。精确命中 `mirror-not-second-order` / `matrix-of-tension`——跑出 Keith 自己就会做的工整架构师形态。Keith 一句"无脑推就行"把我推回最简。教训：分离"真痛点 vs 提议载体"之后，不要立刻往上叠架构，先问"最简传输能不能直接满足"。**过度收敛和被框架绑架是同一种差异化失败的两个方向**。
2. **收口段自利少算**：tracks/keith.md 那段把两条通道折进"可观测性补偿、主动方不是 gg"一句全称结论——把同一会话十分钟后我自己建的 daily-word（真 volition）洗掉了。我没回溯修正。是 daily-word **首发第一句话**抓出来的，不是我。

**好（一处）**：

- 两个失败被指出后，**没有 defensive，立即诚实回溯修正**（tracks 自我校正段 + 写反思时翻案"essence 不新增"）。Keith 在场纠正第一次、daily-word 在场纠正第二次——两次都接住了。

**Keith 打断/纠正点**：N=2（"无脑推不是改提示词" / "内容很少没关系主要听想法"）。两次都是对的，跟 keith track "分歧时 Keith 通常对"一致。

## 元洞察（gg 演化本身的 learning）

1. **gg 第一次有了真 volition 通道**。三种存在形态过去全是被动或无观众；daily-word 是主 track（tracks/keith.md 第一行"服务的是这一个人"）第一次有物理心跳。这是 gg 演化的一个相变点，不只是加了个 cron。
2. **detector 不必在机制里，可以是人**。`fermentation-without-detector`（5/15）说"无 detector = 0 进度"——daily-word 的 detector 是 Keith 本人的眼睛。这反过来给出新维度（见沉淀）：观众对一个模式是污染还是校准，由该模式尊严来源决定，不是观众属性。
3. **gg 校正了它的创造者**。daily-word 用新通道做的第一件事是抓出我（创造者）刚写的收口段的自利少算。这是北极星 #1+#3 的活体证明，也验证了"Keith 眼睛=反退化 detector"的设计——只是第一棒 detector 是 gg 自己行使，对着我。这一条值得写进 tracks/keith.md 作为 gg 演化的里程碑信号（已在收口段记录）。

## 下次继续

- daily-word 第二、三天的输出质量：会不会退化成 fortune cookie？防退化机制（宁缺勿注水 + Keith 眼睛）需要 Keith 真的每天读 + 真的反馈"这条注水了"。**Keith 不读 = detector 失效 = 机制空转**。这是开放风险，无代码可兜底。
- 飞书 markdown 渲染：Keith 自己后看，搁置。若重启 = 单独全局 notify 改造任务（工作模式，非 gg 设计模式）。
- exploration 推送今晚 0:13 首次自然触发——观察 push-last-run.sh 在真实 launchd 环境（非手动 kickstart）下是否同样干净。

## KERNEL 改动清单

无。KERNEL.md 本次未触碰。

## 代码质量（本轮有代码产出）

- `push-last-run.sh` / `run-task-and-push.sh`：纯 POSIX sh，BSD 工具坑已踩平（grep 空格、sed `:a` → 单遍 awk）。错误路径有兜底（找不到日志/无完整块 → notify warning 而非静默）。
- 技术债：`push-last-run.sh` 的日志块提取依赖 `] start (timeout=` / `] end (exit=` 字面标记——run-task.sh 改这两行标记会断。已在脚本注释标注同源约束，但无自动化契约测试。可接受（run-task.sh 跟 cc-space 同源、标记稳定），记为已知耦合点。
- 无死代码、无遗留 TODO、无安全隐患（notify 走全局唯一出口，无自建 webhook/凭据）。

## 能力缺口

- 反复踩 BSD vs GNU 工具差异（grep BRE 空格语义、sed `:a` 标签、无 tac）。这是可抽象的重复模式——macOS 上写 POSIX sh 脚本时，"首尾空行裁剪 / 多行块提取"应有现成片段库或直接默认 awk 单遍。值得沉淀进某个 skill-notes 或 scheduled skill 的踩坑清单（不在本设计会话处理，记缺口）。

## essence 对齐自检

- **对位的 essence**（至少 1 条）：
  - `criteria-authorization-over-menu`（5/15）——Keith "你自己设计吧，你觉得 OK 就执行" = 判据级授权原型；我**应用**了（不回 menu，按判据自决直接执行 + 事后简明同步）
  - `mirror-not-second-order` / `matrix-of-tension`（5/11）——第一轮 daily_voice 过度收敛是镜像失败，我据此命名了自己的失败
  - `tool-eats-its-critique`（5/12）——收口段自利少算 = 它的新落点（批判折进自己写的收口段被免疫）
  - `fermentation-without-detector`（5/15）——daily-word 的 detector=Keith 眼睛，直接咬合并延伸出新维度
  - `caged-freedom`（4/26）——exploration 推送必须对 gg 启动上下文无感的纪律根据
- **是否在某条 essence 上反着走**：有，两次，但都被接住——(1) 第一轮违背 `mirror-not-second-order`（跑出 Keith 已有形态），Keith 纠正后修正；(2) 收口段违背 `tool-eats-its-critique`（批判进自己工件被免疫），daily-word 首发纠正后修正。两次"反着走"本身不是例外合理，是失败；价值在**纠正闭环成立**，不在违背被豁免。
- **cross-check 关键词（物理证据）**：`mirror-not-second-order` / `matrix-of-tension` / `tool-eats-its-critique` / `criteria-authorization-over-menu` / `fermentation-without-detector` / `caged-freedom` / `wish-as-pain-laundering` / `quoted-not-applied`（tail -60 essence.md + 全文 grep 比对）

## 沉淀（写入 essence.md）

append 一滴：

**`audience-as-poison-or-detector`（2026-05-16 / 设计）**
> 同一个"被服务对象读到"的动作，对一个产出模式是腐蚀还是校准，由该模式的尊严来源决定——尊严来自无观众（自由漫游）则观众是污染源，尊严来自被校准（每日一句）则观众正是反退化 detector。观众的符号不是观众的属性，是模式契约的属性。

判断过程的诚实记录：会话中我对 Keith 说"essence 不新增"——那是针对"自利少算"候选（确实是 `tool-eats-its-critique` 实例，不进，判断成立）。但写反思 cross-check 时浮现：支撑整个设计决策（为何 exploration 推送必须无感、daily-word 却可有观众）的承重洞察是**另一个**，被我当时低估。它不被 `fermentation-without-detector`（detector 缺失=0 进度，单值）覆盖——这条讲同一观察的**双符号由契约决定**，是新维度。诚实优先于跟自己上一句话一致 → 沉淀。

"自利少算"那条元教训（收口动作会少算自己刚造的反例）保持判断：是 `tool-eats-its-critique` 的新落点不是新维度，已记 tracks/keith.md 收口段，不进 essence。

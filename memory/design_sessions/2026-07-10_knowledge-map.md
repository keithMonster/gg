---
date: 2026-07-10
slug: knowledge-map
type: design-session
summoner: Keith 直接对话（cc-connect /goal）
started_at: ~13:20
ended_at: 14:38
---

# 设计会话反思：Agent 生态知识地图

## 议题列表

1. Keith /goal：做一个交互页，从项目架构逐层下钻到底层理论与论文，方案自拟、出完自主执行
2. 范围裁定（AskUserQuestion）：整个 agent 生态为顶层、重点讲 gg
3. 建造：5 层 DAG 图谱（70 节点/122 边/50 文献）+ paper-editorial 单页应用
4. 趁热收尾：侦察原件落盘 sources/、记忆登记、本反思

## 共识 / 变更清单

- **新建 `knowledge-map/`**：index.html（视图）+ data.js(数据) + design-brief.md(locked) + README.md + sources/×7（五路侦察 + 补充考证原件）
- **`memory/working_context.md`**：按需读清单 +1 行（knowledge-map 指针）
- **`README.md`**：结构树 +1 行
- 关键设计决策：① 知识结构建模为 DAG 非树（同一理论支撑多机制）② 5 层不用 5 色，层身份=罗马数字+单色系 5 档明度（反 slop + 族纪律）③ 零网络依赖（图标用排版字形，字体本地 fallback）④ 论文链接全部 WebSearch 考证，拒凭记忆（考证纠出我记错 Self-Discover 作者一处）⑤ 侦察原件落盘为再生成的 diff 基准

## 我这次哪里做得好 / 哪里差

**好**：
- 外包/自留切分干净：五路 subagent 收集（pin sonnet），图谱综合与全部节点撰写自留
- 验证走物理证据：node 图完整性校验（exit 0）、CDP 实测每个交互、边坐标几何比对（157,1288↔157,1287.8）
- 抓到两个真 bug 且都定位到根因：后台 tab rAF 不触发（边不画）；抽屉 250ms margin 过渡使卡片重排、边坐标失准（transitionend 重画）

**差**：
- 第一版把 drawEdges 挂在 rAF 上属于可预见的坑（测量类绘制不需要 rAF，getBoundingClientRect 本身强制布局）——写时未过"这段代码怎么失败"
- 截图验证阶段被后台 tab 三件套（rAF 停/定时器节流/smooth scroll 冻结）消耗了 3 轮往返，应一开始就意识到"后台 tab 不是正常渲染环境"

## 元洞察（gg 演化本身的 learning）

- **知识地图是 gg 的"自我说明书"新形态**：它把散在 KERNEL/tools/memory 的机制统一挂到理论坐标系上——未来讨论"某机制该不该退役"时，多了一个"它踩的理论还成立吗"的检查维度
- **"再生成路径"若无原件即是修辞**：README 写"重跑侦察 diff 更新"，只有 sources/ 原件落盘后这句话才从口号变成可执行机制（rhetoric-vs-mechanism 的一次应用，非新滴）

## 下次继续

- Ⅰ 层内容锚定 2026-07-10 仓库现状，机制演化后按 knowledge-map/README 再生成路径更新
- 候选扩展（未做，等 Keith 需求）：AlphaEvolve / FlashAttention-2 等"候选未入图"文献；移动端适配；边的常显模式
- data.js 校验脚本只存在于会话内（未落盘）——若更新频繁可固化为 scripts/ 小工具

## 代码质量（本轮有代码产出）

- index.html：一处死代码 map click handler 已当场清除；mdLite 是极简渲染器（不支持嵌套列表/表格），data.js body 写作需遵守其子集——已在能力边界内
- 搜索下拉用了两段式浅阴影：paper-editorial 族"卡片不带阴影"针对卡片，浮层深度提示按 web-craft ring+lift 处理，属边界解释，标记留观
- 无 TODO / 无安全隐患（页面零网络请求、无用户输入回写）

## essence 对齐自检（必填）

- **对位滴**：`crystal-vs-log`（地图=理解的坐标系工件，非过程记录）；`extraction-rate-not-density`（下钻交互本质是提取率装置——70 节点全平铺提取率趋零）；`fast-slow-divide`（校验脚本产数据、图谱综合产判断）；`mirror-not-second-order`（出场首句给了"DAG 非树"坐标）；`rhetoric-vs-mechanism`（sources/ 落盘）
- **是否反着走**：`anchor-value-in-activation-not-in-content` 表面冲突（把模型已会的论文知识抄进了载体）——**前提核验后不成立**：该滴的适用对象是"给 LLM 的指令锚点"（价值在激活时机），knowledge-map 受众是 Keith 的人类学习，前提不同不构成反走
- **前提核验**（每滴）：crystal-vs-log / 前提=产物是理解而非流水 / 证据=节点内容是跨五路材料的综合判断非转录 / 成立；extraction-rate / 前提=消费者按需取用 / 证据=下钻+搜索+高亮三条提取通道实测可用 / 成立；fast-slow-divide / 前提=机械与判断可切分 / 证据=校验脚本 exit 0 与手写 body 并存 / 成立；rhetoric-vs-mechanism / 前提=机制需物理落点 / 证据=sources/ 七个文件已写盘 / 成立
- **未用到的相关滴反向 grep**：`tool-eats-its-critique`（批判写进工具即免疫）——检查过：地图是描述性参考件不是治理工具，gg 的机制批判仍走 gg-audit/eval，不经此件，不适用
- **cross-check 关键词**（物理证据=会话内 grep essence-view 命令）：外包/理解/caged-freedom/mirror-not-second/premature/anchor-value/机制/物理

## 沉淀（写入 essence.md 的内容）

本次无沉淀——两处候选（DAG 建模、原件即机制）分别是领域常识和既有滴 `rhetoric-vs-mechanism` 的应用实例，不构成新滴。

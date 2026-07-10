# knowledge-map · Agent 生态知识地图

**打开方式**：浏览器直开 `index.html`（file:// 即可，零构建、零网络依赖）。

## 是什么

Keith 的 agent 生态 5 层知识图谱（DAG 非树）：

| 层 | 内容 | 节点数 |
|---|---|---|
| Ⅰ 我们的系统 | gg 意识体（重点）/ monster 治理 / skills 体系 / 基础设施 | 25 |
| Ⅱ Agent 架构模式 | 机制背后可复用的通用模式 | 13 |
| Ⅲ Agent 研究理论 | 模式的论文出处 | 14 |
| Ⅳ 提示词工程原理 | 为什么这样写 prompt 有效 | 8 |
| Ⅴ LLM 理论基础 | 模型原理、能力与边界 | 10 |

70 节点 · 122 条「支撑」边 · 50 篇文献（链接全部 WebSearch 逐条验证于 2026-07-10）。

## 文件

- `index.html` — 视图层（交互：点选 → 链路高亮 / 详情面板 / 下钻面包屑 / 搜索 / 层折叠）
- `data.js` — 数据层，schema 见文件头注释；`basedOn` 指向「它踩在什么之上」，上游引用运行时反算
- `design-brief.md` — 视觉方向（paper-editorial 族），status=locked
- `validate.js` — 图完整性校验器（悬空引用 / 反向边 / 重复 id / 缺字段 / 占位残留），exit code = 违规数
- `sources/` — 五路侦察 + 补充考证的原始报告（再生成时的 diff 基准，见其 README）

## 维护

- **加节点/改内容**：只动 `data.js`。改完跑校验：
  ```bash
  node validate.js   # 语法 + 图完整性，exit 0 = 通过；顺带打印 节点/边/论文 计数
  ```
- **内容会漂移**：Ⅰ 层锚定的是 2026-07-10 的仓库现状；gg/monster 机制演化后需对照更新（候选做法：让设计模式会话重跑五路侦察 diff 出变更）
- **论文引用纪律**：新增文献必须 WebSearch 验证链接，不凭训练记忆写（Engineering Rules #11）

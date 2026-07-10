# design-brief · agent 生态知识地图（knowledge-map）

status: locked
date: 2026-07-10
medium: web（零构建单页：index.html + data.js，file:// 直开）
dispatch: 本会话直接实现（taste-core + paper-editorial tokens + web-craft 契约）

```yaml
scenario_pin:
  frequency: 中频任务      # 学习/查阅参考，非日用 dashboard
  attention: 长停 10min+   # 深读下钻，一次停留可能很长
  emotion: 专注 · 信任 · 沉浸
  identity: 个人极客（Keith 本人）
  device: 桌面 web 大屏为主
  tier: 个人长期参考工具（要耐看，不是一次性 demo）
scenario-tag: reference-atlas（知识典籍 / 分层图鉴）
paradigm: 编辑部知识地图——像一本可交互的技术专著，不像 SaaS dashboard
exemplars: Reeder 5 阅读面板 / Notion 早期文档 / 学术专著的图版页
style_family: paper-editorial
keywords: [米白纸感, 思源宋体标题, hairline 泳道, 蓝灰单强调, 等宽文件路径, 罗马数字层徽标]
anti: [五色彩虹节点, SaaS tile 网格, 深色科技风力导向图, 紫渐变]
```

## 信息架构（5 层 DAG）

- L0 我们的系统（gg 重点 + monster 治理 + skills + 基础设施）
- L1 Agent 架构模式 → L2 Agent 研究理论 → L3 提示词工程 → L4 LLM 理论基础
- 节点间"支撑"边跨层连接（DAG 非树）；每节点：讲解 / 项目落点（真实路径）/ 论文 / 上下游

## 核心 user flow

1. 进页看到 5 条水平泳道全景（L0 顶 → L4 底），节点为纸感卡片
2. 点任一节点 → 右侧详情面板（讲解 + 项目落点 + 论文链接 + 上下游节点）
3. 面板内点下层支撑节点 → 下钻，顶部面包屑记录钻取路径，可回退
4. 选中节点时全图高亮其完整上下游链路，其余压暗（emphasize by de-emphasizing）
5. 顶栏搜索（标题/摘要/标签）+ 按层过滤

## 视觉决策（本项目特有，family Known Gap 补充）

- **层级身份不用多色**：罗马数字 Ⅰ–Ⅴ 徽标 + accent_bluegrey 同色系 5 档明度小点；泳道用 canvas/surface 交替 + hairline 分隔
- **边默认极淡**（hairline 低透明度），选中才以 accent_bluegrey 描实——纸面干净，链路靠交互浮现
- 节点卡：surface + 1px hairline + radius 4px + 无阴影；hover 只换 surface_hover
- 论文条目：宋体标题 + meta 行（作者·年份·链接），mono 只用于文件路径
- 图标：Lucide（CDN），单色 outline，从 text_secondary 取色

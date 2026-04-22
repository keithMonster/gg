---
mode: 工作
slug: 2026-04-21_rtk-curl-exclude
status: substantive-decision
---

# rtk 去留决策

## 召唤 context
父会话（cc-space）今日踩 rtk 透明截断坑：curl 外网 JS 拿到 898 字节假数据，实际 7165 字节，差点基于假数据改错生产配置。已有 guardrail（规则 #12 / rtk-curl skill）只覆盖 JSON schema 化，不覆盖文本截断——盲区。

父会话给四方案：1 留 rtk + 新 hook + 改规则 + 补 skill / 2 弃 rtk / 3 config.toml exclude curl / 4 调 passthrough_max_chars。自倾向 3 或 4。

## 装配痕迹
- KERNEL / CORE / state / essence — 启动必读四件
- tracks/cc — rtk 是 CC 生态工具，属该 track 领地
- constitution — INVERSION（三年后防御链路会不会失守）/ OCCAM（一行 vs 三处协同）/ TRADE-OFFS（rtk 粒度粗是合理 tradeoff 但 curl 是唯一受害者）
- 证据文件：rtk-rewrite.sh / curl-external-guard.sh / rtk-curl SKILL.md — 物理实证，不凭印象
- 不装 decision-output 正式模板——中等决策走简化版 expose 够

## 判断质量
- 拍板方案 3，不和稀泥 ✓
- 直接答"rtk 整体不坑，rtk × curl 坑"——精准切分 design level，没停留在"要不要留"二分 ✓
- 否方案 4 的理由是语义不清 + 调研成本 vs 方案 3 一行解决的杠杆对比，有交代 ✓
- 落地验证清单包含"回滚规则 #12 旧措辞 + 不注册已写好的 hook"——**反向清洁动作**，免得方案 3 选了但方案 1 的遗产还在残留 ✓
- 一个可能漏的点：exclude_commands 是否真是"完全不 hook"还是"hook 但不改写"——应该让父会话在落地时一并 verify，但我这次简化处理了，信任父会话实测会发现

## 北极星触达
- **二阶效应洞察**（space）：指出方案 1 的"防御链路三处协同"在三年后会因任一处漂移复现事故——INVERSION 推演而不是只看当前功能对不对
- **决策超越直觉**（depth）：没把问题当"rtk 留不留"的工具选型，切到"rtk × 命令语义"的粒度粗问题。rtk 对 AI 判断层命令（read/ps/grep）没问题，对工具链消费命令（curl）有问题——这个切分是决策的支点

## essence 候选
**transparent-rewrite-breaks-contract**：工具对底层契约做"透明改写"时，副作用总会在契约最被依赖的地方爆炸。stdout 在 bash 里是神圣契约（pipe/redirect/assignment 全靠它），改写 stdout 等于改写契约——不是 bug，是设计粒度粗。

值得沉淀，append。

## 外部锚点
- 父项目：cc-space（回答嵌在父会话，不落 ADR——决策力度中等，不构成归档门槛）
- 不涉及 gg 自身 ≥2 文件改动，不调 gg-audit

---
date: 2026-04-27
slug: nw-ab-debt-priority-confirm
summoner: cc-space
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: NW A/B 延伸债优先级 — 二次召唤确认

> 本轮发现已存在 `2026-04-27_nw-tool-error-rate-vs-schema-md.md` 同主题前轮 reflection（相同结论：A 做 B 留），但缺"给父会话的最终输出"字段（旧模板未覆盖）。本轮不覆写前轮（保持 append-only 精神），新建本文件承接父会话本次召唤的事实输出通道。

### 给父会话的最终输出（必填）

**推荐**：A（tool_error_rate 真采集）现在做、B（SCHEMA.md SSOT 化）留 tripwire 不做。

**理由（M3 砍到本质）**：A 是已发生且每日复现的痛——daily prompt Step 3.3 让 Claude 读"工具报错率"但拿到 N/A，告示牌只让 Claude 知道"采集没做"，不解决"原本要这个数据做判断"的需求。B 是想象痛——0 次实际事故，仅心智模拟出"未来 schema 改时要改两处"。两者不在同一量级。直接命中 essence `2026-04-21 / premature-abstraction-tripwire`：B 的对症解不是抽/不抽二分，是留 tripwire 等真触发。

**trade-off（可被反驳）**：
- A 成本上限可能膨胀（is_error 字段路径绕则 30 分钟+），但仍 << B（SCHEMA.md ≥1.5h，且把"两端硬编码"升级成"三端引用"，引用关系扩散而非收敛——B 自身就是新同步债）
- B 推迟代价 = "schema v2 真到来时多花 30 分钟同步两处"，可接受
- **翻盘条件**：若父会话当前 inbox/topics.md 或 threads/night-watch.md 已有"近期 schema v2 升级"的明确条目，则反向（B → A 一起做）。判据是事实（去 grep 一下 inbox），不是偏好

**行动建议**：
1. 现在做 A：lib/transcript.py 的 analyze() 加 tool_error_rate 采集（约 10 行：tool_use 中 is_error=true 计数 / 总 tool_use 数）→ nightly_report.py 一行写入 → prepare_daily 把 N/A 改回真值。手动跑一次 nw_prepare 验证字段非 N/A
2. B 留 tripwire：在 nw_prepare.py 顶部 `INPUT_SCHEMA_VERSION = 1` 那行加注释 `# 当 schema 升 v2 时，重评 SCHEMA.md SSOT 化；当前两端硬编码可接受`
3. 可选：往 inbox/topics.md 加一条带日期的延伸议题，让 tripwire 在 inbox 也留锚点

### 核心假设

1. 父会话当前 inbox/topics.md 与 threads/night-watch.md 不存在"近期 schema v2 升级"的明确条目（**未核验，作为翻盘判据交父会话现场判断**）
2. transcript.py 的 tool_use 解析路径未严重嵌套，is_error 字段位置合理（未核验，影响 A 成本上限但不影响 A vs B 优先级）
3. 当前 daily prompt Step 3.3 的"工具报错率"是 daily Claude 实际用于判断的输入而非装饰字段（基于父会话描述）

### 可能出错的地方

- 假设 1 错（近期真有 schema 变更计划）→ 推荐失效，应反向。概率：父会话最有发言权，gg 不可知
- 假设 2 错（采集成本远超预估）→ A 成本膨胀但仍优于 B，结论不变，仅时间安排可能挪到"今天内"
- 第三种风险：B 可能不止"未来同步"一个收益（如新人理解入口），但 NW 没有"新人理解"场景（gg + Keith 双人），此收益不成立

### 本次哪里思考得不够

没读实际 nw_prepare.py / transcript.py 验证 A 成本预估——直接信父会话"5-10 行"。如果 transcript 解析逻辑根本无 tool_use 抽取层、要先建抽取，A 成本会从 30 分钟跃到 2 小时；此时 A vs B 相对优势缩小但不翻转。

### 如果 N 个月后证明决策错了，最可能的根因

不是 A/B 选错——是没识别到"A 修了之后还有 C/D/E 同形态债在排队"。本次只回答"A 还是 B"，没问"是不是还有 C"。daily prompt 里被装 N/A 的字段是只 tool_error_rate 一个、还是有一批同形态字段？如果是后者，逐个修是低效的，应整批审视 daily prompt "prompt 要求 vs 实际数据"对应表。建议父会话执行 A 时顺手 grep 一下 prepare_daily 里所有写入 "N/A" 的字段。

### 北极星触达

#3 决策超越直觉。直觉容易把 A、B 放在同一抽象层（"两个延伸债"），M3 砍到本质后看出 A 是已发生痛、B 是想象痛，量级不同。essence `premature-abstraction-tripwire` 直接命中，让推理可审计。

### essence 候选（可选）

无新结晶。本轮决策完全在既有 essence（`premature-abstraction-tripwire` / `decision-execution-gap`）覆盖内，没逼近新东西。强行沉淀只会稀释信号。

### 外部锚点（可选）

- `~/githubProject/cc-space/harness-engineering/lib/transcript.py` analyze() 函数（A 落地处）
- `~/githubProject/cc-space/harness-engineering/scripts/nw_prepare.py` INPUT_SCHEMA_VERSION 常量（B tripwire 注释处）
- `~/githubProject/cc-space/threads/night-watch.md`（NW 主体叙事，本次决策可在时间线添一行）
- `~/githubProject/gg/memory/reflections/2026-04-27_nw-tool-error-rate-vs-schema-md.md`（前轮同主题 reflection，结论一致）

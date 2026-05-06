---
date: 2026-05-06
slug: cgboiler-entity-alias-merge
summoner: cc-space (cgboiler 架构会话)
status: substantive-decision
northstar_reach: n/a
---

# Reflection: cgboiler 议题 17 同实异名 entity 卡片分裂治理（方案 E MVP 审查）

### 给父会话的最终输出（必填）

## 决策：**ACK 方案 E**，含 4 条强制修改要求 + 3 个隐藏破坏点 + 闸门量化 + canonical 选择方法

### 一、ACK 方案 E（MVP）—— 不选 B / D

核心理由（按优先递减）：

1. **议题 5 历史定性已物理验证不冲突**（PENDING_DECISIONS L171）："6 个模糊匹配全是同姓异人...audit 接受作为已知误报"——这是 audit_distribution.py 的 **owner→entity** 漂移检查，扫的是 `perspective_owner 写"王亮总"但王亮.md aliases 不含"王亮总"`。本议题是 **entity→entity** 同义碎片扫描（4 张卡片本身互为别名），扫描方向正交、扫描代码独立、不复用。议题 5 判定保留，本议题独立登记为 17。
2. **议题 12 fold v2 灰度还没真跑**——议题 14/15 的 essence (`theory-gap-without-data`) 直接适用于本议题：在没看到全 batch1 跑完的分裂率曲线之前，alias_dict SSOT (B) 是"用清晰对象的确定性伪造模糊对象的确定性"。MVP 先建反馈循环，让分裂率成为可见数据点。
3. **AIBP 4 卡 + 川锅 84 facts 等 TOP 痛点**不需要 alias_dict 也能立即吃掉——MVP 工具足以一次性处理首批存量分裂；alias_dict 解决的是**未来批次的预防**，不是**当前存量**。预防层在没看到复发率前不做。
4. **方案 D（A+B+C）违反 cgboiler 自己 PRINCIPLES §3 反模式表第六行**——"一次性建好，定期重跑而非增量"。在已经跑了 7 batch、1900 facts 的库上同时改 schema/extract/render/audit 是大手术；MVP 的 audit 加扫描 + merge 工具是**纯增量、可独立验证、可独立回滚**。

### 二、4 条强制修改要求

#### 修改 1：**merge_entity.py 必须先 dry-run 不写盘**（必加）

CLI 接口必须分两阶段：

```bash
# 阶段 1：dry-run 输出 plan（必跑，不可跳过）
python3 _pipeline/merge_entity.py \
    --canonical "AI BP工作室" \
    --aliases "AIBP工作室,AIBP室,AI BP团队" \
    --kind org \
    --plan-out /tmp/merge-aibp.plan.json

# 输出：会迁移的 fact 数 / evidence_id 冲突 list / canonical 卡 frontmatter diff / L2 STALE 标记位置
# 人工审 plan 文件，确认无误后

# 阶段 2：apply（必须显式 --apply 才动盘）
python3 _pipeline/merge_entity.py --plan /tmp/merge-aibp.plan.json --apply
```

**理由**：merge 是中等不可逆动作（rm 别名卡 + 改 canonical 卡），失败成本高于 audit 报警。dry-run 是 IRREVERSIBILITY 闸门的工程承诺。Keith 工作流偏好"方案先对齐再动手"——CLI 直接 apply 违反这条工程纪律。

#### 修改 2：**plan 文件必须 git 管，merge 必须配套写 PROGRESS 日志**

每次 merge 一份 plan.json 留盘到 `_pipeline/merge_logs/YYYY-MM-DD_<canonical>.json`（不是 /tmp 一次性），同时在 `_pipeline/PROGRESS.md` 顶部追加一条：

```
### 2026-05-XX | entity merge: AI BP工作室 ⊆ {AIBP工作室, AIBP室, AI BP团队}
- merged_facts: N
- conflicts: 0
- L2 STALE 已标记，等下次 AUTO_TICK l2_refurb
- plan: _pipeline/merge_logs/2026-05-XX_AI-BP工作室.json
```

**理由**：merge 改的是 entity 卡片本体——不是临时探查，是结构性变更。没有日志 = 三个月后忘了"为啥 AIBP 室没了"。这是议题 14 阶段已撞见过的工程债（"中冶焦耐 vs 中冶焦耐院 evidence_id 各属一卡"），要避免本议题处置后又留下"忘了处置过"的二次债。

#### 修改 3：**audit 同义簇扫描必须 stable + reproducible**

audit_distribution.py 加扫描时**必须**：

- 输出**确定性顺序**（按 `(kind, canonical_alphabetical, fact_count_desc)` 排序），不要按 dict 内部哈希顺序——否则每次跑出新 ⚠️ 顺序，无法 git diff
- 提供 `--ignore-clusters <slug,slug,...>` flag，让"已审过决定不合并"的 cluster 加入豁免清单（如议题 5 的同姓异人方向触发的 6 个误报，应该在本议题上线时迁移到 ignore list，而不是让 owner→entity 检查和 entity→entity 检查互相打架）
- 阈值默认温和：**只扫"≥ 3 fact + name 字符串编辑距离 ≤ 2 OR 包含/被包含 OR 缩写匹配（去除空格/连字符后子串相等）"**，不扫边缘 case
- ⚠️ 不阻塞 audit exit code（议题 14 阶段 PRINCIPLES 已经定 audit warning 不阻塞）

**理由**：扫描噪声大 = 信号被淹没。议题 5 已经吃过"6 个误报全部 false positive"的亏，本议题扫描器要一开始就配豁免机制。

#### 修改 4：**首例 AIBP 必须配 audit 双跑回归测试**

首例 merge 跑完后**必须**：

```bash
# merge 前
python3 _pipeline/audit_distribution.py > /tmp/audit-before.txt

# merge AIBP

# merge 后
python3 _pipeline/audit_distribution.py > /tmp/audit-after.txt

diff /tmp/audit-before.txt /tmp/audit-after.txt
```

差异必须**只**包含：
- entity 数 -3（4 → 1）
- AIBP 同义簇 ⚠️ 消失
- canonical 卡 evidence_count 增加 = 别名卡之和

**禁止**出现：evidence_id 数变化 / 跨卡 cite 漂移 / status 字段失配 / doctrine header 警告 / reactive bucket 变化。

**理由**：merge_entity.py 是新工具，第一次实盘跑必须有 before/after 客观比对。这是工程闭环证据（CLAUDE.md Delivery Standard "闭环证据"），不是"我抽几条看了都对"。

### 三、3 个隐藏破坏点（你 spot-check 漏的）

#### 破坏点 1：**视角冲突 (Derived View) 段失效**

SCHEMA §2 卡片结构里有 `## 视角冲突 (Derived View)` 段——多视角对同一事实不一致时呈现。AIBP 4 卡如果各自有 derived view，merge 时**视角冲突的 cite list 需要去重 + 合并**，否则 canonical 卡 derived view 会出现"`[^abc12]` 张吉峰视角 + `[^abc12]` 张吉峰视角"重复条目（如果同 evidence_id 在多张别名卡 derived view 里出现过）。

**修复**：merge_entity.py 处理 derived view 段时按 evidence_id 去重，重复 cite 合并为单条。

#### 破坏点 2：**Related 段双向引用悬挂**

SCHEMA `## Related` 段用 `[[name]]` 引用相关 entity。**别的卡片可能 Related 到 AIBP室** —— merge 后 AIBP室.md 删了，**别的卡片的 [[AIBP室]] 链接变成悬挂引用**。

**修复**：merge_entity.py 必须 grep 全库 `[[<别名>]]`，把所有引用改写为 `[[<canonical>]]`。这一步**不可省**，否则三个月后 batch3 跑完别的人发现 AIBP室 在某个 project 卡的 Related 里是死链。

具体范围：cgboiler/{people,orgs,projects,customers,doctrine,timeline}/ 全扫。

#### 破坏点 3：**doctrine 文件的 proposer / 引用段也可能含别名**

SCHEMA §6.2 doctrine 模板：`proposer: 王亮` + `## 引用` 段的 `[[王亮]]`。AIBP 不是 doctrine 主体，但**类似情况**会在 person 同实异名时翻车——例如未来如果有 person merge，"proposer: 张吉峰总" 这种 frontmatter 字符串值的别名同样要替换。

**修复**：merge_entity.py 扫描范围**包括** doctrine/ 目录下的 frontmatter 字段值（不只是 `[[]]` 链接）。person/org merge 时 frontmatter 字符串值替换是必需的。AIBP 当前只是 org，不踩 doctrine，但工具一开始就要 cover 这一类——否则下一次（首个 person 同实异名）就翻车。

### 四、闸门具体化（MVP → B 升级条件）

你提出"簇数翻倍"——不够具体，且单一指标容易被噪声扰动。建议**三条 OR 闸门**：

**闸门 1：分裂复发率**
batch1 全 26 片跑完后跑 audit 同义簇扫描，统计：
- 已 merge 过的 cluster 在后续 batch 又分裂出新别名卡（如本次 merge AIBP 4 卡到 AI BP工作室，batch1-008 后又出现 AIBP团队.md）的次数
- 触发：**任意 1 个 cluster 复发** = 升级 B（注入 alias_dict 到 extract_prompt）

**闸门 2：累计未处置簇数**
batch1 全 26 片 + batch2 5 片跑完后，audit 报的同义簇 ⚠️ 总数：
- < 5 个 → MVP 维持
- 5-10 个 → 评估期（再跑 batch3 看趋势）
- ≥ 10 个 → 升级 B

**闸门 3：merge 工时**
累计跑 merge_entity.py 的次数 ≥ 10 次 → 即使前两条没触发，工程上也证明手动维护成本太高，升级 B 自动化预防层。

**触发任意一条 = 升级**。**全部不触发 = MVP 即终态**——这种情况是合理结局，不是"还没达成"。

### 五、AIBP 首例 canonical 选择方法（不替你决策，给方法论）

你列了"AI BP工作室 ec=3 + batch1-006 报告含成立大会任命"作为倾向。**这是合理的内容信号，但不是充分的方法论**。建议三步法：

#### 步骤 1：物理实证四张卡的 frontmatter + L2 + facts 数

```bash
for f in "AI BP团队" "AI BP工作室" "AIBP室" "AIBP工作室"; do
  echo "=== $f ==="
  cat "cgboiler/orgs/${f}.md" | head -30
done
```

看：
- 哪张卡 evidence_count 最高
- 哪张卡 L2 写得最实（不是占位）
- 哪张卡 facts 时间跨度最长（最新和最旧 fact 的 date 范围）

#### 步骤 2：grep 原始 note 看川锅人自己怎么称呼

```bash
grep -E "AI ?BP ?(团队|工作室|室)" cgboiler/_pipeline/data/*.jsonl | \
  python3 -c "
import sys, re, collections
c = collections.Counter()
for line in sys.stdin:
    for m in re.findall(r'AI ?BP ?(?:团队|工作室|室)', line):
        c[m] += 1
print(c.most_common())
"
```

按"川锅人自己最常用的字面" 选 canonical。**这是组织自我表征的本体论一致性**——不是 Keith 觉得哪个名字漂亮，是川锅自己怎么叫自己。

#### 步骤 3：核对外部锚定（org-structure.md / 组织资料库）

如果 cgboiler/landscape 或 sizing 客观资料里 AIBP 有正式名字（成立大会决议 / 红头文件），那个是 canonical 的最高权威。

**三步法的优先序**：步骤 3 > 步骤 2 > 步骤 1。即外部权威 > 用法频次 > 当前卡片体量。

#### 关于"AI BP" vs "AIBP" 空格：

这两种是**同一组织的字面变体**，按步骤 2 看川锅人自己用哪个多决定。我个人猜测（不替你决策）：**口头/语音 note 多用"AIBP"无空格，文档/正式公告用"AI BP"有空格**——这种情况下 canonical 选哪个都行，把另一个当 alias 即可。

### 六、是否阻塞议题 12 灰度

**不阻塞**——理由你已说对：

- 议题 12 是 person/王亮维度，本议题主要痛点在 org/project/customer 维度，**对象正交**
- 议题 12 fold v2 改 render_cards.py（fold 逻辑），本议题改 audit_distribution.py + 新文件 merge_entity.py，**代码触点正交**
- 议题 12 的灰度数据本身可能给本议题闸门 1/2 提供更精确的复发率证据，**两者反而互补**

唯一交集：议题 12 fold v2 跑完会产生 _archive 文件，merge_entity.py 必须 cover _archive（你 spot-check 已识别）——这是工程实施层注意，不影响时序。

### 七、议题 5 判定要不要修订

**不要修订，独立登记**。理由你已说对，我额外补一句：

议题 5 当时的判定**精准到了它的扫描方向**——"audit owner→entity 扫描的 6 个 false positive 是同姓异人误报"。这个判定**至今仍然正确**。本议题是反方向 entity→entity 扫描，扫的是不同代码、不同算法、不同数据源。两个判定**共存合法**：

```
议题 5（保留）：owner→entity 漂移扫描的同姓异人 false positive，audit 接受
议题 17（新增）：entity→entity 同义碎片扫描，merge_entity.py 工具治理
```

PENDING_DECISIONS.md 议题 5 段落**不动**，议题 17 单独登记。

### essence 候选

slug: `merge-without-prevent-first`

一句话: 同义碎片治理先建合并工具（MVP）再建预防层（alias_dict）—— 没有合并能力的预防层在已分裂数据上是空头支票。

备选第二行（更哲学）：可见的分裂率比想象的预防机制重要——MVP 是让幽灵问题变成实测数据点的成本最低途径。

### 理由（推理路径）

- 装载 essence: `2026-05-06 / theory-gap-without-data`（议题 15 同源——MVP 让分裂率成为可见数据，alias_dict 升级闸门按数据触发不按理论触发）
- 装载 essence: `2026-04-21 / premature-abstraction-tripwire`（过早抽象的对症解是 tripwire——本议题的 tripwire = audit 同义簇扫描 + 三条 OR 闸门）
- 装载 essence: `2026-05-01 / ssot-distillation-vs-buffering`（不在没数据情况下建 alias_dict SSOT 缓冲层——B 路径就是 buffering 的典型形态）
- 装载 essence: `2026-04-21 / action-type-over-aggressiveness`（同一议题不同动作分流——audit 扫（自动化）+ merge_entity（人工 dry-run + apply）+ 复发闸门（数据驱动）三类动作各自独立裁决，不混档）
- 物理实证：Read PENDING_DECISIONS L171 议题 5 历史定性 / SCHEMA §2 卡片结构（Related + derived view 段）/ render_cards.py L667 aliases=[] 硬编码 / audit_distribution.py L313+ owner→entity 现有扫描

### 核心假设

1. AIBP 4 卡的 8 facts 中**没有 evidence_id 冲突**（同一 quote 在多张卡同 hash）——首例 dry-run 会验证；如果有冲突说明 normalize_quote 已经在跨卡复用 evidence_id（理论上不该有，每个 entity 卡的 fact 是为该 entity 抽的，但 reactive comment 多视角下有可能）
2. cgboiler/{doctrine,timeline,org-structure}.md 等非实体层的 `[[<别名>]]` 引用数量可控（grep 一遍能扫完，不需要建索引）
3. 川锅人自己对 AIBP 的字面用法相对一致（如果 jsonl grep 出 4 种字面频次旗鼓相当——比如各 100 次——那 canonical 选择会变成纯审美，需要 Keith 拍）

### 可能出错的地方

- **最可能崩点**：merge_entity.py 实施时漏 grep 某个非实体层文件的 `[[<别名>]]` 引用（如 `cgboiler/timeline/` 下的旧文件）→ 悬挂链接半年后被发现 → 信任 merge 工具的程度被削弱。**对策**：修改 4 的双跑 audit 测试要 grep 全库扫死链作为后置 verify
- **次可能崩点**：议题 12 灰度跑完产生 _archive，merge_entity.py 处理 _archive 时按"删别名卡 + 迁 facts"逻辑可能误删 _archive 文件结构（_archive 不是普通卡片，是归档载体）。**对策**：merge_entity.py 一开始就显式 cover `--include-archive` flag，默认 false，议题 12 跑通后再 review 是否要默认开
- **第三可能崩点**：闸门 1 复发率统计需要"已 merge cluster 历史"作为基线——MVP 没建这个表 → 闸门 1 实际无法运行。**对策**：merge_logs/ 目录就是基线，闸门 1 跑的时候按 logs 列表回溯检查每个 canonical 是否又出现新的同义簇

### 本次哪里思考得不够

- **MVP merge 一次性吃掉首批 TOP 痛点的具体优先级排序没给**——AIBP 4 卡 / 川锅 84 facts / 川锅环保 24 facts / 创新管理室 23 facts / 工程技术中心 15 facts 五个高 fact 痛点谁先合？我感觉应该按 **fact_count desc** 跑，但川锅 84 facts 那个簇可能 canonical 选择更复杂（"川锅公司"和"川锅本部"哪个更代表组织本体？需要 Keith 拍——它是组织自我表征的根节点）。父会话执行时按 AIBP 先跑（争议小、ec 低、用例代表性强）作为首例，然后川锅 84 这种根节点放最后等其他都跑过证明工具稳定再动
- **merge 后 evidence_count 字段在 frontmatter 自动重算**——render_cards.py 已经强制不可手改，merge_entity.py 应该走 render_cards.py 复用计数逻辑还是自己算？我倾向**复用 render_cards.py 的 inject + count 流程**，避免双源；但 render_cards.py 当前接口是从 jsonl 渲染卡片，可能没有"对已渲染卡片重新计数"的入口——这是工程实施细节，但你 6 条 spot-check 没覆盖
- **议题 13 字符上限漂移**（PENDING L128 临时弹性 1500-2000 字符）和本议题的 L2 STALE_AFTER_MERGE 重写有交互——merge 后 canonical 卡 facts 数翻倍，L2 重写时字符数压力更大。如果 canonical 卡本身已经在弹性档（>800），merge 后必然超 1500 → 触发议题 13 的"普通档/高 fact 双档"决策提前。**这是议题 13 加速触发的副作用，不是问题**，但父会话要知道

### 如果 N 个月后证明决策错了，最可能的根因

- **N=1 个月**：MVP 跑完 AIBP 首例后，发现 audit 同义簇扫描算法假阳性率高（>30%），每次 batch 跑完都报一堆误报淹没真信号 → 错的是阈值（修改 3 的"≥3 fact + 编辑距离 ≤2 OR 缩写匹配"过宽）→ 修复路径：缩窄阈值 + 加 ignore list，不需要升级 B
- **N=3 个月**：batch1 全 26 片跑完后闸门 1 触发（已 merge 的 AIBP 又分裂出 AIBP 团队.md）→ 升级 B alias_dict 注入 extract_prompt → 但发现 alias_dict 在 100-batch 内 token 成本可控、无 prompt 漂移 → MVP 阶段建反馈循环本身价值已兑现，升级是正常演进，**不算错**
- **N=6 个月**：议题 12 fold v2 跑完后发现 _archive 文件结构跟 merge_entity.py 假设不符 → 历史 merge 的别名卡 _archive 全部错位 → 错的是修改 4 的双跑 audit 测试没 cover _archive 状态（当时 _archive 还没产出，无法 cover）→ 修复路径：议题 12 灰度跑通后给 merge_entity.py 加 _archive 兼容性 patch + 回归测一次首批 merge

### 北极星触达

n/a——本议题是 cgboiler 工程治理决策，不直接涉及 gg 三条北极星。但本判断方法论（已沉淀 essence 作工具 + 物理实证 + 闸门量化分流 + IRREVERSIBILITY 闸门强制 dry-run）符合 gg 工作模式标准形态。

### 外部锚点

- `~/githubProject/cc-space/cgboiler/_pipeline/PENDING_DECISIONS.md` ← 议题 5 历史定性 L171 / 议题 17 待登记
- `~/githubProject/cc-space/cgboiler/SCHEMA.md` ← §2 卡片结构（Related + Derived View 段）/ §6.2 doctrine
- `~/githubProject/cc-space/cgboiler/_pipeline/render_cards.py` ← L667 aliases=[] 硬编码
- `~/githubProject/cc-space/cgboiler/_pipeline/audit_distribution.py` ← L313+ owner→entity 扫描（不动）
- `~/githubProject/cc-space/cgboiler/_pipeline/extract_prompt.md` ← L199 "别名留给 render 阶段从 frontmatter aliases 字段合并"（承诺未兑现）
- `~/githubProject/cc-space/cgboiler/_pipeline/FOLD_DESIGN.md` ← 议题 12 灰度（不阻塞）
- 关联议题：5（保留）/ 12（不阻塞）/ 13（加速触发副作用）/ 14（reactive bucket 兼容）/ 15（同源理论缺口提醒）

---
date: 2026-08-14
mode: work
slug: keith-mcp-mailbox-authority-store
status: substantive-decision
caller: monster 主会话（keith-mcp 留言箱真值源层级 + seatbelt write 去留）
---

# keith-mcp 留言真值源：存储拓扑方向裁决

## 给父会话的最终输出

### 总裁决

**方向 = A（留言权威存储迁出通道可达面，落 `~/.config/keith-mcp/`），并强制配一条来自 C 的部件：服务端把每条新增/已投递留言回写只读副本进档案 md 的往返记录。** B 降格为止血，不是方向。

**第二问：止血不够。A 的读侧必须先行**——第一刀是让投递读路径（takeUnread）停止消费 md、切到新 store（改动收敛在 mailbox.mjs + CLI + 测试，caller 协议零变更）。这一刀若不能在 ~1 个工作日内落地，先收回 seatbelt 那行 `write platform-help/mailbox`，档案契约回到停摆态，A 落地后再开。**不接受的状态：止血完成 + write 敞开 + 投递仍读 md，这个组合跨天运行。**

### 框架重写（为什么 menu 三项都没打中）

三个选项都把问题框成存储拓扑题；它实际是**凭据设计题**——「什么算 Keith 说的」目前由 parse 时的格式标记（`<!-- msg status=unread -->` 出现在一份多写者文件的任何位置）定义。README L19「CLI 只是便利层，手写一块同样生效」不是被 A 推翻的设计资产，**它就是漏洞的成文形态**：它把权威凭据定义成 in-band 格式事实。A 的本质是把凭据换成**写路径物理事实**——能写进那个 store 的只有 Keith 侧进程，写入动作本身就是签名。推翻那句 README 是修复本体，不是代价。

「两件事一起干」的合并决策（便利帧）当时隐式做了信任域合并：合并文件的写者集 = 两个角色写者集的并集，而任何从该文件读出权威语气的 reader，读到的是最弱写者。

### 判据链（essence 锚，全部现场核验）

1. `deploy-decision-must-not-read-untrusted-controllable-inputs`（05-19）：以 Keith 名义投递的函数（takeUnread→formatUnread）的事实输入，必须无一是通道物理可写的。B 做不到（Bash 目录内实测 exit=0），A/C 做到。
2. `network-cannot-cut-what-shares-tuple`（05-19）：seatbelt 只认目录、guard 只盖 Write/Edit 工具面——两层隔离都切不到「文件内段」这个维度。**目录粒度隔离下，文件是最小信任量子，「段内分权」物理不存在**。B 出局是物理结论，不是取舍。
3. `security-claim-as-physical-fact-not-injectable-grant`（05-19）：msg 标记是可注入授予的教科书活体。
4. `isolation-is-capability-subtraction-not-caging-the-dangerous-act`（06-25）：A 让「伪造 Keith 声音」从通道动作集里物理消失，且不是造新墙——是把数据搬进已有的墙（`~/.config/keith-mcp/` 已装 audit.jsonl，通道读写皆不可达）。
5. `separation-need-is-not-topology-verdict` 反向配重自检过：最轻形态（B）「装不下」的物理证据已在手（Bash exit=0 / 目录粒度 / guard 工具面），造墙合法。

### A > C 的裁决点

C 的墙 = 「messages 目录 ∉ allowlist write 行」这条**声明式不变量**；而 `read-allowlist.txt` 是活跃追加面（08-10 放行 9 条 → 08-11 整段撤销 → 08-14 开 mailbox write，一周三改），今天的洞本身就是合法需求驱动的权限迭代顺手开出来的——`one-shot-invariant-decays-under-live-append` 的活体。A 的墙是**结构性**的：`~/.config/keith-mcp/` 是服务私有空间，永远不是通道授权候选。次要判据：unread/read 投递状态是运行时队列态，本该跟服务住（`runtime-state-vs-business-data-distinct-ssot-domains` / `owning-service-not-proxy-for-write`），进 git 只会被 auto-commit 扫成噪音；服务端 RMW 与人手并发编辑的丢写竞态也一并消失。

C 的可 grep 性担忧由回写副本消解：档案 md 仍是「一件事一个读面」，动的只是写路径。

### 执行要点（方向层，不是实现清单）

- Keith 写留言路径收敛到 CLI（`mailbox:say` 已存在，stdin 长文）。**不要造「md 手写 → sync 提升入 store」的路径**——那会把 parse-from-md 用 Keith 权限重新引入，洞换个执行者回来。
- 服务端投递后把留言副本 echo 进档案 md 往返记录（通道对 `platform-help` 有 read，回写副本同时服务通道的上下文需求）。
- formatUnread 的「请把上面这段原样转达」是权威放大器，实现层顺手降调（附 ticket/来源指纹），不承重。

### 残余面（A 落地后仍在，明示不静默）

- 通道 Bash 仍可删/覆盖档案 md（毁证据/污染档案）：git 史兜底，「顺手滑移」档可接受；要收也不在 seatbelt 层追文件粒度。
- PM agent 正文注入 → 通道滥用其他能力（prod 部署 / DB）的面本来就在；A 摘掉的是最高杠杆奖品（Keith 的声音），不解决通道自身的注入顺从。
- 威胁模型参数升级建议报 Keith 一句：monster「顺手滑移」框架是给内部 Keith 侧工具定的；platform-help 是唯一消费外部输入的面，其有效写者集含间接注入，该面的威胁模型应显式记为「含注入意图」（`security-invariant-encodes-an-owner-set-threat-model`——这是 owner 参数，落库到 platform-help 文档即可，不改变本裁决）。

## 元属性反思

**核心假设**：① 「A 读侧先行改动量 ~1 个工作日内可落」是我对 mailbox.mjs 单模块收敛度的判断（288 行、投递读写全在此文件、caller 协议不变）——若实现中发现跨模块耦合（prompt.mjs / relay 层持 md 路径语义），窗口拉长，则触发「先收回 write」分支，裁决自带降级路径不翻。② 「~/.config/keith-mcp/ 通道不可达」采信 allowlist default-deny + 该目录不在清单——未实测该路径的 seatbelt 拦截，父会话落地时应加一条出目录写探针。

**可能出错的地方**：Keith 若高频手写 md 留言（而非 CLI），A 的体验税比我估的高——但「能力 > 体验」是 Keith 明示排序，且 CLI 保留同一心智（写一段话给某人）。

**推理盲区**：我没读 seatbelt profile 编译器（cc_codex_wrapper.py）本体，「write 行收回即生效」采信 allowlist 头部注释的机制描述。

**根因预判**：本案根因不是权限开错，是**文档合并决策没被识别为信任域决策**——「两件事一起干」写进 README 时无人问「两个角色的写者集是否同一信任级」。同形态风险点：monster 里其他「一份文件多角色」的载体（如 inbox 双写、threads 的服务端/人手混写面），值得父会话某次夜巡按「写者集 × 权威读者」扫一遍。

**北极星触达**：决策超越直觉（depth）——menu 三选项重写为凭据设计题，「推翻 README 设计的代价」反转为「那句设计就是漏洞」。

**essence 对齐自检**：`deploy-decision-must-not-read-untrusted-controllable-inputs` ✓（判据 1 直接消费）；`network-cannot-cut-what-shares-tuple` ✓（B 出局的物理依据）；`security-claim-as-physical-fact-not-injectable-grant` ✓（凭据重写的理论根）；`isolation-is-capability-subtraction` ✓（A 的定性）；`one-shot-invariant-decays-under-live-append` ✓（A>C 裁决点，allowlist 一周三改是新鲜物理证据）；反向打我的滴：`separation-need-is-not-topology-verdict`（造墙冲动）——已现场核「最轻形态装不下」的物理证据在先；`engineering-impulse-as-load-bearing-disguise`——committed 消费方存在（生产通道正服务真实 PM，洞今天已 commit 开着），非调研背书。对齐度：高。

## essence 候选滴（candidate-unverified）

```
## document-merge-is-a-trust-set-union (2026-08-14) [candidate-unverified]
把两份文档合并成一份的决策（DRY / 便利 / 「两件事一起干」帧）同时是一次静默的信任域合并：
合并文件的写者集 = 各角色写者集的并集，任何从该文件读出权威（以某人名义投递 / 授权语气）的
reader，其实际信任级 = 最弱写者。目录粒度隔离下文件是最小信任量子，「按段分权」在
seatbelt/guard 这类隔离层上物理不存在——权威读者与多信任级写者共文件时，唯一修法是
按写者信任级拆存储，把凭据从 in-band 格式标记换成写路径物理事实。
【前提：隔离层最细粒度 ≥ 文件；文件承载会被机器读出权威的内容】
物理证据：monster keith-mcp mailbox 案——README 明写「两件事一起干」+「手写一块同样生效」，
parseMessages 全文件 matchAll（mailbox.mjs:234），通道获 write 后即可伪造「Keith 给你的留言」
跨 caller 投递；Bash 目录内 exit=0 实证段级/工具级防御全部失效。
相关既有滴：security-claim-as-physical-fact-not-injectable-grant /
network-cannot-cut-what-shares-tuple / deploy-decision-must-not-read-untrusted-controllable-inputs
```

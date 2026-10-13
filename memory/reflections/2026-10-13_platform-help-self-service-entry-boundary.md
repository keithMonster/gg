---
date: 2026-10-13
slug: platform-help-self-service-entry-boundary
summoner: monster 主会话 /root
northstar_reach: "#3 决策超越直觉"
status: substantive-decision
---

# Reflection: platform-help 自助入口与权限边界

### 给父会话的最终输出

**设计裁决：PASS WITH CONDITIONS，可以实施本批受控附件入口与通知静态参数豁免。** 最近核到的五条成功通知都在请求取证或补执行入口，没有一条要求 Keith 裁定业务方案。把“更自主”再写一遍不会移走这个人工环节；应把已经授权的动作变成真正可调用的能力。

开题四问：① 重写问题为“哪些本该由服务闭环的步骤，把 Keith 留成了手工搬运节点”。② 错答案是通知变少、用户任务却停在原地，或能自助了但能写授权根/串用户附件；物理读数应为任务结果、保留的拒绝样本及实际写入集合。③ 对照方向为放开通用 Bash、把应用研发一并收进管家、保留现有权限并补受控能力；前两者分别扩大解释器射程、取消已有 PM 自助分工，均未命中这五条通知的实际诉求。④ 最便宜现实接触已做：读取五条 trace、现行 AGENTS、guard、归属查询测试和 intake-block.json；附件已保存候选、归属查询已有固定入口，不能把历史通知重报为现存故障。

**授权不必再扩一轮。** platform-help/AGENTS.md:16 已明确目标、平台配置、重启、部署和机制层自决；:149 已要求交付到应用 Agent 能动手；:233 保留信任根。分工是对的：平台负责平台步骤，应用 Agent 负责应用源码，请求人确认自身不可逆后果，Keith 只接实际缺失能力/访问权且必须由他完成的一步。

**附件入口准入条件：** 源固定为 monster/.cc-connect/attachments 中单文件名，目标固定为 cg-platform/received-files 中随机新文件；不接受任意路径/目标文件，不覆盖。用已打开文件描述符核普通文件、Unix owner、单链接及大小，拒符号链接和特殊文件；读写有上界，目标目录 0700、文件 0600，成功回执只含路径、字节数和摘要。摘要不符或中断不得留下可误认成功的完成件。保护入口脚本及执行依赖；隔离解释器导入，不从附件目录运行解释器。此入口只复制不解密、不执行、不应用配置，后续候选校验与业务确认沿原入口。

**附件归属的诚实边界：** Unix uid 只证明本机文件 owner；basename 和 SHA 只证明对象/字节，均不证明属于当前 sender/caller。本批沿现有“接入来源＋本任务权限”的服务判断可接受，不新造授权登记体系；不能宣称跨用户附件已经物理隔离。若以后硬绑定，依据必须来自接入端的附件→会话/调用者记录，不能用模型填写的 owner 参数。

**通知豁免准入条件：** 只跳过“正文出现受保护路径文字”的启发式，不跳过调用者、真实写目标、命令结构或其他边界检查。限固定绝对路径 notify.sh 的单条直接静态调用、critical/warning、platform-help 来源、company scope；拒环境前缀、shell 替换、管道、重定向、串联、重复与未知 flag。我已读 notify.sh：--context 只进入正文/trace，不读取文件，因此路径参数可按数据处理；该脚本消费 ALERT_WECOM_SCRIPT 环境覆盖，测试须覆盖显式环境改写，不能把“固定路径”宣传为完整不可变执行闭包。发送授权、独立复核和真实剩余阻塞判据保持原状，不用真实通知作测试。

**本批必须做：** 原注册 hook 链的正反例回放；用合成文件实际复制并核字节/权限；覆盖错误摘要、超限文件、symlink/硬链接/特殊文件、目录换成 symlink、覆盖既有文件、未准入调用者、shell 包装、notify 文本含路径与真的写同一路径。沿既有 494 项基线保留真阳性。说明放在附件及通知使用点，失败结果明确下一执行者，避免再加一套长“自主判断”清单。

**本批不做：** 不重做已修复归属查询、不重放旧票据、不代改 PM 应用源码、不绕远端访问拒绝、不清 release gate、不以少发通知验收。Haiku 上游精确证据和实时 gate 的后续状态须按主代理原件核对结果单列；没有实时结果就说证据未齐，不能因其他功能后来发布而判根因已闭合。

代价：受控入口需要维护，且不会自动解决全部未来工具能力缺口；收益是允许范围能被本地反例验证。下一次遇另一类真实重复障碍，再按动作补能力，不提前搭“万能能力代理”或通用权限配置平台。主代理 output/platform-help/2026-10-13-self-service/README.md 的批次范围与这项裁决一致。此为设计准入，不是实现通过；新脚本、guard 接线与实际测试仍由主代理验收。

### 核心假设

服务仍采用现行统一准入与读取自律策略；本批未获将平台私域和应用源码合并授权的目标。主代理后续状态取证另有独立执行者，我不把其派生文档当远端实况。

### 可能出错的地方

固定入口若接受可变执行依赖、可替换父目录或任意目标，会把窄能力变成改信任根的代理；只校验路径字符串不足。Unix owner 若被解释成业务 owner，会出现无证据的跨用户隔离宣称。

### 本次哪里思考得不够

未运行新实现、未核接入端附件与 caller 的现存关联格式，未复核远端 gate、SSH 或 daemon 实况。授权范围只允许本地读取与设计；这些缺口不能由 trace 填补。

### 如果 N 个月后证明决策错了，最可能的根因

每次堵点都各造一条固定入口而不回看共同能力边界，长期退化为难发现的白名单；或把通知下降误当自助完成率，真实诊断缺口被静默丢弃。

### 北极星触达

#3：把“放权限”的问题改写为“让已授权动作可调用”，并拆开内容字节完整性与请求人归属两个看似同一的安全判断。

### essence 对齐自检

- 对位：criteria-authorization-over-menu、control-flow-vs-fact-supply、safety-flip-needs-scoped-gate-not-deletion；已回原卷核读。
- 反向张力：separation-need-is-not-topology-verdict 与 recurrence-defense-pays-on-second-occurrence 反对无实例造新框架；本批有真实受阻实例，仅补两项入口，不扩大成新授权系统。security-invariant-encodes-an-owner-set-threat-model 要求不把本次范围擅自升成全面对抗隔离；本批仍沿现有服务读取自律。
- cross-check 关键词：criteria-authorization-over-menu、control-flow-vs-fact-supply、safety-flip-needs-scoped-gate、separation-need-is-not-topology-verdict、mixed-queue-funnels-all、security-invariant-encodes-an-owner-set-threat-model。

无 essence 候选：本轮是既有判据在新现场的应用，未得到独立新结晶。未执行业务改动、未外呼、未读凭据正文、未提交推送。

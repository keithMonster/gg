---
date: 2026-08-21
track: architecture
type: exploration
slug: replay-jurisdiction-begins-at-the-declared-input
---

# 重算的管辖权始于被声明的输入——#211 判别式的工业域夜核（供应链安全十二年）

## 为什么是这个方向

雷达：cc 连击 1 晚，architecture 窗口内仅 3 次。昨夜 auto_gg 刚补审入库 #211 `attestation-has-no-fixed-point-under-self-audit`（08-20 工作滴，实测击穿 n=1）——「审一个闸先问它重算了哪一侧」判别式 + 双终点（验证者重算 / 受信捕获根）。软件供应链安全恰是同一问题上跑了十几年的工业域：reproducible builds = replay 端工业化，SLSA provenance = attestation 端出货，Sigstore/Rekor = #207 账本住址律的活体。拿工业演化记录核单案判别式，同时给 #207 的二点归纳补第三域。

三个调研子代理并行取证（SLSA 演化史 / reproducible builds 现实采用 / Sigstore+xz 案），均强制 WebSearch/WebFetch，关键句原文照录。

## 裁决一：工业域整体确证 #211 双终点，且选了第二终点

- **Replay 端被从标准里砍掉**：SLSA v0.1 L4（hermetic + reproducible best-effort）在 v1.0 被官方「defer」（"had to be deferred to a future version in order to allow us to release v1.0 in a reasonable time frame"），至今 v1.2 仍只到 Build L3，hermetic/reproducible 仅在 future-directions 里 "may or may not be part of a future Build L4"〔slsa.dev 原文级〕。
- **Attestation 上限被官方结构化承认**：verifier 只能配置 roots of trust（"the recognized builder identities and the maximum SLSA Build level each builder is trusted up to"）；"SLSA Build L3 does not cover compromise of the build platform itself"〔原文级〕；v0.1 措辞更直白："there is no option but to trust the builder"〔摘要级〕。
- **全行业动作 = 建设受信捕获根**：SLSA L3 本质是把 provenance 签发权从 tenant 挪到 platform（被验者写不到的层）；Sigstore 官方自认整套是信任转移非消除（"simply shifts responsibility for the features of various Sigstore components to different parties…not removing trust!"〔官方博客原文级〕）。
- Reproducible builds 官方定位 = "one option for implementing the requirements"、"enable other build platforms to corroborate the provenance"〔原文级〕——**replay 在工业域是 attestation 的佐证件，不是默认闸**。

#211 的双终点结构在此域完整成立：重算太贵时，工程投资全部流向第二终点（受信捕获根），而不是在 attestation 输入端修补——与 #211「输入端修补零进展」的裁决同向。

## 裁决二（净新增）：replay 端自身有一个 attestation 型软肋——起点 artifact 谁供给

xz-utils 后门（CVE-2024-3094）的结构性事实〔多源原文级交叉〕：

- 后门触发代码只在 maintainer 手工发布的 release tarball 里，git 仓库没有（"The release tarballs upstream publishes don't have the same code that GitHub has…The version of build-to-host.m4 in the release tarballs differs wildly from the upstream"〔thesamesam gist〕）。
- **完美 provenance 抓不到**：攻击者是合法维护者，builder 会如实签发「我诚实地从这个（带毒）tarball 构建」——attestation 忠实地证明了错误的东西。
- **完美 reproducible builds 也没抓到**：NixOS 是近似可复现生态，照样 ship 了恶意版本（"NixOS and reproducible builds did not detect the xz backdoor, and in fact NixOS shipped the malicious builds"〔HN lolinder〕）；躲过 Debian/RPM 触发条件是巧合非机制。重算是忠实函数——起点带毒时，replay 逐字节复现后门。
- 事后行业修法两条〔原文级〕："Diff and review all 'golden' upstream tarballs used by distros against the output of creating a tarball from the git tag"〔thesamesam〕+ 多发行版转向直接从 git 构建（"Several Linux distributions moved toward building packages directly from git with reproducible-build toolchains rather than from upstream tarballs"〔Fedele〕）。

提炼：**replay 的管辖权始于被声明的输入。「什么算输入」的定义权本身是验证链上无人重算的一环**——它留在被验者手里时（maintainer 手工 tarball 就是被声明的起点），replay 端与 attestation 端同归于尽。修法与 #211 双终点同构但作用在上游一层：把链条起点搬进被验者写不到的公开对象（git tag / 最小 source-only tarball）。判别式递归化：审一个闸，问完「它重算了哪一侧」，再问「它从哪里起算、起点谁供给」。

结构条件：这条缝的存在性依赖「起点 artifact 与权威源可分离」——autotools 生态生成文件不入 git、发行版从 tarball 构建，才有 source→tarball 缝。05-19 `deploy-decision-must-not-read-untrusted-controllable-inputs` 的「收敛到不可信方够不到的权威源」在此域的精确形态。

## 裁决三：replay 工业史的消费侧账单（第二候选轴）

- Debian 12 年做到 95-96% 复现率〔官方 micronews "over 95%, and counting" 原文级〕，policy 仍是 "should" 非 "must"〔wiki 原文级〕。
- **独立重建高度中心化**：reproduce.debian.net 主要由一人（Holger Levsen）运营；rebuilderd README 自认 "there's no definite truth, and you could ask multiple instances including one you operate yourself"〔原文级〕——「独立」是架构可能性，不是运行现状。
- **安装侧零默认比对**：apt/pacman 无内建复现性检查〔论文动机陈述佐证，负证据〕。
- **零真实抓获**：12 年、数十万包，未检得任何一起「重建比对抓到真实篡改」纪实；所有引用全是 "could have detected" 反事实句式；真实事件（xz、event-stream、ua-parser-js）全部由异常行为/账号监控抓到〔多方向检索负证据〕。
- 账本侧同构：Rekor 只记录不判断（"single-party attestation that a piece of data existed prior to a certain time"〔原文级〕），但 witness/monitor 生态是纸面假设（"We **assume** that there are multiple monitors of Rekor"〔威胁模型原文级〕；Rekor v2 GA 时 checkpoint 未被见证、公共 witness 网络未上线〔官方博客〕；Trail of Bits："If new entries are not monitored, the security benefits of using a log are greatly reduced"〔原文级〕）。
- 唯一 replay 默认化的活体 = Go：gorebuild nightly 真重建比对（"As of Go 1.21, the Go toolchain is perfectly reproducible"〔go.dev 原文级〕）；注意 sumdb 是纯透明账本（一致性证明，不重建）——Go 把 replay 端和账本端分开建，各司其职。

对位：#195 `trace-presence-substitutes-for-the-check-it-invites`（复现率徽章在读者侧增信，核验动作无人消费）+ #205 `substrate-ships-the-evaluator-body-not-its-eyes` 谱系（能力出货、接线缺席）+ `watchdog-topology-lacks-a-top`(07-03)（账本的看守是假设层）。反驳预期：威慑价值不可证伪——零抓获亦可读作威慑成功或攻击者绕道（xz 恰是绕道实证：攻击者选了验证链覆盖外的缝）。

## 与 #207 账本住址律的第三域对照

#207 前提自注「住址律为二点归纳（IDS 反例+AML 正例各一域）」。本夜补：Rekor/sumdb = 「状态进不判断的机械账本、判断留给查询方」的工业实现，账本住在被验者写不到的独立强制层（Merkle tree + 包含/一致性证明）——第三域正例。但同时暴露住址律的后半句敞口：账本层自身的看守（witness）在此域是未兑现假设——#207「账本层自身的看守问题不在本滴射程」的射程外问题，工业域同样悬置。

## 候选滴与验证关 verdict

**主滴 `replay-jurisdiction-begins-at-the-declared-input`（裁决二）→ PASSED-WITH-EDITS 四修采纳，已入库**。
最强反驳点（E1）：初稿修法句「搬进被验者写不到的公开对象」在锚案上错位——Jia Tan 对 git 有完全写权且真写了（载荷 commit 在 git、只有触发用 m4 在 tarball），git tag 的保护机制是**写入即公开留痕 + 可从权威源重算比对**，不是写权排除；照字面执行会误判 git tag 不合格、或误信「进 git = 进被验者写不到的层」漏掉 git 内投毒面。已改。
E2：补引 `evaluator-input-ownership`(05-19)——最强重复向量经它走（「定义权留生成侧=独立性被收回」的一般形），净新增显式划界为递归判别式 + 重算端点条件化。E3：「同归于尽」拆档——replay 半边直接实证、attestation 半边结构推演（SLSA 级 provenance 本案未部署，属反事实）。E4："no option but to trust the builder" 引号去除改摘要级转述。
Evaluator 输入清单：探索档全文 + #211/05-19 三滴/watchdog/# 207 视图条目亲读 + candidate-refuted 全目录查重（首提，无重掷）；工具痕迹自报仅 Read + 只读 grep/sed，零写操作。

**次候选 `replay-industrializes-capacity-not-consumption`（裁决三）→ REFUTED，不入库，存档如下。**

candidate-refuted: 三滴域实例组合无独立结构性净新增（谱系注自认——#195 机构级形态 + 06-27 replay 域实例 + 07-03 工业面，零净新增申报；与 07-24 REFUTED 案同型）。候选全文：

> 重算能力的工业化不自动生成重算的消费环路：十二年 95% 复现率的生态零真实抓获（全部引用为 "could have detected" 反事实句式，真实事件均由异常行为/账号监控抓到），独立重建收敛于单人运营、安装侧零默认比对，账本的看守以 "we assume" 形态在场——复现率徽章照常在读者侧增信。
> 【前提：「零抓获」为多方向检索级 absence 非全域遍历；威慑效果不可证伪；唯一反例活体 Go（gorebuild nightly 为官方自跑，非第三方环路）；「徽章增信」为帧层推论无读者侧行为直测】

Evaluator 留的复提路径（本夜不重掷）：既有滴不持有的两件事实——① Debian 自产自销（builder 即 consumer）12 年仍零接线，击穿 #205「接线是买家自装件」隐含的「买家会装」出路；② 唯一活体环路 Go 是能力所有者官方自跑——合指向候选未写出的真结构：**「消费环路只在能力所有者主体内部生成，跨主体从不自发」**。若以该跨主体轴为核心句重写复提，按 essence.md 复提规则附本 REFUTED 记录 + 新增对照案例（更多「所有者内环路 vs 跨主体零环路」）再审。

## 证据来源索引

- slsa.dev spec v1.0 whats-new / v1.2 build-requirements / verifying-artifacts / faq / future-directions〔子代理 A 原文级〕
- slsa.dev blog "Mini Shai-Hulud: what SLSA can and cannot do"（"A signed artifact is not necessarily a trustworthy one" / "The boundary of observability is the boundary of the trust context"）〔原文级〕
- docs.sigstore.dev security / threat-model；blog.sigstore.dev "Why you can't use Sigstore without Sigstore" / rekor-v2-ga；Trail of Bits 2025-12-12〔子代理 C 原文级〕
- thesamesam xz gist / manuelfedele git-tarball-gap / luj.fr how-nixos-could-have-detected-xz / HN 43448745〔子代理 C 原文级〕
- tests.reproducible-builds.org / reproduce.debian.net / micronews.debian.org 2025 / wiki.debian.org ReproducibleBuilds / rebuilderd README / go.dev/blog/rebuild〔子代理 B 原文级〕
- arXiv:2505.21642（Arch 75.8%）/ arXiv:2608.18180（管道 vs 验证等级）/ arXiv:2501.15919（nixpkgs 69%→91%，摘要级）/ ICSE25 打包生态（摘要级）

三个子代理均自报 tool_uses 25-30，含 WebSearch/WebFetch；档位标注沿用子代理自报（原文级/摘要级/二手），主会话未逐条亲核网页。

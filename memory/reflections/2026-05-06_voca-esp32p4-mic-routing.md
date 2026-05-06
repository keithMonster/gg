---
date: 2026-05-06
slug: voca-esp32p4-mic-routing
summoner: cc-space
northstar_reach: #1 二阶效应
status: substantive-decision
---

# Reflection: Voca ESP32-P4 物理麦克风路线决策

### 给父会话的最终输出

**推荐**：

1. **做不做：做。但项目身份从「Voca 硬件升级」改名为「ESP32-P4 + UAC2 学习项目」**——按探索项目算，不按工程项目算。Voca 是它的第一个落地工件，不是它的目的。
2. **路线：A（USB Audio Class）优先 spike，timebox 8h（不是 4h），前置 2h 资料 sub-agent 调研**。B 路线（以太网）作为冻结降级，不在 8h 内强切。
3. **项目位置：`cc-space/esp32p4-lab/` 新建工作区**（不放 voca/、不开独立 repo、不进 Voca 主仓 hardware/）——`-lab` 后缀自动激活探索豁免。
4. **起步顺序**：建工作区 + CLAUDE.md → 派资料 sub-agent（2h，强制 WebFetch/WebSearch）→ Keith 并行跑 ESP-IDF hello-world → 8h spike 目标"macOS ioreg 枚举到 UAC"，不要求音质/FN/Voca 端打通 → 通了再写 brief 决定后续。

**理由**（核心三层）：

- **层 1（cost-benefit 框架错位）**：父会话在工程框架下推 A vs B vs C，但本项目按工程算 ROI 是负的（Voca 内置麦已稳定）。Keith 的 5 年北极星 #1（二阶效应洞察）依赖学习稀缺领域——硬件层 / RISC-V / UAC2 / I2S 是真的 LLM 没炒过的冷门，**学习收益巨大**。CLAUDE.md User Profile 明示"研究/学习类工作允许慢、允许反复，不套工程项目 cost-benefit"——本项目命中。
- **层 2（"东西买了找点用"信号读取）**：板子是 86 型墙面控制面板（带继电器 + 工业供电 + RJ45 + LVGL 屏），形态特殊到只能服务长期意图（家居/工业控制），不是合理化消费。Voca 是借口不是终点——**长期项目应该按长期项目对待**。
- **层 3（项目命名物理学）**：叫 `voca-esp32-mic` = 工程框架自动套上 = ROI 砍刀挥下来；叫 `esp32p4-lab` = 探索框架自动豁免。命名 = 引力分配（对应 essence `field-gravity-over-prompt`）。

**trade-off**：

- 8h spike 没通的代价 = 8h 工时 + 一周冻结期写复盘——可接受
- 资料 sub-agent 2h 可能给出"P4 UAC 不成熟"结论 → 此时仍应跑 hello-world（点亮工具链是探索本身的产出，不依赖 spike 结论）
- A 路线即使 UAC 通了，FN 模拟仍可能死在 macOS 私有 HID usage page（**新增第 5 条不确定性**——父会话原列表漏了）—— 此时降级为"USB Audio + 物理键 K1/K2 走另一通道触发录音"，不一定要走 B
- 项目位置选 `cc-space/esp32p4-lab/` 内联 firmware 代码 = 跟 cookie-arcade 模式一致，不脱离 cc-space 心智边界

**未核验假设**：

- esp-iot-solution `usb_device_uac` 组件 P4 适配状态（资料 agent 待证）
- macOS `.function` modifier flag 是否区分 Apple 内键 vs 外接 HID 来源（Apple 私有 HID usage page 行为）
- 86 型面板 Type-C 物理布线是否支持 CH9102 + P4 原生 USB 复合（schematic 待找）

**行动建议**（父会话下一步具体动作）：

1. 把决策草案改名（`voca-esp32-mic` → `esp32p4-lab`），告诉 Keith 命名变更的理由（探索 vs 工程的引力分配）
2. 在 cc-space 新建 `esp32p4-lab/` 工作区，写 CLAUDE.md（声明探索属性 / 列硬件事实 / 列 5 条不确定性 = 父会话原 4 条 + FN 来源识别）
3. 起一个 Task sub-agent 跑 2h 资料调研（强制 prompt：必须 WebFetch/WebSearch，调研 esp-iot-solution P4 UAC 适配 + Waveshare schematic + brianhealey/alaltitov 仓的 USB 配置 + macOS USB HID FN 模拟可行性，返回结构化报告）
4. **同时（不串行）**让 Keith 跑 ESP-IDF hello-world——工具链点亮是 spike 的前置条件
5. 资料 agent + hello-world 都完成后，再启动 8h UAC spike，目标只是 macOS ioreg 枚举到 USB Audio Device

### 核心假设

1. Keith 的探索驱动力对硬件层 = 高优先级（CLAUDE.md User Profile 明示 + 主动买稀缺形态板子的行为信号双佐证）
2. 命名能改变下游决策框架——`-lab` 后缀触发 cc-space CLAUDE.md 的"研究类豁免" memetic effect
3. 8h timebox 对 ESP-IDF + UAC2 调通 macOS 枚举是合理量级（基于 esp-iot-solution 已有 example 的前提）
4. Voca 的 `AVAudioEngine.inputNode` 跟随系统默认输入设备 = 物理事实（已读源码确认）
5. ESP32-P4 USB 2.0 HS 硬件能力 = 真的存在（Espressif 官方文档 + 第三方固件实证已跑通其他 USB device class）

### 可能出错的地方

- 资料 agent 返回"P4 UAC 完全没适配"——此时 spike 路径要重定义（自己实现 UAC2 descriptor 而非用现成组件 = 工时×3，可能超出探索项目合理边界）
- macOS 对 HID FN 来源的限制比预想严，A 路线即使通了也只能"USB Audio + 物理键触发"而非"零改 Voca"——此时 A 路线收益降级，但仍优于 B
- 8h spike 不够——esp-idf 工具链 + I2S codec init + UAC2 descriptor 三层叠 debug 可能 16h 起步，timebox 设计偏乐观

### 本次哪里思考得不够

- 没拉通 esp-iot-solution 仓的 P4 example 实际状态（决策依赖资料 sub-agent，不是我直接核验）—— 这是 cc_agent 模式下我的合法边界（不动代码不 WebFetch），但导致 8h timebox 是基于"应该有 example"的乐观假设，置信度 3/5 不是 5/5
- 86 型面板的物理形态对长期意图的暗示我读出来了，但没去验证 Keith 最近在 cookie-arcade / 家居方向有没有累积信号——这个验证应该在父会话或下一轮会话补上

### 如果 N 个月后证明决策错了，最可能的根因

- 最可能根因：Keith 在 hello-world 阶段就被 ESP-IDF 工具链劝退——硬件项目的真实 onboarding 成本被低估，根本到不了 UAC spike。**信号**：hello-world 拖到 1 周以上没通，应该立刻冻结项目而不是继续推 spike
- 次可能根因：A 路线技术上通了，但 macOS 端 FN 接住失败 + 物理键 K1/K2 + Voca 改造也复杂 = 总改动量 ≥ B 路线 + 收益增量低于预期，回头发现该走 B
- 第三可能根因：项目命名为 `-lab` 后真的按探索节奏走，但 Keith 半年后回看发现"我学到了 ESP-IDF + UAC2 但没产生任何工件"= 探索项目的"学到 ≠ 沉淀"问题

### 北极星触达

#1 二阶效应（space）—— 学硬件层 + USB 协议栈 + RISC-V 嵌入式 = Keith 5 年长期领先里 LLM 不会替你学的稀缺维度。次触达 #2（动态学习反哺）—— `-lab` 工作区命名机制本身是把探索项目从工程项目隔离出来的方法论沉淀，可复用到未来其他探索项目（不只 esp32p4-lab，还包括未来的 hardware-lab 系列）。

### essence 候选

- slug: project-naming-as-frame-allocation
- 一句话: 项目命名是认知框架的引力分配——`-lab` 后缀触发探索豁免，工程后缀触发 ROI 砍刀。改名 = 改下游所有决策的引力方向。
- 是否已 append 到 essence.md: Y

### 外部锚点

- `~/githubProject/Voca/Sources/Voca/Core/HotkeyManager.swift` ← FN 监听机制源码（NSEvent global monitor + flagsChanged）
- `~/githubProject/Voca/Sources/Voca/Core/AudioCapture.swift` ← AVAudioEngine.inputNode 跟随系统默认输入设备（A 路线零改前提）
- `~/githubProject/cc-space/esp32p4-lab/` ← 待 Keith 创建的工作区

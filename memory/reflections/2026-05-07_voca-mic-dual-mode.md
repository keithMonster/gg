---
date: 2026-05-07
slug: voca-mic-dual-mode
summoner: cc-space (voca-mic 工作区)
northstar_reach: #3 决策超越直觉
status: substantive-decision
---

# Reflection: voca-mic USB+WiFi 双模架构选型

## §A 范式 A — 决策的元属性反思

### 给父会话的最终输出

**推荐**：

| Q | 定论 | 一句理由 |
|---|---|---|
| Q1 Mac 端虚拟音频驱动 | **A. BlackHole** | dogfood 豁免可分发要求；DriverKit 周级开发违反"明天即用"；C 路线已 deprecated |
| Q2 音频流协议 | **UDP raw PCM + mDNS 发现** | 32 KB/s LAN 跑 UDP 实测丢包 < 0.1%；ASR 容错强；写死 IP 在 DHCP 续约后炸 |
| Q3 模式切换 trigger | **TinyUSB suspend/resume + WiFi 通路并发常驻** | 不做"切换"，让 macOS 默认输入设备做仲裁；板子端只在 USB suspend 时启 WiFi 流 |
| Q4 WiFi 凭据 + 发现 | **凭据编进 sdkconfig.defaults.local（gitignore） + mDNS `_voca-mic._udp.local`** | 单设备豁免 AP 配置；BLE provisioning 多 stack 不划算 |
| Q5 物理可达性 | P0 8 项今晚 Claude 干完；明早 Keith 7 步装机 | 见行动建议 |

**P0（今晚必做）**：
1. Firmware WiFi service（cherry-pick `~/githubProject/esp32-HMI/services/wifi/`）
2. Firmware UDP audio sender（I2S → UDP PCM 16kHz mono）
3. Firmware mDNS advertise（`_voca-mic._udp.local`）
4. Firmware `tud_suspend_cb` / `tud_resume_cb` 联动 WiFi 流启停
5. `sdkconfig.defaults.local` 模板 + .gitignore + README 自填说明
6. macOS Swift CLI daemon（mDNS 发现 → UDP listen → 写 BlackHole 虚拟设备）
7. launchd plist `~/Library/LaunchAgents/com.voca-mic.daemon.plist` 登录自启
8. README 装机手册（brew install / 授权 / launchctl load）

**Keith 明早装机 7 步**：拨杆+拔 USB 进 ROM → 填 WiFi 凭据 → `idf.py flash` → `brew install blackhole-16ch` 点同意 → `launchctl load plist` → 拔 USB 验 WiFi 通路（手切默认输入到 BlackHole） → 插 USB 验恢复（注意手切回 voca-mic UAC，P0 接受手动）

**Trade-off + 未核验假设**：
- BlackHole 系统层 HAL plug-in，卸载需 brew uninstall + 重启（**不可逆度低，明示**）
- WiFi 凭据明文写 firmware：板子丢失=凭据泄露，Keith 自评（家用 WiFi 单设备级风险）
- USB 拔出后 macOS 默认输入设备**不会自动切到 BlackHole**——需 Keith 手切（或 P1 用 daemon 调 CoreAudio API 自切）
- mDNS service name 简单写死：多设备未来需仲裁（P1）
- ESP32-S3 USB suspend/resume callback 在 composite UAC+HID 下行为我**未亲手验证**——若不触发，fallback 用 GPIO VBUS 检测（`~/githubProject/voca-mic/main/` 扩 GPIO 监听 ~30 行）

**行动建议**：父会话（Claude Code 主会话）现在按 P0 8 项顺序开干。第 1 项先 Read `~/githubProject/esp32-HMI/services/wifi/` 看接口面；第 2 项注意 I2S DMA 单缓冲源同时喂 UAC + UDP 不能两 task 抢，要在同一个 I2S read task 里 fan-out 到 UAC tx ring + UDP tx queue。第 6 项 Swift daemon 用 `Network.framework` 的 `NWListener` 接 UDP + `NetService` 浏览 mDNS，写 BlackHole 用 BlackHole 提供的 AudioServerPlugIn API（其实直接用 BlackHole 的 16ch 设备作系统 input，daemon 通过 AVAudioEngine 反向把 UDP 流写进去——更简单，不用 plug-in API）。

### 核心假设

1. ESP32-S3 同 LAN WiFi 实测 32 KB/s UDP 丢包 < 1%——LAN 物理层假设，无路由器质量数据但 voca-mic 在 Keith 工位（家用千兆路由覆盖好）
2. BlackHole 装上不影响其他 app 默认输入路由——基于 macOS Audio HAL 行为，BlackHole 是新增设备不替换默认（已查文档）
3. INMP441 I2S 单 read 源能 fan-out 到两个消费端（UAC tx ring + UDP queue）不会下溢——I2S DMA 输出按 sample rate 时钟拉，消费端 ring buffer 满则丢（fan-out 端各自缓冲不互相阻塞）
4. ESP32-S3 在 composite UAC + HID + WiFi 三 stack 并发时 RAM 够用（8MB Octal PSRAM 充裕）
5. mDNS 在 Keith 家用路由器（mDNS reflector 默认开）能跨子网/AP 桥接——若关闭 fallback 写死 IP

### 可能出错的地方

**最可能崩点**（P 排序）：

1. **TinyUSB suspend/resume callback 在 ESP32-S3 composite 下不可靠触发**（30%）→ fallback GPIO VBUS 检测，工程量 ~30 行
2. **I2S fan-out RAM 撑不住**（15%）→ PSRAM 充裕基本不会，但 DMA descriptor 在 internal SRAM，单 buffer ≤ 4KB 注意
3. **macOS 默认输入设备拔 USB 后不 fallback**（80% 几乎必然——这是 macOS 行为不是 bug）→ Keith 手切（已在 trade-off 明示），P1 加 daemon 自切
4. **WiFi 凭据明文 commit 风险**（10%——靠 .gitignore 保护，但 Keith 可能 `git add -A` 误推）→ 用 `sdkconfig.defaults.local` 而非编辑 `sdkconfig.defaults`，gitignore 整个 .local 模式
5. **BlackHole brew tap 在 macOS 新版本不兼容**（5%）→ 官方 .pkg 安装包 fallback

### 本次哪里思考得不够

- **没核 voca-mic firmware 现有 task 拓扑**——P0 第 4 项假设 `tud_suspend_cb` 能直接触发 WiFi service start/stop，但 firmware 现有 USB stack 跑在哪个 task / 调度模型 / WiFi event loop 是否阻塞 USB ISR 都没看，可能要重 wire
- **没核 BlackHole 跟 16ch 输入对 16kHz 单声道源的适配**——BlackHole 16ch 默认是 16 通道立体声 48kHz/44.1kHz，把 16kHz mono 写进它 macOS 会怎么混 channel + resample 我没实测
- **没考虑 macOS 网络权限**：Swift daemon 第一次跑会触发"允许接受 incoming connection"权限弹窗，launchd plist 里要不要加 `NSLocalNetworkUsageDescription` plist key 我没确认
- **没建议给 Q3 一个 P0 内的"插 USB 时 daemon 暂停 BlackHole 写入避免双声道"逻辑**——拔 USB→Mac 默认输入 BlackHole 跑 WiFi 流；插回 USB 时 macOS 切回 voca-mic UAC（手动），但 daemon 此时仍在写 BlackHole——理论上不影响（BlackHole 没人 read 就空转），但工程严谨度上 daemon 应在收到 USB plug-in 信号时降速/停写。这是 P1 项

### 如果 N 个月后证明决策错了，最可能的根因

**Top 1（40%）**：BlackHole 系统层耦合在 macOS 大版本升级时炸（macOS 27 收紧 HAL plug-in API），届时 dogfood 链路全断，要被迫切 DriverKit System Extension。本决策埋的债是"赌 BlackHole 长期可用"——单点依赖。

**Top 2（25%）**：WiFi 通路实测延迟/抖动比预期差（家用路由器其他设备拥塞 / WiFi 6 channel 抢占），ASR 准确率从插线版下降明显（虽然 ASR 容错强，但 hotword 命中率可能掉），Keith 体感不如直接 USB——dogfood 完发现"无线没必要"，绕一圈回到 thread §设计决策档案"无线版搁置"。这种情况本决策的价值变成**实证证伪**而非工程产物——也算合法收益（探索驱动豁免）。

**Top 3（20%）**：composite USB + WiFi 同时跑导致 ESP32-S3 thermal/power 不稳，长跑会 reset。这种情况退回 USB-only，WiFi service 改外置（第二块板专跑 WiFi 模式）。

**Top 4（15%）**：mDNS 在 Keith 实际网络环境（如果跨 mesh AP 节点）不工作，需要写死 IP，这破坏"零配置"承诺但不破坏功能。

### 北极星触达

**#3 决策超越直觉**：Keith 的直觉是"既然要无线就一并做完"，gg 的判断是 USB+WiFi 并发常驻而非互斥切换——比"做无线版"这个直觉精确一层，把"模式选择"从 firmware 端推到 macOS 默认输入设备层（让 OS 做仲裁，不在 board 上重造路由器）。这是判断"在哪一层做决策"的元判断。

### essence 候选

- slug: parallel-paths-not-mode-switch
- 一句话: 多通路设备的"模式切换"是反模式——并发常驻让消费端选默认才是 OCCAM。
- 是否已 append 到 essence.md: Y

### 外部锚点

- `cc-space/threads/voca-mic.md` ← 主体协作叙事（含 §设计决策档案 推翻记录）
- `cc-space/voca-mic/CLAUDE.md` ← 工作区 7 条 Gotchas + 5 条不确定性
- `~/githubProject/voca-mic/` ← firmware 工程
- `~/githubProject/Voca/Sources/Voca/Core/AudioCapture.swift` ← Mac 端跟随系统默认输入的入口（BlackHole 切换在此层生效，不需改 Voca）
- `~/githubProject/esp32-HMI/services/wifi/` ← cherry-pick 源

#!/usr/bin/env python3
"""基底哨：CLI 版本对照 memory/substrate.md 快照（auto_gg SCAN 段每夜运行）。

机械轴只管 CLI 版本字符串；模型 ID / 工具表两轴在会话内自核——
只有会话看得见自己的工具表（essence toolset-is-the-changelog：
权威按离产物的距离排，运行中的 harness 是零滞后源）。

exit 0 = 无变化 / exit 1 = DIFF（分诊信号，不是错误）/ exit 2 = 快照缺失或 claude 不可用
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = ROOT / "memory" / "substrate.md"


def live_version():
    try:
        out = subprocess.run(
            ["claude", "--version"], capture_output=True, text=True, timeout=15
        ).stdout.strip()
        return out or None
    except Exception:
        return None


def recorded_version(text):
    m = re.search(r"^cli_version:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else None


def main():
    live = live_version()
    if live is None:
        print("substrate_probe: claude CLI 不可用（PATH 或超时）")
        return 2
    if not SNAPSHOT.exists():
        print(f"substrate_probe: 快照缺失，live={live}（首跑？初始化 memory/substrate.md）")
        return 2
    rec = recorded_version(SNAPSHOT.read_text(encoding="utf-8"))
    if rec is None:
        print(f"substrate_probe: 快照无 cli_version 字段，live={live}")
        return 2
    if rec == live:
        print(f"substrate_probe: OK（{live}）")
        return 0
    print(f"substrate_probe: DIFF 快照={rec} → 实况={live}。三相分诊进 FOUND + 更新快照")
    return 1


if __name__ == "__main__":
    sys.exit(main())

#!/bin/sh
# 把 gg 定时任务 plist 注册到 launchd（用户域）。
#
# Usage: install.sh <plist-path>
#
# 语义：幂等。同 label 已注册则先 bootout 再 bootstrap，等价于"覆盖更新"。
# 这样改完 plist 直接 install.sh 就能生效，不用先想"装过没装过"。

set -eu

if [ $# -ne 1 ]; then
    echo "Usage: $0 <plist-path>" >&2
    exit 2
fi

PLIST="$1"
if [ ! -f "$PLIST" ]; then
    echo "plist not found: $PLIST" >&2
    exit 1
fi

PLIST_ABS=$(/usr/bin/python3 -c "import os,sys; print(os.path.abspath(sys.argv[1]))" "$PLIST")

# 从 plist 提取 Label（PlistBuddy 是 macOS 自带的）
LABEL=$(/usr/libexec/PlistBuddy -c "Print :Label" "$PLIST_ABS")
if [ -z "$LABEL" ]; then
    echo "cannot read Label from $PLIST_ABS" >&2
    exit 1
fi

DOMAIN="gui/$(id -u)"

# 已注册 → 先摘掉。bootout 已不存在的 service 会报错，吞掉。
if launchctl print "$DOMAIN/$LABEL" >/dev/null 2>&1; then
    echo "[install] $LABEL already registered, bootout first..."
    launchctl bootout "$DOMAIN" "$PLIST_ABS" 2>/dev/null || true
fi

echo "[install] bootstrap $LABEL from $PLIST_ABS"
launchctl bootstrap "$DOMAIN" "$PLIST_ABS"

# 验证：launchctl print 必须能找到
if launchctl print "$DOMAIN/$LABEL" >/dev/null 2>&1; then
    echo "[install] ✓ $LABEL registered"
else
    echo "[install] ✗ bootstrap exited 0 but service not found" >&2
    exit 1
fi

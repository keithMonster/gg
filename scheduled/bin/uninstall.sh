#!/bin/sh
# 摘掉 gg 定时任务（不删 plist 文件，只 bootout 服务）。
#
# Usage: uninstall.sh <plist-path | label>
#
# 既能传 plist 路径，也能传 label——bootout 接受两种形式。

set -eu

if [ $# -ne 1 ]; then
    echo "Usage: $0 <plist-path | label>" >&2
    exit 2
fi

ARG="$1"
DOMAIN="gui/$(id -u)"

if [ -f "$ARG" ]; then
    PLIST_ABS=$(/usr/bin/python3 -c "import os,sys; print(os.path.abspath(sys.argv[1]))" "$ARG")
    LABEL=$(/usr/libexec/PlistBuddy -c "Print :Label" "$PLIST_ABS")
    TARGET="$PLIST_ABS"
else
    LABEL="$ARG"
    TARGET="$DOMAIN/$LABEL"
fi

if ! launchctl print "$DOMAIN/$LABEL" >/dev/null 2>&1; then
    echo "[uninstall] $LABEL not registered, nothing to do"
    exit 0
fi

echo "[uninstall] bootout $LABEL"
launchctl bootout "$DOMAIN" "$TARGET" 2>&1 || {
    # bootout 在某些情况下返回非零但服务实际已摘——再 print 验证
    if ! launchctl print "$DOMAIN/$LABEL" >/dev/null 2>&1; then
        echo "[uninstall] ✓ $LABEL removed (despite bootout warning)"
        exit 0
    fi
    echo "[uninstall] ✗ failed to remove $LABEL" >&2
    exit 1
}

echo "[uninstall] ✓ $LABEL removed"

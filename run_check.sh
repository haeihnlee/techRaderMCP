#!/bin/bash
# 컨퍼런스 새 콘텐츠 자동 체크 스크립트
# cron: 매일 오전 9시 실행

SCRIPT_DIR="/home/haen/conference-mcp"
LOG_FILE="$SCRIPT_DIR/check.log"
PYTHON="$SCRIPT_DIR/.venv/bin/python"

cd "$SCRIPT_DIR"

RESULT=$("$PYTHON" - <<'EOF'
import os, sys
os.environ.setdefault("ANTHROPIC_BASE_URL", "https://llm.hedej.lge.com")

# load .env
env_file = "/home/haen/conference-mcp/.env"
if os.path.exists(env_file):
    for line in open(env_file):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            if v:
                os.environ[k] = v

sys.path.insert(0, "/home/haen/conference-mcp")
from server import check_new_content
print(check_new_content(days=1, auto_summarize=True))
EOF
2>&1)

echo "[$(date '+%Y-%m-%d %H:%M:%S')] =========" >> "$LOG_FILE"
echo "$RESULT" >> "$LOG_FILE"

# 새 콘텐츠가 있으면 알림
COUNT=$(echo "$RESULT" | grep -cE "^[▶📰]" || true)
if [ "$COUNT" -gt 0 ]; then
    # 데스크탑 알림
    DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus \
        notify-send "🎉 컨퍼런스 새 콘텐츠" "${COUNT}개의 새 영상/글이 있습니다" \
        --urgency=normal --icon=dialog-information 2>/dev/null || true

    # Teams / 이메일 알림
    "$PYTHON" "$SCRIPT_DIR/notify.py" "$RESULT" >> "$LOG_FILE" 2>&1
fi

#!/bin/bash
# 컨퍼런스 새 콘텐츠 자동 체크 스크립트
# cron: 매일 오전 9시 실행

SCRIPT_DIR="/home/haen/conference-mcp"
LOG_FILE="$SCRIPT_DIR/check.log"
PYTHON="$SCRIPT_DIR/.venv/bin/python"
CLAUDE_BIN="${CLAUDE_BIN:-/home/haen/.local/bin/claude}"

# cron 환경에서도 claude CLI를 찾을 수 있도록
export PATH="/home/haen/.local/bin:$PATH"
export CLAUDE_BIN

cd "$SCRIPT_DIR"

# ── 1단계: 새 콘텐츠 감지 + 트렌딩 조회 (LLM 호출 없음) ──────────────────────
RESULT=$("$PYTHON" - <<'EOF'
import os, sys

env_file = "/home/haen/conference-mcp/.env"
if os.path.exists(env_file):
    for line in open(env_file):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            if v:
                os.environ[k] = v

sys.path.insert(0, "/home/haen/conference-mcp")
from server import check_new_content, get_trending

conf_result = check_new_content(days=1)
trending_result = get_trending(sources="github,hackernews,devto,geeknews", limit=10)

print("===== 컨퍼런스 =====")
print(conf_result)
print("\n===== 트렌딩 =====")
print(trending_result)
EOF
2>&1)

echo "[$(date '+%Y-%m-%d %H:%M:%S')] =========" >> "$LOG_FILE"
echo "$RESULT" >> "$LOG_FILE"

# ── 2단계: 새 컨퍼런스 콘텐츠 자동 요약 (헤드리스 Claude Code, Max 구독) ────
# check_new_content 출력 형식:
#   ▶ [컨퍼런스명] 제목
#      <URL>
#      게시: ...
SAVED_FILES=()
while IFS= read -r line; do
    # 컨퍼런스명·제목 파싱
    if [[ "$line" =~ ^[▶📰][[:space:]]\[(.+)\][[:space:]](.+)$ ]]; then
        CONF_NAME="${BASH_REMATCH[1]}"
        CONF_TITLE="${BASH_REMATCH[2]}"
        # 다음 줄에서 URL 추출은 별도 루프에서 처리
        EXPECT_URL=1
        continue
    fi
    if [ "${EXPECT_URL:-0}" = "1" ]; then
        URL=$(echo "$line" | tr -d ' ')
        EXPECT_URL=0
        if [ -n "$URL" ] && [[ "$URL" =~ ^https?:// ]]; then
            echo "[$(date '+%Y-%m-%d %H:%M:%S')] 요약 시작: $URL ($CONF_NAME)" >> "$LOG_FILE"
            # 헤드리스 Claude Code로 /add-link 슬래시 커맨드 실행
            ADD_OUTPUT=$(timeout 200 "$CLAUDE_BIN" --print --no-session-persistence \
                --max-budget-usd 0.50 \
                "/add-link $URL $CONF_NAME" 2>&1)
            echo "$ADD_OUTPUT" >> "$LOG_FILE"
            # 저장된 파일 경로 추출 (save_summary_text 출력: "✅ 저장 완료: <경로>")
            SAVED=$(echo "$ADD_OUTPUT" | grep -oE "/home/haen/conference-mcp/summaries/[^[:space:]]+\.md" | head -1)
            if [ -n "$SAVED" ] && [ -f "$SAVED" ]; then
                SAVED_FILES+=("$SAVED")
            fi
        fi
    fi
done <<< "$RESULT"

# ── 3단계: 알림 ─────────────────────────────────────────────────────────────
CONF_COUNT=$(echo "$RESULT" | grep -cE "^[▶📰]" || true)
TREND_COUNT=$(echo "$RESULT" | grep -cE "^- \*\*\[" || true)
TOTAL_COUNT=$((CONF_COUNT + TREND_COUNT))

if [ "$TOTAL_COUNT" -gt 0 ]; then
    NOTIFY_MSG=""
    [ "$CONF_COUNT" -gt 0 ] && NOTIFY_MSG="컨퍼런스 ${CONF_COUNT}건"
    [ "$TREND_COUNT" -gt 0 ] && NOTIFY_MSG="${NOTIFY_MSG:+$NOTIFY_MSG · }트렌딩 ${TREND_COUNT}건"

    DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus \
        notify-send "🔥 개발 뉴스" "$NOTIFY_MSG" \
        --urgency=normal --icon=dialog-information 2>/dev/null || true

    # notify.py에 결과 전달 — 컨퍼런스 다이제스트 + 트렌딩 전체
    "$PYTHON" "$SCRIPT_DIR/notify.py" "$RESULT" >> "$LOG_FILE" 2>&1

    # 저장된 요약 파일을 Teams에 개별 카드로 게시
    for SAVED in "${SAVED_FILES[@]}"; do
        "$PYTHON" "$SCRIPT_DIR/notify.py" --file "$SAVED" >> "$LOG_FILE" 2>&1
    done
fi

# ── 4단계: 새 요약 파일 GitHub push ────────────────────────────────────────
NEW_SUMMARIES=$(git -C "$SCRIPT_DIR" ls-files --others --exclude-standard summaries/ 2>/dev/null)
if [ -n "$NEW_SUMMARIES" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 새 요약 파일 push 시작" >> "$LOG_FILE"
    git -C "$SCRIPT_DIR" add summaries/ >> "$LOG_FILE" 2>&1
    git -C "$SCRIPT_DIR" commit -m "auto: daily summary $(date '+%Y-%m-%d')" >> "$LOG_FILE" 2>&1
    git -C "$SCRIPT_DIR" push origin main >> "$LOG_FILE" 2>&1 \
        && echo "[$(date '+%Y-%m-%d %H:%M:%S')] git push 완료" >> "$LOG_FILE" \
        || echo "[$(date '+%Y-%m-%d %H:%M:%S')] git push 실패" >> "$LOG_FILE"
fi

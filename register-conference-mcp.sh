#!/bin/bash
# Conference Summarizer MCP CasePack 등록 스크립트
# 사용법: ./register-conference-mcp.sh <username> <password>

HUB_URL="http://10.157.71.52:5000"
USERNAME="${1:?Usage: $0 <username> <password>}"
PASSWORD="${2:?Usage: $0 <username> <password>}"
COOKIE_JAR=$(mktemp)

echo "=== ASF MCP Hub CasePack 등록 ==="
echo "서버: $HUB_URL"
echo "사용자: $USERNAME"
echo ""

# 1) 로그인 (JSON API 사용)
echo "[1/3] 로그인 중..."
LOGIN_RESP=$(curl -s -c "$COOKIE_JAR" -X POST "$HUB_URL/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"$USERNAME\",\"password\":\"$PASSWORD\"}" \
  -w "\n%{http_code}")

HTTP_CODE=$(echo "$LOGIN_RESP" | tail -1)
LOGIN_BODY=$(echo "$LOGIN_RESP" | sed '$d')

if [ "$HTTP_CODE" != "200" ]; then
  echo "로그인 실패 (HTTP $HTTP_CODE). 계정 정보를 확인하세요."
  echo "$LOGIN_BODY"
  rm -f "$COOKIE_JAR"
  exit 1
fi
echo "로그인 성공!"

# 2) CasePack 생성 (REST API)
echo "[2/3] CasePack 등록 중..."

RESPONSE=$(curl -s -b "$COOKIE_JAR" -X POST "$HUB_URL/api/v1/casepacks/" \
  -H "Content-Type: application/json" \
  -d '{
  "title": "Conference Summarizer MCP (개발 컨퍼런스/트렌딩 자동 요약)",
  "summary": "Google I/O, Flutter, Apple WWDC 등 주요 개발 컨퍼런스의 새 콘텐츠와 GitHub/Hacker News/GeekNews 트렌딩을 매일 자동 감지하고, Claude Code 헤드리스 모드로 한국어 요약을 생성해 파일/Teams로 배포하는 MCP 서버입니다.",
  "platform": "CrossPlatform",
  "problem_statement": "개발 트렌드를 따라가려면 매일 여러 YouTube 채널, 블로그 RSS, GitHub Trending, Hacker News 등을 일일이 확인해야 합니다. 영상은 시간이 걸리고, 영어 콘텐츠는 핵심만 빠르게 파악하기 어렵습니다. 컨퍼런스 시즌에는 세션이 한꺼번에 쏟아져 따라잡기가 더 힘듭니다.",
  "solution_approach": "MCP 서버로 9개 도구(check_new_content, get_trending, extract_url_content, save_summary_text 등)를 제공하고, cron이 매일 새 콘텐츠를 감지한 뒤 헤드리스 Claude Code(/add-link 슬래시 커맨드)로 한국어 요약을 자동 생성합니다. YouTube 자막은 Transcript API → Whisper 폴백으로 100% 커버, 결과는 Markdown 파일 저장 + Teams 카드 게시 + GitHub 자동 푸시까지 자동화합니다.",
  "tags": ["MCP", "conference", "summarization", "youtube", "whisper", "claude-code", "trending", "cron", "teams-webhook"],
  "keywords": ["컨퍼런스", "요약", "트렌딩", "GoogleIO", "WWDC", "Flutter", "GitHub Trending", "HackerNews", "GeekNews", "Whisper", "YouTube"],
  "author": "haeihn.lee",
  "team": "SW Platform",
  "guide_document": "# Conference Summarizer MCP 셋업 가이드\n\n## 개요\n\n개발 컨퍼런스의 새 콘텐츠와 트렌딩 글을 자동으로 감지하고, Claude Code로 한국어 요약을 생성해 파일·Teams·GitHub에 배포하는 MCP 서버입니다.\n\n### 제공 도구 (9개)\n\n| 도구 | 설명 |\n|---|---|\n| `check_new_content` | 모니터링 중인 모든 컨퍼런스에서 최근 N일간 새 콘텐츠 감지 |\n| `get_trending` | GitHub Trending / Hacker News / Dev.to / Reddit / GeekNews 인기글 조회 |\n| `extract_url_content` | YouTube 자막(Transcript API → Whisper 폴백) 또는 웹페이지 본문 추출 |\n| `save_summary_text` | Claude가 작성한 한국어 요약 마크다운을 파일로 저장 |\n| `list_conferences` | 현재 모니터링 중인 컨퍼런스 목록 |\n| `add_conference` | 모니터링할 컨퍼런스 추가 (YouTube 채널, RSS, 웹사이트) |\n| `remove_conference` | 모니터링 목록에서 컨퍼런스 제거 |\n| `get_summaries` | 저장된 요약 파일 목록 조회 |\n| `read_summary` | 저장된 요약 파일 내용 읽기 |\n\n---\n\n## 1. 클라이언트 설정 (Claude Code 사용자용)\n\n로컬에서 stdio 방식으로 실행합니다.\n\n### CLI 명령어\n\n```bash\nclaude mcp add -s user conference-summarizer \\\n  /path/to/conference-mcp/.venv/bin/python \\\n  /path/to/conference-mcp/server.py\n```\n\n### 설정 파일 직접 편집 (`~/.mcp.json`)\n\n```json\n{\n  \"mcpServers\": {\n    \"conference-summarizer\": {\n      \"command\": \"/path/to/conference-mcp/.venv/bin/python\",\n      \"args\": [\"/path/to/conference-mcp/server.py\"]\n    }\n  }\n}\n```\n\n### 연결 확인\n\n```\n/mcp\n```\n\n정상 시 `conference-summarizer: connected` 표시.\n\n---\n\n## 2. 서버 셋업 (관리자용)\n\n### 사전 요구사항\n\n- Python 3.10+\n- ffmpeg (Whisper 폴백용)\n- YouTube Data API v3 키\n- (선택) Teams 인커밍 웹훅 URL\n\n### 설치\n\n```bash\n# 1) 클론\ngit clone git@github.com:haeihnlee/techRaderMCP.git conference-mcp\ncd conference-mcp\n\n# 2) 가상환경 + 의존성\npython3 -m venv .venv\nsource .venv/bin/activate\npip install -r requirements.txt\n\n# 3) 환경변수 (.env)\ncat > .env <<EOF\nYOUTUBE_API_KEY=YOUR_KEY_HERE\nTEAMS_WEBHOOK_URL=YOUR_WEBHOOK_HERE\nEOF\n```\n\n### 모니터링 대상 등록 (`config.json`)\n\n```json\n{\n  \"conferences\": [\n    {\n      \"name\": \"Google I/O\",\n      \"youtube_channels\": [\"UCVHFbw7woebKtXIlUlFpyxRw\"],\n      \"rss_feeds\": [],\n      \"websites\": [\"https://io.google/\"]\n    }\n  ]\n}\n```\n\n또는 Claude Code에서 자연어로:\n- \"Flutter 컨퍼런스 추가해줘. YouTube 채널은 UCwXdFgeE9KYzlDdR7TG9cMw\"\n\n### 일일 자동 실행 (cron)\n\n```bash\ncrontab -e\n# 매일 오전 9시\n0 9 * * * /path/to/conference-mcp/run_check.sh\n```\n\n`run_check.sh` 동작:\n1. `check_new_content(days=1)` + `get_trending()` 으로 새 항목 감지\n2. 항목별로 헤드리스 Claude Code 실행 → `/add-link <URL>` 슬래시 커맨드가 자동 요약 생성\n3. `notify.py` 가 Teams에 다이제스트 + 개별 요약 카드 게시\n4. 새 요약 파일을 git commit + push\n\n---\n\n## 3. 사용법\n\n### Claude Code에서 자연어 질의\n\n- \"지난 7일간 새로 올라온 컨퍼런스 영상 보여줘\"\n- \"GitHub 트렌딩 10개 알려줘\"\n- \"이 YouTube 링크 요약해줘: https://...\"\n- \"저장된 Flutter 요약 목록 보여줘\"\n\n### 슬래시 커맨드 (`.claude/commands/`)\n\n- `/add-link <URL> [컨퍼런스명]` — URL 추출 → 한국어 요약 → 저장\n- `/news-list` — 저장된 요약 전체 목록\n- `/add-subscription` — 새 모니터링 대상 등록\n\n---\n\n## 4. 요약 산출물 구조\n\n```\nsummaries/\n├── Google I_O/\n│   └── 20260513_144530_session-title.md\n├── Flutter/\n│   └── 20260512_091200_widget-of-the-week.md\n└── 기타/\n    └── 20260511_180000_hn-trending-post.md\n```\n\n각 파일 형식:\n```markdown\n## 🔑 핵심 요약\n## 📌 주요 내용\n## 💡 인사이트\n## 🔗 참고\n```\n\n---\n\n## 5. 트러블슈팅\n\n| 증상 | 해결 방법 |\n|---|---|\n| YouTube 자막 없음 | Whisper 폴백 자동 동작 — ffmpeg 설치 확인 (`which ffmpeg`) |\n| `YOUTUBE_API_KEY` 누락 | `.env` 파일에 키 추가 후 cron 재실행 |\n| Teams 카드 미수신 | `TEAMS_WEBHOOK_URL` 확인, `notify.py` 단독 실행으로 디버그 |\n| cron에서 claude CLI 못 찾음 | `run_check.sh` 의 `CLAUDE_BIN` 경로 확인 |\n| 사내 프록시 인증서 오류 | `ca-bundle.pem` 배치 후 `NODE_EXTRA_CA_CERTS` 설정 |",
  "git_references": [
    {
      "repo_url": "git@github.com:haeihnlee/techRaderMCP.git",
      "branch": "main"
    }
  ]
}')

echo "$RESPONSE" | python3 -m json.tool 2>/dev/null || echo "$RESPONSE"

# 3) 결과 확인
CASE_ID=$(echo "$RESPONSE" | python3 -c "import sys,json; print(json.load(sys.stdin).get('data',{}).get('case_id',''))" 2>/dev/null)

if [ -n "$CASE_ID" ]; then
  echo ""
  echo "[3/3] 등록 완료!"
  echo "  CasePack ID: $CASE_ID"
  echo "  URL: $HUB_URL/casepacks/$CASE_ID"
else
  echo ""
  echo "[3/3] 등록 결과를 확인하세요."
fi

rm -f "$COOKIE_JAR"

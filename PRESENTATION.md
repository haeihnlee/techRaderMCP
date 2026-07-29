# Conference Summarizer MCP

> 개발자 컨퍼런스 새 영상·포스트를 자동 감지해서 한국어로 요약해주는 MCP 서버.

---

## 1. 동기

- 매년 Google I/O, Flutter Forward, Apple WWDC, Google Cloud Next 같은 컨퍼런스가 쏟아지지만 **다 챙겨 보기 어려움**.
- 영어 자막을 일일이 읽고 정리하는 데 시간 소모가 큼.
- 트렌딩 사이트(GitHub Trending, Hacker News, GeekNews 등)도 매일 챙기기 번거로움.

→ **Claude Code에 슬래시 커맨드 하나 치면 끝.** 추출·요약·저장까지 자동화.

---

## 2. 전체 아키텍처

```
┌─────────────────────────────────────────────────────────────────┐
│                      Claude Code (사용자)                         │
│                            │                                     │
│                  /add-link, /get-trending,                       │
│                  /add-subscription, /news-list                   │
│                            │                                     │
│                            ▼                                     │
│             ┌───────────────────────────────┐                   │
│             │  Conference Summarizer MCP    │                   │
│             │      (server.py / FastMCP)    │                   │
│             └────────┬──────────────────────┘                   │
│                      │                                          │
│   ┌──────────────────┼──────────────────┐                       │
│   ▼                  ▼                  ▼                       │
│ YouTube           RSS 피드           웹페이지                    │
│ (자막 + Whisper)   (feedparser)      (BeautifulSoup)             │
│   │                  │                  │                       │
│   └──────────────────┼──────────────────┘                       │
│                      ▼                                          │
│              raw 본문 텍스트                                     │
│                      │                                          │
│                      ▼                                          │
│        Claude (Code 또는 헤드리스)                              │
│              한국어 요약 작성                                    │
│                      │                                          │
│                      ▼                                          │
│     summaries/<conference>/<timestamp>_<title>.md               │
└─────────────────────────────────────────────────────────────────┘
```

**핵심 디자인:** 추출은 MCP, 요약은 Claude. 책임 분리.

---

## 3. 핵심 컴포넌트

| 파일 | 역할 |
|---|---|
| `server.py` | MCP 서버 (FastMCP). 도구 9개 노출 |
| `.claude/commands/*.md` | 슬래시 커맨드 정의 (4개) |
| `config.json` | 구독 컨퍼런스 목록 (YouTube 채널 / RSS / 웹사이트) |
| `summaries/<conference>/` | 자동 생성된 한국어 요약 마크다운 |
| `requirements.txt` | Python 의존성 |
| `.env.example` | 필요 환경변수 템플릿 |

---

## 4. 현재 모니터링 중인 컨퍼런스

`config.json`에 등록된 6개 소스. cron 자동 감지 + `/add-subscription`으로 추가/제거 가능.

| 컨퍼런스 | YouTube 채널 | RSS 피드 | 웹사이트 |
|---|---|---|---|
| **Google I/O** | Google for Developers | — | https://io.google/ |
| **Flutter** | Flutter | Medium 블로그 | — |
| **Apple WWDC** | — | Apple Developer Releases | https://developer.apple.com/wwdc/ |
| **Apple TV** | Apple TV+ 공식 채널 | — | — |
| **Google Cloud Next** | Google Cloud Tech | — | — |
| **Android** | Google for Developers | Android Developers Blog | — |

소스 종류:
- **YouTube 채널**: 매일 새 영상 업로드 감지 (자막 추출 → 한국어 요약)
- **RSS 피드**: 새 포스트 감지 (본문 → 한국어 요약)
- **웹사이트**: 기준 페이지 변경 감지 (현재는 메타 정보 위주)

추가 가능한 다른 예시: PyCon Korea, JSConf, KubeCon, AWS re:Invent, Rust Conf, Vue.js Conf 등 — `/add-subscription`으로 즉시 등록.

---

## 5. 사용 가능한 Skills (Slash Commands)

Claude Code에서 바로 호출할 수 있는 4개의 슬래시 커맨드.

### 4.1 `/add-link <URL> [컨퍼런스명]`

링크 하나로 추출 → 한국어 요약 → 파일 저장.

```
/add-link https://www.youtube.com/watch?v=xxxxx Flutter
/add-link https://blog.example.com/post
/add-link https://youtu.be/abc PyCon Korea
```

**처리 단계:**
1. URL 파싱 (컨퍼런스명 생략 시 "기타")
2. `extract_url_content` 도구로 자막/본문 추출 (12000자 절단)
3. Claude가 한국어 요약 작성 (4섹션: 핵심 요약 / 주요 발표 / 개발자 포인트 / 버전·일정)
4. `save_summary_text` 도구로 파일 저장
5. (선택) git add/commit/push로 GitHub 동기화

### 4.2 `/get-trending [소스] [개수]`

GitHub Trending, Hacker News, Dev.to, GeekNews(news.hada.io), Reddit에서 인기글 한 번에 조회.

```
/get-trending                                      # 기본 (4개 소스, 각 10개)
/get-trending github,hackernews,devto,reddit       # Reddit 포함
/get-trending geeknews 5                           # GeekNews만 5개
```

각 항목에 짧은 설명·태그·언어 정보 포함.

### 4.3 `/add-subscription <이름> <URL1> [URL2] ...`

새로운 컨퍼런스/소스를 모니터링 목록에 추가. URL 종류(YouTube 채널 / RSS / 웹사이트)를 자동 분류.

```
/add-subscription "PyCon Korea" https://www.youtube.com/@PyConKR
/add-subscription "Rust Blog" https://blog.rust-lang.org/feed.xml
/add-subscription "AWS reInvent" https://www.youtube.com/channel/UCxxx https://aws.amazon.com/blogs/feed/
```

YouTube `@핸들`은 Data API로 채널 ID 자동 변환.

### 4.4 `/news-list`

저장된 요약 마크다운들을 컨퍼런스별로 그룹핑해서 보여줌.

```
## 저장된 요약 목록

**Flutter**
1. Full-stack Dart: Cloud Functions for Firebase — 2026-05-06
   `flutter/20260506_150059_Full-stack_Dart_Cloud_Functions_for_Firebase__Flutter_Demo.md`
...
```

---

## 6. MCP 도구 (Tools)

`server.py`가 `@mcp.tool()` 데코레이터로 노출하는 9개 도구. 슬래시 커맨드 내부에서 호출되거나, 직접 호출도 가능.

| 도구 | 입력 | 역할 |
|---|---|---|
| `extract_url_content` | url, conference_name | YouTube/웹페이지에서 raw 본문 추출 (12000자 절단) |
| `save_summary_text` | conference, title, source_url, summary_md | 미리 작성된 요약 마크다운을 파일로 저장 |
| `check_new_content` | days | 구독 컨퍼런스에서 최근 N일 새 콘텐츠 감지 |
| `get_trending` | sources, limit | GitHub/HN/Dev.to/GeekNews/Reddit 트렌딩 |
| `add_conference` | name, channels, rss, websites | 구독 목록에 새 컨퍼런스 추가 |
| `remove_conference` | name | 구독 제거 |
| `list_conferences` | — | 현재 구독 목록 |
| `get_summaries` | conference, limit | 저장된 요약 파일 목록 |
| `read_summary` | file_path | 특정 요약 파일 읽기 |

---

## 7. Whisper / 자막 추출 파이프라인

YouTube는 영상마다 자막 사정이 달라서 **2단계 폴백 구조**.

```
get_youtube_transcript(video_id):

  ① YouTubeTranscriptApi
     ├─ ko / en / en-US 수동 자막 시도
     └─ 자동 생성 자막 시도
        │
        │  (모두 실패하면)
        ▼
  ② Whisper 폴백
     yt-dlp로 오디오만 다운로드(.mp3, 64kbps)
     → whisper("base") 모델로 음성 → 텍스트
```

### Whisper 따로 설치해야 하나?

**아니요. `pip install -r requirements.txt` 한 번이면 끝.**

| 의존성 | 설치 방법 | 크기 | 비고 |
|---|---|---|---|
| `openai-whisper` | `pip install` (requirements.txt) | venv 5GB (torch 포함) | 격리 설치 |
| `ffmpeg` 바이너리 | `imageio-ffmpeg`가 패키지에 동봉 | ~80MB | **시스템 ffmpeg 설치 불필요** |
| Whisper 모델(`base.pt`) | 첫 실행 시 자동 다운로드 | ~139MB | `~/.cache/whisper/`에 캐시 |

`base` 모델은 CPU에서도 동작. 실제로는 1단계(YouTube Transcript API)에서 90%+ 처리되고 Whisper 폴백은 비상용.

| 환경 | 60분 영상 transcribe |
|---|---|
| GPU (CUDA) | 3-5분 |
| CPU only | 30-60분 |
| 공식 자막 있음 | 즉시 |

---

## 8. 설치 가이드

### 8.1 환경 준비

```bash
git clone <repo>
cd conference-mcp
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 8.2 환경변수 (`.env`)

`.env.example`을 `.env`로 복사하고 채우기.

```bash
ANTHROPIC_API_KEY=sk-ant-...    # Claude API 키 (slash 커맨드용)
YOUTUBE_API_KEY=AIza...         # YouTube Data API v3 키 (채널 새 영상 감지용)
```

### 8.3 Claude Code MCP 등록

`~/.claude.json` 또는 프로젝트 루트의 `.mcp.json`:

```json
{
  "mcpServers": {
    "conference-summarizer": {
      "command": "/path/to/conference-mcp/.venv/bin/python",
      "args": ["/path/to/conference-mcp/server.py"]
    }
  }
}
```

Claude Code 재시작 → 슬래시 커맨드와 9개 MCP 도구 즉시 사용 가능.

### 8.4 본인 저장소 연결 (요약을 쌓을 곳)

`/add-link` 는 요약을 저장한 뒤 **`origin` 으로 자동 커밋·푸시**합니다.
푸시 대상은 저장소의 `origin` 과 현재 브랜치를 그대로 쓰므로, 각자 본인 공간을
연결하면 요약이 개인 저장소에 쌓입니다.

**방법 1 — fork 후 clone** (원본 업데이트를 받아오기 쉬움)

```bash
# GitHub / mod.lge.com 웹에서 fork 후
git clone <본인 fork URL> conference-mcp
cd conference-mcp
git remote add upstream <원본 URL>   # 원본 업데이트 받을 때: git pull upstream main
```

**방법 2 — 빈 저장소 새로 만들어 연결**

```bash
cd conference-mcp
git remote remove origin              # 원본을 가리키던 origin 제거
git remote add origin <본인 저장소 URL>
git push -u origin main
```

> **확인**: `git remote -v` 의 `origin` 이 본인 저장소여야 합니다.
> 원본을 그대로 가리키면 푸시가 권한 오류로 거부됩니다.

`origin` 을 설정하지 않아도 요약은 **로컬에 정상 저장**됩니다 —
푸시만 건너뛰고 안내 메시지가 나옵니다.

### 8.5 테스트

표준 라이브러리만 쓰므로 추가 설치 없이 실행됩니다. 네트워크에 접속하지 않습니다.

```bash
.venv/bin/python -m unittest test_server -v
```

본문 유효성 검사(`_detect_unusable_content`)의 회귀 테스트 16건이 들어 있습니다.
임계값(웹페이지 400자 / YouTube 120자, 고유줄 3개)을 조정할 때 기존 케이스가
깨지지 않는지 확인하는 용도입니다.

---

## 9. 사용 예시 (데모 흐름)

### 시나리오 A: 새 영상 보고 요약

```
> /add-link https://www.youtube.com/watch?v=CRszhkEjd8s "Google Cloud Next"
```

→ 60초 후 `summaries/google_cloud_next/<ts>_Google_Cloud_Live_MCP_Toolbox.md` 생성.
→ 4섹션 한국어 요약 + 메타정보(컨퍼런스/출처/요약 일시) 포함.

### 시나리오 B: 매일 아침 트렌딩 체크

```
> /get-trending
```

→ GitHub Trending 10개 + HN Top 10 + Dev.to 7일 트렌딩 + GeekNews 10개를 한 번에 마크다운으로 받음. 각 항목에 짧은 설명까지.

### 시나리오 C: 새 컨퍼런스 추가

```
> /add-subscription "JSConf Korea" https://www.youtube.com/@JSConfKorea
```

→ YouTube 핸들을 채널 ID로 변환해서 `config.json`에 등록. 이후 `check_new_content` 호출 시 자동 감지.

### 시나리오 D: 그동안 모은 요약 한눈에

```
> /news-list
```

→ 컨퍼런스별 그룹핑된 목록과 총 개수.

---

## 10. 디자인 특징

1. **추출과 요약의 책임 분리**
   MCP는 raw 본문만 제공. 요약 작성은 호출 측 Claude가 수행.
   → 모델 변경, 프롬프트 수정, 요약 형식 변경이 코드 변경 없이 가능.

2. **공식 자막 우선, Whisper는 폴백**
   비용·시간 최소화. GPU 없어도 동작.

3. **번들된 ffmpeg**
   `imageio-ffmpeg`로 시스템 의존성 0. apt/brew install 필요 없음.

4. **슬래시 커맨드 = 마크다운 텍스트**
   워크플로 수정이 코드 빌드 없이 텍스트 편집으로 끝남. 새 워크플로 추가도 간단.

5. **MCP 표준 따름**
   Claude Code뿐 아니라 Claude Desktop, Cursor 등 MCP 호환 어디든 등록 가능.

---

## 11. 한계 / 알려진 이슈

| 이슈 | 비고 |
|---|---|
| JS 동적 렌더링 페이지 | SPA(예: Apple Developer 일부)는 본문 추출이 부실 — 메타정보만 들어올 수 있음 |
| Whisper CPU 추론 속도 | GPU 없으면 긴 영상은 느림. 공식 자막 있으면 무관 |
| 12000자 본문 절단 | 매우 긴 콘텐츠는 일부만 요약에 반영 |
| 헤드리스 Claude의 git 권한 | 인터랙티브에선 가능, 헤드리스 자동화에선 권한 거부될 수 있음 |

---

## 12. 파일 구조 (공유 repo 기준)

```
conference-mcp/
├── server.py                  # MCP 서버 (FastMCP, 도구 9개)
├── config.json                # 컨퍼런스 구독 목록
├── requirements.txt
├── .env.example
├── .gitignore
├── .claude/commands/          # 슬래시 커맨드 정의
│   ├── add-link.md
│   ├── add-subscription.md
│   ├── get-trending.md
│   └── news-list.md
└── summaries/                 # 자동 생성된 요약 (예시 데이터)
    ├── flutter/
    ├── apple_wwdc/
    ├── google_cloud_next/
    ├── google_i_o/
    ├── android/
    ├── apple_tv/
    └── 기타/
```

---

## 13. 확장 아이디어

- 📊 누적 요약 통계 대시보드 (Streamlit)
- 🔔 채팅앱 푸시(Slack/Discord/Teams 등 — 사용자가 직접 webhook 연결)
- 🌐 다국어 요약 (영어·일본어 옵션)
- 🎯 키워드 필터링 (관심 분야만 자동 요약)
- 🤝 팀 공유용 GitHub Pages 배포

---

## 부록 A. 의존성 라이브러리

```
mcp[cli]>=1.0.0           # MCP 프로토콜
anthropic>=0.40.0         # Claude API (선택, 직접 사용 시)
google-api-python-client  # YouTube Data API v3
youtube-transcript-api    # 자막 1차 시도
feedparser                # RSS 파싱
httpx                     # HTTP 클라이언트
beautifulsoup4            # HTML 파싱
yt-dlp                    # YouTube 오디오 다운로드 (Whisper 폴백용)
openai-whisper            # 음성 → 텍스트
imageio-ffmpeg            # ffmpeg 바이너리 동봉
python-dotenv             # .env 로딩
```

## 부록 B. 환경변수

| 이름 | 용도 | 필수 여부 |
|---|---|---|
| `ANTHROPIC_API_KEY` | Claude API (`/add-link` 슬래시 커맨드 내부에서 모델 호출용) | 필수 |
| `YOUTUBE_API_KEY` | 채널 새 영상 감지 (`check_new_content`) | 권장 |

---

## 발표 시 강조 포인트

1. **"Claude Code에 슬래시 한 번"이라는 단순함** — 복잡한 파이프라인이 아닌 자연어 워크플로
2. **추출(MCP) ↔ 요약(Claude) 책임 분리** — 확장성·유지보수
3. **시스템 의존성 0** — pip install 한 번으로 whisper + ffmpeg 모두
4. **MCP 표준** — Claude 생태계 어디서든 등록해서 사용

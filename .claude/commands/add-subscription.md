모니터링할 새 구독을 추가합니다. 새 콘텐츠가 생길 때마다 run_check.sh 크론잡이 자동으로 감지·요약·알림합니다.

Arguments: $ARGUMENTS
(형식: `<이름> <URL1> [URL2] ...`)

다음 단계로 처리하세요:

## 1. 인자 파싱

$ARGUMENTS를 파싱합니다:
- 첫 번째 토큰: 구독 이름 (예: "PyCon Korea", "Rust Conf")
- 나머지 토큰들: URL 목록

$ARGUMENTS가 비어있으면 아래 안내 출력 후 종료:
```
사용법: /add-subscription <이름> <URL> [URL2] ...

URL 종류별 예시:
  YouTube 채널:  https://www.youtube.com/@GoogleDevelopers
                 https://www.youtube.com/channel/UCVHFbw7woebKtXIlUlFpyxRw
  RSS 피드:      https://feeds.example.com/rss
                 https://medium.com/feed/flutter
  웹사이트:      https://io.google/
```

## 2. URL 분류

각 URL을 분석해서 종류를 판별합니다:

**YouTube 채널 판별:**
- URL에 `youtube.com/channel/` 포함 → `channel/` 뒤의 ID 추출 (예: `UCVHFbw7woebKtXIlUlFpyxRw`)
- URL에 `youtube.com/@` 포함 → YouTube Data API로 핸들 → 채널 ID 변환 필요
  - Bash 실행: `cd /home/haen/conference-mcp && source .env 2>/dev/null; .venv/bin/python -c "
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
load_dotenv()
yt = build('youtube', 'v3', developerKey=os.environ['YOUTUBE_API_KEY'])
handle = '<핸들명>'  # @ 제거
res = yt.channels().list(part='id', forHandle=handle).execute()
print(res['items'][0]['id'] if res.get('items') else 'NOT_FOUND')
"`
- 그냥 채널 ID처럼 생긴 문자열 (`UC`로 시작하는 24자) → 그대로 사용

**RSS 피드 판별:**
- URL 경로에 `/feed`, `/rss`, `/atom`, `feeds.`, `.xml` 포함 → RSS로 분류

**웹사이트 판별:**
- 위 두 가지에 해당 없으면 웹사이트로 분류

## 3. add_conference 호출

`mcp__conference-summarizer__add_conference` 도구를 호출합니다:
- name: 구독 이름
- youtube_channel_ids: 분류된 채널 ID들 (쉼표 구분)
- rss_feeds: 분류된 RSS URL들 (쉼표 구분)
- websites: 분류된 웹사이트 URL들 (쉼표 구분)

## 4. 결과 출력

성공 시:
```
✅ 구독 추가 완료!

이름: <이름>
YouTube 채널: <채널 ID들 또는 없음>
RSS 피드: <URL들 또는 없음>
웹사이트: <URL들 또는 없음>

매일 오전 9시 크론잡(run_check.sh)이 새 콘텐츠를 자동으로 체크합니다.
지금 바로 확인하려면: mcp__conference-summarizer__check_new_content 도구 사용
```

## 사용 예시

```
/add-subscription "PyCon Korea" https://www.youtube.com/@PyConKR
/add-subscription "Rust Blog" https://blog.rust-lang.org/feed.xml
/add-subscription "AWS re:Invent" https://www.youtube.com/channel/UCd6MoB9NC6JDt4oP2RdnFJQ https://aws.amazon.com/blogs/aws/feed/
```

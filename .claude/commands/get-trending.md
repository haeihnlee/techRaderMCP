개발 트렌딩 콘텐츠를 가져옵니다. GitHub Trending, Hacker News, Dev.to, Reddit, GeekNews(news.hada.io) 인기글을 조회합니다.

Arguments: $ARGUMENTS
(형식: 없음 또는 `<소스>` 또는 `<소스> <개수>`)
- 소스 예시: `github,hackernews,devto,geeknews` (기본값) 또는 `github,hackernews,devto,reddit,geeknews`
- 개수: 소스별 최대 항목 수 (기본값: 10)

다음 단계로 처리하세요:

1. $ARGUMENTS 파싱:
   - 비어있으면: sources="github,hackernews,devto,geeknews", limit=10
   - 첫 토큰이 쉼표 포함 or 알려진 소스명이면 sources로 사용
   - 숫자 토큰이 있으면 limit으로 사용

2. `mcp__conference-summarizer__get_trending` 도구를 호출합니다:
   - sources: 파싱한 소스 (기본값: "github,hackernews,devto,geeknews")
   - limit: 파싱한 개수 (기본값: 10)

3. 결과를 그대로 출력합니다.

사용 예시:
- `/get-trending` — 기본 (GitHub + HN + Dev.to + GeekNews, 각 10개)
- `/get-trending github,hackernews,devto,reddit,geeknews` — Reddit 포함
- `/get-trending geeknews 5` — GeekNews만 5개

요약할 링크를 받아서 저장합니다.

Arguments: $ARGUMENTS
(형식: `<URL>` 또는 `<URL> <컨퍼런스명>`)

다음 단계로 처리하세요:

1. $ARGUMENTS에서 URL과 컨퍼런스명을 파싱합니다.
   - 첫 번째 토큰이 URL (http:// 또는 https://로 시작)
   - 두 번째 토큰 이후가 있으면 컨퍼런스명 (없으면 "기타" 사용)
   - $ARGUMENTS가 비어있으면 "URL을 입력해주세요. 예: `/add-link https://example.com [컨퍼런스명]`" 출력 후 종료

2. `mcp__conference-summarizer__summarize_url` 도구를 호출합니다.
   - url: 파싱한 URL
   - conference_name: 파싱한 컨퍼런스명 (또는 "기타")
   - save: true

3. 결과를 출력합니다.
   - 성공 시: "✅ 요약 완료!" + 저장된 파일 경로
   - 실패 시: "❌ 요약 실패: " + 오류 내용

사용 예시:
- `/add-link https://www.youtube.com/watch?v=xxxxx Google I/O`
- `/add-link https://blog.example.com/post`

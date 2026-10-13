run_check.sh 의 헤드리스 요약 전용 프롬프트입니다. `/add-link` 의 1~4단계와 같고,
git commit·push 는 run_check.sh 4단계가 대신하므로 여기서는 하지 않습니다
(Bash 등 내장 도구를 끄고 MCP 도구 2개만 써서 토큰을 줄이기 위함).

인자는 이 프롬프트 맨 끝 `Arguments:` 줄에 있습니다 (형식: `<URL> <컨퍼런스명>`).

다음 단계로 처리하세요:

## 1. 인자 파싱

- 첫 번째 토큰이 URL, 두 번째 토큰 이후가 컨퍼런스명 (없으면 "기타")

## 2. 콘텐츠 추출

`mcp__conference-summarizer__extract_url_content` 를 호출합니다 (url, conference_name).
응답의 `## 메타` 에서 title, source_url, conference_name 을 파싱합니다.
응답이 "오류:" 또는 "콘텐츠를 가져올 수 없습니다"로 시작하면 그 메시지를 그대로 출력하고 종료합니다.

## 3. 한국어 요약 작성

추출된 본문을 개발자 관점에서 한국어로 요약합니다. **아래 섹션 헤딩을 정확히 그대로** 사용하세요
(Teams 알림 파서가 이 섹션명을 파싱하므로 변경 금지).

- API명·클래스명·플래그·명령어는 `backtick`, 중요 키워드는 **굵게**
- Breaking Change·주의사항은 > 인용문 블록
- 버전/날짜/수치가 여러 개면 표로 정리
- bullet 은 한 줄에 한 가지, 섹션 사이 구분선(---)

```
## 🔑 핵심 요약
- (핵심 내용 1)
- (핵심 내용 2)
- (핵심 내용 3)

---

## 📣 주요 발표 내용
(신기능·변경사항 bullet)

---

## 💡 개발자 포인트
(실제 개발에 영향 주는 내용)

---

## 📅 버전 / 출시 일정
(표, 없으면 "해당 없음")
```

## 4. 파일로 저장

`mcp__conference-summarizer__save_summary_text` 를 호출합니다
(conference_name, title, source_url, summary_markdown).

## 5. 결과 출력

요약 본문은 다시 출력하지 말고 한 줄만 출력하세요:
- 성공: `✅ 요약 완료: <save_summary_text 가 반환한 절대 경로>`
- 실패: `❌ 요약 실패: <오류 내용>`

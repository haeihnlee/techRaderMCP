요약할 링크를 받아서 콘텐츠를 추출하고, Claude가 직접 한국어 요약을 작성한 뒤 파일로 저장합니다.

Arguments: $ARGUMENTS
(형식: `<URL>` 또는 `<URL> <컨퍼런스명>`)

다음 단계로 처리하세요:

## 1. 인자 파싱

$ARGUMENTS에서 URL과 컨퍼런스명을 파싱합니다.
- 첫 번째 토큰이 URL (http:// 또는 https://로 시작)
- 두 번째 토큰 이후가 있으면 컨퍼런스명 (없으면 "기타" 사용)
- $ARGUMENTS가 비어있으면 "URL을 입력해주세요. 예: `/add-link https://example.com [컨퍼런스명]`" 출력 후 종료

## 2. 콘텐츠 추출

`mcp__conference-summarizer__extract_url_content` 도구를 호출합니다.
- url: 파싱한 URL
- conference_name: 파싱한 컨퍼런스명 (또는 "기타")

도구가 반환하는 마크다운에서 다음 메타를 파싱합니다:
- title (영상/페이지 제목)
- source_url (원본 URL)
- conference_name
- type (youtube | webpage)

도구 응답이 "오류:" 또는 "콘텐츠를 가져올 수 없습니다"로 시작하면 ❌ 메시지로 종료합니다.

## 3. 한국어 요약 작성

추출된 본문을 개발자 관점에서 한국어로 요약합니다. **아래 형식·섹션 헤딩을 정확히 그대로** 사용하세요 (Teams 알림 파서가 이 섹션명을 파싱하므로 변경 금지).

**작성 규칙 (가독성 최우선):**
- API명·클래스명·플래그·명령어는 반드시 `backtick` 코드 포맷으로 표기
- 중요 키워드·기술명은 **굵게** 강조
- 특히 중요한 주의사항이나 Breaking Change는 > 인용문 블록으로 강조
- 버전/날짜/수치 정보가 여러 개면 표(table)로 정리
- bullet point는 핵심만, 한 줄에 한 가지 내용만 담을 것
- 각 섹션 사이 구분선(---) 삽입

요약 형식:

```
## 🔑 핵심 요약
- (핵심 내용 1)
- (핵심 내용 2)
- (핵심 내용 3)

---

## 📣 주요 발표 내용
(신기능·변경사항을 bullet로 정리. 기술명은 `코드` 또는 **굵게**)

---

## 💡 개발자 포인트
(실제 개발에 영향 주는 내용. Breaking Change나 주의사항은 > 블록으로 강조)

---

## 📅 버전 / 출시 일정
(버전·날짜 정보가 있으면 표로, 없으면 "해당 없음")
```

## 4. 파일로 저장

`mcp__conference-summarizer__save_summary_text` 도구를 호출합니다.
- conference_name: 파싱한 컨퍼런스명
- title: 추출 단계에서 받은 title
- source_url: 추출 단계에서 받은 source_url
- summary_markdown: 위에서 작성한 요약 마크다운 (섹션 4개)

## 5. 결과 출력

성공 시:
```
✅ 요약 완료!
저장 위치: <save_summary_text가 반환한 경로>
```

실패 시:
```
❌ 요약 실패: <오류 내용>
```

## 사용 예시

- `/add-link https://www.youtube.com/watch?v=xxxxx Google I/O`
- `/add-link https://blog.example.com/post`
- `/add-link https://youtu.be/MWaWw6v6Rn4 PyCon Korea`

# The magic behind GenLatte: Flutter, Firebase, and Gemini

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=DHWiny5bjJc
- **요약 일시**: 2026-06-16 09:09:27

---

## 🔑 핵심 요약
- **Google Cloud Next 26**의 데모 앱 **GenLatte**: 사용자가 `Gemini`와 대화하며 만든 이미지를 실제 커피 위에 인쇄해주는 체험형 앱
- 기술 스택은 **Flutter**(UI) + **Firebase**(백엔드) + **Gemini**(AI), 이미지 생성은 **Nano Banana** 모델 담당
- 핵심 패러다임은 **GenUI(Agent-to-UI)** — AI가 콘텐츠 생성과 동시에 UI를 **온디맨드로 조립**해 개인화 경험을 제공

---

## 📣 주요 발표 내용
- 사용자가 "내 happy place"를 입력하면 **Nano Banana**가 여러 후보 이미지를 생성
- 이미지 선택 후 `tweak`(보정) 기능으로 취향에 맞게 커스터마이징 가능
- 이때 **Gemini**가 콘텐츠를 만들고, UI 요소를 **실시간으로 stitching(조립)** 하여 화면 구성
- 최종 선택한 이미지를 **커피 프린터**로 전송해 라떼 아트로 인쇄 (데모에서는 "용이 떠다니는 라스베이거스" 이미지)
- **agentic development / agentic features**를 앱에 결합한 2026년형 앱 개발 방향성 제시

---

## 💡 개발자 포인트
- **GenUI(Agent-to-UI)** 패턴이 핵심: 정적으로 설계된 화면 대신 **AI가 런타임에 UI를 생성·조립**하는 방식
- `Flutter` + `Firebase` + `Gemini` 조합으로 풀스택 생성형 앱을 빠르게 구성하는 레퍼런스 사례

> 기존에는 "디자이너가 미리 만든 화면"이 사용자 경험의 한계였다면, 이제는 **사용자의 상상력**이 한계 — UI 자체가 사용자에 맞춰 동적으로 생성됨

- 적용 가능 시나리오 예시:
  - **레스토랑**: 보유 재료로 다이너가 원하는 요리를 정밀 커스터마이징
  - **리테일**: 쇼퍼가 이미 가진 옷과 매장 상품을 매칭
- 단순 텍스트 생성형 AI를 넘어 **이미지 생성(Nano Banana) + 동적 UI + 물리적 출력(프린터)** 까지 연결한 멀티모달 파이프라인

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| 행사 | Google Cloud Next 26 |
| 데모 앱 | GenLatte |
| 핵심 기술 | Flutter, Firebase, Gemini, Nano Banana, GenUI |

> 구체적 SDK 버전·정식 출시일은 본 영상에서 언급되지 않음 (데모 성격)

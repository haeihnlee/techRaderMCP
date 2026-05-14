# Personalized lattes with Flutter, Gemini, GenUI | Demo

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=-NLK4gpT0m4
- **요약 일시**: 2026-05-14 09:03:44

---

## 🔑 핵심 요약
- **Flutter + Firebase + Gemini** 조합으로 만든 데모 앱 `Gen Latte` 소개 — 사용자가 Gemini와 대화하며 자신의 "happy place" 이미지를 생성해 라떼 위에 인쇄
- **GenUI(Generative UI)** 패러다임을 시연: Gemini가 단순히 응답만 하는 게 아니라 후속 질문을 동적으로 생성해 **UI 자체를 주도**
- 이미지 생성은 `Nano Banana`(Gemini 이미지 모델)를 활용해 1차 4장 → 사용자 응답 기반 후속 라운드로 정제하는 **반복 정제(refinement) 흐름**

---

## 📣 주요 발표 내용
- **앱 구성**: 사용자가 이름·우유 종류·"happy place"를 입력하면 Gemini가 4장의 후보 이미지 생성
- 선택된 이미지에 대해 Gemini가 **동적으로 사전 작성한 후속 질문** 제시 (예: "디지털 인터페이스 복잡도", "조명 톤", "등장할 새 종류", "디테일 수준")
- 사용자의 답변을 모아 **업데이트된 프롬프트**를 Gemini로 재전송 → 두 번째 라운드 이미지 생성
- 최종 선택 이미지가 바리스타에게 전달되어 **실제 라떼 아트로 인쇄**
- UI 흐름 전체가 `Flutter` 단일 코드베이스로 구현, 백엔드/AI 연동은 `Firebase`가 담당

---

## 💡 개발자 포인트
- **GenUI 패러다임**: 정적으로 짜둔 폼/위저드 대신 LLM이 **다음 단계 질문과 옵션을 런타임에 결정**해 UI를 생성 → Flutter 앱에서도 적용 가능한 새로운 UX 모델
- Flutter 앱에서 Gemini를 호출할 때 `Firebase AI Logic`(과거 Vertex AI in Firebase) 같은 SDK로 클라이언트→AI 직접 연결 흐름이 일반화되는 추세
- **이미지 정제 루프 설계**: 1차 결과 + 사용자 피드백 질문 → 2차 결과 패턴은 텍스트뿐 아니라 이미지 생성 워크플로에도 그대로 적용 가능

> **핵심 메시지**: "Gemini가 UI를 운전(drive)할 수 있게 하자" — 개발자가 모든 분기 UI를 직접 코딩하지 않고 모델에 위임하는 새로운 앱 설계 방식 제시

---

## 📅 버전 / 출시 일정
해당 없음 (컨셉 데모 영상으로 구체적 출시 일정·버전 정보 없음)


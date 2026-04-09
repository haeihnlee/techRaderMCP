# firebase_ai (Package of the Week)

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=tp7Ojf7dPVI
- **요약 일시**: 2026-04-08 16:01:33

---

## 🔑 핵심 요약
- `firebase_ai` 패키지는 Flutter 앱에서 **Gemini** 및 **Imagine API**에 직접 접근할 수 있는 올인원 서버리스 패키지
- 텍스트, 이미지, 영상, 오디오, 문서 등 **멀티모달 입력**을 지원하며 이미지 생성까지 가능
- **단일 턴(Single-turn)** 및 **멀티 턴(Multi-turn) 대화** 모두 지원

---

## 📣 주요 발표 내용

- 🔧 **시작 절차**
  - Firebase Console에서 프로젝트 생성 후 **Gemini Developer in Firebase AI Logic API** 활성화 필요
  - `firebase_core` 및 `firebase_ai` 패키지를 Flutter 프로젝트에 추가
  - `flutterfire configure` 명령어로 Flutter 앱과 Firebase 프로젝트 연결

- 🤖 **지원 모델 유형 3가지**

| 모델 타입 | 설명 |
|---|---|
| `GenerativeModel` | 텍스트 등 일반 콘텐츠 생성 |
| `LiveModel` | **Gemini Live API**를 통한 스트리밍 입출력 |
| `ImagineModel` | 이미지 생성 기능 접근 |

- 🖼️ **이미지 생성/편집**
  - `Gemini Flash Image Model` (코드명: **Nano Banana**) 사용
  - `GenerationConfig`에서 응답 타입을 **텍스트 + 이미지**로 지정 필요
  - 응답에서 `inlineData` 파트를 통해 이미지 데이터 추출

- 💬 **멀티 턴 대화(Chat)**
  - 동일한 모델 객체에서 `startChat()` 메서드 호출
  - `sendMessage()`로 메시지 전송 및 응답 파싱
  - **Firebase AI Logic**이 전체 대화 히스토리를 자동으로 관리

---

## 💡 개발자 포인트

- 프롬프트는 `Content` 객체 리스트로 구성하며, 텍스트 외에도 **이미지·비디오·오디오·문서** 포함 가능
- 단일 응답이 필요하면 `generateContent()` 메서드 사용
- 멀티 턴 대화가 필요하면 `startChat()` → `sendMessage()` 패턴 사용

> ⚠️ **이미지 생성 모델 사용 시**, 반드시 `GenerationConfig`를 통해 응답 타입(텍스트/이미지)을 명시적으로 지정해야 하며, 응답 파싱 방식이 일반 텍스트 모델과 **다름**에 주의

- 서버 없이 **Flutter 앱 클라이언트에서 직접 Gemini API 호출** 가능 → 백엔드 구축 비용 절감
- 자세한 정보는 `pub.dev`의 `firebase_ai` 패키지 페이지 참고

---

## 📅 버전 / 출시 일정

해당 없음 (영상 내 구체적인 버전 및 출시 일정 정보 없음)

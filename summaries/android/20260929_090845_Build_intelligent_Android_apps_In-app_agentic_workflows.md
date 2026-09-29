# Build intelligent Android apps: In-app agentic workflows

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/09/android-agentic-workflows.html
- **요약 일시**: 2026-09-29 09:08:45

---

## 🔑 핵심 요약
- **ADK(Agent Development Kit)** + **AG-UI** + **A2UI** 세 가지 프로토콜을 결합해 Android 앱 내 클라우드 기반 에이전틱 워크플로우를 구현하는 방법 소개
- 장기 실행 다단계 작업(예: 여행 예약)을 클라우드 백엔드 에이전트에 위임하고, Android 앱은 진행 상황 표시 및 사용자 입력만 담당
- `A2UI` 프로토콜로 서버가 UI 컴포넌트를 동적으로 기술해 앱 업데이트 없이 UI 변경 가능

---

## 📣 주요 발표 내용
- **ADK(Agent Development Kit)**: Python 기반 에이전트 정의 및 실행 프레임워크. `FunctionTool`로 커스텀 도구 등록, `InMemoryRunner`로 비동기 실행
- **AG-UI 프로토콜**: 에이전트-클라이언트 간 양방향 표준 통신 레이어. 서버는 SSE(Server-Sent Events)로 스트리밍, Android Kotlin SDK가 타입 세이프 이벤트(`TextMessageContentEvent` 등)로 자동 매핑
- **A2UI 프로토콜**: 서버가 JSON 페이로드로 렌더링할 UI 컴포넌트(카탈로그)와 속성을 동적으로 명세
- **Jetpack Compose A2UI Renderer** 신규 라이브러리 제공:
  - `androidx.a2ui:a2ui-model:1.0.0-alpha01`
  - `androidx.a2ui.compose:compose-runtime:1.0.0-alpha01`
  - `androidx.a2ui.compose:compose-ui:1.0.0-alpha01`
  - `androidx.compose.material3:material3-a2ui:1.0.0-alpha01`
- `A2uiSchemaManager`가 카탈로그 JSON 스키마를 시스템 프롬프트에 자동 삽입해 LLM이 유효한 페이로드 생성 가능

---

## 💡 개발자 포인트
- 에이전트 모델로 `gemini-3.1-flash-lite` 사용 (ADK 코드 예시 기준)
- **`require_confirmation=True`** 옵션으로 예약 같은 불가역 작업에 사용자 확인 필수 처리 가능
- AG-UI Kotlin SDK 사용 시 `HttpAgent`, `HttpAgentConfig`, `RunAgentInput`으로 백엔드 연결

> ⚠️ A2UI는 현재 `v0.9` 버전이며, Compose A2UI 라이브러리도 `alpha01` 단계입니다. 프로덕션 적용 시 API 안정성을 주의하세요.

> ⚠️ ADK A2UI 통합은 현재 Python 버전만 A2UI 지원 포함. 다른 언어 버전은 미지원.

- A2UI 카탈로그 컴포넌트(`InteractiveOptionPicker`, `SeatSelectionPicker`, `BookingStatus` 등)를 Android 측에서 `A2uiCatalog`로 등록해야 렌더링 가능
- 백엔드 UI 변경 시 앱 재배포 불필요 — 서버가 컴포넌트 속성만 업데이트

---

## 📅 버전 / 출시 일정

| 라이브러리 | 버전 |
|---|---|
| `androidx.a2ui:a2ui-model` | `1.0.0-alpha01` |
| `androidx.a2ui.compose:compose-runtime` | `1.0.0-alpha01` |
| `androidx.a2ui.compose:compose-ui` | `1.0.0-alpha01` |
| `androidx.compose.material3:material3-a2ui` | `1.0.0-alpha01` |
| AG-UI Protocol | — |
| A2UI Protocol | `v0.9` |
| ADK 에이전트 모델 | `gemini-3.1-flash-lite` |


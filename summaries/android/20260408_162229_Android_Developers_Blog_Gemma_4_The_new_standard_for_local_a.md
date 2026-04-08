# Android Developers Blog: Gemma 4: The new standard for local agentic intelligence on Android

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/04/gemma-4-new-standard-for-local-agentic-intelligence.html
- **요약 일시**: 2026-04-08 16:22:29

---

## 핵심 요약 (3줄)
- Google이 Gemma 4를 출시하며 Android 개발 전반(개발 도구 + 온디바이스 앱)에 로컬 에이전틱 AI를 통합한다.
- Android Studio에서 Gemma 4를 로컬 모델로 사용해 Agent Mode 기반 코드 어시스턴스를 완전히 로컬 환경에서 활용할 수 있다.
- ML Kit GenAI Prompt API를 통해 앱 내에서 Gemma 4를 온디바이스로 실행할 수 있으며, 이전 버전 대비 최대 4배 빠르고 배터리를 60% 절약한다.

## 주요 발표 내용
- **Android Studio + Gemma 4 (로컬 AI 코딩)**
  - Gemma 4를 Android Studio의 로컬 모델로 선택하여 Agent Mode 전체 기능 활용 가능
  - 레거시 코드 리팩토링, 신규 앱/기능 빌드, 반복적 버그 수정 등 지원
  - 모델과 추론이 개발자 로컬 머신에서만 실행되어 완전한 프라이버시 보장

- **온디바이스 Gemma 4 (ML Kit GenAI Prompt API)**
  - Gemma 4 E2B, E4B 모델을 AICore 지원 디바이스에서 직접 실행 가능
  - **AICore Developer Preview** 공식 런칭으로 프로토타이핑 시작 가능
  - 기존 Gemini Nano 대비 최대 **4배 빠른 속도**, **60% 배터리 절감**
  - Gemma 4는 차세대 Gemini Nano 4의 베이스 모델로 채택됨

- **오픈 라이선스 및 생태계**
  - Apache 오픈 라이선스 제공으로 자유로운 상업적 활용 가능
  - 향후 **Android Bench**에 Gemma 4 및 기타 오픈 모델 벤치마크 추가 예정
  - 현재 Gemini Nano는 이미 **1억 4천만 대** 이상의 디바이스에 탑재 중

## 개발자에게 중요한 포인트
- **로컬 완결형 AI 개발환경**: 인터넷 연결 없이 개발 머신에서 Gemma 4 추론이 가능하므로, 비용 절감 및 코드 프라이버시 확보 측면에서 유리
- **온디바이스 AI 앱 개발 준비**: ML Kit GenAI Prompt API로 Gemma 4를 앱에 통합할 수 있어, 서버 의존 없는 AI 기능 구현이 가능해짐
- **AICore Developer Preview 활용**: 연내 출시될 플래그십 디바이스(Gemini Nano 4 탑재)에 대비해 지금부터 Gemma 4 E2B/E4B로 프로토타이핑 시작 권장
- **Agent Mode 적극 활용**: Gemma 4는 처음부터 Agent Mode를 고려해 훈련되었으므로, 도구 호출(Tool Calling) 기반의 복잡한 개발 워크플로우 자동화에 적합
- **모델 선택 기준**: Android Bench 업데이트 예정이므로, 향후 성능/배터리/품질 트레이드오프 데이터를 기반으로 모델 선택 가능

## 출시 일정 / 버전 정보
| 항목 | 내용 |
|------|------|
| 발표일 | 2026년 4월 2일 |
| Gemma 4 모델 | E2B, E4B (AICore Developer Preview에서 사용 가능) |
| AICore Developer Preview | 현재 출시 (즉시 사용 가능) |
| Gemini Nano 4 탑재 플래그십 디바이스 | **2026년 하반기 출시 예정** |
| Android Bench Gemma 4 지원 | **향후 릴리즈 예정** (구체적 일정 미정) |

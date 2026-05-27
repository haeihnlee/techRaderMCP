# Android Developers Blog: Top AI on Android updates for building intelligent experiences from Google I/O ‘26

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/android-ai-intelligence-system.html
- **요약 일시**: 2026-05-27 09:09:03

---

## 🔑 핵심 요약
- **Android가 OS에서 Intelligence System으로 전환** — 앱이 에이전트와 자연스럽게 협력하는 플랫폼으로 진화
- **`AppFunctions` (Android MCP)** 출시로 앱이 on-device **MCP 서버** 역할 수행, Gemini 등 에이전트와 통합
- **Gemini Nano 4 Preview**, **Firebase AI Logic Hybrid Inference**, **ADK for Android** 등 온디바이스·하이브리드 AI 풀스택 제공

---

## 📣 주요 발표 내용

**1. AppFunctions (Android MCP)** — Experimental Preview
- 앱을 **on-device MCP 서버**로 동작시켜 앱의 도구·서비스·데이터를 시스템·에이전트와 공유
- 새 **`skill`** 로 코드베이스 내 AppFunctions를 손쉽게 생성
- **test agent** 제공 — 시뮬레이션 환경에서 AppFunctions 디버깅·실험 가능
- **Early Access Program** 운영 중

**2. Gemini Nano 4 Preview & ML Kit GenAI APIs**
- **`AICore Developer Preview`** 로 Nano 4 모델 프리뷰·프로토타이핑
- **ML Kit GenAI `Prompt API`** 로 프로덕션 전환 지원 (플래그십 기기 연내 출시)
- **Structured Output API** — 객체 클래스 기반 신뢰성 있는 출력 보장
- **Prefix Caching** — 공통 프롬프트의 중간 LLM 상태 재사용으로 추론 시간 단축
- **LiteRT-LM** 으로 fine-tuned 자체 SLM 탑재 가능

**3. Hybrid Inference & Agents**
- **Firebase AI Logic Hybrid Inference** — `PREFER_ON_DEVICE` / `PREFER_CLOUD` / `ONLY_ON_DEVICE` / `ONLY_CLOUD` 라우팅 모드 제공
- **A2UI Jetpack Compose Renderer** — 에이전트가 "UI를 말하도록" 하여 A2UI 메시지를 네이티브 Compose UI로 자동 렌더링
- **ADK for Android** v1 — 온디바이스·클라우드 모델 간 멀티 에이전트 워크플로우, orchestration·context·session 관리

---

## 💡 개발자 포인트

> **AppFunctions는 Experimental Preview 단계** — 프로덕션 배포 전 Early Access Program 가입 필요. API 안정성은 변동 가능.

- **앱이 곧 에이전트의 도구**가 되는 패러다임 — 기존 딥링크/Intent 기반 통합에서 **MCP 기반 선언적 통합**으로 이동
- 온디바이스 AI 채택 시 **`Prefix Caching`** 활용으로 추론 지연 최소화 가능
- 하이브리드 라우팅은 **명시적 모드 지정**으로 제어 — 데이터 민감도·네트워크 상황에 따라 `ONLY_ON_DEVICE` 등 정책 설계 필요
- **A2UI Compose Renderer** 도입 시 에이전트 응답 UI 일관성 확보 — 커스텀 UI 구성 부담 감소
- **ADK for Android** 는 멀티 에이전트 오케스트레이션 표준 — 복잡한 워크플로우 구축 시 Cloud-side ADK와 통합 고려

---

## 📅 버전 / 출시 일정

| 항목 | 상태 / 일정 |
|---|---|
| AppFunctions (Android MCP) | Experimental Preview (Early Access 모집 중) |
| Gemma 4 | 2026년 4월 출시 |
| Gemini Nano 4 | AICore Developer Preview / 연내 플래그십 기기 탑재 |
| ML Kit GenAI Structured Output API | Upcoming |
| A2UI Jetpack Compose Renderer | Upcoming |
| ADK for Android | v1 실험판 제공 |
| 발표일 | 2026-05-26 (Google I/O 2026) |


# 17 Things to know for Android developers at Google I/O

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/17-things-android-developers-google-io.html
- **요약 일시**: 2026-05-20 09:12:15

---

## 🔑 핵심 요약
- **Android CLI 정식 출시** + **Google AI Studio**로 프롬프트 한 줄로 네이티브 Android 앱 빌드 가능
- **Compose-first 전환 공식화**: Views는 유지보수 모드 진입, 모든 신규 가이드/라이브러리는 Compose 기반
- **Adaptive by Default**: 폰·폴더블·태블릿·차량·XR·Googlebook까지 단일 코드베이스로 확장, Jetpack Glance로 위젯도 통합

---

## 📣 주요 발표 내용

**🛠️ AI 에이전트 + 개발 도구**
- `Android CLI` Stable 릴리스 — **Claude Code, Codex, Antigravity** 등 임의 에이전트가 Android Studio의 심볼 분석·Compose 프리뷰·`Journeys` E2E UI 테스트 호출 가능
- **Google AI Studio**: 프롬프트 → Jetpack Compose + Kotlin 기반 네이티브 앱 자동 생성, 임베디드 에뮬레이터 + Play Console 내부 테스트 트랙 배포까지 지원
- **Android Bench**: LLM 리더보드에 `Gemma 4` 등 오픈웨이트 모델 추가
- **Migration Assistant**: iOS/React Native/웹 앱을 Jetpack Compose 기반 네이티브 Android로 자동 변환 (수주 → 수시간)

**🤖 앱에 AI 통합**
- `Gemini Nano 4` 프리뷰 — 온디바이스 데이터 추출·요약
- **Firebase AI Logic** — URL/Maps/웹 검색 그라운딩 지원
- **Agent Development Kit (ADK) for Android** + `AG-UI`, `A2UI` 프로토콜
- **AppFunctions**: 앱을 **온디바이스 MCP 서버**처럼 동작시키는 Jetpack 라이브러리 (Early Access)

**📱 Compose & Adaptive**
- `Jetpack Navigation 3`, 실험적 `Grid`/`FlexBox` 레이아웃, 비터치 입력 강화
- `CameraX` — 모든 윈도우 사이즈에서 정상 프리뷰
- **Googlebook**(신규 노트북 폼팩터) + Desktop Emulator (Android Studio Canary)
- **Jetpack Glance**: 모바일·Wear OS·차량 위젯을 단일 Compose 모델로 통합, `RemoteCompose` 통합

**🚗 🥽 📺 신규 폼팩터**
- **Android for Cars**: Car App Library로 Android Auto + Automotive OS 동시 빌드, Android 17 폰의 Android Auto에 **주차 중 비디오 재생** 추가
- **Android XR Developer Preview 4**: XR Runtime, `Jetpack SceneCore`, `ARCore for Jetpack XR` 곧 Beta 진입
- **Google TV**: Pointer Remote 지원 선언 가능, **Engage SDK**(구 Video Discovery API)로 추천·재개·엔타이틀먼트 통합

**🎬 미디어**
- `CameraXViewfinder` Composable, **Media3 AI Effects**(Magic Eraser, Studio Sound)
- `CodecDB` — 칩셋별 인코딩 권장값, ExoPlayer 신규 **Scrubbing Mode**

---

## 💡 개발자 포인트

> ⚠️ **Breaking 방향성: Views는 유지보수 모드로 전환**
> 신규 기능·문서·라이브러리는 모두 **Compose-first**로 작성됩니다. View 기반 신규 프로젝트는 사실상 권장되지 않으며, 기존 코드도 점진적 Compose 마이그레이션이 권장됩니다.

> 📌 **AppFunctions = 앱이 MCP 서버가 된다**
> Gemini/에이전트가 여러분의 앱 기능을 "tool"로 호출할 수 있게 되므로, 지금부터 핵심 기능을 함수 단위로 노출 가능한 구조로 설계해두는 것이 유리합니다.

- **Android CLI** 도입으로 Claude Code/Codex 같은 외부 에이전트가 IDE의 무거운 분석 기능(심볼 해석, 경고 분석, Compose 프리뷰 렌더링)을 호출 가능 — 로컬 AI 워크플로 자동화 여지가 크게 확장됨
- 대형 화면 디바이스 5.8억 대 + 멀티 디바이스 사용자 결제액 14배 → **Adaptive 레이아웃 미적용 = 매출 손실**
- `Jetpack Glance` + `RemoteCompose`로 모바일/차량은 고해상도 애니메이션, Wear OS는 저전력 네이티브 렌더링을 한 코드로 처리
- Android Auto 비디오 재생은 **Android 17 폰** 한정 — 타겟 SDK·디바이스 분기 필요

---

## 📅 버전 / 출시 일정

| 항목 | 상태 / 버전 |
|---|---|
| Android CLI | **Stable** (정식 릴리스) |
| Gemini Nano 4 | Preview |
| AppFunctions | Private Preview / Early Access Program |
| Android XR SDK | **Developer Preview 4** (XR Runtime/SceneCore/ARCore for Jetpack XR → 곧 Beta) |
| Jetpack Glance + Android Widgets 통합 | Android **17** |
| Android Auto 비디오 재생 | Android **17** 폰 (Beta 카테고리, 신청 필요) |
| Desktop Android Emulator | Android Studio **Canary** |
| Views (UI Toolkit) | **Maintenance Mode** |
| 발표 시점 | 2026-05-19 (Google I/O) |


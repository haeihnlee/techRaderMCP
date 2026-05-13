# Android Developers Blog: Building for the Intelligence System on Android

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/the-android-show-developers-cut-2026.html
- **요약 일시**: 2026-05-13 09:06:04

---

## 🔑 핵심 요약
- **Android가 "운영체제(OS)"에서 "인텔리전스 시스템"으로 전환**되며, 디바이스가 사용자 의도를 예측해 앱을 자동 호출하는 패러다임으로 이동합니다.
- **Gemini Intelligence** 출시: 코드 수정 없이도 `Gemini`가 멀티스텝 작업(예: 카페 주문, 장보기 카트 구성)을 앱 대신 실행 → 고의도(high-intent) 트래픽 유입.
- **AppFunctions API**(MCP 유사) + **Jetpack Glance / RemoteCompose** 기반 위젯 확장 + **XR/차량/Googlebooks 등 폼팩터 적응형 개발** 강화.

---

## 📣 주요 발표 내용

### 1. Gemini Intelligence & Task Automation
- `Gemini`가 선택된 앱들에서 **자동 태스크 실행** 가능 (음식 주문, 차량 호출 등으로 시작 → 폴더블·워치·차량·XR 글래스로 확대).
- 개발자는 **코드 변경 없이** Gemini가 자사 앱으로 사용자를 라우팅하도록 노출됩니다.

### 2. AppFunctions (Private Preview)
- 앱의 서비스·데이터·액션을 **자연어 설명과 함께** OS·에이전트에 직접 노출하는 API.
- `KakaoTalk` 등이 프라이빗 프리뷰 참여 — "메시지 보내기", "음성 통화 시작" 같은 기능을 인텔리전스 시스템 트리거로 제공.
- 이미 25개 앱의 유스케이스에서 로컬 실행 지원, **Early Access Program** 등록 가능.

### 3. Widgets — Jetpack Glance + RemoteCompose
- 위젯이 **차량(Android Auto 2.5억 대)** 까지 확장.
- 새 엔진 **`RemoteCompose`** 도입: snapscroll, expressive buttons, particle effects 등 프리미엄 인터랙션.
- **Create My Widget**: Gemini가 사용자 요청대로 홈스크린/Wear OS용 어댑티브 위젯을 직접 생성.

### 4. 어댑티브 UI 빌딩 블록
- **`Jetpack Navigation 3`**: Scene decorators, `NavDisplay`의 shared elements 빌트인 지원.
- **`Jetpack Compose 1.11`**: 반응형 레이아웃용 `Grid`, `Flexbox`, `MediaQuery`, `Style` (Experimental — 피드백 모집 중).
- **Car App Library**: "build once" 미디어/비디오 앱을 Android Auto + Android Automotive OS 모두 지원, 주차 시 풀스크린 비디오 가능.
- **Android XR SDK**: `Jetpack Compose Glimmer`(글래스용 glanceable UI), `Jetpack Projected APIs`, `ProjectedTestRule` API 신설. **Developer Preview 4** 다음 주 공개.

---

## 💡 개발자 포인트

> **🚨 패러다임 시프트 주의:** Android 앱의 진입점이 더 이상 "런처 아이콘"만이 아닙니다. 사용자는 **Gemini를 통해 앱 기능을 직접 호출**하므로, AppFunctions로 핵심 기능을 노출하지 않으면 **인텔리전스 트래픽에서 누락**될 수 있습니다.

- **무코드 통합 vs API 통합 2-track 제공**: 가장 쉬운 길은 자동 라우팅 등록, 더 큰 통제권을 원하면 **AppFunctions API(MCP 스타일)** 사용.
- **`RemoteCompose`는 백워드 호환** — Android 16+ 에서 새 기능을 자동 활용, 구버전에서는 graceful degradation. `Jetpack Glance`만 쓰면 자동 처리됩니다.
- **XR 글래스 대비**: `Jetpack Compose Glimmer` + `Jetpack Projected APIs` 로 폰 ↔ FoV 브리지 UI를 미리 준비하는 것이 권장됩니다.
- **Compose 1.11의 `Grid`/`Flexbox`/`MediaQuery`/`Style`** 은 Experimental 플래그 해제 전 단계 — 지금 피드백 보내면 API 형태에 영향 가능.

---

## 📅 버전 / 출시 일정

| 항목 | 출시 시기 / 버전 |
|------|------------------|
| Gemini Intelligence (1차) | **2026년 여름**, 최신 Galaxy + Pixel 폰부터 |
| Gemini Intelligence (확장) | 2026년 하반기 — 워치·차량·글래스·랩탑 |
| Android XR SDK | **Developer Preview 4 — 다음 주 공개** |
| Jetpack Compose | **1.11** (Grid/Flexbox/MediaQuery/Style Experimental) |
| Jetpack Navigation | **3** (Scene decorators 추가) |
| RemoteCompose 풀 지원 OS | **Android 16+** |
| 후속 발표 | **Google I/O — 다음 주** |


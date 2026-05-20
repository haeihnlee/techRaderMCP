# Android Developers Blog: Adaptive development for the expanding Android ecosystem

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/android-adaptive-development-ecosystem.html
- **요약 일시**: 2026-05-20 09:16:46

---

## 🔑 핵심 요약
- **Android 17 (API level 37)** 부터 **Adaptive-First 개발**이 표준이 되며, 대형 화면(sw > 600dp)에서 orientation·resizability 제한 **opt-out이 제거**됨
- 폰·폴더블·태블릿·Chromebook·XR·자동차 등 **5억 8천만 대 이상의 대화면 디바이스** 시장에서 멀티 디바이스 사용자는 폰 전용 대비 **평균 9배(폴더블은 14배)** 더 소비
- **Jetpack Compose** 중심으로 `Grid`/`FlexBox`/`MediaQuery API`/`Styles API` 등 신규 레이아웃 프리미티브 출시, **Googlebook(차세대 ChromeOS)** 으로 데스크톱 컴퓨팅 확장

---

## 📣 주요 발표 내용

- **Android 17 Adaptive 기본화**
  - 대형 화면(sw > 600dp)에서 orientation/resizability **개발자 opt-out 제거**
  - `UNIVERSAL_RESIZABLE_BY_DEFAULT` 플래그로 SDK 36에서 사전 테스트 가능
  - Google Play에 **"Optimized for large screens" 배지** 도입

- **확장된 서피스(Surface)**
  - **Connected Displays**: Android 16 QPR3에서 stable, Pixel·Samsung 모바일 기기를 외부 디스플레이로 데스크톱 환경 전환
  - **Car Ready Mobile Apps** 프로그램 및 **Android TV 포인터 지원** 강화
  - **Googlebook**: ChromeOS의 차세대 버전, Android 스택 기반의 laptop-class 성능 제공

- **Jetpack Compose 신규 API**
  - `Grid`, `FlexBox` — CSS 영감의 1D/2D 레이아웃
  - **Navigation 3 (1.1)**: `Scene Decorators`로 화면을 bar·rail·dialog로 감싸기
  - **MediaQuery API** (experimental): 윈도우 크기·포인터 정밀도 등 디바이스 UI 능력 관찰
  - **Styles API** (experimental): state 기반으로 시각 속성 동적 변경

- **비터치 입력 지원** (Compose 1.11)
  - 트랙패드 지원이 마우스 수준으로 향상
  - 테스트용 API: `TrackpadInjectionScope`, `performTrackpadInput`
  - 표준 focus ring 내장 지원으로 접근성 강화

- **AI 기반 개발 도구**
  - **Android Skills**: View→Compose, Navigation 2→3, Camera→CameraX 마이그레이션을 돕는 LLM용 모듈 지침
  - **New Project Agent** (Android Studio Panda 2): adaptive 베스트 프랙티스로 프로젝트 초기화

---

## 💡 개발자 포인트

> ⚠️ **Breaking Change**: `targetSdk = 37` (Android 17) 로 빌드하면 sw > 600dp 디바이스에서 더 이상 fixed orientation이나 non-resizable 설정을 강제할 수 없습니다. 기존에 회피용 opt-out에 의존하던 앱은 **반드시 다양한 디스플레이 크기 대응 작업이 필요**합니다.

- **마이그레이션 전 테스트**: SDK 36에서 `UNIVERSAL_RESIZABLE_BY_DEFAULT` 플래그를 켜고 동작 검증 권장 (Developer Options → App Compatibility Changes)
- **Compose First 권장**: 새 UI는 View 대신 Jetpack Compose로 작성, `Grid`/`FlexBox`로 반응형 레이아웃 구성
- **입력 다양성 고려**: 대화면에서는 키보드·트랙패드·마우스·스타일러스가 주 입력. `performTrackpadInput` 등으로 자동화 테스트 추가
- **Googlebook 대비**: Android Studio Canary의 **Desktop Emulator** 로 laptop-class 환경 사전 검증
- **비즈니스 임팩트**: 폴더블 사용자 14x 지출 데이터를 근거로 adaptive 대응 ROI 강조 가능

---

## 📅 버전 / 출시 일정

| 항목 | 버전 / 상태 | 비고 |
|---|---|---|
| **Android 17** | API level 37 | Adaptive-first 표준, opt-out 제거 |
| **Connected Displays** | Android 16 QPR3 | Stable 출시 |
| **Jetpack Compose** | 1.11 | 트랙패드 지원, focus ring |
| **compose-navigation3** | 1.1 | Scene Decorators 추가 |
| **MediaQuery API / Styles API** | Experimental | Compose 신규 |
| **Android Studio** | Panda 2 | New Project Agent 포함 |
| **Desktop Emulator** | Android Studio Canary | Googlebook 대비 |
| **Google I/O 2026** | 발표일: 2026-05-19 | io.google에서 전체 업데이트 확인 |


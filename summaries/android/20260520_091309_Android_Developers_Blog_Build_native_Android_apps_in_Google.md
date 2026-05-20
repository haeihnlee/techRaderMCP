# Android Developers Blog: Build native Android apps in Google AI Studio

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/build-android-apps-google-ai-studio.html
- **요약 일시**: 2026-05-20 09:13:09

---

## 🔑 핵심 요약
- **Google AI Studio**에서 프롬프트만으로 **Kotlin + Jetpack Compose** 기반 네이티브 Android 앱을 **브라우저에서 즉시** 생성 가능
- 설치 없이 웹에서 **임베디드 Android Emulator**, **adb 설치**, **Google Play 내부 테스트 트랙 게시**까지 end-to-end 워크플로우 제공
- ZIP 다운로드 또는 **GitHub 내보내기**로 **Android Studio**로 매끄럽게 핸드오프 가능

---

## 📣 주요 발표 내용
- **AI Studio → Native Android 앱 생성**: 단일 프롬프트로 다화면 앱까지 빌드. 별도 SDK 설치/라이브러리 구성 불필요
- **클라우드 반복 개발**: 브라우저 내장 **Android Emulator**로 빌드 중 앱을 즉시 프리뷰
- **즉시 설치**: USB로 디바이스 연결 후 통합된 `adb`로 바로 인스톨
- **Google Play 직접 배포**: 개발자 계정 연동 시 앱 레코드 생성 → 번들 패키징 → **internal testing track** 업로드까지 자동화
- **Android Studio 핸드오프**: 프로젝트 ZIP 다운로드 또는 GitHub로 export → **Gemini in Android Studio** 또는 **Antigravity**(Android CLI 통합 에이전트)로 이어서 개발
- **초기 지원 카테고리**:
  - 개인 유틸리티 / 간단한 소셜 앱 (습관 트래커, 스터디 퀴즈, 일정 등)
  - **하드웨어 연동 앱**: Camera, GPS/Location, Accelerometer, Bluetooth 등 네이티브 API
  - **Gemini API 통합 AI 앱**

---

## 💡 개발자 포인트
- 기존 웹 기반 AI 앱 빌더 대비, **오프라인 지원·백그라운드 서비스·하드웨어 센서(GPS·BT·NFC)** 등 네이티브의 강점을 그대로 활용 가능
- **Jetpack Compose**가 공식 추천 toolkit으로 명시 — Compose 기반 코드 생성이 디폴트
- 프롬프트 → 프로토타입 → 실기기 테스트 → Play 내부 테스트 배포까지 한 자리에서 처리되므로 **PoC/MVP 사이클이 극단적으로 단축**
- AI Studio는 가벼운 반복 개발용, **복잡한 디바이스 타입 지원이나 고급 툴**이 필요해지면 Android Studio로 전환하는 워크플로우 권장

> ⚠️ 초기 릴리스는 **단순 유틸리티·하드웨어·AI 앱** 중심으로 범위가 제한됨. 복잡한 멀티모듈/대규모 앱은 아직 AI Studio 단독으로 다루지 않는 것으로 보임.

> 📌 곧 추가 예정: **Play Test Track 테스터 초대**, **Firestore / Firebase Auth / Firebase App Check** 등 Firebase 통합

---

## 📅 버전 / 출시 일정
| 항목 | 상태 | 비고 |
|------|------|------|
| AI Studio에서 Android 앱 빌드 | **2026-05-19 출시** | 오늘부터 사용 가능 |
| Google Play 내부 테스트 트랙 게시 | 출시됨 | AI Studio에서 직접 publish |
| Play 테스터 초대 관리 | Coming soon | AI Studio 내에서 초대 |
| Firebase 통합 (Firestore / Auth / App Check 등) | Coming soon | out-of-the-box 지원 예정 |


# Android Developers Blog: Building Premium Android Experiences at Google I/O '26

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/06/building-premium-android-experiences-google-io-26.html
- **요약 일시**: 2026-06-03 09:09:24

---

## 🔑 핵심 요약
- **Android 17**부터 디바이스 RAM 기반 **앱 메모리 한도**가 도입되어, 한도를 넘으면 앱이 강제 종료됨 → 가벼운 메모리 풋프린트가 필수가 됨
- Android Studio에 **`R8 Configuration Analyzer`** 신규 추가 → 비효율적인 `keep rules`를 찾아내 최적화·난독화·축소 점수로 진단
- **Jetpack Glance + `RemoteCompose`**로 폰·워치·자동차 위젯을 하나의 Compose 모델로 통합 개발
- **CameraX 1.5 + Media3**로 캡처부터 편집·재생까지 미디어 파이프라인 전체를 프로덕션급으로 구성

---

## 📣 주요 발표 내용

**1. 성능 — `R8 Configuration Analyzer`**
- Android Studio에 신규 도입된 R8 진단 도구
- 최적화를 가로막는 과도하게 광범위한 `keep rules`를 식별
- **최적화·난독화·축소(shrinking) 점수** 제공
- 사례: **Monzo**는 R8 설정 최적화로 콜드 스타트 **30% 개선**, ANR **35% 감소**

**2. 도달 범위 — Widgets 통합 (`Jetpack Glance` + `RemoteCompose`)**
- 폰 홈 화면, **Wear Widgets**(기존 **Tiles**에서 명칭 변경), 자동차 위젯을 **하나의 Compose 기반 모델**로 개발
- **`RemoteCompose`**: 익숙한 Compose 도구로 원격 표면(remote surface)에 네이티브 렌더링되는 UI 로직 정의
  - Wear OS에서는 리소스 제약 하드웨어에서도 고성능 글랜서블 경험 보장
  - 모바일·자동차에서는 위젯에 더 풍부한 표현력을 주는 새 프레임워크로 활용

**3. 미디어 — `CameraX` + `Media3` 프로덕션 툴킷**
- **`CameraXViewfinder` Composable**: 폴더블·태블릿 등 모든 폼팩터에서 프리뷰 스케일·반응성 보장
- **CameraX v1.5**: 고프레임레이트·슬로모션 캡처, PiP 멀티태스킹 지원
- **`Media3 AI Effects` 라이브러리**(예정): Image & Video Enhance, Magic Eraser, Studio Sound을 통합 인터페이스로 제공
- **`Media3 Transformer`**: 멀티 에셋 편집/합성 개선
- **`CodecDB`**: 칩셋별 데이터 기반 인코딩 추천
- **ExoPlayer Scrubbing Mode**: 부드러운 탐색(seeking) 경험
- **`CastPlayer` API**(Media3): 향상된 Cast 지원

---

## 💡 개발자 포인트

> **⚠️ Breaking Change — Android 17 앱 메모리 한도**
> Android 17은 디바이스 RAM 기반의 보수적인 앱 메모리 한도를 도입합니다. 극단적인 메모리 누수·아웃라이어를 시스템 차원에서 차단하기 위한 것으로, **이 임계값을 넘으면 앱이 강제 종료(terminated)됩니다.** 가벼운 메모리 풋프린트는 더 이상 선택이 아니라 필수 요구사항입니다.

- 위 메모리 한도 대응을 위해 **`R8` 최적화가 사실상 필수** → `R8 Configuration Analyzer`로 불필요한 `keep rules`를 정리해 코드 축소·메모리 헤드룸 확보
- 위젯을 개발 중이라면 **Tiles → Wear Widgets** 명칭 변경과 **Jetpack Glance 통합 모델**로의 마이그레이션 흐름을 확인할 것
- 미디어 앱은 `CameraX`/`Media3` 조합으로 캡처~재생 전 과정을 단일 스택으로 통합 가능 → 폼팩터 분기 코드 최소화

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| 발표 시점 | Google I/O '26 (블로그 게시 2026-06-02) |
| Android 17 | RAM 기반 앱 메모리 한도 도입 |
| CameraX | v1.5 (고프레임레이트·슬로모션·PiP) |
| Media3 AI Effects | 제공 예정(will provide) |
| R8 Configuration Analyzer | Android Studio에 추가 |


# Android Developers Blog: Celebrating 5 years of Jetpack Compose

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/07/five-years-of-jetpack-compose.html
- **요약 일시**: 2026-07-29 15:44:00

---

## 🔑 핵심 요약
- **Jetpack Compose 1.0** 출시 5주년 (2021.07.28 → 현재 **1.11**), 상위 1,000개 앱 중 **68% 이상**이 프로덕션에서 사용 중
- Google I/O 2026에서 **Compose-first** 선언 — 향후 모든 UI 개발은 Compose로만 진행되고 **Views 툴킷은 유지보수 모드** 진입
- 올해 **적응형(adaptive) API** 대폭 추가: `FlexBox`, `Grid`, `MediaQuery`, `Styles`

---

## 📣 주요 발표 내용
- **폼팩터 확장**: 모바일을 넘어 **Compose for TV**, **Wear OS**, **Glance for Widgets**, 디스플레이 글래스용 **Jetpack Compose Glimmer**까지 지원
- **디자인 시스템 진화**: 출시 당시 Material 2 컴포넌트 → 현재 **Material 3 Expressive** 지원
- **Material Design**도 초점을 전면 Compose로 이동 — `findViewById` 시대의 종료 선언
- **Compose Multiplatform** (JetBrains 협업)으로 desktop / iOS / web까지 확장
- 커뮤니티 라이브러리 하이라이트
  - `telephoto` (Saket Narayan) — 팬·줌 제스처 + 대용량 이미지 서브샘플링
  - `Touch Robot` (Saket Narayan) — 인터랙션 애니메이션 테스트 자동화
  - `Haze` (Chris Banes) — 배경 블러 처리
  - `molecule` / `mosaic` (Jake Wharton) — Compose 런타임을 터미널 UI 등에 활용
- 탄생 배경: Views 툴킷 언번들링 프로젝트 + Kotlin 내 XML 임베딩 실험이 합쳐져, **컴파일러 플러그인 + 런타임 + Kotlin** 기반 선언형 툴킷으로 완성

---

## 💡 개발자 포인트

> **Breaking / 전략적 변경**: **Views 툴킷이 maintenance mode로 전환**되었습니다. 신규 UI 기능은 더 이상 Views에 추가되지 않으므로, 신규 화면은 Compose로 작성하고 레거시 View 화면의 마이그레이션 로드맵을 지금 수립해야 합니다.

- **적응형 UI**가 올해의 핵심 축입니다. 폴더블·태블릿·TV 대응 시 수동 브레이크포인트 분기 대신 `MediaQuery`, `FlexBox`, `Grid`를 검토하세요.
- **Material 2 → Material 3 Expressive** 전환을 준비하세요. 컴포넌트/테마 API가 다르므로 점진 마이그레이션 계획이 필요합니다.
- 멀티플랫폼을 고려한다면 **Compose Multiplatform**으로 Android 코드의 UI 레이어 재사용 범위를 확인해볼 시점입니다.
- `Touch Robot`처럼 **제스처·애니메이션 스냅샷 테스트**가 가능해졌습니다. Paparazzi 기반 워크플로에 통합해 애니메이션 회귀를 잡을 수 있습니다.

`Touch Robot` 사용 예:

```kotlin
paparazzi.gif(end = 3_000) {
  DebitCard(Modifier.testTag("card"))
  val touchRobot = rememberTouchRobot()
  LaunchedEffect(Unit) {
    touchRobot.onNode(hasTestTag("card")).performGesture {
      draw(path = createAndroidHeadPath(), duration = 3.seconds)
    }
  }
}
```

---

## 📅 버전 / 출시 일정

| 항목 | 버전 / 날짜 |
| --- | --- |
| Compose 1.0 정식 출시 | 2021-07-28 |
| 현재 최신 안정 버전 | **1.11** |
| 다음 버전 | **1.12** (coming soon) |
| Compose-first 발표 | Google I/O 2026 |
| 5주년 블로그 게시 | 2026-07-28 |
| 라이브 "Birthday party" (Android Developers YouTube) | 2026-07-30 13:00 UTC |


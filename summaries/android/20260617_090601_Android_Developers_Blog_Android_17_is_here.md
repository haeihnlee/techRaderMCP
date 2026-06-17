# Android Developers Blog: Android 17 is here

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/06/Android-17.html
- **요약 일시**: 2026-06-17 09:06:01

---

## 🔑 핵심 요약
- **Android 17** 정식 출시 — 대부분의 Pixel 지원 기기에 배포, **AOSP 소스코드 공개**
- OS를 넘어 **인텔리전스 시스템**으로 전환: `AppFunctions` API로 앱 기능을 **Android MCP**(온디바이스 Model Context Protocol) 도구로 노출, Gemini 등 AI 에이전트가 호출 가능
- **Adaptive-first** 표준 전환: 대화면(sw > 600dp)에서 **방향·리사이즈 제한 강제 제거**(API 37 타겟)
- **Compose-first** 선언: 모든 신규 API/라이브러리가 Compose 전용, 기존 View 기반(`Fragment`, `RecyclerView`, `ViewPager`)은 **유지보수 모드** 진입

---

## 📣 주요 발표 내용

**🤖 인텔리전스 시스템 (AppFunctions)**
- `@AppFunction(isDescribedByKDoc = true)` 어노테이션 + KDoc 주석만으로 앱 기능을 AI 도구로 등록 (Jetpack 라이브러리 alpha)
- AI 에이전트가 앱의 로컬 상태에 직접 접근해 워크플로 실행
- **AppFunctions agent skill** 제공: 워크플로 분석 → Kotlin 코드 자동 생성 → KDoc 최적화 → 테스트용 ADB 명령 제공
- Gemini 연동은 현재 **private preview**, EAP 신청: `goo.gle/eap-af`

**📐 Adaptive-first (대화면 대응)**
- 전 세계 **5.8억대 대화면 기기** + **Googlebooks**(Android 스택 기반 차세대 ChromeOS) 출시 예정
- `screenOrientation`, `setRequestedOrientation()`, `resizeableActivity=false`, `minAspectRatio`/`maxAspectRatio` 등 레거시 제약이 **시스템에서 무시됨** (게임은 예외)
- **차세대 멀티태스킹**: App Bubbles(런처 아이콘 롱프레스로 플로팅 전환), Bubble Bar(대화면 태스크바), desktop interactive PiP(상호작용 가능한 PiP)
- **Continue On**: 기기 간 작업 이어받기 — `setHandoffEnabled()` + `onHandoffActivityDataRequested()` 구현

**🎨 Compose-first 전환**
- 모든 신규 Android API/라이브러리/툴/가이드가 **Jetpack Compose 전용**
- `android.widget` 패키지 및 View 기반 Jetpack 라이브러리는 **유지보수 모드**(중요 버그 수정만, 신규 기능 없음)
- **Jetpack Compose adaptive skill** + **XML to Compose Migration Skill**(AI 기반 레거시 레이아웃 자동 변환) 제공
- `NavigationSuiteScaffold`, Navigation 3 Scenes(`ListDetailSceneStrategy`/`SupportingPaneSceneStrategy`), Compose 1.11 FlexBox/Grid·트랙패드 지원

**⚡ 성능 & 효율**
- **앱 메모리 한도 강제**: 기기 총 RAM 기준 한도 초과 시 프로세스 강제 종료
- **R8 Optimizer** full mode + R8 configuration analyzer로 바이트코드 풋프린트 축소
- Android Studio Panda에 **LeakCanary 네이티브 통합**
- `ProfilingManager`의 `TRIGGER_TYPE_ANOMALY`로 메모리 한도 도달 시 힙 덤프 자동 캡처
- **ART 세대별 GC**: 짧은 수명 객체 대상 young-generation 스윕으로 CPU·전력·UI 끊김 감소

---

## 💡 개발자 포인트

> **Breaking Change — 대화면 방향/리사이즈 제약 무력화**
> API level 37을 타겟하는 앱은 대화면(sw > 600dp)에서 `screenOrientation`, `setRequestedOrientation()`, `resizeableActivity=false`, aspect ratio 제약이 모두 무시됩니다. 앱은 임의의 윈도우 크기·free-form 윈도잉에 대응해야 합니다. (게임은 `app category` 기준 예외)

> **Breaking Change — Activity 재생성 동작 변경**
> `CONFIG_KEYBOARD`, `CONFIG_KEYBOARD_HIDDEN`, `CONFIG_NAVIGATION`, `CONFIG_TOUCHSCREEN`, `CONFIG_COLOR_MODE` 변경 시 기본적으로 Activity를 재시작하지 않고 `onConfigurationChanged()`로 전달합니다. 전체 재시작이 필요하면 `android:recreateOnConfigChanges` 매니페스트 속성으로 **명시적 opt-in** 필요.

> **메모리 한도 강제 종료 주의**
> 메모리 한도로 종료되면 `ApplicationExitInfo.getDescription()`이 `"MemoryLimiter:AnonSwap"`를 반환합니다. R8 full mode·프로파일링으로 풋프린트를 사전 점검하세요.

- **Compose 마이그레이션 권장**: View 기반 컴포넌트는 신규 기능 지원이 끊기므로 신규 개발은 Compose로 진행
- AppFunctions는 지금부터 준비 가능 — ADB 명령 + 테스트 에이전트 앱으로 미리 검증

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
| --- | --- |
| Android 17 출시일 | 2026년 6월 16일 |
| API Level | 37 |
| 배포 대상 | 대부분의 지원 Pixel 기기 (신규 기기는 추후 몇 달 내) |
| 소스코드 | AOSP에 공개 |
| AppFunctions Jetpack | alpha |
| Gemini 연동 | private preview (EAP: `goo.gle/eap-af`) |
| Googlebooks (차세대 ChromeOS) | 출시 예정 |


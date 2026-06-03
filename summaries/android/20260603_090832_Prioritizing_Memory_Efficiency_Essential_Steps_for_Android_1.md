# Prioritizing Memory Efficiency: Essential Steps for Android 17

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/06/prioritizing-memory-efficiency-steps-for-android-17.html
- **요약 일시**: 2026-06-03 09:08:32

---

## 🔑 핵심 요약
- **Android 17**부터 시스템이 기기 **총 RAM 기준 앱 메모리 한도**를 강제 적용하며, 초과 시 **stack trace 없이 프로세스를 강제 종료**한다.
- 메모리 누수·과다 사용은 잦은 **GC(가비지 컬렉션)** → UI 끊김, **LMK(Low Memory Killer)** 발생 → 콜드 스타트·유저 상태 손실로 이어진다.
- Google이 권장하는 5대 최적화 전략: **R8 최적화**, **이미지 로딩 최적화**, **메모리 누수 탐지**, **메모리 트리밍**, **ProfilingManager 관측**.

---

## 📣 주요 발표 내용

**1. Android 17 앱 메모리 한도 도입**
- "한 개의 불량 앱(one bad actor)"이 기기 전체의 멀티태스킹·안정성을 망치는 것을 방지.
- **Foreground Service** 등 보호 상태의 앱이 메모리를 독점하면, LMK가 정상 앱·백그라운드 작업을 대신 종료해 **연쇄 종료(cascading kill)** 발생.
- 필드에서 한도 적용 여부 확인: `ApplicationExitInfo`의 `getDescription()` 호출 → exit reason이 `REASON_OTHER`, description에 `"MemoryLimiter:AnonSwap"` 포함.
- `TRIGGER_TYPE_ANOMALY` 기반 프로파일링으로 한도 도달 시 **heap dump 자동 캡처** 가능.

**2. R8로 바이트코드 최적화 극대화**
- 클래스·메서드·필드명을 축약하고 미사용 코드/리소스를 제거해 메모리 풋프린트 감소.
- 디지털 뱅크 **Monzo** 적용 결과: **ANR율 35%↓, 콜드 스타트 30%↑, 앱 크기 9%↓**.
- `build.gradle` 설정: `isShrinkResources = true`, `isMinifyEnabled = true`.
- `proguard-android-optimize.txt` 사용(레거시 `proguard-android.txt`는 **AGP 9에서 미지원**).
- `gradle.properties`에서 `android.enableR8.fullMode = false` 제거.
- **Configuration Analyzer**로 Obfuscation·Optimization·Shrinking 점수 및 keep rule 영향 진단.

**3. 이미지 로딩 최적화**
- **Bitmap**은 앱 메모리에서 가장 큰 객체 — 100KB 압축 이미지도 디코딩되면 수 MB RAM 차지.
- 권장 라이브러리: **Coil**(Kotlin/Compose), **Glide**(Java).
- 다운샘플 `inSampleSize`·`DownsampleStrategy`, 레터박스는 `InsetDrawable`로 처리.
- 투명도 불필요 시 `RGB_565` 사용(`ARGB_8888` 대비 메모리 절반).
- 기하 도형은 `ShapeDrawable`(벡터) 활용, 수동 관리 시 `bitmap.recycle()`로 재사용.
- **Android Studio Narwhal 4**: Heap Dump에서 ⚠️ 경고로 **중복 Bitmap** 탐지.

**4. 메모리 누수 탐지**
- **Android Studio Panda 3**의 **LeakCanary 프로파일러 태스크** — 누수 분석을 기기가 아닌 **개발 머신에서 수행**해 속도 향상.
- IDE 내 소스코드 연동(`Go to declaration`)으로 누수 추적·수정 마찰 최소화.

---

## 💡 개발자 포인트

> ⚠️ **Breaking Change**: 레거시 `proguard-android.txt`는 **Android Gradle Plugin 9에서 더 이상 지원되지 않습니다.** 반드시 `proguard-android-optimize.txt`로 전환하세요.

> ⚠️ Android 17에서 메모리 한도를 초과하면 앱이 **stack trace 없이** 종료됩니다. 일반적인 크래시 리포팅으로는 원인 추적이 어려우므로, `ApplicationExitInfo.getDescription()`에서 `"MemoryLimiter:AnonSwap"` 문자열을 체크해야 합니다.

- R8 keep rule은 **최대한 좁게(narrow scope)** 작성 — `-dontoptimize`, `-dontshrink`, `-dontobfuscate` 같은 전역 옵션과 Activity/Service/View를 통째로 keep하는 룰을 제거해야 최적화가 풀린다.
- **라이브러리 개발자**는 소비자에게 필요한 룰만 `consumer-rules`에, 내부 보호 룰은 `proguard-rules.pro`에 분리해야 한다.
- 메모리 한도는 로컬 디버깅 명령으로 **시뮬레이션**해 사전 검증 가능 (메모리 한도 문서 참고).
- Google Play Console에 향후 **필드 메모리 지표**가 추가 제공될 예정.

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| 발표일 | 2026년 6월 2일 |
| 메모리 한도 강제 적용 | **Android 17**부터 |
| `proguard-android.txt` 미지원 | **AGP 9**부터 |
| 중복 Bitmap 탐지 | **Android Studio Narwhal 4** |
| LeakCanary 프로파일러 태스크 | **Android Studio Panda 3** |


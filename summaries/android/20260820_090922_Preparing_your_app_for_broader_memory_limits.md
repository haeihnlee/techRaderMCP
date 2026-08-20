# Preparing your app for broader memory limits

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/08/app-broader-memory-limits.html
- **요약 일시**: 2026-08-20 09:09:22

---

## 🔑 핵심 요약
- Android 17에서 도입된 앱별 메모리 제한이 4GB~16GB+ 기기 전체로 확대 적용될 예정
- 메모리 한도 초과 시 **zRAM 스와핑 → 프로세스 강제 종료** 순으로 점진적 제재
- `Android vitals`, `Firebase Crashlytics 20.1.0`, `ProfilingManager`를 통한 메모리 모니터링 체계화 권고

---

## 📣 주요 발표 내용
- **Android 17 per-app 메모리 제한** 확대: Pixel 기기에서 시작해 향후 1년간 더 많은 제조사의 4GB~16GB+ 기기로 확산
- 메모리 한도 초과 시 Android의 단계적 조치:
  - **zRAM 스와핑**: 앱 페이지를 압축 RAM으로 강제 이동 → CPU 오버헤드 발생 → UI 버벅임
  - **프로세스 강제 종료**: zRAM 임계치 초과 시 앱 종료
- `ApplicationExitInfo.getDescription()`로 메모리 제한 원인 감지 가능 (`REASON_OTHER` + `"MemoryLimiter:AnonSwap"` 문자열)
- `TRIGGER_TYPE_ANOMALY`로 메모리 한도 도달 시 자동 힙 덤프 캡처 지원
- **Firebase Crashlytics `20.1.0`**: OOM 예외 및 메모리 리미터 종료 이벤트에 추가 디버그 데이터 제공
- **`ProfilingManager` API (Android 15, API level 35)**: 운영 기기에서 Java 힙 덤프·힙 프로파일 프로그래밍 방식 수집 가능

---

## 💡 개발자 포인트
> **앱이 메모리 한도를 초과하면 zRAM 스와핑으로 성능이 저하되고, 계속 증가하면 프로세스가 종료됩니다. 단계적으로 확산되므로 지금 바로 메모리 최적화를 시작해야 합니다.**

- **메모리 문제 감지 방법**:
  - `ApplicationExitInfo.getDescription()` 반환값에서 `"MemoryLimiter:AnonSwap"` 확인
  - Google Play Console → **Android vitals** → `Memory Usage (Anonymous RSS + swap)`, `Bitmap Memory Usage` 지표 활용
  - `ProfilingManager`에서 `TRIGGER_TYPE_OOM` / `TRIGGER_TYPE_ANOMALY` 트리거 등록
- **테스트**: `Memory Limiter adb commands`로 다양한 RAM 설정 환경 시뮬레이션 가능
- 메모리 최적화 권고 사항: R8 설정 최적화, 이미지 로딩 최적화, Android Studio 메모리 누수 탐지, 앱 백그라운드 전환 시 메모리 해제

---

## 📅 버전 / 출시 일정

| 항목 | 버전 / 시점 |
|------|------------|
| Android 17 per-app 메모리 제한 도입 | Android 17 (Pixel 우선 적용) |
| 더 많은 기기로 확대 | 향후 1년 내 (2026~2027) |
| Firebase Crashlytics 추가 메모리 디버그 데이터 | `20.1.0` |
| ProfilingManager API | Android 15 (API level 35) |


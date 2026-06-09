# Datadog delivers millions of in-depth performance insights with ProfilingManager

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/06/datadog-profilingmanager-performance-insights.html
- **요약 일시**: 2026-06-09 09:12:48

---

## 🔑 핵심 요약
- **Datadog**이 **Android 15+** 의 `ProfilingManager` API를 자사 **RUM(Real User Monitoring)** 및 **Continuous Profiling**에 통합
- 운영(production) 환경에서 콜스택 샘플·필드 트레이스·힙 덤프를 **낮은 오버헤드**로 직접 수집 → 주간 **수백만 건** 프로파일 처리
- 기존의 "어떤 문제가 발생했는가(ANR률 등)"에서 벗어나 **"왜(why) 발생했는가"** 코드 라인 단위 원인 분석이 가능해짐

---

## 📣 주요 발표 내용
- `ProfilingManager`는 **Android 15**에 도입된 시스템 서비스로, 앱이 운영 환경에서 **프로그래밍 방식**으로 성능 데이터를 수집
- 지원 수집 방식: **CPU 트레이스**, **콜스택 샘플링**, **Java 힙 덤프**, **네이티브 힙 프로파일**
- 수집된 트레이스는 외부 스토리지로 업로드 후 **`Perfetto`** 트레이스 분석 UI에서 검토 가능
- **자동 트리거 기반 수집**: 초기에는 `APP_FULLY_DRAWN` 신호 중심, 향후 `ANR`·`OOM`·`COLD_START` 트리거로 확장 예정
- **시스템 레벨 Perfetto 서비스(`traced`)** 와 직접 연동하여 백그라운드 사전 기록 모델로 예측 불가능한 이슈 포착
- **온디바이스 데이터 필터링**: 타 프로세스의 불필요한 정보를 기기 단에서 제거해 파일 크기 최소화·앱 관련 데이터만 전달
- 실사례: 한 Google 커뮤니케이션 앱이 필드 트레이스로 콜드 스타트 지연을 추적 → 백그라운드 **TTS 서비스가 startup 중 불필요하게 prewarm**되어 메인 스레드를 sleep시킨 원인 발견

---

## 💡 개발자 포인트
- 기존 RUM은 **TTID(time to initial display)**, **ANR률**, CPU 부하, frozen frame 등 표면 지표만 제공했으나, `ProfilingManager`로 **근본 원인(root cause)** 추적 경로가 열림
- Datadog은 자체 트레이스 프로세서 구현(Android Debug API 활용) 대신 `ProfilingManager`를 선택 → **샘플링 결정 오버헤드를 OS에 위임**하는 가장 성능적인 방안

> ⚠️ `ProfilingManager`의 **내장 rate limiting**을 안정성 안전장치로 활용해야 합니다. 과도한 텔레메트리 요청이 사용자 기기에 부담을 주는 것을 방지합니다.

> 📌 **샘플링 빈도와 데이터 수집량의 균형**이 중요합니다. 의미 있는 인사이트를 얻을 만큼 충분히 수집하되, 시스템 강제 샘플링으로 UX 영향을 인지 불가능한 수준으로 유지하세요.

- 향후 Datadog은 Android 프로파일링 데이터를 **코딩 에이전트의 1차 입력값**으로 삼아 성능 병목을 자율 해결하는 방향(탐지→개선 피드백 루프)을 목표로 함
- 적용은 **Datadog Mobile Real User Monitoring** 및 공식 문서 참고

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 지원 OS | **Android 15+** |
| 초기 트리거 | `APP_FULLY_DRAWN` |
| 확장 예정 트리거 | `ANR`, `OOM`, `COLD_START` |
| 처리 규모 | 주간 수백만 건 프로파일 (2026년 6월 Datadog 내부 데이터) |
| 게시일 | 2026년 6월 8일 |

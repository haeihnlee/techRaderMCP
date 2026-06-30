# Eclipsa Video: HDR That Looks Right on Every Screen

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/06/eclipsa-video-hdr-review.html
- **요약 일시**: 2026-06-30 09:11:56

---

## 🔑 핵심 요약
- Google이 화면마다 제각각인 **HDR** 렌더링 문제를 해결하는 새 표준 **`Eclipsa Video`**를 발표
- Apple·NBCUniversal과 공동 개발한 오픈 스펙 **`SMPTE ST 2094-50`** 기반으로, 프레임 단위 동적 밝기 가이드를 영상에 함께 전달
- **Android 17(API 37)**부터 플랫폼에 네이티브 내장, **Jetpack Media3/ExoPlayer**가 추가 설정 없이 자동 지원

---

## 📣 주요 발표 내용
- **`Eclipsa Video`**: 디스플레이별 추측 렌더링을 없애고, 영상이 **정확한 렌더링 가이드라인**을 직접 운반하는 HDR 표준
- 핵심 3가지 이점:
  - **일관된 기준선** — `HDR reference white`로 표준 텍스트·UI의 밝기 기준을 통일해 눈부심 방지
  - **적응형 헤드룸(Adaptive headroom)** — 화면별 밝기 한계에 맞춰 하이라이트를 동적으로 스케일링 (프리미엄 TV는 강렬하게, 모바일은 갑작스러운 과노출 방지)
  - **창작 의도 보존** — 정적 설정이 아닌 **프레임 단위(frame-by-frame)** 지시로 색·대비·분위기 그대로 전달
- **오픈 표준**이라 모든 앱 개발사·하드웨어 제조사가 자유롭게 통합 가능

---

## 💡 개발자 포인트
- **`Jetpack Media3`** 통합으로 **`ExoPlayer`**가 Eclipsa Video 메타데이터를 **추가 플레이어 설정 없이 자동 처리**
- 재생·캡처 구성은 공식 가이드를 참고해 앱에 적용
- 오픈소스 도구 **`HDR Explorer`**로 `SMPTE ST 2094-50` 메타데이터와 동적 게인 커브를 실시간 확인 가능

> ⚠️ **주의:** Eclipsa Video 재생·캡처는 **Android 17(API 37) 이상** + **Eclipsa Compliance 테스트를 통과한 HDR 디스플레이** 기기에서만 네이티브 지원됩니다. 하위 버전 기기에서는 동작을 보장할 수 없습니다.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| ---- | ---- |
| 발표일 | 2026년 6월 29일 |
| 지원 시작 | **Android 17 (API level 37)** 이상 |
| 기반 스펙 | `SMPTE ST 2094-50` (오픈, Google·Apple·NBCUniversal 공동 개발) |
| 기기 요건 | HDR 디스플레이 + Eclipsa Compliance 테스트 통과 |
| 현재 상태 | 롤아웃 진행 중 (지원 앱·기기 점진 확대) |

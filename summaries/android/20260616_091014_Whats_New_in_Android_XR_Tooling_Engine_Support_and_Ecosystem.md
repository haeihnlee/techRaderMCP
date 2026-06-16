# What's New in Android XR: Tooling, Engine Support, and Ecosystem Updates

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/06/what-is-new-android-xr.html
- **요약 일시**: 2026-06-16 09:10:14

---

## 🔑 핵심 요약
- **Android XR SDK Developer Preview 4** 출시 — 노트북에서 몰입형(immersive)·증강(augmented) 경험을 모두 타깃팅
- **Unreal Engine·Godot 공식 지원** 추가 (기존 Unity와 함께), 데스크톱 도구 **Android XR Engine Hub** 공개
- 물리적 기기 없이 **Android Studio XR 에뮬레이터**로 테스트 가능, **Samsung Galaxy XR**은 현재 출시 완료

---

## 📣 주요 발표 내용
- **Developer Preview 4 (DP4)**: 몰입형/증강 경험을 모두 타깃하는 라이브러리 포함, `Android Studio`에서 XR 에뮬레이터로 코드 반복 작업 가능
- **지능형 안경(eyewear) 확장**: 기존 모바일 앱을 보완형 증강 경험으로 전환하는 **`Jetpack Projected` 라이브러리** 제공
  - 새 **`Device Availability API`**는 표준 Android Lifecycle 상태와 연동 → 안경 착용 여부에 따라 앱 동작을 네이티브하게 적응
  - **`Android CLI` + display glasses skill**로 모바일 앱을 증강 경험으로 확장 (Jetpack Compose Glimmer 디자인 패턴 내장)
  - **`Jetpack Compose Glimmer`** 업데이트: 광학 시스루(optical see-through) 디스플레이 텍스트 가독성 최적화, 터치패드 최적화 내비게이션 컴포넌트
  - **NAVER Papago**가 모바일 경험을 디스플레이 글래스로 가져오는 사례 탐색 중
- **위치 기반 글로벌 몰입 경험**: 코어 perception 라이브러리에 Kotlin-first 아키텍처 업그레이드
  - **`ARCore for Jetpack XR`** + Google **VPS(Visual Positioning System)** 결합 → 고정밀 실세계 위치에 디지털 콘텐츠 앵커링 (Geospatial API 얼리 프리뷰)
- **엔진 지원 확대**: **Unreal Engine·Godot 공식 지원** + **Android XR Engine Hub**(Windows 데스크톱 도구)로 엔진 뷰포트 내 실시간 테스트
- **Android XR Developer Catalyst Program**: 디스플레이 글래스·wired XR 글래스 등 프리릴리스 하드웨어 및 Google Play 출시 가이드 제공, 현재 지원 접수 중

---

## 💡 개발자 포인트
- 하드웨어 없이도 **Android Studio XR 에뮬레이터**로 바로 개발 시작 가능 — 진입 장벽 낮음
- 기존 모바일 앱을 처음부터 새로 만들 필요 없이 **`Jetpack Projected`**로 증강 경험으로 확장하는 것이 권장 경로

> **`Device Availability API`가 표준 Android Lifecycle에 연동**되므로, 안경 착용/미착용 상태 전환을 별도 콜백이 아닌 익숙한 Lifecycle 패턴으로 처리할 수 있습니다.

- Unity에 묶이지 않고 **Unreal·Godot** 기존 워크플로우 그대로 Android XR로 포팅 가능
- 위치 기반 XR을 만든다면 **`ARCore for Jetpack XR` + VPS** 조합이 핵심 (단, Geospatial API는 아직 얼리 프리뷰)

---

## 📅 버전 / 출시 일정
| 항목 | 상태 |
| --- | --- |
| Android XR SDK | **Developer Preview 4** (현재 제공) |
| Samsung Galaxy XR | 현재 출시 완료 (available now) |
| Unreal Engine / Godot 지원 | 공식 지원 추가 |
| Geospatial API (wired XR glasses) | 얼리 프리뷰 (early preview) |
| Developer Catalyst Program | 지원 접수 중 |
| 발표일 | 2026년 6월 15일 (AWE / Google I/O 연계) |

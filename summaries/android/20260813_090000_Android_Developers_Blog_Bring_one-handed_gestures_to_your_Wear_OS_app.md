---
title: "Android Developers Blog: Bring one-handed gestures to your Wear OS app"
source_url: "https://android-developers.googleblog.com/2026/08/one-handed-gestures-wear-os.html"
conference: "Android"
saved_at: "2026-08-13T09:00:00"
---

## 🔑 핵심 요약
- **Wear OS 7**에서 개발자가 앱에 직접 원핸드 제스처를 통합할 수 있는 새 **Gestures framework** 및 공개 API 출시
- **Compose for Wear OS 1.7 beta**(`androidx.wear.compose:compose-material3:1.7.0-beta01`)부터 `Modifier.oneHandedGesture` 사용 가능
- **Spotify** 등 파트너사가 이미 API 채택 시작 — 화면 터치 없이 음악 재생/일시정지 구현

---

## 📣 주요 발표 내용
- **두 가지 제스처 타입** 지원:
  - `GestureAction.Primary` (Pixel Watch 기준: 더블 핀치): 현재 화면의 가장 중요한 액션 수행 (타이머 시작/정지, 통화 수락 등)
  - `GestureAction.Dismiss` (Pixel Watch 기준: 손목 돌리기): 기본적으로 시스템 Back에 매핑, 특정 케이스에서 재정의 가능
- `Modifier.oneHandedGesture` 를 기존 Composable에 추가하는 3단계 구현 절차:
  1. `rememberOneHandedGestureConfiguration(action = ...)` 으로 제스처 설정 정의
  2. `OneHandedGestureClickIndicatorState` 또는 `OneHandedGestureScrollIndicatorState` 로 인디케이터 상태 초기화
  3. `Modifier.oneHandedGesture(gestureConfiguration, onGestureAvailable, onGesture)` 적용
- `GestureAction.Primary`를 **스크롤**에도 활용 가능: `TransformingLazyColumn`, `ScalingLazyColumn`, `HorizontalPager`, `VerticalPager` 지원
- 제스처 힌트 컴포넌트 신규 제공:
  - `OneHandedGestureClickIndicator` — 버튼용
  - `OneHandedGestureScrollIndicator` — 스크롤용
  - `OneHandedGestureHorizontalPageIndicator` — HorizontalPager용
  - `OneHandedGestureVerticalPageIndicator` — VerticalPager용

---

## 💡 개발자 포인트
- 제스처 API는 **Wear OS 7 이상** 기기 + **Compose for Wear OS 1.7 beta** 이상이 모두 필요

> ⚠️ 현재 하드웨어 지원은 **Pixel Watch 3 이상**에 한정. OEM 확산은 Wear OS gesture framework 채택 여부에 달려 있음.

- `onGestureAvailable` 콜백으로 시스템이 제스처 준비를 알릴 때 `indicatorState.showIndicator()`를 호출해 힌트 애니메이션 표시
- `onGestureLabel` 파라미터로 접근성(TalkBack 등) 대응 레이블 설정 필수
- 제스처 힌트 노출 빈도는 사용자 설정에서 조절 가능 — 앱 레벨에서 강제하지 말 것

---

## 📅 버전 / 출시 일정

| 항목 | 버전 / 날짜 |
|---|---|
| Compose for Wear OS 첫 지원 버전 | `1.7.0-beta01` |
| 플랫폼 요구사항 | Wear OS 7 이상 |
| 하드웨어 지원 시작 | Pixel Watch 3 (Wear OS 6.1, 원핸드 제스처 첫 도입) |
| 블로그 게시일 | 2026-08-12 |

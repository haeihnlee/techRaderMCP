# Android Developers Blog: What's new in the Jetpack Compose August '26 release

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/08/jetpack-compose-august-2026-release.html
- **요약 일시**: 2026-08-13 09:08:19

---

## 🔑 핵심 요약
- **Jetpack Compose 1.12** (BOM `2026.08.00`) stable 릴리즈 — `MeshGradientPainter`, Wide Color Gamut(P3), HDR 렌더링 등 풍부한 그래픽 API 추가
- `compileSdk` **API 37** 및 **AGP 9.2.0 이상** 필수로 Breaking Change 발생
- TTID(첫 프레임 생성 시간)가 **Views 수준과 동등**해지는 성능 개선 달성

---

## 📣 주요 발표 내용

### 그래픽
- **`MeshGradientPainter`** 추가 — 멀티포인트 유기적 컬러 그라데이션 생성 가능
- **Wide Color Gamut (P3)** 및 **HDR 렌더링** 전파이프라인 지원 — 비sRGB 색공간 색상이 클램핑 없이 그대로 렌더링
- `GraphicsLayer` / `Modifier.graphicsLayer`에 `LayerOutsets` 추가 — 레이어 시각적 경계 확장 가능

### 런타임 최적화
- `SideEffect`에 **key 인자** 오버로드 추가 — 특정 key 변경 시만 실행, `LaunchedEffect` 대비 **최대 90% 빠름**
- `DeferredTargetAnimation` experimental 졸업

### 애니메이션
- **`DeferredAnimatedContent` / `DeferredAnimatedVisibility`** 추가 — 예측 뒤로 가기 등 2단계 전환 구현 가능
- 제스처 추적 중 애니메이션 속성(scale, offset) 수동 조작 후 velocity 포함 자동 핸드오프 지원
- `SharedContentConfig`에 `permitTransformDuringDeferredTransition` 플래그 추가

### 텍스트 & 입력
- **`BasicTextField` 리치텍스트 포맷** — `TextFieldBuffer.addStyle()`로 `SpanStyle` / `ParagraphStyle` 프로그래매틱 적용
- **`SelectionState` API** — `rememberSelectionState()`로 텍스트 선택 프로그래매틱 제어 (`selectAll()`, `clear()`, `select(TextRange)` 등)
- **Credential Manager 통합** — `credentialRequest` semantics 속성으로 패스키·저장 자격증명 프롬프트 직접 연동 (API 34+)
- `KeyboardType`에 `Date`, `Time`, `DateTime`, `SignedDecimal` 추가
- `BasicSecureTextField` 기본값 `TextObfuscationMode.System`으로 변경

### 레이아웃
- **Grid 레이아웃 Named Areas** (`@Experimental`) — 숫자 인덱스 대신 `area("header", ...)` 이름으로 컴포넌트 배치

### 테스트
- `hasPendingWork` — 클럭 진행 없이 UI 대기 작업 여부 수동 확인
- `runWithoutImplicitWait` — 수동 클럭 프레임 스텝 시 암묵적 동기화 비활성화로 테스트 속도 향상

---

## 💡 개발자 포인트

> **Breaking Change**: `compileSdk` **API 37** 필요, **AGP 9.2.0 이상** 필수. AGP 버전 미달 시 빌드 실패.

> **Deprecated**: `Modifier.onFirstVisible()` → `Modifier.onVisibilityChanged()`로 마이그레이션 필요. 더 정밀한 가시성 임계값 추적 제공.

- `SideEffect`는 `DisposableEffect`, `LaunchedEffect`보다 **먼저** 실행됨 — 기존 effect 마이그레이션 시 실행 순서 의존성 주의
- **Styles API**는 아직 experimental 유지 — 타입 안전성·커스텀 디자인 시스템 지원 기반 구축 중, **Breaking Change 예상**
- WCG 색상은 지원하지 않는 색공간(CieXyz, CieLab, Oklab) 또는 Android 9(API 28) 이하에서 자동으로 sRGB 폴백
- Semantics click listener가 이제 **메인 스레드**에서 호출되어야 함 — `SoundEffectOnInteraction` 추가에 따른 변경, 일부 테스트 케이스 영향 가능

---

## 📅 버전 / 출시 일정

| 항목 | 값 |
|---|---|
| Compose BOM | `2026.08.00` |
| Compose 버전 | 1.12 |
| 최소 `compileSdk` | API 37 |
| 최소 AGP | 9.2.0 |
| 출시일 | 2026년 8월 12일 |


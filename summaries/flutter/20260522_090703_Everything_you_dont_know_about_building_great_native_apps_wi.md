# Everything you don't know about building great native apps with Flutter

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=2z7U6GU7QwQ
- **요약 일시**: 2026-05-22 09:07:03

---

## 🔑 핵심 요약
- **Flutter**는 App Store/Google Play에서 **2위 앱 개발 SDK**이며, MAU 150만·앱 100만 개 이상 규모로 성장
- **Material/Cupertino**를 프레임워크에서 분리해 `material_ui`·`cupertino_ui` **first-party pub 패키지**로 이전 → 디자인 시스템 업데이트로 인한 UI 깨짐 방지
- Android 네이티브 뷰 임베딩을 위한 신규 **Hybrid Composition** 모드와 **Swift Package Manager** 기본 지원으로 네이티브 통합 품질·DX 동시 향상

---

## 📣 주요 발표 내용

### 1) 디자인 시스템 분리 (Material/Cupertino Decoupling)
- 중복 속성·로직을 **base class**로 이동, 스타일링 없는 **core widget** 신설
- 현재 단계 핵심 작업:
  - 프레임워크 내장 Material/Cupertino 구현을 **freeze**
  - `material_ui`, `cupertino_ui` **first-party pub 패키지**로 향후 개발 이전
- **Material Expressive**, **Apple Liquid Glass** 같은 신규 디자인 시스템을 서브클래싱 없이 구현 가능
- `shader`, **Metal**, **Vulkan** 등 저수준 그래픽 파이프라인 활용도 확대

### 2) Android Platform View 렌더링 진화
| 모드 | 특징 | 한계 |
|---|---|---|
| **Virtual Display** | offscreen buffer → Flutter texture | 텍스트 입력·접근성 깨짐 |
| **Hybrid Composition** | Android view 계층에 직접 배치 | GPU↔CPU round-trip로 성능 저하 |
| **Texture Layer Hybrid Composition** | native 그리기를 texture로 redirect | `SurfaceView` 미지원 |
| **Hybrid Composition (신규)** | OS 레벨 컴포지팅 (`AHardwareBuffer`, `SwapChain`, `SurfaceControl`) | Android API 34+ & Vulkan 필요 |

- 신규 모드는 **SurfaceView 지원**, 화면 찢김 없는 고성능 스크롤, 고품질 터치 입력을 모두 달성
- 향후 **기본 렌더링 모드**로 채택 예정 — Android Manifest 플래그로 opt-in 테스트 가능

### 3) iOS DX 개선 — Swift Package Manager
- **Flutter 3.44**부터 **SPM이 기본**, `CocoaPods`/`Ruby` 의존성 제거
- Flutter 플러그인이 Swift 패키지 생태계에 직접 참여 가능
- Xcode 내장이므로 **Ruby 설치 불필요**

### 4) Native Interop
- **JNIgen** (Android) — 실험적, 개발 활발
- iOS는 현재 Objective-C 브리지 경유 → **Swiftgen** 개발 중 (Swift → Dart 바인딩 직접 생성)

---

## 💡 개발자 포인트

> **Breaking Change 주의**: Material/Cupertino가 향후 pub 패키지로 이전됩니다. 현재 SDK 내장 위젯을 서브클래싱한 코드는 **마이그레이션 필요**.

- **Flutter 버전 업그레이드 시 UI가 무작위로 깨지던 문제**가 해결됨 — 디자인 시스템 버전을 의존성으로 명시 관리 가능
- 신규 **Hybrid Composition**은 SurfaceView 기반 네이티브 뷰(예: `WebView`, `MapView`, 비디오 플레이어)를 임베드할 때 즉시 도입 검토 권장
  - 적용 조건: **Android API 34+**, **Vulkan 지원 기기**
  - `AndroidManifest.xml` 또는 run command 플래그로 테스트 가능
- SPM 마이그레이션 전제조건:
  - **Flutter 3.24 이상**
  - **모든 플러그인이 SPM 마이그레이션 완료** 상태여야 함 (아니면 자동으로 CocoaPods fallback)
- 네이티브 코드 직접 호출이 필요하면 `jnigen`·`ffigen` 우선 검토, Swift 전용 API는 향후 `swiftgen` 출시 대기

---

## 📅 버전 / 출시 일정

| 항목 | 버전 / 시점 |
|---|---|
| **SPM 기본 채택** | Flutter **3.44** |
| **SPM 마이그레이션 가능 최소 버전** | Flutter **3.24** |
| **신규 Hybrid Composition (Android)** | Android **API 34+**, **Vulkan** 지원 기기 (현재 opt-in) |
| **Material/Cupertino pub 패키지 이전** | 진행 중 (multi-year effort, freeze 단계) |
| **swiftgen / jnigen / ffigen** | 실험적 (Experimental) |


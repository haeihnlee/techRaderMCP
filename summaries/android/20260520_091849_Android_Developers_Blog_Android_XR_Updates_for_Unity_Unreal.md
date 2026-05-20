# Android Developers Blog: Android XR Updates for Unity, Unreal, and Godot

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/android-xr-updates-unity-unreal-godot.html
- **요약 일시**: 2026-05-20 09:18:49

---

## 🔑 핵심 요약
- **Android XR**이 이제 **Unity**뿐 아니라 **Unreal Engine 5.6.1**과 **Godot 4.6.2+**까지 공식 지원
- **Android XR Engine Hub** (Windows) 출시 — 디바이스의 OpenXR 센서 데이터를 데스크톱 에디터로 실시간 스트리밍, APK 빌드 없이 Play Mode에서 즉시 테스트 가능
- Unity용 **AXRIF (Android XR Interaction Framework)** 개발자 프리뷰 공개 — 멀티모달 입력 전환·시선 보조 제스처·물리 기반 2D UI 인터랙션을 추상화

---

## 📣 주요 발표 내용

### Android XR Engine Hub (Windows)
- 디바이스 perception 데이터를 PC 에디터로 **실시간 스트리밍**하는 데스크톱 브리지
- 지원 OpenXR 확장:
  - `XR_EXT_hand_tracking` & `hand_interaction` — 26포인트 손 메시 스트리밍
  - `XR_EXT_eye_gaze_interaction` — 시선 추적 데이터 가상화
  - `XR_EXT_palm_pose` & `XR_EXT_uuid` — 정밀 추적·영구 객체 ID
  - `XR_ANDROID` 벤더 확장 — Eye/Face Tracking, Passthrough, Trackables (평면 감지·hit testing)

### Unreal Engine 지원 (Developer Preview)
- 대상 버전 **Unreal Engine 5.6.1**
- **Android XR vendor plugin for Unreal** 통해 손 추적·얼굴 추적·씬 이해(평면 감지, depth) 접근
- **Blueprints** 또는 **C++** 양쪽 지원

### Godot 지원 (정식)
- **Godot Foundation** 및 **W4 Games**와 협력하여 Godot 4.6.2+ 공식 지원
- **Godot OpenXR Vendors plugin 5.1** 필요 — scene meshing, dynamic resolution, light estimation 등 활성화
- W4가 이식한 `MoAT`, `Expedition to Blobotopia`는 이미 Google Play에서 라이브

### Unity 업데이트
- **Unity OpenXR: Android XR 1.13** 패키지 (Unity 6.5 Beta 대응)
- **Application SpaceWarp**이 uGUI 및 TextMeshPro까지 확장
- Android XR Extensions v1.3.1 신규 기능:
  - `android.software.xr.api.SPATIAL` manifest 태그를 `XRSessionFeature`에서 직접 관리
  - `TryGetFineEyePoses` 메서드로 고정밀 Fine Eye Poses 제공
  - Unity Editor PlayMode 내 **Direct Preview** 지원 (Windows 전용)

### AXRIF (Android XR Interaction Framework) for Unity
- Unstyled·opinionated 입력 툴킷, 시스템 기본 인터랙션과 일관성 보장
- 핵심 기능 3가지:
  - **자동 멀티모달 입력 전환** — 6DoF 컨트롤러, 3D 마우스, 손 추적, 시선 간 전환 상태머신 관리
  - **Gaze-Assisted Gesture** — 시선 타겟팅 + 핀치 선택 등 원거리 정밀 인터랙션
  - **Physics-Based 2D UI Interaction** — 플로팅 패널 위 poke·swipe 제스처

---

## 💡 개발자 포인트

> ⚠️ **Breaking Change**: Unity의 **Android XR (Extensions): Hand Mesh**가 제거됨. 이제 **extensions 패키지의 통합 Hand Mesh Data**를 사용해야 함.

- **반복 속도 대폭 단축**: Engine Hub의 Direct Preview로 eye-tracking·spatial mapping 변경 시마다 풀 APK 빌드/설치를 반복할 필요가 없어짐 — 가장 큰 생산성 이득
- **엔진 선택권 확대**: 기존 Unity 종속에서 벗어나 Unreal·Godot으로도 프로덕션급 XR 앱 출시 가능 (Godot의 MoAT 사례가 증명)
- **OpenXR 표준 기반 통합**: 벤더 플러그인을 함께 쓰면 표준 + Android XR 전용 기능을 모두 활용 가능
- **AXRIF 채택 시 이점**: 시스템 기본 동작과 자동 일치하므로 멀티모달 입력 처리 구현 부담이 크게 감소 — 직접 구현 대신 프레임워크 채택 권장
- **Spatial API 타깃 레벨 선언**이 `XRSessionFeature` 설정으로 단순화되어 manifest 직접 편집 부담 감소

---

## 📅 버전 / 출시 일정

| 항목 | 버전 / 일정 |
|---|---|
| Unreal Engine 대상 | **5.6.1** (Developer Preview) |
| Godot 대상 | **4.6.2 이상** |
| Godot OpenXR Vendors plugin | **5.1** |
| Unity OpenXR: Android XR 패키지 | **1.13** (Unity 6.5 Beta) |
| Android XR Extensions for Unity | **v1.3.1** |
| Unity 6.5 정식 | **2026년 여름 예정** |
| AXRIF | Developer Preview (Unity) |
| Engine Hub 지원 OS | Windows 전용 |
| 발표일 | 2026-05-19 (Google I/O 2026) |


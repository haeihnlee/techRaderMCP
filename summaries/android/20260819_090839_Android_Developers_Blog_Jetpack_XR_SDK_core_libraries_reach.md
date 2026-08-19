# Android Developers Blog: Jetpack XR SDK core libraries reach beta: The next milestone for Android XR

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/08/jetpack-xr-sdk-core-libraries-beta.html
- **요약 일시**: 2026-08-19 09:08:39

---

## 🔑 핵심 요약
- **Jetpack XR SDK** 핵심 라이브러리 3종(`SceneCore`, `ARCore for Jetpack XR`, `XR Runtime`)이 **Beta**에 도달
- `Jetpack Compose for XR`는 곧 Beta 예정 (현재 alpha17)
- 개발자 미리보기 피드백을 반영한 API 안정화로 **프로덕션 워크플로우 통합 권장** 시점

---

## 📣 주요 발표 내용
- **`Jetpack SceneCore` Beta**: Android XR 씬 그래프 구성, 3D 모델·공간 오디오·Entity-Component 시스템 지원
- **`ARCore for Jetpack XR` Beta**: 깊이 추정(Depth Estimation), 영구 앵커, 히트 테스팅, 평면 인식 등 AR 인지 기능 제공
- **`XR Runtime` Beta**: 기기 라이프사이클·세션 생성·시스템 설정 처리하는 런타임 기반 라이브러리
- **테스트 지원 확장**: 공간 오디오, XR 디바이스, 세션 설정에 대한 신규 테스트 API 추가
- **Kotlin 코루틴 지원**: `Session.create`가 suspend 함수로 변경
- **API 명칭 정리**: `AnchorEntity` → `AnchorSpace`로 리네임, `ActivitySpace`와 `AnchorSpace` 모두 공통 `SpaceEntity` 클래스 상속

---

## 💡 개발자 포인트

**Gradle 의존성 추가 예시:**
```kotlin
dependencies {
    implementation("androidx.xr.scenecore:scenecore:1.0.0-beta02")
    implementation("androidx.xr.arcore:arcore:1.0.0-beta02")
    implementation("androidx.xr.runtime:runtime:1.0.0-beta02")
    implementation("androidx.xr.compose:compose:1.0.0-alpha17")
}
```

> **Breaking Change**: `AnchorEntity`가 `AnchorSpace`로 리네임되었으며, `Session.create`가 suspend 함수로 변경됨. 기존 코드 수정 필요.

- 테스트는 **Samsung Galaxy XR** 또는 **Android XR Emulator**에서 가능
- 기존 2D 앱 포팅과 신규 3D XR 앱 모두 지원

---

## 📅 버전 / 출시 일정

| 라이브러리 | 버전 | 상태 |
|---|---|---|
| `androidx.xr.scenecore:scenecore` | 1.0.0-beta02 | **Beta** |
| `androidx.xr.arcore:arcore` | 1.0.0-beta02 | **Beta** |
| `androidx.xr.runtime:runtime` | 1.0.0-beta02 | **Beta** |
| `androidx.xr.compose:compose` | 1.0.0-alpha17 | Alpha (Beta 예정) |

발표일: 2026년 8월 18일

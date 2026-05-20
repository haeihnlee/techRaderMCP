# Android Developers Blog: Updates to the Android XR SDK: Introducing Developer Preview 4

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/android-xr-sdk-developer-preview-4-updates.html
- **요약 일시**: 2026-05-20 09:17:46

---

## 🔑 핵심 요약
- **Android XR SDK Developer Preview 4** 출시, 헤드셋·유선 XR 글래스·인텔리전트 안경을 아우르는 **크로스 디바이스 개발** 통합 강화
- 폼팩터 명칭 변경: AI glasses → **audio glasses**, display AI glasses → **display glasses**
- 핵심 라이브러리 (`XR Runtime`, `Jetpack SceneCore`, `ARCore for Jetpack XR`)가 곧 **Beta**로 승격 예정

---

## 📣 주요 발표 내용

### Audio / Display Glasses 용 증강 경험
- **Jetpack Projected**: `Device Availability API` 추가 — 착용 상태와 연결 신호를 표준 `Lifecycle.State` 값(`STARTED`/`CREATED`/`DESTROYED`)으로 통합
- `ProjectedTestRule` API 추가 — `projected-testing` 아티팩트로 보일러플레이트 없이 단위 테스트 환경 자동 셋업
- **Jetpack Compose Glimmer** UI 라이브러리에 **Google Sans Flex** 폰트 적용 (광학 시스루 디스플레이 가독성 향상)
- 새 컴포넌트: `Stacks` (터치패드 최적화 그룹), `Title Chips` (콘텐츠 카드 분류·컨텍스트)

### XR 헤드셋 / 유선 XR 글래스 용 몰입형 경험
- **Jetpack SceneCore**: `GltfModelNode`로 3D 모델의 pose·머티리얼·텍스처·애니메이션을 노드 단위로 세밀 제어
- **Custom Meshes** (experimental) — `CustomMesh.BuilderFromMeshData`로 런타임 지오메트리 프로그래매틱 생성
- **Compose for XR**: `SpatialGltfModel` / `SpatialGltfModelState`로 glTF 네이티브 지원, 노드·애니메이션 직접 접근
- **ARCore for Jetpack XR**: 유선 XR 글래스용 **Geospatial API** 프리뷰 — VPS와 `Gemini Live API` 결합으로 **87개국** 실세계 위치 기반 고정밀 앵커링

### 게임 엔진 지원 확대
- **Unreal Engine**, **Godot** 공식 지원 추가
- Unity 가속화 도구 + **Android XR Interaction Framework** 출시
- **Android XR Engine Hub** 신규 — 선호 엔진에서 직접 실행 가능

---

## 💡 개발자 포인트

> ⚠️ **Breaking Change**: 레거시 `Guava` / `RxJava3` 패키지가 제거되고 **Kotlin-first 아키텍처**로 전환됩니다. 기존 Jetpack XR 코드 마이그레이션 필요.

> 📌 폼팩터 명칭이 **AI glasses → audio glasses**, **display AI glasses → display glasses**로 변경되었습니다. 문서·API 참조 시 신규 명명 사용.

- Beta 승격 전 마지막 Preview 단계 — API 안정성 검증 및 피드백 반영 적기
- `Device Availability API`는 표준 `Lifecycle.State`를 재사용하므로 기존 안드로이드 개발자에게 학습 곡선이 낮음
- Custom Meshes는 **experimental** 상태 — 프로덕션 코드에 도입 시 향후 API 변경 가능성 고려
- VPS + Gemini Live API 조합으로 AI 가이드 워킹투어 등 **위치+컨텍스트 인지 경험** 구현 가능
- **Android XR Developer Catalyst Program** 지원 시 audio/display glasses 프로토타입 및 **XREAL Project Aura** 사전 액세스 가능

---

## 📅 버전 / 출시 일정

| 항목 | 상태 | 비고 |
|------|------|------|
| Android XR SDK | **Developer Preview 4** | 2026-05-19 발표 |
| `projected-testing` | `1.0.0-alpha07` | ProjectedTestRule 제공 |
| XR Runtime / Jetpack SceneCore / ARCore for Jetpack XR | 곧 **Beta** 승격 예정 | 시점 미공개 |
| Custom Meshes | **Experimental** | Preview 4 포함 |
| Geospatial API (유선 XR 글래스) | **Early Preview** | 87개국 지원 |
| Android XR 디바이스 정식 출시 | **2026년 말 예정** (later this year) | - |


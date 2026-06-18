# Building a Mixed-Reality Tour Guide with Android XR, the Geospatial API, and Gemini

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/06/android-xr-geospatial-api-gemini.html
- **요약 일시**: 2026-06-18 09:06:11

---

## 🔑 핵심 요약
- **Geospatial API**가 `ARCore for Jetpack XR`에 **프리뷰**로 추가되어, Google **VPS**(Visual Positioning System)로 디지털 콘텐츠를 현실 세계에 **서브미터(sub-meter) 정확도**로 앵커링 가능
- Geospatial API + **Gemini API**(Firebase AI Logic) + **Google Maps Grounding** + **Jetpack XR SDK**를 결합해 핸즈프리 몰입형 워킹 투어 데모 **XR Geospatial Tour** 구현
- LLM의 좌표 환각(hallucination)을 **Google Maps Grounding**으로 보정하고, **Gemini 2.5 TTS**로 음성 가이드까지 제공

---

## 📣 주요 발표 내용
- **위치 측위**: `geospatial.createGeospatialPoseFromPose()`로 `GeospatialPose`(위도·경도·heading)를 GPS보다 정밀하게 획득
- 정확도 확보를 위해 `horizontalAccuracy`·`orientationYawAccuracy`를 임계값까지 모니터링 (실내·미인식 지역이면 "야외 공공장소로 이동" 안내)
- **투어 생성**: `gemini-3.5-flash` 모델에 `Tool.googleMaps()`와 `responseSchema`(구조화 JSON)를 지정해, 사용자 좌표 기반의 도보 투어 3개 생성
- **음성 가이드**: `gemini-2.5-flash-tts` 모델에 `ResponseModality.AUDIO`를 설정해 텍스트 대신 오디오 데이터 직접 반환, `InlineDataPart`에서 raw 오디오 바이트 추출
- **3D 렌더링**: **Jetpack Compose for XR**로 `InfoSphere` 컴포저블 구현 — `SpatialBox`, `SceneCoreEntity`, `GltfModelEntity`로 3D 오브 배치, `InteractableComponent`로 탭 인터랙션, `AnimatedSpatialVisibility`로 2D 패널 전환

---

## 💡 개발자 포인트
- **VPS 기반 정밀 측위**: 단순 GPS가 아닌 컴퓨터 비전 기반 VPS로 3D 웨이포인트를 실제 지형에 정렬 가능 → 월드 스케일 AR 경험의 진입 장벽이 크게 낮아짐
- **좌표 환각 대응이 핵심**: LLM은 풍부한 설명 생성엔 강하지만 정확한 위경도를 환각할 수 있음

> ⚠️ 정확한 좌표가 필요한 기능에는 LLM 출력을 그대로 신뢰하지 말고, 반드시 **Google Maps Grounding**으로 실제 장소 데이터에 그라운딩할 것.

- Firebase AI Logic 한 백엔드에서 텍스트 생성(`gemini-3.5-flash`)·TTS(`gemini-2.5-flash-tts`)를 모두 처리 → 멀티모달 파이프라인 단순화
- 2D Compose UI와 3D SceneCore 엔티티를 `SpatialBox` 안에서 함께 배치 가능해, 기존 Compose 지식을 XR로 자연스럽게 확장

> 📌 Geospatial API는 현재 **프리뷰** 단계이며, 지원 지역(supported areas)에서만 정확도가 보장됨.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| 발표일 | 2026-06-17 (Google I/O 2026 연계 발표) |
| Geospatial API (ARCore for Jetpack XR) | **프리뷰** 제공 중 |
| 텍스트 생성 모델 | `gemini-3.5-flash` |
| TTS 모델 | `gemini-2.5-flash-tts` |
| 디바이스 | XREAL Project Aura (개발 중) |
| Android XR Developer Catalyst Program | **신청 접수 시작**, 향후 수개월 내 devkit 제공 |


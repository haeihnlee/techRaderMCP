# Experimental hybrid inference and new Gemini models for Android

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/04/Hybrid-inference-and-new-AI-models-are-coming-to-Android.html
- **요약 일시**: 2026-04-18 09:03:27

---

## 🔑 핵심 요약
- **Firebase API for Hybrid Inference** 출시로 온디바이스(Gemini Nano)와 클라우드 추론을 단일 API로 통합 제어 가능
- 이미지 생성 모델 **Nano Banana Pro / Nano Banana 2** 신규 출시로 고품질·고속 이미지 생성 지원
- **Gemini 3.1 Flash-Lite** 프리뷰 공개로 더 고도화된 유즈케이스를 낮은 레이턴시로 처리 가능

---

## 📣 주요 발표 내용

### 🔀 Hybrid Inference (실험적)
- `firebase-ai-ondevice` 의존성 추가만으로 온디바이스 + 클라우드 추론 통합 사용 가능
- `InferenceMode.PREFER_ON_DEVICE` : 기기에 Gemini Nano 없으면 클라우드로 폴백
- `InferenceMode.PREFER_IN_CLOUD` : 오프라인 상태면 온디바이스로 폴백
- 온디바이스 추론은 내부적으로 **ML Kit Prompt API** 사용
- 클라우드 추론은 **Vertex AI** 및 **Developer API** 모두 지원
- AI Sample Catalog에 **Hybrid Inference 샘플** 신규 추가 (리뷰 생성 + 다국어 번역 데모)

### 🖼️ 신규 이미지 생성 모델 (Nano Banana 시리즈)

| 모델명 | 공식 명칭 | 특징 |
|---|---|---|
| **Nano Banana Pro** | Gemini 3 Pro Image | 고품질 에셋 생성, 특정 폰트/필기체 텍스트 렌더링 |
| **Nano Banana 2** | Gemini 3.1 Flash Image | 고속·대용량 처리, 인포그래픽·스티커·일러스트 등 범용 |

- **Firebase AI Logic SDK**를 통해 바로 통합 가능
- **Magic Selfie 샘플** 업데이트 → Nano Banana 2로 셀피 배경 교체 기능 구현

### ⚡ Gemini 3.1 Flash-Lite
- **Gemini Flash-Lite** 패밀리 최신 버전, 현재 **프리뷰** 단계
- 앱 내 메시지 번역, 음식 사진으로 레시피 생성 등 실용적 유즈케이스에 적합
- **Gemini 2.5 Flash-Lite**에 준하는 레이턴시 제공

---

## 💡 개발자 포인트

### 의존성 추가 방법
```kotlin
dependencies {
    implementation("com.google.firebase:firebase-ai:17.11.0")
    implementation("com.google.firebase:firebase-ai-ondevice:16.0.0-beta01")
}
```

### Hybrid Inference 초기화 예시
```kotlin
val model = Firebase.ai(backend = GenerativeBackend.googleAI())
    .generativeModel(
        modelName = "gemini-3.1-flash-lite",
        onDeviceConfig = OnDeviceConfig(
            mode = InferenceMode.PREFER_ON_DEVICE
        )
    )
val response = model.generateContent(prompt)
```

> ⚠️ **현재 온디바이스 모델 제한사항**
> 온디바이스 모델은 **단일 턴 텍스트 생성**에만 특화되어 있으며,
> 입력은 **텍스트** 또는 **단일 Bitmap 이미지**만 지원됩니다.
> 멀티턴 대화나 복잡한 입력 형식은 현재 미지원 — 반드시 [공식 limitations 문서](https://firebase.google.com) 확인 필요.

> 🧪 **Hybrid Inference API는 실험적(Experimental) 상태**입니다.
> 프로덕션 적용 전 충분한 검증이 필요하며, 향후 라우팅 로직이 변경될 수 있습니다.

---

## 📅 버전 / 출시 일정

| 항목 | 버전 / 상태 | 발표일 |
|---|---|---|
| `firebase-ai` | `17.11.0` | 2026년 4월 17일 |
| `firebase-ai-ondevice` | `16.0.0-beta01` | 2026년 4월 17일 |
| **Nano Banana Pro** (Gemini 3 Pro Image) | GA | 수 주 전 출시 |
| **Nano Banana 2** (Gemini 3.1 Flash Image) | GA | 수 주 전 출시 |
| **Gemini 3.1 Flash-Lite** | Preview | 2026년 4월 17일 |

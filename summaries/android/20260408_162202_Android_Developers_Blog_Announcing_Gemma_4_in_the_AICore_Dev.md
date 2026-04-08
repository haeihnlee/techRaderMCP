# Android Developers Blog: Announcing Gemma 4 in the AICore Developer Preview

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/04/AI-Core-Developer-Preview.html
- **요약 일시**: 2026-04-08 16:22:02

---

## 핵심 요약 (3줄)
- Google이 최신 온디바이스 AI 모델 **Gemma 4**를 AICore Developer Preview를 통해 공개했습니다.
- Gemma 4는 이전 버전 대비 최대 **4배 빠르고 60% 배터리 절약**, 140개 이상 언어 및 멀티모달(텍스트·이미지·오디오) 지원합니다.
- Gemma 4는 향후 출시될 **Gemini Nano 4의 기반 모델**이므로, 지금 작성한 코드가 Gemini Nano 4 탑재 기기에서도 자동 호환됩니다.

---

## 주요 발표 내용

- **Gemma 4 두 가지 사이즈 제공**
  - `E4B`: 고성능 추론 및 복잡한 작업에 최적화
  - `E2B`: E4B 대비 **3배 빠른** 속도, 저지연 최적화

- **향상된 기능 영역**
  - **추론(Reasoning)**: Chain-of-thought 및 조건문 처리 품질 향상 (예: 커뮤니티 가이드라인 위반 판단)
  - **수학(Math)**: 수치 계산 및 수학적 질의 정확도 향상
  - **시간 이해(Time Understanding)**: 캘린더, 알람, 리마인더 관련 시간 추론 능력 강화
  - **이미지 이해(Image Understanding)**: OCR, 차트 분석, 필기 인식 정확도 향상

- **140개 이상 언어 네이티브 지원** → 글로벌 다국어 앱에 적합

- **ML Kit Prompt API 업데이트**: 모델 버전(`E2B`/`E4B`) 직접 지정 가능
  ```kotlin
  modelConfig = ModelConfig {
      releaseTrack = ModelReleaseTrack.PREVIEW
      preference = ModelPreference.FULL // 또는 FAST
  }
  ```

- **향후 Developer Preview 기간 중 추가 예정 기능**
  - Tool Calling
  - Structured Output
  - System Prompts
  - Thinking Mode (in Prompt API)

---

## 개발자에게 중요한 포인트

- **코드 호환성 보장**: Gemma 4 기반으로 작성한 코드는 연내 출시 예정인 Gemini Nano 4 탑재 기기에서 **별도 수정 없이 동작** → 지금 개발 시작해도 리스크 없음

- **모델 타겟 지정 API 신규 도입**: `ModelReleaseTrack.PREVIEW` + `ModelPreference.FULL/FAST` 조합으로 테스트 시 원하는 모델 변형 선택 가능

- **`checkStatus()` 호출 필수**: 모델 다운로드 여부 및 사용 가능 여부를 반드시 확인 후 추론 호출 권장

- **지원 기기 제한 (Preview 기간)**
  - AICore 지원 기기: Google, MediaTek, Qualcomm AI 가속기 활용
  - 비지원 기기: CPU로 동작 (최종 성능과 다를 수 있음)
  - 비지원 기기 대안: **AI Edge Gallery 앱**으로 테스트 가능

- **Android Studio 연동**: 프롬프트 테스트 및 ML Kit 구현을 Android Studio에서 바로 진행 가능, 코드 없이 Developer Preview UI에서 먼저 체험 가능

- **시작 방법 요약**
  1. AICore Developer Preview 신청(opt-in)
  2. 테스트 기기에 Gemma 4 모델 다운로드
  3. ML Kit 구현 업데이트 후 Android Studio에서 빌드

---

## 출시 일정 / 버전 정보

| 항목 | 내용 |
|------|------|
| 발표일 | 2026년 4월 2일 |
| 현재 상태 | **AICore Developer Preview** (정식 출시 전) |
| Gemini Nano 4 탑재 기기 출시 | **2026년 내 예정** (구체적 일정 미공개) |
| 추가 기능 지원 (Tool Calling 등) | Preview 기간 중 순차 업데이트 예정 |
| 모델 버전 | Gemma 4 E2B (Fast) / E4B (Full) |

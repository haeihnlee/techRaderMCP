# Android Developers Blog: Android Studio supports Gemma 4: our most capable local model for agentic coding

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/04/android-studio-supports-gemma-4-local.html
- **요약 일시**: 2026-04-08 16:21:17

---

## 핵심 요약 (3줄)
- Android Studio에서 로컬 AI 모델 **Gemma 4**를 공식 지원하며, 인터넷 없이도 AI 코딩 어시스턴트를 사용할 수 있게 됨
- Gemma 4는 Android 개발에 특화되어 훈련된 모델로, Agent Mode에서 멀티스텝 코딩 작업(기능 설계, 리팩토링, 빌드 오류 수정 등)을 수행 가능
- 코드가 로컬 머신에서만 처리되어 **프라이버시 보호 및 비용 절감** 효과를 동시에 제공

## 주요 발표 내용
- **Gemma 4 로컬 모델 지원**: Android Studio에서 Gemma 4를 AI 코딩 어시스턴트로 선택 가능
- **Agent Mode 통합**: 자율적인 멀티스텝 작업 수행 지원
  - 새 기능/앱 전체 생성 (예: "calculator 앱 만들어줘")
  - 코드베이스 전체 리팩토링 (예: 하드코딩 문자열 → strings.xml 마이그레이션)
  - 빌드 오류 자동 감지 및 반복 수정
- **3가지 모델 크기** 제공으로 하드웨어 사양에 따라 선택 가능:
  | 모델 | 필요 RAM | 저장공간 |
  |------|---------|---------|
  | Gemma E2B | 8GB | 2GB |
  | Gemma E4B | 12GB | 4GB |
  | Gemma 26B MoE | 24GB | 17GB |
- **LM Studio / Ollama** 연동을 통해 로컬 모델 실행

## 개발자에게 중요한 포인트
- **프라이버시**: 모든 Agent Mode 요청이 로컬에서 처리되므로 코드가 외부 서버에 전송되지 않음 → 보안이 중요한 기업 환경에 적합
- **비용 없음**: API 키나 쿼터 소모 없이 복잡한 에이전틱 워크플로우 실행 가능
- **오프라인 사용 가능**: 인터넷 연결 없이도 AI 코딩 지원
- **Android 개발 특화**: Kotlin, Jetpack Compose 등 Android 모범 사례를 인식하여 코드 생성
- **권장 모델**: 일반 Android 앱 개발자에게는 **Gemma 26B MoE** 권장 (단, RAM 24GB 필요)
- **설정 방법**: Settings > Tools > AI > Model Providers에서 LM Studio 또는 Ollama 인스턴스 추가 후 Gemma 4 모델 다운로드

## 출시 일정 / 버전 정보
- **발표일**: 2026년 4월 2일
- 최신 버전의 Android Studio 설치 필요 (구체적인 버전명 미기재)
- Ollama 및 LM Studio를 통해 현재 즉시 다운로드 및 사용 가능

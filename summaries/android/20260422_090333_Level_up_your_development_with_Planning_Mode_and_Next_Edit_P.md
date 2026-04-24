# Level up your development with Planning Mode and Next Edit Prediction in Android Studio Panda 4

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/04/android-studio-panda-4-planning-mode-next-edit-prediction.html
- **요약 일시**: 2026-04-22 09:03:33

---

## 🔑 핵심 요약
- **Android Studio Panda 4** 가 안정(Stable) 버전으로 출시되어 프로덕션 사용 가능
- AI 에이전트가 코드를 작성하기 전 **계획 단계**를 먼저 거치는 **Planning Mode** 도입
- 현재 커서 위치와 무관하게 다음 수정 위치를 예측하는 **Next Edit Prediction(NEP)** 추가

---

## 📣 주요 발표 내용

### 🗺️ Planning Mode (계획 모드)
- 에이전트가 코드 작성 전 **멀티 스테이지 추론 프로세스**로 구현 계획을 먼저 수립
- 대화 모드를 `"Planning"` 으로 전환 후 프롬프트를 입력하면 활성화
- 개발자가 구현 계획에 **코멘트를 추가** → `Submit Comments` → 에이전트가 계획 수정
- 실행 중 **Task List** 아티팩트로 진행 상황을 단계별로 추적 가능
- 작업 완료 후 **Walkthrough** 아티팩트로 변경 사항 요약 제공

### 🔮 Next Edit Prediction (NEP)
- 최근 편집 패턴을 분석하여 **커서 위치가 아닌 다른 위치의 다음 수정**을 예측·제안
- 예: 함수 파라미터 추가 → 해당 함수의 **모든 호출부 수정 위치** 자동 제안
- **단일 키 입력**으로 멀티 위치 제안을 수락하여 흐름 상태(Flow State) 유지

### 🤖 Gemini API Starter Template
- `File > New > New Project` 에서 `Gemini API Starter` 템플릿 선택으로 즉시 시작
- **Firebase AI Logic** 를 활용하여 클라이언트 코드에 API 키 임베드 불필요
- **Firebase 통합 자동화**로 백엔드 설정 없이 Gemini 모델 연결
- `텍스트`, `이미지`, `비디오`, `오디오` 멀티모달 입력 지원
- 프로토타입 → 글로벌 서비스까지 재설계 없이 확장 가능한 **프로덕션 레디 아키텍처**

### 🌐 Agent Web Search
- **Android Knowledge Base** 외에 Google 웹 검색으로 외부 라이브러리 최신 정보 조회
- 지식 공백 감지 시 **자동으로 웹 검색 트리거**
- 프롬프트에 `"search the web for..."` 포함 시 **수동으로 웹 검색 요청** 가능
- **Coil**, **Koin**, **Moshi** 등 서드파티 라이브러리 최신 설정 가이드 실시간 조회

---

## 💡 개발자 포인트

- **NEP**는 데이터 클래스 수정, 컨스트럭터 변경, Composable 업데이트 등 **연쇄적인 수정이 필요한 패턴**에서 생산성을 크게 향상시킴
- **Planning Mode**는 규모가 크거나 아키텍처 정밀도가 요구되는 작업에 특히 유효 — 단순 작업보다 **복잡한 장기 프로젝트**에 활용 권장

> ⚠️ **Gemini API Starter 템플릿 사용 시 주의:** API 키를 클라이언트 코드에 직접 삽입하지 말 것. 반드시 **Firebase AI Logic**를 통해 키 관리를 위임해야 보안이 보장됩니다.

- **Agent Web Search**는 별도 설정 없이 자동 동작하나, 민감한 내부 코드/정책이 있는 환경에서는 에이전트의 외부 쿼리 범위를 별도 검토 필요

---

## 📅 버전 / 출시 일정

| 버전 | 상태 | 출시일 | 주요 기능 |
|---|---|---|---|
| **Android Studio Panda 2** | Stable | - | AI 기반 New Project 플로우, **Version Upgrade Assistant** |
| **Android Studio Panda 3** | Stable | - | **Agent Skills** (`.skills` 디렉토리), **Agent Permissions**, Car App 템플릿 |
| **Android Studio Panda 4** | ✅ Stable | **2026년 4월 21일** | **Planning Mode**, **NEP**, Gemini API 스타터 템플릿, Agent Web Search |

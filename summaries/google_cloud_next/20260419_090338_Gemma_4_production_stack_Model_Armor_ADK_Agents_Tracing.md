# Gemma 4 production stack: Model Armor, ADK Agents, Tracing

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=7wENq-LMHgQ
- **요약 일시**: 2026-04-19 09:03:38

---

## 🔑 핵심 요약
- **Gemma 4** 모델을 프로덕션 환경에서 안전하게 운영하기 위한 **보안·관측성·에이전트** 스택 구성 방법 소개
- **Model Armor**로 프롬프트 인젝션·탈옥 공격을 차단하고, **ADK**(Agent Development Kit) + **LiteLLM**으로 모델 무관 에이전트 구축
- **Cloud Trace** 및 GPU 메트릭 수집으로 프로덕션 서빙 비용·성능 모니터링 구현

---

## 📣 주요 발표 내용

### 🔒 보안 / Model Armor
- 🛡️ **Model Armor**: 프롬프트 인젝션, 탈옥(Jailbreaking), 악성 입력, **PII** 유출을 탐지·차단하는 Google Cloud 전용 서비스
- 🔌 사용 방식 3가지:
  - `Python SDK` 직접 호출
  - `Model Armor REST API` 호출
  - **Application Load Balancer**의 `Service Extension`으로 연결 → 백엔드 도달 전 자동 필터링
- 🔗 **ADK Callback**과 연동 가능:
  - `before_agent_callback` — 에이전트 호출 전 악성 입력 검사
  - `after_model_callback` — 모델 응답에서 민감 데이터 유출 검사

---

### ⚖️ 로드 밸런서 & 트래픽 라우팅
- 🌐 **Regional External Application Load Balancer** 1개로 두 백엔드(`vLLM`, `Ollama`) 단일 엔드포인트 관리
- 🗺️ `URL Map` 기반 라우팅 → 호출 경로에 따라 서비스 분기
- 📦 백엔드 표현 단위: **NEG**(Network Endpoint Group), Cloud Run 연동 시 타입은 `serverless`
- 🔗 `Service Extension`을 통해 로드 밸런서에 **Model Armor** 플러그인 연결

---

### 🤖 ADK 에이전트 + LiteLLM
- 🧩 **ADK**(Agent Development Kit)는 **모델 무관(model-agnostic)** 프레임워크
- 💡 **LiteLLM**을 브릿지로 사용 → Gemini 외 **Gemma 4** 등 오픈 모델도 ADK에서 구동 가능
- 🚀 완성된 에이전트는 **Cloud Run**에 배포 (`cloud build` 자동화)

---

### 📊 관측성 / 메트릭
- 📈 수집 대상 핵심 메트릭:

| 메트릭 | 용도 |
|---|---|
| **Time to First Token (TTFT)** | 응답 체감 속도 |
| **GPU Utilization** | 인프라 비용 최적화 |
| **Request per Second (RPS)** | 처리량 모니터링 |
| **Request Latency** | SLA 관리 |
| **Output Tokens per Request** | 토큰 비용 추적 |

- 🔍 **Cloud Trace**를 통해 에이전트 전체 파이프라인 트레이싱

---

## 💡 개발자 포인트

> ⚠️ **GPU 크레딧 미제공**: 이번 핸즈온 랩은 GPU 리소스가 필요하므로 무료 GCP 크레딧이 제공되지 않습니다. 실습 시 별도 과금 주의.

> ⚠️ **Model Armor는 Load Balancer 없이도 사용 가능**: 단일 엔드포인트 구조라도 `Python SDK` 또는 `API` 직접 호출로 ADK 콜백에 통합할 수 있습니다. 로드 밸런서 도입이 필수 조건이 아님.

- **NEG 타입 선택 주의**: Cloud Run 백엔드 연결 시 반드시 `--network-endpoint-type=serverless` 지정 필요
- **LiteLLM 연동 패턴**: ADK에서 Gemma 4 사용 시 `LiteLLM` 래퍼를 통해 Cloud Run에 배포된 Ollama/vLLM 엔드포인트를 가리키도록 설정
- **콜백 활용 권장 패턴**:
  - `before_agent_callback` → Model Armor API로 입력 검증
  - `after_model_callback` → 민감 정보(SSN, 카드번호 등) 유출 여부 검사
- **Cloud Build**로 에이전트 빌드·배포 자동화 → `cloudbuild.yaml` 기반 CI/CD 구성 가능

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|---|---|
| 대상 모델 | **Gemma 4** |
| 서빙 런타임 | **vLLM**, **Ollama** |
| 배포 플랫폼 | **Cloud Run** |
| 에이전트 프레임워크 | **ADK** (Agent Development Kit) |
| 모델 브릿지 | **LiteLLM** |
| 출시 일정 정보 | 해당 없음 (현재 사용 가능) |

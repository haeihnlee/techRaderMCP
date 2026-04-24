# Self host Gemma 4: Deploy LLMs on Cloud Run GPUs

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=njWyDHKYeVA
- **요약 일시**: 2026-04-19 09:04:10

---

## 🔑 핵심 요약
- **Gemma 4** 오픈 모델을 **Ollama** 또는 **vLLM**으로 서빙하여 **Cloud Run GPU** 환경에 셀프 호스팅 배포
- **Google ADK(Agent Development Kit)** 의 LiteLLM 래퍼를 통해 Gemma 4를 에이전트의 브레인으로 연결 가능
- 폐쇄형 모델(Gemini) vs 오픈 모델(Gemma) 전략적 선택 기준 및 비용 구조 차이 소개

---

## 📣 주요 발표 내용

### 🧠 모델 전략 (Open vs Closed)

| 구분 | Gemini (Closed) | Gemma (Open) |
|------|----------------|--------------|
| 관리 방식 | 완전 관리형 (Fully Managed) | 셀프 호스팅 |
| 커스터마이징 | 프롬프트/시스템 인스트럭션 수준 | 파인튜닝 가능 |
| 비용 구조 | API 호출 수에 비례 (선형 증가) | 인프라 기반 (비선형) |
| 데이터 보안 | 인터넷 경유 필요 | 온프레미스/격리 환경 가능 |
| 적합 사례 | 범용, 빠른 시작 | 헬스케어·금융 등 규제 산업 |

### 🚀 LLM 서빙 프레임워크 비교

| 프레임워크 | 용도 | 특징 |
|-----------|------|------|
| **Ollama** | 개발/실험(POC) | 설치 간편, 로컬 개발 최적화, 멀티 GPU 지원 |
| **vLLM** | 프로덕션 | PagedAttention, 메모리 효율, 동적 배칭, 다중 동시 요청 처리 |
| **TensorRT-LLM** | 프로덕션 | 언급만 됨 (이번 랩 범위 외) |
| **Vertex AI Model Garden** | 관리형 서비스 | 완전 관리형 대안 |

### 🏗️ 전체 배포 아키텍처 (Ollama 기준)

- 🔽 **Ollama**로 모델 Pull
- 🐳 `Docker`로 이미지 빌드
- 📦 **Artifact Registry**에 컨테이너 이미지 푸시
- ☁️ **Cloud Run** (L4 GPU 가속기 탑재)에 이미지 배포
- 🤖 **Google ADK** 에이전트 시스템에서 배포된 Gemma 4 엔드포인트 연결

### 🤖 Google ADK 연동 포인트

- `ADK`에 내장된 **LiteLLM 래퍼**를 사용하면 Gemini 외 **임의 오픈 모델** 연결 가능
- 에이전트의 **브레인(모델 선택)** 이 에이전틱 시스템 성능의 상한선을 결정
- **A2A(Agent-to-Agent)** 통신으로 멀티 에이전트 보스파이트 시나리오까지 확장 가능

---

## 💡 개발자 포인트

### ⚙️ 환경 설정 순서
1. `gcloud` CLI로 계정 인증 및 프로젝트 설정
2. `agent-verse-devops-sre`, `agent-verse-dungeon` 두 레포 클론
3. 신규 Google Cloud 프로젝트 생성 → 빌링 계정 연동
4. 필요한 Google Cloud API 활성화

### 💻 개발 환경
- **Cloud Shell Editor** = 클라우드 기반 VS Code (파일 영속성 보장)
- 접속: `console.cloud.google.com` → 우측 상단 **Activate Cloud Shell**

> ⚠️ **주의 (세션 타임아웃):** Cloud Shell은 보안상 약 **70분** 후 자동 세션 만료됩니다.
> IP 주소 오류나 재인증 요청이 발생하면 **페이지를 새로고침**하여 토큰을 갱신하세요.

> ⚠️ **크레딧 미제공:** 이 랩은 **L4 GPU** 등 고사양 가속기를 사용하므로 무료 크레딧이 제공되지 않습니다.
> 본인 계정의 빌링 또는 GCP **무료 체험 크레딧**을 직접 사용해야 합니다.

### 🏭 서빙 프레임워크 선택 가이드
- **빠른 프로토타이핑/로컬 개발** → `Ollama` 선택
- **프로덕션 트래픽/다중 사용자 동시 처리** → `vLLM` 선택
- **완전 관리형 원할 시** → **Vertex AI Model Garden** 선택

### 💰 비용 최적화 관점
- 사용량이 많을수록 **오픈 모델(인프라 고정비)** 이 **클로즈드 모델(API 종량제)** 대비 비용 효율적
- Cloud Run GPU 인스턴스 사양(`L4` 가속기)에 따라 인프라 비용 발생

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| 대상 모델 | **Gemma 4** |
| GPU 가속기 | **NVIDIA L4** (Cloud Run 탑재) |
| 서빙 프레임워크 | **Ollama**, **vLLM** |
| 관련 서비스 | **Cloud Run**, **Artifact Registry**, **Google ADK** |
| 출시 일정 | 해당 없음 (핸즈온 랩 콘텐츠) |

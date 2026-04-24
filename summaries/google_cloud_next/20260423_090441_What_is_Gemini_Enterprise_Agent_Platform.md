# What is Gemini Enterprise Agent Platform?

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=j8qW5poBkEU
- **요약 일시**: 2026-04-23 09:04:41

---

## 🔑 핵심 요약
- **Gemini Enterprise Agent Platform**은 엔터프라이즈 수준의 AI 에이전트를 빌드·배포·관리·최적화하는 통합 플랫폼
- 기존 **Vertex AI**의 진화형으로, 모델 중심에서 **에이전트 퍼스트 에코시스템**으로 재구조화됨
- 빌드(`ADK`) → 배포(`Agent Runtime`) → 거버넌스(`Agent Gateway`, `Model Armor`) → 최적화(`Evaluation`, `Optimizer`)의 완전한 라이프사이클 지원

---

## 📣 주요 발표 내용

### 🏗️ Build (빌드)

- 🔧 **ADK (Agent Development Kit)**: 에이전트 빌드 핵심 프레임워크
  - 지원 언어: `Python`, `TypeScript`, `Java`, `Go`
  - 순차형 에이전트부터 복잡한 **멀티 에이전트 시스템**까지 지원
  - 최신 버전에서 **결정론적 그래프 기반 에이전트** 빌드 가능 (동적 모델 추론 vs 엄격한 결정론 선택 가능)
  - **Gemini** 최적화이나 **Anthropic Claude**, **Ollama** 오픈 웨이트 모델 등 외부 모델도 통합 가능

- 🔌 **외부 도구 연동**: `MCP (Model Context Protocol)` 표준 패턴으로 완전 지원
- 🤝 **에이전트 간 통신**: `A2A (Agent-to-Agent Protocol)` 내장 지원 — LangGraph, CrewAI, AG2 등 타 프레임워크와 협업 가능

- 💻 **Agent CLI**: 에이전트 생성·관리 자동화를 위한 완전한 프로그래밍 인터페이스
  - AI 시스템 개발용 **에이전트 스킬** 제공
  - 자동 평가(Automated Evaluation) 및 자동 배포 지원

- 🖱️ **Agent Studio**: Cloud Console의 **로우코드 비주얼 빌더**
  - 에이전트 플로우 시각적 설계 및 실시간 테스트
  - `ADK` 코드로 내보내기 → `Cloud Run`, `GKE` 등 어디서든 배포 가능

- 🌱 **Agent Garden**: 금융 분석, 마케팅 캠페인 등 **엔터프라이즈 패턴 사전 빌드 템플릿** 라이브러리

---

### 🚀 Scale (스케일)

- ⚡ **Agent Runtime**: 엔터프라이즈 에이전트 전용 **관리형 PaaS**
  - 콜드 스타트 **1초 미만**
  - 최대 **7일간** 장기 실행 에이전트 지원
  - `ADK` 최적화이나 `LangGraph`, `LangChain` 등 **프레임워크 무관(agnostic)** 배포 가능

- 💬 **Session 관리**: 사용자-에이전트 간 상호작용 자동 추적, 커스텀 세션 ID로 내부 고객 레코드 매핑 가능
- 🧠 **Memory Bank**: 사용자 장기 기억 유지 기능
- 🔒 **Sandbox**: 코드 실행 및 레거시 UI 조작을 위한 안전한 격리 환경

---

### 🛡️ Governance (거버넌스)

- 🪪 **Agent Identity**: 배포된 모든 에이전트에 고유 **IAM 원칙(principal)** 자동 부여
- 📋 **Agent Registry**: `Agent Runtime`, `GKE`, **Gemini Enterprise**, **Google Workspace** 배포 에이전트 자동 카탈로깅
  - 1st party/Apigee `MCP 서버` 자동 등록, 서드파티 에이전트 수동 등록 지원
- 🔐 **IAM Policy**: 에이전트·도구·레지스트리에 세분화된 접근 권한 정책 설정
- 🧹 **Model Armor**: 프롬프트 인젝션 차단 및 PII 유출 방지 — 입력 프롬프트/응답 모두 새니타이징
- 🚦 **Agent Gateway**: 모든 인그레스/이그레스 단일 진입점으로 정책 감사 및 강제 집행
- 🚨 **Anomaly Detection**: **LLM-as-a-Judge** 프레임워크로 비정상 추론 패턴 감지
  - 에이전트 보안 전용 **Security Dashboard** 제공

---

### 📈 Optimize (최적화)

- 🔭 **Agent Observability**: 에이전트 의사결정 전 과정 완전 가시화
  - 턴키 대시보드 + 자동 트레이싱으로 도구 호출 및 로직 오류 추적
- 🗺️ **Topology**: 멀티 에이전트 시스템 및 `MCP 서버` 전체 구조를 **그래프 뷰**로 시각화, 집계 트레이스 제공
- 🧪 **Evaluation**: 복잡한 멀티스텝 상호작용 **자동 평가**
- 🎲 **Simulation**: 수천 개의 샘플 상호작용 **자동 생성** → 프로덕션 배포 전 엣지 케이스 테스트
- 🔄 **Optimizer**: 실패 신호 기반 에이전트 지시문 자동 개선 → **지속적 피드백 루프** 구현

---

## 💡 개발자 포인트

> ⚠️ **Breaking Change 주의**: `Vertex AI`가 **Agent Platform**으로 재구조화됨. 모델 가든(Model Garden)·모델 트레이닝 포함. **기존 Vertex AI 핵심 기능은 변경 없음**이 공식 확인되었으나, 용어 전환 기간 중 혼용 발생 예상.

- **멀티 에이전트 설계 시** `A2A` 프로토콜 채택을 우선 고려 — 프레임워크 독립적으로 협업 가능
- `MCP`를 외부 도구 연결의 **표준 패턴**으로 사용할 것
- **생성형 AI의 비결정론적 특

# How to build and scale multi-agent AI systems on GKE

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=zI8KUvtHMvU
- **요약 일시**: 2026-08-25 09:06:02

---

## 🔑 핵심 요약
- **GKE(Google Kubernetes Engine)** 위에서 멀티 에이전트 AI 워크로드를 배포·보안·확장하는 방법을 소개
- `Kubernetes-sigs Agent Sandbox`를 활용한 에이전트 애플리케이션 자동 평가 파이프라인 구축
- **Gemini** 와 **MCP(Model Context Protocol)** 를 통해 GKE 인프라 진단·자동화 워크플로우를 재사용 가능한 스킬로 구성

---

## 📣 주요 발표 내용
- **Agent Sandbox on GKE**: `Kubernetes-sigs/agent-sandbox`를 사용해 에이전트 워크로드를 안전하게 격리·평가
- **GKE 장애 자동 진단**: **Gemini** + **MCP**로 인프라 전체 컨텍스트를 파악하고 진단 워크플로우를 자동화
  - 반복되는 진단 절차를 `reusable skill`로 저장해 재활용 가능
- **분산 멀티미디어 지식 수집 파이프라인**: **Gemini 2.5 Flash** 를 활용해 엔티티 정보를 추출하는 분산 멀티미디어 파이프라인을 GKE 위에서 구현
- **멀티 에이전트 아키텍처**: 여러 에이전트가 협력하는 시스템을 Kubernetes의 스케일링·오케스트레이션 능력과 결합

---

## 💡 개발자 포인트
- **MCP(Model Context Protocol)** 가 GKE 인프라 진단에 적용되는 실제 사례 — LLM 에이전트에게 클러스터 상태를 직접 노출하는 패턴
- `Agent Sandbox`는 신뢰할 수 없는 에이전트 코드를 격리 실행할 때 유용 — 보안 경계를 Kubernetes 네이티브로 관리

> **주의**: 멀티 에이전트 시스템을 GKE에 올릴 때는 에이전트 간 통신 및 권한 격리를 반드시 검토해야 함. Agent Sandbox가 이 부분을 다룸.

- Gemini 2.5 Flash 사용 — 고속 추론이 필요한 파이프라인 단계에 적합
- 진단 스킬을 MCP tool로 정의하면 다른 에이전트나 팀에서도 재사용 가능

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 모델 | Gemini 2.5 Flash |
| 플랫폼 | GKE (Google Kubernetes Engine) |
| 프로토콜 | MCP (Model Context Protocol) |
| 샌드박스 | `kubernetes-sigs/agent-sandbox` |


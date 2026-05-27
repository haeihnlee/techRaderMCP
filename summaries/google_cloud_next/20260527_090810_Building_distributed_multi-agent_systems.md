# Building distributed multi-agent systems

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=VjBijrS19gY
- **요약 일시**: 2026-05-27 09:08:10

---

## 🔑 핵심 요약
- **분산 멀티 에이전트 시스템**을 Google Cloud Run에 배포하는 실전 핸즈온 세션
- **AI Course Creator** 예제로 Researcher / Judge / Content Builder 역할을 분리한 모듈러 아키텍처 구성
- 핵심 스택: **ADK** (Agent Development Kit) + **A2A** (Agent-to-Agent 프로토콜) + **Cloud Run**

---

## 📣 주요 발표 내용
- **3부작 "Production Ready AI" 랩 시리즈** 발표
  - Lab 1 (오늘): 멀티 에이전트 시스템 구축
  - Lab 2 (6/30): 에이전트 **Evaluation**
  - Lab 3 (7/28): 에이전트 **Security**
- **모놀리식 프롬프트 대신 전문화된 소형 에이전트 squad** 구성을 권장 — 평가·디버깅·스케일링이 독립적으로 가능
- 사용 기술 스택:
  - `ADK`: AI 에이전트 빌드·실행 프레임워크, **ADK Web UI** 플레이그라운드 내장
  - `A2A`: 서로 다른 프레임워크의 에이전트가 능력을 발견하고 안전하게 협업하기 위한 오픈 프로토콜
  - `Cloud Run`: 각 에이전트를 독립 컨테이너로 서버리스 실행
- **Judge Agent 패턴**: LLM 출력 품질을 프로그래밍 방식으로 게이트
  - 구조화된 **JSON** 응답으로 `pass`/`fail` + 상세 피드백 반환
  - 통과 시 다음 단계로, 실패 시 Researcher 재호출
- **Loop Agent 아키텍처**: Researcher ↔ Judge 간 반복 피드백 자동화
- **Cloud Run MCP Server**로 배포 — IAM, Content Safety 등 보안 기능 통합 제공

---

## 💡 개발자 포인트
- "로컬에서 잘 돌아가는 에이전트"에서 "프로덕션 트래픽을 견디는 시스템"으로 가는 격차가 큰 만큼, **모듈식 설계**가 필수
- **Judge 패턴**은 매 출력을 수동 리뷰하지 않고도 **품질 보장**이 가능한 핵심 패턴 — 할루시네이션 방지에 효과적
- ADK Web UI에서 **개별 컴포넌트를 격리 테스트** 가능 → 전체 워크플로우에 묻히기 전에 디버깅 완료

> ⚠️ **반드시 `maximum iteration limit` 설정**: Loop Agent가 무한 루프에 빠지면 토큰을 무제한 소비. 토픽이 너무 광범위할 때 특히 위험.

> 💡 **프로덕션 이슈 사례**: Google Cloud Next 현장에서 가장 많이 나온 질문은 ① "에이전트가 실제로 가치를 전달하는지 어떻게 검증?" ② "악의적 사용에 대한 보안은?" — Lab 2·3에서 다룸.

- 각 에이전트를 **Cloud Run 컨테이너 1개씩** 배포 → 독립 스케일링/배포 가능
- A2A 프로토콜로 **이종 프레임워크 간 협업** 가능 — 벤더 락인 회피

---

## 📅 버전 / 출시 일정

| 항목 | 일정 |
|------|------|
| Lab 1: Multi-Agent System 구축 | 이번 세션 (공개됨) |
| Lab 2: Agent **Evaluation** | 2025-06-30 |
| Lab 3: Agent **Security** | 2025-07-28 |
| 관련 시리즈 | **The Agent Factory** (Google Cloud Tech YouTube 팟캐스트) |


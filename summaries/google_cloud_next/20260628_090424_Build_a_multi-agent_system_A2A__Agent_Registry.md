# Build a multi-agent system: A2A & Agent Registry

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=-MME36Ft9Gc
- **요약 일시**: 2026-06-28 09:04:24

---

## 🔑 핵심 요약
- **A2A(Agent-to-Agent) 프로토콜**은 "AI 에이전트를 위한 HTTP"로, 프레임워크(ADK·LangChain·LangGraph·CrewAI)에 상관없이 에이전트끼리 서로를 발견하고 작업을 주고받게 해준다.
- 에이전트가 50~100개로 늘어나면 무엇이 있는지·누가 소유하는지·어떻게 동적으로 호출하는지가 문제가 되는데, 이를 푸는 다음 단계가 **Agent Registry**다.
- 각 에이전트는 **Agent Card**(`/agent_card.json`)라는 "명함/LinkedIn 프로필"로 자신의 스킬·능력·연결 방법을 노출한다.

---

## 📣 주요 발표 내용
- **A2A 프로토콜**: Google이 1년 전 발표. HTTP가 브라우저·서버 종류를 가리지 않듯, A2A를 말하는 에이전트는 구현 프레임워크와 무관하게 통신 가능 — **"no custom glue"**.
- **Agent Card**: 에이전트의 신원이자 명세서. 스킬·능력·연결 방법(URI, 프로토콜 바인딩)을 담는다. 파일 위치는 `/agent_card.json`.
- **기본 통신 흐름 (Client ↔ Remote Agent)**:
  - 원격 에이전트 B를 **discoverable**하게 노출
  - 클라이언트 에이전트 A가 B의 **Agent Card**를 읽어 능력 파악
  - URI·프로토콜 바인딩(예: HTTP JSON) 확인 후 `message` 객체(role + 멀티모달/JSON)로 요청 전송
- **통신 모드**:
  - **Synchronous(폴링)**: 버블티가 준비됐는지 계속 물어보는 방식 — 비효율적
  - **Asynchronous(SSE 스트리밍/구독)**: 준비되면 알림을 받아 가져오는 방식 — 효율적
- **Agent Registry**: 조직 내 다수 에이전트의 **존재 파악·관리·소유자 확인·동적 호출**을 담당. 클라우드/온프렘에 흩어진 에이전트 **sprawl(난립)** 문제를 해결.

---

## 💡 개발자 포인트
- 프로덕션 멀티 에이전트 시스템에서는 하나의 슈퍼 에이전트보다 **"1 에이전트 = 1 책임"** 으로 나눠 A2A로 연결하는 구조가 권장된다.
- A2A 없이 로컬에서 직접 연결하면 커스텀 HTTP·인증·URL 관리가 필요하고 **tight coupling**이 되어 수정·재배포가 번거롭다.

> **Loose coupling이 핵심:** A2A를 쓰면 각 에이전트를 개별 서버에 배포하고 해당 에이전트만 독립적으로 수정·배포할 수 있어 확장·유지보수가 훨씬 쉬워진다.

- ADK의 workflow agent(sequential 등 sub-agent 연결)는 로컬 결합에 적합하지만, 분산·독립 배포·동적 발견이 필요하면 A2A가 정답.
- 동기/비동기 모드는 모두 A2A로 설정 가능하므로 유스케이스에 맞춰 폴링 vs SSE 구독을 선택할 것.

---

## 📅 버전 / 출시 일정
해당 없음 (A2A 프로토콜은 약 1년 전 발표, Agent Registry는 그 다음 단계로 소개됨)

# Building long-running AI agents with ADK

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=JsNbFnT0QCw
- **요약 일시**: 2026-06-17 09:03:40

---

## 🔑 핵심 요약
- **ADK(Agent Development Kit)** 로 몇 주 단위로 실행되는 **long-running AI agent** 를 만드는 패턴 소개
- 신규 입사자 **온보딩 코디네이터 에이전트** 예제: 환영 패킷 발송 → 서명 대기 → 하드웨어 배송 대기 → Day 1 일정 생성
- 핵심은 **event-driven dormancy(이벤트 기반 휴면)** — 폴링 루프·스레드 없이 외부 이벤트만 기다리며 컨텍스트 손실 없이 재개

---

## 📣 주요 발표 내용
- Shubham·Eric이 작성한 블로그 **"Building long-running AI agents that never lose context with ADK"** 기반 (오픈소스)
- 에이전트가 **welcome packet** 발송 후 즉시 **dormant 상태**로 진입 → 며칠간 멈춰 있어도 됨
- 외부 액션(서명, 하드웨어 배송 등)이 발생하면 **resume turn**으로 깨어나 다음 단계 진행
- **multi-agent delegation**: 코디네이터가 IT 계정 프로비저닝을 전담 **subagent**에 위임, 각 에이전트의 reasoning chain을 깔끔하게 유지
- 배송 확인은 운영 환경에서 **shipping provider의 webhook callback**(API endpoint)으로 처리, 데모에선 carrier webhook을 시뮬레이션
- 프런트엔드까지 포함된 오픈소스 레포로 커스터마이징 가능

---

## 💡 개발자 포인트
- **durable memory** 를 DB의 **enum state(state machine)** 로 관리 — vector store의 raw JSON chat log가 아님
  - → 몇 주가 지나도 **context pollution / token bloat 없음**
- 상태 전이는 **state machine이 강제** → 에이전트가 단계를 건너뛰도록 유도(coerce)될 수 없음
- UI가 낙관적으로(optimistically) 갱신되지 않고, 백엔드 **resume turn 완료 후**에만 상태 반영

> 일반 챗봇 에이전트와의 결정적 차이 3가지:
> ① **durable schema state**(enum in DB) ② **event-driven dormancy**(쉴 때 완전히 sleep) ③ **multi-agent delegation**

> 컨테이너가 휴면 중엔 폴링 루프·스레드 스피닝이 전혀 없어 그대로 scale 가능 — "가짜가 아닌 진짜 long-running 패턴"임을 증명

---

## 📅 버전 / 출시 일정
해당 없음 (블로그·예제 레포 모두 오픈소스로 공개)


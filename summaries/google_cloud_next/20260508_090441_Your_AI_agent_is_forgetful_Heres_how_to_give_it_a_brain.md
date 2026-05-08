# Your AI agent is forgetful. Here's how to give it a brain.

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=b9Dx7uGxwsg
- **요약 일시**: 2026-05-08 09:04:41

---

## 🔑 핵심 요약
- **AI 에이전트의 "금붕어 메모리 문제"** — 모델·툴링만 강조하다 보면 정작 **메모리(memory)** 가 빠져 똑똑한 에이전트가 바보처럼 보임
- **Google ADK(Agent Development Kit)** 로 메모리를 구현하는 6가지 패턴 중 **앞 3가지** 소개: `Session`, **Multi-agent State**, **Persistent Database Session**
- 단일 대화 → 다중 에이전트 컨텍스트 공유 → 재시작 후에도 유지되는 영속 메모리로 단계적 확장

---

## 📣 주요 발표 내용
- **1) Session 메모리 (대화 이력 보관)**
  - `Session` 객체를 생성·사용하면 한 대화 안에서 사용자 발화·응답을 모두 기억
  - "도쿄 2일 여행, 역사 명소 선호" 같은 컨텍스트가 후속 질문에 자동 반영
  - 가장 기본적인 에이전트 메모리 타입

- **2) Multi-agent State (에이전트 간 공유)**
  - `state` 는 **세션 전체가 공유하는 디지털 폴더** 역할
  - 예: `foodie_agent` 가 결과를 `destination` 키에 저장 → `transportation_agent` 가 프롬프트에서 `{destination}` 로 참조
  - 두 에이전트를 `SequentialAgent` 타입의 root agent로 묶어 순차 실행
  - ADK Web UI에서 state 값을 실시간으로 확인 가능

- **3) Persistent Database Session (영속 메모리)**
  - 기본 in-memory 세션은 **스크립트 종료·서버 재부팅 시 전부 소실**
  - **DatabaseSessionService** 로 교체하면 며칠·몇 주·몇 달 전 대화도 회상 가능
  - 구현 흐름: 세션 서비스에서 **이전 세션 조회 → 이전 컨텍스트 빌드 → 현재 query에 주입**

---

## 💡 개발자 포인트
- AI 앱 빌드 시 흔히 모델·툴 선택에만 집중하지만, **사용자 경험을 좌우하는 건 메모리** — "내 취향을 기억하는 비서"의 핵심
- ADK 사용 시 `Session` → `state` → `DatabaseSessionService` 로 단계적 확장 패턴이 표준 경로

> ⚠️ **주의: in-memory 세션은 휘발성**
> 데모/프로토타입은 OK지만, 프로덕션에서는 반드시 `DatabaseSessionService` 로 전환해야 재시작 후에도 사용자 컨텍스트가 살아남음

- 다중 에이전트 협업 시 prompt에 `{key}` 형태로 state를 참조 → 에이전트 간 결합도를 낮추면서 데이터 전달
- 후속 영상에서 **나머지 3가지 메모리 패턴** 공개 예정 (장기 기억·요약·시맨틱 메모리 등으로 추정)

---

## 📅 버전 / 출시 일정
해당 없음 (개념·패턴 소개 중심 영상, ADK는 이미 사용 가능)


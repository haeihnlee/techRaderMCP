# How we built 1,000 AI agents that run a marathon

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=WSIzaih2vq4
- **요약 일시**: 2026-05-31 09:03:50

---

## 🔑 핵심 요약
- Google Cloud Next 개발자 키노트에서 시연한 **"Race Condition"** 레퍼런스 아키텍처 — **1,000개의 AI 에이전트**가 라스베이거스 마라톤을 실시간 시뮬레이션
- 각 러너 에이전트는 독립 세션으로 수분 상태·속도를 자체 판단하며, 4계층 **폴리글랏(polyglot) 스택**(Angular + Go + Python ADK + 인프라)으로 구성
- 핵심 최적화는 **두 가지 디스패치 모드**(`subscriber` / `callable`) — 1,000개 동시 세션을 ~10초 내 처리하기 위해 HTTP 대신 **관리형 Redis Pub/Sub** 채택
- 전체 코드가 **오픈소스**로 공개되어 직접 실행·학습 가능

---

## 📣 주요 발표 내용
- **4계층 아키텍처**로 시스템 구성:
  - **Angular 프론트엔드** — 1,000개 점(러너)이 움직이는 실시간 시뮬레이션 UI
  - **Go 게이트웨이** — 고동시성 "트래픽 캅". 수천 개 WebSocket·메시지를 무리 없이 처리
  - **Python ADK 에이전트** — 모든 AI 로직. 성숙한 **`ADK`(Agent Development Kit)** 생태계 활용
  - **인프라 계층** — `Redis`(Memorystore) / `Pub/Sub` 기반 통신 프로토콜
- 에이전트 종류: **planner**(계획), **simulator**(시뮬레이터), **runner**(러너) 등으로 구분
- **두 가지 디스패치 모드**:
  - **`subscriber`** — 러너 에이전트용. 장수명 Redis 구독을 유지하고, 매 tick마다 시뮬레이터가 발행한 메시지에 전체 에이전트가 동시에 깨어나 응답. **HTTP 지연 없이 sub-millisecond** 응답
  - **`callable`** — planner·simulator용. **`A2A`(Agent-to-Agent) HTTP 프로토콜**로 요청 시에만 동작하고 **0까지 스케일 다운**
- **Gemini Enterprise Agent Platform** 런타임 위에서 callable 에이전트가 대기
- 러너 에이전트는 **A2A `agent card`**에 자신의 디스패치 방식을 정의해 프로토콜을 확장

---

## 💡 개발자 포인트
- **"최고의 도구를 적재적소에"** 라는 원칙으로 언어를 분리 — Go는 실시간 통신, Python은 AI 로직. 이 분리 덕분에 1,000개 에이전트가 동시에 "생각"해도 시스템이 빠르게 반응
- 처음엔 표준 **A2A over HTTP**만으로 시작했으나, 1,000개 동시 메시지에서 **네트워크 오버헤드가 병목**이 되어 Redis Pub/Sub로 점진적으로 전환한 실전 의사결정 과정 공유
  > "프레임워크·표준·프로토콜을 설계된 그대로 쓰려 했지만, 1,000개 세션에 동시 메시지를 보내고 ~10초 내 응답을 모으려니 HTTP로는 효율적으로 스케일되지 않았다. 에이전트를 최적화하면 결국 네트워크가 병목이 된다."
- **비용 최적화 인사이트**: planner·simulator 같은 "thinker"는 idle CPU 비용을 없애려 callable(scale-to-zero)로, runner 같은 "doer"는 hot path라 subscriber로 — 부하 특성에 따라 통신 방식을 다르게 설계
- 관리형 Redis는 **단일 노드로 약 10만 동시 메시지** 처리 가능 → 작은 인스턴스로도 충분
- A2A 프로토콜의 **확장 메커니즘**을 활용하면 표준을 깨지 않고 커스텀 디스패치 추가 가능
- "데모와 풀 프로덕션 사이의 레퍼런스 아키텍처"로 공개 — 커뮤니티가 개선 코드를 작성하도록 유도

---

## 📅 버전 / 출시 일정
해당 없음 (오픈소스 레퍼런스 아키텍처, Google Cloud Next 개발자 키노트 시연)


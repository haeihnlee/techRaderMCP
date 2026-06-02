# Build long-running agents with Google's Agentic Stack | The Agent Factory

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=VGpfnbr7rso
- **요약 일시**: 2026-06-02 09:06:10

---

## 🔑 핵심 요약
- Google Cloud AI의 **Addie Osmani**가 **장기 실행 에이전트(long-running agents)** 구축을 위한 Google의 **Agentic Stack**을 시연
- 기존 챗봇형 에이전트와 달리, 장기 실행 에이전트는 **세션을 넘어 상태를 유지**하며 수 시간·수일·수주에 걸쳐 워크플로를 완수
- 작업 단위가 단일 프롬프트가 아닌 **워크플로(workflow)** 이며, 에이전트가 다단계 프로세스를 end-to-end로 소유
- 안정적 동작을 위한 **3대 조건**: ① 진짜 잠들 수 있을 것(이벤트 기반 휴면) ② 매 단계 체크포인트(영속 상태) ③ 자기 결과를 스스로 평가하지 말 것(평가자 분리)

---

## 📣 주요 발표 내용
- **풀 프로덕션 에이전트 스택** 출시: `ADK 2.0` (그래프 기반 워크플로 런타임), **agent CLI**(skills 사전 패키징), **managed agents API**, `Gemini 3.5 Flash`, **anti-gravity 2.0**
- `agent CLI`의 skills로 **Cloud Run에 장기 실행 에이전트 배포** 등을 손쉽게 수행 가능
- **3대 설계 원칙**:
  - **진짜 잠들 수 있어야 함** → `active polling`(블로킹 스레드로 컴퓨트 낭비) 지양, web hook·스케줄·휴먼 승인·tool callback 같은 **외부 이벤트로 깨어남**
  - **모든 단계에 체크포인트** → 상태를 매 전이마다 **영속 저장**, 컨테이너 크래시·재배포 후에도 정확히 멈춘 지점부터 재개(환각 메모리 없음)
  - **자기 평가 금지** → Anthropic 등 연구상 에이전트는 자기 출력을 **과대평가**하는 경향. **planner + generator + 별도 evaluator** 3-에이전트 구성 권장
- **신입 온보딩 코디네이터 에이전트** 라이브 데모 (동료 Shubham·Eric의 오픈소스 블로그 *"building long-running AI agents that never lose context with ADK"* 기반):
  - 웰컴 패킷 발송 → **수일간 휴면(dormant)** → 서명 대기 → IT 프로비저닝 → 하드웨어 배송 → Day-1 일정 제공
  - UI가 낙관적 업데이트 없이 **`ADK resume turn` 완료를 기다린 뒤** 갱신 → 패턴이 실제임을 증명
  - **skills registry** 연동도 손쉽게 확장 가능 (대부분의 primitive가 그대로 매핑)
- **코딩**을 가장 대표적인 장기 실행 워크로드로 제시 (단일 프롬프트가 아닌 의존적 문제의 연쇄)

---

## 💡 개발자 포인트
- 데모 코드는 **완전한 오픈소스**이며 커스터마이즈 가능한 프런트엔드 포함 → 바로 실습 가능
- 표준 챗봇 에이전트와 **장기 실행 패턴의 3가지 차이**:
  - **내구성 메모리(durable memory)**: 상태가 DB의 `enum` 스키마로 관리됨 → vector store의 raw JSON 채팅 로그가 아님

> ⚠️ 채팅 로그를 그대로 쌓지 않으므로 **컨텍스트 오염(context pollution)·토큰 비대화(token bloat)** 가 없음. 수주간 유휴 상태여도 토큰이 부풀지 않음

- **이벤트 기반 휴면**: pause gate 사이에서 에이전트는 계속 실행되지 않고 **완전히 휴식(at rest)** → 불필요한 컴퓨트 소모 제거
- **멀티 에이전트 위임**: 코디네이터가 IT 계정 프로비저닝을 직접 처리하지 않고 **전문 sub agent에 위임**, 각 에이전트의 추론 체인을 깨끗하게 유지
- **상태 머신(state machine)** 이 단계 순서를 강제 → 에이전트가 단계를 건너뛰도록 유도(coerce)될 수 없음
- 역할 기반 분기 확장 예시: 엔지니어는 **GitHub 접근**, 디자이너는 **Figma 접근** 등 role에 맞춰 패턴 매칭하여 맞춤형 온보딩 제공 가능

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| `ADK 2.0` | 그래프 기반 워크플로 런타임, agent CLI 포함 (최근 출시) |
| `Gemini 3.5 Flash` | 신규 모델 |
| anti-gravity 2.0 | 신규 출시 |
| managed agents API | 신규 출시 |
| 온보딩 에이전트 블로그/레포 | 발표 시점 기준 "이번 주" 공개된 오픈소스 |

> 영상 transcript가 12,000자에서 절단되어, 코딩 데모 등 후반부 일부 내용은 요약에 포함되지 않았습니다.


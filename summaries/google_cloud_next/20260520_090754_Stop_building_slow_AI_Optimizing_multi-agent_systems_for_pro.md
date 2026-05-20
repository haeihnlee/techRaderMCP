# Stop building slow AI: Optimizing multi-agent systems for production

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=ge5cLd8uics
- **요약 일시**: 2026-05-20 09:07:54

---

## 🔑 핵심 요약
- Google Cloud Next 데모용 **멀티 에이전트 시스템**(마라톤 플래너) 설계 과정에서 얻은 **프로덕션 최적화 노하우** 공유
- 처음엔 6+ 에이전트로 시작했으나 **레이턴시 문제**로 `Simulator`/`Planner`/`Evaluator` 3개 에이전트 구조로 축소
- **실시간 평가(real-time evaluation)** + **A2A 프로토콜** + **A2UI(Agent-to-UI)** 패턴을 결합한 아키텍처

---

## 📣 주요 발표 내용
- **3-에이전트 아키텍처**로 단순화: `Simulator`, `Planner`, `Evaluator`
- **Evaluator를 별도 에이전트**로 분리한 이유 → "Agent as a Judge" 패턴 실험 및 평가 로직 반복 개선 용이
- **모델 다양화로 평가 편향 제거**: 플랜 생성은 `Gemini 3 Flash`, 평가는 `Gemini 3.1 Pro` 사용
- **Skill vs Tool 구분**: Skill = 추가 프롬프트/지침 + 번들된 Tool. A2UI용 Skill에 **18개 기본 UI 컴포넌트 카탈로그**와 JSON 페이로드 **검증 Tool** 번들
- **A2A 프로토콜의 확장성** 활용 → Agent Card에 `capabilities` 노출, HTTP 외에 **Pub/Sub callable** 추가하여 1,000개 동시 세션 처리
- **Memorystore + Pub/Sub** 기반 시뮬레이션 (1,000 러너 세션 동시 실행)
- **Gemini Enterprise Agent Platform**의 **Evaluation Service** 연동 → 사전 정의 메트릭 + 커스텀 메트릭 혼합으로 시간 경과 추적

---

## 💡 개발자 포인트
> **레이턴시 최적화는 멀티 에이전트 시스템에서 "동작"과 "프로덕션"을 가르는 결정적 요소.** 작동하는 프로토타입과 실제로 쓸 만한 시스템은 완전히 다르다.

**평가(Evaluation) 최적화 핵심 트릭:**
- 기존 **7개 평가 기준을 개별 호출** → 비결정적(non-deterministic) 기준을 **단일 호출로 통합**
- `Gemini 3.1 Pro`의 컨텍스트 처리력 활용 가능
- 평가는 **일회성이 아닌 지속적(recurrent)** 프로세스로 설계

**지각적 속도(perceived latency) 개선:**
- **Server-Sent Events 스트리밍** 활성화 (`Agent Engine` / `Cloud Run` 양쪽 모두 지원, 기본값 아님)
- A2A 프로토콜 확장으로 **에이전트별 호출 메커니즘 분리** (Planner = HTTP, Runner = Pub/Sub)
- 호출 방식을 **하드코딩하지 말고 Agent Card capabilities로 노출**

**A2UI 패턴 적용 시:**
- 에이전트가 JSON 페이로드로 UI 기술 → 프론트엔드가 렌더링하는 구조
- 반드시 **출력 검증 Tool**을 함께 번들할 것 (잘못된 UI 페이로드 차단)

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| 플랜 생성 모델 | `Gemini 3 Flash` |
| 평가 모델 | `Gemini 3.1 Pro` |
| 플랫폼 | `Gemini Enterprise Agent Platform` (구 Agent Engine 포함) |
| 런타임 옵션 | `Agent Runtime` / `Cloud Run` |
| 프로토콜 | `A2A` (Agent-to-Agent), `A2UI` (Agent-to-UI) |


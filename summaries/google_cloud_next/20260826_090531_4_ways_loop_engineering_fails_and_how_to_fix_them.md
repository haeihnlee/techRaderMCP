# 4 ways loop engineering fails (and how to fix them)

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=ruNekO9De8E
- **요약 일시**: 2026-08-26 09:05:31

---

## 🔑 핵심 요약
- **Loop Engineering(루프 엔지니어링)** 은 "내가 계속 프롬프트를 치는 대신, **목표를 주고 시스템이 스스로 재시도**하게 만드는 것" — 즉 자신을 시스템으로 대체하는 패턴
- AI 시대의 무한 루프는 메모리·스택이 아니라 **토큰(= 실제 비용)** 을 태운다 → **stop rule과 cost cap이 필수**
- 에이전트가 자기 결과물을 자기가 평가하면 **confirmation bias·context pollution** 발생 → 평가는 반드시 분리
- 목표는 **검증 가능(checkable)** 해야 하고, 문제가 커지면 loop을 넘어 **Graph Engineering** 으로 전환

---

## 📣 주요 발표 내용

영상은 loop engineering이 실패하는 **4가지 패턴**과 각각의 처방을 정리합니다.

**① Runaway Loop (탈출 조건 없는 루프)**
- retry 로직을 루프로 감싸놓고 **exit condition을 빼먹는** 고전적 실수
- 예전엔 앱이 멈추는 정도였지만, 지금은 **토큰을 태워 돈이 나간다**
- 처방: **명시적 stop rule** — `max_iterations = 5`, **time limit**, **token/call limit** 중 최소 하나

**② Unverified Autonomy (검증 없는 자율성)**
- 같은 대화에서 동일 작업을 반복시키면 에이전트가 **이전 context/memory를 재사용**
- 첫 시도가 틀렸거나 데이터가 나빴다면 **오류가 그대로 증폭**됨 → **confirmation bias**
- 처방: **Agent A ↔ Agent B 상호 평가**(separation of concerns), **LLM as a judge**, 또는 명시적 평가 지표

**③ Uncheckable Goals (검증 불가능한 목표)**
- `"이 요약을 더 좋게 만들어줘"` 같은 지시는 **"better"의 정의가 없어** LLM이 헤맴
- 처방: **non-debatable·non-negotiable 기준** 으로 바꾸기
  - `단어 수 10개 이하`
  - `컴파일 에러 0건`

**④ Complexity (단일 루프의 한계)**
- "한 단락 요약" 정도는 단일 루프로 충분
- 반면 "**이미지·표 포함 50페이지 PDF**"는 단일 루프가 **context limit에 걸려 무너짐**
- 처방: **Graph Engineering** 으로 이동 — 조직도처럼 **노드/엣지로 워크플로를 오케스트레이션**하고, **loop을 graph의 한 구성요소로 배치**

---

## 💡 개발자 포인트

- **비용 가드레일을 코드 레벨에 박아두세요.** 반복 횟수·시간·토큰 상한 중 하나라도 없는 에이전트 루프는 프로덕션에 올리면 안 됩니다.

> ⚠️ **자기 채점 금지 (Never let an agent rubber stamp its own work).**
> 영상의 비유: *"에이전트가 자기 결과를 평가하게 하는 건 유치원생에게 자기 숙제를 채점하게 하는 것"*.
> 평가자는 **반드시 별도 에이전트나 결정론적 검증기**여야 합니다.

- **종료 조건을 "판단"이 아니라 "측정"으로 설계하세요.** 루프의 exit condition은 LLM의 주관적 판단이 아니라, 테스트 통과·컴파일 결과·수치 임계값처럼 **기계가 참/거짓을 낼 수 있는 것**이어야 합니다.
- **같은 세션에서 같은 작업을 반복 호출하는 패턴을 의심하세요.** context 재사용이 성능 최적화처럼 보이지만, 초기 오류를 고착시키는 **context pollution 경로**가 됩니다. 필요하면 **fresh context로 재시작**.
- **loop → graph 전환 시점의 신호**: 산출물이 길어지고(멀티 섹션·멀티 모달), 단계 간 의존성이 생기고, context limit 경고가 뜨기 시작할 때.
- 적용 스코프 정리: **loop engineering은 "제한적(contained)·검증 가능(verifiable)·반복적(repetitive)" 작업에 적합** 합니다. 그 밖은 graph.

---

## 📅 버전 / 출시 일정

해당 없음 (제품 출시가 아닌 아키텍처 패턴/베스트 프랙티스 세션)

**참고 수치 (영상에서 언급된 예시 값)**

| 항목 | 예시 기준 |
| --- | --- |
| 최대 반복 횟수 | `max_iterations = 5` |
| 기타 stop rule | time limit, token limit, call 수 limit |
| 검증 가능한 목표 예 | 단어 수 10개 이하, 컴파일 에러 0건 |
| 단일 루프 한계 예시 | 이미지·표 포함 50페이지 PDF |


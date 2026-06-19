# 3 patterns to build long-running AI agents

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=l6KeLCuB90o
- **요약 일시**: 2026-06-19 09:05:11

---

## 🔑 핵심 요약
- **Long-running agent**은 단일 컨텍스트 윈도우에 갇히지 않고 **세션을 넘어 상태(state)를 유지**하며 수 시간~수 주 단위로 동작하는 에이전트입니다.
- 작업 단위가 단발성 **prompt**가 아니라 멀티스텝 **workflow** 전체이며, 에이전트가 프로세스를 end-to-end로 소유합니다.
- 이를 구현하려면 **① 진짜 잠들 수 있는 에이전트(dormancy) ② 모든 단계의 체크포인트(durable state) ③ 자기 평가 금지(분리된 evaluator)** 3가지가 반드시 충족돼야 합니다.

---

## 📣 주요 발표 내용
- **Dormancy (휴면)**: 에이전트는 사람처럼 "진짜로 잠들" 수 있어야 함. `active polling`으로 스레드를 점유해 compute를 태우지 말고, **webhook · schedule · 사람 승인 · tool callback** 같은 외부 이벤트로 깨어나야 함.
- **Durable State (영속 상태)**: 모든 상태 전이마다 상태를 **durably persist**. 컨테이너가 crash 나도 서버를 redeploy 해 정확히 멈춘 지점부터 재개 가능. 환각된 메모리나 가짜 중간 단계 없이 이어가야 함 (예: 직원 온보딩, 대출 심사처럼 며칠이 걸리는 작업).
- **Separated Evaluation (분리된 평가)**: 코드를 짠 에이전트가 같은 에이전트로 리뷰하면 안 됨. **planner · generator · evaluator** 3-에이전트 구성이 state-of-the-art.
- 에이전트가 자주 부딪히는 **3개의 벽**: ① 컨텍스트 품질 저하(context degrading) ② 영속 상태 부재로 인한 drift·중단 ③ 자기 검증 실패(self-verification).
- 이를 돌파한 **3대 breakthrough**: **agent harness 엔지니어링** 발전, **persistent memory 패턴**(living plan을 markdown으로, change log를 lab notes로, `Ralph loop` 등 long-running loop 활용), **관리형 인프라**.

---

## 💡 개발자 포인트
- 에이전트가 자기 결과물을 평가하면 **일관되게 과대평가**합니다. Anthropic 등 여러 연구실의 결론이며, 품질 보장을 위해 **독립된 evaluator**로 실제 결과를 테스트해야 합니다.

> ⚠️ **자기 채점(self-grading) 금지**: 같은 에이전트로 코드 작성과 리뷰를 동시에 하지 마세요. 에이전트는 자기 출력에 과신(overconfident)하므로 planner / generator / evaluator를 분리하세요.

> ⚠️ **블로킹 폴링 금지**: 응답을 기다리며 스레드를 점유하지 말고, 외부 이벤트(webhook·schedule·callback)로 깨어나는 이벤트 드리븐 휴면 구조로 설계하세요.

- 모든 단계에서 **체크포인트 저장**을 전제로 설계해야 crash·redeploy 후에도 무결하게 재개됩니다.
- living plan은 **markdown**, 진행 이력은 **change log**로 관리하는 persistent memory 패턴이 실전에서 유효합니다.
- 프로덕션 예시로 **Gemini Enterprise Agent platform**의 sessions / memory bank(장기 메모리)가 소개됐습니다.

---

## 📅 버전 / 출시 일정
해당 없음

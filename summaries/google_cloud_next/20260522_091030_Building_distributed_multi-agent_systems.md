# Building distributed multi-agent systems

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=VjBijrS19gY
- **요약 일시**: 2026-05-22 09:10:30

---

## 🔑 핵심 요약
- 단일 **LLM**으로는 현실 세계의 복잡한 문제를 풀기 어려움 → **다중 에이전트(multi-agent)** 협업이 필요
- 자가 교정(self-correcting) **Course Creation Pipeline**을 처음부터 구축하는 라이브 데모
- 로컬 개발 환경에서 **프로덕션**까지 옮기는 전체 워크플로우 시연

---

## 📣 주요 발표 내용
- **전문화 에이전트(Specialized Agents)** 구성
  - 도구를 사용하는 **Researcher** 에이전트
  - **Pydantic** 기반 **Judge** 에이전트로 결과물 검증
- **스마트 오케스트레이션(Smart Orchestration)**
  - `LoopAgent`를 활용한 반복·자가 교정 루프 구성
  - 여러 에이전트가 협력하는 분산 구조 설계
- 라이브 코딩으로 **로컬 → 프로덕션** 배포 흐름 시연

---

## 💡 개발자 포인트
- **단일 LLM 호출의 한계**를 인정하고, 역할 분담된 에이전트 구조로 전환하는 패턴을 익힐 수 있음
- `Pydantic` **스키마**로 에이전트 출력 검증 → 환각/오류를 구조적으로 차단
- `LoopAgent` 같은 오케스트레이션 프리미티브로 **자가 교정 파이프라인** 구현 가능

> ⚠️ 영상에 **자막이 제공되지 않아** 세부 코드와 API 사용법은 영상 시청을 통해 직접 확인 필요. 본 요약은 영상 설명(description) 기반.

- 분산 멀티 에이전트 시스템은 **Google Cloud**의 에이전트 런타임(예: Vertex AI Agent / ADK)과 결합 시 운영 안정성 확보에 유리

---

## 📅 버전 / 출시 일정
해당 없음 (라이브 데모 세션)

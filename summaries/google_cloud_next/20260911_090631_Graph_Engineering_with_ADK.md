# Graph Engineering with ADK

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=Mzr7byMFy_4
- **요약 일시**: 2026-09-11 09:06:31

---

## 🔑 핵심 요약
- **Graph Engineering**은 에이전트와 결정론적 함수를 노드로, 그 연결을 엣지로 구성하는 워크플로우 패턴
- 단일 거대 프롬프트("one giant prompt") 방식은 환각(hallucination)을 유발하며, 구조화된 그래프가 그 해결책
- **ADK2**(Google Agent Development Kit 2)를 사용해 팬아웃·조인·라우터 패턴으로 비용 효율적인 에이전트 시스템 구축 가능

---

## 📣 주요 발표 내용
- **Graph Engineering의 계층 구조**: Prompt Engineering → Context Engineering → Loop Engineering → Graph Engineering 순으로 발전
- `ADK2`의 핵심 개념 세 가지:
  - **Fan-out**: 의존성 없는 병렬 노드 동시 실행 (날씨·코스·피트니스 동시 fetch)
  - **Join**: 여러 브랜치 결과를 하나의 딕셔너리로 집계하는 노드 — 별도 집계 에이전트 불필요
  - **Router**: 조건에 따라 분기 실행, LM 라우터와 결정론적 라우터 중 선택
- `dynamic fan-out`: 런타임에 병렬 프로세스 수를 모르는 경우 동적 워크플로우로 그래프 형태를 코드에서 결정

---

## 💡 개발자 포인트
- **예측 가능한 작업은 함수(노드)에, 추론이 필요한 작업만 모델(에이전트 노드)에** 배치하는 것이 핵심 원칙
- LM 라우터 vs 결정론적 라우터 선택 기준:
  - 입력이 자유 텍스트이거나 분기 신호를 if문으로 읽을 수 없으면 → **LM 라우터**
  - 분기 집합이 닫혀 있고 데이터에 신호가 있으면 → **결정론적 라우터** (비용 절감 + 신뢰성 향상)

> 단일 모델 호출 안에 모든 단계를 넣으면 아무것도 fetch할 수 없고, 테스트할 수 없으며, 신뢰할 수 없다. 구조가 해결책이다.

- 마라톤 예시에서 팬아웃·조인·라우터 적용 결과, **LM 호출 1회**만으로 전체 전략 생성 — 비용 최소화 달성
- 그래프가 필요 없는 경우: 입력이 도착하기 전에 워크플로우를 그릴 수 없다면 `dynamic workflow`를 고려

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 사용 SDK | **ADK2** (Google Agent Development Kit 2) |
| 출시 일정 언급 | 없음 |

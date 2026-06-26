# Implementing DeepMind innovation: Deep research API

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=05043f3GseE
- **요약 일시**: 2026-06-26 09:13:25

---

## 🔑 핵심 요약
- Google이 **Deep Research API**를 공개 — 수백 개 소스 탐색·검증·종합·시각화까지 자동 수행하는 **에이전트 자체를 API로 제공**한다.
- 수천 시간·수천 달러가 걸리던 리서치 작업을 **수 분, 단 몇 달러**로 단축한다.
- 신규 **`interactions API`**(통합 API)를 통해 모델과 에이전트를 함께 호출하고, **자체 데이터(RAG)·원격 MCP 서버**와 연결할 수 있다.

---

## 📣 주요 발표 내용
- **Deep Research API 출시** — 컨슈머 Gemini 앱의 Deep Research 경험을 개발자가 자기 애플리케이션에 직접 임베드할 수 있게 됨.
- **작동 구조 3단계**:
  - **Meta Planning**: 쿼리를 분해해 구조화된 계획 수립 (사용자가 계획을 함께 다듬을 수 있음)
  - **Research Loop**: 검색 → 결과 읽기 → 추론을 계획 완료까지 반복
  - **Synthesizing**: 초안 작성 → 출처 검증·인용 첨부 → 구조화된 리포트 생성
- **인라인 그래픽 지원** — Gemini의 코딩 능력으로 차트·그래프 생성, **`Nano banana`** 모델로 인터랙티브 인포그래픽 제작.
- **데이터 연결** — `file search`로 내부 PDF를 **Firebase** 기반 RAG 스토어에 업로드하거나, **금융·농업 등 도메인 특화 파트너의 원격 서버**에 연결 가능.
- **벤치마크 성능** — Deep Research preview/Max 에이전트가 **Humanity's Last Exam에서 55.6점** 달성, 자체 **Deep Research QA** 벤치마크로 복잡한 검색 과제 평가.

---

## 💡 개발자 포인트
- **`interactions API`** 는 모델과 에이전트를 통합 호출하는 새 API — Deep Research 결과를 곧바로 Gemini 모델에 넘겨 **번역·후속질문·TTS 팟캐스트 변환** 등으로 체이닝할 수 있다.
- 직접 eval을 돌리거나 품질 튜닝을 할 필요 없이 **API 소비만으로** 향상된 factuality·groundedness를 얻는다.

> **장시간 실행 주의**: Deep Research 요청은 수 초가 아니라 **수 분~수 시간**이 걸린다. 상태는 서버에서 관리되며, 연결이 끊겨도 발급받은 **event ID / 전체 request ID**로 재접속·폴링이 가능하도록 resiliency가 설계되어 있다.

- 외부 도메인 데이터는 **원격 MCP 서버** 연동으로 확보 — 신뢰할 수 있는 서드파티의 독점 데이터를 리서치에 결합할 수 있다.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| Deep Research API | **Google AI Studio에서 오늘 이용 가능** |
| Gemini Enterprise Agent 플랫폼 | **향후 수일 내** 제공 예정 |
| 제공 형태 | `interactions API`를 통해 사용 |


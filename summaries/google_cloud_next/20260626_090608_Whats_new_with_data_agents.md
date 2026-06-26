# What's new with data agents

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=Z-AfOcWO_kk
- **요약 일시**: 2026-06-26 09:06:08

---

## 🔑 핵심 요약
- **BigQuery 기반 데이터 에이전트**가 대거 업데이트되어 SQL 작성·파이프라인·ML·분석을 자연어로 처리
- **데이터 엔지니어링 에이전트**, **데이터 사이언스 에이전트**, **BigQuery 대화형 분석**이 모두 **GA(정식 출시)** 전환
- Gartner 예측: **2027년까지 비즈니스 의사결정의 50% 이상**이 에이전트 AI로 증강·자동화

---

## 📣 주요 발표 내용

Google은 에이전트 투자를 **3개 영역**으로 구분합니다.

- **① 어시스티브(Assistive)** — `BigQuery Assistant`
  - BigQuery Studio 우측 채팅 패널에서 SQL **바이브 코딩** 지원
  - 신규 SQL 작성, 기존 쿼리 트러블슈팅, **쿼리 최적화**, 느린 쿼리 탐지
  - Gemini in BigQuery 처리 데이터량이 1년 새 **30배** 증가

- **② 페르소나·태스크별 데이터 에이전트**
  - **데이터 엔지니어링 에이전트** — 자연어로 복잡한 데이터 파이프라인을 수 분 내 구축, 명세 검토·수정 가능 → **GA**
  - **데이터 사이언스 에이전트** — BigQuery `Colab` 노트북에서 데이터 탐색·피처링·ML 모델 빌드·정확도 검증 → **GA**
  - **대화형 분석 에이전트(Conversational Analytics)** — 비즈니스 사용자 대상, Looker는 11월부터 GA, **BigQuery 버전도 GA**

- **③ 프리미티브 API·툴** — `SDK`, `MCP API` 등으로 개발자가 직접 에이전트 구축·배포

신규 기능:
- **Deep Data Research (Deep Dive)** — Gemini Enterprise에서 구조화/비구조화/실시간 웹 데이터를 종합해 **장문 리포트** 생성
- **Agentic Workflows(프리뷰)** — 이벤트·스케줄 기반으로 에이전트 자동 트리거
- 에이전트를 **Data Studio** 및 **Gemini Enterprise**에 퍼블리싱 (allowlist 프리뷰)

---

## 💡 개발자 포인트

- **BigQuery 대화형 분석**은 과거 조회를 넘어 **예측·핵심 동인 분석·이상 탐지**까지 자연어로 수행 — 테이블·스키마·모델 지식 불필요
- **멀티모달 처리** 지원: 대용량 텍스트·이미지를 자연어 쿼리로 처리 가능
- 데모에서 `fix it` 한 번으로 `user_id`/`order_id` 혼동 버그 자동 수정, `SAFE_DIVIDE` 추가, 날짜 필터 기반 **파티션 프루닝** 최적화 시연

> 기존에 **몇 주~몇 달** 걸리던 ML 모델링·파이프라인 작업이 **수 분** 단위로 단축됨. 단, 에이전트가 생성한 명세·쿼리는 사람이 반드시 검토(human-in-the-loop)하는 구조로 설계됨.

- 에이전트는 **API로도 제공**되어 원하는 surface에 직접 배포 가능

---

## 📅 버전 / 출시 일정

| 기능 | 상태 |
| --- | --- |
| 데이터 엔지니어링 에이전트 | **GA** |
| 데이터 사이언스 에이전트 | **GA** |
| BigQuery 대화형 분석 | **GA** |
| Looker 대화형 분석 | GA (2025년 11월~) |
| Gemini Enterprise 퍼블리싱 | Allowlist 프리뷰 |
| Deep Data Research (Deep Dive) | 프리뷰 |
| Agentic Workflows | 프리뷰 |


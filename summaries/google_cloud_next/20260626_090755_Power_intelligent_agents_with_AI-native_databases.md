# Power intelligent agents with AI-native databases

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=7awKinJhGPo
- **요약 일시**: 2026-06-26 09:07:55

---

## 🔑 핵심 요약
- Google이 AI와 데이터 스택을 수직 통합한 새 카테고리 **Agentic Data Cloud**를 발표 — "데이터를 AI로 옮기는" 대신 "AI를 데이터로 가져오는" 전략
- **AI-native 데이터베이스 `AlloyDB`**가 핵심: 100% PostgreSQL 호환에 벡터·텍스트·그래프·시계열 검색과 Gemini 기반 `AI 함수`를 SQL 한곳에서 제공
- 에이전트가 기업 데이터를 신뢰성 있게 다루도록 **MCP 도구 + 자연어→SQL 인터페이스 + 지식 카탈로그**로 구성된 Data Agent 플랫폼 제공

---

## 📣 주요 발표 내용
- **Agentic Data Cloud** — 단순 인사이트가 아닌 에이전트를 위한 *system of action*. 오픈 표준(Postgres) 채택, 모델·데이터·실행 위치 자유 선택(BYO data/model)
- **3대 기둥**
  - **AI-native 데이터베이스**: 이미지·영상·시계열·그래프 등 멀티모달 데이터를 임베딩으로 저장, DB 내장 AI 모델로 처리
  - **Data Agent 플랫폼**: `MCP Toolbox`(오픈소스), 자연어 인터페이스, 신뢰 가능한 **Knowledge Catalog**(에이전트의 컨텍스트 중심)
  - **사전 구축(pre-built) 에이전트**: 개발자·운영자·비즈니스 사용자용, Conversational Analytics 포함
- **`AlloyDB`** 강화
  - Google 독자 **`ScanNN` 인덱스**(Google Search/YouTube 기반) — **100억+ 벡터** 지원
  - `pgvector`에 **컬럼형 엔진** 적용 → 표준 대비 **최대 4배 빠른 벡터 검색**, 설정 변경 불필요
  - **Hybrid Search**: 벡터 + 풀텍스트(**BM25 랭킹**) 결합을 SQL 함수로 제공
  - `AlloyDB Omni`로 온프레미스·타 클라우드·로컬 노트북 어디서나 실행
- **`AI 함수`** (Gemini 내장 지식 활용, 자연어로 프로그래밍 가능)
  - `AI.RANK`(리랭킹), `AI.IF`(필터), `AI.GENERATE`(주석/설명 생성)
  - 신규: `analyze sentiment`, `summarize` 함수
  - `FORECAST` 함수 — Google **`TimesFM`** 시계열 파운데이션 모델로 수개월 걸리던 예측을 초 단위로
- **자연어→SQL** 산업 표준 **BIRD 벤치마크 1위** 달성 (Conversational Analytics)
- **Anthropic**과 협력 — MCP 창시자 David Soria와 함께 모델 컨텍스트 프로토콜 표준 발전

---

## 💡 개발자 포인트
- 기존 데이터 사일로(분리된 웨어하우스·운영 DB)가 에이전트 도입의 최대 걸림돌 — 데이터 이동 없이 DB 내에서 AI를 실행해 **실시간 상태** 기반으로 에이전트 동작 가능
- `AlloyDB`는 관계형 스토어 + 고성능 벡터 스토어 + 분석 엔진(표준 Postgres 대비 **100배 빠름**)을 단일 destination으로 통합 → 별도 벡터 DB 운영 부담 감소
- 키워드 검색만으로는 부족 — **Hybrid Search로 top 1,000~2,000 후보 추출 후 `AI.RANK`로 의도 기반 리랭킹**하는 패턴이 권장됨 (예: "산토리니 여름에 맞는 셔츠" 같은 세계 지식 필요 쿼리)
> **비용 주의:** 신규 `AI.IF` 최적화 버전은 기본 LLM 호출 대비 **약 1,000배 비용 절감** — 대규모 AI 적용 시 최적화 함수 사용 여부가 비용을 크게 좌우함
- 에이전트는 **MCP 도구**로 DB에 접근 — Google `MCP Toolbox`(오픈소스)에 커뮤니티 기여 가능
- 인덱스 타입(ScanNN/HNSW)은 향후 **구현 디테일로 추상화** 예정 — 지금부터 특정 인덱스에 강하게 결합하지 않는 설계 권장

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| Agentic Data Cloud | 발표 (신규 카테고리) |
| AlloyDB 100억+ 벡터 / ScanNN | 지원 발표 |
| pgvector 컬럼형 엔진 (4배 가속) | 출시 예정(coming) |
| BM25 Hybrid Search | 출시 예정 기능 |
| AI 함수: analyze sentiment / summarize | 신규(올해) |
| AI.IF 최적화 버전 | GA |
| TimesFM (FORECAST) | 제공 중 |

> 세부 GA 날짜는 영상에서 명시되지 않음 — 일부 기능은 "coming/예정" 단계


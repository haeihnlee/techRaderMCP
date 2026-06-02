# AlloyDB AI: Revolutionizing Hybrid Search for PostgreSQL

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=gKHLlObVwrA
- **요약 일시**: 2026-06-02 09:05:07

---

## 🔑 핵심 요약
- **AlloyDB AI**가 PostgreSQL에 **키워드(Full-text) + 벡터(Semantic) 하이브리드 검색**을 통합해, 일주일짜리 리서치를 클릭 몇 번으로 단축
- 자체 **`ScaNN`** 인덱스(14년 구글 연구 기반)로 **100억+ 벡터** 규모의 필터 검색을 표준 Postgres 대비 **최대 10배 빠르게** 처리
- DB 내부에서 임베딩 생성·`AI summarize`·`AI generate` 등 **Gemini 기반 AI 함수**를 SQL로 직접 호출

---

## 📣 주요 발표 내용
- **인라인 임베딩 생성**: `embeddings` 함수로 복잡한 파이프라인이나 async Python 없이 수백만 개 임베딩을 수 분 만에 생성
- **다양한 벡터 인덱스 지원**
  - **`ScaNN`**: 구글 산업 표준 알고리즘, 100억+ 벡터 확장 + 필터 검색
  - **`HNSW`**: AlloyDB **컬럼형 엔진** 가속으로 최대 **4배 빠름**
- **Full-text 검색 강화**
  - 네이티브 **`GIN` 인덱싱** 지원
  - 신규 **`rum` 확장**으로 최신 수준의 전문 검색 성능 제공
  - **`BM25` 네이티브 지원 예정**(coming soon)
- **하이브리드 검색 + 리랭킹**: **`RRF`(Reciprocal Rank Fusion)** 또는 Vertex AI의 **`semantic-ranker-512`** 등 다양한 랭킹 모델로 재정렬, **자체 모델(BYO)** 도 연동 가능
- **DB 내장 AI 함수**: `AI summarize`로 핵심 리스크 추출, `AI generate`로 최신 기업 개요 생성 — Gemini의 지식을 SQL에서 바로 활용

---

## 💡 개발자 포인트
- 임베딩 생성을 DB 함수로 위임하면 **별도 ETL/임베딩 파이프라인 코드가 불필요** → 운영 부담 감소
- 키워드 검색의 **이진(binary) 한계**(예: "shipping"으로 검색 시 "Maritime" 문서 누락)를 시맨틱 검색으로 보완

> 동일 하이브리드 쿼리가 기존 방식에서는 **90초 이상** 걸리던 것이 AlloyDB에서는 **서브초(sub-second)** 로 단축 — 대규모 RAG/검색 워크로드의 지연 병목 해소에 직접적 영향

- 기존 **Oracle / SQL Server** 워크로드를 PostgreSQL 호환 AlloyDB로 현대화하는 마이그레이션 시나리오에 적합

---

## 📅 버전 / 출시 일정
| 기능 | 상태 |
| --- | --- |
| `ScaNN` / `HNSW` 벡터 인덱스 | 사용 가능 |
| `GIN` 인덱싱, `rum` 확장 | 사용 가능 |
| `RRF` 리랭킹, Vertex AI 랭킹 모델 연동 | 사용 가능 |
| 네이티브 **`BM25`** 지원 | **출시 예정 (coming soon)** |

> 구체적 GA 날짜는 영상에서 언급되지 않음 — 도입 검토 시 Google Cloud 팀 문의 권장

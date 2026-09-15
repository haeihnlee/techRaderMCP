# Introducing BM25 on AlloyDB & Cloud SQL

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=-JxQb-kjFHk
- **요약 일시**: 2026-09-15 09:09:19

---

## 🔑 핵심 요약
- **AlloyDB**와 **Cloud SQL**에 **BM25** 풀텍스트 검색 랭킹이 네이티브로 지원됨
- 기존 벡터 검색과 결합한 **하이브리드 검색**을 단일 DB에서 처리 가능 — 별도 검색 DB 불필요
- `pgtermsearch` 익스텐션(TigerData 개발)을 통해 `CREATE INDEX ... USING BM25` 한 줄로 설정

---

## 📣 주요 발표 내용
- **AlloyDB 벡터 성능 개선 현황**
  - `SCAN` 인덱스: 필터링 워크로드에서 표준 HNSW 대비 **최대 10배 빠름**
  - **100억 벡터** 규모까지 확장 가능, 메모리 사용량 **4배 절감**
  - 컬럼형 엔진 가속으로 표준 HNSW 대비 **4배 빠른 성능**
- **BM25 네이티브 지원** — `pgtermsearch` 익스텐션으로 Postgres 안에서 직접 사용
  - `term frequency`, `inverse document frequency`, `document length normalization` 기반 랭킹
  - 파라미터 `K1`(반복 단어 가중치), `B`(문서 길이 페널티)로 세밀한 튜닝 가능
- **인덱스 선택 가이드**

  | 인덱스 | 적합한 경우 |
  |--------|------------|
  | `GIN` | JSON·블로그·멀티테넌트 태그 필터링, 범용 |
  | `RUM` | 법률 문서 등 정확한 구문 검색 (디스크 사용량 ↑) |
  | `BM25` | Gen AI RAG, 알고리즘 기반 현대적 관련성 랭킹 |

- **하이브리드 검색 쿼리 구성**: Vector Search CTE + BM25 Text Search CTE → `FULL OUTER JOIN` + **Reciprocal Rank Fusion(RRF)** 스코어 결합
- `hybrid_search` UDF에서 BM25 인덱스 지원 추가 예정 (곧 출시)

---

## 💡 개발자 포인트
- Postgres 기본 `ts_rank`는 대규모에서 성능 저하 및 키워드 스터핑에 취약 — **BM25로 대체 권장**
- BM25 인덱스 생성 예시:
  ```sql
  CREATE EXTENSION pgtermsearch;
  CREATE INDEX bm25_idx ON products USING bm25 (description)
    WITH (text_config = 'english', k1 = 1.2, b = 0.75);
  ```
- BM25 검색 시 특수 연산자(`@@` 계열) 사용, **낮은(더 음수) 스코어 = 높은 관련성**
- RAG 파이프라인 구현 시 희귀 단어(`cherry`)가 일반 단어(`tree`)보다 높은 점수 — 직관과 다를 수 있으므로 주의

> BM25 랭킹 방향: **더 음수에 가까울수록 관련성이 높음** — `ORDER BY score ASC` 사용

---

## 📅 버전 / 출시 일정
| 항목 | 상태 |
|------|------|
| BM25 on AlloyDB & Cloud SQL | 현재 사용 가능 (`pgtermsearch` 익스텐션) |
| `hybrid_search` UDF BM25 지원 | 곧 출시 예정 (Stay tuned) |

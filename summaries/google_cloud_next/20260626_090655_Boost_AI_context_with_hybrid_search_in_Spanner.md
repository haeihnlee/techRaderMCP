# Boost AI context with hybrid search in Spanner

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=fAf4Zh-CC08
- **요약 일시**: 2026-06-26 09:06:55

---

## 🔑 핵심 요약
- **Cloud Spanner**가 검색 전용 플랫폼을 따로 두지 않고 **Full-text · Vector · Hybrid 검색**을 한 DB 안에서 제공 — Google Drive·Gmail·YouTube·Uber 등이 이미 사용 중
- **Hybrid search**는 키워드 검색과 벡터(의미) 검색 결과를 **RRF(Reciprocal Rank Fusion)**로 병합해 두 방식의 장점을 결합
- CRM 스타트업 **Attio** 사례: Postgres 쿼리 플래너 한계로 2021년 Spanner 전환, 정형·비정형 데이터를 단일 레이어(`Universal Context`)로 통합

---

## 📣 주요 발표 내용
- **Spanner = 멀티모델 데이터 플랫폼**: 동일 데이터로 관계형(OLTP)·검색·그래프 워크로드를 데이터 복제 없이 처리
- 검색 3종 기능
  - **Full-text search**: 키워드 검색 + **fuzzy search**(오타·동의어 매칭)
  - **Vector search**: AI로 데이터 의미를 이해해 문맥 기반 검색 (예: `space LEGO for 8 plus`)
  - **Hybrid search**: 위 둘을 **RRF**로 병합해 랭킹
- 데모: 동일 쿼리에서 full-text(2건) → vector(더 많지만 age 4–7 등 부정확 포함) → hybrid(전부 8+ 매칭, 품질 최상)로 결과 개선 시연
- **운영 이점**: 별도 검색 엔진 불필요 → ETL 파이프라인·데이터 중복·**data lag(stale 결과)** 문제 제거
- 가용성: 업계 최고 수준 **5 nines(99.999%) SLA**, near-limitless 확장성

---

## 💡 개발자 포인트
- **데이터를 한 곳에 유지**: 검색을 위해 다른 시스템으로 데이터를 복사할 필요가 없어 ETL·중복·스테일 데이터 이슈가 사라짐

> **주의:** 별도 검색 플랫폼을 운영하면 DB → 검색엔진 복제 과정에서 **data lag**이 발생해 오래된(stale) 검색 결과를 반환할 수 있다. Spanner는 트랜잭션 일관성으로 이를 방지.

- **Query hints로 쿼리 플랜 직접 지정** 가능 (Oracle 계열과 유사) — `join order`, `join method`, `parallelism`을 개발자가 명시
  - 수만~수십만 테넌트의 **멀티테넌트 워크로드**에서 옵티마이저가 좋은 판단을 못 할 때, hint로 **결정적(deterministic) 쿼리 플래닝**과 **tail latency** 제어 확보
- **Global external consistency**: API 요청·MCP 서버가 트랜잭션 일관성 있는 데이터를 조회 → 사람과 AI 에이전트 모두에게 일관된 컨텍스트 제공
- Attio는 정형 데이터(딜 소유자·금액)와 비정형 데이터(이메일·통화 녹취·제품 사용 로그)를 **Boolean·Vector·Full-text 검색**으로 한 번에 노출

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| ---- | ---- |
| Spanner 쿼리 옵티마이저 | 버전 8 (발표 시점) |
| Attio Postgres → Spanner 전환 | 2021년 (집중 워크로드 이전) |
| Attio 관계형 워크로드 전면 이전 | 2022년 초 |
| SLA | 99.999% (5 nines) |


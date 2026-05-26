# AlloyDB Lakehouse Federation: Unified access to BigQuery and Google Cloud Lakehouse

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=ZmstWYjUPiA
- **요약 일시**: 2026-05-26 09:03:52

---

## 🔑 핵심 요약
- **AlloyDB Lakehouse Federation**으로 OLTP DB에서 **BigQuery**와 **Iceberg/Parquet 데이터 레이크**를 데이터 이동 없이 단일 쿼리로 조인 가능
- 벡터 검색(임베딩 기반 시맨틱 검색) 결과를 BigQuery 재무 참조 데이터와 즉시 조인하여 분석 가속화
- **One-click Reverse ETL**로 BigQuery 데이터를 AlloyDB 로컬 테이블로 자동 동기화하여 초저지연 쿼리 지원

---

## 📣 주요 발표 내용
- **AlloyDB Lakehouse Federation** 신규 기능 공개
  - AlloyDB를 **단일 액세스 레이어(unified access layer)**로 사용
  - 연결 문자열 변경이나 추가 데이터 소스 관리 없이 외부 데이터 쿼리
- **벡터 검색 + 외부 데이터 조인**
  - 데모: S&P 500 10-K 보고서 **320만 개 텍스트 청크/임베딩**을 AlloyDB에 저장
  - 자연어로 시맨틱 검색 후 BigQuery의 매출/영업이익 데이터와 즉석 조인
- **자동 푸시다운(pushdown)** 지원
  - 필터·집계(aggregate)를 BigQuery로 푸시하여 성능 및 정확도 유지
- **One-click Reverse ETL**
  - BigQuery → AlloyDB 로컬 테이블 정기 동기화
  - 참조 데이터 접근 시 성능 트레이드오프 0
- **Apache Iceberg / Parquet** 직접 쿼리
  - 데이터 레이크에 아카이브된 과거 10-K Parquet 데이터를 그대로 조회

---

## 💡 개발자 포인트
- **트랜잭션 DB + DW + 데이터 레이크**를 한 SQL 인터페이스에서 다룰 수 있어 ETL 파이프라인 단순화
- **벡터 검색이 일반 SQL과 동일 컨텍스트**에서 동작 → RAG 워크로드의 메타데이터 필터링이 훨씬 자연스러워짐
- 지연 시간 요구사항에 따라 두 가지 패턴 선택 가능:

| 패턴 | 사용 시점 | 데이터 위치 |
|------|----------|-----------|
| **Federation (pushdown)** | 데이터 이동 없이 즉시 조회 | 원본(BigQuery/Iceberg) 그대로 |
| **Reverse ETL** | 초저지연이 필요할 때 | AlloyDB 로컬 테이블로 복제 |

> **참고:** Federation은 푸시다운 덕에 빠르지만, 가장 낮은 latency가 필요한 트랜잭션성 워크로드에서는 Reverse ETL 패턴이 권장됨

- 레거시 **Oracle/SQL Server → AlloyDB** 마이그레이션 사례(Cymbal Investments)에서 실제 활용 시나리오 제시

---

## 📅 버전 / 출시 일정
해당 없음 (영상에서 정확한 GA/Preview 일정은 언급되지 않음 — Google Cloud 영업팀 문의 안내)


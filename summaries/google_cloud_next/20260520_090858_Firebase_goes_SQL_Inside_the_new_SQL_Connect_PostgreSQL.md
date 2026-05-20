# Firebase goes SQL: Inside the new SQL Connect (PostgreSQL)

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=SOoBKKDO0Lc
- **요약 일시**: 2026-05-20 09:08:58

---

## 🔑 핵심 요약
- Firebase가 작년 Cloud Next에서 발표한 **Data Connect**를 **SQL Connect**로 리브랜딩하며 본격적인 **PostgreSQL 기반 SQL DB** 제품으로 진화
- **실시간 갱신**(`@refresh`), **Custom Resolvers**, **Native SQL**, **Caching**, **Transactions**, **Views** 등 신기능 대거 추가
- 스키마/쿼리만 **GraphQL**로 정의하면 iOS·Android·Web·Flutter용 **강타입 SDK 자동 생성** → 별도 백엔드·미들웨어 불필요

---

## 📣 주요 발표 내용
- **데이터 모델링**: `GraphQL` DDL로 테이블·외래키·기본값 정의. Firebase Auth와 통합된 server value(`auth.uid`) 직접 사용 가능
- **실시간(Real-time) 지원**: 새 `@refresh` 디렉티브로 mutation 실행 시 query 자동 재실행
  - 조건부 갱신 (특정 사용자, 특정 임계값) 또는 시간 인터벌 기반 갱신 지원
- **Custom Resolvers**: `Cloud Functions`를 통해 외부 API 읽기/쓰기 가능 (예: X API 호출, Gemini로 헤드라인 자동 생성)
- **Native SQL**: PostgreSQL **확장 풀 활용** 가능
  - **`pgvector`** → 벡터 검색 (예: "apple" 검색 시 phone·computer 같은 의미적 유사 결과)
  - **`PostGIS`** → 지리 검색 (주변 사용자 기반 쿼리)
- **Transactions**: `@transaction` 디렉티브로 여러 mutation/query를 원자적(atomic)으로 묶기. 변수 전달 가능, 하나 실패 시 전체 롤백
- **Views**: SQL View를 강타입 GraphQL SDK로 호출 (예: "특정 종목 최대 보유자" 같은 집계 쿼리)
- **Access Control**: role 기반 권한 체크를 쿼리 안에서 직접 정의

---

## 💡 개발자 포인트
- 쿼리 작성 방식에 따라 **타입 안정성 트레이드오프**가 다름:

  | 방식 | 타입 안정성 | 자유도 |
  |------|------------|--------|
  | Native GraphQL | ✅ 강타입 | 단순 쿼리만 |
  | SQL View | ✅ 강타입 | SQL 작성 가능 |
  | Pure Native SQL | ❌ `any` 반환 | 자유롭게 작성 (클라이언트에서 타입 정의 필요) |

- `auth.uid`를 **서버 값으로 직접 주입**하기 때문에 클라이언트가 user id를 전달할 필요 없음 → **스푸핑/DDOS 방어**에 유리

> ⚠️ **Firestore(NoSQL) 사용자 주의**: SQL Connect는 별도 제품이며, 관계형 스키마·외래키·트랜잭션이 필요한 신규 프로젝트에 적합. 기존 Firestore 앱을 자동 마이그레이션하지 않음

- **지원 플랫폼**: `iOS`, `Android`, `Web`, `Flutter` 클라이언트 SDK + 서버용 **Admin SDK** 제공
- 피드백·기능 요청은 **Firebase UserVoice**에 `#SQLConnect` 태그로 제출

---

## 📅 버전 / 출시 일정

| 항목 | 상태 |
|------|------|
| SQL Connect (Data Connect 리브랜딩) | **Cloud Next에서 발표** (현재 사용 가능) |
| `@refresh` 디렉티브 (real-time) | **Next에서 신규 출시** |
| Custom Resolvers / Native SQL / Views / Transactions | **신규 발표 기능** |


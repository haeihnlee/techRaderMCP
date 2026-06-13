# Converting SQL Server code to PostgreSQL

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=MGNPQZiUl6c
- **요약 일시**: 2026-06-13 09:03:44

---

## 🔑 핵심 요약
- **Google Cloud Database Migration Service(DMS)**가 SQL Server(T-SQL) 스키마를 **PostgreSQL**로 자동 변환해주는 과정을 시연
- DMS는 단순 변환을 넘어 **Gemini** 연동으로 각 변환의 이유와 Postgres 관용 표현(idiomatic pattern)을 설명해주는 "학습 도우미" 역할 수행
- `IDENTITY`, `BIT`, `GETDATE()` 등 T-SQL 고유 문법이 Postgres 표준 문법으로 어떻게 매핑되는지 구체적으로 소개

---

## 📣 주요 발표 내용
- SQL Server의 `CREATE TABLE` 문을 DMS **Conversion Workspace**에 넣으면 Postgres 버전이 자동 생성됨
- 자동 증가 키: T-SQL `IDENTITY` → Postgres `GENERATED AS IDENTITY` (SQL 표준 준수 문법)로 변환
  - Postgres 10 이전에는 `SERIAL` 의사 타입(pseudo type)을 사용했다는 버전 차이까지 Gemini가 설명
- 불리언 플래그: T-SQL `BIT` → Postgres `BOOLEAN`으로 매핑 (true/false 값의 관용적 타입)
- 타임스탬프 기본값: T-SQL `GETDATE()` → Postgres `LOCALTIMESTAMP`로 변환
  - `LOCALTIMESTAMP`는 트랜잭션 시작 시점의 **시간대 정보 없는 현재 시각**을 반환하는 표준 함수
- 타입 매핑: `DATETIME2` → `TIMESTAMP WITHOUT TIME ZONE`(축약형 `TIMESTAMP`)으로 정밀도와 시간대 비인식 동작 유지

---

## 💡 개발자 포인트
- 기존 SQL Server 스키마를 그대로 활용해 Postgres 문법을 학습할 수 있어, 마이그레이션과 학습을 동시에 진행 가능
- 플래그 컬럼을 `INT`로 만드는 흔한 실수 대신 Postgres가 제공하는 `BOOLEAN` 타입을 사용할 것

> **주의**: 자동 증가 키는 구버전 방식인 `SERIAL`이 아닌 SQL 표준인 `GENERATED AS IDENTITY` 사용이 권장됩니다. 또한 `GETDATE()`의 올바른 대응은 시간대 비인식 동작을 유지하는 `LOCALTIMESTAMP`입니다.

- 낯선 키워드를 만날 때마다 검색할 필요 없이 DMS + Gemini가 인라인으로 설명해주므로 변환 패턴을 익히며 빠르게 진행 가능

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| PostgreSQL 10 이전 | 자동 증가 키에 `SERIAL` 의사 타입 사용 |
| PostgreSQL 10 이후 | SQL 표준 `GENERATED AS IDENTITY` 권장 |

DMS Conversion Workspace는 현재 사용 가능하며 별도 출시 일정은 언급되지 않았습니다.

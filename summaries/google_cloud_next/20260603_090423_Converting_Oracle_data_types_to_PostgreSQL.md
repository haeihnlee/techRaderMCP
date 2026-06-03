# Converting Oracle data types to PostgreSQL

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=bxfqwGdoS2w
- **요약 일시**: 2026-06-03 09:04:23

---

## 🔑 핵심 요약
- **Google Cloud Database Migration Service(DMS)** 의 **Conversion Workspace** 를 이용한 Oracle → PostgreSQL 스키마 자동 변환 데모
- 단순 변환에 그치지 않고 **Gemini** 가 각 데이터 타입 변환 이유를 실시간으로 설명해주는 **"타입 튜터"** 역할 수행
- Oracle과 PostgreSQL의 미묘한 타입 차이(`varchar2`, `number`, `date`)로 인한 마이그레이션 함정을 학습하며 신뢰 기반으로 전환

---

## 📣 주요 발표 내용
- **DMS Conversion Workspace** 에서 Oracle 소스를 연결하면 좌측 원본 Oracle DDL, 우측 자동 변환된 **Cloud SQL for PostgreSQL** 코드를 나란히 표시
- 변환된 라인을 클릭해 **Gemini** 에게 "왜 이렇게 변환됐는지" 설명 요청 가능
- 세 가지 핵심 타입 변환 사례 시연:
  - `varchar2` → `varchar` : Oracle 전용 타입을 표준 SQL 타입으로 매핑
  - `number` → `decimal` : 정밀도(precision)·스케일(scale) 보존
  - `date` → `timestamp without time zone` : 날짜+시간 컴포넌트 모두 보존

---

## 💡 개발자 포인트
- **`varchar2` → `varchar`**: Oracle은 길이가 **byte 또는 character** 둘 다 의미할 수 있지만, PostgreSQL은 **항상 character** 기준 → 멀티바이트 언어 처리가 단순해짐
- **`number` → `decimal`**: 금융 데이터의 정확한 정밀도·스케일 유지에 필수. 정수 전용 컬럼이라면 성능을 위해 `bigint` 사용을 DMS가 제안하기도 함

> ⚠️ **`date` 타입 주의 (대표적 마이그레이션 함정)**
> Oracle의 `date` 타입은 실제로 **날짜 + 시간(초 단위까지)** 을 함께 저장합니다.
> 이를 PostgreSQL `timestamp` 로 매핑해야 **시간 데이터의 묵시적 절단(silent truncation)** 을 방지할 수 있습니다.

- 자동 변환을 맹목적으로 수용하지 말고 **Gemini 설명과 상호작용** 하며 검증 → 인지 부하(cognitive load) 감소 + 견고한 DB 기반 확보

---

## 📅 버전 / 출시 일정
해당 없음 (제품 데모 — 별도 버전·출시 일정 정보 없음)

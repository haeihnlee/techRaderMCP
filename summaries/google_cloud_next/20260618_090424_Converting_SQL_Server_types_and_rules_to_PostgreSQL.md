# Converting SQL Server types and rules to PostgreSQL

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=W4nKY6Tk_eQ
- **요약 일시**: 2026-06-18 09:04:24

---

## 🔑 핵심 요약
- **Database Migration Service(DMS)**가 SQL Server → PostgreSQL 마이그레이션 시 스키마에 담긴 **비즈니스 규칙까지 자동 이전**한다.
- SQL Server의 **사용자 정의 타입(User Defined Type)**을 PostgreSQL의 **`DOMAIN`** 으로 변환하며, 부착된 **`CHECK` 제약조건**도 함께 가져온다.
- 동일 타입이 여러 테이블에 쓰여도 규칙을 **한 번만 정의**하므로 수작업 제약조건 추가에서 오는 휴먼 에러를 제거한다.

---

## 📣 주요 발표 내용
- SQL Server에서는 `varchar` 기반 **사용자 정의 타입**(예: 전화번호·이메일)에 `CHECK` 규칙을 붙여 스키마 레벨에서 검증을 강제할 수 있다.
- **DMS**는 이 타입을 단순히 베이스 타입으로만 변환하지 않고, PostgreSQL의 표준 SQL 기능인 **`DOMAIN`** 으로 변환한다.
- 변환 과정에서 원본의 **`CHECK` 제약조건을 그대로 이식**하여 데이터 무결성을 보존한다.
- `DOMAIN`은 자체 제약조건을 가진 커스텀 데이터 타입으로, **PostgreSQL에서 사용자 정의 타입에 대응하는 관용적(idiomatic) 표현**이다.
- DMS의 **Conversion Workspace**에서 전체 스키마와 규칙을 함께 변환·검증할 수 있다.

---

## 💡 개발자 포인트
- SQL Server 사용자 정의 타입을 PostgreSQL로 옮길 때, `DOMAIN`을 쓰면 검증 로직을 **타입 정의 한 곳에 중앙화**할 수 있다.

> **핵심 이점:** 전화번호 타입이 10개 테이블에 사용되더라도, 각 컬럼에 `CHECK` 제약을 일일이 추가할 필요 없이 **DMS가 규칙을 한 번만 마이그레이션**한다. 수동 작업으로 인한 누락·오타 위험이 사라진다.

- 단순 데이터 이동이 아니라 수년간 스키마에 축적한 **검증 규칙·안전장치(intelligence & safeguards)까지 함께 이전**된다는 점이 마이그레이션 품질의 핵심이다.

---

## 📅 버전 / 출시 일정
해당 없음

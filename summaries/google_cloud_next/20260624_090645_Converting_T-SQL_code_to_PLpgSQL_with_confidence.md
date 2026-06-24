# Converting T-SQL code to PL/pgSQL with confidence

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=eHnUcar6tL4
- **요약 일시**: 2026-06-24 09:06:45

---

## 🔑 핵심 요약
- **Database Migration Service(DMS)**가 `T-SQL` 저장 프로시저를 단순 직역이 아니라 **Postgres 모범 패턴으로 지능적 현대화**하며 변환
- 임시 테이블·커서 기반의 절차적 로직을 **CTE(Common Table Expression) 기반 set-based 방식**으로 자동 리팩토링
- 변환 결과를 **Gemini**가 *왜 더 나은지*까지 설명해 성능 튜닝 기법을 함께 학습 가능

---

## 📣 주요 발표 내용
- 예시: `get high value customers` 라는 `T-SQL` 프로시저 — 임시 테이블 생성 → 초기 데이터 삽입 → 추가 정보로 업데이트 → 결과 조회하는 전형적 **절차적(procedural) 패턴**
- **DMS** 변환 결과는 임시 테이블을 만들지 않고, 전체 다단계 프로세스를 **단일 Postgres 함수 + CTE**로 재구성
- 단순 line-for-line 번역이 아니라 **코드의 의도(intent)를 인식**해 우수한 패턴으로 구현
- **Gemini**가 변환 근거를 설명: 임시 테이블을 CTE로 바꿔 **set-based 접근**을 유도 (Postgres 표준 방식)

---

## 💡 개발자 포인트
- **set-based + CTE** 방식의 성능 이점: Postgres **쿼리 플래너가 전체 연산을 하나의 단위로 인식** → 더 효율적인 실행 계획 생성, 물리적 임시 테이블의 쓰기/읽기 대비 **IO 감소**

> 기존 `T-SQL`의 임시 테이블·커서 패턴을 그대로 옮기면 동작은 하지만 비효율적입니다. DMS는 레거시 패턴을 현대적 Postgres 패턴으로 **리팩토링**하므로, 마이그레이션 결과물의 쿼리 구조가 원본과 달라질 수 있음에 유의하세요.

- 복잡한 레거시 코드일수록 **마이그레이션 = 현대화** 기회로 활용 가능 (best practice 내장)

---

## 📅 버전 / 출시 일정
해당 없음

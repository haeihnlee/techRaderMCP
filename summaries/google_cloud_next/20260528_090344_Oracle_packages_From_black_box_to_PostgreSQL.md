# Oracle packages: From black box to PostgreSQL

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=cZdv9ySzkOA
- **요약 일시**: 2026-05-28 09:03:44

---

## 🔑 핵심 요약
- **Google Cloud Database Migration Service(DMS)**가 Oracle의 `PL/SQL 패키지`를 PostgreSQL로 단순 이전이 아닌 **지능형 리팩토링**으로 변환
- PostgreSQL에는 `package` 개념이 없어 발생하던 마이그레이션 장벽을, DMS가 **전용 스키마(schema) 컨테이너**로 자동 변환해 해결
- **Gemini 기반 설명 기능(explainability)**으로 변환 결과의 "왜(why)"까지 설명해 팀의 코드 신뢰·유지보수 지원

---

## 📣 주요 발표 내용
- **DMS Code Conversion**: Oracle 소스 DB를 연결하면 `packages` 노드 등 모든 객체를 좌측 패널에서 탐색 가능
- 예시로 분기별 재무 리포팅 로직이 담긴 `Reports` 패키지를 선택해 변환 시연
- DMS는 흩어진 함수들로 쪼개지 않고, 원본 패키지의 모든 로직을 담는 **전용 PostgreSQL 스키마**를 생성
  - 원본 코드의 **논리적 그룹화(logical grouping)**와 **캡슐화(encapsulation)** 구조를 그대로 보존
- **Gemini "Explain the conversion logic" 프롬프트**로 변환 객체별 로직 설명 제공
  - "스키마 생성은 PostgreSQL에서 네임스페이싱을 구현하는 관용적(idiomatic) 방식"임을 확인·교육

---

## 💡 개발자 포인트
- 수십 년간 누적된 핵심 비즈니스 로직이 잠긴 Oracle 패키지를, 느리고 비싼 수작업 리팩토링 없이 자동 변환 가능
- 단순 변환이 아니라 **올바른 아키텍처 패턴(스키마 기반 네임스페이싱)을 팀에 학습**시켜 줌

> **주의:** PostgreSQL에는 Oracle `package`에 대응하는 1:1 구조가 없습니다. DMS는 이를 **별도 스키마**로 매핑하므로, 마이그레이션 후 호출 경로·네임스페이스 참조가 바뀐다는 점을 코드 전반에서 확인해야 합니다.

- 대상 환경은 **Cloud SQL for PostgreSQL** 인스턴스이며 변환 결과는 Conversion Workspace의 draft 패널에서 검토

---

## 📅 버전 / 출시 일정
해당 없음 (Google Cloud 무료 체험 및 DMS 문서 참고 안내)

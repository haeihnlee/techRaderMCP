# Automatic Read Scaling with AlloyDB Transparent Query Forwarding (TQF)

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=iofy_GTwt3E
- **요약 일시**: 2026-05-12 09:12:49

---

## 🔑 핵심 요약
- **AlloyDB**에 신규 도입된 `Transparent Query Forwarding (TQF)`로 **읽기 쿼리를 자동으로 read pool에 분산**하는 기능 공개
- 애플리케이션 코드 수정·엔드포인트 변경 없이 **primary 인스턴스의 부하를 자동 분리** 가능
- `read-after-write consistency` 지원으로 **stale data 문제 없이** 트래픽 자동 라우팅

---

## 📣 주요 발표 내용
- Cymbal Investments(가상 금융사) 시나리오로 시연: Oracle/SQL Server → **AlloyDB** 마이그레이션 환경
- 시장 개장 시 30% 쓰기 + 70% 읽기 트래픽 시뮬레이션, TQF 비활성 시 **100% primary 집중**
- TQF 활성화 시 AlloyDB가 **읽기 전용 쿼리를 자동 식별**해 read pool로 포워딩
- Read pool은 옵션으로 **columnar engine**을 활용해 분석 쿼리 가속 가능
- 표준 PostgreSQL 대비 **25배 이상 빠른 replication** 성능으로 read-after-write consistency 보장

---

## 💡 개발자 포인트
> **Breaking-point 없는 도입**: 애플리케이션 코드 재작성이나 별도 read 엔드포인트 분리 없이 단순히 TQF 토글만으로 read scaling 적용 가능

- 기존에는 read-only 워크로드를 수동으로 찾아 다른 엔드포인트로 지정하거나 앱을 재설계해야 했음 → TQF가 이를 **자동화**
- **OLTP + 분석 쿼리 혼합** 워크로드(예: 고빈도 트레이딩, 실시간 대시보드)에 적합
- Read pool로 forwarding되더라도 `read-after-write` 정합성이 보장되므로 **eventual consistency 우회 코드 불필요**
- Primary는 **write 전용**으로 격리되어 CPU 경합 감소 → mission-critical 트랜잭션 지연 최소화

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 제품 | **AlloyDB for PostgreSQL** |
| 기능명 | `Transparent Query Forwarding (TQF)` |
| 출시 상태 | 발표 시점 신규 공개 (자세한 GA 일정은 Google Cloud 영업팀 문의) |
| 관련 기능 | Columnar engine, 25x faster replication |


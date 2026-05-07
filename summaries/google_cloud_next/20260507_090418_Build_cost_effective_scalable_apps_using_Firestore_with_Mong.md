# Build cost effective, scalable apps using Firestore with MongoDB compatibility

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=I1ouAtwryww
- **요약 일시**: 2026-05-07 09:04:18

---

## 🔑 핵심 요약
- **Firestore**가 **MongoDB 호환 API**를 정식 지원하여, 기존 MongoDB 코드·드라이버·툴을 그대로 재사용 가능
- **서버리스 문서 DB**로 인프라 관리 부담 없이 무한 확장과 **5-nines(99.999%) SLA** 제공
- 실시간 구독 쿼리·오프라인 캐싱·**Gemini/RAG** 통합으로 AI 앱 개발에 최적화

---

## 📣 주요 발표 내용
- **MongoDB 호환성**: 기존 MongoDB 호환 DB 사용자라면 코드 변경 없이 Firestore로 마이그레이션 가능
- 고급 **Aggregation Pipeline** 지원 — `count`, `group`, `lookup` 등 수백 개의 MongoDB 호환 연산자/스테이지 사용 가능
- **라이브 스트리밍 마이그레이션 도구** 제공 → 다운타임 최소화
- **실시간 Push 기반 동기화** 내장: WebSocket·폴링 없이 SDK가 최신 데이터로 자동 갱신
- **Generative AI 생태계 통합**: RAG, Gemini CLI, 코드 에디터 직접 연동
- **엔터프라이즈 거버넌스**: `IAM`, `VPC`, **CMEK**(고객 관리 암호화 키) 지원
- **멀티 리전 복제** 및 Google Cloud 통합 리소스 관리

---

## 💡 개발자 포인트
- 기존 MongoDB 앱을 운영 중이라면 **드라이버·툴체인 변경 없이** 서버리스 환경으로 전환 가능 → DevOps의 샤드/서버 관리 부담 제거
- `Firestore SDK`의 **실시간 구독**과 오프라인 캐싱은 모바일·웹 앱에서 별도 동기화 인프라 구축 없이 사용 가능
- AI 에이전트 구축 시 Firestore 데이터 + 사용자 쿼리 → **RAG 파이프라인**에 바로 투입 가능
- **`Gemini CLI`** 또는 코드 에디터에서 Firestore를 직접 호출하는 워크플로우 구성 가능

> **과금 모델 주의**: 용량(capacity) 기반이 아닌 **read / write / delete operation 단위 과금**. 트래픽 패턴에 따라 비용 예측·최적화 전략을 새로 설계할 것.

> **Greenfield vs. Migration** 모두 타깃: 신규 프로젝트면 Free Tier로 즉시 시작, 기존 MongoDB 워크로드면 라이브 스트리밍 모드로 무중단 이전을 권장.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| 가용성 SLA | 99.999% (5-nines) |
| Free Tier | 제공 중 (즉시 시작 가능) |
| 상세 출시일 | 해당 없음 (영상 내 미공개) |


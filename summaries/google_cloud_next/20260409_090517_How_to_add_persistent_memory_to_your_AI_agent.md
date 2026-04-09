# How to add persistent memory to your AI agent

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=HDqzJJhZsxw
- **요약 일시**: 2026-04-09 09:05:17

---

## 핵심 요약 (3줄)
- ADK(Agent Development Kit)의 세션 서비스를 In-Memory에서 Database Session Service로 교체하여 앱 재시작 후에도 대화 이력을 유지할 수 있다
- 사용자별 장기 선호도(채식주의, 관심 테마 등)를 저장하는 User Profile Store를 별도 DB 테이블로 구성하여 새로운 세션에서도 개인화가 가능하다
- 에이전트에 `recall_user_preference` / `save_user_preference` 두 가지 툴을 부여하고, 시스템 프롬프트로 호출 순서를 명시적으로 지시하는 것이 핵심 설계 패턴이다

---

## 주요 발표 내용

- **Persistent Session Service 도입**
  - 기존 `InMemorySessionService` → `DatabaseSessionService`로 교체
  - SQLite 파일 또는 PostgreSQL 등 실제 DB에 모든 메시지·상태 변경사항 저장
  - `get_or_create_session()` 헬퍼 함수로 기존 세션 재개 또는 신규 생성 처리

- **ADK 세션 서비스 3종 비교**
  | 타입 | 특징 |
  |------|------|
  | `InMemorySessionService` | 빠르지만 재시작 시 초기화 |
  | `DatabaseSessionService` | 직접 DB 관리, 재시작 후에도 대화 유지 |
  | `VertexAI SessionService` | Google Cloud 관리형, 다음 에피소드에서 상세 다룸 |

- **User Profile Store 설계**
  - `(user_id, preference_key, preference_value)` 구조의 단순 테이블
  - 키 예시: `dietary`, `favorite_theme`, `transport_mode`
  - 두 가지 에이전트 툴 제공: `recall_user_preference`, `save_user_preference`
  - 각 툴은 context에서 `user_id`를 자동으로 참조하여 사용자별 격리 보장

- **에이전트 시스템 프롬프트 설계 패턴**
  - 대화 시작 시 → `recall_user_preference` 먼저 호출
  - 조회 결과 기반으로 즉시 개인화 응답 생성
  - 대화 종료 전 → 새로운 사실 발견 시 `save_user_preference` 호출

---

## 개발자에게 중요한 포인트

- **에이전트 로직 변경 없이 스토리지 교체 가능**
  - 세션 서비스는 플러그인 구조로 설계되어 있어, 비즈니스 로직 수정 없이 `SessionService` 구현체만 swap하면 됨

- **두 가지 메모리 레이어를 명확히 분리해야 함**
  - **Session(단기)**: 동일 대화 내 문맥 유지 → DB Session Service로 영속화
  - **User Profile(장기)**: 세션 간 사용자 특성 유지 → 별도 preference 테이블

- **툴 호출 순서는 프롬프트로 강제해야 함**
  - LLM이 자율적으로 판단하게 두면 recall을 누락할 수 있으므로, 시스템 프롬프트에 "대화 시작 시 반드시 recall 먼저" 명시 필요

- **User Profile 설계는 작고 구조적으로 유지**
  - 비정형 텍스트가 아닌 key-value 구조로 저장해야 쿼리/업데이트가 용이함
  - 방대한 데이터 저장은 다음 에피소드의 Memory Bank(Vector Search)에서 다룸 예정

- **다음 단계 예고**: Vertex AI Session Service + Memory Bank를 활용한 대화 아카이빙 및 멀티모달(텍스트·이미지·오디오·비디오) 의미 기반 검색 구현 예정

---

## 출시 일정 / 버전 정보

- 해당 없음
  - (단, 사용 프레임워크는 **Google ADK(Agent Development Kit)** 이며, Vertex AI Session Service 연동은 다음 에피소드에서 다룰 예정)

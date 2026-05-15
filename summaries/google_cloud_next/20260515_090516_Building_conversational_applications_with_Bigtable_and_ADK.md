# Building conversational applications with Bigtable and ADK

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=HE1ldmzennU
- **요약 일시**: 2026-05-15 09:05:16

---

## 🔑 핵심 요약
- **Bigtable + ADK(Agent Development Kit)** 조합으로 사용자 식별 기반 헬스케어 컨시어지 에이전트 구현 사례
- **Agent-as-Tool 패턴**: 루트 에이전트가 query/search/booking 3개 서브에이전트를 도구처럼 호출
- `tool_context`로 OAuth 사용자 ID를 백채널 전달해 **Row-level 접근 제어**, `pydantic` + **Model Armor**로 SQL/프롬프트 인젝션 이중 방어

---

## 📣 주요 발표 내용

### 🔐 인증 & 사용자 컨텍스트
- **Google Auth Platform**에서 OAuth 클라이언트 생성 후 `Google Calendar` scope 포함
- 에이전트는 **서비스 계정**으로 실행되지만, 도구는 **end-user identity**로 스코프 다운
- 캘린더 접근, DB row-level 접근 제어, 에이전트 메모리 3곳에서 사용자 ID 활용

### 🤖 에이전트 아키텍처
- **Root agent** + 3개 서브에이전트 (`agent-as-tool` 패턴)
  - **Query agent**: Bigtable SQL 질의
  - **Search agent**: Google Search grounding + Maps로 인근 의료시설 탐색
  - **Booking agent**: Google Calendar에서 빈 슬롯 검색·예약
- 사전 컨텍스트 도구: `get_profile_info` (나이/성별/우편번호), `update_time` (현재 시각 — 상대 시간 질의 대응)

### 🗄️ Bigtable 데이터 모델
- `patients` 테이블 (user email을 row key) — **4개 column family**: `profile`, `prescriptions`, `visits`, `tests`
- Bigtable column family는 **SQL의 Map 타입**으로 표현 (key-value)
- > **Bigtable이 `GoogleSQL` API를 지원**한다는 점이 핵심 (PL/SQL 스타일 쿼리 가능)

### 🛠️ 도구 구현
- Bigtable SDK의 **`query_tool`**: SQL 쿼리를 몇 줄로 function tool화
- `pydantic`으로 타입 강제 → SQL Injection 차단
- `tool_context`에서 user identity를 가져와 row key 필터에 강제 주입 (에이전트가 임의 변경 불가)

### 🛡️ 보안 레이어
- **`pydantic`** 타입 검증: row key 필터 우회 시도 차단 데모
- **Model Armor** 콜백: `injection`, `jailbreaking` 템플릿으로 프롬프트 인젝션 차단
- Model Armor는 **입·출력 양방향** 검사 (에이전트 지시, SSN, 신용카드 번호 등)

### 📊 평가 & 자가 개선
- ADK의 **eval 시각화** 도구로 회귀 탐지
- **Hill-climbing 루프**: 에이전트가 eval 실행 → 지시문/도구 설명 자동 튜닝 → 재실행하는 self-tuning 파이프라인 구성

---

## 💡 개발자 포인트

> **Row-level Security는 반드시 `tool_context` 경유**로 구현하세요. 에이전트가 인자로 user_id를 받아 필터에 넣으면, 프롬프트로 다른 사용자 사칭이 가능합니다.

- **운영(Operational) 워크로드 vs 분석(Analytics) 워크로드 분리 권장**
  - 적은 데이터 추출 (주문/지원티켓 등) → ADK function tool로 충분
  - 대량 데이터 분석 → **Conversational Analytics API** / Data Agent Developer Platform 사용
- 차트 렌더링: 에이전트에게 **JSON 포맷** 응답을 요청하고 클라이언트(예: `three-charts`)에서 그리기
- 응답 포맷팅 (markdown table 등)은 **agent instructions에 명시**해야 일관성 확보
- SQL Injection 방어는 `pydantic` 1차 + Model Armor 2차 **다층 방어** 권장

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| Bigtable SQL (`GoogleSQL`) API | 데모에서 사용 — GA 여부 별도 확인 필요 |
| ADK `query_tool` (Bigtable 통합) | 데모 시점 사용 가능 |
| Model Armor (injection/jailbreak 템플릿) | 데모 시점 사용 가능 |
| Conversational Analytics API | 분석 워크로드용 별도 제품 |


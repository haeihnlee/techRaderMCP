# What's new in Looker: Empowering business users in the governed agentic era

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=u72ZSc8jLg4
- **요약 일시**: 2026-06-26 09:11:36

---

## 🔑 핵심 요약
- **Looker**가 단순 데이터 시각화에서 **데이터 에이전시(data agency)**로 전환 — 지난 12개월간 **Gemini**를 전 스택에 주입해 BI 워크플로우를 전면 재설계
- 핵심 3대 축: **대화형 BI(Conversational BI)**, **AI 기반 셀프서비스 경험**, **모든 앱·워크플로우·AI 에이전트에 연결되는 오픈 플랫폼**
- 신규 발표 3종: **Dashboard Agents**(대화하는 대시보드), **Triggered Workflows**(능동적 모니터링·알림), **Gemini Enterprise 통합**

---

## 📣 주요 발표 내용

- **Agentic Data Cloud**: Gemini가 주입된 데이터 생태계로 모든 클라우드·엔진을 연결. Knowledge Catalog + Looker를 통합해 데이터 전체를 **agent-ready** 상태로 만듦 — "human scale → agent scale"로의 전환

- **Dashboard Agents** (신규)
  - 정적 차트 모음이던 대시보드에 **대화 기능**을 직접 탑재
  - 숫자 뒤의 "why"를 자연어로 질문, 즉시 요약·심층 인사이트 제공
  - **Cross filter** 등 UI 컨트롤과 에이전트가 연동 → 필터 상태를 존중하며 응답 ("AI power + UI control")
  - 대시보드에서 **Explore**(데이터 탐색)로 즉시 점프, 추론 과정 투명하게 확인 가능

- **Triggered Workflows** (신규)
  - 수동 리포팅 → 능동적 모니터링으로 전환
  - 메트릭을 지속 추적하다 변동 발생 시 팀에 자동 알림
  - *Coming soon*: 이메일·**Slack** 알림 등 실시간 액션 트리거

- **Conversational Analytics 강화**
  - **Fast thinking mode** 도입으로 질문↔인사이트 사이 마찰 감소
  - **Agent led disambiguation**: 모호한 질문 시 역질문으로 사용자 의도 확인 (예: "Stephen" → DB 내 동명이인 목록 제시 후 선택)
  - 하나의 에이전트에 최대 **5개 Explorer** 연결 가능 → `AlloyDB`(트랜잭션) ↔ `BigQuery` 등 모델 간 자동 traverse
  - **Enhanced Analytics** 옵션: 백엔드에서 `Python` 코드 실행으로 복잡한 질문 처리

- **Gemini Enterprise 통합**: Looker Agent를 Gemini Enterprise 앱 내에서 사용·관리. 다른 Enterprise Agent와 함께 단일 경험으로 운영

---

## 💡 개발자 포인트

- **Explore = 시맨틱 레이어의 pre-joined view**. 에이전트가 여러 Explorer를 자동 횡단하므로, 거버넌스된 시맨틱 모델 설계가 정확도의 핵심
- 에이전트 설정: 이름·설명·**custom instructions**·Enhanced Analytics(`Python` 백엔드) 토글 → Workspace 스타일 원클릭 공유 및 **Gemini Enterprise** 퍼블리시 지원
- **Thinking ↔ Fast 모드** 전환 가능 — 정밀도 vs 속도 트레이드오프를 사용자가 선택

> **거버넌스가 일관된 단일 기반(governance layer)** 위에서 모든 인사이트가 제공된다는 점이 강조됨. AI에 정확한 컨텍스트를 주려면 데이터 전반의 거버넌스·시맨틱 정의가 선결 조건

- 접근 방식 다양화: 셀프서비스 대시보드 / 임베디드 분석 / API / Gemini Enterprise — 데이터 상호작용을 **omnipresent**하게 제공
- 모든 기능은 현재 사용자가 직접 체험 가능("available to try at home")하다고 언급

---

## 📅 버전 / 출시 일정

| 항목 | 상태 |
| --- | --- |
| Conversational Agent (by agent) | 작년 **Q4** 출시 |
| Dashboard Agents | 발표(이용 가능) |
| Triggered Workflows | 발표(이용 가능) |
| Slack·이메일 실시간 액션 트리거 | **Coming soon** |
| Gemini Enterprise 내 Looker Agent | 이용 가능 |
| Gemini 3 / Fast thinking mode | 적용됨 |


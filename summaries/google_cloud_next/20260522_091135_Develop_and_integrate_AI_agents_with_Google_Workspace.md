# Develop and integrate AI agents with Google Workspace

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=erRPuV1EQ_c
- **요약 일시**: 2026-05-22 09:11:35

---

## 🔑 핵심 요약
- **Google Workspace + Google AI** 통합으로 Gmail/Drive/Docs/Chat/Calendar 등 일상 워크플로우를 자동화하는 **AI 에이전트**를 구축·배포·게시할 수 있음
- AI 솔루션도 결국 소프트웨어이므로 **데이터·액션·인터페이스** 3대 축이 필요하며, Workspace는 이 모든 것을 트러스티드 플랫폼으로 제공
- **No-code(AppSheet)** → **Low-code(Apps Script)** → **Pro-code(ADK + MCP)** → **Gemini Enterprise** 까지 단계별 빌딩 옵션 제공

---

## 📣 주요 발표 내용
- **Workspace AI 기본 제공 기능**
  - Gmail의 **AI Overview / Thread Summary**, 사이드바 **Ask Gemini**
  - Meet의 **Take Notes for Me** (회의 충돌 시 자동 노트)
  - **NotebookLM**: 사용자 제공 자료(재무보고서, 시장분석, 내부 전략 문서) 기반 AI 리서치 파트너 — overview/slides/infographics 생성
  - **Workspace Studio**: 사용자가 starters + steps로 개인 AI 워크플로우를 빌드·관리·공유 (예: 매일 뉴스 요약을 Chat으로)

- **개발자 빌딩 옵션**
  - **AppSheet** (no-code), **Apps Script** (low-code), 그 외 임의 스택 (pro-code)
  - Gmail 메시지 접근·Calendar 이벤트 생성 등 광범위한 **API/Library** 제공
  - 대부분의 Workspace UI는 **Add-on**으로 확장 가능 (예: Gmail 사이드바에서 Travel Concierge 에이전트 호출)

- **MCP & ADK 통합**
  - Google이 **Cloud/Workspace용 MCP 서버 & 툴**을 지속 출시 — 커스텀 API wrapper보다 안전하고 쉬움
  - **Gemini CLI + Antigravity** + Workspace MCP로 로컬 개발환경과 실시간 조직 데이터 브리지
  - **ADK 프레임워크**에서 MCP 툴을 등록하고 instruction으로 사용 시점 정의

- **Gemini Enterprise Agent Platform**
  - 150+ pre-built 모델 (Gemini 포함) + custom 튜닝/트레이닝
  - **Agent Designer / Runtime** — 오픈소스 프레임워크, sessions, memories, MCPs, code execution 지원
  - **Connectors** for Gmail, Chat, Drive, Calendar, People → 런타임에 비즈니스 데이터 검색
  - 거버넌스·모니터링·관찰·평가·트레이싱 툴 포함
  - **UI는 미제공** — 자체 UI 또는 Workspace Add-on과 통합 필요

- **Gemini Enterprise (최상위 레이어)**
  - 조직 전체에 에이전트를 **discover/create/share/orchestrate** 하는 완성 플랫폼
  - **A2A(agent-to-agent) protocol** 또는 Cloud Marketplace로 에이전트 등록
  - 사용자가 직접 prompting + manual editing으로 personal **no-code agent** 생성 가능

---

## 💡 개발자 포인트
- **Client-agnostic**: Google AI 스택을 강제하지 않음 → 기존 스택 그대로 통합 가능
- 에이전트 빌드 시 커스텀 API wrapper보다 **공식 MCP 서버** 사용 권장 — 안전성·유지보수 측면에서 우위
- Workspace UI 통합 시 **Add-on (Apps Script 기반)** 이 가장 빠른 진입점 (예: Travel Concierge 예제)
- **Agent Platform Search API / Google-managed MCP server**로 Workspace 데이터를 RAG 컨텍스트로 활용 가능

> ⚠️ **중요**: Agent Platform 자체는 UI를 제공하지 않음. 자체 UI 또는 Workspace Add-on을 반드시 따로 구현해야 함. Gemini Enterprise를 쓰면 web app UI까지 제공됨.

- 모니터링 권장 차세대 기술:
  - **Connectors & MCP servers** (계속 증가하는 툴 생태계)
  - **A2A & agent-to-UI protocols** (표준화된 통신·생성형 UI)
  - **Full-duplex 모델** (예: `Gemini Live`) — 새로운 상호작용 패턴
  - **Skills** — MCP 툴을 보완하는 부상 중인 개념

---

## 📅 버전 / 출시 일정

| 항목 | 상태 |
|---|---|
| NotebookLM (Workspace 통합) | 작년(2025) 추가 |
| Workspace Studio | 올해(2026) 초 출시 |
| Gemini CLI / Antigravity + Workspace MCP | 사용 가능 |
| Gemini Enterprise Agent Platform | 사용 가능 |
| A2A / agent-to-UI 프로토콜 | 확장 중 (지속 모니터링 권장) |


# The ABCs of agent building

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=rjoMZyxncUI
- **요약 일시**: 2026-05-23 09:05:01

---

## 🔑 핵심 요약
- **AI 에이전트를 외부 시스템과 연결**하기 위해 등장한 6가지 프로토콜(**MCP, A2A, UCP, AP2, A2UI, AG-UI**)을 한 번에 정리한 세션
- 전통적 API는 사람을 가정하지만, 에이전트는 **카탈로그 탐색·결제·스트리밍**에서 벽에 부딪힘 → 각 프로토콜이 특정 문제를 해결
- Google의 오픈소스 **Agent Development Kit(`ADK`)** 기반으로 "주방 매니저 에이전트"를 단계적으로 확장하며 시연

---

## 📣 주요 발표 내용

**1. `MCP` (Model Context Protocol) — 도구/데이터 연결**
- 매 API마다 커스텀 툴을 작성하는 대신, **MCP 서버 URL만 추가**하면 런타임에 도구 자동 발견
- ADK에서는 `MCPToolset` 으로 서버당 3줄이면 연결 완료
- **프로토타이핑 단계**에서 가장 빛남

**2. `A2A` (Agent-to-Agent) — 다른 에이전트와 협업**
- 각 에이전트가 well-known URL에 **agent card**를 노출 → 능력 광고
- ADK의 `to_a2a()` 한 줄로 에이전트를 A2A 서비스로 노출 가능
- 프레임워크 무관하게 `send_message`로 위임

**3. `UCP` (Universal Commerce Protocol) — 상거래 표준**
- `/.well-known/ucp` 엔드포인트로 **머천트·카탈로그 발견**
- HTML 파싱 없이 **타입드 체크아웃 요청** (line items, quantities, payment details)

**4. `AP2` (Agent Payments Protocol) — 결제 권한·감사**
- **Checkout Mandate**: 승인된 머천트·구매 가능 항목 정의
- **Payment Mandate**: 지출 한도·결제 수단·사용자 인증 기록
- **서명된 영수증(Signed Receipts)** 으로 전체 감사 추적

**5. `A2UI` (Agent-to-User Interface) — 동적 UI 생성**
- **18개 프리미티브**(카드, 버튼, 텍스트 필드, 데이터 피커, 슬라이더 등) 조합
- 에이전트는 HTML 대신 **선언적 JSON 페이로드** 생성 → Lit / Angular / Flutter 등에서 렌더

**6. `AG-UI` — 실시간 스트리밍**
- `text_message_content`, `tool_call_result`, `run_finished` 등 **타입드 스트리밍 이벤트** 표준화
- ADK에서는 `ADKAgent` 래퍼 3줄로 프론트엔드 실시간 동기화

---

## 💡 개발자 포인트

> ⚠️ **모든 프로토콜을 동시에 도입할 필요 없음** — 지금 가진 문제에 맞는 것부터 골라 쓰기

- **실 데이터 부족** → `MCP` 부터 시작
- **다른 팀의 에이전트와 협업 필요** → `A2A` 추가
- **상거래/결제** → `UCP` + `AP2` (라이프사이클 전체 커버: 발견·체크아웃·인증·감사)
- **풍부한 UX** → `A2UI` (레이아웃과 데이터 분리, 같은 페이로드를 여러 렌더러에서 재사용)
- **사용자가 진행 상황을 보고 싶을 때** → `AG-UI`

> 💡 `A2UI`는 **레이아웃 한 번 전송 → 데이터만 갱신** 패턴이라 다중 렌더러 호환성이 뛰어남

> 💡 `AP2`의 mandate는 "프롬프트로 한도 알려주고 기도하는" 방식을 **타입드 가드레일**로 대체 — 보안/감사 측면에서 큰 진전

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|---|---|
| 프레임워크 | Google **Agent Development Kit (`ADK`)** (오픈소스) |
| 학습 리소스 | ADK Tools & Integrations 페이지, **Generative AI Repo** (GitHub) — `MCP` / `A2A` 노트북 제공 |
| 출시 일정 | 별도 명시 없음 (세션은 프로토콜 개념·통합 시연 중심) |

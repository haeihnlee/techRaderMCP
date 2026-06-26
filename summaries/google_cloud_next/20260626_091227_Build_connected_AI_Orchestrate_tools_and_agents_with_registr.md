# Build connected AI: Orchestrate tools and agents with registries and ADK

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=C5zYVlBsHLQ
- **요약 일시**: 2026-06-26 09:12:27

---

## 🔑 핵심 요약
- **에이전트 구축**의 패러다임이 "에이전트를 만드는 것"에서 "**대규모로 운영·관리하는 것**"으로 이동했다 (조직 내 중복 에이전트·MCP 서버 난립 문제).
- **Agent Registry**가 에이전트·MCP 서버·모델의 **단일 진실 공급원(Single Source of Truth)** 역할을 하며, **ADK**에 몇 줄 코드로 통합된다.
- **Agent Identity**(SPIFFE 기반)와 **Spec Boost**(레거시 API → 에이전트용 스펙 자동 생성)로 보안·문서화 문제를 해결한다.

---

## 📣 주요 발표 내용
- **Agent Registry** — 조직 내 모든 에이전트·MCP·모델의 **단일 진실 공급원**
  - 서드파티 MCP 서버를 **간편 등록** 가능 (포털 / API / SDK)
  - **`ADK`에 내장 지원** — 등록된 에이전트·MCP를 몇 줄 코드로 호출
- **Agent Identity** — **SPIFFE 기반** 표준 에이전트 신원 (`SPIFFE ID`)
  - 신원이 **에이전트 라이프사이클에 종속** → 배포 시 생성, 삭제 시 권한까지 함께 제거
  - **Secure Credentials Vault** 제공 — API 키, `OAuth 2.0` 자격증명을 안전하게 저장
- **Spec Boost** (DeepMind 기술, 백엔드 `Gemini` 기반)
  - 스펙이 없으면 **API 로그 기반으로 OpenAPI 스펙을 자동 생성**
  - 기존 스펙은 **사람·에이전트가 읽기 쉽게 최적화**
  - 프로덕션 실제 동작과 문서 간 **diff·merge** 지원
- **API Hub → MCP 변환** — API 스펙을 **원클릭으로 MCP 서비스화**, Agent Registry와 자동 동기화
- **Klook 사례** — 실제 멀티 에이전트 시스템에 Agent Platform 적용 (여행/액티비티 어드바이저 데모)

---

## 💡 개발자 포인트
- 새 에이전트를 만들기 전에 **Registry를 먼저 검색**해 기존 weather agent/MCP 등 재사용 자산을 찾는 워크플로우 권장 (중복 구축 방지).
- 기존 엔터프라이즈 API가 **에이전트 친화적이지 않으면** LLM이 호출 시 **환각(hallucination)**을 일으키거나 실패한다 → **풍부하고 정확한 OpenAPI 스펙이 필수**.

> ⚠️ **Spec Boost로 생성·병합된 스펙은 사람 승인(human sign-off) 없이는 게시되지 않는다.** AI가 로그를 분석하다 기존 스펙을 발견하면 prod와 문서의 diff를 확인 후 머지하는 단계를 반드시 거친다.

> 🔐 기존에는 프로젝트 내 **모든 에이전트가 하나의 서비스 계정을 공유**해 세밀한 권한 관리가 어려웠다. Agent Identity는 에이전트별 신원을 부여해 **rogue 권한이 남지 않도록** 한다.

---

## 📅 버전 / 출시 일정
해당 없음 (작년 Next에서 **A2A 프로토콜** 발표, 올해는 Agent Platform·Registry·Spec Boost 중심 소개)


# Can we fix this AI agent in 60 minutes? (Live builder Q&amp;A)

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=md2VFN6SojQ
- **요약 일시**: 2026-04-16 09:04:09

---

## 🔑 핵심 요약

- 비기술직 개발자가 **vibe coding**으로 만든 AI 영업 지원 에이전트(`Titanium`)를 실시간으로 프로덕션 수준으로 리팩토링하는 라이브 세션
- 하드코딩된 10개 케이스 스터디 → **1,600개 Google 공개 케이스 스터디** 동적 검색으로 확장하는 것이 핵심 목표
- **Gemini SDK** 기반 V1에서 **ADK(Agent Development Kit)** 기반 V2로 마이그레이션 전략 시연

---

## 📣 주요 발표 내용

- 🤖 **Titanium 에이전트 V1 아키텍처**
  - `orchestrate_all()` 함수로 **팬아웃(fan-out) 패턴** 구현 — 여러 고객사를 순차가 아닌 병렬로 리서치
  - `verify_intel()` 함수로 **할루시네이션 방지** 검증 레이어 추가
  - **Grounding with Google Search** 활성화 및 `temperature` 낮게 설정으로 사실 기반 응답 유도
  - **지수 백오프(Exponential Backoff)** 적용으로 API 레이트 리밋 및 네트워크 불안정 대응

- 🔧 **V2 마이그레이션 전략 (`ADK` 기반)**
  - **Gemini SDK** → **ADK(Agent Development Kit)** 전환 권장
  - `Sequential Agent` 패턴으로 리서치 → 이메일 초안 → 검증 단계를 순서대로 실행
  - **ADK Dev Skills** 활용 — Gemini CLI, Cloud Code 등 다양한 코딩 에이전트와 호환되는 ADK 개발 가이드 스킬셋
  - **Playwright** 헤드리스 브라우저로 Google 케이스 스터디 사이트 크롤러 별도 구현

- 📋 **프롬프팅 베스트 프랙티스**
  - 코딩 시작 전 반드시 **계획(Plan) 먼저 생성** 요청
  - `"reverify your work"` 지시로 에이전트가 스스로 두 번 검토하게 유도
  - `.env` 파일 + **Application Default Credentials(ADC)** 로 GCP 인증 관리

---

## 💡 개발자 포인트

> ⚠️ **Breaking Change 주의**: 기존 **Gemini SDK** 직접 호출 방식은 단순 프로토타입에는 유효하나, 팀 배포·확장성을 고려하면 반드시 **ADK**로 전환을 고려해야 함

> ⚠️ **하드코딩 케이스 스터디의 한계**: 소수의 케이스 스터디를 직접 삽입하면 동일 데이터 포인트가 반복 사용되어 품질 저하 및 팀 확장 불가 — **동적 RAG 검색 구조**로 전환 필수

- **팬아웃 패턴** 도입 시 처리 시간 대폭 단축 (기존 약 15분 → 병렬화 후 단축)
- LLM API 호출 시 **Exponential Backoff** 는 선택이 아닌 필수 — 레이트 리밋·네트워크 불안정 대비
- `temperature` 를 낮게 설정하면 사실 기반 태스크(이메일, 리서치)에서 **환각(hallucination) 감소**
- **베이비 스텝 원칙**: V1 기능을 ADK로 1:1 복제 후 → 신규 기능 점진적 추가 권장
- **ADK Dev Skills** 를 코딩 에이전트에 주입하면 ADK 앱 개발 품질 및 속도 향상

---

## 📅 버전 / 출시 일정

| 구분 | 내용 |
|---|---|
| **Titanium V1** | Gemini SDK 직접 호출, 케이스 스터디 하드코딩 (현재) |
| **Titanium V2** | ADK 기반 Sequential Agent + Playwright 크롤러 + 동적 케이스 스터디 검색 (세션 내 라이브 구현 중) |
| **ADK Dev Skills** | 세션 기준 최근 릴리스, Gemini CLI·Cloud Code 등 지원 |
| **목표 시간** | 60분 내 V2 MVP 완성 (라이브 챌린지) |

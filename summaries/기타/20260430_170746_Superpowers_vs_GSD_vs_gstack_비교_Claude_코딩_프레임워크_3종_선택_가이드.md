# Superpowers vs GSD vs gstack 비교, Claude 코딩 프레임워크 3종 선택 가이드

- **컨퍼런스**: 기타
- **출처**: https://youtu.be/MWaWw6v6Rn4?si=fhSDndijl3FpN0ge
- **요약 일시**: 2026-04-30 17:07:46

---

## 🔑 핵심 요약
- **Claude Code** 위에서 돌아가는 3대 오픈소스 프레임워크 — **Superpowers**, **GSD**, **gstack** — 의 철학·접근법을 비교
- 셋은 **경쟁 관계가 아니라 서로 다른 레이어**의 문제를 해결: Superpowers=프로세스, GSD=컨텍스트, gstack=관점/역할
- 처음에는 **Superpowers 단독**으로 2주간 사용해 보고, 부족한 레이어를 진단한 뒤 GSD/gstack을 점진적으로 쌓는 순서 추천

---

## 📣 주요 발표 내용

### 1. Superpowers (제시 빈센트, GitHub Star 149K)
- **프로세스 강제** 철학 — 시니어 개발자의 일하는 방식을 AI에 이식
- 7단계 워크플로우 강제: **Brainstorm → Spec → Plan → TDD → Sub-agent → Review → Finalize**
- 핵심은 **TDD 강제**: `Red → Green → Refactor` 사이클을 권장이 아니라 **강제** (테스트 없이 짠 코드는 지우고 다시 작성)
- 서브 에이전트 병렬 실행 + 자동 코드 리뷰 내장

### 2. GSD (Get Shit Done) (렉스 크리스토퍼슨 / glittercowboy, GitHub Star 51K)
- **컨텍스트 로트(Context Rot)** 문제를 정조준
- 컨텍스트 사용량별 품질 변화:

| 사용량 | 품질 |
|--------|------|
| 0~30% | 최상의 품질 |
| 50% 초과 | 쫓기듯 짜기 시작 |
| 70% 초과 | 환각, 요구사항 누락 |

- 작업을 **Plan / Execute / Review** 3단계로 분리, 각 단계마다 **새 서브 에이전트 + 깨끗한 20만 토큰 컨텍스트** 부여
- 메인 세션은 30~40% 수준 유지 → 며칠짜리 장기 작업도 흐트러지지 않음
- Amazon, Google, Shopify, Webflow 엔지니어들이 실사용 인증

### 3. gstack (게리 탄 / Y Combinator CEO, GitHub Star 71K)
- **역할 기반 격리** — AI 한 명에게 23개 역할을 번갈아 부여
- 주요 역할 모드:
  - `CEO 모드`: 제품 본질·방향 검토
  - `Engineering Manager 모드`: 아키텍처·엣지 케이스
  - `Designer 모드`: 시각 일관성·AI slop 검출
  - `QA 모드`: 실제 브라우저 테스트
  - `Security Officer 모드`: **OWASP Top 10** 자동 감사
- 각 역할은 **자기에게 필요한 컨텍스트만** 보고 다른 정보는 차단

---

## 💡 개발자 포인트

> **세 프레임워크는 서로 다른 레이어의 문제를 풀므로 결합 사용이 가능하다.**
> - Superpowers = "**어떻게** 일할 것인가" (실행 프로세스)
> - GSD = "**어디서** 일할 것인가" (작업 환경/컨텍스트)
> - gstack = "**무엇을** 할 것인가" (결정과 관점)

**3-레이어 결합 구조 (커뮤니티 추천):**
1. **상층 — gstack**: 의사결정 레이어 (`Office Hour` skill, `CEO Review`, `Engineering Review`)
2. **중층 — GSD**: 컨텍스트 레이어 (`PROJECT.md`, `DECISIONS.md`, `KNOWLEDGE.md` 주기적 로드)
3. **하층 — Superpowers**: TDD 기반 실제 코드 실행 레이어

> ⚠️ **결합 사용 시 함정**
> - **토큰 비용 폭증**: gstack 모든 skill 활성화 시 1회 실행에 **1만 토큰 초과**. 평소엔 core skill만 켜고 큰 결정에만 무거운 리뷰 호출
> - **인터랙티브 프롬프트 충돌**: Superpowers의 인터랙티브 프롬프트가 GSD 컨텍스트 격리와 충돌 → **CI 환경에서는 비활성화 필수**
> - **과적용 금지**: 한 줄 수정에 7단계 워크플로우 적용은 **숨막힘**. 작은 작업엔 적용하지 말 것

**상황별 선택 가이드:**
- 자기 훈육이 약하고 코드부터 짜는 습관 → **Superpowers** (TDD 강제)
- 며칠짜리 장기 세션에서 AI가 바보가 되는 게 짜증 → **GSD** (컨텍스트 격리)
- 파운더/사이드 프로젝트로 제품·디자인·QA까지 챙겨야 함 → **gstack** (역할별 게이트)

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| Superpowers 시작 | 2025년 10월 (제시 빈센트 블로그) |
| Superpowers 설치 | `/plugin install superpowers` (Anthropic 공식 마켓플레이스) |
| GSD 설치 | GitHub clone + 설치 스크립트, 또는 GSD plugin package |
| gstack 설치 | GitHub `garry-tan/gstack` README 참조, **사용할 skill만 선별 활성화 권장** |
| 비고 | **3종 모두 오픈소스·무료** |


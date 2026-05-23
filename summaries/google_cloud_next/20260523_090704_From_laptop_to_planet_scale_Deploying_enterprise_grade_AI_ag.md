# From laptop to planet scale: Deploying enterprise grade AI agents

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=yxVQ3BUj1u8
- **요약 일시**: 2026-05-23 09:07:04

---

## 🔑 핵심 요약
- **개인 노트북용 에이전트**에서 **엔터프라이즈 행성 규모(planet scale) 에이전트**로 가는 여정과 그 사이의 갭(Day 2 운영 문제)을 다룬 세션
- Google Cloud의 **Gemini Enterprise Agent Platform**이 **Build → Scale → Govern → Optimize** 전 주기를 커버하는 핵심 솔루션으로 소개됨
- 개발자 진입점이 다양화됨: **Agent Studio**(비주얼), **Managed Agents API**(설정 기반), **ADK**(코드 우선), **Agent CLI**, **Antigravity**(에이전틱 코딩 IDE)

---

## 📣 주요 발표 내용
- **Gemini Enterprise Agent Platform** 출시 (Google Cloud Next에서 약 한 달 전 발표)
  - 에이전트 **identity**, **credential 관리**, **agent registration**, **agent evaluation** 등 Day 2 운영을 위한 프리미티브 제공
  - 수백~수천 개 에이전트 환경에서 "어떤 에이전트가 무엇을 했는지" 추적·디버깅 가능
- **Agent Studio**: 코드 없이 서브에이전트 구조를 시각적으로 구성, 모델 선택, SDK 코드 생성까지 지원
- **Managed Agents API**: configuration-first 접근 방식 (엔지니어링-first인 `ADK`와 대비)
- **Agent Development Kit (`ADK`)**: 10줄 코드로 에이전트 시작 가능, 안전·일관성 있는 프레임워크
- **Agent CLI**: 그동안 SDK 팀이 공유해온 skills/best practices/workflows를 하나의 패키지로 통합 (수천 stars 확보)
- **Antigravity**: Google I/O 2026 메인 발표 중 하나. **agentic coding & multi-agent orchestration** 전용 UI
  - 기존 IDE보다 "여러 에이전트와 그 산출물 관리" 쪽으로 진화한 인터페이스
  - `Agent CLI`, `Managed Agents API` 등 다른 플랫폼 구성요소와 호환

---

## 💡 개발자 포인트
- "랩탑에서 잘 돌던 에이전트가 프로덕션에서 무너지는" 이유는 **Day 2 운영 영역(트레이싱, 거버넌스, 평가, credential, blast radius 제어)** 부재 때문
- Grady Booch 인용: *"소프트웨어의 역사는 추상화 상승의 역사"* — 에이전트도 지금 "성장(grow up) 모먼트"를 지나는 중

> ⚠️ **Blast Radius 주의**: 개인 에이전트를 회사 데이터/서드파티에 그대로 연결하지 말 것. 의료(HIPAA) 같은 규제 산업에서는 **"YOLO mode"** 실행 절대 금지. Agent Platform의 managed credential 흐름을 사용하라는 것이 권고사항.

- 진입 경로 선택 가이드:
  - **비주얼/비개발자** → `Agent Studio`
  - **설정 기반 빠른 구성** → `Managed Agents API`
  - **코드 우선 개발자** → `ADK` + `Agent CLI`
  - **에이전틱 코딩 환경** → `Antigravity` (Claude Code 대안 포지션)
- 가드레일이 있는 플랫폼에서 빌드하면 **downside risk가 줄어** 실험을 더 과감하게 할 수 있다는 점이 핵심 메시지

---

## 📅 버전 / 출시 일정

| 항목 | 상태 / 시점 |
| --- | --- |
| Gemini Enterprise Agent Platform | Google Cloud Next 2026 발표 (약 1개월 전) |
| Agent CLI | Next에서 공식 발표, 현재 공개 (수천 GitHub stars) |
| Antigravity | Google I/O 2026 메인 발표, 현재 사용 가능 |
| ADK | 공개 사용 가능 (10줄 시작 예제 제공) |


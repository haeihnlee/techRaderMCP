# Why Your AI Agent Fails in Production (And How to Catch It)

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=wPdoZRbvaF4
- **요약 일시**: 2026-10-01 09:05:38

---

## 🔑 핵심 요약
- 프로덕션 AI 에이전트 품질 문제는 **"vibe check"(감으로 확인)** 에 기대기 때문에 생김. 기대하는 품질을 **수치화된 eval**로 바꿔야 회귀를 잡을 수 있음
- Google **AI Agent Clinic (Eval Edition)**: LangGraph 기반 에이전트 **DocsHound**를 대상으로 **60분 안에 eval을 구축**하는 4단계 실습
- **OpenTelemetry + OpenInference**로 트레이스를 표준화하면 **ADK가 아닌 프레임워크**(LangGraph, CrewAI 등)도 Google Cloud 에이전트 플랫폼에서 평가 가능

---

## 📣 주요 발표 내용
- **Eval 4단계 워크플로우**
  1. **Antigravity**(코딩 에이전트)에 에이전트 소스 코드를 넘겨 내부 동작과 트레이스를 분석시킴
  2. Google Cloud 팀이 만든 **evaluation toolkit**으로 eval 스캐폴딩 — 셋업 기간을 **몇 주에서 1시간**으로 단축
  3. 도메인 전문가가 말하는 "좋은 결과"를 Antigravity에게 가르쳐 **eval metric을 큐레이션** (AI가 초안, 사람이 가이드)
  4. eval을 실행하고 결과를 시각화해 다음 버전을 **정량적으로** 어떻게 개선할지 방향 잡기
- **DocsHound 데모**: GitHub 저장소 URL을 넣으면 이슈(50개)와 PR(30개), 공식 문서를 조사해 **문서 공백**(예: audio streaming 지원 누락)을 찾아냄 → GUI에서 markdown 편집 → **PR 자동 생성**
- 배포한 LangGraph 에이전트를 **Gemini Enterprise Agent Platform**의 Deployments 화면과 로그에서 바로 확인
- Antigravity가 트레이스로 **Mermaid 아키텍처 다이어그램**과 문서를 만들어 코드 이해를 도움
- 기존 시나리오 하나(ADK 저장소 분석)를 바탕으로 **T3 Code, OpenCode, Pi agent** 같은 오픈소스 저장소용 테스트 시나리오를 재현 가능하게 추가 생성

---

## 💡 개발자 포인트
- **OpenTelemetry**는 텔레메트리 표준이지만, 프레임워크마다(LangGraph / CrewAI / ADK) span과 인자 구조가 다름 → **OpenInference**로 LLM/에이전트 전용 스키마를 맞춰야 함
- 에이전트를 OpenInference 호환으로 만들어 두면 **내부 구현이 바뀌어도 eval 파이프라인을 다시 만들 필요가 없음**
- Eval 데이터셋을 만들 때는 **이미 성공한 실제 실행 트레이스 하나**에서 시작하고, 코딩 에이전트로 비슷한 시나리오를 늘리는 방식이 효율적
- **LLM-as-a-judge**로 트레이스를 검토하는 것이 앞으로 에이전트를 개선하는 주된 방식이 될 것이라는 의견
- 다른 기여자가 PR을 올렸을 때 메인테이너가 생각하는 품질과 같은지 판단하려면, 그 기준을 **실행 가능한 metric**으로 옮겨 두어야 함

> ⚠️ 감으로 확인하면 다른 사람의 변경이나 프롬프트 수정 때문에 생긴 **회귀(regression)** 를 놓칩니다. 새 버전을 배포하기 **전에** eval을 돌리는 흐름을 만드세요.

---

## 📅 버전 / 출시 일정
해당 없음


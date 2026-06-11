# What are AI agents?

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=Zqno_vux6d8
- **요약 일시**: 2026-06-11 09:04:38

---

## 🔑 핵심 요약
- **AI 에이전트**는 단순히 응답만 하는 챗봇과 달리, 요청을 분석해 **스스로 판단하고 행동(API 호출·코드 실행)** 하는 소프트웨어다
- **ReAct**(Reasoning + Acting) 패러다임 — `추론 → 행동 → 관찰 → 조정`의 반복 사이클이 현대 에이전트의 기반이다
- Google **ADK**(`Agent Development Kit`)로 멀티 에이전트 **블로그 작성 봇**을 단계별로 직접 구현하는 실습 데모

---

## 📣 주요 발표 내용

**에이전트의 3가지 행동 패턴**

- **Sequential(순차형)**: 조립 라인처럼 단계별 실행 → 예측 가능하지만 경직됨
- **Reactive(반응형)**: 현재 상태를 보고 즉석에서 도구 선택 → 유연하나 계획성 없음
- **Deliberate/Planning(계획형)**: 먼저 계획을 세운 뒤 실행 → 의존성 있는 다단계 목표에 적합

**ADK 핵심 구성요소**

- `LlmAgent`: 모델로 구동되는 실제 작업 에이전트 (planner, writer)
- `LoopAgent`(워크플로우 에이전트): 검증 실패 시 **자동 재시도**(최대 3회) 처리
- `output_key`: 에이전트 결과를 **shared state**에 저장 → 다음 에이전트가 자동으로 이어받음
- `BaseAgent` 서브클래싱으로 커스텀 에이전트 확장 가능

**블로그 작성 에이전트 구조**

- `blog_planner` → 토픽을 받아 마크다운 **아웃라인** 생성 (제목·서론·4~6 섹션·결론)
- `outline_validation_checker` → 아웃라인 검증, 통과 시 `OK` / 미달 시 `retry`
- `blog_writer` → 아웃라인을 전체 블로그 포스트로 작성 (대상: SW 엔지니어)
- `blog_post_validation_checker` → 작성된 글 검증
- 각 planner/writer를 **LoopAgent로 감싸** `robust_blog_planner`, `robust_blog_writer` 구성
- root agent `blogger`가 두 로봇 루프를 **tool로 호출**하여 전체 워크플로우 조율

---

## 💡 개발자 포인트

- **명시적 출력 지시가 신뢰성을 높인다** — "제목+서론+4~6섹션+결론" 식으로 산출물 형식을 구체적으로 명시할수록 LLM 출력이 안정적이다

> **검증 + 재시도 루프**가 핵심 안전망: checker가 `retry`를 반환하면 LoopAgent가 동일 지시로 최대 3회까지 재실행 → 모델이 빠뜨린 항목을 스스로 보정한다

- **shared state 패턴**: `output_key`로 결과를 상태에 저장하면 에이전트 간 데이터를 직접 전달하지 않고도 파이프라인 연결 가능
- root agent에는 **노출할 tool만 제한적으로 제공**하여 워크플로우를 명확하고 통제 가능하게 유지
- 문제 성격에 맞는 패턴 선택 — 단순/예측 가능 → Sequential, 동적 → Reactive, 의존성 있는 다단계 → Planning

**환경 설정**

- `uv` 설치 → `pip install google-adk` (Google ADK 설치)
- `agent.py` 작성 후 `adk web` 명령으로 로컬 UI에서 에이전트 실행·상호작용

---

## 📅 버전 / 출시 일정
해당 없음 (개념 설명 및 핸즈온 튜토리얼 영상)


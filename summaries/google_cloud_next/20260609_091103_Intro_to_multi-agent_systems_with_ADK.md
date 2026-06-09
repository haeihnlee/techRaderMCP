# Intro to multi-agent systems with ADK

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=0Z0GUDakR_A
- **요약 일시**: 2026-06-09 09:11:03

---

## 🔑 핵심 요약
- Google의 **ADK(Agent Development Kit)**로 도구를 갖춘 에이전트와 **멀티 에이전트 시스템**을 손쉽게 구축하는 방법을 소개
- 에이전트는 결국 **"도구를 가진 LLM이 루프를 돌며 작업을 완수하는 것"** — ADK는 이 루프 제어·도구 연결 보일러플레이트를 대신 처리
- `ADK create`, `ADK run`, `ADK web` 만으로 에이전트 생성부터 로컬 테스트·디버깅까지 가능
- 핵심은 **에이전트를 다른 에이전트의 도구(tool)로 장착**해 오케스트레이터를 구성하는 멀티 에이전트 패턴 (예: 검색 → URL 검증)

---

## 📣 주요 발표 내용
- **에이전트 정의**: LLM + 도구(tools) + 작동 루프. ADK가 루프 제어와 종료 판단 등 반복 코드를 추상화
- **사전 준비**: **AI Studio**에서 Gemini API 키 발급 → `pip install google-adk` (가상환경 권장)
- **첫 에이전트 생성**: `ADK create first_agent` → 모델(`Gemini 3 flash preview`)·`name`·`description`·`instructions`(시스템 프롬프트)만 정의하면 완성
- **테스트 방법 2가지**
  - `ADK run first_agent` — 터미널에서 대화형 테스트
  - `ADK web` — `127.0.0.1:8000` 로컬 웹 UI 제공, **stack trace 확인 가능**해 디버깅에 유용
- **도구(tool) 장착**: `get_current_time` 같은 Python 함수를 정의하고 `tools=[...]` 리스트에 추가하면 LLM이 최신 정보 획득 가능 (LLM의 학습 cut-off 한계 극복)
- **내장 Google Search 도구**: ADK에 포함되어 `import` 만으로 사용. 단, 기본 단일 호출 제한 때문에 `bypass_multiple_tools_limit=True` 설정 필요
- **멀티 에이전트 시스템 (핵심 데모)**
  - `URL verifier` 에이전트: `fetch_url` 도구로 실제 페이지를 가져와 `verified / not verified / inconclusive` 반환 → **LLM as a judge** 패턴
  - `researcher` 오케스트레이터: `search_agent`와 `verify_agent`를 **도구로 장착**해 검색 결과의 URL 정확성을 교차 검증

---

## 💡 개발자 포인트
- **에이전트를 도구로 쓰는 구조**가 ADK 멀티 에이전트의 핵심 — 각 에이전트에 단일 책임을 부여하면 성능·메모리·비용 관리가 쉬워짐
- 에이전트별로 **다른 LLM 모델 혼용 가능**: 간단한 작업은 저렴·빠른 모델, 복잡한 추론은 고성능·고비용 모델로 배분
- **LLM as a judge** 패턴으로 한 에이전트의 출력을 다른 에이전트가 검증 → 환각(hallucination) 완화

> ⚠️ **주의: Google Search 도구도 LLM이 출처 URL을 환각(hallucinate)할 수 있어, 일부 링크가 404가 됩니다.** 검색 결과를 신뢰하려면 별도 검증 에이전트로 URL 실존 여부를 반드시 교차 확인하세요.

> ⚠️ Google Search 사용 시 기본값은 **단일 도구 호출만 허용**됩니다. 포괄적 검색 결과가 필요하면 `bypass_multiple_tools_limit=True`를 명시해야 합니다.

- 학습데이터 cut-off로 LLM은 "지금 몇 시?", "오늘 날짜?"에 정확히 답할 수 없음 → 도구 장착으로 실시간 정보 보강이 정석
- 시작점: **`adk.dev`** 의 Get Started 가이드

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| 프레임워크 | Google ADK (Agent Development Kit), Python 패키지 `google-adk` |
| 데모 사용 모델 | `Gemini 3 flash preview` |
| 로컬 웹 UI | `127.0.0.1:8000` (`ADK web`) |
| 시작 가이드 | adk.dev |

> 영상 내 별도 정식 출시일/버전 로드맵 언급은 없음 (튜토리얼 성격)


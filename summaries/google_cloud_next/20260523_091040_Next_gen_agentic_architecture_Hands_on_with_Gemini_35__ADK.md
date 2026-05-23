# Next gen agentic architecture: Hands on with Gemini 3.5 & ADK

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=XZJk_S82Gpk
- **요약 일시**: 2026-05-23 09:10:40

---

## 🔑 핵심 요약
- **Gemini 3.5 Flash** 공개: 프론티어급 성능을 더 낮은 비용으로 제공, 코딩·Agentic·멀티모달 모두 강화
- **Gemini Omni** 발표: 모든 입력 모달리티를 비디오로 변환하는 신규 생성형 미디어 모델 (Nano Banana 계열 후속)
- **Gemini Enterprise Agent Platform** 4대 축(Build / Scale / Govern / Optimize)과 **ADK**, **Agent Runtime**, **Agent Registry**, **Evaluation** 등 풀스택 에이전트 인프라 통합 제공

---

## 📣 주요 발표 내용
- **IO 2026 발표 라인업 5종**: Anti-Gravity 2.0, Spark, Managed Agents, **Gemini 3.5**, **Gemini Omni**
- **Gemini 3.5 Flash 벤치마크 개선치**
  - `Terminal Bench`: 터미널/배치 작업 처리 능력 대폭 향상
  - `SWE Bench Pro`: 업계 표준에서 큰 폭 개선 (Flash임에도 Pro급 결과)
  - `MCP Atlas`: 78 → **83.6** (MCP 호출 효율성)
  - `Tool Use`: **56%** 향상
- **성능 특성**: 3.1 Pro 수준 결과를 유지하면서 **token/sec** 속도가 대폭 빨라짐 → 이름값(Flash)대로 응답 속도가 체감되는 수준
- **Gemini Omni 활용처**: `Flow`, **Gemini 앱**, **YouTube Shorts**에서 이미 사용 가능. **API**·**Agent Platform** 곧 출시 예정
  - 월드 날리지(world knowledge) 내장 → 비현실적 프롬프트도 물리/맥락에 맞게 렌더링
  - 비디오 내 텍스트 렌더링, 다중 모달 입력 → 비디오 출력 지원
- **Agent Platform 구성 요소**
  - **ADK (Agent Development Kit)**: 복합 에이전트 빌드 프레임워크
  - **Agent Runtime**: 보안 환경에서 에이전트 배포·운영
  - **Agent Registry**: 수백~수천 개 에이전트 관리·탐색
  - **Agent Security**: 거버넌스/보안
  - **Evaluation**: 조직 기준에 맞춘 에이전트 평가 (시간 흐름·벤더 변경에 대응)

---

## 💡 개발자 포인트
- **Flash 가격은 소폭 상승했지만**, 단위 결과당 비용은 대폭 감소 — 대규모 서비스에서 수십억 달러 절감 효과 (Sundar 키노트 인용)
- 코딩 하네스(`Anti-Gravity`, **Anti-Gravity CLI** 등)에서 Agentic 체감 성능 차이가 가장 크게 나타남
- 모델 접근 방식
  - **Agent Platform Studio UI**: 노코드 빌드·미디어 생성
  - **Google Gemini SDK** 또는 **ADK**: 프로그래밍 방식 접근
- **Evaluation은 일회성이 아닌 지속 관리 필수**

> ⚠️ "Day 1에 만든 평가 기준은 6개월 뒤 무용지물" — 벤더 교체·언어 변경 시 컨텍스트가 달라지므로 **Evaluation 파이프라인을 상시 재검증**해야 함

> 📌 0→1(Build)뿐 아니라 1→N(Scale·Govern·Optimize)까지 고려한 설계 필수. Registry 없이 수천 개 에이전트 운영은 사실상 불가능

---

## 📅 버전 / 출시 일정

| 항목 | 상태 | 비고 |
|------|------|------|
| Gemini 3.5 Flash | **출시** | 본 세션에서 데모 |
| Gemini 3.5 Pro | 미발표 | 추후 공개 예정 |
| Gemini Omni (소비자) | **사용 가능** | Flow, Gemini 앱, YouTube Shorts |
| Gemini Omni (API / Agent Platform) | **Coming Soon** | 키노트에서 예고 |
| Anti-Gravity 2.0 / Spark / Managed Agents | 발표됨 | 본 세션 외 별도 트랙 |


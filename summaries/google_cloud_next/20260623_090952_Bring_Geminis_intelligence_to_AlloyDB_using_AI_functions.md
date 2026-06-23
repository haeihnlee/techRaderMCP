# Bring Gemini's intelligence to AlloyDB using AI functions

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=PxbLWePxt40
- **요약 일시**: 2026-06-23 09:09:52

---

## 🔑 핵심 요약
- **AlloyDB AI functions**는 `Gemini` 같은 파운데이션 모델의 지능을 SQL 함수 형태로 데이터베이스에 직접 가져온다.
- `AI.rank` / `AI.if` / `AI.generate` / `AI.forecast` 등 **GA(정식 출시)** 함수로 재랭킹·지능형 필터링·생성·시계열 예측을 SQL 한 줄로 처리.
- **Optimized AI functions**(로컬 모델 학습 방식)로 행 단위 LLM 호출 대비 최대 **23,000배 빠르고 6,000배 저렴**하게 처리 가능.

---

## 📣 주요 발표 내용
- **하이브리드 검색 + AI.rank**: 상위 1,000건 결과를 `Gemini`의 외부 지식(예: "산토리니 여름 날씨에 맞는 셔츠 소재")으로 자연어 프롬프트 기반 재랭킹.
- **GA로 출시된 LLM 기반 함수**
  - `AI.rank` — 결과 재정렬 (semantic ranker 버전 포함)
  - `AI.if` — 지능형 필터링 (예: 거래 사기 여부 판별)
  - `AI.generate` — 비정형 데이터를 `JSON` 등으로 변환·생성
  - `AI.forecast` — **TimesFM** 기반 시계열 예측 (재고 최적화·매출 전망)
- **신규 AI functions**
  - `AI.analyze_sentiment` — 감정 분류
  - `AI.summarize` — 긴 텍스트를 요약
  - **aggregate summarize** — 여러 행(row)에 걸친 데이터를 통합 요약
- **데모(Simple Gadgets 마켓플레이스)**: 리뷰 통합 요약, 리뷰 감정 통계, "수심 40m 이상 방수 카메라" 같은 정밀 조건 필터링을 `AI.if`로 구현. 조건 미충족 시 **거짓 양성(false positive) 없이 0건 반환**.

---

## 💡 개발자 포인트
- `AI.if`는 단순 최근접 매칭(하이브리드 검색)과 달리 **임베딩 데이터에 대해 구체적 조건을 평가**해 거짓 양성을 제거한다 — "방수"라는 단어만 보고 10m 카메라를 반환하는 문제를 해결.
- **비용/성능 우려에 대한 해법**: 모든 행마다 LLM을 호출하는 부담을 줄이기 위한 가속 기법 제공.
  - 비동기 벌크 프롬프트(asynchronous bulk prompt)
  - AI function acceleration
  - 배열 기반 처리(array-based processing)

> ⚡ **Optimized AI functions (현재 `AI.if` 지원)**: 사용자의 임베딩과 LLM 출력으로 **로컬 모델을 학습**시켜 LLM 대신 호출. 벤치마크상 초당 최대 **100,000행**을 **0.1센트 미만**으로 처리 — 행 단위 LLM 호출 대비 최대 23,000배 빠르고 6,000배 저렴.

- 사용법: `prepared statement`로 AlloyDB 내부에 로컬 모델을 생성 → `AI.if` 호출 시 LLM 대신 로컬 모델이 동작.
- 관리자 도구 예시: `AI.summarize`(제품 태그라인 생성), `AI.generate`(설명 → 표준 `JSON` 추출, 카탈로그 자동화), `AI.forecast`(5개월 판매 예측).

---

## 📅 버전 / 출시 일정
| 함수 / 기능 | 상태 |
| --- | --- |
| `AI.rank` (semantic ranker 포함) | GA (정식 출시) |
| `AI.if` | GA |
| `AI.generate` | GA |
| `AI.forecast` (TimesFM 기반) | GA |
| `AI.analyze_sentiment` | 신규 |
| `AI.summarize` / aggregate summarize | 신규 |
| Optimized AI functions (`AI.if` 지원) | 신규 |


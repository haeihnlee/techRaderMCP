# Turn Audio into Action with Gemini 3.5 Transcribe

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=r2xhPB-wWIQ
- **요약 일시**: 2026-09-25 09:05:25

---

## 🔑 핵심 요약
- **Gemini 3.5 Transcribe**는 Google Cloud Agent Platform에서 제공하는 차세대 전사(Speech-to-Text) 모델로, 고정밀 음성 인식과 음성 특화 기능 제공
- 파일 기반 전사(`gemini-3.5-transcribe`)와 실시간 스트리밍 전사(`gemini-3.5-transcribe-live`) 두 가지 모델 ID 지원
- 전사 결과를 다른 Gemini 모델(예: `gemini-3.7-flash`)과 연계해 감정 분석·요약 등 구조화된 인사이트 파이프라인 구축 가능

---

## 📣 주요 발표 내용
- **두 가지 모델 ID 제공**:
  - `gemini-3.5-transcribe` — 이미 녹음된 파일(클라우드 스토리지 등) 처리용
  - `gemini-3.5-transcribe-live` — 실시간 스트리밍 전사용 (자막, 받아쓰기 등)
- **기본 내장 기능**:
  - 자동 언어 감지
  - 화자 분리(Speaker Diarization)
  - 단어 수준 타임스탬프
  - **맞춤형 어휘(Custom Vocabulary)** — 산업별 전문 용어(의료·법률·금융 등) 정확도 향상
- Agent Platform API를 통해 접근 가능하며, 모델 학습 없이 즉시 활용 가능
- 전사 후 `gemini-3.7-flash` 등 다른 Gemini 모델로 체이닝해 감정 점수·불만 분류·통화 요약 등 분석 자동화 가능

---

## 💡 개발자 포인트
- 맞춤형 어휘 힌트 없이 의료·법률 전문 용어를 처리하면 오인식 발생 → **Custom Vocabulary 설정 필수**
- 실시간 스트리밍은 `gemini-3.5-transcribe-live`, 배치 처리는 `gemini-3.5-transcribe` — **용도에 따라 모델 ID 구분**
- 전사 파이프라인 예시 (배치):
  1. GCS 버킷에서 오디오 파일 로드
  2. `gemini-3.5-transcribe`로 전사 (화자 분리 옵션 활성화)
  3. 전사 텍스트를 `gemini-3.7-flash`에 전달 → 감정 분석·요약 등 후처리
- 실시간 파이프라인 예시:
  1. 마이크 스트림 → `gemini-3.5-transcribe-live` API
  2. 응답 스트림에서 텍스트 실시간 렌더링
> 모델 학습이나 복잡한 도구 연결 없이 Agent Platform 모델만으로 엔드투엔드 파이프라인 구축 가능 — 빠른 프로토타이핑에 적합

---

## 📅 버전 / 출시 일정
| 모델 | 상태 |
|------|------|
| `gemini-3.5-transcribe` | Google Cloud Next 발표 시점 기준 공개 |
| `gemini-3.5-transcribe-live` | Google Cloud Next 발표 시점 기준 공개 |
| `gemini-3.7-flash` (분석용) | 이미 사용 가능 |

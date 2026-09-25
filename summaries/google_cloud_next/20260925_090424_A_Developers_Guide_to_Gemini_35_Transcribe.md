# A Developer's Guide to Gemini 3.5 Transcribe

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=TMW8wot2sd4
- **요약 일시**: 2026-09-25 09:04:24

---

## 🔑 핵심 요약
- **Gemini 3.5 Transcribe**는 음성-텍스트 변환 전용 모델로, 화자 분리·단어 타임스탬프·사용자 지정 어휘 등 전용 제어 기능을 제공
- 사용 목적에 따라 **동기식(배치)** 과 **실시간 스트리밍** 두 가지 모드로 나뉘며, 각각 별도의 모델 ID와 API를 사용
- 모든 작업은 **Google GenAI SDK** 하나로 처리되며, Gemini Enterprise Agent Platform 클라이언트 설정 한 번으로 두 모드 모두 사용 가능

---

## 📣 주요 발표 내용
- `gemini-3.5-transcribe` — 완성된 녹음 파일 처리용 (`generateContent` API)
- `gemini-3.5-transcribe-live` — 실시간 스트리밍 오디오 처리용 (`live.connect` API / WebSocket)
- **단어 수준 타임스탬프**: `word_timestamp=true` 설정 시 각 단어의 시작·종료 오프셋 반환 → 캡션, 검색 인덱싱, 영상 동기화에 활용
- **다국어 지원**: 기본 자동 감지, `language_codes` 명시로 예측 가능한 결과 확보 / 다국어 혼합 오디오도 처리
- **화자 분리(Speaker Diarization)**: 응답 파트별 화자 라벨 반환으로 누가 무엇을 말했는지 재구성 가능
- **사용자 지정 어휘(Custom Vocabulary)**: 제품명·특수 용어 구문 목록을 추가해 인식률 향상
- 오디오 입력 방법: 메모리 내 바이트 로드 또는 **Google Cloud Storage** `gs://` URI 직접 참조(업로드 불필요)

---

## 💡 개발자 포인트
- **동기식 패턴**: 오디오 바이트 → `Part` 객체 → `generate_content_config` 내 `AudioTranscriptionConfig` 구성 → `generateContent` 호출
- **스트리밍 패턴**: `live.connect` 세션 열고 **두 개의 코루틴** 동시 실행
  - 전송: 원시 PCM 데이터를 작은 블록으로 푸시 (`realtime_input`), 모노 다운믹스 권장
  - 수신: `interim_input_transcription`(실시간 변경 추정치) vs `input_transcription`(최종 확정 세그먼트) 구분
> ⚠️ 스트리밍 시 `response_modalities`를 반드시 `TEXT`로 설정해야 전사 결과가 올바르게 반환됨
> ⚠️ 사용 API(`generateContent` vs `live.connect`)에 따라 **다른 모델 ID**를 사용해야 하므로 혼용 금지
- 공통 옵션(`language_codes`, `custom_vocabulary`)은 동기식·스트리밍 모두 동일하게 지원

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 모델 (배치) | `gemini-3.5-transcribe` |
| 모델 (스트리밍) | `gemini-3.5-transcribe-live` |
| SDK | `google-genai` (Google GenAI SDK) |
| 출시 일정 | 명시 없음 (영상 공개 기준 현재 이용 가능) |

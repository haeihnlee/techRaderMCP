# Coding with ADK to beat a text adventure game

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=omytUseAJy8
- **요약 일시**: 2026-06-18 09:05:15

---

## 🔑 핵심 요약
- Google Cloud Live에서 **ADK(Agent Development Kit)**로 텍스트 어드벤처 게임을 자동 플레이하는 에이전트를 라이브 코딩으로 시연
- 게임 **"Garden of Forgotten Props"**(Zork 스타일)는 Level 0을 수동으로 익힌 뒤 Level 1부터 에이전트가 대신 플레이하도록 설계됨
- **ADK는 모델·언어에 종속되지 않으며** Python/Java/Go/TypeScript/C#(+Kotlin 베타)을 지원, Gemini에 최적화

---

## 📣 주요 발표 내용
- **ADK 개요**: 에이전트는 결국 **LLM과 대화하는 코드 조각**이라는 관점에서 설명
- **지원 언어**: `Python`, `Java`, `Go`, `TypeScript`, `C#` (`Kotlin`은 아직 pre/beta)
- **모델 agnostic**: Gemini가 기본이자 최적화 대상이지만 OpenAI·Claude 등 타 모델도 연결 가능
- **Gemini 접근 2가지 경로**
  - **Vertex AI** 경유 (Google Cloud 계정 + 프로젝트) — 시연에서 사용
  - **AI Studio** 에서 API 키 발급 후 에이전트 설정 시 전달
- **개발 환경**: 로컬 IDE 또는 **Google Cloud Shell**(도구 사전 설치되어 편리, 시연에서 사용)
- **게임 구조**: Level 0~3, 레벨이 올라갈수록 수동 플레이가 어려워져 에이전트 전환을 유도
- **게임 명령어**: `look`, `inventory`, `examine`, `take`, `use`, `drop`, `move`(north/south/east/west), `quit`, `help`
- **리더보드**: 월간 리더보드 + 라이브 전용 24시간 특별 이벤트 리더보드로 경쟁 요소 제공

---

## 💡 개발자 포인트
- 에이전트 구현 **언어 선택은 중요하지 않다** — 어떤 언어로 만들든 핵심은 LLM(Gemini) 연동
- **로컬 개발 시 사전 준비**: `gcloud` 설치 → `gcloud auth login` → `gcloud auth application-default login` → 프로젝트 설정. **Cloud Shell을 쓰면 이 과정이 모두 생략**됨
- AI Studio 경로는 API 키만으로 시작 가능해 진입장벽이 낮고, Vertex AI 경로는 Google Cloud의 빌링·프로젝트 체계와 통합됨

> ⚠️ Vertex AI 경로는 **billing이 활성화된 Google Cloud 계정과 프로젝트**가 필요합니다. 단순 학습 목적이라면 AI Studio API 키 방식이 더 간단합니다.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| ADK 지원 언어 (정식) | Python, Java, Go, TypeScript, C# |
| ADK 지원 언어 (베타) | Kotlin (pre/beta) |
| 라이브 이벤트 리더보드 | 게시 후 24시간 (예: EU 18:00 ~ 익일 18:00) |
| 월간 리더보드 | 매월 갱신 (시연 시점 6월) |

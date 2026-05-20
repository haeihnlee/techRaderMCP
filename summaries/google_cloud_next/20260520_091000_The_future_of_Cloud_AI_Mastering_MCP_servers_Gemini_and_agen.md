# The future of Cloud AI: Mastering MCP servers, Gemini, and agentic workflows

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=-FRomcsclxw
- **요약 일시**: 2026-05-20 09:10:00

---

## 🔑 핵심 요약
- **ADK(Agent Development Kit)** 기반 멀티 에이전트 시스템 구축법 소개, Python/Go/TypeScript/Java 지원
- **Skills + Tools** 조합으로 컨텍스트를 효율적으로 관리하는 새로운 패턴 제시 (YAML 메타데이터 + Markdown body 구조)
- **Google Maps remote MCP 서버**와 **Google Workspace MCP 서버**를 활용한 실전 에이전트 데모 (라스베이거스 마라톤 플래너) 공개, GitHub `race-condition` 저장소로 오픈소스화

---

## 📣 주요 발표 내용

### 🧠 에이전트 기반 구조
- **ADK (Agent Development Kit)**: Google이 시작한 오픈소스 프로젝트
  - Python 기본 라이브러리 외 **Go, TypeScript, Java** 지원
- **모델 선택의 자유**: `Gemini 3.1`, `Flash`, `Pro` 권장이지만 Claude, GPT, GKE 자체 호스팅 오픈 모델도 가능

### 🛠️ Tools vs Skills
| 구분 | 역할 |
|------|------|
| **Tools** | 단순 함수 호출 (계산, MCP 서버 호출, DB 접근) |
| **Skills** | YAML 메타데이터 + Markdown body 구조의 지식 패키지 |

- Skills 동작 방식
  - 에이전트 시작 시 모든 스킬의 **YAML 메타데이터만** 컨텍스트에 로드
  - 작업 중 필요한 시점에 해당 스킬의 **markdown body·스크립트·참조** 추가 로드
  - 컨텍스트를 깔끔하게 유지하면서 필요할 때만 확장

### 🏃 데모: 라스베이거스 마라톤 플래너
3개의 핵심 스킬로 구성:

1. **GIS Spatial Engineering Skill**
   - Python 스크립트로 `GeoJSON` 데이터를 처리
   - 정확히 `26.2 마일 / 42.195 km` 경로를 수학적으로 계산
   - 후반부 고도, 급수대 위치 등 제약조건 반영

2. **Mapping Skill**
   - **Google Cloud remote MCP for Google Maps** 활용
   - 자연어로 Google Maps API 호출
   - 위치 정보 + 과거 기상 데이터 결합

3. **Race Director Skill**
   - 마라톤 운영 노하우 문서 (출발 구간 차선 수, 급수대 간격, 화장실 등)
   - 기존 **Google Doc**을 **Google Workspace MCP 서버**로 가져와 Gemini가 스킬 포맷으로 변환

---

## 💡 개발자 포인트

> **"2026년 개발 환경": Claude, Gemini CLI, Anti-gravity 등 코딩 하네스를 적극 활용하라.**
> 저장소에 `GEMINI.md`, Gemini Skills, Claude Skills 파일을 함께 배포하면 어떤 하네스에서도 즉시 작동.

- **컨텍스트 매니지먼트가 핵심**: 단순 프롬프트 작성이 아닌 "tools + skills + context"의 효율적 조합이 production-ready 에이전트의 조건
- **데이터 그라운딩 필수**: 모델에 추측시키지 말고 GeoJSON·Maps API·과거 날씨 같은 **실제 데이터**로 grounding
  - 예시: 마라톤 경로 좌표는 LLM 추론이 아닌 Python 수학 연산으로 산출
- **MCP 활용 전략**
  - Google Maps API → `Google Maps MCP 서버`로 자연어 접근
  - Google Docs → `Google Workspace MCP 서버`로 가져와 자동 변환
- **오픈소스 레퍼런스**: `race-condition` GitHub 저장소에서 planner agent 전체 코드 확인 가능

---

## 📅 버전 / 출시 일정

| 항목 | 정보 |
|------|------|
| 발표 시점 | Google Cloud Next (개발자 키노트) |
| ADK 지원 언어 | Python, Go, TypeScript, Java |
| 권장 모델 | `Gemini 3.1` (Flash / Pro) |
| 오픈소스 공개 | `race-condition` GitHub 저장소 (Next 기간 중 공개) |


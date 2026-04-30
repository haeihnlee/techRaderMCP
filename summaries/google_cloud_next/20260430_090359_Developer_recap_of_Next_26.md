# Developer recap of Next ‘26

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=N7N0TU9tkzw
- **요약 일시**: 2026-04-30 09:03:59

---

## 🔑 핵심 요약

- **Google Cloud Next '26**에서 공개된 **멀티 에이전트 시스템** 구축 데모 및 신규 개념 상세 소개
- **ADK(Agent Development Kit)** 기반으로 **Skills + Tools** 조합을 통해 효율적인 컨텍스트 관리가 가능해짐
- 데모 앱 **Race Condition** (라스베이거스 마라톤 플래닝 시뮬레이터)이 **오픈소스**로 공개됨

---

## 📣 주요 발표 내용

- 🧰 **ADK (Agent Development Kit)** 정식 소개
  - Google이 시작했지만 **오픈소스** 프로젝트
  - 지원 언어: **Python**, **Go**, **TypeScript**, **Java**

- 🤖 지원 모델 (모델 선택 자유)
  - `Gemini 2.5 Flash`, `Gemini 2.5 Pro` 등 Gemini 계열
  - **Bring Your Own Model** 지원: Anthropic, OpenAI, GKE 자체 호스팅 모델 등 모두 연동 가능

- ⚡ **Skills** — 신규 핵심 개념
  - 구조: `YAML 메타데이터` (짧은 설명) + `Markdown 본문` (코드·스크립트·레퍼런스 포함)
  - 에이전트 시작 시 **YAML 메타데이터만 로드** → 필요 시 전체 Markdown 본문을 동적으로 로드
  - 컨텍스트 윈도우를 효율적으로 절약하는 **지연 로딩(Lazy Loading)** 방식

- 🛠️ **Tools** — 기존 함수 호출 방식
  - 순수 연산 함수 또는 외부 서비스 호출 모두 가능
  - **MCP(Model Context Protocol) 서버** 연동 지원

- 🗺️ 데모에서 활용된 Skills / Tools 목록

| 이름 | 유형 | 역할 |
|---|---|---|
| `GIS Spatial Engineering` | Skill (Python 스크립트) | GeoJSON 기반 마라톤 루트 계산 (42.195km) |
| `Mapping` | Skill (MCP) | `Google Maps Remote MCP` 서버 연동, 날씨 정보 포함 |
| `Race Director` | Skill (문서 변환) | Google Docs → Skill 자동 변환 (`Google Workspace MCP` 활용) |

- 📂 **Race Condition** 시뮬레이션 앱 오픈소스 공개
  - GitHub 리포지토리명: `race-condition`
  - `agents.mmd`, `gemini.mmd` 파일 포함 (AI 코딩 어시스턴트 친화적 구성)
  - **Gemini CLI**, **Claude**, **Cursor** 등 AI 코딩 도구와 즉시 연동 가능

---

## 💡 개발자 포인트

- **Skills의 핵심 가치는 컨텍스트 효율화**
  - 기존 방식은 모든 툴 정보를 컨텍스트에 올려 토큰 낭비 발생
  - Skills는 `YAML` 요약만 유지 → 실행 필요 시 전체 `Markdown` 로드 → **토큰 절감 + 응답 품질 향상**

- **자연어로 API 호출** — MCP 서버 활용
  - Google Maps API를 직접 쿼리하는 대신 `Google Maps Remote MCP`를 통해 자연어로 접근 가능

- **Google Docs → Skill 자동 변환 워크플로**
  - 기존 사내 문서(Google Docs)를 `Google Workspace MCP` + Gemini로 Skill 형식으로 변환
  - 인간이 읽던 문서를 에이전트가 소비 가능한 형태로 빠르게 전환 가능

> ⚠️ **중요**: Skills는 2026년 기준 **비교적 새로운 개념**으로, 기존 Tools 방식과 병행 사용을 권장. 두 개념의 역할 구분(Tools = 함수 실행, Skills = 컨텍스트 효율적 지식 로딩)을 명확히 이해하고 설계해야 함.

> 💡 **오픈소스 활용 팁**: `race-condition` 리포에 포함된 `.mmd` 파일은 Gemini CLI / Claude 등 AI 코딩 어시스턴트가 프로젝트 구조를 자동으로 파악할 수 있도록 설계되어 있어, **AI-assisted 개발 워크플로**에 바로 활용 가능.

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|---|---|
| 공개 시점 | Google Cloud Next '26 기간 중 오픈소스 공개 |
| ADK 지원 언어 | Python (최초), Go / TypeScript / Java (추가 지원) |
| 지원 Gemini 모델 | `Gemini 2.5 Flash`, `Gemini 2.5 Pro` 등 |
| 데모 앱 | `race-condition` GitHub 리포 (영상 설명란 링크 참조) |

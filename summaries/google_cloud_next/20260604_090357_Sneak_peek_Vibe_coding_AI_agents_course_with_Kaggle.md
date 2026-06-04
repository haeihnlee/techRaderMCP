# Sneak peek: Vibe coding AI agents course with Kaggle

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=eG5RpppF-Xo
- **요약 일시**: 2026-06-04 09:03:57

---

## 🔑 핵심 요약
- **Kaggle**과 **Google**이 공동 진행하는 신규 무료 강좌 **"5 Days of Coding Agents"**(코딩 에이전트 5일 과정)의 사전 소개 영상
- 최근 **Google Cloud Next**와 **I/O**에서 발표된 에이전트 개발 스택(`Antigravity 2.0`, `ADK 2.0`, `Managed Agents API`, 50+ Google 관리형 MCP 서버)을 강좌에서 직접 다룰 예정
- 코드랩·라이브스트림·백서·Discord를 활용한 **멀티모달 집중 과정**으로, AI 발전 속도가 너무 빨라 "책으로 내면 출간 전 구버전이 된다"는 문제의식에서 출발

---

## 📣 주요 발표 내용

**🧑‍🏫 강좌 개요**
- 진행: Brenda Flynn(Kaggle 파트너십 리드), Anant Nawalgaria, Smitha(Google Cloud DevRel 엔지니어, 라이브스트림 호스트)
- **네 번째 시즌**으로, 지난 6개월간의 급격한 AI 발전 내용을 반영해 전면 개편

**🛠️ 강좌에서 다룰 Google 신규 에이전트 스택**

- **`Antigravity` (안티그래비티)** — 에이전트 우선 개발 플랫폼
  - I/O에서 `Antigravity 2.0` 독립형 데스크톱 앱 출시
  - 여러 에이전트를 **병렬 실행**, 동적 서브에이전트 생성, 백그라운드 자동화 작업 예약
  - **AI Studio · Android · Firebase** 네이티브 연동
  - 터미널용 `Antigravity CLI`도 제공(동일 품질, 속도 최적화)

- **`Gemini Enterprise Agent` 플랫폼** — 기존 **Vertex AI의 진화형**
  - `Model Garden`에서 **200개 이상 모델** 선택 가능
  - 상호작용 · DevOps · 오케스트레이션 + **보안/거버넌스** 강화

- **`ADK 2.0` (Agent Development Kit)** — 개발자용 에이전트 개발 키트
  - 통합 **그래프 기반 엔진**: 동적 모델 추론 ↔ 엄격한 결정론적 워크플로우를 슬라이더로 조절
  - **Android용 Kotlin SDK(베타)** 추가 → 모바일 에이전트와 백엔드 Python 에이전트 연동

- **`Managed Agents API`** — 단일 API 호출로 격리된 Linux 환경에서 추론·도구 사용·코드 실행하는 에이전트 생성
  - `Antigravity` 에이전트 하네스 기반, **`Gemini 3.5 Flash`** 구동
  - 영속적·격리 환경으로 **호출 간 재개(resume)** 지원

- **Google 관리형 MCP 서버 50개 이상** (GA 또는 프리뷰)
  - `BigQuery`, `Maps`, `Workspace`, `Cloud Run` 등 → 모든 Google Cloud 서비스가 기본적으로 **MCP 지원**
  - `Model Armor`로 **프롬프트 인젝션 방어** + 전체 관측성(observability) 내장

**🎮 Kaggle 플랫폼 신규 기능**
- **Game Arena** — 모델 간 직접 대결(예: 체스)로 정적 벤치마크가 아닌 **상호 비교 평가**
- **Benchmarks** — 사용자가 직접 태스크를 정의하면 Kaggle이 백엔드 인프라를 처리하는 공개 벤치마크 플랫폼

---

## 💡 개발자 포인트

- **에이전트를 코드로 직접 구축**하려는 개발자라면, 강좌가 다루는 `ADK 2.0`·`Managed Agents API`가 실전 진입점
- "머신이 아닌 미션을 관리하라(manage the mission, not the machine)" — Google Cloud가 격리 환경·스케일링 등 인프라 부담을 대신 처리
- 모든 Google Cloud 서비스가 **기본 MCP 지원**이 되면서, 프로토타입과 프로덕션 배포의 경계가 사실상 사라짐

> **주목:** 엔터프라이즈가 에이전트를 **자율 실행(autonomous)** 시키려면 보안/거버넌스가 핵심. `Gemini Enterprise Agent`의 거버넌스 기능과 `Model Armor`(프롬프트 인젝션 방어)가 이를 담당한다.

> **모바일 개발자 참고:** `ADK 2.0`의 **Kotlin SDK(베타)**로 Android 온디바이스 에이전트와 백엔드 Python 에이전트를 끊김 없이 협업시킬 수 있다.

---

## 📅 버전 / 출시 일정

| 항목 | 상태 / 버전 | 비고 |
|------|------------|------|
| Antigravity | `2.0` (독립형 데스크톱) | I/O에서 발표, CLI 버전 동시 제공 |
| ADK | `2.0` | Android용 Kotlin SDK는 **베타** |
| Managed Agents API | 신규 | `Gemini 3.5 Flash` 구동 |
| Google 관리형 MCP 서버 | **50개 이상** GA 또는 프리뷰 | Next에서 발표 |
| Gemini Enterprise Agent | Vertex AI 후속 | Model Garden 200+ 모델 |
| 5 Days of Coding Agents 강좌 | 4번째 시즌 (예정) | Kaggle × Google 공동, 무료 |


# Build a multi-agent system using ADK & MCP

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=W54cRxp-bSA
- **요약 일시**: 2026-06-30 09:11:12

---

## 🔑 핵심 요약
- **Google ADK**(Agent Development Kit) + **MCP** + **Gemini 3 Flash**로 멀티에이전트 영화 추천 시스템을 구현한 데모
- **루트 에이전트**가 각 서브에이전트의 `description`을 LLM으로 읽고 라우팅 — `if-else` 분기 코드 없이 의도 감지
- 프로덕션 수준의 핵심 패턴 4가지: **MCP 웹 접근**, **3단계 안전 콜백**, **세션 상태 영속화**, **instruction 템플릿**

---

## 📣 주요 발표 내용
- **멀티에이전트 구조**: 루트(`Critique's Cut Director`) 아래 3개 서브에이전트
  - `critic` — 영화 리뷰 담당
  - `recommender` — 다음 볼 영화 추천
  - `watchlist` — 대화 전반에 걸쳐 개인 목록 관리
- **MCP로 실제 웹 접근**: 오픈소스 `MCP server fetch`를 연결해 에이전트가 Rotten Tomatoes 페이지 HTML을 직접 읽고 평점을 실시간 추출 (movie API·하드코딩 없음)
- **ADK MCP tool set**이 `uvx`로 서버를 자식 프로세스로 띄우고 표준 IO 전송·툴 디스커버리까지 한 번의 선언으로 처리
- **커스텀 툴**: 일반 Python 함수의 시그니처·docstring을 읽어 자동으로 툴 스키마 생성. 타입 안정성을 위해 `Pydantic` 모델(`WatchlistAction` enum, `WatchlistResult`) 사용
- **`tool_context` 주입**: 함수에 선언하면 ADK가 런타임에 세션 컨텍스트를 자동 제공 (LLM 스키마에는 노출 안 됨) → 워치리스트를 세션 상태에 읽고 씀
- **instruction 템플릿**: 프롬프트의 `{user_watchlist}` 중괄호 구문을 ADK가 세션 상태로 치환 → 코드 없이 컨텍스트 인지형 프롬프트
- **글로벌 instruction**: 루트에 선언하면 계층 전체 에이전트에 적용 (마크다운 포맷 강제, 주제 이탈 방지)
- **`output_key`**: 에이전트 응답을 세션 상태에 자동 저장(`last_review`)해 재조회 없이 참조

---

## 💡 개발자 포인트
- **3단계 안전 콜백**이 데모를 프로덕션으로 끌어올리는 핵심 (프레임워크 포크·몽키패치 불필요한 1급 확장 포인트)

| 콜백 | 위치 | 역할 |
| --- | --- | --- |
| `before_model_callback` | 루트, LLM 호출 전 | **입력 방화벽** — 5개 정규식으로 프롬프트 인젝션 탐지 |
| `after_model_callback` | LLM 응답 후 | **출력 필터** — PII(이메일·주소·전화·SSN) 마스킹 |
| `before_tool_callback` | watchlist 에이전트, 툴 실행 전 | **인자 검증** — 제목 200자·목록 50개 제한, 공백 제거 |

> `before` 콜백에서 `LlmResponse`를 반환하면 LLM 호출 자체가 **단락(short-circuit)** 됩니다. 모델은 메시지를 보지 못하고 **토큰 0·지연 0**으로 즉시 거부 응답. 정규식은 결정적이고 무료 — 알려진 공격 패턴에 적합하며, 신종 공격은 그 위에 LLM 분류기를 얹는 방어 심층화 권장.

- **세션 상태 영속화**: 워치리스트는 모듈 전역 변수가 아니라 ADK 세션 상태 엔진에 저장 → 다른 턴·다른 에이전트에서도 유지
- 전체 프로젝트는 **단 4개의 Python 파일**(agent 정의, guardrails, models, tools) + API 키 환경 파일. `pip install` → 키 설정 → `adk run`

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| 사용 모델 | **Gemini 3 Flash** |
| 프레임워크 | Google **ADK** (Agent Development Kit) |
| 프로토콜 | **MCP** (Model Context Protocol) |
| 참고 | 자세한 내용은 `ADK.dev` 참고 |


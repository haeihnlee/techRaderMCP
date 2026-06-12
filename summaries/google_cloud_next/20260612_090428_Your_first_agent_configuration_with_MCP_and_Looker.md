# Your first agent configuration with MCP and Looker

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=yeRvxe7MRj4
- **요약 일시**: 2026-06-12 09:04:28

---

## 🔑 핵심 요약
- **Google ADK**(Agent Development Kit)와 **MCP Toolbox for Databases**를 이용해 **Looker**에 연결되는 기본 AI 에이전트를 처음부터 구성하는 실습 가이드
- `tools.yaml` 파일 하나로 Looker 소스와 도구(`get_connections` 등)를 선언하면 LLM이 description을 보고 알맞은 도구를 자동 호출
- 빈 프로젝트에서 시작해 **로컬에서 동작하는 에이전트 앱**(`adk web`)까지 완성 — 엔터프라이즈 데이터에 그라운딩된 에이전트의 첫걸음

---

## 📣 주요 발표 내용
- **Looker + AI 에이전트 연동**: Looker의 데이터 모델링·거버넌스·시각화 기능을 LLM 에이전트에서 직접 활용 가능
- **ADK(Agent Development Kit)**: Google 스케일에서 검증된 **오픈소스 에이전트 프레임워크** — `adk create <agent_name>`으로 agent Python 파일, env 파일, init 파일 자동 생성
- **MCP Toolbox for Databases**: Looker용 **사전 구축(pre-built) AI 도구** 제공 — 대시보드 조회, Look/Explore 조회, dev mode 전환, 대시보드 생성, **헬스 분석**까지 지원
- `tools.yaml` 구성 방식:
  - `sources` 키 아래 Looker 소스 정의 (`kind: looker`, base URL, 포트 포함)
  - `tools` 키 아래 사용할 도구 정의 — 예: `get_connections` (DB 메타데이터 조회)
  - client ID/secret은 **환경변수 참조 문법**으로 주입
- 에이전트 Python 파일에서 **stdio 서버 파라미터**로 로컬 MCP 서버를 연결하고, MCP tool set을 지정한 뒤 원하는 LLM으로 **root agent**를 생성
- `adk web`으로 실행 후 "What tools do you have available?"로 도구 노출 확인 — `tools.yaml`에 도구를 추가하고 재시작하면 즉시 반영

---

## 💡 개발자 포인트
- **인증 준비가 선행 조건**: Looker 계정에서 **client ID / client secret** API 자격증명을 발급받아 **환경변수로 보관**해야 MCP 서버가 사용자를 대신해 동작 가능

> 계정 설정에서 API 키 관리 메뉴가 보이지 않으면 **Looker 관리자에게 권한을 요청**해야 합니다. 자격증명을 코드에 하드코딩하지 말고 반드시 환경변수로 관리하세요.

- 개발 환경: **`uv` 패키지 매니저**로 Python 가상환경 생성 → `google-adk` 설치 + 추가 의존성 별도 설치 필요
- **도구 description이 곧 라우팅 로직**: LLM은 `tools.yaml`의 description을 읽고 호출할 도구를 결정하므로, 명확한 설명 작성이 에이전트 품질을 좌우
- 도구는 최소 1개로 시작해 점진적으로 확장하는 패턴 권장 — Looker용 MCP 도구는 계속 추가되고 있어 주기적 확인 필요
- `tools.yaml` 수정 후에는 `adk web` **재시작**이 필요 (핫 리로드 아님)

---

## 📅 버전 / 출시 일정
해당 없음

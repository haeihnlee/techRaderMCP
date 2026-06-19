# How to build an AI Agent and MCP Server (step-by-step)

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=wBnnA8aIxUs
- **요약 일시**: 2026-06-19 09:06:52

---

## 🔑 핵심 요약
- **MCP**(Model Context Protocol)는 에이전트가 외부 도구와 통신하는 **표준 프로토콜**로, 둘 사이의 "번역기" 역할을 한다
- 각 도구는 **독립된 프로세스**로 실행되어 `stdio`(표준 입출력)로 에이전트와 통신 → 격리·상호운용·확장에 유리
- Google **ADK**(Agent Development Kit) 기반 블로그 작성 에이전트에 Google Trends MCP 서버를 붙여 **실시간 트렌드 데이터**를 가져오는 실습 진행

---

## 📣 주요 발표 내용
- **MCP의 동작 흐름**
  - 도구는 자체 프로세스로 실행되고, 에이전트가 `stdio`로 연결
  - 에이전트가 "어떤 도구가 있냐"고 물으면 서버가 **도구 이름·인자·반환값 스키마** 목록을 응답
  - 에이전트가 `도구명 + JSON 인자`로 호출하면 도구가 실행 후 **JSON 결과** 반환
- **MCP가 강력한 이유 4가지**
  - **격리(Isolation)**: 도구가 죽어도 에이전트는 멈추지 않음
  - **상호운용(Interoperable)**: Python·Go·Node 등 언어 무관
  - **발견 가능(Discoverable)**: 도구가 스키마로 자신을 설명 → 런타임에 사용법 파악
  - **확장(Scalable)**: 에이전트 코드 수정 없이 도구 추가·교체·버전 관리 가능
- **MCP 서버 구현 4단계** (단일 Python 파일)
  - 일반 함수 `trends`를 `FunctionTool`로 래핑 → 시그니처·docstring에서 스키마 자동 생성
  - **MCP Server 객체** 생성 (에이전트와 도구 사이의 작은 프로그램)
  - **2개 핸들러** 구현: `list_tools`(도구 목록 응답) + `call_tool`(이름 검증 후 실제 함수 호출)
  - 서버를 `stdio`에 연결하고 `asyncio.run`으로 핸드셰이크 실행
- 마지막으로 `main agent.py`에서 root agent의 tools 목록에 `trends_mcp`를 추가하면 끝

---

## 💡 개발자 포인트
- **스키마 수동 작성 불필요**: `FunctionTool`이 함수 시그니처와 docstring을 검사해 자동으로 스키마를 생성한다
- 에이전트 입장에서 MCP 도구 호출은 **로컬 함수 호출과 완전히 동일**하게 보인다 → 기존 에이전트에 자연스럽게 통합
- `adk_to_mcp_tool_type` 헬퍼가 ADK 메타데이터를 MCP 클라이언트가 기대하는 형식으로 변환
- 프로토콜의 핵심은 단순함: **"이름 + 인자 입력 → JSON 결과 출력"**
> 도구 호출 시 반드시 **이름을 검증(sanity check)** 한 뒤 인자를 전달하고, 오류 발생 시 작은 JSON 에러를 반환하며 상세 내용은 `stderr`에 로깅할 것. 이 패턴이 에이전트를 가볍게 유지하면서 외부 세계와 연결하는 핵심이다.
- `adk web` 명령으로 ADK Web UI를 띄워 MCP 연결된 에이전트와 바로 상호작용 가능

---

## 📅 버전 / 출시 일정
해당 없음 (튜토리얼 영상 — 특정 버전·출시 일정 정보 없음)


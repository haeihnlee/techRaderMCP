# How to deploy an AI agent to Cloud Run (step by step)

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=bjZ2M7ThOBc
- **요약 일시**: 2026-07-09 09:05:15

---

## 🔑 핵심 요약
- 로컬에서 만든 AI 에이전트를 **ADK(Agent Development Kit)** 로 개발해 **Cloud Run**에 배포하는 전체 과정을 보여주는 실습 영상
- `MCP 서버`에 안전하게 연결되는 툴(Zoo MCP 서버 + Wikipedia 조회)을 가진 "동물원 투어 가이드" 에이전트를 예시로 사용
- 단일 `deploy` 명령으로 컨테이너 빌드부터 Cloud Run 서비스 생성까지 자동화되며, 결과물로 공개 URL이 발급됨

---

## 📣 주요 발표 내용
- **Cloud Run 동작 모델**: 요청이 오면 컨테이너를 띄우고, 트래픽이 늘면 자동 스케일 아웃, 트래픽이 없으면 **0으로 스케일 다운**되어 유휴 비용이 없음
- 사전 준비: Google Cloud 계정 + **Project IDX** 필요, 관련 코드랩(`build and deploy an ADK agent that uses an MCP server on Cloud Run`) 제공
- 사전 단계로 `run`, `Cloud Build`, `Artifact Registry`, `Vertex AI`, `Compute` API를 프로젝트당 1회 활성화
- `requirements.txt`에 의존성을 **버전 고정(pin)** 하여 컨테이너를 가볍게 유지하고 콜드 스타트를 빠르게 함
- 에이전트 런타임용 **전용 서비스 계정**을 생성하고, `Vertex AI` 호출 권한과 (보호된 경우) MCP 서버 호출 권한을 부여
- `.env` 파일에 모델 이름과 MCP 서버 URL 등 설정값을 분리해서 관리 (Cloud Run에서는 환경변수나 Secret Manager 사용 권장)
- `agent.py` 구성 요소:
  - 방문자의 첫 프롬프트를 공유 상태(state)에 저장하는 헬퍼 툴
  - `MCPToolset`으로 Zoo MCP 서버 연결 (인증 필요 시 Cloud Run 대상 signed ID token을 bearer token으로 전달)
  - `LangChain adapter`를 활용한 Wikipedia 조회 툴
  - **researcher agent** (MCP 툴/Wikipedia 툴 선택 사용) + **presenter agent** (친근한 응답 포맷팅)를 `SequentialWorkflowAgent`로 연결
  - 대화 진입점 역할을 하는 `root agent`가 인사 후 researcher→presenter 워크플로우로 전달
- 배포: `adk deploy` 계열 명령이 소스 빌드 → Artifact Registry 푸시 → Cloud Run 서비스 생성까지 한 번에 처리, `--with_ui` 플래그로 테스트용 웹 UI도 함께 제공

---

## 💡 개발자 포인트
> **주의**: 서비스 계정에 MCP 서버 호출용 `Cloud Run Invoker` 역할을 부여하지 않으면 배포 후 `403` 오류가 발생하는 가장 흔한 실수라고 강조함
> **주의**: `Vertex AI User` 역할을 부여하지 않으면 서비스는 정상 기동되지만 모델 호출 시 런타임 권한 오류가 발생함
- 배포 시 "unauthenticated access 허용" 여부를 묻는데, 실습 목적으로는 허용하지만 **운영 환경에서는 서비스를 private으로 유지하고 인증 프록시나 백엔드 연동을 앞단에 둘 것을 권장**
- MCP 기반 툴 설계 덕분에 이후 기능(툴) 추가 시 오케스트레이션 코드를 다시 작성할 필요 없이 확장 가능
- 테스트 후에는 Cloud Run 서비스와 (실습용으로 생성한) Artifact Registry 소스 배포 리포지토리를 정리(`--quiet` 플래그로 프롬프트 생략 가능)해 불필요한 리소스를 남기지 않을 것

---

## 📅 버전 / 출시 일정
해당 없음
</summary_markdown>
</invoke>


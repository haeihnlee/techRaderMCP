# Automate project intake with multi-agent AI using MCP, Google ADK, Cloud Run, and BigQuery

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=okx6dUzDPRY
- **요약 일시**: 2026-06-03 09:06:25

---

## 🔑 핵심 요약
- **Google ADK** + **A2A**(Agent-to-Agent) + **MCP**를 결합해 프로젝트 인테이크(접수)를 자동화하는 **멀티 에이전트 시스템** 데모
- Asana 폼 제출 → 약 **20초** 만에 리스크 점수·리소스 가용성·과거 패턴 분석·실시간 워크스페이스 컨텍스트가 자동 보강된 태스크 반환
- 모든 에이전트가 개별 **Cloud Run** 컨테이너로 동작하며 요청 사이 **0으로 스케일(scale-to-zero)** → 요청당 과금으로 비용 효율화

---

## 📣 주요 발표 내용
- **3계층 아키텍처**로 구성
  - **좌측**: Asana → 폼 제출이 태스크를 만들고 **webhook** 발화 (휴먼 인터페이스)
  - **중앙**: Google Cloud → webhook 리시버, **ADK 오케스트레이터**, 전문 에이전트 4개
  - **우측**: Asana를 다시 **데이터 소스**로 사용 (live work graph 조회)
- **오케스트레이터**는 Google **ADK LLM 에이전트**
  - 세션 상태 관리, Gemini API 연결, 툴 디스패치 로직을 ADK가 대신 처리
  - 에이전트 정의는 인스트럭션과 툴을 모델링한 **클래스 하나**가 전부
- 에이전트 4종: **BigQuery 분석가** / **리소스 어드바이저** / **Asana 컨텍스트** / **리스크 스코어러**
  - 오케스트레이터가 3개는 **병렬**, 1개는 **A2A 프로토콜**로 **순차** 디스패치
- 전문 에이전트는 모두 **Vertex AI**를 통해 **Gemini** 사용
- **BigQuery 에이전트**: Google 관리형 **BigQuery MCP 서버**에 연결, 요청에 맞춰 **런타임에 SQL을 직접 생성**해 수백 개 과거 프로젝트에서 패턴 탐색

---

## 💡 개발자 포인트
- **MCP 툴셋 재사용**: `MCPToolset` 같은 동일 클래스로 URL만 바꿔 BigQuery·Asana 등 서로 다른 MCP 서버에 동일한 방식으로 연결 → "오픈 표준"의 실전 의미
- **오케스트레이터 디커플링**: 오케스트레이터는 각 전문 에이전트의 내부 구현을 모르고, **URL로 태스크를 보내고 결과만 대기**
  - 덕분에 오케스트레이터를 건드리지 않고 에이전트를 **교체·추가·변경** 가능
- **인증 자동화**: BigQuery 에이전트는 **Application Default Credentials**와 **Secret Manager**를 자동 사용. 같은 프로젝트라도 에이전트별로 다른 자격증명 적용 가능
- **관측성(Observability)**: 각 에이전트의 요청·페이로드·응답, 오케스트레이터↔에이전트 통신이 모두 **Google Cloud Logging**에 추적됨

> ⚠️ 흔한 실수: 모든 데이터를 CSV로 덤프해 매 실행마다 프롬프트에 주입하는 방식은 **컨텍스트 윈도우를 초과**시키고 **API 비용을 급증**시키며, 데이터가 바뀌는 순간 **stale(낡음)** 상태가 됩니다. → 런타임 SQL 생성 + MCP 라이브 조회로 해결.

> 💡 전체 소스 코드가 **GitHub**에 공개되어 있어 clone 후 몇 개 명령으로 본인의 Google Cloud 프로젝트에서 바로 실행 가능.

---

## 📅 버전 / 출시 일정
해당 없음 (제품 출시가 아닌 아키텍처/구현 데모 세션)


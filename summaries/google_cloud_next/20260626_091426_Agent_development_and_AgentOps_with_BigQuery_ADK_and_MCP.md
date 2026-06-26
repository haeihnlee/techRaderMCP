# Agent development and AgentOps with BigQuery, ADK, and MCP

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=tQGalTBL1Ek
- **요약 일시**: 2026-06-26 09:14:26

---

## 🔑 핵심 요약
- **BigQuery 기반 에이전트** 구축을 위한 옵션을 **스택(stack)** 형태로 제공 — 위로 갈수록 Google이 제공하는 가치(추론·Gemini)가 커지고, 아래로 갈수록 개발자의 유연성·소유권이 커짐
- **`ADK`(Agent Development Kit)**, **오픈소스 `MCP Toolbox`**, **관리형 `BigQuery MCP Server`**, **Data Agent**까지 4단계 선택지가 모두 **GA(정식 출시)** 상태
- **Agent Analytics** 출시 — 코드 **한 줄 추가**로 에이전트 활동 로그를 BigQuery로 실시간 스트리밍해 **AgentOps/관측성(observability)** 확보

---

## 📣 주요 발표 내용
- **`ADK` + BigQuery 1st-party 툴** (stable/GA)
  - **Foundational 툴**: 테이블 탐색·메타데이터 조회·다양한 모드 쿼리
  - **Advanced 툴**: 예측(forecasting), 기여도 분석(contribution analysis) 등 BigQuery 고급 기능
  - 외부에서 만든 **Data Agent를 ADK 내 툴**로 재사용 가능, **BigQuery Skills**도 ADK에 직접 내장
  - `pip install` 시 BigQuery 툴이 기본 포함 — **10줄 이내 코드**로 Data Agent 완성

- **오픈소스 `MCP Toolbox`** (stable/GA)
  - 다중 데이터 커넥터 포함, **`YAML`로 툴 구성** 후 로컬/원격 MCP 서버 실행
  - 핵심: **파라미터화된 SQL(parameterized SQL)** 로 커스텀 툴 정의 → 에이전트가 SQL을 직접 쓰지 않고 파라미터만 전달해 **결정성(determinism)** 확보

- **관리형 `BigQuery MCP Server`** (GA)
  - 엔드포인트: **`bigquery.googleapis.com/mcp`** / Zero-ops, 완전 관리형·원격·확장 가능
  - **`IAM` · audit log · `VPC SC`** 등 거버넌스 통합
  - **read-only SQL 툴**(DML/DDL 차단)과 **read-write SQL(`execute SQL`) 툴** 제공
  - **Cloud Registry** 등에서 검색 가능 / Anthropic·Glean 등이 내부·고객용으로 활용 중

- **Data Agent** (GA)
  - Google의 에이전트 하네스·추론·Gemini를 그대로 쓰고 **데이터셋만 가져오면** 콘솔에서 바로 대화
  - **Knowledge Catalog** 컨텍스트 자동 수집 + 비즈니스 컨텍스트 추가 가능
  - **Gemini Enterprise · Looker Studio · Slack** 등으로 게시·배포, API로 업무 앱 통합

- **Agent Analytics** (GA, 4개월 전 출시)
  - **ADK용 오픈소스 플러그인** + **LangGraph용 콜백 핸들러**
  - **한 줄 변경**으로 에이전트 활동을 BigQuery 테이블에 **스트리밍 write** → 거의 실시간 분석, 멀티모달 로그 지원

---

## 💡 개발자 포인트
- 지난 **6개월간 에이전트 개발자 20배 증가**, 월 수백만 쿼리가 agentic 연결을 통해 BigQuery로 유입 — 프로덕션 도입 단계로 빠르게 이동 중
- **에이전트 관측성은 전통적 관측성과 다름**:
  - 에이전트 **로그는 코드만큼 중요** (실행 전엔 동작을 알 수 없음, 개발 단계에서도 필요)
  - 로그가 **에이전트 평가(golden dataset 비교)·최적화**의 핵심 → 단순 group by/filter로 부족, **LLM-as-a-judge** 같은 고급 분석 필요
  - 향후 로그는 **멀티모달**(이미지·비디오·오디오 전사) 성격

> **데이터 보호 주의:** read-only SQL 툴은 모든 DML/DDL을 차단해 에이전트가 **의도치 않게 데이터를 수정하는 것을 방지**합니다. 데이터 소유자는 에이전트 개발자에 의존하지 않고 **`IAM` deny 정책으로 read-write 툴 접근을 프로젝트 차원에서 직접 차단**할 수 있습니다.

> **write mode `block`** 사용 시 데이터 변경이 전혀 일어나지 않도록 강제할 수 있어, 읽기 전용 Data Agent 구성에 권장됩니다.

- 인증은 **Application Default Credentials, OAuth, bearer token** 등 다양한 방식 지원
- MCP 서버 사용 시 **audit log에 추가 라벨**이 붙어 MCP 단위 **비용 추적** 가능

---

## 📅 버전 / 출시 일정

| 항목 | 상태 |
| --- | --- |
| `ADK` BigQuery 1st-party 툴 / Skills | **GA (stable)** |
| 오픈소스 `MCP Toolbox` | **GA (stable)** |
| 관리형 `BigQuery MCP Server` | **GA** |
| Data Agent | **GA** |
| Agent Analytics (ADK 플러그인 / LangGraph 콜백) | **GA** (약 4개월 전 출시) |


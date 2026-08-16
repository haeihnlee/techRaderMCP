# Data agent kit: Your coding agent can now query your data

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=Vs2_Palg1QY
- **요약 일시**: 2026-08-16 09:03:48

---

## 🔑 핵심 요약
- **Data Agent Kit**은 Google이 만든 통합 데이터 에이전트 도구로, BigQuery·Cloud SQL·AlloyDB·Spanner 등 Google Cloud 데이터 서비스에 에이전트가 직접 접근할 수 있게 해줌
- VS Code 계열 IDE(Anti-gravity, Cloud Code, Codex 등) 확장으로 설치하며, 원클릭으로 각 서비스의 **MCP 서버**를 활성화할 수 있음
- **Skills(가이드북)**와 **MCP(커넥터)**의 조합으로 에이전트가 Google Cloud 환경을 이해하고 실제 데이터를 조회·실행할 수 있음

---

## 📣 주요 발표 내용
- **Data Agent Kit** = Agent Skills + MCP Tools + IDE 통합의 패키지
- 지원 IDE: Anti-gravity, Cloud Code, Codex, Gemini CLI 등 VS Code 계열 전반
- 활성화 가능한 MCP: `BigQuery`, `Cloud SQL`, `AlloyDB`, `Spanner`, `Knowledge Catalog`
- **Knowledge Catalog** 통합으로 BigQuery·Cloud SQL·Cloud Storage의 데이터 자산을 단일 뷰에서 탐색 가능
- **Agent Skills**: BigQuery 개발 방법론, Spark ML 작업 등 도메인별 마크다운 가이드 제공
- 자연어 프롬프트로 CFO 질문("평균 주문 금액이 왜 줄었나?")에 대한 데이터 분석을 에이전트가 자동 수행

---

## 💡 개발자 포인트
- **Skills vs MCP 차이점**:
  - `Skills`: 에이전트가 Google Cloud 서비스를 올바르게 사용하는 방법을 담은 가이드북 (마크다운)
  - `MCP`: 실제 데이터베이스에 보안 연결하여 쿼리 실행·데이터 조회 등 액션을 수행하는 커넥터

- MCP는 Google Cloud 계정 인증 기반으로 **보안 연결**을 제공함

> 에이전트가 항상 MCP를 호출하지는 않음 — "이 질문에 테이블 조회가 필요하다"고 판단될 때만 자동으로 BigQuery MCP를 호출함

- GitHub 리포에서 직접 설치도 가능
- 확장 설치 후 설정 패널에서 프로젝트·리전·Billing Project 지정 및 필요한 API 원클릭 활성화

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 관련 IDE | Anti-gravity 2.0 (Google I/O 이후 출시) |
| 설치 방법 | VS Code 확장 마켓플레이스 또는 GitHub repo |
| 출시 상태 | 현재 사용 가능 (hands-on 데모 진행) |


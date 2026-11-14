# Decide which Looker MCP integration is right for you?

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=24WH740Xn9M
- **요약 일시**: 2026-11-14 09:04:42

---

## 🔑 핵심 요약
- AI 에이전트를 **MCP(Model Context Protocol)**로 Looker에 연결하는 방법은 **Looker 관리형 MCP 서버**와 오픈소스 **MCP Toolbox for Databases** 두 가지
- 관리형 MCP 서버는 Looker에 내장되어 있어 **즉시 설정·네이티브 OAuth·유지보수 불필요**가 장점
- MCP Toolbox는 직접 호스팅하는 서버로 **에이전트별 도구 범위 지정·여러 데이터소스 연결·엔지니어링 제어**가 장점

---

## 📣 주요 발표 내용
- **Looker 관리형 MCP 서버**: Looker Core / Looker(original) 관리자가 서버를 활성화하고 노출할 도구를 선별
- 관리자는 Looker 관리 화면에서 도구를 하나씩 켜고 끄며, 승인되지 않은 엔드포인트는 에이전트에 보이지 않음
- **MCP Toolbox for Databases**: 오픈소스 서버이자 프레임워크로, 관리형 서버보다 **사전 구축 도구 카탈로그가 훨씬 넓음**
- Toolbox를 쓰면 Looker의 **LookML 지표·지식 카탈로그**와 **Spanner** 같은 외부 데이터소스를 하나의 흐름 안에서 함께 쿼리 가능
- 데모 1: **VS Code Looker 확장 프로그램**을 클라이언트로 등록 → OAuth 로그인 → 인스턴스 상태 점검 요청
- 데모 2: **Agent Development Kit(ADK)** + `tools.yaml`로 도구를 정의 → 로컬 실행 → **Cloud Run**에 배포

---

## 💡 개발자 포인트
> 관리형 MCP 서버의 도구 활성화는 **인스턴스 전체에 적용**됩니다. 서버 단계에서 에이전트 A에는 켜고 B에는 끄는 식의 설정은 불가능합니다.
- 관리형 서버에서 에이전트별로 범위를 제한하려면 **서비스 계정이나 사용자 역할(Role) 권한**으로 처리해야 함
- 관리형 서버를 쓰려면 관리자가 Looker에 **호출할 클라이언트 앱을 등록**해야 함
- 관리형 서버 인증은 **Looker SSO + OAuth** 방식이며 **API 키나 자격 증명이 로컬에 저장되지 않음**
- 인증 후 에이전트는 **해당 사용자의 Looker 권한 범위 안에서만** 동작
- Toolbox에서는 `tools.yaml`을 고쳐 노출할 소스·도구를 줄이거나 늘릴 수 있음
- Toolbox는 서버를 여러 개 띄울 수 있어 **에이전트·작업마다 다른 도구 세트**를 따로 호스팅 가능하며, 다른 Looker 사용처에 영향을 주지 않음
> Toolbox는 관리 책임이 Looker UI에서 **자체 인프라와 개발팀**으로 옮겨갑니다. 다른 사람이 쓰게 하려면 Cloud Run 등에 배포하고 런타임을 직접 운영해야 합니다.

| 구분 | Looker 관리형 MCP 서버 | MCP Toolbox for Databases |
| --- | --- | --- |
| 호스팅 | Looker 내장 | 자체 호스팅 (예: Cloud Run) |
| 도구 제어 | 관리자 UI 토글 (인스턴스 전체) | `tools.yaml` (에이전트·작업별) |
| 인증 | 네이티브 OAuth / SSO | 직접 구성 |
| 데이터소스 | Looker | Looker + 외부 DB (Spanner 등) |
| 운영 부담 | 없음 | 서버 인프라 직접 관리 |

---

## 📅 버전 / 출시 일정
해당 없음

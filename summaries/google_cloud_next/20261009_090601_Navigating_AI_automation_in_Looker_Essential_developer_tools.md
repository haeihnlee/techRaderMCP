# Navigating AI automation in Looker: Essential developer tools for agents

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=JvASK8qX4hg
- **요약 일시**: 2026-10-09 09:06:01

---

## 🔑 핵심 요약
- Looker 스택에 **AI 에이전트**를 도입하기 위한 5가지 개발자 도구 소개: **Looker Skills**, **Looker CLI**, **Looker 관리형 MCP 서버**, **MCP Toolbox for Databases**, **Looker VS Code 확장**
- **Skills**가 에이전트에게 "무엇을 할지"를 알려주고, **CLI / MCP**가 "어떻게 실행할지"를 담당하는 구조
- 에이전트 권한은 연결된 **Looker 사용자 계정의 역할·폴더 권한을 그대로 상속**하므로 최소 권한 서비스 계정 설계가 핵심

---

## 📣 주요 발표 내용
- **Looker Skills (에이전트용 문서)**
  - 사람과 에이전트 모두 읽을 수 있는 **Markdown 파일** 형태의 전문 지침서
  - 에이전트는 각 파일 헤더의 `name`, `description` 메타데이터만 상시 보관 → 프롬프트 의도에 맞을 때만 전체 Skill을 로드 (컨텍스트 절약)
  - 로드된 지침은 작업 메모리에 동적으로 추가되어 LLM의 초기 가정을 **도메인별 규칙**으로 대체
  - 무거운 작업은 메인 에이전트가 **임시 서브 에이전트**를 생성해 필요한 지침만 전달
  - Looker 오픈소스 저장소에 **온보딩 / 감사(audit) / 성능 최적화** Skill 제공
- **Looker CLI**
  - **Go 기반** CLI로 Looker API를 래핑
  - 터미널 명령으로 대시보드·폴더·사용자·스케줄 등 플랫폼 리소스를 쿼리·자동화
  - 관리자가 활성화해야 하며, 표준 **Looker API 자격 증명** 또는 **OAuth** 필요
- **Looker 관리형 MCP 서버**
  - Looker 플랫폼 내부에 기본 호스팅 → 외부 인프라 불필요
  - 관리자가 **Admin > Platform > MCP** 메뉴에서 도구 on/off
  - Antigravity CLI, Cursor, Claude Desktop 등 AI 클라이언트를 API 자격 증명 / OAuth로 직접 연결
  - 원시 bash 명령 대신 **검증된 스키마 기반 도구 세트**(Explore 쿼리, 대시보드 생성 등) 제공
- **MCP Toolbox for Databases (오픈소스)**
  - 로컬 / Docker / 클라우드 등 사용자 환경에 **셀프 호스팅**
  - **다중 소스 오케스트레이션**: 한 세션에서 Looker + **BigQuery**, **AlloyDB** 등 동시 쿼리
  - 구성 파일을 직접 관리해 **에이전트별 도구 세트 노출**(클라이언트 수준 스코핑) 가능
- **Looker VS Code 확장**
  - 로컬 **Git** 제어를 유지하면서 파일을 Looker **Development Mode**와 직접 동기화
  - API 키 / OAuth로 연결 후 **내부 프록시**를 실행 → 로컬 AI 에이전트가 동일 인증 세션으로 관리형 MCP 서버 사용

---

## 💡 개발자 포인트
> ⚠️ **Looker API 키는 사용자 계정의 권한·역할·폴더 접근권한을 100% 상속**합니다. 개인 자격 증명 대신 **필요한 역할만 할당된 전용 서비스 계정** 사용을 권장합니다.

> ⚠️ **관리형 MCP 서버의 도구 활성화는 인스턴스 전체에 적용**됩니다. 도구를 토글하면 연결된 모든 클라이언트에 영향을 주므로, 개별 에이전트 경계는 **사용자 역할 / 모델 세트 / 폴더 접근**으로 제한해야 합니다.

- 도구 선택 가이드:

| 도구 | 적합한 상황 | 범위 제어 |
|------|------------|----------|
| **Looker CLI** | 로컬에서 에이전트가 터미널로 리소스 자동화 | 계정 권한 |
| **관리형 MCP 서버** | 인프라 없이 빠른 연결 | 인스턴스 전체 |
| **MCP Toolbox for Databases** | Looker + DB 다중 소스, 에이전트별 도구 분리 | 클라이언트 단위 |
| **VS Code 확장** | LookML 개발 + 로컬 Git + 에이전트 협업 | 인증 세션 공유 |

- 에이전트 Skill 설계 시 헤더 메타데이터(`name`, `description`)를 명확하게 작성해야 적절한 시점에 로드됨
- 영상 하단의 **Codelab** 링크로 직접 설정 실습 가능

---

## 📅 버전 / 출시 일정
해당 없음

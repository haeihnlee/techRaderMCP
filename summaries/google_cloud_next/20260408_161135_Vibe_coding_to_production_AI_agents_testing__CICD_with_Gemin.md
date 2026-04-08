# Vibe coding to production: AI agents, testing & CI/CD with Gemini CLI

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=qCBreTfjFHQ
- **요약 일시**: 2026-04-08 16:11:35

---

## 핵심 요약 (3줄)
- Gemini CLI를 활용한 컨텍스트 엔지니어링으로 ADK(Agent Development Kit) 기반 AI 에이전트를 효율적으로 개발하는 방법을 다룸
- Gemini.MD 파일을 통한 프로젝트/글로벌 레벨 컨텍스트 관리와 스킬(Skill) 파일을 통한 동적 컨텍스트 로딩 기법을 소개
- 에이전트 평가(trajectory 분석, 응답 비교), CI/CD 파이프라인 구축, Cloud Run 배포까지 에이전트 개발 전체 라이프사이클을 커버

---

## 주요 발표 내용

- **Gemini.MD 파일 시스템**
  - 프로젝트 루트의 `.gemini` 폴더 내 `Gemini.MD` 파일 = 프로젝트 레벨 컨텍스트
  - 사용자 홈 디렉토리의 `.gemini` 폴더 내 파일 = 글로벌 레벨 컨텍스트
  - Gemini CLI 실행 시 항상 어시스턴트 인스트럭션으로 자동 주입됨

- **스킬(Skill) 기반 동적 컨텍스트 로딩**
  - 필요할 때만 lazily load되는 스킬 MD 파일로 컨텍스트 효율화
  - 항상 로드되는 Gemini.MD와 달리, 관련 시점에만 컨텍스트 활성화

- **ADK 에이전트 설계 문서(agent.design.MD) 활용**
  - LM 에이전트 생성 방법, 패키지 임포트, 에이전트 인스트럭션 등을 담은 블루프린트 파일
  - 로컬 파일로 저장 후 Gemini CLI가 참조하여 올바른 ADK 에이전트 코드 생성

- **Gemini CLI 멀티에이전트 기능**
  - 단순 LLM 래퍼가 아닌 서브에이전트 위임(delegation) 가능
  - 코드베이스 분석 시 "investigator agent" 등 전문화된 서브에이전트 자동 호출

- **에이전트 평가(Agent Evaluation)**
  - Trajectory 분석 및 응답/출력 비교 기능

- **CI/CD 파이프라인 + Cloud Run 배포**
  - 에이전트 빌드 → 배포 → 클라우드 상에서 "보스 파이트(boss flight)" 테스트까지 포함

---

## 개발자에게 중요한 포인트

- **컨텍스트 엔지니어링이 핵심 역량**
  - 모델 성능 한계를 탓하기 전에, 올바른 컨텍스트를 올바른 방식으로 제공하는 것이 바이브 코딩의 핵심
  - ADK를 모르더라도 설계 문서를 컨텍스트로 주입하면 Gemini CLI가 올바른 ADK 에이전트를 생성 가능

- **Gemini.MD 파일 배치 전략**
  - 프로젝트 공통 코딩 표준(Python docstring, type hint 등)은 Gemini.MD에 등록
  - 특정 기능에 특화된 상세 설계(예: 에이전트 설계)는 별도 로컬 파일 또는 스킬로 분리 관리 권장

- **Gemini CLI 실행 위치에 따른 접근 범위 차이**
  - 프로젝트 루트에서 실행 시 전체 폴더 접근 가능
  - 서브폴더에서 실행 시 해당 서브폴더로 범위 제한됨 → 실행 위치 관리 중요

- **자연어로 Shell/Git 명령 대체 가능**
  - `curl`, `git clone` 등 기억하지 않아도 자연어 명령으로 파일 다운로드·조작 가능
  - 반복적인 CLI 작업을 자연어 인터페이스로 추상화

- **멀티에이전트 아키텍처(A2A 서버 포함)**
  - Shadow Blade Agent 등 게임 도메인 특화 에이전트를 ADK로 구축
  - A2A(Agent-to-Agent) 서버, Docker, Cloud Run 배포 구조를 스타터 파일로 제공

---

## 출시 일정 / 버전 정보

해당 없음 (특정 버전 번호나 출시 예정일에 대한 언급 없음. Google ADK 및 Gemini CLI 기반의 핸즈온 랩 세션으로 구성됨)

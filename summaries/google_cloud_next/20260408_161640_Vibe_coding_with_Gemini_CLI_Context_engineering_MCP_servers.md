# Vibe coding with Gemini CLI: Context engineering, MCP servers & extensions

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=cfPW2nTVNOQ
- **요약 일시**: 2026-04-08 16:16:40

---

## 핵심 요약 (3줄)
- Gemini CLI는 터미널 기반의 AI 코딩 에이전트로, MCP 서버 연동 및 확장(Extension) 기능을 통해 개발 워크플로우를 자동화할 수 있다
- Cloud Shell 환경에서 Gemini CLI를 활용한 Vibe Coding(AI 보조 코딩) 실습을 다루며, Artifact Registry, Cloud Run 등 GCP 서비스와의 통합을 포함한다
- 2부 시리즈로 구성되어 있으며, 1부는 MCP 서버/Extension, 2부는 Agent Skills, Hooks, CI/CD 파이프라인 및 클라우드 배포를 다룬다

## 주요 발표 내용
- **Gemini CLI 소개**: 터미널에서 직접 실행하는 AI 코딩 에이전트 (vs. IDE 기반의 Project IDX/Cursor 계열과 차별화)
- **MCP(Model Context Protocol) 서버 연동**: `settings.json` 파일을 통해 MCP 서버를 Gemini CLI에 연결하는 방법 소개
- **Extension 지원**: Gemini CLI에 다양한 확장 기능을 추가하여 도구(Tool) 활용 범위 확장
- **컨텍스트 엔지니어링**: 프로젝트 레벨 및 유저 레벨 메모리(Memory)를 활용한 컨텍스트 관리 방법
- **Design Doc 작성**: Vibe Coding 품질 향상을 위한 설계 문서 작성 방법론 포함
- **A2A(Agent-to-Agent) 연결**: 별도 배포된 Dungeon 에이전트와 CLI 에이전트 간 연결 구성
- **2부 예고**: Agent Skills, Hooks(가드레일), 테스트 자동화, CI/CD 통합, Cloud Run 배포

## 개발자에게 중요한 포인트

**환경 설정**
- Google Cloud Shell을 개발 환경으로 사용 (원격 VM, 파일 영속성 보장)
- 필요 API 활성화 = 비용 발생 아님 (단순히 서비스 스위치 ON)
- Artifact Registry = GCP의 Docker Hub 역할, Cloud Run 배포 전 이미지 호스팅 필수

**Gemini CLI 사용 비용**
- 무료 계정: Gemini 2.5 모델 사용 가능, 호출 횟수 제한 있음
- 유료 계정: Gemini 3 모델 접근 가능
- CLI 자체 설치 및 기본 사용은 **무료**

**보안 / 프로덕션 주의사항**
- 서비스 계정은 역할별로 분리하는 것이 권장 사항 (최소 권한 원칙)
- 실습에서는 편의상 단일 서비스 계정에 다중 역할 부여 → 프로덕션에서는 지양
- Google 개인 계정 사용 권장 (기업/EDU 계정은 제한으로 인한 실습 블로커 발생 가능)

**Gemini CLI vs. IDE 기반 에이전트 비교**
- Gemini CLI: 터미널 중심, 스크립트/자동화에 강점
- Windsurf/Cursor 계열(IDE 기반): 에이전트 매니저 UI 제공, 계획 수립 및 코드 편집 시각화에 강점

## 출시 일정 / 버전 정보
- Gemini CLI: 현재 사용 가능 (무료 티어 기준 Gemini 2.5 지원)
- Gemini 3 모델: 유료 계정에서 접근 가능 (정확한 GA 일정 미언급)
- 실습 2부(Skills, Hooks, CI/CD, 배포): 별도 에피소드로 공개 예정 (구체적 날짜 미정)

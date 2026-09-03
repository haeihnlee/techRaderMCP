# End-to-end agentic development with Google Gemini, Antigravity, and GitLab

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=IXc9d_EN4ts
- **요약 일시**: 2026-09-03 09:07:01

---

## 🔑 핵심 요약
- **Gemini**, **Antigravity**, **GitLab**을 결합해 아이디어 구상부터 코드 생성, 리뷰, 배포까지 이어지는 **엔드 투 엔드 에이전틱 개발 워크플로**를 시연합니다.
- Gemini가 생성한 UI 시안을 바탕으로 GitLab 이슈·브랜치·머지 리퀘스트를 만들고, 별도 작업 브랜치에서 실제 코드를 구현합니다.
- GitLab Duo 에이전트의 코드 리뷰와 보안 스캔, Artifact Registry 업로드를 거쳐 애플리케이션을 **Cloud Run**에 배포합니다.

---

## 📣 주요 발표 내용
- 기존 Python 애플리케이션의 UI를 현대화하기 위해 Gemini에 새로운 UI 시안용 `PNG` 생성을 요청합니다.
- Antigravity에 구성한 **GitLab MCP 서버**를 통해 자연어 지시로 GitLab 이슈를 생성합니다.
- 생성된 이슈를 기반으로 UI 개선 계획용 브랜치와 머지 리퀘스트를 준비합니다.
- Antigravity에서 머지 리퀘스트의 작업 브랜치로 전환해 변경사항이 `main` 브랜치에 직접 반영되지 않도록 합니다.
- Gemini에 UI 이미지를 분석하고 애플리케이션에 맞는 코드를 작성하도록 요청합니다.
- 생성된 변경사항을 검토·승인한 뒤 Gemini의 도움으로 커밋 메시지를 작성하고 원격 GitLab 브랜치에 푸시합니다.
- GitLab Duo 에이전트 플랫폼의 `develop with Gemini` 에이전트를 머지 리퀘스트 리뷰어로 추가해 배포 전 코드를 검토합니다.
- 머지 후 GitLab CI/CD 파이프라인이 실행되고, 보안 스캔과 **Artifact Registry** 업로드를 거쳐 **Cloud Run**에 배포합니다.

---

## 💡 개발자 포인트
- **자연어 기반 개발 자동화**: GitLab MCP 서버를 사용하면 이슈 생성 등 ALM 작업을 IDE 또는 에이전트 대화 흐름 안에서 수행할 수 있습니다.
- **브랜치 격리**: AI가 생성한 코드는 반드시 머지 리퀘스트용 작업 브랜치에서 반영하고, 검토 후 `main`에 병합하는 흐름이 안전합니다.
- **사람의 승인 단계 유지**: 코드 생성 후 변경사항 요약을 확인하고 승인하는 단계를 두어 AI 결과를 바로 원격 저장소에 반영하지 않습니다.
- **에이전트 간 역할 분리**: 한 에이전트는 구현을 담당하고, GitLab Duo 에이전트는 별도 리뷰어로 동작하도록 구성할 수 있습니다.
- **배포 전 검증**: Cloud Run 배포 전에 보안 스캔과 Artifact Registry 업로드를 파이프라인에 포함해 공급망과 런타임 배포 품질을 점검합니다.

> GitLab과 Google Cloud 통합을 시작하기 전에 **Google Artifact Management** 및 **Google IAM** 통합이 사전 설정되어 있는지 확인해야 합니다.

> AI가 생성한 변경사항도 일반 코드와 동일하게 리뷰·테스트·보안 검사를 거친 뒤 병합하고 배포해야 합니다.

---

## 📅 버전 / 출시 일정
해당 없음

# Run Security Analysis using Gemini CLI locally and on GitHub

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=kDtJXgllXko
- **요약 일시**: 2026-04-08 16:17:07

---

## 핵심 요약 (3줄)
- Gemini CLI의 오픈소스 보안 확장(Security Extension)을 통해 로컬 및 GitHub PR에서 자동 보안 분석이 가능하다.
- 시크릿 노출, 인젝션 취약점, 인증 문제, LLM 안전성, 의존성 취약점(OSV DB 기반) 등 다양한 보안 스캔을 지원한다.
- CI/CD(GitHub Actions)에 통합하여 팀 전체 코드 기여물에 동일한 보안 기준을 자동 적용할 수 있다.

## 주요 발표 내용
- **Gemini CLI 보안 확장(Security Extension)** 공개 — Google이 직접 개발한 오픈소스 확장
- **지원 취약점 스캔 범위:**
  - 시크릿/자격증명 노출 (Secrets Management)
  - 안전하지 않은 데이터 처리 (Insecure Data Handling)
  - 인젝션 취약점 (Injection Vulnerabilities)
  - 인증 문제 (Authentication)
  - LLM 안전성 (LLM Safety)
  - **최신 추가: 의존성 취약점 스캔** — Google OSV(Open Source Vulnerabilities) DB 활용
- **로컬 사용 방법:**
  - 확장 설치 후 `/security` 슬래시 커맨드로 커스텀 명령 실행
  - 자연어로 스캔 범위 지정 가능 (예: "모든 HTML 파일 스캔")
  - Yolo 모드(Ctrl+Y) 지원 — 읽기 전용 작업이므로 안전
  - To-do 리스트 생성 → 파일 분석 → 결과 요약 순으로 진행
- **GitHub Actions 연동:**
  - 공식 레포의 예시 워크플로우 복사 후 적용
  - Workload Identity Federation으로 GitHub ↔ Google Cloud 인증 구성
  - 신규 PR 생성 시 자동으로 보안 리뷰 워크플로우 트리거
  - 기존 PR에는 `@GeminiCLI/review` 코멘트로 수동 트리거 가능
- **실사용 레퍼런스:** Gemini CLI, Project Chip, Flutter 등 Google 소유 레포에서 이미 PR 리뷰에 활용 중

## 개발자에게 중요한 포인트
- **개인 기여자:** 코드 커밋 전 로컬에서 보안 스캔 실행 → 사전 취약점 제거 습관화 가능
- **팀/레포 관리자:** GitHub Actions에 통합하면 팀원 모두에게 동일한 보안 기준 강제 적용 가능 (로컬 스캔을 잊은 경우에도 자동 커버)
- **OSV 의존성 스캔** 추가로 서드파티 라이브러리 취약점도 자동 감지 — 별도 도구 없이 통합 관리 가능
- **확장 가능한 아키텍처(Extensible Architecture)** 설계 — 향후 더 고급 보안 분석 기법 추가 시 확장 용이
- **인증 설정**은 제공된 쉘 스크립트로 자동화 가능 — 초기 설정 진입 장벽 낮음
- **무료 Google Cloud 크레딧 제공 코드랩** 활용 가능 — 비용 부담 없이 체험 가능

## 출시 일정 / 버전 정보
- 현재 사용 가능한 상태로 발표 (정확한 버전 번호나 GA 날짜는 언급되지 않음)
- OSV 기반 의존성 스캔은 "최근 추가(Most Recently Added)"된 기능으로 언급
- 코드랩(무료 크레딧 포함) 현재 제공 중

# Agent-first workflows from prompt to production

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=CBL6KgCsQNY
- **요약 일시**: 2026-05-22 09:12:34

---

## 🔑 핵심 요약
- **AI 코딩의 Day 2 문제**(배포·모니터링·디버깅)를 **agent-first 워크플로우**로 해결하는 방법 소개
- `Antigravity` + **Google-managed MCP 서버**로 로그 조회·코드 수정·재배포를 자연어로 자동화
- **Data Agent Kit**으로 Firestore 같은 NoSQL DB도 자연어로 안전하게 조작 가능 (skills 내장)

---

## 📣 주요 발표 내용
- **`Antigravity` 에이전트 도구 데모**: AI Studio로 vibe-coding한 게임("Dino Quest")이 부하로 503 에러 → 음성 입력으로 "Dino Quest 뭐가 잘못됐는지 찾아줘" 명령 → 에이전트가 자동으로 로그·메트릭 조회 후 원인 진단
- **Google-managed MCP 서버 50개+ 제공**: `BigQuery`, `Cloud Run` 등 GCP 서비스에 **API 키 없이** 안전하게 연결
- **`Developer Knowledge MCP`**: AI / Cloud / Firebase 등 12개 이상 Google 공식 문서를 통합 → **최대 8~12시간 이내 최신 문서**가 에이전트로 주입 (Claude Code, Codex, Antigravity 등 모든 도구에서 사용 가능)
- **`Data Agent Kit`** 시연:
  - Firestore 같은 **document DB**에 자연어로 "모든 유저에게 treat 5개 추가" 요청
  - 에이전트가 **Python 스크립트를 작성**하고, **실행 전 사용자 승인 요청** (보안)
  - 단순 MCP 호출이 아닌 **skills(노하우) 내장**으로 올바른 방식으로 DB 조작

---

## 💡 개발자 포인트
- 대부분의 개발자는 AI를 **빌드·문서화·코딩**에만 쓰고 있지만, **Day 2 영역(배포·디버깅·운영)** 자동화가 진짜 생산성 향상의 핵심
- **MCP 기반 워크플로우 mindset shift** 필요: 더 이상 콘솔에서 클릭하거나 API 키 관리할 필요 없이 에이전트가 라이브 환경에 직접 연결

> ⚠️ **보안 주의**: 에이전트가 코드를 실행하기 전 **명시적 사용자 승인 단계**가 반드시 들어가야 함. Antigravity는 Python 실행 전 permission을 요청하는 패턴을 기본 채택.

> 💡 **outdated documentation 문제**: 에이전트가 옛 버전 문서를 참고하면 잘못된 코드 생성. `Developer Knowledge MCP`로 최신 Google 문서를 자동 주입하여 해결.

- Firestore 같은 **NoSQL/document DB**는 SQL과 달리 단순 쿼리로 업데이트 불가 → Data Agent Kit이 skills로 이 복잡성을 추상화
- vibe-coded 앱도 **Cloud Run + Firebase** 조합으로 **신용카드 없이 첫 두 앱은 무료 배포** 가능

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|---|---|
| 행사 | Google Cloud Next (Dev Keynote 연계 세션) |
| 핵심 도구 | `Antigravity 2.0`, `AI Studio` |
| Managed MCP 서버 | 50개 이상 (BigQuery, Cloud Run 등 포함) |
| Developer Knowledge MCP | Google Docs 12개 이상 통합, **최신성 8~12시간 이내** |
| 무료 배포 | Cloud Run + Firebase 첫 2개 앱 (신용카드 불요) |


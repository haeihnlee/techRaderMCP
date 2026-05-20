# Dynamic Firebase skills: Architecting agent ready codebases

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=urBML_2BbD8
- **요약 일시**: 2026-05-20 09:04:02

---

## 🔑 핵심 요약
- **Firebase Skills**를 클라이언트에 동적 로딩하여, 작은 컨텍스트 윈도우로도 상황별 챗봇(환불/업셀 등)을 분리 운영하는 패턴 소개
- **Antigravity** AI DevTool을 활용해 Brownfield(기존) 코드베이스를 *agent-ready*하게 만드는 실전 팁 공유
- AI 개발의 핵심은 코딩 자체보다 **계획(Planning) 단계**에 시간을 투자하는 것 — 전체 작업 시간의 약 **60%**가 설계에 쓰여야 함

---

## 📣 주요 발표 내용
- **Dynamic Firebase Skills 패턴**
  - Firebase의 `AI Logic` + `Firestore`를 통해 클라이언트에 skill을 동적 배포
  - 시나리오별(환불 처리, 업셀 등)로 skill을 분리하여 **컨텍스트 오염 방지** (sandbox)
  - 파일 스토리지 업로드 시 Cloud Function이 자동으로 **YAML 메타데이터** 생성
  - 앱 자체는 **Flutter + Firebase**로 구성, Antigravity에서 통합 빌드
- **Antigravity 활용 영역**
  - 앱스토어 스크린샷·아이콘 생성 등 **비코딩 작업**부터 monorepo 관리까지 커버
  - 여러 프로젝트를 각각 agent로 띄우고 **agent manager**가 조율하는 멀티 에이전트 구조 지원
- **Agent-Ready 코드베이스 만드는 법**
  - 모든 디렉토리에 요약 + 파일 리스트가 담긴 `context.md` 생성
  - 자주 쓰는 작업을 **skill로 추출**
  - **테스트 커버리지** 확보 (agent가 빠르게 변경하므로 회귀 방지 필수)
  - 아키텍처를 **수평적(flat)·horizontal**으로 전환 → 상태를 한 레이어에 두고 리팩토링 용이
- **추천 워크플로우 도구**
  - 프로토타입 공유: **AI Studio**
  - 리서치·문제 분해: **NotebookLM**, **Gemini app**
  - UI 디자인 탐색: **Stitch** (아이디어를 시각화 가능한지 검증)

---

## 💡 개발자 포인트
- **Brownfield 코드베이스에 agent를 투입하기 전**, 먼저 디렉토리별 `context.md` 작성을 자동화하라. agent가 매번 전 파일을 읽지 않아도 빠르게 컨텍스트를 파악 가능
- 인간은 **패턴 매칭**에 강하므로, agent의 작업 결과(파일 시스템·스트리밍 출력)에서 패턴 이탈을 빠르게 캐치하고 **즉시 course-correct**하는 운영 방식이 효과적

> ⚠️ **Greenfield는 존재하지 않는다** — 코드를 한 줄이라도 작성하는 순간 Brownfield가 된다. 즉 *agent-ready 설계*는 신규 프로젝트에서도 첫날부터 적용해야 한다.

> 💡 **Planning 비중 60%** — Gemini app / NotebookLM으로 사전 리서치·프롬프트·컨텍스트를 충분히 만든 뒤 Antigravity에 진입하면 MVP 속도가 극적으로 빨라진다. "어떻게"보다 "어디로 가는지·성공 기준이 무엇인지"를 명확히 하라.

- 큰 파일은 agent에게 **작은 함수로 분리**하도록 지시하고, 유사 로직을 같은 디렉토리로 모으면 다음 작업 시 컨텍스트 품질이 개선됨
- Skill은 단순 정보 묶음이 아니라 **"호출할 도구 + 응답 톤 + 살펴봐야 할 신호"**를 컴팩트하게 패키징하는 단위로 설계할 것

---

## 📅 버전 / 출시 일정
해당 없음 (DevRel 인터뷰 형식, 별도 릴리스 정보 없음)


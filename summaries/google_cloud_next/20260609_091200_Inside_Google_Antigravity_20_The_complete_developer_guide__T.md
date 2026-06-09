# Inside Google Antigravity 2.0: The complete developer guide | The Agent Factory

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=Dk4MD6TNiWE
- **요약 일시**: 2026-06-09 09:12:00

---

## 🔑 핵심 요약
- **Google Antigravity 2.0**는 단순 agentic IDE를 넘어 **agent-first 플랫폼**으로 전환 — `Agent Manager`, `CLI`, `SDK`, `IDE`를 모두 포함
- **Skills**가 핵심 — 모델에 전달할 컨텍스트를 압축하는 "치트시트"로, 재사용 자산·디자인 시스템·트리거형 워크플로우를 담음
- 코드 리뷰는 **선택과 집중** — API 계약/백엔드 인터페이스는 깊게 검토하되, 마케팅 사이트는 시각적 결과만 확인
- **Gemma 4**는 `LM Studio` 등으로 **API 호출 없이 로컬 실행** 가능 (오프라인·비행기 환경에서도 활용)

---

## 📣 주요 발표 내용
- **Antigravity 2.0 구성요소**: `Agent Manager`, `CLI`, `SDK`, `IDE` — 기존 agentic IDE에서 agent-first 플랫폼으로 재설계
- **Skills(스킬)**: 모델용 컨텍스트 압축 도구
  - 재사용 스크립트·타입·디자인 시스템을 내장
  - 글로벌/프로젝트 단위로 등록 (예: Obsidian, Flutter, Firebase, shadcn 전용 스킬)
  - 일회성 트리거부터 전체 앱 빌드까지 워크플로우화
- **I/O 출시 기능들** (Customizations 탭에서 관리)
  - **Android CLI**: 커맨드라인에서 Android 앱 빌드
  - **Chrome 확장 / DevTools / Modern Web Guidance**: 최신 CSS·웹 기능 접근성 향상
- **MCP 서버**: Flutter·Dart 프로젝트에서 **hot reloading**과 dev tooling 제공 → 에이전트가 빌드에 필요한 컨텍스트 확보
- **Gemma 4 로컬 활용**: `LM Studio`로 오프라인 에이전트 구동, 자동완성·지식 검색에 사용

---

## 💡 개발자 포인트
- **"첫 예제는 내가 직접 작성"** 패턴 — 에이전트가 추측하지 않도록 첫 버전을 직접 쓰고, 에이전트가 그 패턴을 확장·복제하게 함
- **Flat Architecture 권장**: `state` / `UI` / `data`를 분리 → 에이전트가 엉뚱한 폴더에 코드를 넣으면 즉시 궤도 수정 가능
- 리뷰 강도는 작업 성격에 따라 차등 적용:

> **API 스키마 변경은 신중하게.** 작은 변경도 사용자의 버전 업데이트/페치 부담을 크게 늘림. "실수였어요, 되돌릴게요"가 통하지 않으니 **API 계약은 확정 전 반드시 깊게 리뷰**할 것.

- 코딩을 **분재(bonsai) 가꾸기**에 비유 — 끊임없이 가지치기해 단순하고 직선적인 구조를 지향 (단순함 ≠ 쉬움)
- AI는 **테스트 스위트를 더 풍부하게** 작성해 자신감 있게 배포하는 데 활용 가능
- 일상의 toil(반복작업) 자체를 에이전트로 자동화 — 프롬프트만으로 Swift 확장/Chrome 확장 전체를 빌드한 사례 소개

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
| --- | --- |
| 플랫폼 | Google Antigravity 2.0 (agent-first) |
| I/O 출시 | Android CLI, Chrome 확장, DevTools, Modern Web Guidance |
| 로컬 모델 | Gemma 4 (`LM Studio`로 로컬 실행) |

> 구체적 날짜·버전 넘버는 영상에서 명시되지 않음 — 위 기능들은 올해 Google I/O 기준 출시분으로 언급됨

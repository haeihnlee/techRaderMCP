# Android Developers Blog: Inside Android Skills - Built for deprecation

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/08/android-skills-philosophy.html
- **요약 일시**: 2026-08-07 09:06:31

---

## 🔑 핵심 요약
- 공식 **Android Skills**는 SOTA 모델이 "아직 모르는" 영역만 골라 만든다 — 모델이 이미 아는 걸 가르치지 않는 것이 원칙
- 스킬 하나당 **100~200 토큰**이 매 태스크 기본 컨텍스트에 주입되고, 실제 활성화되면 수천 토큰으로 뛴다 → 스킬 쌓아두기는 역효과
- 프로젝트의 최종 목표는 **deprecation(폐기)** — "오늘의 스킬은 내일의 모델 안에 들어간다"

---

## 📣 주요 발표 내용
- 2026년 4월 공식 Android Skills 공개 이후 약 **20개** 스킬 배포
- 대상은 의도적으로 **빠르게 변하는 좁은 영역**에 한정: **AGP 9**, **Navigation 3**, 고급 **Camera API**, **Perfetto SQL**
- 모든 스킬은 배포 전 **eval(평가) 세트**를 통과해야 함 — 스킬이 켜져 있으면 pass, 꺼져 있으면 fail 해야 유효
  - > **"Evals are to skills what integration tests are to code."** — 스킬에게 eval은 코드의 통합 테스트와 같다
- eval은 `timeout_s`, `repository`, `prompt`, `commands.build`, `acceptance_criteria` (`project_builds`, `llm_diff_judge`) 구조의 YAML로 정의
- 최소 **Android Studio + 최신 Gemini Flash**에서 검증, 스킬에 따라 **Gemini Pro**·**Antigravity**·서드파티 에이전트까지 호환성 확인
- 모든 eval은 **Knowledge Base 접근 상태**로 실행 → 공식 문서에 이미 있고 모델이 검색해서 찾는 정보면 스킬로 만들지 않음
- **Pull Request는 비활성화** — 평가 인프라가 내부 전용이라 외부 PR을 재평가할 방법이 없음. 대신 **issue**로 버그·최적화·신규 스킬 요청

---

## �ололение 개발자 포인트
- 기본기(Kotlin, Compose 같은)용 스킬은 설치 전에 "내 모델이 이걸 정말 모르나?"를 먼저 따져볼 것
  - > **스킬 하나 설치 = 모든 태스크에 100~200 토큰 상시 과금.** 기본 스킬 대량 설치는 비용만 늘리고 효과는 떨어진다.
- 수백 개 스킬을 설치하는 대신 **Android Knowledge Base** 하나를 쓰는 게 훨씬 효율적
  - Android Studio 에이전트는 이미 내장 도구로 제공
  - 다른 에이전트를 쓰면 **Android CLI**를 설치해 `docs` 커맨드로 공식 문서 접근
- 모델이 과신하며 문서를 안 찾을 때: `AGENTS.md`(또는 동등 파일)에 아래 한 줄 추가
  - `Always consult the official Android documentation when dealing with Android APIs`
- **기본/코어 스킬이 오히려 값어치 있는 4가지 상황**
  | 상황 | 이유 |
  | ------ | ------ |
  | 프롬프트가 모호할 때 | "이 화면에 애니메이션 추가해" 같은 느슨한 지시를 최신 API·스크린샷 테스트 패턴으로 유도 |
  | 작고 저렴한 모델 사용 | **Gemma 4** 같은 open-weight 모델의 지식 공백을 스킬이 메워줌 |
  | 레거시 코드 리팩터링·리뷰 | 모델이 주변 레거시 패턴에 맞추려는 습관을 코어 스킬로 깨뜨림 |
  | 표준에서 벗어난 아키텍처 | LLM은 "Google 방식"을 선호 → 커스텀 뷰 레이어라면 자체 스킬로 명시 필요 |
- 커뮤니티 코어 스킬: **Chris Banes**(Compose/Kotlin 종합), **Ivan Morgillo**(Compose 프로젝트 감사), **Jaewoong Eum**(테스팅·퍼포먼스)
  - > **보안 주의:** 수십~수백 개 스킬이 담긴 저장소는 AI 생성·미검증일 가능성이 높고 **악성 또는 편향된 지시**가 섞일 수 있다. 반드시 신뢰할 수 있는 출처에서만 받고, 범용 소프트웨어 엔지니어링 스킬(대부분 웹 개발용)은 무턱대고 설치하지 말 것.
- 신규 모델이 나오면 eval을 재실행 → 통과하면 해당 스킬은 몇 달 유예 후 **은퇴(retire)**. 스킬 의존 워크플로는 영구적이지 않다고 가정해야 함

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| ------ | ------ |
| 공식 Android Skills 최초 공개 | 2026년 4월 |
| 본 블로그 포스트 | 2026년 8월 6일 |
| 현재 공식 스킬 수 | 약 20개 |
| 검증 기준 모델 | Gemini Flash (최신), 일부 Gemini Pro |
| 스킬 은퇴 정책 | 신규 모델이 eval 통과 시, 사용자 전환 기간(수 개월) 후 폐기 |


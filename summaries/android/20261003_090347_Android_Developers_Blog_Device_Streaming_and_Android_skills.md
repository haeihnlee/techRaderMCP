# Android Developers Blog: Device Streaming and Android skills - available in Android CLI

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/10/android-cli-device-streaming-and-skills.html
- **요약 일시**: 2026-10-03 09:03:47

---

## 🔑 핵심 요약
- **Android CLI**에서 **Android Device Streaming**을 지원해, 에이전트가 터미널에서 원격 실기기에 접속할 수 있음
- 공식 **Android skills**(`SKILL.md`)가 **20개 이상**으로 늘어남. `developer.android.com`의 최신 가이드를 에이전트 컨텍스트에 바로 넣어 줌
- **Wear Compose Material 3 skill**(`wear/wear-compose-m3`) 소개. FotMob 사례: 오후 한나절에 리스트 8개 마이그레이션

---

## 📣 주요 발표 내용
- **Android CLI**: 특정 AI 에이전트나 도구에 묶이지 않는 커맨드라인 Android 개발 도구
  - `android-cli` skill과 함께 쓰면 에이전트가 프로젝트 생성, 빌드, 테스트, 에뮬레이터 생성·실행, 테스트 실행을 처리함
- **Android Device Streaming (CLI 지원)**
  - **ADB over SSL** 보안 연결로 원격 실기기(예: **Pixel 10 Pro**)를 USB로 꽂은 것처럼 다룸
  - 기기 할당, 빌드 배포, 로그·트레이스 수집, 헤드리스 스크린샷을 모두 터미널에서 수행
  - 사용 순서: 프로젝트 연결 → 에이전트에게 원격 기기 목록 요청 → 사용할 기기 선택
- **Android skills 주요 목록**
  - **Play 정책 감사**: manifest, 런타임 권한, target SDK, 개인정보 고지 점검
  - **Restore Credentials**: `Credential Manager`로 기기 설정·클라우드 복원 시 재인증 구현
  - **Intent 보안**: implicit intent 하이재킹 방지, broadcast receiver 보안, `PendingIntent` 검증
  - **Profiler**: 프레임 드랍 진단, CPU/메모리 트레이스 해석, 자연어 질의를 **PerfettoSQL**로 변환
  - **CameraX**: 레거시 `Camera1`/`Camera2` 코드를 lifecycle-aware CameraX로 교체
  - **Leanback → Compose for TV** 마이그레이션
  - **Media3 Cast**: `Media3` 미디어 세션과 Google Cast 수신기 간 재생 상태 동기화
  - **Play Engage SDK** 연동
  - **테스트 전략 구성**: 유닛 테스트, Compose UI 테스트 규칙, 스크린샷 테스트
  - **R8 설정 감사**
- **Wear Compose M3 skill**: 원형 화면, rotary 입력, ambient 모드, 전력 최적화, `TransformingLazyColumn`, `AppScaffold`/`ScreenScaffold` 같은 Wear 전용 패턴을 에이전트에게 알려 줌

---

## 💡 개발자 포인트
- **skill 관리 명령어**

| 작업 | 명령어 |
|---|---|
| 초기 설정 (`android-cli` skill 설치) | `android init` |
| 공식 skill 목록 보기 | `android skills list` |
| 프로젝트에 skill 설치 | `android skills add wear-compose-m3 --project=.` |
| 전체 업데이트 | `android skills update --all` |
| 개별 업데이트 | `android skills update wear-compose-m3` |

- skill은 **환경에 구애받지 않음**: Android Studio, Antigravity, **Claude**, **Codex** 등 서드파티 에이전트에서도 동작
- 실기기가 없어도 하드웨어·OS별 이슈를 **Device Streaming**으로 CI/에이전트 워크플로우에서 검증할 수 있음
- **Android TV 개발자**는 **Leanback → Compose for TV** 마이그레이션 skill을 눈여겨볼 만함
- FotMob 사례에서 skill이 모델 단독일 때의 실수를 잡아냄:
> `ScreenScaffold`의 `contentPadding`을 리스트에 넘기지 않거나, theme typography 대신 하드코딩한 `sp`를 쓰는 실수 → skill이 교정함
- FotMob 결과: 레거시 래퍼와 rotary/focus 보일러플레이트를 모두 지웠고, 에뮬레이터에서 스크롤·rotary·edge morphing·RTL 동작을 확인함
- skill에는 반드시 eval이 따라야 한다는 철학은 "Inside Android Skills - Built for deprecation" 글 참고

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|---|---|
| 게시일 | 2026-10-02 |
| Android Device Streaming (CLI) | 지금 사용 가능 |
| Android skills | 20개 이상 공개 |
| Wear Compose M3 skill | 공개됨 (`wear/wear-compose-m3`) |


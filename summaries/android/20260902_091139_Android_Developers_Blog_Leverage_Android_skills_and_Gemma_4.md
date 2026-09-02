# Android Developers Blog: Leverage Android skills and Gemma 4 in Android Studio Quail 4

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/09/leverage-gemma-4-android-studio-quail.html
- **요약 일시**: 2026-09-02 09:11:39

---

## 🔑 핵심 요약
- **Android Studio Quail 4**가 안정화 채널에 출시되어 프로덕션 개발에 사용할 수 있습니다.
- IDE에 **23개의 큐레이션된 Android skills**가 기본 탑재되어 Android API, 마이그레이션, 빌드 설정 관련 AI 지원이 강화됩니다.
- `Gemma 4` 로컬 모델을 IDE에서 직접 실행해 소스 코드를 외부로 전송하지 않고 오프라인 AI 코딩과 멀티파일 리팩터링을 수행할 수 있습니다.

---

## 📣 주요 발표 내용
- Android Studio Agent가 프롬프트 메타데이터를 분석해 관련 skills를 자동으로 탐색하고 호출합니다.
- 기본 제공 skills에는 `AGP 9 Upgrade`, `Android Profiler`, `Navigation3`, `Adaptive` 등이 포함됩니다.
- 팀별 개발 규칙과 워크플로에 맞춘 **커스텀 skills**를 직접 만들 수 있습니다.
- Android Studio 외부의 CLI AI에서도 `android skills add --all` 명령으로 Android skills를 설치할 수 있습니다.
- `Gemma 4`는 모델 선택기 또는 `Settings > Tools > AI > Model Providers > Gemma`에서 원클릭으로 다운로드·검증·업데이트할 수 있습니다.
- 경량 추론 엔진이 IDE에 포함되어 별도 서드파티 설정 없이 로컬 모델을 실행합니다.
- 클래스, 함수, 메서드, 파일 경로가 Agent 응답에서 클릭 가능한 하이퍼링크로 표시됩니다.
- `Recent Chats` 패널에서 병렬 Agent의 실행 중·입력 대기·완료 상태를 실시간으로 확인할 수 있습니다.
- 멀티스텝 작업 결과의 `Task`와 `Walkthrough`가 `Summary of Changes` 탭으로 통합됩니다.
- 추론 모델의 사고 과정은 접을 수 있는 블록으로 표시됩니다.
- API 키, Google AI Pro/Ultra, Gemini Enterprise를 통해 더 높은 모델 성능과 quota를 사용할 수 있습니다.

---

## 💡 개발자 포인트
- `Gemma 4`는 최소 **12GB RAM**에서 실행할 수 있으며, **32GB 이상**의 메모리 환경에서 가장 원활하게 동작합니다.
- 로컬 Agent의 멀티파일 리팩터링은 네트워크 연결 없이 수행되므로 민감한 소스 코드가 로컬 머신 밖으로 나가지 않습니다.
- 로컬 모델 사용 시 원격 모델의 토큰 quota 제한을 받지 않지만, 하드웨어에 따라 응답 속도와 작업 가능 범위가 달라질 수 있습니다.
- 번들 skills는 IDE 설정의 IDE-wide 토글로 전체 비활성화할 수 있습니다.
- 병렬 채팅을 사용할 때 `Recent Chats`의 파란색 배지는 백그라운드 작업이 검토 가능한 상태임을 의미하며, 빨간색 표시는 사용자 입력이 필요하다는 뜻입니다.

> **주의:** Android Studio Quail 4는 Quail 시리즈의 최종 안정화 릴리스입니다. 업그레이드 전 프로젝트의 AGP, Navigation, 디바이스 적응형 UI 설정과 알려진 이슈를 확인하세요.

---

## 📅 버전 / 출시 일정
| 항목 | 일정 / 상태 |
|---|---|
| Android Studio Quail 4 | 2026년 9월 1일 안정화 채널 출시 |
| Android skills | 23개 기본 제공 |
| `Gemma 4` 로컬 모델 | Quail 4에 네이티브 통합 |
| Gemini Enterprise 지원 | 최신 Canary 채널에서 일부 조직 대상 제공 |
| Quail 시리즈 | Quail 4가 최종 안정화 릴리스 |

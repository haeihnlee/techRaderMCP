# Android Developers Blog: Android Studio Quail 2 is Stable: Multi-task with the Android Studio AI agent

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/06/android-studio-quail-2-stable-features.html
- **요약 일시**: 2026-07-15 09:04:36

---

## 🔑 핵심 요약
- **Android Studio Quail 2**가 정식(Stable) 출시되어 프로덕션 사용 가능
- **Agent Mode**가 새 아키텍처로 재설계되어 **여러 채팅을 동시에 병렬 진행**할 수 있음
- 오픈소스 메모리 누수 탐지 도구 **LeakCanary**가 Profiler에 네이티브 통합됨
- **App Quality Insights(AQI)**가 Agent Mode와 통합되어 크래시 원인 분석부터 수정까지 자동화

---

## 📣 주요 발표 내용
- **병렬 에이전트 채팅**: `+` 아이콘으로 새 대화를 열고 `History` 아이콘으로 여러 작업 탭 간 이동 가능. UI 리팩터링, ProGuard 규칙 수정, 문서 생성 등을 동시에 진행 가능
- 채팅마다 **다른 LLM 모델**을 선택해 사용할 수 있음 (Android 개발 작업에서 LLM 성능을 비교한 **Android Bench** 참고)
- **LeakCanary 통합**: 힙 분석을 테스트 기기가 아닌 개발 PC에서 수행하여 리크 추적 속도가 최대 **5배** 빨라지고 테스트 앱은 끊김 없이 유지됨
  - 리크 탐지 시 색상으로 구분된 인터랙티브 트레이스 제공
  - `Go to declaration`으로 누수 객체의 정확한 코드 라인으로 즉시 이동
  - `Fix with Agent` 클릭 시 Gemini 에이전트가 원인을 설명하고 리스너 언바인딩, static 참조 제거 등 수정 코드를 직접 작성
- **AQI + Agent Mode 통합**: 크래시 클릭 시 요약 제공, `See more`로 소스 코드와 전체 스택 트레이스 기반 상세 분석 채팅 오픈
  - `Fix with AI` 클릭 시 수정 계획을 제안하고 승인 후 코드 변경을 직접 적용 및 검증까지 수행
- IntelliJ 플랫폼 기반 안정성·성능 개선 다수 반영

---

## 💡 개발자 포인트
> **Worktree 지원은 아직 제공되지 않음.** 동일 프로젝트 파일을 수정하는 병렬 채팅을 동시에 실행하면 에디터 충돌이 발생할 수 있으니 주의 필요

- 메모리 누수 디버깅과 크래시 분석을 에디터 밖으로 나가지 않고 처리할 수 있어 워크플로 단절이 크게 줄어듦
- 여러 작업을 병렬로 진행할 때 모델별 특성에 맞게 작업을 배분하는 것이 유용 (예: 가벼운 작업은 빠른 모델, 복잡한 리팩터링은 고성능 모델)

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| 버전 | Android Studio Quail 2 |
| 상태 | Stable (정식 출시) |
| 발표일 | 2026-07-14 |


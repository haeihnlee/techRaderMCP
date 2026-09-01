# Android Developers Blog: Emulator control for adaptive app development

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/08/emulator-adaptive.html
- **요약 일시**: 2026-09-01 09:09:42

---

## 🔑 핵심 요약
- **Android Emulator**를 터미널의 `adb emu` 명령으로 직접 제어해 적응형 앱 테스트를 빠르게 자동화할 수 있습니다.
- 폴더블 기기의 접기·펼치기, 화면 회전, 물리적 자세(posture), 리사이즈 프리셋 변경을 즉시 실행할 수 있습니다.
- 여러 에뮬레이터를 동시에 실행할 때는 `adb -s <serial> emu <command> <parameter>`로 특정 가상 디바이스를 지정할 수 있습니다.

---

## 📣 주요 발표 내용
- 폴더블 화면 상태를 전환하려면 `adb emu fold`와 `adb emu unfold`를 사용합니다.
  - `fold`: 외부의 작은 화면 구성을 표시합니다.
  - `unfold`: 내부 화면을 표시합니다.
- 방향 전환 테스트는 `adb emu rotate`로 수행하며, 기기를 시계 방향으로 90도 회전시킵니다.
- 지원되는 자세 목록과 현재 센서 상태는 `adb emu posture`로 조회합니다.
- 특정 자세는 `adb emu posture <posture_id>`로 설정합니다. 예를 들어 반쯤 열린 테이블탑 모드는 `adb emu posture 2`입니다.
- 리사이즈 에뮬레이터의 화면 크기 프리셋은 `adb emu resize-display`로 조회합니다.
- 화면 크기는 `adb emu resize-display <index>`로 변경하며, 기본 프리셋은 `0: phone`, `1: unfolded`, `2: tablet`입니다.

---

## 💡 개발자 포인트
- `adb emu` 명령은 실행 직후 셸에 제어권을 돌려주는 **fire-and-forget 방식**이므로 반복적인 수동 조작과 여러 에뮬레이터 실행을 줄일 수 있습니다.
- 폴더블·대형 화면 앱은 폼팩터별 레이아웃뿐 아니라 **상태 보존**, **구성 변경**, **상태 복원**까지 명령줄에서 반복 검증할 수 있습니다.
- 자세 ID는 가상 디바이스마다 지원 범위가 다르므로 먼저 `adb emu posture`로 목록을 확인해야 합니다.

> Pixel Fold 및 Resizable AVD 같은 표준 템플릿은 자세 `1`, `2`, `3`만 지원합니다. 지원하지 않는 자세를 지정하면 `KO: Failed to set posture` 오류가 반환됩니다.

- 여러 AVD를 대상으로 테스트 자동화할 때는 각 에뮬레이터의 serial을 명시해 잘못된 디바이스에 명령이 실행되지 않도록 해야 합니다.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|---|---|
| 게시일 | 2026년 8월 31일 |
| 대상 기능 | Android Studio Resizable Emulator 및 `adb emu` 콘솔 단축 명령 |
| 지원 테스트 | 폴더블 상태, 회전, 자세 센서, 화면 크기 프리셋 |


# Android Developers Blog: Android CLI Now Stable 1.0: Accelerate developing for Android using any agent

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/android-cli-stable-1-0-agent-development.html
- **요약 일시**: 2026-05-20 09:15:01

---

## 🔑 핵심 요약
- **Android CLI 1.0 Stable** 정식 출시 — `Gemini`, `Antigravity`, `Claude Code`, `Codex` 등 어떤 에이전트와도 함께 사용 가능
- 새로운 `android studio` 명령어로 에이전트가 **Android Studio의 정적 분석·심볼 탐색·Compose Preview** 기능을 직접 호출 가능
- `apt-get`, `winget`, `homebrew` 지원 및 **Android Skills 라이브러리 대폭 확장** (XR, CameraX, Perfetto SQL 등)

---

## 📣 주요 발표 내용

### 1. Google Antigravity 통합
- `Google Antigravity 2.0`에 **Android 리소스 번들**(CLI + skills) 옵션 추가
- 설치 시 온보딩 또는 `Settings > Customizations > Build With Google Plugins`에서 활성화

### 2. `android studio` 명령어 신설 (핵심)
Android Studio Quail **preview 버전**과 연결되어 에이전트가 IDE의 깊은 컨텍스트 기능을 활용:

| 명령어 | 기능 |
|---|---|
| `analyze-file` | 에디터 내장 inspection으로 파일의 오류·경고 분석 |
| `find-declaration` | 심볼(클래스/메서드/리소스)의 정의 위치를 시맨틱 분석으로 탐색 |
| `find-usages` | 프로젝트 전체에서 심볼의 모든 참조·선언 탐색 |
| `render-compose-preview` | Jetpack Compose Preview를 이미지·UI 계층으로 렌더링 |
| `version-lookup` | Google Maven 등에서 라이브러리 최신 버전 조회 |
| `open-file` | Android Studio에서 파일 바로 열기 |

연결 상태 확인: `android studio check`

### 3. 설치 채널 확대
- `winget install -e --id Google.AndroidCLI` (Windows)
- `apt-get`, `homebrew` 추가 지원
- **user-local 디렉터리**에 기본 설치 (권한 이슈 완화)

### 4. Journeys 지원
- **자연어로 작성된 사용자 시나리오**를 에이전트가 실제 앱 위에서 실행
- 테스트·검증·데이터 수집에 활용 가능

### 5. 새로운 Android Skills
- **Display Glasses + Jetpack Compose Glimmer (XR)**
- **Migration to CameraX** (Camera1/Camera2 → CameraX 마이그레이션)
- **Perfetto SQL** (자연어 → 트레이스 쿼리 변환)
- **Adaptive UI** / **Testing setup** / **Styles API** / **AppFunctions**

---

## 💡 개발자 포인트

> **Android Studio Quail preview 버전**이 있어야 `android studio` 명령어가 작동합니다. 안정 채널 Android Studio는 아직 미지원.

- 기존 사용자는 `android update` 한 번이면 신기능 사용 가능
- 에이전트가 IDE 기능을 쓰려면 반드시 `android init`으로 **skill을 최신화**해야 함
- skill 탐색·설치 워크플로:
  ```bash
  android init
  android skills list
  android skills add --skill=<skill-name>
  ```
- `find-declaration` + `analyze-file` + `open-file` 조합으로 **에이전트가 코드 수정 후 IDE에서 Compose Preview를 시각적으로 검토**하는 흐름이 권장됨
- CLI 단독 사용 시에도 정적 분석·의존성 관리가 가능해져 **CI나 헤드리스 환경**에서도 활용도 증가

---

## 📅 버전 / 출시 일정

| 항목 | 정보 |
|---|---|
| Android CLI | **Stable 1.0** (2026-05-19 발표) |
| Android Studio | **Quail preview** 필요 (안정판 미지원) |
| 발표 행사 | **Google I/O '26** |
| 다운로드 | `d.android.com/tools/agents` |


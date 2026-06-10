# Android Developers Blog: Top 3 updates for Android developer productivity

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/06/android-developer-productivity-updates.html
- **요약 일시**: 2026-06-10 09:06:02

---

## 🔑 핵심 요약
- **Android CLI**가 마침내 **1.0 정식(stable) 버전**으로 출시 — `studio` 명령으로 Android Studio와 직접 연동
- **Android skills** 저장소가 17개 이상으로 확장 — LLM에 도메인 특화 워크플로우 지식 제공
- **Google Antigravity**가 Android 개발 공식 지원 (Android resources bundle 추가)
- **Android Bench** 리더보드에 오픈 모델(`Gemma 4`)과 최신 모델(`Gemini 3.5 Flash`) 추가

---

## 📣 주요 발표 내용

**1. Android CLI 1.0 정식 출시**
- `studio` 명령으로 에이전트가 **Android Studio와 직접 연동(bridging)** 가능
- 프로그래밍 방식 버전 조회, **Journeys** 지원 등 신규 기능 추가
- 에이전트 실행 중에도 **성능 프로파일러, Compose Preview, Android Device Streaming** 등 Studio 전용 도구 활용
- `npm`, `homebrew` 등 더 많은 패키지 매니저로 설치 가능

**2. Android skills 확장 (17개+)**
- LLM을 **특화 워크플로우·도메인 지식**에 그라운딩하여 복잡한 작업 정확도 향상
- 신규 스킬 영역: **Adaptive UI**, XR용 `Jetpack Compose Glimmer`, **CameraX 마이그레이션**, `Perfetto SQL` 트레이스 분석, `Jetpack Compose Styles API`, **AppFunctions**, Credential Manager 이메일 검증, **Engage SDK**, 테스트 셋업, Wear OS Material3 등

**3. Android Bench 모델 확대**
- 실제 Android 개발 과제로 **LLM 성능을 평가**하는 리더보드
- 요청에 따라 **오픈 모델 평가** 추가 (로컬 모델 `Gemma 4` 포함)
- 최신 모델 `Gemini 3.5 Flash` 추가, 장기 실행(long running) 난이도 과제도 곧 추가 예정

**4. Google Antigravity 지원**
- **Android resources bundle**(Android CLI + skills 포함) 제공
- 온보딩 시 또는 `Settings > Customizations > Build With Google Plugins` 메뉴에서 설치

---

## 💡 개발자 포인트

> **Android CLI가 1.0 stable로 격상** — 이제 프로덕션 워크플로우에 안정적으로 도입 가능하며, 에이전트 기반 개발이 본격화됩니다.

- 스킬 설치/조회는 CLI 명령으로 간단히 처리:
  - 목록 조회: `android skills list`
  - 추가: `android skills add --skill=<skill-name>`
- 에이전트 + Android CLI + **Android Studio 동시 실행** 조합이 권장 워크플로우 — 프로파일러·Compose Preview 등 GUI 전용 기능을 에이전트가 활용 가능
- Antigravity, Android CLI, Android Studio 어디서 개발하든 **동일한 AI 도구·지식** 활용 가능

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| Android CLI | **v1.0 정식(stable)** 출시 |
| Android skills | **17개+** 제공 중 |
| Android Bench 신규 모델 | `Gemma 4`, `Gemini 3.5 Flash` |
| 발표일 | 2026년 6월 9일 (Google I/O) |
| 장기 실행 과제 | Android Bench에 **곧 추가 예정** |

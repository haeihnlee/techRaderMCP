# Android Developers Blog: Bringing our latest frontier model to Android Developers

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/10/bringing-gemini-4-argon-to-android-agentic-engineering-antigravity-cli.html
- **요약 일시**: 2026-10-14 09:08:55

---

## 🔑 핵심 요약
- Google의 최신 프론티어 모델 **Gemini 4 Argon**을 오늘부터 Android 개발 환경 전반에서 사용 가능
- **Google Antigravity**(standalone·Android Studio Canary), **Android Studio**(Gemini API 유료 티어), **Google AI Studio**, **Firebase AI Logic**에서 제공
- 공식 `android-cli-plugin` 으로 에이전트를 로컬 Android 도구(Gradle·빌드 툴)에 연결해 **엔드투엔드 에이전틱 개발** 지원

---

## 📣 주요 발표 내용
- **Gemini 4 Argon**: 코딩·금융·법률·보안·과학 등 복잡한 실제 작업의 **장기(long-horizon) 자율 실행**과 다단계 작업 계획 능력 강화
- **Self-Healing Build Loops**: 로컬 빌드 실패 시 Antigravity 실행 하네스가 **Gradle daemon** 에러 스트림과 **Kotlin 컴파일러 로그**를 직접 수집 → 모델이 근본 원인을 반복 진단해 수정안 도출
- 연속 편집 라운드 동안 **일관된 가설 유지**, 내부 **AST(Abstract Syntax Tree) 인식**으로 보다 정확한 편집
- **Jetpack Compose UI 생성**: 바로 프로덕션에 쓸 수 있는 수준의 Compose 코드 생성
- **AGSL 셰이더**: `Modifier.graphicsLayer` 블록과 shader brush에 복잡한 **AGSL** 코드를 직접 작성 (frosted glass, 동적 조명, ripple 효과 등) — **120 FPS** Compose 애니메이션과 함께 동작하는 경량 GPU 셰이더
- **Android CLI 플러그인**: Antigravity 데스크톱 앱·IDE 확장·CLI 어디서든 에이전트가 로컬 Android 도구를 프로그래밍 방식으로 실행하고 커스텀 developer skill 수행

---

## 💡 개발자 포인트
- **Antigravity Desktop 설정**: Settings > Customizations > Build With Google Plugins (또는 Antigravity Plugin Marketplace)에서 `android-cli-plugin` 을 Enabled로 전환
- **Android Studio Canary 설정**: agent tool window에서 Antigravity 계정으로 로그인하면 에디터 옆에서 바로 에이전틱 워크플로 사용
- **터미널 설정 (Antigravity)**: `agy plugin install android-cli-plugin`
- **터미널 설정 (그 외 터미널 에이전트)**: `android init`
- **Firebase AI Logic**으로 모바일·웹 앱에서 Gemini 4 Argon을 **클라이언트 사이드**에서 호출 가능 (Gemini API 유료 티어)
- Google AI Studio의 **Playground** 및 **Build**에서도 사용 가능

> **주의**: Antigravity 경로는 **Google AI Ultra 구독**이 필요하며, Android Studio·AI Studio·Firebase AI Logic의 API 경로는 **Gemini API 유료 티어**가 필요합니다. 지원 지역에서만 순차 롤아웃됩니다.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 발표일 | 2026-10-13 |
| Gemini 4 Argon 출시 | 2026-10-13부터 지원 지역에 글로벌 롤아웃 |
| Antigravity 데스크톱 지원 OS | macOS, Windows, Linux |
| Android Studio 통합 | 최신 **Android Studio Canary** (Antigravity 로그인) |
| Gemini API 소개 가격 | 2026-11-30까지 |
| 접근 요건 | Google AI Ultra 구독 또는 Gemini API 유료 티어 |

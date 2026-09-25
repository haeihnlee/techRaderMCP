# Build your way: Use any AI agent of your choice in Android Studio

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/09/build-your-way-use-any-ai-agent-in-android-studio.html
- **요약 일시**: 2026-09-25 09:08:10

---

## 🔑 핵심 요약
- Android Studio에 **BYOA(Bring Your Own Agent)** 기능 도입 — Claude Agent, Codex, Google Antigravity 등 원하는 AI 에이전트를 Android Studio에 직접 연동 가능
- `ACP(Agent Client Protocol)` 기반으로 프로젝트 그래프·빌드 설정·플랫폼 정보를 에이전트에 직접 주입하여 토큰 효율과 응답 정확도 향상
- **Android Studio Rabbit 2** Canary 채널부터 프리뷰로 제공 시작

---

## 📣 주요 발표 내용
- **BYOA 기능** 출시: Claude Agent(Anthropic), Codex(OpenAI), Antigravity(Google) 등 ACP 호환 에이전트를 IDE에서 직접 사용
- **Native Tool Injection**: 빌드 진단, `Jetpack Compose Preview`, Android SDK 도구, 에뮬레이터 제어를 에이전트가 직접 실행
- **서브에이전트 위임**: 코드 리뷰·테스트 등 세부 작업을 전문 서브에이전트에게 분리 실행 가능
- **세분화된 권한 제어**: 일반 작업은 에이전트 자율 실행, 위험 작업은 사용자 승인 대기
- **Gemini 사용자**: 최신 `Gemini Flash 3.8` 등 최신 모델과 더 높은 AI 쿼터를 위해 **Google Antigravity 에이전트** 사용 권장
  - Google AI Pro/Ultra 플랜 또는 Gemini API 키로 로그인 지원
  - Gemini Enterprise 사용 조직은 기존 보안·프라이버시 혜택 유지

---

## 💡 개발자 포인트
- 에이전트가 파일 읽기/쓰기, 쉘 명령 실행, 테스트 실행, 웹 검색까지 **IDE 환경 내에서 직접 수행**
- **Android Knowledge Base**와 Android Skills가 에이전트에 자동 제공되어 최신 Android 모범 사례 반영
- 쿼터 소진이나 성능 저하 시 다른 에이전트로 **즉시 전환** 가능 (플로우 연속성 유지)
- 장기 세션 유지 및 프로젝트 슬래시 커맨드·메모리 자동 로드 지원

> BYOA는 현재 **Canary 채널 프리뷰** 단계이므로, 버그 발견 시 공식 이슈 트래커에 리포트 권장

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| 출시 채널 | Android Studio Canary (Rabbit 2) |
| 프리뷰 시작 | 2026년 9월 24일 |
| 지원 에이전트 | Claude Agent, Codex, Google Antigravity |
| 추가 에이전트 등록 | Settings > Tools > AI > Agents 에서 조회 가능 |

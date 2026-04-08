# Android Developers Blog: Increase Guidance and Control over Agent Mode with Android Studio Panda 3

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/04/Increase-Guidance-and-Control-over-Agent-Mode-with-Android-Studio-Panda-3.html
- **요약 일시**: 2026-04-08 16:25:31

---

## 핵심 요약 (3줄)
- Android Studio Panda 3가 안정(Stable) 버전으로 출시되어 AI 에이전트 모드에 대한 세밀한 제어와 커스터마이징 기능이 강화됨
- **Agent Skills** 기능으로 프로젝트별 맞춤 AI 지시사항을 정의하고, **Agent 권한 관리**로 AI가 수행할 수 있는 작업 범위를 세밀하게 통제 가능
- 자동차 앱 개발을 위한 **Empty Car App Library App** 템플릿이 추가되어 Android Auto/Automotive OS 앱 개발이 간소화됨

---

## 주요 발표 내용

### 🤖 Agent Skills (에이전트 스킬)
- `.skills` 디렉토리 내 `SKILL.md` 파일로 팀/프로젝트 맞춤형 AI 작업 지침 정의 가능
- 에이전트가 자동으로 스킬을 감지·적용하거나, `@스킬명` 입력으로 수동 트리거 가능
- 코드 리뷰 기준, 사내 라이브러리 사용법 등 조직 특화 워크플로우 지식을 AI에 주입 가능
- Gemini 및 **서드파티 원격 LLM**과도 호환

### 🔐 Agent 권한 관리 (Granular Agent Permissions)
- 파일 읽기, 셸 명령 실행, 웹 접근 등 작업별 권한을 명시적으로 요청·승인
- **"Always Allow" 규칙** 설정으로 반복 승인 피로도 감소
- 한 번 승인한 명령은 이후 자동 실행되어 작업 흐름 유지
- SSH 키 등 민감 파일 접근은 항상 명시적 승인 필요
- **옵션형 샌드박스** 모드로 에이전트를 완전히 격리된 환경에서 실행 가능

### 🚗 Empty Car App Library App 템플릿
- Android Auto 및 Android Automotive OS를 동시 지원하는 드라이빙 최적화 앱 보일러플레이트 자동 생성
- `New Project > Empty Car App Library App` 선택만으로 바로 개발 시작 가능

---

## 개발자에게 중요한 포인트

- **팀 단위 AI 표준화 가능**: `SKILL.md`를 Git으로 공유하면 팀 전체가 동일한 AI 작업 방식을 사용할 수 있어, 코딩 컨벤션·라이브러리 사용법 등을 AI에 일관되게 적용 가능
- **보안 민감 프로젝트에 유리**: 에이전트가 접근 가능한 파일/명령을 세밀하게 제한할 수 있어 기업 환경에서도 안전하게 Agent Mode 활용 가능
- **샌드박스 활용 권장**: 실험적이거나 검증되지 않은 AI 작업 수행 시 샌드박스 모드로 격리 실행하여 의도치 않은 코드베이스 변경 방지
- **차량용 앱 진입 장벽 완화**: 기존에는 복잡한 설정이 필요했던 카 앱 프로젝트를 템플릿으로 즉시 시작 가능
- **Panda 2 기능과 연속성**: 이전 Panda 2의 AI 기반 New Project Flow, Version Upgrade Assistant와 함께 사용하면 전체 개발 사이클을 AI로 보조 가능

---

## 출시 일정 / 버전 정보

| 항목 | 내용 |
|------|------|
| 버전명 | Android Studio Panda 3 |
| 채널 | **Stable (안정 버전)** |
| 출시일 | 2026년 4월 2일 |
| 이전 버전 | Android Studio Panda 2 (2026년 3월) |
| 다운로드 | [Android Studio 공식 다운로드 페이지](https://developer.android.com/studio) |

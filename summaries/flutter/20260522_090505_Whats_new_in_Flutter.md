# What's new in Flutter

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=I1uIbGh1dGE
- **요약 일시**: 2026-05-22 09:05:05

---

## 🔑 핵심 요약
- **Flutter 3.44**와 **Dart 3.12** 정식 출시 — 월 활성 개발자 **150만 명**, 컨트리뷰터 1,700명 돌파
- **AI 에이전트 워크플로우** 지원 대폭 강화: `MCP 서버` + 새로운 **Hot Reload 자동 연동** + **Dart/Flutter Agent Skills** 공개
- **Generative UI(GenUI)** 패러다임 본격화 — Flutter SDK 기반 `A2UI 프로토콜` 패키지 다운로드 연초 대비 **500% 증가**

---

## 📣 주요 발표 내용

### 🎯 Dart 3.12 신규 언어 기능
- **명명 생성자 파라미터로 private 인스턴스 필드 초기화** 간소화 — 컴파일러가 initializer list를 자동 생성
- **Primary Constructor** 실험적 지원 — 클래스 헤더에서 직접 인스턴스 변수 선언 가능
- **Dart on Cloud Functions for Firebase** 정식 출시 — HTTP/Callable 함수를 순수 Dart로 작성, `AOT` 컴파일로 **콜드 스타트 10ms** 수준
- **Dart Admin SDK**로 서버 측에서 Firebase 서비스 접근 가능

### 🛠️ 개발자 경험 개선
- `dart format` 거의 즉시 실행, `dart analyze` **약 50% 빨라짐** (AOT 스냅샷 적용)
- **커스텀 Analyzer 플러그인** 지원 — 팀별 진단·Quick Fix 확장 가능
- `pub cache gc` 명령어 추가 — 미사용 패키지 자동 정리
- **Widget Previews** + Flutter Inspector 풀 지원 — 화면 크기·테마·텍스트 스케일 매트릭스로 위젯 격리 테스트

### 🤖 AI 에이전트 통합
- **Dart/Flutter MCP 서버**에 **Hot Reload 기능** 추가 — 에이전트가 코드 변경 후 자동으로 실행 중인 앱에 연결·리로드
- **Dart/Flutter Agent Skills** 공개 — Progressive Disclosure 방식으로 토큰 절약
- **Firebase Agent Skills for Flutter** 신규 출시
- **Genkit Dart** 프리뷰 — Google/Anthropic/OpenAI 등 멀티 모델 프로바이더 지원, 타입 안전 구조화 출력·Tool Calling·관찰가능성 내장

### 📱 On-device AI
- **Flutter Gemma 패키지**에 **LiteRT-LM** 풀 지원 임박 — Android/iOS/Web/Windows/Linux/macOS 등 **6개 Stable 플랫폼** 전체에서 GPU·NPU 가속
- **Firebase AI Logic** — 서버 측 프롬프트 템플릿 지원 (앱에 프롬프트 임베드 불필요)
- Gemma 3 Impact Challenge 우승작: **Gemma Vision** (시각 장애 보조), **Vetiver** (인지 장애 일상 보조) 모두 Flutter로 제작

### 🎨 Generative UI
- **A2UI 프로토콜** — Google이 정의한 에이전트-클라이언트 간 UI 협업 오픈소스 프로토콜
- Flutter A2UI SDK가 동적 GenUI 경험의 기반 제공

---

## 💡 개발자 포인트

> **Build Hooks**가 정식 출시되어 CocoaPods/CMake/Gradle 같은 플랫폼별 빌드 파일을 유지할 필요 없이 Dart 패키지 내에서 네이티브 코드 컴파일·번들링이 가능합니다.

- **풀스택 Dart 시대 도래**: Cloud Functions가 Dart를 지원하므로 클라이언트·서버 코드를 단일 언어로 작성 가능. `AOT` 덕분에 서버리스 콜드 스타트 부담 최소화
- **AI 워크플로우 표준화**: MCP 서버 + Agent Skills 조합으로 코딩 에이전트가 Flutter best practice 기반으로 코드 생성. **수동 빌드/실행 단계 제거** (Hot Reload 자동 연동)
- **On-device LLM 전략**: 비용·네트워크 제약 환경이라면 **Flutter Gemma + LiteRT-LM** 조합으로 6개 플랫폼 일관된 추론 환경 확보
- **UX 패러다임 전환**: 텍스트 응답 일변도의 AI UX에서 벗어나, `A2UI` 기반 동적 UI 생성으로 차별화 가능
- 새 Dart 문법(shorthands, primary constructors)은 보일러플레이트를 크게 줄이나 일부는 **실험적 단계**이므로 프로덕션 적용 시 검토 필요

---

## 📅 버전 / 출시 일정

| 항목 | 버전 / 상태 |
|---|---|
| Flutter | **3.44** (Stable) |
| Dart | **3.12** (Stable) |
| Dart on Cloud Functions | 정식 출시 |
| Firebase AI Logic 서버 프롬프트 템플릿 | 정식 출시 |
| Firebase Agent Skills for Flutter | 신규 출시 |
| Genkit Dart | **Preview** |
| Primary Constructors | **Experimental** |
| Flutter Gemma + LiteRT-LM 풀 지원 | Coming Soon |

### 📊 생태계 지표
| 지표 | 수치 |
|---|---|
| 월 활성 Flutter 개발자 | 150만 명 |
| 컨트리뷰터 수 | 1,700명 |
| 최근 1년 변경사항 | 1,800+ |
| pub.dev 30일 다운로드 | **13억+** |
| A2UI 패키지 다운로드 증가율 (YTD) | **+500%** |


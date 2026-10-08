# Write and deploy full stack Dart apps with Flutter and Cloud Functions for Firebase

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=CcyX-pqjDp0
- **요약 일시**: 2026-10-08 09:03:49

---

## 🔑 핵심 요약
- **FlutterCon(올랜도)** 현장 인터뷰: Flutter 팀 Andrew와 **Firebase DevRel 리드 Arthur Thompson**의 대담
- **Firebase 프로젝트 = Google Cloud 프로젝트** → 확장성 걱정 없이 시작, 필요 시 `BigQuery`·`Cloud Logging` 등 GCP 제품을 바로 연결
- **Firebase AI Logic**: 서버 측 프롬프트 템플릿 + **App Check 재전송 방지(replay protection)** 로 모델 엔드포인트를 안전하게 보호
- 개발 워크플로용 **Firebase Agent Skills / MCP 서버**가 웹 중심에서 **모바일·Flutter 환경까지 확장**

---

## 📣 주요 발표 내용
- **Firebase의 두 가지 역할**
  - 에이전트가 개발자와 함께 앱을 빌드하도록 지원 (**Agent Skills**, **MCP 서버**)
  - 수백만 사용자 규모까지 확장 가능한 **인프라** 제공
- **Next / I/O 주요 출시**: **Genkit**, **SQL Connect**
- **2026 방향성**: 에이전트 기반 개발 환경과의 통합 지점 확대
  - **AI Studio**의 Firebase 에이전트
  - **Android Studio**
  - **Antigravity**
- **Firebase AI Logic** 보안 기능
  - **서버 측 프롬프트 템플릿**: 프롬프트를 클라이언트에 두지 않음 → 프롬프트 인젝션 위험 감소
  - 앱 재배포 없이 서버에서 프롬프트 수정 가능
  - **App Check** 통합: 합법적인 앱만 모델 엔드포인트 호출 가능
  - **Replay protection**: 토큰 1회 사용 강제 → 토큰 탈취·재사용·할당량 남용 차단
- **Firebase Skills 확장**: 모바일/Flutter 환경에서 설치 시 해당 환경에 최적화된 가이드를 에이전트에 제공

---

## 💡 개발자 포인트
- Firebase는 "작게 시작하고 나중에 갈아타는" 플랫폼이 아님 — GCP 위에서 그대로 성장 가능
- 앱 내 AI 기능 추가 시 체크리스트
  - 프롬프트는 **서버 측 템플릿**으로 관리
  - **App Check** + **replay protection** 활성화로 엔드포인트 남용 방지

> ⚠️ 클라이언트에 프롬프트를 하드코딩하면 프롬프트 인젝션·엔드포인트 남용 위험이 커집니다. AI 기능은 "올바르게 구현하지 않으면 위험"하다는 점이 강조되었습니다.

- **Skills / MCP는 이식성이 높음**: AI Studio·Antigravity 같은 Google 도구뿐 아니라 서드파티 에이전트 빌더·다른 모델/에디터에서도 동작
- Firebase 입문 추천: **Authentication(인증)** 부터 시작
  - 거의 모든 앱에 필요하지만 실수하기 쉬운 영역
  - 로그인 화면·사용자 정보 처리를 빠르게 끝내고 앱 핵심 기능에 집중 가능
- 주목할 트렌드: **Firebase AI Logic**을 생성형 UI 계열 기술과 결합해 Flutter 앱에서 새로운 사용자 경험 제공

> ℹ️ 영상 제목은 "Full stack Dart apps with Cloud Functions for Firebase"이지만, 실제 내용은 Firebase 전반·AI 기능에 관한 인터뷰입니다.

---

## 📅 버전 / 출시 일정
| 항목 | 시점 / 내용 |
|------|-------------|
| **Genkit**, **SQL Connect** | Google Cloud Next / Google I/O에서 출시 |
| Firebase 에이전트 통합 확대 | 2026년 로드맵 (AI Studio, Android Studio, Antigravity) |
| Firebase Skills 모바일/Flutter 지원 | 최근 확장 (구체적 날짜 언급 없음) |


# Catching up | Observable Flutter #90

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=16TV1WXI5WU
- **요약 일시**: 2026-06-06 09:03:50

---

## 🔑 핵심 요약
- **Google Cloud Next 2026** 및 **Google I/O 2026** 발표 이후 Dart/Flutter 생태계 변화를 진행자(Craig Labens)가 정리하는 캐주얼 라이브 방송
- 올해 생태계 테마는 **"Flutter everywhere, everyday, built by everyone, for everyone"** — `full-stack Dart`, `AI agentic UI`, `모듈형 프레임워크 아키텍처` 세 축으로 정리
- **Firebase Cloud Functions의 Dart 지원**(experimental), **Gen UI**, **Material/Cupertino 프레임워크 분리**가 가장 주목받는 변화

---

## 📣 주요 발표 내용
- **Full-stack Dart**: `Firebase Functions`를 **Dart로 작성**하는 기능이 experimental로 도입 — 수년간 커뮤니티가 기다려온 기능
- **AI Agentic UI (Gen UI)**: `Gemini`(또는 선택한 LLM)가 개발자가 허용한 **위젯 카탈로그**를 기반으로 UI를 **온디맨드로 조립**하는 방식
  - 비즈니스 로직이 내장된 **고수준 위젯**을 카탈로그로 제공하는 방식이 더 권장됨
- **모듈형 프레임워크 아키텍처**: `Material`과 `Cupertino`를 프레임워크 본체에서 **분리(decoupling)** — 진행자가 "오랜만에 본 최고의 제안"이라고 평가
- **Firebase Data Connect**: `Postgres` 기반 관계형 데이터 지원 진전 (진행자도 최신 동향 확인 필요하다고 언급)
- **Dart 언어**: `primary constructors` 신규 문법 도입 (Kotlin 등 타 언어에서 차용한 패턴)

---

## 💡 개발자 포인트
- **Firebase Functions를 Dart로 전환** 시 타입 안정성 이점이 있으나, 기존 Node 코드 대비 **재검증 비용**은 여전히 존재 (데모 프로젝트도 시간 부족으로 Node 유지)
- `primary constructors`는 **매우 작은 클래스**에 적합 — 파라미터가 2개를 넘어가면 가독성 측면에서 호불호가 갈릴 수 있음 (진행자는 사용 보류 입장)
- **위젯 분리(widget splitting)**가 Flutter에서 가장 유용한 패턴으로 재차 강조됨

> ⚠️ **Flutter Web의 `Ctrl+F`(브라우저 네이티브 찾기)는 구조적으로 어려운 문제**
> Flutter Web은 DOM이 아닌 **canvas로 렌더링**하므로, 브라우저 기본 검색과 연결하려면 semantics 트리 + 텍스트 geometry를 동기화해야 함.
> 진행자는 브라우저 네이티브 대신 **앱 자체에 Flutter 기반 커스텀 Ctrl+F 위젯**을 구현하는 방향을 제안 (`SelectableText`도 동일 메커니즘 관련)

---

## 📅 버전 / 출시 일정

| 항목 | 상태 |
|------|------|
| Firebase Functions (Dart 작성) | experimental (실험 기능) |
| Firebase Data Connect (Postgres) | 진행 중 / 동향 확인 필요 |
| Gen UI (AI Agentic UI) | 신규 발표 |
| Material/Cupertino 프레임워크 분리 | 발표됨 |
| Dart `primary constructors` | 언어 기능 도입 |

> 정확한 GA 버전·날짜는 본 영상에서 명시되지 않음 (Google Cloud Next 2026 / I/O 2026 발표 기반 논의)


# Primary constructors and private named parameters

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=tFVFB-mel0w
- **요약 일시**: 2026-09-18 09:03:40

---

## 🔑 핵심 요약
- **Dart 3.12**부터 `private named parameters` 지원 — `_` 로 시작하는 named 파라미터를 생성자에서 직접 사용 가능
- `primary constructors` 도입으로 클래스 선언 시 반복되는 필드/생성자 보일러플레이트 대폭 축소
- 두 기능 모두 **기존 문법과 완전 호환** — 선택적으로 적용 가능

---

## 📣 주요 발표 내용

### Private Named Parameters (Dart 3.12+)
- 기존에는 `_`(언더스코어)로 시작하는 필드는 외부 파일에서 named 파라미터로 접근 불가
- Dart의 privacy 모델: `_`로 시작하는 모든 멤버는 **같은 파일 내에서만** 접근 가능
- 이전에는 별도의 중간 변수를 두는 우회 코드가 필요했음
- Dart 3.12부터 `_field` 형태의 named 파라미터를 생성자에서 직접 선언 가능

### Primary Constructors
- 클래스 선언부의 `()`에 생성자 파라미터를 바로 작성하는 새 문법
- `var` 또는 `final` 키워드를 붙이면 **자동으로 필드와 바인딩**
- 기존 필드 선언과 생성자 선언 중복 제거 가능
- factory 생성자에서 중복 클래스명 생략 가능
- 인스턴스 변수도 primary constructor의 파라미터를 직접 참조하여 초기화 가능

---

## 💡 개발자 포인트

> **기존 문법은 항상 유효** — primary constructor 도입이 기존 코드를 deprecated 하지 않음

- `final` vs `var` 선택에 따라 불변/가변 필드 결정
- 간단한 **data class**나 **DTO** 구현 시 primary constructor 도입 권장
- IDE의 **quick fix**로 기존 클래스를 새 문법으로 빠르게 변환 가능
- AI 에이전트를 사용 중이라면 **Flutter 공식 skills** 설치 권장 — primary constructor 문법을 학습한 문서 포함
- 팀 컨벤션에 따라 파라미터 수 기준으로 적용 범위 결정 가능

---

## 📅 버전 / 출시 일정

| 기능 | 최소 Dart 버전 |
|------|-------------|
| Private named parameters | Dart **3.12** |
| Primary constructors | Dart **3.12** |


# Holafly: Calling native APIs from Flutter

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=eqow9BS2su8
- **요약 일시**: 2026-09-15 09:03:39

---

## 🔑 핵심 요약
- **Flutter**에서 플랫폼별 네이티브 API(eSIM 관리 등)를 호출하는 방법을 다룸
- `pigeon` 패키지를 사용해 iOS(Swift)·Android(Kotlin) 바인딩을 자동 생성
- 각 플랫폼 구현을 독립적인 패키지로 캡슐화하고 단일 **Dart API**로 노출

---

## 📣 주요 발표 내용
- eSIM 관리 모델처럼 OS마다 전용 API가 있어 Flutter 추상화가 없는 경우, 네이티브 코드 직접 작성이 필요
- **플랫폼별 독립 패키지** 구조: iOS/Android 구현을 별도 패키지로 분리
- `pigeon`으로 iOS·Android가 **동일한 인터페이스**를 Dart에서 사용할 수 있도록 바인딩 생성
- 네이티브 컴포넌트를 **standalone package**로 캡슐화 후, 메인 앱에 공개 인터페이스로 노출

---

## 💡 개발자 포인트
- Flutter 기본 추상화가 없는 네이티브 기능(예: eSIM API)은 직접 Kotlin/Swift 코드 작성 필요
- `pigeon` 사용 시 플랫폼 채널 보일러플레이트를 줄이고 타입 안전한 Dart↔네이티브 통신 가능

> **패키지 분리 전략**: 각 네이티브 기능을 독립 패키지로 분리하면 재사용성과 테스트 용이성이 높아짐

---

## 📅 버전 / 출시 일정
해당 없음

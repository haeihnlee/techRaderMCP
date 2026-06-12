# ChangeNotifier (Technique of the Week)

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=iBRrnCqzTuk
- **요약 일시**: 2026-06-12 09:03:46

---

## 🔑 핵심 요약
- **상태 관리**의 핵심 문제: 데이터 변경 시 앱 전체를 리빌드하지 않고 **특정 위젯만** 갱신하는 방법
- `ChangeNotifier`는 구독 중인 위젯에게 리빌드 시점을 알려주는 클래스
- UI 측에서는 `ListenableBuilder`로 구독하여 `notifyListeners()` 호출 시 해당 위젯만 리빌드

---

## 📣 주요 발표 내용
- 카운터 값이 화면 여러 곳에 표시되는 예시로, 한 데이터 변경이 **여러 위젯 동기화**를 요구하는 상황을 설명
- 해결책: `ChangeNotifier`를 **상속(extends)** 한 모델 클래스 작성
  - 변경되는 상태를 노출하는 **프로퍼티** 정의
  - 상태를 갱신하는 **메서드** 정의
  - 메서드 내에서 상태 변경 후 `notifyListeners()` 호출 → 구독 위젯 리빌드 신호
- UI에서는 `ListenableBuilder` 사용
  - `listenable`(예: 카운터 모델)과 `builder` 함수를 전달
  - `notifyListeners()` 호출 시 구독 중인 각 `ListenableBuilder`가 builder를 재실행하여 UI가 항상 동기화됨

---

## 💡 개발자 포인트
- 외부 패키지 없이 **Flutter 기본 제공 API**만으로 가벼운 상태 관리 구현 가능 — 간단한 앱이나 국소적 상태 공유에 적합
- 패턴 정리: 모델은 `ChangeNotifier` 상속 → 상태 변경 메서드에서 `notifyListeners()` → UI는 `ListenableBuilder`로 구독

> `notifyListeners()`는 반드시 **상태를 변경한 후**에 호출해야 합니다. 호출을 빠뜨리면 구독 위젯이 리빌드되지 않아 UI와 데이터가 어긋납니다.

- 추가 학습: `ChangeNotifier` 및 기타 Flutter 기법은 **flutter.dev** 공식 문서 참고

---

## 📅 버전 / 출시 일정
해당 없음

# Guard Clauses (Technique of the Week)

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=4sxrFXhMxy4
- **요약 일시**: 2026-10-07 09:03:40

---

## 🔑 핵심 요약
- **Dart 패턴 매칭**에 **가드 절(Guard clause)**을 붙이면 `case` 안에서 임의의 불리언 조건을 검사할 수 있음
- 문법은 패턴 뒤에 `when <불리언 표현식>`을 붙이는 형태
- 가드가 `false`면 switch를 빠져나가지 않고 **다음 `case`로 넘어감** — 중첩 `if` 없이 선언적인 분기 가능

---

## 📣 주요 발표 내용
- 예제: `Shape` 클래스와 하위 타입 `Circle`, `Rectangle`의 이름을 출력하는 함수
- 데이터 구조 기반 매칭만으로는 **정사각형(Square)**처럼 "조건을 만족하는 `Rectangle`"을 구분하기 어려움
- `case` 본문에 중첩 `if`를 쓰는 방식은 가독성이 떨어지고, 도형 종류가 늘수록 더 복잡해짐
- 해결책: `case Rectangle(:final width, :final height) when width == height:` 처럼 **`when` 가드**로 조건 추가
- 동작 순서
  - 패턴 매칭 성공 → 가드 표현식 평가
  - `true` → 해당 `case` 본문 실행
  - `false` → 다음 `case` 평가로 진행
- 가드 절 사용 가능 위치: **`switch` 문**, **`switch` 표현식**, **`if-case` 문**

---

## 💡 개발자 포인트
- 새 하위 클래스(`Square`)를 만들지 않고도 **기존 타입 + 조건**으로 세분화된 분기 가능
- 더 구체적인 가드 `case`(예: 정사각형)를 일반 `case`(직사각형)보다 **앞에** 배치해야 의도대로 매칭됨
- `if (shape case Rectangle(:var width, :var height) when width == height)` 형태로 단일 조건 분기에도 활용 가능
> 가드가 `false`일 때 switch가 종료되는 것이 아니라 **다음 case로 fall-through 평가**된다는 점에 유의 — 뒤에 일반 패턴 case를 두어 나머지 경우를 처리할 것
- 자세한 내용은 **dart.dev** 패턴 문서 참고

---

## 📅 버전 / 출시 일정
해당 없음 (가드 절은 Dart 3 패턴 매칭 기능의 일부)

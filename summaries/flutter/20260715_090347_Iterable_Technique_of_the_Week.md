# Iterable (Technique of the Week)

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=i-cTuLn9KNo
- **요약 일시**: 2026-07-15 09:03:47

---

## 🔑 핵심 요약
- 커스텀 클래스가 내부 데이터를 노출하지 않으면서도 `list`, `set`처럼 순회 가능하게 만드는 방법 소개
- 클래스에서 **`Iterable`을 extend**하면 `for-in` 루프, `map`, `first`, `forEach` 등 **30개 이상의 함수형 메서드**를 그대로 사용 가능
- 내부 컬렉션 프로퍼티를 public으로 노출할 필요가 없어짐

---

## 📣 주요 발표 내용
- 예시: 단어 맞추기 게임의 `Word` 클래스 — 내부적으로 `letters`라는 `List`를 보유
- 기존 방식: 순회를 위해 `letters` 프로퍼티를 외부에 노출해야 했음 (캡슐화 위반)
- 개선 방식: `Word` 클래스가 `Iterable`을 extend하도록 변경
  - 이때 구현해야 할 프로퍼티는 단 하나, **`iterator` getter**
  - 내부적으로 감싸고 있는 `List`의 iterator를 그대로 반환("pass the buck")하면 끝

---

## 💡 개발자 포인트
- `Iterable`을 extend하면 별도 노출 없이도 `isEmpty` 체크, `for-in` 순회, `map`/`first`/`forEach` 등 풍부한 함수형 API를 무료로 얻을 수 있음
- 캡슐화(내부 데이터 은닉)와 순회 편의성(`Iterable` 인터페이스)을 동시에 만족시키는 Dart의 관용적 패턴
- 자체 컬렉션형 클래스(래퍼 클래스)를 만들 때 매번 순회 로직을 재구현하는 대신 이 패턴을 재사용할 것
- 자세한 내용은 `dart.dev` 공식 문서 참고

---

## 📅 버전 / 출시 일정
해당 없음

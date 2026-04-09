# Stateful widgets in Flutter

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=Gzz8FwSlsUg
- **요약 일시**: 2026-04-09 09:03:59

---

## 🔑 핵심 요약
- **Flutter**에서 모든 위젯은 **불변(immutable)** 객체이며, 변경되는 것이 아니라 **교체(replace)** 된다
- `StatefulWidget`은 불변의 `StatefulWidget` 클래스와 가변(mutable)의 `State` 객체, **두 클래스**로 구성된다
- UI 상태 변경 시 반드시 `setState()`를 호출해야 Flutter가 리빌드를 수행한다

---

## 📣 주요 발표 내용
- 🧩 **위젯의 본질**: 위젯은 UI 그 자체가 아닌, 현재 프레임을 어떻게 그릴지 알려주는 **단일 사용 레시피(recipe)**
- 🔄 `StatelessWidget` vs `StatefulWidget`: Stateless는 단일 불변 클래스, Stateful은 **위젯 클래스 + State 클래스** 쌍으로 구성
- 🗂️ `State` 객체의 특징:
  - **가변(mutable)** 이며 **재사용 가능**하고 **오래 유지(long-lived)**
  - 실제 `build()` 메서드와 상태 로직을 담당
- 🛠️ `State` 객체의 주요 생명주기 메서드:

| 메서드 | 호출 시점 | 주요 용도 |
|---|---|---|
| `initState()` | State 객체 생성 시 **단 1회** | 애니메이션·텍스트 컨트롤러 등 초기화 |
| `setState()` | 상태 변경 시 직접 호출 | Flutter에 리빌드 요청 |
| `build()` | 빌드/리빌드 필요 시 | UI 위젯 트리 반환 |
| `dispose()` | State 객체가 위젯 트리에서 영구 제거 시 | 컨트롤러 등 리소스 해제 |

---

## 💡 개발자 포인트

- `initState()` 내에서 위젯으로부터 전달받은 데이터를 활용해 초기화할 것
  - State 객체가 아직 위젯에 완전히 연결되기 전이므로 **생성자 대신 `initState()` 사용**이 권장됨

> ⚠️ **주의**: 상태값(변수)만 변경하고 `setState()`를 호출하지 않으면 Flutter는 리빌드를 수행하지 않아 **UI에 아무런 변화가 없다.**
> 반드시 변경 로직을 `setState()` 콜백 내부에서 실행할 것.

- `dispose()`에서 `AnimationController`, `TextEditingController` 등 **리소스를 반드시 해제**하여 메모리 누수 방지
- **상태(State)** 란 단순히 "시간이 지남에 따라 변할 수 있는 모든 데이터"를 의미

---

## 📅 버전 / 출시 일정
해당 없음

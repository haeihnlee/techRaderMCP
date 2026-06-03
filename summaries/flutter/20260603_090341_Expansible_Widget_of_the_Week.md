# Expansible (Widget of the Week)

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=TfoJ55nx1S4
- **요약 일시**: 2026-06-03 09:03:41

---

## 🔑 핵심 요약
- Flutter 위젯 라이브러리의 **`Expansible`** 위젯은 정보를 숨겼다가 사용자 요청 시 펼쳐 보여주는 **접이식(확장형) UI**를 제공한다.
- **항상 보이는 `header`** 와 **기본 숨김 상태인 `body`** 두 영역으로 구성되며, `ExpansibleController`로 펼침/접힘 상태를 제어한다.
- 펼침 애니메이션은 `duration`·`curve`로 손쉽게 커스터마이즈하거나, `expandableBuilder`로 완전히 직접 구현할 수 있다.

---

## 📣 주요 발표 내용
- **`Expansible`** 은 리스트 아이템·버튼처럼 보이며, 눌렀을 때 숨겨진 내용을 드러내는 위젯이다.
- 사용 흐름:
  - **`ExpansibleController`** 를 먼저 생성한다.
  - 컨트롤러를 `Expansible` 위젯에 전달한다.
  - **`header`** (항상 표시)와 **`body`** (기본 숨김, 트리거 시 확장) 두 위젯을 제공한다.
- 일반적으로 사용자가 **header를 탭** 하면 토글된다.
  - header 위젯을 **`GestureDetector`** 로 감싸고, 컨트롤러의 상태를 토글하도록 구현한다.
- 애니메이션 커스터마이징:
  - **`duration`**, **`curve`** 속성으로 확장 애니메이션을 조정한다.
  - 처음부터 직접 만들고 싶다면 **`expandableBuilder`** 로 완전한 제어권을 가진다.

---

## 💡 개발자 포인트
- `body`는 **기본적으로 숨김(hidden)** 상태이므로, 초기 화면 공간을 절약하면서 필요할 때만 정보를 노출하는 UX에 적합하다.
- 토글 동작이 **자동으로 제공되지 않으므로**, header를 직접 `GestureDetector`로 감싸고 컨트롤러 상태를 토글해야 한다.

> 단순 펼침/접힘은 `duration`·`curve`만으로 충분하지만, 커스텀 전환 효과가 필요하면 `expandableBuilder`를 사용해 애니메이션을 처음부터 직접 빌드해야 한다.

- 더 많은 위젯 정보는 **`flutter.dev`** 에서 확인할 수 있다.

---

## 📅 버전 / 출시 일정
해당 없음


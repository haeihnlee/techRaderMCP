# Grandparents’ guide to Stateful vs. Stateless widgets

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=ugCxwq7FBrg
- **요약 일시**: 2026-07-31 09:03:45

---

## 🔑 핵심 요약
- Flutter 개발자들이 **`StatelessWidget`과 `StatefulWidget`의 차이**를 비개발자(조부모)에게 설명해보는 짧은 비유 모음 영상
- 판단 기준은 단 하나 — **"화면이 스스로 바뀔 정보를 들고 있는가"**
- 기술 용어 없이도 설명 가능한 비유들: **신문 vs TV**, **냉장고 안 병 순서**, **WhatsApp 채팅 목록 vs 대화 화면**

---

## 📣 주요 발표 내용
- **신문 vs TV 비유**
  - `StatelessWidget` = **신문** — 인쇄된 정보가 바뀌지 않음
  - `StatefulWidget` = **TV** — 계속 새 정보가 들어오고, 채널(상태)을 바꿀 수 있음
- **레시피 비유**
  - 매번 처음부터 똑같이 만들면 `Stateless`
  - 레시피에 **메모를 추가하고 그 변경을 유지**해야 하면 `Stateful`
- **냉장고 비유**
  - 병 순서를 재배치하고 **다시 열었을 때도 그 순서가 유지**되길 원하면 `StatefulWidget`
  - `StatelessWidget`이면 냉장고는 항상 **원래 순서**로 돌아가 있음
- **WhatsApp 비유**
  - 채팅 목록만 보여주는 화면 → `Stateless`에 가까움
  - 채팅을 선택해 화면이 **변해야 하는 순간** → `Stateful` 필요

---

## 💡 개발자 포인트
- 위젯 선택의 실무 기준은 **"이 위젯이 스스로 기억해야 하는 값이 있는가"** 한 줄로 요약됨
  - 없다 → `StatelessWidget` (더 가볍고, 예측 가능하고, 리빌드 비용이 낮음)
  - 있다 → `StatefulWidget` + `setState`
- **냉장고 비유가 상태 유지(state persistence)의 핵심**을 잘 짚음 — 상태를 위젯이 들고 있지 않으면 리빌드 시 **초기값으로 리셋**된다는 점

> ⚠️ 비유에 주의: WhatsApp 예시처럼 "화면이 바뀌니까 무조건 `StatefulWidget`"은 정확하지 않습니다. 실제로는 상태를 상위로 올리거나(`state lifting`) `Provider`·`Riverpod`·`Bloc` 같은 상태관리 솔루션으로 분리하면 화면이 변해도 위젯 자체는 `Stateless`로 유지할 수 있습니다.

- 팀 내 온보딩·주니어 교육 시 **이 비유 세트를 그대로 재활용**하기 좋음

---

## 📅 버전 / 출시 일정
해당 없음


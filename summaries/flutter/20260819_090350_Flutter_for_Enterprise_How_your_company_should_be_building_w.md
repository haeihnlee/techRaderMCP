# Flutter for Enterprise: How your company should be building with Flutter at scale | Anna Leushchenko

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=_gD4P4ZH2P0
- **요약 일시**: 2026-08-19 09:03:50

---

## 🔑 핵심 요약
- **UK 핀테크 Tide**의 Flutter 아키텍트 Anna Leushchenko가 네이티브 앱을 Flutter 모노레포로 전환한 실전 경험을 공유
- 대규모 Flutter 앱의 핵심 설계 원칙은 **LEGO 개념의 모듈화** — 작은 단위(feature)를 표준 인터페이스로 조합해 국가/시장별 다른 앱 구성
- 엔터프라이즈 Flutter의 핵심 과제는 **확장성·유지보수성·적정 복잡도**의 균형이며, "문제를 한 번 풀고 코드베이스 전체에 곱한다"는 원칙이 핵심

---

## 📣 주요 발표 내용
- **모노레포 + 순수 Flutter** 구성으로 Android/iOS 동시 지원, 웹 확장도 진행 중
- 앱을 작은 feature 단위로 분리하고 **표준 인터페이스**로 연결하는 LEGO 아키텍처 채택
- 각 feature를 독립적으로 **유닛 테스트** 커버 후, 조합 부분(sewing parts)만 통합 테스트
- `analytics` 이벤트 리포팅을 초기에는 명시적 호출로 구현 → 이후 **글로벌 시스템 리스너** 방식으로 리팩터링 (개발자가 신경 쓰지 않아도 자동 보고)
- Flutter 신버전 출시 후 **첫 달 내 업그레이드**를 표준으로 설정하여 최신 상태 유지

---

## 💡 개발자 포인트
- 초기 설계 시 결정해야 할 기본 요소: **상태 관리(State Management)**, **네비게이션**, **의존성 주입(DI)**, **디자인 시스템**
- "코끼리를 어떻게 먹나? 한 번에 한 조각씩" — **분할 정복(divide & conquer)**이 대규모 Flutter 코드 품질 유지의 핵심
- 일관된 구현 패턴이 확립되면 Flutter 버전 업그레이드·아키텍처 변경 시 비용이 크게 줄어듦

> **과잉 설계(overengineering) 주의**: 프로젝트 초기에는 최종 규모를 알 수 없으므로, 미래 과제를 인식하되 지나친 추상화는 피할 것. 스트림/리스너 기반 글로벌 해법은 규모가 커진 뒤 도입해도 늦지 않음.

- Material 디자인 구현을 기반으로 **커스텀 디자인 시스템**을 단계적으로 구축하는 방식 권장
- Flutter의 멀티플랫폼 특성(mobile → web)이 엔터프라이즈 "한 번 작성, 모든 곳 배포" 전략과 잘 맞음

---

## 📅 버전 / 출시 일정
해당 없음

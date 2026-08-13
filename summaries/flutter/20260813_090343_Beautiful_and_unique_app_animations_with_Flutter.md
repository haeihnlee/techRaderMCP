# Beautiful and unique app animations with Flutter

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=PWIMJ6duSkA
- **요약 일시**: 2026-08-13 09:03:43

---

## 🔑 핵심 요약
- Flutter 내장 위젯과 애니메이션 API를 활용해 사용자 참여도를 높이는 앱 애니메이션 구현
- 화면 전환(screen transition)과 커스텀 고유 애니메이션을 결합하여 독창적인 UX 제공
- Flutter 기본 기능과 서드파티 애니메이션 파일을 함께 사용하는 하이브리드 접근법 소개

---

## 📣 주요 발표 내용
- **화면 전환 애니메이션**: Flutter의 내장 네비게이션 전환 효과 활용법
- **커스텀 애니메이션**: 앱 고유의 개성 있는 애니메이션을 직접 설계하는 방법
- **Flutter 위젯 & 애니메이션 API**: `AnimationController`, `Tween`, `AnimatedWidget` 등 기본 제공 기능 적극 활용
- **서드파티 통합**: 외부 툴로 제작한 커스텀 애니메이션 파일을 Flutter 앱에 통합
- Flutter 기본 + 서드파티 라이브러리를 **조합하는 전략**으로 풍부한 애니메이션 구현

---

## 💡 개발자 포인트
- 애니메이션은 단순 시각 효과가 아닌 **사용자 참여도(engagement) 향상**의 핵심 요소
- Flutter 내장 애니메이션만으로 부족할 경우 Lottie, Rive 등 서드파티 애니메이션 파일 포맷 활용 검토
> 커스텀 애니메이션 파일과 Flutter 위젯 애니메이션을 혼용할 때는 성능 오버헤드에 주의하고, `RepaintBoundary`로 렌더링 범위를 제한하는 것이 권장됨
- 화면 전환 시 `PageRouteBuilder`나 `Hero` 위젯을 사용하면 네이티브에 준하는 자연스러운 전환 구현 가능

---

## 📅 버전 / 출시 일정
해당 없음

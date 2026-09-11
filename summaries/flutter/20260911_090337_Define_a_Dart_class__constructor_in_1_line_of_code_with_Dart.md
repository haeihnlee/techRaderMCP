# Define a Dart class & constructor in 1 line of code with Dart 3.13 🤯

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=7zXOgsE-elA
- **요약 일시**: 2026-09-11 09:03:37

---

## 🔑 핵심 요약
- **Dart 3.13**에서 **Primary Constructors**가 공식 안정화됨
- 클래스 필드와 생성자를 **한 줄**로 선언 가능
- `@NativeAsset` 어노테이션을 통한 미사용 네이티브 코드 **트리 쉐이킹** 지원

---

## 📣 주요 발표 내용
- **Primary Constructors 안정화**: 필드 선언과 생성자를 한 줄로 결합하는 간결한 문법 정식 지원
- 클래스 바디 내부에서 `new` 또는 `factory` 키워드 사용 가능, 클래스명 생략 및 빈 바디는 `;`으로 종료
- **`@NativeAsset` 어노테이션**: 앱에서 실제로 호출하는 네이티브 코드만 최종 번들에 포함
  - 패키지의 네이티브 바인딩이 호출되지 않으면 네이티브 바이너리가 번들에서 **완전히 제거**
- **Dart 포맷터 업데이트**: 메서드 호출, 메서드 체이닝, import 섹션 분리에 대한 코드 포맷팅 개선

---

## 💡 개발자 포인트
- Primary Constructors는 해당 릴리즈에서 가장 영향력 있는 기능으로 평가됨
- 앱 번들 크기를 줄이는 데 `@NativeAsset` 트리 쉐이킹이 직접 기여

> **업그레이드 방법**: `flutter upgrade`를 실행하면 Dart 3.13을 즉시 사용 가능

---

## 📅 버전 / 출시 일정

| 버전 | 주요 변경 |
|------|-----------|
| Dart 3.13 | Primary Constructors 안정화, `@NativeAsset` 트리 쉐이킹, 포맷터 개선 |


# Could Dart JNI replace MethodChannel?

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=g_tjuGnihNU
- **요약 일시**: 2026-11-13 09:03:28

---

## 🔑 핵심 요약
- `MethodChannel`을 **JNI/FFI**로 대체하는 것은 *가능하지만 권장하지 않음*
- 기존 `MethodChannel` 코드는 먼저 **Pigeon**으로 이전하는 것이 권장 경로
- 고성능이 정말 필요할 때만 **Pigeon FFI** → 그 이상이면 직접 JNI/FFI 사용

---

## 📣 주요 발표 내용
- JNI·FFI는 **메모리 관리**를 개발자가 직접 처리해야 함
- 파라미터/인수 타입(`float`, `double` 등) 변환을 직접 정확히 맞춰야 하는 등 훨씬 **엄격함**
- JNI/FFI 계층 깊은 곳에서 발생한 문제는 **진단(디버깅)이 까다로움**
- 대다수 사용자에게는 **Pigeon**, 필요 시 **Pigeon FFI**가 최선의 선택
- Pigeon FFI로 전환하면 기본 네이티브 API를 사용할 수 있는 선택지가 생김

---

## 💡 개발자 포인트
- 마이그레이션 권장 순서: `MethodChannel` → **Pigeon** → (필요 시) **Pigeon FFI** → (극한 성능 요구 시) 직접 **JNI/FFI**
- Pigeon FFI 도입 전, 해당 성능 향상이 **실제로 필요한지 먼저 평가**할 것 — 필요 없을 가능성이 높음
- 직접 JNI/FFI를 쓰는 것은 **매우 높은 성능이 요구되는 작업**에 한정

> ⚠️ 주의: JNI/FFI 직접 사용 시 메모리 누수·타입 불일치 문제를 스스로 책임져야 하며, 문제 발생 시 원인 추적이 어렵습니다.

---

## 📅 버전 / 출시 일정
해당 없음

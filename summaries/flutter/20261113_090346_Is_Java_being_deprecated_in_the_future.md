# Is Java being deprecated in the future?

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=etSJQNFiGl4
- **요약 일시**: 2026-11-13 09:03:46

---

## 🔑 핵심 요약
- **JNI** 지원과 관련해 "Java가 앞으로 deprecated 되는가?"라는 질문에 대한 짧은 Q&A 답변
- 'Java'는 **Java 언어**와 Android 앱이 실행되는 **Java 가상 플랫폼(JVM)** 이라는 두 가지 의미로 쓰임
- JNI 지원에서 말하는 Java는 JVM 쪽이며, **JVM 위에서 실행되는 모든 것**이 JNI 네이티브 상호 운용성으로 지원됨

---

## 📣 주요 발표 내용
- Dart의 **JNI 기반 네이티브 상호 운용성**은 특정 언어(Java)가 아니라 **JVM 플랫폼**을 대상으로 함
- 현재 모든 Android 앱은 JVM(Android 런타임) 위에서 실행됨
- 따라서 JVM에서 동작하는 코드라면 JNI interop으로 호출 가능

> 영상에서 Java 언어 자체의 deprecation 여부나 일정에 대한 직접적인 발표는 없음

---

## 💡 개발자 포인트
- Dart ↔ Android 네이티브 연동에서 JNI 방식은 **JVM 바이트코드 기준**으로 동작하므로, Java로 작성된 라이브러리든 JVM 계열 언어로 작성된 라이브러리든 대상이 될 수 있음
- "Java 지원"이라는 표현을 **언어**가 아니라 **런타임/플랫폼** 관점으로 이해해야 함
- `MethodChannel` 대신 JNI 기반 직접 호출을 검토할 때, 기존 JVM 기반 Android SDK·라이브러리 자산을 그대로 활용할 수 있다는 점이 핵심

---

## 📅 버전 / 출시 일정
해당 없음


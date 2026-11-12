# Flutter interop with Pigeon FFI

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=GHH5DHmg_gE
- **요약 일시**: 2026-11-12 09:08:14

---

## 🔑 핵심 요약
- **Pigeon**에 **JNI/FFI 백엔드**가 추가되어, 메시지 직렬화 대신 네이티브 메서드를 **직접 호출**하는 바인딩을 생성할 수 있음
- `MethodChannel`의 **개발 편의성**과 raw JNI/FFI의 **베어 메탈 성능** 사이에서 절충안을 제공
- Dart로 작성한 타입 안전한 인터페이스 계약 하나로 Android 권한 플러그인을 처음부터 끝까지 만드는 데모를 진행

---

## 📣 주요 발표 내용
- 기존 접근법별 트레이드오프 비교
  - `MethodChannel`: 설정은 간단하지만 문자열 기반 메서드 이름, 동적 맵 파싱, 직렬화 때문에 호출마다 **지연 시간**이 늘어남
  - raw JNI/FFI 바인딩: 속도가 빠르고 메모리에 직접 접근할 수 있지만, 복잡한 호스트 API에서는 **래퍼 코드가 크게 늘어남**
- 표준 Pigeon은 플랫폼 바이너리 메신저를 거쳐 인수를 직렬화하는 메시지 핸들러를 생성함
- JNI/FFI 백엔드를 켜면 메시지 전달 대신 **직접 JNI/FFI 바인딩**을 생성해 **직렬화 오버헤드**를 줄임
- `@ConfigurePigeon` 어노테이션에서 `useJni` / `useFfi`를 `true`로 설정하면 기존 네이티브 파이프라인(jnigen/ffigen)으로 바인딩을 생성함
- 네이티브 백엔드가 없는 플랫폼에는 MethodChannel 코드를 생성해 **모든 플랫폼에서 같은 API 인터페이스**를 유지함

---

## 💡 개발자 포인트
- 인터페이스 계약은 보통 `pigeons/messages.dart`에 둠
  - `@ConfigurePigeon`: 코드 생성 방식(JNI 사용, Android 대상, 출력 경로)을 지정
  - `@HostApi()` 추상 클래스: Dart에서 호출할 네이티브 메서드를 선언
  - 계약 메서드가 네이티브 메서드 시그니처와 꼭 같을 필요는 없음
- JNI 백엔드를 쓰면 `pigeon` 외에도 여러 의존성(JNI 관련 패키지)이 필요함
- 패키지 루트에서 Pigeon 생성기를 실행하면, 콘솔 출력으로 JNI가 쓰이는지 확인할 수 있음

> ⚠️ **아키텍처 차이**: Pigeon FFI에서는 엔진의 `BinaryMessenger`에 핸들러를 **등록하지 않습니다**. 대신 **생성된 API Registrar**를 사용합니다.

- Kotlin 플러그인 생명주기 처리
  - Activity에 attach될 때: Registrar가 활성 플러그인 인스턴스를 **JNI 룩업 테이블**에 바인딩
  - detach될 때: `null`을 넘겨 등록 해제
- 데모 구현 예 (Permissions API)
  - `checkPermission`: 활성 Activity 컨텍스트로 `ContextCompat.checkSelfPermission` 호출
  - `requestPermission`: 이미 부여됐는지 확인 → rationale이 필요한지 판단 → 권한 요청 전달
- 로컬 테스트
  - 예제 앱의 `pubspec.yaml`에 버전 대신 **path 의존성**으로 플러그인 지정
  - `AndroidManifest.xml`에 테스트할 권한 선언
- Dart 쪽에서는 `PermissionsApi`를 인스턴스화해 일반 Dart 함수처럼 호출하지만, 실제 실행은 네이티브 Android API에서 직접 이뤄짐
- 참고 자료: flutter.dev 문서, Pigeon GitHub 저장소, pub.dev `pigeon` 페이지

---

## 📅 버전 / 출시 일정
해당 없음


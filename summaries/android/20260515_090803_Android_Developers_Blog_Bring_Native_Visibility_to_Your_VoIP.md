# Android Developers Blog: Bring Native Visibility to Your VoIP App Experience with Telecom's Latest Alpha

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/voip-native-visibility-telecom-alpha.html
- **요약 일시**: 2026-05-15 09:08:03

---

## 🔑 핵심 요약
- **Jetpack Telecom v1.1.0** 알파 릴리즈에서 서드파티 VoIP 앱을 시스템 다이얼러에 네이티브 수준으로 통합
- 통합 통화 기록(**Unified Call History**), 시스템 다이얼러에서의 **네이티브 콜백**, 통화 로그 제외(**Call Log Exclusion**) 3가지 신기능 도입
- **Android 16.1 (SDK 36.1)** 이상에서 동작하며, 초기 단계에서는 Google Meet부터 단계적으로 시스템 다이얼러 렌더링이 활성화됨

---

## 📣 주요 발표 내용
- **통합 통화 기록 (Unified Call History)**
  - 기존에는 VoIP 앱마다 별도로 열어 통화 기록을 확인해야 했음
  - 이제 시스템 다이얼러가 서드파티 VoIP 앱의 통화 로그를 직접 표시
- **네이티브 콜백 (Native Callback)**
  - 시스템 다이얼러에서 바로 VoIP 연락처에 콜백 가능
  - 구현 방법:
    1. `TelecomManager.ACTION_CALL_BACK` 시스템 보호 인텐트 등록
    2. `TelecomManager.addCall` (또는 Jetpack API)로 통화 자동 로깅
    3. `CallControlScope.getCallId`로 발급된 UUID 관리
    4. `TelecomManager.EXTRA_UUID`로 전달된 콜백 인텐트 처리
- **통화 로그 제외 (Call Log Exclusion)**
  - `CallAttributesCompat`의 `isLogExcluded = true` 플래그 설정 시 시스템 로그에서 완전히 숨김
  - 프라이버시·일회성 통신 등 특정 통화를 다이얼러 기록에서 제외 가능
- 신규 기능을 시연하는 **샘플 앱** 제공 ([platform-samples/telecom](https://github.com/android/platform-samples/tree/main/samples/connectivity/telecom))

---

## 💡 개발자 포인트
- 기존 `ConnectionService` 대신 `CallsManager`를 사용하는 흐름의 연장선 — Android O (API 26)까지 하위 호환 유지
- 콜백 구현 시 **UUID 기반으로 통화 세부정보를 앱 측에서 직접 저장·관리**해야 함 (시스템이 EXTRA_UUID만 전달)

> ⚠️ **주의**: 시스템 다이얼러의 네이티브 통화 로그 렌더링은 단계적 출시이며, 스팸 방지를 위해 **보안 패키지 allowlist**로 제어됨. 현재는 **Google Meet** 위주로 활성화되며 일반 서드파티 앱은 별도 등록이 필요할 수 있음.

> 💡 **로컬 테스트 팁**: 실제 시스템 다이얼러 대신 오픈소스 **Telecom Sample Dialer 앱**을 에뮬레이터 환경으로 사용해 콜백·로깅을 검증할 것

- 콜백 인텐트는 `TelecomManager.ACTION_CALL_BACK`으로 시스템 보호되므로, 매니페스트에 정확히 등록해야 동작
- `isLogExcluded` 플래그를 잘못 사용하면 사용자가 통화 기록을 추적할 수 없으니 UX 관점에서 신중히 적용

---

## 📅 버전 / 출시 일정

| 항목 | 값 |
|------|-----|
| 라이브러리 | **Jetpack Telecom v1.1.0** (Alpha) |
| 최소 동작 OS | **Android 16.1 (SDK 36.1)** 이상 (통합 로깅/콜백 기능) |
| 하위 호환 | Android O (API 26) — 기본 CallsManager 기능 |
| 다이얼러 렌더링 단계적 출시 | **Google Meet**부터 시작, 추후 확대 |


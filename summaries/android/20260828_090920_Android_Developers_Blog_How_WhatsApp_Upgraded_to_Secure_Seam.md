# Android Developers Blog: How WhatsApp Upgraded to Secure, Seamless Sign-In for 1 Billion Users with Passkeys

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/08/whatsapp-passkeys-secure-sign-in.html
- **요약 일시**: 2026-08-28 09:09:20

---

## 🔑 핵심 요약
- **WhatsApp**이 10억 명 이상 사용자를 위해 **패스키(Passkey)** 기반 인증을 도입, 피싱 방지 및 원탭 로그인 구현
- Android **Credential Manager API**로 클라이언트 통합, 백엔드는 **Erlang + Rust `webauthn-rs`** 라이브러리로 WebAuthn/FIDO2 처리
- OEM 다양성·Android 버전별 엣지 케이스 대응 위해 Google 팀과 긴밀히 협력, 플랫폼 레벨 개선사항 반영

---

## 📣 주요 발표 내용
- **패스키 도입 배경**: SMS OTP 전달이 불안정한 지역에서도 안정적으로 동작, 계정 탈취·자격증명 도용 방지
- **클라이언트 통합**: `Credential Manager API`가 복잡한 자격증명 프로바이더를 추상화, `request/response` 패턴으로 생성·조회 처리
- **서버 아키텍처**: 4개 진입점(`Begin/Finish Registration`, `Begin/Finish Authentication`)으로 WebAuthn 세레모니 오케스트레이션
- **UX 최적화**: A/B 테스트로 컨텍스트 기반 패스키 생성 프롬프트 개발, Android OS 흐름 성숙에 맞춰 단일 화면으로 간소화
- **멀티 패스키 지원**: `multi_passkey_enabled` 플래그로 자격증명 추가(상한 초과 시 가장 오래된 항목 제거) 또는 교체 모드 선택 가능

---

## 💡 개발자 포인트
- **성능 개선**: 패스키 미생성 사용자(초기 단계 대다수)의 자격증명 조회 레이턴시가 문제 → 콜 패스 계측·병목 제거로 Android 생태계 전체에 이익
- **에러 처리 계층화**: 예외를 `recoverable(복구 가능)` vs `terminal(치명적)` 상태로 분류, 패스키 플로우 실패 시 기존 인증으로 **graceful degradation**

> **Android 13 기기**: `GetPublicKeyCredentialDomException (Failed to decrypt credential)` 발생 사례 있음 — Google과 WhatsApp 공동으로 플랫폼 레벨 수정 적용

> **Android 14 기기**: `CreatePublicKeyCredentialDomException (Unable to get sync account)` 패스키 생성 중 발생 — 동일하게 플랫폼 개선으로 대응

- **서버 측 `needs_update` 플래그**: `webauthn-rs` 라이브러리가 자격증명 갱신 필요 시 신호 → `refresh_credential` 자동 호출
- 상세 에러 코드 가이드: [Credential Manager 에러 가이드](https://developer.android.com/identity/sign-in/credential-manager-error-reference) 참고
- 패스키 모범 사례: [Passkeys best practices blog](https://android-developers.googleblog.com/2024/05/passkeys-best-practices.html) 참고

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| 패스키 도입 시작 | 2023년 (주요 소비자 앱 중 최초) |
| 블로그 게시일 | 2026년 8월 27일 |
| 대상 Android 버전 | Android 13, 14+ (버전별 예외 처리 필요) |

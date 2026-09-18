# Android Developers Blog: Introducing the AndroidX Security State Libraries: A Unified View of Device Security

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/09/introducing-androidx-security-state-libraries.html
- **요약 일시**: 2026-09-18 09:05:37

---

## 🔑 핵심 요약
- **AndroidX Security State 1.1.0** 및 **Security State Provider 1.0.0** 라이브러리 안정 릴리즈 발표
- 단순 SPL 문자열 대신 **시스템·시스템 모듈·커널** 각각의 컴포넌트 수준 보안 패치 레벨(`DSPL`, `PSPL`, `ASPL`) 제공
- 뱅킹·핀테크·MDM 앱에서 기기의 실제 보안 상태를 프로그래밍 방식으로 검증 가능

---

## 📣 주요 발표 내용
- **세 가지 패치 레벨 API** 제공:
  - `DSPL` (Device SPL): 현재 기기에 설치된 패치 레벨 — 네트워크 호출 없이 동기 조회
  - `PSPL` (Published SPL): Android Security Bulletin에 공식 게재된 최신 패치 레벨
  - `ASPL` (Available SPL): 기기에 다운로드·설치 준비된 패치 레벨 — IPC 비동기 조회
- 추적 컴포넌트: **System**(OS OTA), **System Modules**(Google Play 시스템 업데이트), **Kernel**(LTS 버전 기준)
- `androidx.security.state.provider` 라이브러리로 OEM·OTA 클라이언트가 ASPL 정보를 표준화된 방식으로 노출 가능
- **[OSV](https://osv.dev/) 데이터베이스** 연동으로 특정 **CVE** 패치 여부까지 감사 가능
- **Android 17** 신기능: OEM이 SPL 범위를 초과한 개별 보안 픽스를 `Supplemental Patches XML`로 선언 가능 — 즉시 컴플라이언스 입증

---

## 💡 개발자 포인트
- **앱 개발자·MDM**: `androidx.security.state` 라이브러리로 앱 실행 시 동기적으로 `DSPL`을 확인하고, 민감 워크플로우 전에 `ASPL`로 업데이트 대기 여부를 조회해 사용자에게 안내 가능
- **OEM·업데이트 클라이언트**: `androidx.security.state.provider`를 통해 ASPL 정보를 표준 IPC로 노출 — Google Play 시스템 업데이트·GOTA 이미 온보딩 완료

> **주의**: `ASPL`은 비동기 IPC 호출이므로, UI 스레드 차단 없이 코루틴/비동기 방식으로 처리해야 합니다.

- **CVE 수준 감사**: 고보안 앱(예: NFC 탭투페이, 블루투스 근접 공유)은 특정 CVE 픽스 여부를 검증하는 취약점 리포트를 OSV에서 다운로드하여 확인 가능
- 단일 SPL 비교의 한계를 보완 — 월별 업데이트에 신규 위협이 없는 경우 라이브러리가 자동으로 보안 레벨을 "유효(effective)" 상태로 증가 처리

---

## 📅 버전 / 출시 일정

| 라이브러리 | 버전 | 상태 |
|---|---|---|
| `androidx.security:security-state` | 1.1.0 | Stable (2026-09-17 발표) |
| `androidx.security:security-state-provider` | 1.0.0 | Stable (2026-09-17 발표) |
| Android 17 Supplemental Patches XML | - | Android 17 이상 지원 |


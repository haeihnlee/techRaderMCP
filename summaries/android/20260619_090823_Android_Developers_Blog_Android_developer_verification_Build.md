# Android Developers Blog: Android developer verification: Building a safer ecosystem together

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/06/android-developer-verification.html
- **요약 일시**: 2026-06-19 09:08:23

---

## 🔑 핵심 요약
- **개발자 인증(Android developer verification)** 보호 정책이 **2026년 9월 30일**부터 브라질·인도네시아·싱가포르·태국 4개국에서 우선 시행됩니다.
- Google Play를 포함한 **7개 앱스토어**가 참여하며, 2027년에는 인증 디바이스 전체로 글로벌 확대됩니다.
- 앱 등록 자동화를 위한 **신규 API**(상태 조회·콘솔 관리)와 ID·수수료 없는 **limited distribution 계정**이 도입됩니다.

---

## 📣 주요 발표 내용
- **시행일·대상국**: `2026-09-30`부터 **브라질·인도네시아·싱가포르·태국** 사용자 대상으로 발효.
- **참여 스토어 (7개)**: Google(Google Play), Honor(HONOR App Market), OPPO(OPPO App Market), **삼성(Galaxy Store)**, Transsion(Palm Store), vivo(V-Appstore), Xiaomi(GetApps).
- **신규 API 2종**:
  - `Android Developer ID Status API` — 패키지명이 이미 등록됐는지 조회
  - `Android Developer Console API` — 개발 환경에서 직접 패키지명 등록·관리
  - 두 API 모두 **OAuth 위임** 지원 → 서드파티 플랫폼이 대신 등록 처리 가능
- **시스템 서비스**: 2026년 6월부터 대부분의 Android 기기에 자동 설치되어, 연내 개발자 등록 검증에 활용.
- **limited distribution 계정**: 학생·취미 개발자용. 정부 발급 신분증·수수료 없이 **최대 20대 기기**에 앱 공유 가능.

---

## 💡 개발자 포인트
- **Google Play 개발자**: 대부분 이미 인증 완료, 앱의 99% 이상이 등록됨. `Play Console Home`에서 인증 상태 확인 후 미등록 앱을 직접 등록하면 됩니다.
- **Google Play 외부에만 배포하는 개발자**: `Android Developer Console`에 가입해 앱을 등록해야 합니다.
- **CI/CD 통합**: 신규 API로 앱을 대량(bulk) 등록하거나 파이프라인에 직접 통합 가능.

> ⚠️ **Breaking Change**: 위 4개국 참여 스토어에서는 `2026-09-30`부터 **앱 등록이 필수**입니다. 미등록 앱은 `adb`(Android Debug Bridge) 또는 advanced flow로만 사이드로드 가능합니다.

> 🔐 **advanced flow**: 미인증 개발자 앱 설치 시 강압형 사기(coercion scam)를 막는 보안 체크포인트를 포함하되, 파워 유저의 사이드로딩 권한은 유지합니다.

---

## 📅 버전 / 출시 일정
| 시점 | 내용 |
| ------ | ------ |
| 2026년 6월 | 검증용 **시스템 서비스** 자동 설치 시작 |
| 2026년 7월 | `Android Developer ID Status API` 글로벌 출시 / `Console API` 및 limited distribution 계정 early access 시작 |
| 2026년 8월 | limited distribution 계정·`Console API` 글로벌 출시 / **advanced flow** 출시 |
| 2026년 9월 30일 | 브라질·인도네시아·싱가포르·태국 참여 스토어에서 **앱 등록 필수화** |
| 2027년 이후 | 인증 요구사항 **글로벌 확대** |

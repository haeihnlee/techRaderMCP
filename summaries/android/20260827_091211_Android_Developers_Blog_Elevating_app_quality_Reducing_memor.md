# Android Developers Blog: Elevating app quality: Reducing memory usage and improving device migration

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/08/app-quality-memory-optimization-secure-onboarding.html
- **요약 일시**: 2026-08-27 09:12:11

---

## 🔑 핵심 요약
- Google Play가 **메모리 사용량**과 **기기 이전 온보딩**에 관한 새로운 앱 품질 요구사항 발표
- 2027년 2월부터 메모리·DEX 코드 최적화 기준 미달 앱은 Play 노출 및 게시 제한
- 2027년 4월부터 `Restore Credentials API`를 통한 **Zero-Tap Sign-In** 미지원 앱도 동일 제재

---

## 📣 주요 발표 내용

**1. 앱 메모리 사용량 감소 및 코드 최적화**
- **Dynamic Memory Usage** (Anonymous RSS + Swap): 앱 상태(포그라운드·백그라운드 등)와 기기 RAM 버킷별로 평가
- **Bitmap Memory Usage**: 비가시 상태(백그라운드·캐시)에서 비트맵을 오래 유지하지 않도록 요구
- **Optimized DEX Code**: `R8` 등 shrinking 도구로 최소 **25% coverage** 충족 필수 (최적화·축소·난독화 포함)

**2. Zero-Tap Sign-In (기기 이전 온보딩)**
- `Android Restore Credentials API` 사용 필수화
- 새 기기 첫 실행 시 탭 없이 자동 로그인 복원 지원
- 게임은 현재 예외이나 2027년 중 별도 가이드 예정

**3. Play Console 신규 도구 제공**
- **Android vitals** 내 동적 메모리·비트맵 메모리 신규 지표 추가
- Out-of-Memory 크래시 전용 필터 추가
- 업로드된 앱 번들에 대한 **DEX 코드 최적화 인사이트** 제공
- 임계값 초과 시 Android vitals 개요 페이지에 경고 표시

---

## 💡 개발자 포인트

- `R8`(또는 동등 도구)를 반드시 활성화하고 **최적화·shrink·난독화 커버리지 25% 이상** 확보할 것
- 백그라운드·캐시 상태에서 비트맵 참조를 적시 해제하도록 코드 점검 필요
- 로그인 기능이 있는 모든 앱(선택·필수 불문)은 `Restore Credentials API` 통합 준비 시작

> ⚠️ **2027년 2월 이후 메모리/DEX 기준 미달 앱**, **2027년 4월 이후 Zero-Tap Sign-In 미지원 앱**은 Google Play 노출 축소 및 게시 기능 제한을 받을 수 있습니다.

---

## 📅 버전 / 출시 일정

| 항목 | 시행 시기 |
|---|---|
| 메모리 사용량 (Anonymous RSS + Swap) 기준 적용 | 2027년 2월 |
| Bitmap 메모리 사용량 기준 적용 | 2027년 2월 |
| DEX 코드 최적화 (25% coverage) 의무화 | 2027년 2월 |
| Zero-Tap Sign-In (`Restore Credentials API`) 의무화 | 2027년 4월 |
| 추가 진단 도구(Memory Limiter 지표 등) 제공 | 2026년 하반기 예정 |


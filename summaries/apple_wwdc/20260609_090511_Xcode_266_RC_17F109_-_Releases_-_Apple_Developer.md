# Xcode 26.6 RC (17F109) - Releases - Apple Developer

- **컨퍼런스**: Apple WWDC
- **출처**: https://developer.apple.com/news/releases/?id=06082026h
- **요약 일시**: 2026-06-09 09:05:11

---

## 🔑 핵심 요약
- Apple이 **`Xcode 26.6` RC(Release Candidate, 빌드 `17F109`)** 를 배포했습니다.
- RC는 정식 출시 직전의 **최종 후보 빌드**로, App Store 제출에 사용 가능한 안정 버전입니다.
- 배포일은 **2026년 6월 8일**이며, WWDC26 발표 흐름과 맞물린 릴리즈입니다.

---

## 📣 주요 발표 내용
- **`Xcode 26.6` Release Candidate** 정식 공개
- 빌드 번호: **`17F109`**
- 다운로드(`View downloads`) 및 릴리즈 노트(`View release notes`)가 Apple Developer 사이트에 함께 제공됨
- RC 단계 진입 → `26.6` 정식 버전이 곧 GA(General Availability)로 전환될 예정

> ⚠️ 원본 릴리즈 페이지는 빌드 정보 위주로 짧게 제공됩니다. 변경된 SDK·API·버그 수정 상세 항목은 Apple Developer의 **`View release notes`** 링크에서 직접 확인이 필요합니다.

---

## 💡 개발자 포인트
- RC 빌드는 **정식 릴리즈와 동일한 코드베이스**로 간주되므로, 마이그레이션·회귀 테스트를 미리 진행하기에 적합합니다.
- 앱 빌드·아카이브 환경을 `Xcode 26.6`으로 올리기 전, CI 파이프라인의 **Xcode 버전 핀(pin)** 과 **command line tools** 경로(`xcode-select`) 점검을 권장합니다.

> Breaking Change 여부는 본문에 명시되어 있지 않습니다. SDK 버전 상승에 따른 deprecation 경고가 있을 수 있으니, 정식 채택 전 **`View release notes`** 확인 후 적용하세요.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| 제품 | Xcode |
| 버전 | `26.6` |
| 단계 | RC (Release Candidate) |
| 빌드 번호 | `17F109` |
| 배포일 | 2026-06-08 |


# iPadOS 26.5 RC 2 (23F77) - Releases - Apple Developer

- **컨퍼런스**: Apple WWDC
- **출처**: https://developer.apple.com/news/releases/?id=05082026b
- **요약 일시**: 2026-05-09 09:04:10

---

## 🔑 핵심 요약
- **iPadOS 26.5 RC 2** (빌드 `23F77`) 가 **2026년 5월 8일** 자로 Apple Developer 채널에 배포되었습니다.
- 이번 빌드는 **Release Candidate 2 (RC 2)** 단계로, 일반 사용자 대상 정식 출시 직전의 마지막 검증용 빌드입니다.
- 다운로드 및 릴리즈 노트는 Apple Developer 사이트의 Releases 페이지에서 확인할 수 있습니다.

---

## 📣 주요 발표 내용
- **iPadOS 26.5 RC 2** 빌드 `23F77` 공개
- 직전 RC 1 빌드 이후의 잔여 이슈 수정 및 안정성 개선이 포함된 것으로 추정되는 **GM(Gold Master) 후보** 빌드
- 다운로드 경로: Apple Developer → Downloads / Releases
- 정식 릴리즈 노트는 별도 페이지(`View release notes`)에서 제공

---

## 💡 개발자 포인트
> **RC 2 빌드는 사실상 정식 출시 빌드와 동일**한 코드 베이스를 기반으로 합니다. 앱의 호환성 검증을 RC 2 기준으로 마무리하고, App Store 제출 빌드를 이 환경에서 최종 테스트하는 것이 안전합니다.

- 기존 베타에서 발견된 회귀 이슈가 있다면 **RC 2에서 재현 여부를 다시 확인**해야 합니다 — 정식 출시 전 마지막 수정 기회입니다.
- 빌드 번호 `23F77` 을 CI/디바이스 매트릭스에 추가하여 회귀 테스트를 돌리는 것을 권장합니다.
- `iPadOS 26.5` 신규 API를 사용 중이라면 `Xcode` 의 최신 SDK와 연동하여 동작 확인이 필요합니다.

---

## 📅 버전 / 출시 일정

| 항목 | 값 |
|------|-----|
| OS | iPadOS 26.5 |
| 빌드 번호 | `23F77` |
| 단계 | RC 2 (Release Candidate 2) |
| 배포일 | 2026-05-08 |
| 채널 | Apple Developer |


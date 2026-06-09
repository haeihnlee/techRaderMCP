# App Store Connect API 4.4 - Releases - Apple Developer

- **컨퍼런스**: Apple WWDC
- **출처**: https://developer.apple.com/news/releases/?id=06082026a
- **요약 일시**: 2026-06-09 09:04:31

---

## 🔑 핵심 요약
- Apple이 **App Store Connect API `4.4`** 버전을 **2026년 6월 8일** 릴리스했습니다.
- App Store Connect API는 앱 메타데이터·빌드·심사·판매 데이터를 **REST로 자동화**하는 인터페이스입니다.
- 이번 공지는 릴리스 발표 페이지로, 상세 변경 내역은 페이지 내 **`View release notes`** 링크에서 확인할 수 있습니다.

---

## 📣 주요 발표 내용
- **App Store Connect API `4.4`** 정식 배포
- 릴리스 페이지에서 **`Download file`** (OpenAPI 스펙 파일)과 **`View release notes`** 제공
- 통상적으로 minor 버전 업데이트에는 **신규 엔드포인트 추가**, **기존 리소스 속성 확장**, **버그 수정**이 포함됩니다

> ⚠️ 본 공지 본문에는 세부 변경 항목이 노출되지 않았습니다. 정확한 신규/변경 엔드포인트는 반드시 원문의 `View release notes`를 확인하세요.

---

## 💡 개발자 포인트
- CI/CD 파이프라인에서 App Store Connect API를 사용 중이라면 **`4.4` OpenAPI 스펙**을 내려받아 클라이언트 SDK를 재생성하는 것을 권장합니다.
- minor 버전은 일반적으로 **하위 호환**을 유지하지만, deprecated 표시된 필드가 있는지 릴리스 노트에서 점검하세요.
- `fastlane`, `xcrun altool`, 자체 스크립트 등 API 의존 도구들의 **스펙 버전 동기화** 여부를 확인하세요.

> 자동화 스크립트는 응답 스키마 변경에 민감하므로, 신규 필드 추가 시 파싱 로직이 깨지지 않는지 회귀 테스트를 권장합니다.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| 버전 | App Store Connect API `4.4` |
| 릴리스 일자 | 2026년 6월 8일 |
| 제공 자료 | OpenAPI 스펙 파일(`Download file`), 릴리스 노트(`View release notes`) |


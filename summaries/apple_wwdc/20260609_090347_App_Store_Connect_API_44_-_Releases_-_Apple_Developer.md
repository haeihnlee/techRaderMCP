# App Store Connect API 4.4 - Releases - Apple Developer

- **컨퍼런스**: Apple WWDC
- **출처**: https://developer.apple.com/news/releases/?id=06082026a
- **요약 일시**: 2026-06-09 09:03:47

---

## 🔑 핵심 요약
- **App Store Connect API 4.4** 버전이 **2026년 6월 8일** 릴리스됨 (WWDC26 주간 발표)
- App Store Connect 운영 자동화를 위한 **REST API**의 정기 업데이트 버전
- 이 페이지는 릴리스 공지로, 상세 변경 내역은 **`View release notes`** 및 **`Download file`** 링크에서 확인 필요

---

## 📣 주요 발표 내용
- **`App Store Connect API`** 가 **4.4** 로 버전업
- 릴리스 날짜: **June 8, 2026**
- 공지 페이지에서 제공하는 항목:
  - **`Download file`** — OpenAPI 스펙(SDK 생성용 스키마) 다운로드
  - **`View release notes`** — 신규 엔드포인트·필드·변경 사항 상세 노트

> ⚠️ 본 공지 페이지 본문은 메타 정보만 포함합니다. 실제 추가/변경된 엔드포인트, deprecated 항목, 스키마 변경은 **release notes 원문**을 반드시 확인하세요.

---

## 💡 개발자 포인트
- **App Store Connect API**는 앱 메타데이터·심사 제출·TestFlight·매출 리포트 등을 코드로 자동화하는 핵심 인터페이스입니다.
- 새 버전의 **OpenAPI 스펙(`Download file`)**을 받아 클라이언트 SDK / 타입 정의를 재생성하면 신규 필드를 바로 활용할 수 있습니다.

> 🔧 **권장 액션**: CI/CD나 내부 배포 자동화에서 App Store Connect API를 쓰고 있다면, `4.4` release notes의 **Breaking Change / Deprecation** 항목을 점검 후 스펙을 최신으로 갱신하세요. 마이너 버전이라도 필드 deprecation이 포함될 수 있습니다.

- 인증은 기존과 동일하게 **JWT 기반 API Key** 방식을 사용합니다 (별도 명시 변경 없는 한 호환 유지).

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| API 버전 | **App Store Connect API 4.4** |
| 릴리스 날짜 | **2026-06-08** |
| 유형 | REST API 정기 업데이트 (마이너 버전) |
| 상세 노트 | 원문 페이지의 `View release notes` 링크 참조 |


# App Store Connect API 4.4.1 - Releases - Apple Developer

- **컨퍼런스**: Apple WWDC
- **출처**: https://developer.apple.com/news/releases/?id=07152026a
- **요약 일시**: 2026-07-16 09:04:50

---

## 🔑 핵심 요약
- Apple이 **App Store Connect API `4.4.1`**을 2026년 7월 15일 출시
- 마이너 패치 버전으로, `OpenAPI Specification` 파일이 함께 갱신 배포됨
- 세부 변경 내역은 별도 릴리즈 노트 페이지에서 확인 가능 (본문은 JS 렌더링이라 자동 추출 제한)

---

## 📣 주요 발표 내용
- **App Store Connect API** 버전이 `4.4.1`로 업데이트됨
- 배포 리소스
  - **OpenAPI Specification** 다운로드: `app-store-connect-openapi-specification.zip`
  - **Release Notes** 페이지: `developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-4-4-1-release-notes`
- 버전 넘버링(`4.4.x`)으로 볼 때 신규 엔드포인트 추가보다는 **버그 수정/필드 보완 성격의 패치**로 추정됨

---

## 💡 개발자 포인트
- App Store Connect API를 연동 중인 CI/CD 파이프라인이나 자동화 스크립트가 있다면, 최신 **OpenAPI spec**을 받아 코드 생성기(예: `openapi-generator`)를 다시 돌려 스키마 변경 여부를 확인 권장
- 자동 요약 도구로는 릴리즈 노트 상세 항목(신규 엔드포인트, 필드 변경, deprecated 여부)을 가져오지 못했으므로, **정확한 변경사항은 원문 릴리즈 노트를 직접 확인** 필요

> 패치 버전(`4.4.1`)이므로 Breaking Change 가능성은 낮지만, 프로덕션 자동화에 반영 전 원문 확인을 권장합니다.

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
| --- | --- |
| 버전 | `4.4.1` |
| 출시일 | 2026-07-15 |


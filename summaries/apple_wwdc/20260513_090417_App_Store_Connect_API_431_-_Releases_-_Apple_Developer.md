# App Store Connect API 4.3.1 - Releases - Apple Developer

- **컨퍼런스**: Apple WWDC
- **출처**: https://developer.apple.com/news/releases/?id=05122026a
- **요약 일시**: 2026-05-13 09:04:17

---

## 🔑 핵심 요약
- **App Store Connect API 4.3.1** 마이너 업데이트가 2026년 5월 12일 릴리스됨
- Apple Developer 공식 릴리스 페이지에 게시된 SDK/도구 업데이트
- 상세 변경사항은 별도 **Release Notes** 및 다운로드 파일로 제공

---

## 📣 주요 발표 내용
- `App Store Connect API` **4.3.1** 버전이 공식 릴리스됨
- Apple Developer Releases 채널을 통해 배포 자료(다운로드 파일 + 릴리스 노트) 공개
- 4.3.x 트랙의 **패치 업데이트**로, 4.3.0 대비 호환성 유지 (semver 기준)

---

## 💡 개발자 포인트
- App Store Connect API를 사용 중인 CI/CD 파이프라인 및 자동화 스크립트는 신규 버전 호환성을 확인할 것
- CLI 도구(`xcrun altool`, `fastlane`, 자체 스크립트 등)에서 API 클라이언트 의존성을 사용한다면 업그레이드 검토 권장

> ⚠️ 본 페이지에서 제공되는 본문 정보가 매우 제한적이므로, 실제 변경 내역은 반드시 **공식 Release Notes**를 직접 확인해야 합니다.

> 💡 패치 버전(4.3.0 → 4.3.1)이므로 Breaking Change 가능성은 낮지만, 인증/메타데이터 업로드 등 critical path에서는 staging 환경 검증 후 적용 권장

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| 제품 | App Store Connect API |
| 버전 | 4.3.1 |
| 릴리스 일자 | 2026-05-12 |
| 배포 채널 | Apple Developer Releases |
| 제공 형식 | Download file + Release Notes |


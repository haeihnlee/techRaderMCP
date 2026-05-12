# iPadOS 16.7.16 (20H392) - Releases - Apple Developer

- **컨퍼런스**: Apple WWDC
- **출처**: https://developer.apple.com/news/releases/?id=05112026k
- **요약 일시**: 2026-05-12 09:10:19

---

## 🔑 핵심 요약
- **iPadOS 16.7.16** (빌드 `20H392`) 가 **2026-05-11** 자로 Apple Developer 릴리즈 채널에 공개되었습니다.
- iPadOS 16 계열에 대한 **레거시 유지보수 업데이트**로, 최신 iPadOS 17/18/26 라인과 별개로 구형 디바이스를 위해 지속 배포 중인 트랙입니다.
- 페이지에는 **다운로드** 와 **릴리즈 노트** 링크만 제공되며, 상세 변경사항은 별도 노트 페이지에서 확인 필요합니다.

---

## 📣 주요 발표 내용
- 빌드 번호: **`20H392`** — iPadOS 16 계열 (`20Hxxx`) 의 점진적 패치 빌드
- 배포 채널: **Apple Developer Releases** (`developer.apple.com/news/releases`)
- 게시일: **2026년 5월 11일**
- 제공 리소스
  - `View downloads` — 개발자 계정으로 IPSW/구성 프로파일 다운로드
  - `View release notes` — 변경 내역 및 알려진 이슈

---

## 💡 개발자 포인트
- iPadOS 16.x 계열은 **iPad (5th/6th gen)**, **iPad Pro 9.7"/12.9" (1st gen)** 등 **iPadOS 17 미지원 디바이스**의 최종 지원 라인입니다.

> ⚠️ iPadOS 17 이상으로 업그레이드되지 않는 구형 iPad를 타깃 디바이스로 가진 경우, **`Deployment Target`을 iPadOS 16으로 유지**하거나 **`@available` 분기 처리**가 필요합니다.

- 신규 API 추가보다는 **보안 패치 / 안정성 수정** 위주일 가능성이 높으므로, 기존 앱은 회귀 테스트 위주로 검증하면 됩니다.
- 엔터프라이즈/MDM 환경에서는 `20H392` 빌드를 **승인 빌드 리스트**에 추가하여 사용자 OTA 업데이트 차단/허용 정책을 조정하세요.

---

## 📅 버전 / 출시 일정

| 항목 | 값 |
|---|---|
| OS | iPadOS |
| 버전 | **16.7.16** |
| 빌드 | `20H392` |
| 출시일 | 2026-05-11 |
| 채널 | Developer Releases (정식) |
| 계열 | iPadOS 16 레거시 유지보수 |


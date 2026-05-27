# visionOS 26.6 beta (23O5728e) - Releases - Apple Developer

- **컨퍼런스**: Apple WWDC
- **출처**: https://developer.apple.com/news/releases/?id=05262026e
- **요약 일시**: 2026-05-27 09:06:40

---

## 🔑 핵심 요약
- **visionOS 26.6 beta** (빌드 `23O5728e`)가 2026년 5월 26일 Apple Developer 채널에 릴리스됨
- Apple Vision Pro 대상 차기 마이너 업데이트의 첫 베타로, **다운로드**와 **릴리스 노트**가 동시 공개됨
- 정식 GA 이전 단계이므로 프로덕션 앱 검증 및 호환성 테스트를 시작할 시점

---

## 📣 주요 발표 내용
- **빌드 번호**: `23O5728e` — visionOS 26.x 트랙의 마이너 업데이트(`26.6`) 첫 베타 시드
- **배포 채널**: Apple Developer Releases 페이지를 통해 즉시 시드 (`View downloads` / `View release notes` 링크 제공)
- **대상 플랫폼**: **Apple Vision Pro** (visionOS 전용 SKU)
- 동일 일자 릴리스 트랙(`iOS 26.6 beta`, `iPadOS 26.6 beta`, `macOS 26.6 beta`, `tvOS 26.6 beta`)과 **동시 시드**되어 OS 간 의존성 점검에 적합

---

## 💡 개발자 포인트
- **테스트 디바이스 분리**: 베타는 **개발용 Vision Pro**에 설치하고 메인 디바이스 적용은 보류 권장
- **Xcode/SDK 매칭**: visionOS 26.6 SDK가 포함된 최신 Xcode 베타로 빌드해야 신규 심볼/Behavior 변경 사항을 정확히 검증 가능
- **RealityKit·ARKit 회귀 테스트**: 공간 컴퓨팅 앱은 트래킹/렌더링 회귀가 잦으므로 손/시선/공간 앵커 시나리오 우선 검증

> ⚠️ **베타 OS에는 알려진 이슈**가 포함될 수 있으므로 반드시 **릴리스 노트(View release notes)**를 먼저 확인 후 설치할 것. 다운그레이드가 불가하거나 까다로운 경우가 많음.

> 📌 같은 26.6 트랙으로 **iOS/iPadOS/macOS/tvOS**가 함께 시드되었으므로, 멀티플랫폼 앱은 **5종 OS 베타 매트릭스**에서 동시 검증 권장.

---

## 📅 버전 / 출시 일정
| 항목 | 값 |
|------|-----|
| OS | visionOS |
| 버전 | 26.6 beta |
| 빌드 | `23O5728e` |
| 릴리스 일자 | 2026-05-26 |
| 대상 디바이스 | Apple Vision Pro |
| 채널 | Apple Developer (베타 시드) |


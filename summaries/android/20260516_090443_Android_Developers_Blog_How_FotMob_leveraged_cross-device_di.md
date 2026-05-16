# Android Developers Blog: How FotMob leveraged cross-device discovery to score record Wear OS adoption

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/fotmob-wear-os-adoption-cross-device-discovery.html
- **요약 일시**: 2026-05-16 09:04:43

---

## 🔑 핵심 요약
- **FotMob**이 폰 앱 내에서 **Wear OS 앱 cross-device 설치 플로우**를 도입해 5년 만에 **하루 설치 2~3배** 폭증 달성
- 핵심은 `NodeClient` + `CapabilityClient`로 **Wear OS 앱 미설치 디바이스만 탐지**하고, `RemoteActivityHelper`로 **워치 Play Store를 원격 실행**
- 신규 **In-App Install Prompts 라이브러리**(`CrossDevicePromptManager`)가 출시되어 동일 플로우를 더 쉽게 구현 가능

---

## 📣 주요 발표 내용
- **문제 인식 (Discovery Gap)**: Wear OS 디바이스를 보유한 FotMob 사용자 다수가 워치 앱 존재 자체를 인지하지 못함
- **연결된 워치 탐지**: `nodeClient.connectedNodes.await()`로 페어링된 Wear OS 노드 조회
- **앱 설치 여부 확인**: Wear OS 패키지에 XML capability(`CAPABILITY_WEAR_APP`) 정의 후 `capabilityClient.getCapability(..., FILTER_REACHABLE)`로 reachable 노드 조회 → **capability가 없는 노드만 추천 후보**로 필터
- **Half-page 교육 프롬프트** UI: 워치 앱 스크린샷을 보여주며 설치/취소 선택지 제공 (intrusive 하지 않게 설계)
- **원격 설치 실행**: `RemoteActivityHelper.startRemoteActivity()`로 `market://details?id=...` Intent를 워치 노드에 전달해 Play Store 실행
- **신규 라이브러리 발표**: `CrossDevicePromptManagerFactory.create(activity)` → `requestInstallationPromptFlow()` → `launchPromptFlow()` 패턴으로 위 과정을 추상화

---

## 💡 개발자 포인트
- **Wearable Data Layer API**(`NodeClient`, `CapabilityClient`, `RemoteActivityHelper`)만으로 자체 cross-device 설치 UX 구현 가능 — 추가 백엔드 없이 클라이언트 측만으로 처리
- Capability는 **Wear OS 모듈 쪽 XML 리소스**로 선언해야 하며, 폰 앱은 `FILTER_REACHABLE`로 현재 도달 가능한 노드만 필터링하는 것이 핵심
- **신규 In-App Install Prompts 라이브러리** 사용 시 자체 구현보다 보일러플레이트가 크게 감소 — `CrossDevicePromptException` 캐치로 errorCode 기반 에러 처리 필요

> **실측 효과**: 출시 100% 도달 후 **48시간 내 1,500+ 신규 설치**, 일평균 대비 **2~3배** 증가. 워치 앱 노출 채널이 부족한 팀이라면 ROI가 매우 높은 기능.

> **UX 주의**: 프롬프트는 사용자에게 **도움이 되는(helpful)** 형태여야지 강요(intrusive)로 느껴지면 안 됨 — 스크린샷·dismiss 옵션 제공 권장.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 게시일 | 2026-05-15 |
| 적용 API | Wearable Data Layer (`NodeClient`, `CapabilityClient`, `RemoteActivityHelper`) |
| 신규 라이브러리 | **In-App Install Prompts** (`CrossDevicePromptManager`) |
| 참고 샘플 | DataLayer sample, In-App Install Prompts library |


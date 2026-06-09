# WWDC 2026 Keynote & Platforms State of the Union

- **컨퍼런스**: Apple WWDC
- **출처**: https://www.engadget.com/2189698/everything-announced-at-apples-wwdc-2026-keynote/
- **요약 일시**: 2026-06-09 17:54:19

---

## 🔑 핵심 요약

2026년 6월 8일 열린 WWDC 2026. Tim Cook이 9월 1일 John Ternus에게 CEO를 넘기기 전 마지막으로 진행한 WWDC. 핵심은 (1) 구글 Gemini 기반의 **Siri AI** 정식 등장, (2) **Foundation Models 프레임워크의 서드파티 클라우드 모델 개방**, (3) Liquid Glass 디자인 조정 + 대폭적인 성능 개선이다. 개발자 베타는 6월 8일 공개, 정식 출시는 올 가을.

- **OS 라인업**: iOS 27, iPadOS 27, macOS "Golden Gate"(macOS 27), watchOS 27, tvOS 27, visionOS 27
- **AI 모델 구조**: 온디바이스 `AFM Core` / `AFM Core Advanced`(멀티모달·sparse 아키텍처), 서버용 `AFM Cloud Pro`(구글 클라우드 Nvidia GPU, Gemini Frontier급)
- **EU 주의**: DMA 규제로 iOS/iPadOS용 Siri AI는 EU 초기 미제공 (macOS·visionOS·watchOS는 제공)

## 🎙️ Siri AI — 대대적인 개편

2024년에 처음 시연 후 계속 미뤄지던 Siri 개편이 마침내 **'Siri AI'**라는 이름으로 등장했다.

- **대화형 어시스턴트**: 화면 내용을 읽고, 내 메시지·메일·사진을 뒤져서 답변. 카드 형태로 답하고 이어서 대화 가능
- **구글 Gemini 기반**: 가장 무거운 작업은 `AFM Cloud Pro` 모델이 처리(구글 클라우드의 Nvidia GPU에서 구동, Gemini Frontier급 품질)
- **새 인터페이스**: iOS 27에서 화면 중앙을 아래로 스와이프하면 Siri AI 호출. Dynamic Island에 애니메이션 표시
- **화면 인식 액션**: 페스티벌 일정 스크린샷에서 원하는 공연만 골라 캘린더에 추가, 카메라가 보는 것에 대한 질문 등 (구글 Visual Intelligence와 유사)
- **전용 챗봇 앱**: 텍스트·이미지 생성, 파일 분석 등. 음성 표현력/말 속도 커스터마이징 가능
- **지원 플랫폼**: iOS/iPadOS/macOS/watchOS/visionOS/CarPlay/AirPods
- **대상 기기**: iPhone 16 이상, iPhone 15 Pro/Pro Max, M1 이상 iPad/Mac, Vision Pro, Apple Watch Series 10 이상 등
- ⚠️ **초기엔 영어만**, **EU에서는 iOS/iPadOS용 Siri AI 미제공**(DMA 규제 이유, 단 macOS·visionOS·watchOS에는 제공)

## ✨ Apple Intelligence 신규 기능

- **Safari**: 탭을 주제별 자동 정리, 웹페이지 변경(가격 인하·재입고) 알림, 설명만으로 커스텀 확장 프로그램 생성
- **Passwords**: 취약/유출된 로그인 정보를 한 번에 강화하고 해당 사이트 비번까지 자동 갱신
- **Messages/Mail**: 내 문체를 흉내내는 스마트 답장
- **Calendar**: 설명으로 이벤트 추가·수정, 연락처·위치 자동 추가
- **Photos**: 가상 리프레이밍, 이미지 확장(Extend) 도구 — 생성·편집 이미지엔 SynthID 워터마크
- **접근성 강화**: VoiceOver 이미지 설명 풍부화, Action 버튼으로 카메라 질의응답, Accessibility Reader 요약·번역 지원
- **AirPods용 커스텀 EQ** (iOS 27)

## 🧑‍💻 개발자에게 유용한 정보 (Dev Tools & API)

### Foundation Models 프레임워크
- 3줄 Swift API로 온디바이스 모델 호출(오프라인·프라이빗·무료·API key 불필요)은 유지
- **iOS 27에서 확장**: 더 큰 베이스 모델, 확장된 컨텍스트 윈도우, **온디바이스 파인튜닝**(데이터 외부 유출 없음), **이미지 입력**(멀티모달), 커스텀 AI 스킬 추가
- **서드파티 클라우드 모델 개방**: 새 `LanguageModel` 프로토콜로 모델 제공자가 공통 추론 인터페이스 구현 → 온디바이스 Apple 모델과 클라우드 Gemini가 **동일 API 뒤에** 위치
- **Gemini 연동**: 구글이 Firebase Apple SDK를 통해 Gemini를 Foundation Models 프레임워크에 네이티브로 제공

### Xcode 27 / Swift
- **온디바이스 AI 코드 완성**: Apple Silicon에서 클라우드 왕복 없이 예측형 멀티라인 코드 완성, 서드파티 AI 모델로 라우팅 옵션
- **MCP(Model Context Protocol) 플랫폼 전반 지원**: Claude·Codex 등 에이전트가 프로젝트 자율 탐색, 기능 스캐폴딩, 멀티파일 리팩터링
- 시뮬레이터 속도 향상, Git 워크플로 통합 강화, Instruments(메모리·에너지) 프로파일링 개선
- Swift 6.2 동반

### SwiftUI / App Intents
- SwiftUI·UIKit에 **폴더블 대비** 적응형 레이아웃 API(힌지 상태 감지, 멀티 구성 디스플레이 처리)
- **App Intents가 Siri 연동의 필수 표면(mandatory surface)** 으로 승격 → **SiriKit 공식 deprecation 예고**. 앱의 Siri AI 노출을 원하면 App Intents로 마이그레이션 필요

## 🎨 디자인 변경 (Liquid Glass & macOS)

- **Liquid Glass 조정**: 기본 외형을 덜 투명하게 변경 + **투명도(opacity) 슬라이더** 추가로 사용자가 직접 조절
- **macOS 디자인 통일**: 앱 간 통일된 툴바, 화면 끝까지 확장되어 산만함을 줄이는 사이드바, 모든 윈도우의 더 좁은 모서리 곡률(corner radius), 앱 아이콘 리프레시
- 생성·편집 이미지에는 **SynthID 워터마크** 적용

## ⚡ 성능 개선 (개발자·사용자 모두 체감)

- **속도 향상**: AirDrop 전송 / Mail 메시지 로딩 / Apple Music 재생 시작 **최대 80%↑**
- 앱 실행 **최대 30%↑**, 카메라 롤 사진 표시 **최대 70%↑**, Wi-Fi→셀룰러 전환도 더 빠르게
- **구형 기기 가속**: CPU 스케줄러 수정으로 iPhone 11 이상에서 체감 향상 (iOS 27은 iOS 26 지원 모델 전체 지원)
- **검색 인프라 재구축**: Spotlight·Mail·Photos 기반을 새로 구축해 더 안정적·효율적, 새 파일/데이터를 거의 즉시 인덱싱
- iCloud 공유 앨범이 **풀 해상도** 지원 (Android·Windows 포함)

## 👨‍👩‍👧 자녀 보호 / 안전

- **Child account 도입** — 13세 미만 필수, 18세까지 유지 가능
- 연락처·앱·웹사이트 접근 제어, 앱 시간 제한 세분화, Screen Time 재설계
- iPhone 없는 자녀를 위한 Apple Watch 설정 방법 추가

## 📦 OS 버전 & 출시

- **iOS 27, iPadOS 27, macOS "Golden Gate"(macOS 27), watchOS 27, tvOS 27, visionOS 27**
- 개발자 베타 **6월 8일 공개**, 정식 출시는 **올 가을** (퍼블릭 베타는 7월 중순 예상)

## 🔗 출처

- [Everything announced at Apple's WWDC 2026 keynote — Engadget](https://www.engadget.com/2189698/everything-announced-at-apples-wwdc-2026-keynote/)
- [Development tool updates from WWDC: Foundation Models, Xcode 26, Swift 6.2 — SD Times](https://sdtimes.com/softwaredev/development-tool-updates-from-wwdc-foundation-models-framework-xcode-26-swift-6-2-and-more/)
- [Bringing the latest Gemini models to Apple developers — Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/bringing-gemini-models-to-apple-developers/)
- [WWDC 2026 Keynote Confirmed: Core AI, MCP platform-wide — ChatForest](https://chatforest.com/builders-log/wwdc-2026-keynote-confirmed-apple-ai-platform-builder-guide/)
- [Apple Foundation Models WWDC 2026: Multimodal + Python SDK — byteiota](https://byteiota.com/apple-foundation-models-wwdc-2026-multimodal-python-sdk/)
- [WWDC 2026 live updates — CNBC](https://www.cnbc.com/2026/06/08/apple-wwdc-2026-live-updates.html)
- [WWDC26 — Apple Developer](https://developer.apple.com/wwdc26/)

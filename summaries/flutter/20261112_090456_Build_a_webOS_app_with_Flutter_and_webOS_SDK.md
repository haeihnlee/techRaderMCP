# Build a webOS app with Flutter and webOS SDK

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=jnLKELaDGIM
- **요약 일시**: 2026-11-12 09:04:56

---

## 🔑 핵심 요약
- LG가 **webOS Flutter SDK**를 2025년 6월 30일 공개 출시했으며, 이 SDK로 LG TV·스마트 모니터용 Flutter 앱을 개발·실행·테스트·패키징할 수 있음
- LG는 자체 **webOS 임베더**로 OLED부터 보급형 모델까지 TV 라인업 전반의 **시스템 앱**을 Flutter로 구동 중
- Flutter 팀은 서드파티 임베더를 Flutter SDK에 붙여 쓸 수 있게 하는 **"플러그인 가능한 플랫폼(Pluggable Platforms)"** 이니셔티브를 진행 중

---

## 📣 주요 발표 내용
- LG가 webOS에 Flutter를 채택한 이유는 **3F**: **Fast**(메모리가 적은 TV 하드웨어에서도 성능이 좋음), **Free**(오픈소스라 확장 가능), **Flourishing**(커뮤니티 성장)
- 첫 PoC는 2024년 출시한 **TV Guide Japan** 앱으로, 4방향 포커스 탐색이 있는 촘촘한 스크롤 편성표를 구현
- SDK는 **Flutter 3.22**를 지원하며, 출시 시점에 상태 관리·**Firebase** 연동 등을 포함한 **플러그인 25개**를 함께 제공
- 아키텍처: **webOS 임베더**가 Flutter 엔진과 Dart 코드를 TV 플랫폼 서비스에 연결하고, SDK가 TV용으로 교차 컴파일해 설치 가능한 앱 패키지를 생성
- 빌드 방식은 모바일·웹·데스크톱 Flutter 앱과 동일
- LG는 앞으로 Flutter 신규 버전에 맞춰 릴리스 일정을 조정하고 SDK 도구를 개선할 계획 (GitHub 저장소에서 피드백 접수 중)
- **Pluggable Platforms**: 플랫폼 팀이 Flutter tool·엔진을 따로 포크해 관리하지 않아도, 표준 Flutter SDK에 자체 임베더를 붙일 수 있게 하는 것이 목표. 기기 시뮬레이터 같은 도구도 플러그인 형태로 넣는 것을 지향함

> 주의: 자막에는 산출물이 "APK"로 나오지만, webOS의 앱 패키지 형식은 보통 **IPK**입니다. 자동 번역 오류로 보입니다.

---

## 💡 개발자 포인트
- **개발 환경**
  - macOS: 제공되는 **개발 컨테이너(dev container)** 저장소를 clone해서 빌드해야 함 (webOS CLI와 webOS NDK가 함께 설치됨)
  - Windows: **WSL 2** 필요
  - Ubuntu: 컨테이너 단계 없이 바로 진행 가능
- **초기 설정**: `precache` 명령으로 Flutter 엔진을 받고, `doctor` 명령으로 **webOS 플랫폼** 설정이 맞는지 확인
- **TV 연결**
  - TV에 **Developer Mode 앱**을 설치하고 LG 개발자 계정으로 로그인
  - **Key Server**를 켜고 passphrase를 복사하면 TV가 재시작됨
  - TV IP로 사용자 정의 장치를 등록하고 SSH 키와 passphrase를 입력하면 `devices` 목록에 TV가 표시됨
- **실행**: webOS 플랫폼으로 새 프로젝트를 만든 뒤 `debug` 명령 하나로 빌드·패키징·설치·실행까지 진행됨
- **Hot Reload**가 TV에서도 동작함 (터미널에서 `R`을 누르면 상태를 유지한 채 화면 갱신)
- 빌드 모드 3종을 그대로 지원
  - **Debug**: 핫 리로드
  - **Profile**: DevTools로 TV 칩의 프레임 레이트와 메모리를 직접 확인
  - **Release**: 출시용 성능 최적화 빌드
- TV가 없으면 **Linux** 플랫폼을 추가해 빌드하고 동작을 먼저 확인할 수 있음
- TV UI에서는 **4방향(D-pad) 포커스 탐색** 설계가 중요함 (TV Guide Japan 사례)

> 주의: SDK가 지원하는 버전은 **Flutter 3.22**입니다. 최신 Flutter stable과 버전 차이가 있을 수 있으니 패키지·플러그인 호환성을 미리 확인하세요.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 첫 Flutter PoC 앱 (TV Guide Japan) | 2024년 출시 |
| webOS Flutter SDK 공개 출시 | 6월 30일 (2025년) |
| 지원 Flutter 버전 | 3.22 |
| 출시 시 제공 플러그인 | 25개 |
| Pluggable Platforms | 진행 중 (일정 미발표) |


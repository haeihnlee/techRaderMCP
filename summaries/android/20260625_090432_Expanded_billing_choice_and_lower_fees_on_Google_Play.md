# Expanded billing choice and lower fees on Google Play

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/06/play-expanded-billing.html
- **요약 일시**: 2026-06-25 09:04:32

---

## 🔑 핵심 요약
- **Google Play**가 결제 유연성 확대와 함께 수수료 체계를 개편 — `service fee`(서비스 수수료)와 `billing fee`(결제 수수료)를 **분리**
- 개발자는 Google Play 결제 외에 **대체 결제 시스템** 또는 **외부 웹 링크**로 사용자를 유도 가능 (먼저 **US / UK / EEA** 대상)
- 서비스 수수료는 연 수익 **첫 $1M까지 10%**부터 시작, 모든 자동 갱신 구독에도 10% 적용
- `2026년 6월 30일`부터 US·UK·EEA에서 신규 수수료 구조 시작

---

## 📣 주요 발표 내용
- **billing choice program(결제 선택 프로그램)** 신설 — 영국·EEA·미국의 디지털 서비스/콘텐츠 제공 개발자에게 글로벌 제공, 이후 추가 시장으로 확대
- 개발자는 **UX 가이드라인**에 따라 자체 **choice screen(선택 화면)** 을 직접 디자인 가능 (Google Play 기본 화면 대체)
- **서비스 수수료와 결제 수수료 분리**가 핵심 변화
  - Google Play 결제 사용 시: 서비스 수수료 + **결제 수수료 5%**(US·UK·EEA) 추가
  - 대체 결제·외부 웹 링크 사용 시: **결제 수수료 미적용**
- 파트너 대상 프로그램 개편: **Games Level Up**(개편) + **Apps Experience**(신규)
  - 요건 충족 시 **인하된 program rate card(프로그램 요율표)** 적용 대상

---

## 💡 개발자 포인트
- 수수료율이 거래 사용자의 설치 시점에 따라 달라짐 — **New installs** vs **Existing installs** 구분 필수
  - **New installs**: 해당 지역 신규 수수료 구조 출시일 **이후** 최초 설치/업데이트한 사용자
  - **Existing installs**: 출시일 **이전** 최초 설치/업데이트한 사용자
- 자동 갱신 구독은 결제 수단과 무관하게 **일괄 10% 서비스 수수료** 적용

> **주의:** Google Play 결제를 계속 쓰면 5% 결제 수수료가 추가되지만, 대체 결제/외부 링크를 쓰면 결제 수수료가 없습니다. 다만 세금·환불·구독 처리 등 195개 시장의 복잡성은 직접 부담해야 하므로 단순 수수료 비교가 아닌 운영 비용 전반을 따져야 합니다.

> Games Level Up / Apps Experience 프로그램 요율표는 `2026년 9월 30일`부터 적용되므로, 그 전에 가이드라인을 검토하고 앱/게임을 준비해 두는 것이 유리합니다.

---

## 📅 버전 / 출시 일정
| 항목 | 일정 | 대상 |
| --- | --- | --- |
| 신규 수수료 구조 (수수료 분리) 시작 | 2026-06-30 | US · UK · EEA |
| Games Level Up / Apps Experience 요율표 적용 | 2026-09-30 | 요건 충족 파트너 |
| 추가 시장 확대 | 추후 staggered 일정 공개 | 글로벌 |


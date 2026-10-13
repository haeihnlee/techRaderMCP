# Why Flutter and Go are exploding

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=ZOUgNXycY7k
- **요약 일시**: 2026-10-13 09:06:37

---

## 🔑 핵심 요약
- Google Cloud 프레임워크·언어 담당 아웃바운드 PM **Abdallah Sheban**이 출연해 **Genkit**, **Flutter/Dart**, **Go** 등이 AI 에이전트 시대에 성장하는 이유를 설명
- **Genkit**은 *기존 앱에 AI 기능을 점진적으로 추가*하는 용도, **ADK**는 *독립형 멀티 에이전트 시스템 구축* 용도로 포지셔닝이 다름
- **생성형 UI(GenUI)**는 UI 구성의 주도권을 AI 에이전트에게 넘기는 새 패러다임이며, **구조화된 입출력**은 이를 받쳐 주는 도구
- **Flutter**는 임베디드 분야로 확장 중 — **Toyota**(2026 RAV4), **LG webOS**, **Samsung Tizen**이 실제로 사용하고 있음

---

## 📣 주요 발표 내용
- **Genkit 포지셔닝**
  - 오픈소스 프레임워크이며, 풀스택 개발자나 1인 개발자가 기존 앱에 AI·에이전트 기능을 붙일 때 사용
  - AI 전용 앱을 따로 유지할 필요 없이 일반 코드처럼 기능을 하나씩 추가할 수 있음
  - 지원 언어: **JavaScript/TypeScript, Dart, Go, Python**
  - 클라이언트와 서버 양쪽에서 동작하고, 둘을 분리해 구성할 수도 있음
- **ADK(Agent Development Kit)**
  - 플랫폼 팀이 만들고 여러 팀이 가져다 쓰는 **독립형 에이전트** 구축용
  - 오케스트레이션이 많이 들어가는 **멀티 에이전트 시스템**에 적합
- **Genkit Flows**
  - 코드를 감싸는 **고차 함수(high-order function)** 개념
  - Flow 내부 전체에 **observability**가 자동으로 붙음 → **Developer UI**에서 세밀하게 디버깅 가능
  - 결정론적 코드와 LLM 호출(예: Gemini로 형식 변환)을 하나의 Flow로 묶어 패키징
- **구조화된 입출력**
  - JS 생태계에서는 `Zod`를 Genkit에 함께 묶어 제공
  - Dart에는 마땅한 라이브러리가 없어 Google이 직접 **`Schematic`**을 만듦 (Zod와 비슷한 역할)
  - 모델 제공사 API가 돌려주는 구조화 출력(JSON)을 각 언어에서 네이티브 타입으로 쓸 수 있게 변환
- **Flutter GenUI**
  - 화면을 코드로 미리 정해 두지 않고, **컴포넌트 카탈로그 + 시스템 프롬프트**만 제공하면 AI 에이전트가 화면을 구성
  - 예: 온보딩 단계마다 필요한 필드만 동적으로 보여 주는 폼
- **Flutter 임베디드 확장 / Pluggable Platforms**
  - 커뮤니티가 만든 임베더: **Apple Watch**, **Wear OS**, **Raspberry Pi** 등
  - **"Pluggable Platforms"** 이니셔티브: 공식 지원하지 않는 플랫폼에도 쉽게 배포할 수 있게 하는 것이 최우선 과제
  - Toyota는 차량용(automotive-grade) Linux 임베더로 인포테인먼트를 구축

---

## 💡 개발자 포인트
- **도구 선택 기준**
  - 기존 앱에 AI 기능을 점진적으로 추가할 때 → `Genkit`
  - 여러 팀이 공유하는 독립형 멀티 에이전트를 만들 때 → `ADK`
- 운영 환경에서는 LLM의 **비결정성**을 다루기 위해 **스키마 기반 구조화 출력**이 사실상 필수
  - TS → `Zod`, Dart → `Schematic`
- 결정론적 단계 ↔ LLM 단계 사이의 데이터 전달은 Flow 안에서 스키마로 검증하는 패턴을 권장
- GenUI에서 구조화된 입출력은 **필수가 아님**
  - 표시만 하는 컴포넌트는 입력이 필요 없을 수 있음
  - 상호작용하는 컴포넌트는 입출력을 정의해 활용
- Flutter는 LSP·analyzer·성능 도구를 함께 제공하고, **AI 에이전트도 이 도구들을 그대로 쓸 수 있음**
  - 단일 코드베이스라 유지 인력과 **토큰 비용** 측면에서도 경제적이라고 강조
- **TV/임베디드 개발자 참고**: LG는 **모든 스크린 기기에서 webOS + Flutter**를 사용 중이라고 언급됨

> ⚠️ 현재 공식 지원하지 않는 플랫폼(커스텀 임베더)을 대상으로 하려면 **약간 다른 Flutter 버전**을 써야 합니다. Pluggable Platforms가 나오면 이 부분이 바뀔 예정입니다.

> ℹ️ 자막 추출이 약 12,000자에서 잘려, 후반부(임베더 동작 원리, **Go** 관련 논의)는 요약에 포함되지 않았습니다.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| Toyota RAV4 2026년형 | Flutter 기반 인포테인먼트 탑재 |
| Toyota Land Cruiser, Highlander | 출시 예정 모델에 적용 예정 |
| Flutter Pluggable Platforms | 진행 중인 이니셔티브 (일정 미공개) |


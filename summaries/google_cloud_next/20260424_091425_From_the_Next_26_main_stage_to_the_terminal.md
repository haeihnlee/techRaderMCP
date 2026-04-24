# From the Next ‘26 main stage to the terminal

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=m9HeWXndjAU
- **요약 일시**: 2026-04-24 09:14:25

---

## 🔑 핵심 요약

- Google Cloud Next에서 **Gemini Enterprise Agent Platform** 공개 — 에이전트의 빌드·스케일·거버넌스·최적화를 하나의 플랫폼으로 통합
- 프로토타입 → 프로덕션 전환의 어려움(Identity, Governance, Memory 등)을 플랫폼 레벨에서 해결
- **장기 실행 에이전트(Long-running Agent)** 및 **Memory Bank** GA 발표로 엔터프라이즈 수준의 에이전트 신뢰성 확보

---

## 📣 주요 발표 내용

### 🏗️ Build — `ADK` (Agent Development Kit)
- 🟢 **Python**, **Go**, **TypeScript**, **Java** 4개 언어 공식 지원
- 에이전트를 빠르게 빌드하고 프로덕션까지 올리기 위한 핵심 프레임워크
- `ADK`는 **빌드 단계**의 핵심이며, 거버넌스·최적화 기능과는 별도 레이어로 분리

### 🔐 Govern — 새로운 거버넌스 기능들
- 🆕 **Agent Gateway** 도입 — 에이전트 접근 제어 중앙화
- 🆕 **Agent Identity** — 에이전트별 **암호학적(cryptographically generated) 고유 ID** 발급
- 🆕 **Agent Registry** — 에이전트 등록 및 관리
- 🆕 **Anomaly Detection** — 에이전트 행동 이상 탐지 (숨겨진 핵심 기능으로 언급)
- 에이전트 행동에 대한 **Audit Trail(감사 추적)** 확보 가능

### 🧠 Scale — Memory & 장기 실행
- 🟢 **Memory Bank** GA — 세션 간·시간 축을 넘나드는 메모리 관리 자동화
  - 개발자가 메모리 전문가가 아니어도 자동으로 중요 정보 저장·관리
- 🟢 **Long-running Agent** 지원 — 수 시간이 아닌 **수일~1주일** 단위 실행 가능
  - 실행 중 상태 지속성(Persistence) 보장

### ⚙️ Optimize — 에이전트 평가 (신규 필러)
- 최적화 필러 전체가 **완전 신규** 도입
- 토큰 최적화 등 다양한 차원의 에이전트 성능 평가 기능 포함 (상세 내용은 추가 발표 예정)

---

## 💡 개발자 포인트

> **Breaking Concept**: 기존에는 Identity, Memory, Governance를 각각 별도 서비스를 엮어서 구현해야 했으나, **Agent Platform**이 이를 통합 제공 — 직접 구현 코드 대폭 감소 예상

- `ADK`의 **거버넌스 기능은 ADK 자체가 아닌 별도 플랫폼 레이어**임을 명심할 것
  - `ADK` = 빌드 프레임워크 / Govern 기능 = Agent Platform 상위 레이어
- **Agent Identity**는 토큰 재사용·공유 방식 대신 **암호학적 크리덴셜** 방식으로 전환
  - 기존에 임시 토큰이나 계정 공유로 에이전트 인증을 처리했다면 마이그레이션 검토 필요
- **Memory Bank**는 자체 메모리 솔루션 구축을 위한 **Lego 블록**처럼 활용 가능
  - 커스텀 메모리 솔루션의 기반 레이어로도 사용 권장
- **Long-running Agent** 사용 시 중간 상태 유실 방지를 위해 **Persistence 설계를 반드시 고려**

---

## 📅 버전 / 출시 일정

| 기능 | 상태 | 비고 |
|------|------|------|
| `ADK` (Python/Go/TypeScript/Java) | **GA** | 전년도 Next에서 최초 발표 |
| **Memory Bank** | **GA** | 약 6개월 전 롤아웃 후 GA |
| **Long-running Agent** | **GA** | Gemini Enterprise에서 사용 가능 |
| **Agent Identity / Registry / Gateway** | **신규 발표** | 출시 시점 미명시 |
| **Anomaly Detection** | **신규 발표** | 출시 시점 미명시 |
| **Optimize 필러** | **신규 발표** | 상세 스펙 추가 공개 예정 |

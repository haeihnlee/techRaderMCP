# Google Cloud Next '26 Developer Keynote recap

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=o9es-h7SMPQ
- **요약 일시**: 2026-05-14 09:04:35

---

## 🔑 핵심 요약
- **Google Cloud Next '26** Developer Keynote 회고 영상으로, **AI 에이전트 개발 생태계**의 가속화가 핵심 메시지
- **`ADK`(Agent Development Kit)**, **`MCP` 서버**, **스킬(Skills) 레포지토리**, **에이전트 옵저버빌리티** 등 에이전트 빌더 도구가 대거 발표
- **GEAR**(Enterprise Agent Ready) 프로그램과 **Builder Hub**, **Google Skills**를 통한 개발자 업스킬링 트랙 확대

---

## 📣 주요 발표 내용
- **`ADK`(Agent Development Kit)**
  - **Python, JavaScript** 등 다국어 지원 — "5줄 코드"로 에이전트 시작 가능
  - **`Agent Engine`** 및 **Gemini Enterprise Agent Platform**과 긴밀 통합

- **멀티 에이전트 오케스트레이션 & 거버넌스**
  - 대규모 조직에서 신뢰 가능한 에이전트 운영을 위한 **거버넌스 / 보안 / 인프라** 지원
  - 비즈니스 파트너가 코드 빌딩에 참여 가능한 **Gemini Enterprise** 환경

- **Skills 레포지토리**
  - 필요한 순간에 지식을 주입해 **토큰 최적화 & 컨텍스트 효율화**
  - 에이전트 성능 튜닝의 새로운 표준 도구로 강조

- **에이전트 옵저버빌리티**
  - 에이전트 동작 디버깅 / 트레이싱을 위한 신규 도구
  - 기존의 불투명한 디버깅 경험을 개선

- **`MCP` 서버 for Google Cloud**
  - Google Cloud용 **`MCP` 서버**가 박스 형태로 제공 — 즉시 활용 가능

- **GEAR (Enterprise Agent Ready)**
  - 새로운 **러닝 패스 2종** 추가, **Google Skills**와 통합
  - 매월 **35 크레딧** 제공, 연중 신규 콘텐츠 지속 추가

---

## 💡 개발자 포인트
- **어디서부터 시작할까?** → **`ADK`** 로 시작하는 것이 권장됨. 이후 `Agent Engine`, Gemini Enterprise로 자연스럽게 확장 가능
- **자바스크립트 개발자도 환영** — Python 외 다양한 언어 지원으로 "Meet you where you are" 기조

> ⚠️ **토큰 비용 최적화가 핵심 이슈로 부상** — 단순 RAG 대신 **Skills**를 통해 필요한 시점에만 지식 주입하는 패턴이 표준화되는 흐름. 컨텍스트 비대화로 인한 비용 폭증을 막으려면 새 아키텍처 학습 필수.

- **에이전트 디버깅이 진짜 가능한 시대** — 옵저버빌리티 도구를 적극 활용해 블랙박스 문제 해결
- **노코드 ↔ 하이코드 협업** — 비개발 직군이 같이 빌딩에 참여하는 워크플로우 설계가 새로운 시도 영역
- **커뮤니티 활용** — **GDG**, **DevFest**, **Google Developer Program**, **GDE** 등 로컬/온라인 채널에서 다양한 핸즈온 가능

---

## 📅 버전 / 출시 일정
| 항목 | 상태 / 일정 |
|------|-----------|
| `ADK` (Agent Development Kit) | 일반 사용 가능, Python + JavaScript 등 다국어 |
| `MCP` server for Google Cloud | Google Cloud에 기본 제공 |
| GEAR 학습 패스 2종 추가 | Google Cloud Next '26 시점에 공개 |
| Google Skills 월 크레딧 | 매월 **35 크레딧** |
| GEAR 신규 콘텐츠 | 2026년 연중 지속 추가 |


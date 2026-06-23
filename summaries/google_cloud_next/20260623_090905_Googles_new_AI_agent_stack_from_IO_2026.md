# Google's new AI agent stack from I/O 2026

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=pg6TOXyiIuo
- **요약 일시**: 2026-06-23 09:09:05

---

## 🔑 핵심 요약
- Google이 **에이전트 스택을 4단계 "사다리"** (Agent Studio → Managed Agents API → Antigravity → ADK 2.0)로 정리, 팀 수준에 맞춰 시작하고 점진적으로 올라갈 수 있게 설계
- 모든 단계는 **Agent-to-Agent(A2A) 프로토콜**을 공통 레일로 사용해 상호 운용 — 특정 단계에 lock-in되지 않음
- 신규 기본 모델 **`Gemini 3.5 Flash`** 출시 — 비용/성능 균형형, 장기 실행(long-horizon) 에이전트 작업에 최적화, 신형 TPU와 공동 설계

---

## 📣 주요 발표 내용
- **에이전트 4단계 사다리 (Rungs)**
  - **Rung 1 — Agent Studio**: 로우코드·UI 기반, 시각적으로 시작 후 코드로 전환 가능
  - **Rung 2 — Managed Agents API**: 단일 API 호출, 완전 호스팅. **설정(configuration) 우선** 접근, 입문자용
  - **Rung 3 — Antigravity 2.0**: 에이전트 우선 개발 플랫폼, 다중 에이전트 오케스트레이션
  - **Rung 4 — `ADK 2.0`**: 풀코드 레벨 제어, **엔지니어링 우선** 접근
- **`ADK 2.0` GA** — 기존 명령형(imperative) 오케스트레이션에서 **그래프 기반(graph-based)** 으로 전환. 결정론(deterministic) ↔ 창의성을 슬라이더로 조절, 수 분~수 시간 장기 작업 지원
- **Agent CLI** (Cloud Next 발표) — 에이전트 스캐폴딩·로컬 실행·eval 작성·배포까지 end-to-end. 배포 타깃은 **Agent Platform**(인프라 관리 불필요, 오토스케일)
- **Skill Registry** — 조직 범위의 **비공개 스킬 저장소**. 스킬은 마크다운 파일(지침+도구). **동적 디스커버리**로 런타임에 필요한 스킬만 로드 → 공유 거버넌스 + 경량 에이전트
- **Gemini Spark** — 24/7 개인 에이전트. 전용 VM·Managed Runtime에서 실행, 폰 잠금 중에도 백그라운드 동작. 작업마다 격리된 ephemeral VM 사용
- **Agent Payments Protocol (AP2)** — 거래용 가드레일. mandate(허용 한도·대상)를 설정하면 에이전트가 그 범위 내에서만 결제 수행
- **Gemini 3.5 Flash** — 신규 기본 모델, 다수 에이전트 벤치마크에서 `Gemini 3.1 Pro` 능가
- **Model Garden** — 실사용 학습이 반영된 에이전트 템플릿 다수 추가
- **Gemini Omni** — 텍스트·이미지·오디오·비디오 등 모든 입력으로 고품질 영상 생성, Gemini의 실세계 추론에 기반

---

## 💡 개발자 포인트
- 진입점은 자유롭게 선택하되 **하나에 종속되지 않는다** — 동일한 A2A 프로토콜·플랫폼이 모든 단계를 관통하므로 팀 성숙도에 맞춰 단계적으로 이동 가능
- **`ADK 2.0`의 그래프 기반 전환**이 가장 큰 변화 — 워크플로를 단계 그래프로 기술하고, 작업 성격에 따라 결정론 vs 창의성을 조절
  > 명령형 → 그래프 기반으로 오케스트레이션 패러다임이 바뀌므로, 기존 ADK 사용자는 마이그레이션 검토 필요
- **Managed Agents API의 핵심은 "managed"** — 샌드박스 프로비저닝·환경 관리 불필요, 상태(파일·state)가 영속되어 후속 호출에서 이어서 작업 가능
- **Skill Registry**로 "스킬 한 번 작성 → 조직 전체 재사용" + 에이전트는 필요 스킬만 온디맨드 로드
- **Antigravity SDK**로 동일 에이전트 하니스를 자체 인프라에 호스팅 가능. Cloud 고객은 Agent Platform 연동 시 **보안 경계 내에서 실행 + 데이터 보호 정책 상속**
- 프로덕션 운영 시 **Agent Identity**(어떤 에이전트가 무엇을 하는지 추적·디버깅)와 **Governance**(blast radius 제한)가 배포 신뢰성의 핵심

---

## 📅 버전 / 출시 일정
| 항목 | 상태 / 버전 | 비고 |
| --- | --- | --- |
| `Gemini 3.5 Flash` | 신규 출시, 새 기본 모델 | `Gemini 3.1 Pro` 대비 에이전트 벤치마크 우위, TPU 공동 설계 |
| `ADK 2.0` | **GA** | 그래프 기반 오케스트레이션 |
| Agent CLI | Cloud Next 발표 | 배포 타깃 = Agent Platform |
| Antigravity | 2.0 (Desktop / CLI / SDK) | 에이전트 우선 개발 플랫폼 |
| Managed Agents API | 발표 | 단일 호출, 완전 호스팅 |
| Gemini Spark | 신규 | 24/7 개인 에이전트 |
| AP2 (Agent Payments Protocol) | 발표 | 결제 가드레일 |
| Gemini Omni | 신규 | 멀티모달 입력 → 영상 생성 |


# Is it possible to fix K8s degradation in one click with Gemini Cloud Assist?

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=6Ez2VII8V00
- **요약 일시**: 2026-07-10 09:07:34

---

## 🔑 핵심 요약
- **Palo Alto Networks**(Prisma Access) SRE 팀이 **GCP 관측성 도구**와 **Gemini Cloud Assist**로 이슈를 고객보다 먼저 감지·해결하는 사례 인터뷰
- 자체 **AIOps** 프레임워크를 `BigQuery` 기반으로 구축해 상관관계(correlation) 분석으로 장애를 빠르게 식별
- **Gemini Cloud Assist** 에이전트로 **Kubernetes 클러스터 과부하/성능 저하**를 감지하고, 제안된 조치를 **클릭 한 번으로 원격 조치(remediation)** 가능

---

## 📣 주요 발표 내용
- Prisma Access는 글로벌 VPN 솔루션으로 **파이브나인(5-nines) 수준 SLA**를 제공 — SRE 팀이 사전 감지(proactive detection)에 집중
- 자체 **AIOps** 도구: `BigQuery` 위에서 상관관계 로직을 돌려 특정 고객(군)에 영향 주는 이슈를 조기 식별 후 인시던트 관리 사이클로 연결
- **에이전틱(agentic) 전환**: GCP가 제공하는 **MCP 게이트웨이**와 통신하는 에이전트를 구축, 이슈 삼각측량(triangulation)을 에이전트가 대신 수행
- 에이전트는 **Gemini Enterprise Agent 플랫폼**에서 호스팅, **Gemini Cloud Assist**의 심층 조사(deep investigation)·사전 알림(proactive alerting) 기능 활용

---

## 💡 개발자 포인트
- **MTTD/MTTR**(평균 감지/복구 시간) 단축이 에이전트 도입의 핵심 성공 지표 — SRE 자동화 도입 시 참고할 만한 측정 기준
- K8s 서비스 저하 시 **Cloud Assist**가 원인 분석 + 조치 제안까지 제공하므로, 수동 런북 기반 대응을 에이전트 기반으로 대체하는 아키텍처 방향성 제시
- 관측성 데이터(로그·메트릭)를 `BigQuery`로 모아 AI 상관분석을 돌리는 패턴은 자체 AIOps 구축 시 재현 가능한 구조

> 인터뷰 형식 세션으로 구체적인 API/설정 방법은 다루지 않음 — 실제 적용은 **Gemini Cloud Assist** 공식 문서 확인 필요

---

## 📅 버전 / 출시 일정
해당 없음

# Inside Google's new AI hardware

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=jb-td2mspPE
- **요약 일시**: 2026-07-09 09:04:21

---

## 🔑 핵심 요약
- **Ironwood**(7세대 TPU)로 대규모 학습을 지원하며 최대 **100만 개 TPU**까지 확장 가능
- **Google Axion**(Arm 기반 커스텀 칩)으로 DB·웹서버 등 표준 컴퓨트 워크로드의 비용 효율을 개선
- **Physical AI**(로봇 시뮬레이션 학습)와 **Google Distributed Cloud**(온프레미스 Gemini)로 엣지·규제 환경까지 AI 인프라 커버

---

## 📣 주요 발표 내용
- **Ironwood (TPU v7)**: 랙 1개(큐브) 기준 최대 `9,216`개 칩, 랙 `144`개로 pod 1개 구성. Pod 간에도 확장해 최대 **100만 TPU**까지 단일 학습 워크로드 지원
- 칩 간 연결에 **ICI**(Inter-Chip Interconnect) 사용 — 고속·저지연 연결로 대규모 학습 속도 확보
- **Google Axion**: Arm 기반 프로세서 라인업
  - `N4A`: 비용에 민감한(cost-sensitive) 워크로드용
  - `C4A`: 성능 중심(performance-effective) 워크로드용
- **Physical AI**: 창고·물류·제조 현장의 로봇 자동화를 위해, `G4` 인스턴스 + **NVIDIA RTX** GPU로 클라우드 상에서 대규모 병렬 시뮬레이션 학습을 수행한 뒤, 학습된 모델을 Google Distributed Cloud를 통해 엣지(로봇)로 배포
- **Google Distributed Cloud + Gemini**: 이번 행사에서 온프레미스에서 Gemini를 구동하는 Google Distributed Cloud를 발표. **NVIDIA B300(Blackwell)** 시스템을 지원하며 컴퓨트·네트워킹·스토리지를 포함한 풀스택 구성 제공

---

## 💡 개발자 포인트
- 대규모 모델 학습이 필요하다면 Ironwood TPU pod 단위(최대 9,216칩) 확장성을 염두에 두고 아키텍처 설계 가능
- 일반적인 백엔드/DB 워크로드는 Axion(`N4A`/`C4A`)으로 비용 대비 성능 최적화 검토 가치 있음
- 로봇·엣지 AI를 다룬다면 시뮬레이션 학습(클라우드) → 엣지 배포(Distributed Cloud) 파이프라인 구조를 참고할 만함

> 규제·데이터 주권 요구사항으로 클라우드 사용이 어려운 경우, **데이터가 사이트를 벗어나지 않는** Google Distributed Cloud + Gemini 온프레미스 조합이 대안이 될 수 있음

---

## 📅 버전 / 출시 일정
해당 없음 (구체적 출시일 미언급, 컨퍼런스 발표 시점 기준 신규 공개 내용)

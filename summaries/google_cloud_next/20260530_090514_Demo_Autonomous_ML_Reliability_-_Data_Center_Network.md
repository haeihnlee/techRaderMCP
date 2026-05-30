# [Demo] Autonomous ML Reliability - Data Center Network

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=0yKGILWlngY
- **요약 일시**: 2026-05-30 09:05:14

---

## 🔑 핵심 요약
- **에이전트(agent) 기반**으로 Google Cloud 상의 **ML 학습 워크로드 신뢰성**을 자동 관리하는 데모
- 학습 작업의 **성능 이상(straggler·hang)** 을 에이전트가 자동 탐지·진단하고, **문제 인스턴스를 정확히 지목(localization)**
- 결함 인스턴스 격리 → **최신 체크포인트(checkpoint)에서 재시작** 까지 완화 단계를 자동 제안, 성능을 baseline으로 복구

---

## 📣 주요 발표 내용
- **활성 학습 워크로드 모니터링**을 에이전트에게 지시하면 학습 **throughput** 안정성을 실시간 추적
- 두 작업에서 성능 저하 발생 — 한 작업은 **straggler**(느려짐), 다른 작업은 **hang**(멈춤) 으로 에이전트가 이상 유형을 정확히 분류
- **localization** 단계에서 straggler·stall을 유발한 **특정 인스턴스(root cause)** 를 정확히 식별
- 에이전트가 완화 절차까지 제시 → 결함 인스턴스 격리(outcast) 후 **최신 checkpoint 재시작**
- 복구 후 다시 모니터링을 지시, 성능이 **baseline 수준으로 회복**됨을 확인

---

## 💡 개발자 포인트
- 대규모 ML 학습에서 빈번한 **straggler / hang** 장애를 사람이 수동으로 디버깅하지 않고 **에이전트가 탐지→진단→완화**까지 자동 수행
- 핵심은 **인스턴스 단위 root cause localization** — 어떤 노드가 병목·정지의 원인인지 자동 지목해 복구 시간을 단축
> 결함 인스턴스를 격리한 뒤에는 처음부터가 아니라 **최신 checkpoint**에서 재시작하므로 학습 진행분 손실을 최소화하는 설계가 전제

---

## 📅 버전 / 출시 일정
해당 없음


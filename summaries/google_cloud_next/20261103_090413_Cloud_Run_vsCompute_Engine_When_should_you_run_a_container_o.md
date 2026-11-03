# Cloud Run vs.Compute Engine: When should you run a container on serverless vs. managing a full VM?

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=yJ3U4TJqya0
- **요약 일시**: 2026-11-03 09:04:13

---

## 🔑 핵심 요약
- **Cloud Run**과 **Compute Engine(VM)**의 차이는 우열이 아니라 **통제권 vs 편리함**의 트레이드오프
- 머신 자체(GPU, OS 제어, 상시 실행)가 필요하면 **VM**, 코드만 실행하면 되면 **Cloud Run**
- 실제 시스템에서는 API는 Cloud Run, GPU 작업은 VM처럼 **두 가지를 혼용**하는 경우가 많음

---

## 📣 주요 발표 내용
- **Compute Engine(VM)**: 클라우드에서 컴퓨터 한 대를 통째로 빌리는 개념
- VM은 크기 선택·소프트웨어 설치가 자유롭고, 트래픽 유무와 관계없이 **24시간 실행**됨
- VM은 패치·보안 유지 등 **운영 책임이 사용자에게** 있음
- **Cloud Run**: 컨테이너 이미지를 넘기면 플랫폼이 실행을 관리하는 서버리스 방식
- Cloud Run은 트래픽 급증 시 **복제본(인스턴스)을 자동 추가**
- 요청이 없으면 **0으로 스케일 다운(scale to zero)** → 유휴 시간 비용 없음

---

## 💡 개발자 포인트
- **VM을 선택할 때**
  - 학습용 **GPU**가 필요한 경우
  - 하루 종일 돌아가는 **백그라운드 작업**
  - 특수 소프트웨어 설치 또는 **OS 완전 제어**가 필요한 경우
  - 항상 실행되어야 하는 워크로드 (상시 가동 VM이 더 저렴할 수 있음)
- **Cloud Run을 선택할 때**
  - **웹 앱 / API** 배포
  - 트래픽이 들쭉날쭉하거나 예측하기 어려운 경우
  - 서버 관리 없이 "그냥 동작"하기를 원하는 경우
- 하이브리드 구성 예: API 레이어는 Cloud Run, GPU·배치 작업은 Compute Engine

> 주의: 상시 트래픽이 꾸준한 워크로드는 Cloud Run의 scale-to-zero 이점이 사라지므로, 비용 측면에서 VM이 더 유리할 수 있음

| 항목 | Compute Engine (VM) | Cloud Run |
|---|---|---|
| 통제권 | 머신·OS 전체 | 컨테이너 수준 |
| 운영 부담 | 패치·보안 직접 관리 | 거의 없음 |
| 스케일링 | 수동/직접 구성 | 자동 (0까지 축소) |
| 유휴 비용 | 24시간 과금 | 없음 |
| 적합 워크로드 | GPU, 상시 백그라운드, 특수 SW | 웹 앱, API, 변동 트래픽 |

---

## 📅 버전 / 출시 일정
해당 없음


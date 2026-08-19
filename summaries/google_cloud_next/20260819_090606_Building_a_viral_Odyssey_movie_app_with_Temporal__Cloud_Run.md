# Building a viral Odyssey movie app with Temporal & Cloud Run

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=1LInqYY2m9Y
- **요약 일시**: 2026-08-19 09:06:06

---

## 🔑 핵심 요약
- **Temporal**의 Durable Execution으로 크래시-프루프 워크플로우 구현 — 장애 발생 시 자동 재개
- **IMAXing** 서비스: 미국 전역 IMAX 좌석 공석 알림, 8,000+ 구독자 확보한 바이럴 사이드 프로젝트
- Temporal 워커를 **Cloud Run 서버리스**로 실행하는 신규 기능 (알파 출시 단계)

---

## 📣 주요 발표 내용
- **Temporal** 오픈소스 개발자 플랫폼: 워크플로우의 핵심 전환점마다 내구성(Durability) 보장
  - 인프라 장애·네트워크 오류 등 예기치 못한 실패 시 자동 복구
  - `Signal` 기반 워크플로우 간 통신: 극장 모니터링 → 구독 워크플로우로 알림 전달
  - 알림 중복 방지를 위한 1분 타이머 집계 로직 내장
- **Cloud Run + Temporal 서버리스 워커** 통합 (신규):
  - 기존: 상시 실행 프로세스 → 스파이크 대비 오버프로비저닝 필요
  - 신규: Temporal 사용량 기반으로 자동 스케일업/다운
- **Entity Workflows 패턴**: 구독 1건 = 워크플로우 1개, 수천 개 동시 운영
- AI 코딩 에이전트를 활용해 Terraform 및 `gcloud` CLI 인프라 배포 자동화

---

## 💡 개발자 포인트
- Temporal의 `Signal`을 활용하면 외부 이벤트로 슬리핑 워크플로우를 깨울 수 있음
- 서버리스 Temporal 워커는 CPU 사용률이 아닌 **Temporal 큐 깊이** 기반으로 스케일링 → 정밀한 오토스케일링

> **주의**: Temporal 서버리스 Cloud Run 워커는 2026년 현재 알파 단계로 전 계정 미배포 상태.
> 일반 사용자는 still uses 기존 상시 워커 방식을 사용해야 함.

- **비용 참고**: 미국 전역 IMAX 모니터링(~9개 워커 노드) 기준 월 $200 수준
- **Grafana** + **GCP** 조합으로 Temporal 워크플로우 메트릭 시각화

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| Temporal Cloud Run 서버리스 워커 | 2026년 8월 알파 출시 시작 |
| IMAXing 서비스 구독자 | 8,000명+ (2026년 8월 기준) |
| 운영 비용 | 월 ~$200 (9개 워커 노드) |

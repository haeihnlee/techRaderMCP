# Preview: building a viral movie app with Temporal & Cloud Run

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=eeRnNHjpHQk
- **요약 일시**: 2026-08-20 09:06:26

---

## 🔑 핵심 요약
- **IMAXing**: 전국 IMAX 상영 좌석을 모니터링해 빈 자리가 생기면 알려주는 바이럴 사이트
- **Temporal** + **Google Cloud Run** 조합으로 구현, 사전 공개(pre-release) Temporal 서버리스 워커 사용
- The Odyssey 70mm IMAX 티켓 15만 명 동시 구매로 화제가 된 이벤트에서 착안

---

## 📣 주요 발표 내용
- 개발자 Andrew가 직접 제작한 사이드 프로젝트 **IMAXing** 소개
- 미국 전역 IMAX 상영관의 좌석 현황을 실시간으로 추적
- 좌석이 열리면 알림을 제공하는 모니터링 서비스
- **Temporal 서버리스 워커** (pre-release) + **Cloud Run** 배포 아키텍처

---

## 💡 개발자 포인트
- **Temporal 서버리스 워커**는 현재 pre-release 단계로, 일반 Temporal 대비 인프라 관리 부담 감소
- **Cloud Run**과 Temporal을 결합해 이벤트 기반 폴링 작업을 서버리스로 처리
- 짧은 영상(프리뷰)으로 상세 기술 구현은 별도 세션에서 다룰 예정

> 이 영상은 짧은 티저 클립으로, 전체 발표 내용은 temporal.io 또는 cloud.google.com/run 에서 확인 가능

---

## 📅 버전 / 출시 일정
| 항목 | 상태 |
|------|------|
| Temporal 서버리스 워커 | Pre-release (사전 공개) |
| Cloud Run | GA (정식 출시) |


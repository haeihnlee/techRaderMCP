# How to monitor & optimize Google Gemini agents with Grafana Cloud

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=RJSRBzryPQs
- **요약 일시**: 2026-09-04 09:05:45

---

## 🔑 핵심 요약
- **Grafana Cloud**의 AI 관측 가능성 기능으로 **Google Gemini** 기반 에이전트를 프로덕션 환경에서 실시간 모니터링 가능
- `Grafana Sigil SDK`를 사용해 **OpenTelemetry** 기반 계측을 추가하면 모든 도구 호출·결정·응답을 캡처할 수 있으며, 에이전트 로직 변경 없이 래퍼(wrapper)만 추가하면 됨
- 관찰 → 분석 → 개선 → 반복 루프를 **Slack + Grafana 어시스턴트 + Claude**로 자동화 가능

---

## 📣 주요 발표 내용
- **Google Agent Development Kit**으로 구축한 Gemini 기반 금융 비서 에이전트를 시연
- `sigil` 클라이언트 설정: Grafana Cloud 엔드포인트, 인스턴스 ID, API 키 설정 후 `process_query` 블록과 `sigil_client.start_tool_execution()` 래퍼 추가
- **Grafana Cloud AI 관측 대시보드** 주요 메트릭:
  - 요청 수, 오류율, 지연 시간, 첫 번째 토큰까지 걸리는 시간(TTFT)
  - 시간별 토큰 사용량 및 에이전트별 토큰 사용 현황
  - 도구 호출 입출력 값과 소요 시간 추적
- **Evaluations(평가) 기능**: AI 판별기를 설정하여 에이전트 응답 품질 점수화 및 이상 알림 설정 가능
- **Slack 자동화 워크플로우**: Grafana Slack 앱을 추가하면 채널에서 직접 에이전트 분석 및 개선 제안 요청 가능
- Claude와 연동하여 분석 결과 기반 시스템 프롬프트·에이전트 코드 자동 수정 지원

---

## 💡 개발자 포인트
- 로컬 테스트와 달리 프로덕션에서는 수백~수천 명의 동시 요청을 처리해야 하므로 **규모 있는 관측 가능성 레이어**가 필수
- `Sigil SDK` 계측은 기존 에이전트 코드를 변경하지 않고 **래퍼 추가만으로** 구현 가능 — 도입 비용이 낮음
- 실제 운영 중 발견된 이슈 예시: 레이트 리밋 초과, 토큰 급증, `Gemini 2.5 Pro` 지연 시간 발생

> **주의**: 평가(Evaluations) 기능을 통한 품질 모니터링 설정 없이 프로덕션에 배포하면 응답 품질 저하를 사후에 발견하기 어려움

- **관측 → 분석 → 개선 루프 자동화 아키텍처**:
  1. `Sigil` (OpenTelemetry 레이어) → 텔레메트리 전송
  2. **Grafana Cloud** → 데이터 수집 및 시각화
  3. **Slack Grafana 어시스턴트** → 자동 분석
  4. **Claude / Claude Code** → 코드 수정 및 개선

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 모델 | Gemini 2.5 Pro (시연에 사용) |
| 관측 SDK | Grafana Sigil (OpenTelemetry 기반) |
| 배포 채널 | Google Cloud Marketplace에서 Grafana Cloud 시작 가능 |


# Prevent surprise cloud bills: enforce hard spending caps on Gemini API & Vertex AI

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=yiqabpMJJNE
- **요약 일시**: 2026-09-25 09:06:20

---

## 🔑 핵심 요약
- **Google Cloud** 콘솔에서 **Gemini API / Vertex AI** 등의 서비스에 **지출 한도(Spending Cap)** 를 설정하여 예산 초과 시 앱을 자동으로 차단할 수 있다
- 한도 초과 시 HTTP `403` 상태 코드와 함께 요청이 차단되며, 콘솔에서 즉시 한도를 해제할 수도 있다
- 지출 한도는 **프로젝트 단위**로 적용되므로, 테스트/운영 환경을 별도 프로젝트로 분리하는 것이 권장된다

---

## 📣 주요 발표 내용
- Google Cloud 결제 콘솔 → '예산' 메뉴에 **'지출 한도 적용(Spending Cap)'** 옵션 신규 추가
- 현재 지출 한도를 지원하는 서비스:
  - **Gemini API** (API 키 기반 인증)
  - **Vertex AI** (서비스 계정 기반 인증)
  - **Cloud Run**
  - **Cloud Run Functions**
- 한도에 근접하면 **자동 알림** 발송, 한도 초과 시 앱 요청 자동 차단
- 차단 응답: `HTTP 403` + "프로젝트 지출 한도 초과" 에러 메시지

---

## 💡 개발자 포인트
> **한도 적용까지 몇 분의 지연이 있으므로**, 실제 예산보다 **약간 낮게** 한도를 설정할 것을 권장한다. 그 몇 분 사이에 발생한 비용은 그대로 청구된다.

- `Gemini API` vs `Vertex AI` 구분:
  - `Gemini API` → **API 키** 인증 사용 시
  - `Vertex AI` → **서비스 계정** 인증 사용 시
- 테스트 환경과 프로덕션 환경을 **별도 GCP 프로젝트**로 분리하면, 테스트용 스크립트가 프로덕션 장애를 유발하지 않는다
- 일부 서비스는 한도 도달 전에도 청구 금액이 급격히 증가하면 선제적으로 지출 제한이 발동될 수 있다
- 이 기능은 기존의 '알림(Notification)' 방식과 달리 **실제 트래픽을 강제 차단**하는 선제적 대응 수단이다

---

## 📅 버전 / 출시 일정
해당 없음 (기능은 영상 공개 시점에 이미 Google Cloud 콘솔에 반영됨)


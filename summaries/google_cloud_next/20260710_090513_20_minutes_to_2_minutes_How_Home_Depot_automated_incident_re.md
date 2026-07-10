# 20 minutes to 2 minutes: How Home Depot automated incident responses with OpenTelemetry

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=SpfgNqPIMNI
- **요약 일시**: 2026-07-10 09:05:13

---

## 🔑 핵심 요약
- **Home Depot**이 **AIOps** 도입으로 인시던트 대응 시간을 **20분 → 2분**으로 단축
- `Gemini` 모델을 활용해 **근본 원인 분석(RCA)**, 이슈 요약, 해결 방향 제시를 자동화
- **OpenTelemetry**의 일관된 라벨링 + **Managed Service for Prometheus**로 데이터 일관성을 확보한 것이 LLM 정확도의 핵심 기반

---

## 📣 주요 발표 내용
- **AIOps 패러다임 전환**: 기존에는 알림 발생 시 엔지니어가 대시보드·로그를 직접 분석했지만, 이제 `Gemini`가 **페어 리라이어빌리티 엔지니어**처럼 증상 평가 → 요약 → 근본 원인 → 다음 조치를 제시
- **Managed Service for Prometheus (GMP)**를 SLA 알림 엔진으로 사용, 높은 **카디널리티**를 감당하며 멀티 프로젝트·멀티 스토어 데이터를 한곳에 통합
- **OpenTelemetry**로 시스템 전반에 **일관된 라벨(consistent labels)**을 부여 → AI가 더 많은 컨텍스트로 **상관관계(correlation)** 분석 → 예측·RCA 정확도 향상
- 단순 알림이 아닌 **컨텍스트 알림(context alerting)**: 알림과 함께 시스템 컨텍스트를 제공
- **사용자 경험(UX) 중심 관점**으로 전환: 시스템 지표가 아닌 "사용자가 무엇을 보는가"를 기준으로 리더·개발자·프로덕트·네트워크 팀이 **같은 언어**로 소통

---

## 💡 개발자 포인트
- **오픈 표준(OpenTelemetry) 채택**이 AIOps의 전제 조건: 라벨이 일관돼야 LLM이 데이터를 정확히 상관 분석할 수 있음
- 관측 데이터가 여러 곳에 흩어져 있으면("different dialects") AI 분석 정확도가 떨어짐 → **데이터 통합·일관성 확보가 우선**
- 다음 단계 로드맵: RCA 제공을 넘어 AI가 **자동으로 수정 PR을 생성**하고 개발자가 리뷰하는 구조 지향 (아직 human-in-the-loop 필수)

> 현재 단계에서는 AI가 근본 원인 분석까지만 담당하며, 실제 수정·배포 판단은 여전히 사람이 검증해야 함 (deterministic한 자동 수정은 "step two")

---

## 📅 버전 / 출시 일정
해당 없음

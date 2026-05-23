# Moving AI agents beyond "Hello World" to real production

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=DVyRuMbtrmc
- **요약 일시**: 2026-05-23 09:13:27

---

## 🔑 핵심 요약
- AI 에이전트 개발의 화두는 더 이상 'vibe coding'이 아니라 **프로덕션 운영(Day 2)** 단계로 이동 중
- **Google Cloud MCP 서버**를 통해 로컬 에이전트가 로그·메트릭·서비스 정보를 안전하게 통합 조회 가능
- 자연어 프롬프트 하나(`"find out what's wrong with my Dino quest app"`)만으로 근본 원인 분석부터 BigQuery 분석까지 자동화

---

## 📣 주요 발표 내용
- **Day 2 운영의 어려움**: 배포는 쉬워졌지만, 로그 분석·성능 튜닝·장애 대응 등 운영 단계가 여전히 가장 까다로움
- **MCP(Model Context Protocol) 기반 운영 자동화**
  - `Anti-gravity` IDE + **Google Managed MCP** 조합으로 클릭 몇 번에 Cloud 리소스 연결
  - 단일 에이전트가 `Cloud Run` 서비스 탐색 → 로그 수집 → 에러 분석을 일괄 수행
- **다중 증상(Multi-symptom) 분석**: 첫 번째 증상에 매몰되지 않고 여러 증상을 종합해 **root cause** 도출
- **코드 ↔ 운영 데이터 연결**: SRE와 개발자 사이의 경계를 허물어, 에이전트가 코드와 프로덕션 메트릭을 함께 분석
- **데이터 에이전트 툴킷**: 과거에는 ETL 파이프라인 작성 → BigQuery 적재 → SQL 분석이 필요했던 작업을 에이전트가 7~8개 쿼리를 알아서 실행
- **프로액티브 모니터링**: CPU 급등 등 이상 징후 발생 시 `Slack` 알림 자동 발송

---

## 💡 개발자 포인트
- **자연어 디버깅의 한계 인지 필요**: 서비스 이름이 프롬프트와 맞아야 에이전트가 정확히 찾아냄 (예: 앱 이름 `Dino quest` ↔ 서비스명 `dinosaur`)
- **Streaming Log → BigQuery 파이프라인**을 에이전트가 자동 구성 → BigQuery 내부 구조를 몰라도 운영 분석 가능

> ⚠️ 에이전트가 "성공"이라 보고해도 보안·취약점은 별도로 점검해야 함. **adversarial 프롬프트로 직접 결함을 찾는 습관**이 필수

- 도메인 지식이 있는 사용자는 **context를 명시적으로 주입**해 에이전트의 분석 품질을 끌어올리는 것이 효과적
- SRE 영역의 진입 장벽(Console 탐색, SQL 작성)이 크게 낮아져, 개발자도 운영을 직접 다룰 수 있는 흐름

---

## 📅 버전 / 출시 일정
해당 없음 (컨셉·시연 중심 키노트 대담)


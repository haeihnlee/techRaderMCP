# From systems of intelligence to systems of action: Yasmeen Ahmad on the agentic data cloud

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=WQIODOuXWr8
- **요약 일시**: 2026-05-15 09:07:12

---

## 🔑 핵심 요약
- **System of Intelligence → System of Action**: 대시보드·예측 모델로 멈추던 데이터 활용이 **agentic 시스템**을 통해 실제 비즈니스 액션(원장·운영·마케팅 시스템 자동 호출)까지 이어짐
- AI-ready 데이터의 핵심은 깨끗한 데이터(50%) + **컨텍스트/의미(나머지 50%)**. `Knowledge Catalog`가 정형·비정형 데이터의 **inferred schema/meaning**을 자동 생성해 에이전트가 사용
- `Gemini Enterprise`가 데이터의 단일 **front door**가 되어 `BigQuery`·`AlloyDB`·`Looker`의 대화형 에이전트와 `Deep Research` 에이전트를 통합 제공

---

## 📣 주요 발표 내용
- **Agentic Data Cloud** 비전: 데이터를 단순 저장 대상이 아닌 **추론 루프 안에서 실시간으로 활성화**되는 자산으로 전환
- **Knowledge Catalog 강화**
  - GenAI가 컬럼/테이블/역할 설명을 사람보다 정확히 자동 추론
  - 비정형 PDF 수천 건에 대해 **inferred schema·관계**를 생성 (1,000 PDF를 컨텍스트 윈도우에 못 넣는 비용·물리 한계 해결)
- **Gemini Enterprise 통합 (내년 확대)**
  - `BigQuery`/`AlloyDB`/`Looker`에서 만든 **대화형 에이전트**를 Gemini Enterprise에 게시
  - **Deep Research 에이전트 ↔ Knowledge Catalog 연동**: 웹 데이터 + 문서 + 엔터프라이즈 데이터를 함께 추론 (예: 날씨/교통 + 배송 데이터 → 실시간 배송 최적화)
- **Data Agent Kit** 출시 (Next에서 발표)
  - 에이전트용 plugins / extensions / tools / skills 모음
  - `BigQuery` 파이프라인 빌드·최적화, `Spark` 파이프라인 fine-tune 등을 네이티브 지원
- **Intent-driven Engineering**: persona 기반(데이터 사이언티스트 전용/엔지니어 전용) 에이전트에서 벗어나, 한 에이전트가 데이터 수집→가공→모델링→시각화→앱 배포까지 **end-to-end 수행**
- **Cross-Cloud Lakehouse**
  - `Cross Cloud Interconnect` + intelligent buffer/caching으로 AWS·Azure 데이터를 **이동 없이** 조회
  - `Databricks Unity Catalog`, `Snowflake Polaris`, `AWS S3 Glue`까지 연결
  - **Apache Iceberg**가 핵심 포맷 표준화 역할

---

## 💡 개발자 포인트
- 데이터 거버넌스 작업의 패러다임 전환: 컬럼 설명·business glossary를 사람이 채우던 작업이 **GenAI 자동 추론**으로 대체됨 → 데이터 카탈로그 운영 비용·정확도 모두 개선
- 비정형 데이터(PDF·문서)도 이제 **schema-less 그대로 두지 말고** Knowledge Catalog에 올려 inferred schema를 활용하는 것이 표준 패턴

> ⚠️ **컨텍스트 윈도우에 raw 문서를 다 넣는 RAG 패턴은 비용·정확도 한계 명확**. inferred schema 기반 카탈로그 → 필요한 데이터만 선별 호출하는 구조로 가야 함

- 단일 monolithic 에이전트가 아닌 **agent swarm** 설계가 새 표준. 페르소나 고정 대신 **tool/skill 주입**으로 범용 에이전트화
- 멀티클라우드 전략: 데이터를 GCP로 옮기지 않고 **`Iceberg` + Cross-Cloud Interconnect**로 in-place 쿼리 가능 → 마이그레이션 비용/락인 회피
- `Gemini Enterprise`를 **사내 데이터 챗 인터페이스의 front door**로 두고, 백엔드는 BigQuery/AlloyDB/Looker 에이전트로 분리하는 아키텍처 권장

---

## 📅 버전 / 출시 일정
| 항목 | 시점 |
|------|------|
| Data Agent Kit | Google Cloud Next에서 발표 (현재 이용 가능) |
| Deep Research × Knowledge Catalog 연동 | 발표 시점 제공 |
| BigQuery / AlloyDB / Looker 대화형 에이전트의 Gemini Enterprise 게시 통합 확대 | **2027년 (next year)** 예정 |
| Cross-Cloud Lakehouse (Iceberg 기반 AWS/Azure/Databricks/Snowflake 연결) | 현재 이용 가능 |


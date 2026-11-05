# Trusted agents, real outcomes: Driving AI impact at scale with Google's Agentic Data Cloud

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=Px17s40VY34
- **요약 일시**: 2026-11-05 09:06:29

---

## 🔑 핵심 요약
- Google Data Cloud VP/GM Andy Gutmans가 **에이전트형 데이터 클라우드(Agentic Data Cloud)** 를 발표함. 사람이 물어볼 때까지 기다리는 **"지능형 시스템"** 에서, 에이전트가 직접 실행하는 **"행동 시스템"** 으로 옮겨 가는 것이 목표임
- 레거시 1세대 레이크하우스가 에이전트 규모에서 무너지는 원인으로 세 가지를 꼽음: **폐쇄형 사일로**, **신뢰 격차**(맥락 부족), **비용 나선**
- 이를 해결하는 축은 네 가지임: `Apache Iceberg` 기반 **경계 없는 레이크하우스**, `BigQuery`·`AlloyDB`·`Spanner` 엔진의 **에이전트 규모 탄력성**, **Knowledge Catalog** 의 맥락 계층, Gemini 플러그인과 `Data Agent Kit`(MCP) 기반의 **에이전트 우선 실무 경험**

---

## 📣 주요 발표 내용
- **경계 없는 레이크하우스 (Apache Iceberg 기반)**
  - Gemini가 레이크하우스에서 직접 동작함. 여러 클라우드에 걸친 레코드를 자연어로 쿼리할 수 있음
  - **AWS·Azure 교차 클라우드 인터커넥트 + 캐싱** 정식 출시(GA). 비공개 보안 연결을 쓰며, 가변 데이터 전송 비용이 없음
  - 비정형 데이터(Cloud Storage)까지 자동으로 인덱싱하는 **Knowledge Catalog** 와 직접 통합됨
- **AlloyDB → Iceberg 직접 액세스**
  - ETL이나 데이터 복사 없이 Cloud Storage의 Iceberg 테이블을 쿼리함
  - **단일 Postgres 쿼리**로 실시간 운영 데이터와 과거 레이크하우스 데이터를 함께 조회함
  - 레이크하우스 런타임 카탈로그와 통합됨. Iceberg 테이블을 AlloyDB 테이블과 같이 등록할 수 있음
- **BigQuery 엔진 개선**
  - `BigQuery Graph` GA: ETL 없이 관계형 테이블 위에서 페타바이트급 그래프 분석(노드/엣지 모델링)을 수행함
  - `TimesFM 3.0`(프리뷰): Google Research의 다변량 시계열 예측 파운데이션 모델. **SQL에서 바로** 예측함
  - `TabFM`(프리뷰): 제로샷 표 형식 예측 ML 모델. 특성 공학, 하이퍼파라미터 튜닝, 커스텀 학습이 필요 없음
  - **유연한 확장(flexible scaling)**: 최소 사용량 없이 **초 단위 과금**, 자동 확장 워크로드 비용을 평균 최대 34% 절감함
- **Managed Service for Apache Spark**
  - **Lightning Engine** 이 기본으로 켜져 있음. 오픈소스 Spark보다 약 5배 빠름
  - 더 빠른 시작을 추가 비용 없이 제공함. 워크로드 긴급도에 맞추는 **성능 최적화 모드**가 추가됨
- **운영 DB의 "백만 에이전트" 대응**
  - **AlloyDB의 에이전트용 Postgres**: 리더 노드를 수 초 안에 프로비저닝하고, 수요가 줄면 **0으로 스케일**함
  - **Spanner/Bigtable Data Boost**: 독립적인 서버리스 컴퓨팅으로 스토리지를 직접 읽음. 트랜잭션 SLA에 영향 없이 워크로드가 격리됨
  - `AlloyDB Express`(프리뷰): 개발자와 코딩 에이전트용. 2초 미만 프로비저닝, 0까지 일시 중지, Private IP, 1~2 vCPU / 20GB 구성
  - `Spanner Omni` GA: Spanner를 클라우드, 온프레미스, 노트북 등 어디서든 실행함
- **Knowledge Catalog**
  - 운영 DB, 분석 데이터, 타사 카탈로그, 비정형 문서, SaaS(SAP, Workday)에서 메타데이터와 의미적 맥락을 자율적으로 집계함
  - 검색할 때 **보안 권한**을 적용해 승인된 정보만 반환함
  - 새 **Studio 환경**: AI 받은 편지함으로 에이전트가 보는 맥락을 탐색하고, 공백을 찾고, 보강 제안을 검토함. 신뢰도 임계값, 자동 회귀 테스트, **Git 버전 롤백**을 지원함
- **에이전트 우선 실무 경험**
  - Gemini 데이터 과학·엔지니어링 플러그인: 원하는 결과만 설명하면 PySpark 생성, 노트북 제공, 모델 학습, 자체 문제 해결까지 처리함
  - Gemini 운영 보고·분석 플러그인: Knowledge Catalog로 **검증된 쿼리를 재사용**함. Looker·Tableau·Power BI 네이티브 커넥터로 라이브 인터랙티브 대시보드를 지원함
  - `Data Agent Kit` GA: VS Code, Cloud Code, Antigravity 같은 IDE와 CLI에 Google Data Cloud 도구를 **네이티브 MCP 도구**로 통합함

---

## 💡 개발자 포인트
- 에이전트 정확도는 **모델보다 맥락**이 좌우함. 자체 벤치마크에서 Knowledge Catalog 기반 에이전트는 정확도가 약 4배 높았음. 맥락 계층부터 설계하는 것이 좋음
- **OLTP + 레이크하우스 조인**: AlloyDB에서 Iceberg를 직접 쿼리하면 운영 데이터와 이력 데이터 사이의 ETL 파이프라인을 줄일 수 있음
- 에이전트 트래픽은 **급격하고 일시적**임. 핵심 트랜잭션 DB가 자원 경쟁을 겪지 않도록 읽기 워크로드를 격리해야 함 (`Data Boost`, AlloyDB 리더 노드 자동 프로비저닝 등)
- 코딩 에이전트 테스트용 DB는 `AlloyDB Express` 처럼 **빠른 프로비저닝 + scale-to-zero** 환경이 비용 면에서 유리함
- ML 파이프라인 없이 **SQL만으로** 시계열 예측(`TimesFM 3.0`)과 표 형식 예측(`TabFM`)을 할 수 있음. 프로토타이핑 비용이 크게 줄어듦
- BI 쪽은 **지표 모델을 한 번 정의**하고 에이전트가 이를 검증된 SQL로 바꾸는 패턴이 효과적임 (PayPal: Looker MCP 서버 + AI 에이전트)
- Knowledge Catalog의 회귀 테스트와 Git 롤백은 **맥락 자체를 코드처럼 버전 관리**하는 운영 방식을 시사함

> ⚠️ 주의: 원본 자막이 12,000자에서 잘려, 후반부 데모(재난 대응 시나리오)와 Yahoo 사례, Q&A 내용은 이 요약에 없음
>
> ⚠️ 주의: 일부 수치(100배, 4배, 75% 등)는 Google 자체 벤치마크·발표 기준임

---

## 📅 버전 / 출시 일정

| 항목 | 상태 |
| --- | --- |
| AWS·Azure 교차 클라우드 인터커넥트 + 캐싱 | GA |
| AlloyDB Iceberg 직접 액세스 | 발표 (상태 미기재) |
| `BigQuery Graph` | GA |
| `TimesFM 3.0` (BigQuery) | 프리뷰 |
| `TabFM` (BigQuery) | 프리뷰 |
| BigQuery 유연한 확장 | 발표 |
| AlloyDB 에이전트용 Postgres | 최근 발표 |
| `AlloyDB Express` | 프리뷰 |
| `Spanner Omni` | GA |
| Knowledge Catalog Studio | 발표 |
| `Data Agent Kit` | GA |

| 주요 수치 | 값 |
| --- | --- |
| BigQuery·AlloyDB AI 기능 속도/비용 | 최대 100배 빠르고 저렴 |
| Iceberg 관리 데이터 규모 (1년) | 3배 이상 증가 |
| BigQuery 쿼리 속도 / 처리 비용 (1년) | +35% 이상 / -40% 이상 |
| Lightning Engine vs 오픈소스 Spark | 약 5배 빠름 |
| Spark 가격 대비 성능 우위 | 주요 대안 대비 3배 이상 |
| BigQuery 유연한 확장 비용 절감 | 평균 최대 34% |
| Knowledge Catalog 효과 | 정확도 약 4배, 지연 -33%, 토큰 -75% |
| Virgin Voyages | 에이전트 1,000개 이상, 매출 +28%, 일정 조정 6시간 → 11분 |
| PayPal (Looker MCP) | 인사이트 속도 +50%, 직원 5,000명, 정확도 거의 100% |
| UKG People Fabric (AlloyDB) | 1,000개 이상 조직 사용 |


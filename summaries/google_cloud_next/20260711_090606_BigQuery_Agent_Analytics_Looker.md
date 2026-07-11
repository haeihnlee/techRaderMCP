# BigQuery Agent Analytics Looker

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=hZ6vAiJlqWs
- **요약 일시**: 2026-07-11 09:06:06

---

## 🔑 핵심 요약
- **Looker**가 에이전트의 텔레메트리 데이터를 분석하는 **BigQuery Agent Analytics 블록**을 신규 출시
- **ADK(Agent Development Kit)**나 **LangChain**으로 만든 에이전트의 실행 로그(프롬프트, LLM 요청/응답 등)를 `BigQuery`로 스트리밍하고, `LookML`로 모델링해 대시보드/Explore를 즉시 제공
- 마켓플레이스에서 설치만 하면 코드 작성 없이 바로 대시보드 사용 가능, 필요 시 `LookML`로 커스터마이징도 가능

---

## 📣 주요 발표 내용
- **연동 절차**
  - `BigQuery API` 활성화 후 서비스 계정에 **BigQuery Job User**, **BigQuery Data Editor** 권한 부여
  - `Cloud Project`와 `Dataset ID`를 준비하고, SDK/플러그인 설정에 명시
  - 앱 실행 시 플러그인이 자동으로 스키마를 구성하여 에이전트 이벤트(사용자 메시지 수신, 에이전트 시작, LLM 요청 전송, 응답 등)를 BigQuery 데이터셋에 스트리밍
- **Looker Block 설치**
  - BigQuery ↔ Looker 커넥션 생성 후 마켓플레이스에서 블록 설치 시 커넥션, Cloud Project, Dataset ID, 테이블(기본값 `agent_events`)을 지정
  - 설치·연결만으로 비즈니스 사용자에게 바로 대시보드 제공 가능
- **커스터마이징(확장)**
  - 다른 프로젝트로 블록을 가져오려면 프로젝트 매니페스트 파일의 **remote dependency** 파라미터에 GitHub 저장소 URL과 브랜치명을 지정해 import
  - import된 블록 파일은 기본적으로 **read-only**
  - View/Explore를 로컬 모델 파일로 연장(extend)하고, 대시보드는 원본 모델에 종속되므로 로컬 프로젝트로 복사한 뒤 참조 모델을 교체하고 고유 이름을 부여해야 함
  - 예시: `JSON_VALUE` (BigQuery `JSON` 파싱 syntax)를 사용한 `dimension`을 LookML로 작성해 사용자 프롬프트를 파싱하는 커스텀 확장 시연
- **대시보드 에이전트(Dashboard Agents)**
  - 대시보드에 적용된 필터를 반영해 자연어로 질의응답 가능 (예: "앞으로 5일간 토큰 사용량 예측은?")

---

## 💡 개발자 포인트
- 로컬 개발 시 인증 설정과 서비스 계정 권한(`BigQuery Job User`, `BigQuery Data Editor`) 부여가 선행되어야 데이터 스트리밍이 동작함
> Import한 Looker Block 파일은 **read-only**이므로, 커스텀 확장을 하려면 반드시 View/Explore를 로컬 모델 파일로 옮겨 확장(extend)해야 하며, 대시보드도 복사 후 참조 모델을 교체해야 정상 동작함
- 별도 `LookML` 지식 없이도 마켓플레이스 설치만으로 기본 대시보드를 제공할 수 있어, 빠른 PoC나 비개발 조직 대상 배포에 적합

---

## 📅 버전 / 출시 일정
해당 없음

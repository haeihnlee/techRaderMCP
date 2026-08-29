# Automate Google Cloud with Cloud CLI Remote MCP Server

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=-fb0ycu4kiU
- **요약 일시**: 2026-08-29 09:07:35

---

## 🔑 핵심 요약
- **Google Cloud CLI Remote MCP Server**를 사용하면 로컬 바이너리 설치 없이 AI 에이전트가 Google Cloud 리소스를 대화형으로 조작할 수 있다.
- 에이전트는 `gcloud` CLI와 BigQuery용 `bq` 명령을 통해 로그 분석, Cloud Storage 점검, 데이터 적재량 검증을 수행한다.
- 변경 작업 전 사용자 확인을 거치고, 사용자 **IM 자격 증명**과 보안 샌드박스를 활용해 엔터프라이즈 거버넌스를 유지한다.

---

## 📣 주요 발표 내용
- 플러그인 설정에서 Remote MCP Server를 활성화하면 별도의 로컬 실행 파일 설치 없이 바로 사용할 수 있다.
- 자연어 요청만으로 `gcloud` 명령을 실행해 Cloud Logging의 야간 파이프라인 장애 원인을 분석한다.
- Cloud Storage 버킷을 확인해 배치 파일이 활성 디렉터리가 아닌 staging 디렉터리에 잘못 배치된 사실을 찾는다.
- `bq` 명령으로 BigQuery 적재 상태를 조회해 전날에는 5개 행이 적재됐지만 당일에는 0개임을 검증한다.
- 에이전트가 `gcloud storage cp`를 실행해 파일을 active 디렉터리로 이동하고 파이프라인을 복구한다.

---

## 💡 개발자 포인트
- 복잡한 로그 필터 문법이나 별도 SQL 도구 전환 없이 자연어 기반으로 장애 조사와 데이터 검증을 연결할 수 있다.
- `gcloud` 및 `bq` 명령을 에이전트 도구로 노출하면 Cloud Storage, Cloud Logging, BigQuery를 하나의 대화 흐름에서 연계할 수 있다.
- 데이터 이동처럼 상태를 변경하는 명령은 실행 전에 사용자 확인을 요구하도록 설계해야 한다.

> Remote MCP Server는 편리한 자동화를 제공하지만, 실제 변경 작업은 반드시 명시적 확인과 최소 권한의 사용자 자격 증명 아래에서 실행해야 한다.

- 모든 작업이 사용자 IM 자격 증명으로 수행되므로 조직의 IAM 권한 모델과 감사 정책을 사전에 점검해야 한다.
- 보안 샌드박스와 명령 실행 승인 정책을 함께 적용하면 에이전트의 자율성과 운영 통제를 균형 있게 유지할 수 있다.

---

## 📅 버전 / 출시 일정
해당 없음

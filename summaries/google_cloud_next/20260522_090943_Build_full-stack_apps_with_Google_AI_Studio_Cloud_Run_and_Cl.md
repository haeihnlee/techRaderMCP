# Build full-stack apps with Google AI Studio, Cloud Run, and Cloud SQL

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=8F8RRNYNWe4
- **요약 일시**: 2026-05-22 09:09:43

---

## 🔑 핵심 요약
- **Google AI Studio**에서 vibe coding만으로 프론트엔드·백엔드·DB를 포함한 **풀스택 앱**을 `Cloud Run`에 바로 배포 가능
- GCP 프로젝트·`gcloud` 설치·신용카드·결제 계정 없이 **Gmail 계정만으로** 시작 가능 (비전통 GCP 고객 대상 번들 제공)
- DB는 `Cloud SQL for PostgreSQL` 또는 `Firestore` 선택 가능, **end-user 인증**도 기본 제공

---

## 📣 주요 발표 내용
- **Frictionless full-stack 배포** 발표: AI Studio Build 모드에서 프롬프트만으로 앱 생성·배포
- 자동 프로비저닝되는 리소스:
  - `Cloud SQL` 데이터베이스 (초 단위 생성, 스키마 자동 구성)
  - `Cloud Run` 호스팅 (자동 스케일)
  - 이메일 기반 **end-user authentication** 플로우
- 운영 기능: **로그·메트릭** 조회, **환경 변수** 수정(재빌드 불필요), **앱 일시중지/재개/삭제**
- 데모 시나리오: 이웃 도구 공유 앱(`neighborhood tool library`) 구축
  - 프롬프트로 스키마·샘플데이터 자동 생성
  - 파일 업로드 또는 Google Drive 링크로 데이터 로드 (**NoSQL 쿼리 불필요**)
  - PostgreSQL extension을 활용한 **smart search**(오타 허용·자연어 검색) 구현
- 앱 성장 시 **원클릭으로 정식 GCP 계정 onboarding** → 신용카드 등록 후 전체 기능 사용

---

## 💡 개발자 포인트
- 코드 한 줄 작성 없이 대화형 프롬프트와 클릭 몇 번으로 **DB-powered 풀스택 앱** 완성 가능
- 인증 추가 시 AI 에이전트가 `users` 테이블을 자동 생성하고 **데이터 프라이버시 필터링**까지 수행
- Smart search는 **approximate matching** + **semantic search**를 PostgreSQL extension으로 동시 구현

> ⚠️ **주의**: 무료 번들은 비전통 GCP 고객용 진입점이며, 앱 수에 한도가 있음 ("a given number of full stack web applications"). 운영용으로 확장하려면 정식 GCP 계정 onboarding 필요.

> 💡 **vibe coder 경험**: 시간 제한 없이 여러 앱을 빌드 가능하고, 배포 후에도 AI Studio로 돌아가 반복 개선(iterate) 가능.

---

## 📅 버전 / 출시 일정
해당 없음 (Google Cloud Next 세션 발표, 일반 공개 일정 미명시)


# 7 AI agent patterns to improve your coding workflow

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=Z9WbG3m7Da4
- **요약 일시**: 2026-08-28 09:07:08

---

## 🔑 핵심 요약
- 코딩 에이전트에 **모듈형 스킬(skills)**을 추가하면 긴 프롬프트 없이도 고품질 결과를 얻을 수 있음
- 스킬은 단순 텍스트 파일로, `.agents/skills` 또는 `gemini/config/skills` 폴더에 배치하면 에이전트가 필요 시 동적으로 로드
- **7가지 스킬 디자인 패턴**을 조합해 도메인 지식 주입부터 멀티스텝 파이프라인까지 구현 가능

---

## 📣 주요 발표 내용
- **Domain Knowledge**: 특정 도메인 전문 지식 주입 (프론트엔드 UI, 성능 최적화, API 설계 등)
  - Google Cloud 공식 스킬 레포 제공: `Cloud Run`, `AlloyDB`, `BigQuery`, `Cloud SQL` 등 지원
- **Tool Wrappers**: 외부 툴 연동 스킬 (Chrome DevTools 브라우저 테스트, `Git` 워크플로우 자동화)
- **Inversion**: 에이전트가 추측 대신 개발자에게 명확화 질문을 유도하는 패턴
  - `context engineering`, `planning and task breakdown`, `debugging and error recovery` 포함
  - `/grill me` 명령어로 요구사항 명확화 질의응답 가능 (Anti-gravity에 내장)
- **Generators**: 구조화된 출력 생성 (BDD, 문서·**ADR** 작성, 소스 기반 개발)
- **Reviewers**: 코드 품질·보안 체크리스트 기반 자동 코드 리뷰 (`code review and quality`, `security and hardening`)
- **Pipelines**: 엄격한 순서로 멀티스텝 워크플로우 실행 (TDD 3단계 파이프라인: 실패 테스트 → 코드 작성 → 리팩터링)
- **Meta Skills**: 다른 스킬들을 자동으로 관리하는 마스터 라우터 역할 (`using agent skills`)

---

## 💡 개발자 포인트
- 스킬은 **에이전트가 필요할 때만 동적 로드**하므로 컨텍스트 낭비 없음
- 커스텀 스킬 작성도 가능 — 텍스트 파일로 작성 후 코드랩 참고
- **Debugging 스킬**은 무작위 코드 시도를 막고, 로그·상태 데이터를 먼저 수집한 뒤 코드 작성하도록 강제

> ⚠️ Inversion 패턴의 `debugging and error recovery` 스킬: 에이전트가 버그에 임의의 코드를 대입하는 것을 방지하고 **근본 원인 분석(root cause analysis) 워크플로우**를 강제함

- **ADR(Architecture Decision Record)**: 선택한 아키텍처 결정을 공식 문서화하여 에이전트가 이를 참고해 일관된 결정 유지

---

## 📅 버전 / 출시 일정
해당 없음

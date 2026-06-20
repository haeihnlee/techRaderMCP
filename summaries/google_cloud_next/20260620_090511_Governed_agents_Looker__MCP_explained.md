# Governed agents: Looker + MCP explained

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=CgwslR4pgL4
- **요약 일시**: 2026-06-20 09:05:11

---

## 🔑 핵심 요약
- **Looker의 거버넌스된 시맨틱 레이어**와 AI 에이전트를 **MCP**(Model Context Protocol)로 연결해, fragile한 raw SQL 대신 **검증된 데이터 모델**을 직접 다루는 에이전트를 구축
- **MCP Toolbox for Databases**(오픈소스)가 Looker를 표준화된 MCP 도구로 노출 → 프로젝트마다 통합 코드를 다시 짤 필요 없음
- **Google ADK**(Agent Development Kit)로 LLM·에이전트를 오케스트레이션하며, **모델 종류에 구애받지 않는** 유연한 구조 제공

---

## 📣 주요 발표 내용
- **MCP를 "범용 언어"로 활용**: 에이전트가 복잡한 API 호출 방법을 몰라도, 표준화된 도구 세트를 통해 Looker 기능을 발견·호출
- 이 도구들은 Looker 모델링 레이어에 직접 매핑되어, **LookML에 정의된 dimensions·measures·access filters를 그대로 준수**하며 메타데이터 조회·모델 탐색·쿼리 실행 가능
- **MCP Toolbox for Databases**
  - 데이터 소스를 MCP 도구로 노출하는 **프로덕션 레디** 오픈소스
  - **pre-built Looker tool set** 내장 (LookML 프로젝트 감사부터 거버넌스된 쿼리 실행까지)
  - 에이전트에 **노출할 도구를 선택 지정** 가능 → 용도별 에이전트 분리 운용
- **3계층 아키텍처**
  - **모델링 레이어**: Looker + LookML — 비즈니스 로직 중앙화, 신뢰할 수 있는 단일 출처(source of truth)
  - **전송 레이어(Transport)**: MCP + GenAI Toolbox — Looker 내부 함수(메타데이터 조회·쿼리 실행)를 `tools.yml`로 정의된 표준 도구로 변환
  - **애플리케이션 레이어**: Google ADK — LLM·에이전트 오케스트레이션, MCP로 도구 발견 후 호출

---

## 💡 개발자 포인트
- **비즈니스 로직은 Looker에, 실행은 에이전트에** 분리 — 에이전트가 직접 SQL을 작성하지 않으므로 깨지기 쉬운 쿼리 위험 제거
- 도구 설정은 `tools.yml` 구성 파일로 선언 → 에이전트별로 필요한 도구만 선택해 노출
- ADK는 **원하는 어떤 모델이든 사용 가능**하여 프레임워크가 특정 LLM에 종속되지 않음

> **MCP 브리지가 Looker 인스턴스와 항상 동기화**되므로, LookML을 변경하면 그 변화가 **즉시 에이전트의 컨텍스트에 반영**됩니다. 데이터가 대시보드를 넘어 에이전트 애플리케이션까지 확장됩니다.

---

## 📅 버전 / 출시 일정
해당 없음


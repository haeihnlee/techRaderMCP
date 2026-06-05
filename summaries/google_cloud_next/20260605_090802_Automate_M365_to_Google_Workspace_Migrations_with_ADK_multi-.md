# Automate M365 to Google Workspace Migrations with ADK multi-agents

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=9BwFgEFVLOk
- **요약 일시**: 2026-06-05 09:08:02

---

## 🔑 핵심 요약
- **Google ADK**(Agent Development Kit)로 M365 라이선스를 **Google Workspace**로 매핑하는 멀티 에이전트를 구축한 사례
- 신뢰성 있는 에이전트의 핵심은 단순 API 호출이 아니라 **상태 관리·라우팅·가드레일**
- 거대한 단일 프롬프트 대신 작고 집중된 **서브 에이전트**로 분리해 환각(hallucination)과 디버깅 부담을 줄임

---

## 📣 주요 발표 내용
- **Sequential Agent**로 파이프라인 구성: `입력 파서` → `리서처` → `리포터`가 각자 전용 시스템 프롬프트로 동작
- 각 에이전트가 **단일 책임**만 맡아 정확도↑, 디버깅↑
- **Loop Agent**로 자기 교정(self-correcting) 루프 구성
  - `License Mapper` + `Report Reviewer`를 페어링
  - 리뷰어가 누락 기능·깨진 포맷(불필요한 이모지 등)을 검사 후 매퍼로 되돌려 수정
- 데이터 정확도: **Google Search**(실시간 grounding) + 로컬 **기능 매트릭스 CSV** 지식 베이스 결합
- **로깅 플러그인**을 드롭인하여 프롬프트·응답 데이터를 logging sink로 스트리밍 → 프로덕션 관측성(observability) 지원
- 최종 산출물은 정형화된 **10-챕터 리포트**

---

## 💡 개발자 포인트
- **Context Caching**: 거대한 로컬 CSV를 매 실행마다 프롬프트에 주입하면 컨텍스트 윈도우 소모·API 비용 급증
  - ADK 내장 캐싱으로 지식 베이스를 **한 번만 로드**, TTL·토큰 한도는 내부 처리 → 지연·토큰 절감
- **배포**: `Agent Engine`으로 **명령어 한 줄** 배포. 별도 `Dockerfile`·호스팅 인프라 불필요

> **HTTP 429 (resource exhaustion) 해결 팁**: HTTP 헤더 2개만 추가하면 **priority inference**를 활성화해 모델 엔드포인트에서 보장된 우선 슬롯을 확보할 수 있음

---

## 📅 버전 / 출시 일정
해당 없음


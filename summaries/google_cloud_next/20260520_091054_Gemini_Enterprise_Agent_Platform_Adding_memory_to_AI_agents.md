# Gemini Enterprise Agent Platform: Adding memory to AI agents

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=5m9ppmJuJHk
- **요약 일시**: 2026-05-20 09:10:54

---

## 🔑 핵심 요약
- **Gemini Enterprise Agent Platform**이 AI 에이전트에 메모리를 부여하는 3가지 메커니즘(`Sessions`, `Memory Bank`, RAG)을 공개
- **20줄 미만의 코드**로 세션 상태 저장 및 자동 메모리 추출이 가능하며, 모든 데이터는 클라우드에 자동 보관
- **AlloyDB Auto Embeddings**와 **Data Agent Kit**(VS Code 확장)로 RAG 파이프라인 구축 부담을 대폭 경감

---

## 📣 주요 발표 내용
- **`Agent Sessions`**: 대화 상태를 클라우드에 자동 저장 → 세션 종료 후에도 재개 가능 (예: 마라톤 경로의 랜드마크 정보를 state로 유지)
- **`Agent Memory Bank`**: 매 turn마다 유용한 정보를 자동으로 추출·저장하여 향후 대화에서 재활용 (예: "라스베이거스 시는 낙타를 공도에서 금지" 같은 사실을 다음 플랜에 자동 반영)
- **`AlloyDB` Auto Embeddings**: 신규 레코드 삽입 시 임베딩을 자동 생성 → 데이터 엔지니어의 임베딩 파이프라인 운영 부담 제거
- **Data Agent Kit**: `VS Code`, OSS Code, Cloud Shell에서 대부분의 GCP 데이터베이스와 직접 상호작용
- **Data Engineering Agent**: 프롬프트 기반으로 `Dataform` 또는 신규 지원되는 `DBT` 파이프라인과 오케스트레이션을 자동 생성
- **Agent Skills**: GCP 제품별 큐레이션된 **13개의 신규 스킬** 공개 (Google Cloud 공식 repo 제공, 확장 가능)
- 데모용 레포 `race-condition`을 통해 **원클릭 배포**로 직접 마라톤 플래너 에이전트 실행 가능

---

## 💡 개발자 포인트
- 메모리/세션 관리를 직접 로컬 파일로 구현하지 말고 **Memory Bank에 위임** → 보일러플레이트 코드 제거
- RAG 파이프라인 구축 시 **AlloyDB Auto Embeddings**로 임베딩 생성 단계를 데이터베이스 레벨에서 처리하면 인서트 직후 즉시 RAG 활용 가능
- PDF/Doc 청킹은 여전히 직접 설계해야 하는 부분 — 컨텍스트 유지 및 구조화된 청킹 전략 필수 (제공 codelab 참고)

> **참고**: 발표된 모든 기능에 대해 **75개 이상의 codelab**이 공개되어 있으며, 데모 코드는 전부 GitHub에서 실행/확장 가능 — "숨겨진 기능"이 아니라 즉시 검증 가능한 자산

- 기존 스킬을 템플릿으로 활용해 특수 요구사항(예: 임베딩 처리 커스터마이징)을 손쉽게 확장 가능

---

## 📅 버전 / 출시 일정
| 항목 | 상태 |
|------|------|
| Gemini Enterprise Agent Platform (Sessions / Memory Bank) | 공개 (Google Cloud Next 발표) |
| AlloyDB Auto Embeddings | 사용 가능 |
| Data Agent Kit (VS Code 확장) | 이번 주 출시 |
| Agent Skills (13개 신규) | 출시 (GCP repo) |
| DBT 파이프라인 지원 (Data Engineering Agent) | 신규 추가 |

# Building GPU-accelerated multi-agent apps with Google ADK and Gemma 4

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=vIyhQGBkn34
- **요약 일시**: 2026-05-12 09:12:11

---

## 🔑 핵심 요약
- **Google ADK**(Agent Development Kit)와 **Gemma 4**로 GPU 가속 멀티 에이전트 앱을 처음부터 구축하는 라이브 세션
- **Cloud Run** + **NVIDIA RTX PRO 6000 GPU** 조합으로 오픈소스 모델을 효율적으로 서빙하는 아키텍처 소개
- **Milvus** 벡터 DB를 통한 정책(policy) 검색 RAG 파이프라인을 멀티 에이전트와 연결하는 패턴 시연

---

## 📣 주요 발표 내용
- **세션명**: Building GPU-accelerated multi-agent apps with Google ADK and Gemma 4
- **발표자**: Chelsie Czop (Google) + Jay Rodge (**NVIDIA**)
- **데모 주제**: 처음부터 구축하는 **지속가능성(sustainability) 인텔리전스 앱**
- 오픈소스 **Google Agent Development Kit (ADK)** 로 전문 에이전트 팀(specialist agents) 오케스트레이션
- **Gemma 4** 모델을 `Cloud Run` 위에서 `NVIDIA RTX PRO 6000` GPU로 서빙
- **Milvus** 를 벡터 스토어로 사용해 정책 문서 retrieval 구성
- 로컬 모델 배포부터 프로덕션 agentic 워크플로 스케일링까지 다루는 아키텍처

---

## 💡 개발자 포인트
- **ADK는 오픈소스**라 자체 인프라에서도 멀티 에이전트 패턴을 그대로 적용 가능 — 벤더 락인 부담이 낮음
- **Cloud Run GPU**는 서버리스 기반으로 LLM을 띄울 수 있어, GKE/Compute Engine 대비 운영 부담이 적은 옵션
- **Gemma 4**처럼 오픈 가중치 모델 + 자체 GPU 서빙 조합은 API 비용·데이터 거버넌스가 중요한 워크로드에 적합
- RAG 컴포넌트로 `Milvus`를 채택 — 자체 호스팅 가능한 벡터 DB가 필요한 팀에 참고할 만한 스택

> 자막이 제공되지 않는 라이브 세션이라 코드 레벨의 세부 구현은 영상에서 직접 확인 필요. 핵심 가치는 **"ADK + Gemma + Cloud Run GPU + Milvus"** 라는 end-to-end 오픈 스택 레퍼런스 아키텍처입니다.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| 모델 | `Gemma 4` |
| 프레임워크 | `Google ADK` (오픈소스) |
| 런타임 | `Cloud Run` + `NVIDIA RTX PRO 6000` GPU |
| 벡터 DB | `Milvus` |
| 출시 일정 | 영상 설명에 명시된 GA 일정 없음 (라이브스트림 세션)


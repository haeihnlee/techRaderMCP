# Build a production-ready RAG agent with Google Agent Development Kit (ADK), Gemini, and Cloud Run

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=sWHMIjgcxEU
- **요약 일시**: 2026-08-29 09:12:52

---

## 🔑 핵심 요약
- **Google Agent Development Kit(ADK)**와 **Gemini**를 사용해 검색 증강 생성(`RAG`) 에이전트를 구축하는 흐름을 다룹니다.
- `Streamlit` 기반 UI를 에이전트에 결합하고 **Cloud Run**에 배포해 프로덕션 형태로 운영하는 방법을 소개합니다.
- 공식 Codelab을 따라 문서 검색과 생성 응답을 연결하는 애플리케이션을 직접 구현할 수 있습니다.

---

## 📣 주요 발표 내용
- `ADK`를 활용해 검색·문서 조회·응답 생성을 조합하는 RAG 에이전트 구조를 설명합니다.
- `Gemini`를 생성 모델로 연결해 검색된 컨텍스트를 바탕으로 답변을 생성합니다.
- `Streamlit`으로 빠르게 대화형 애플리케이션 UI를 구성합니다.
- 구현한 애플리케이션을 **Cloud Run**에 컨테이너 기반으로 배포합니다.
- 실습 자료로 [Cloud Run 콘솔](https://g.dev/cloud/cloud-run-console)과 [RAG Agent ADK Codelab](https://g.dev/cloud/rag-agent-adk)을 제공합니다.

---

## 💡 개발자 포인트
- RAG 애플리케이션은 모델 호출만으로 구성하지 않고, 검색 단계와 생성 단계를 명시적으로 분리해 최신·도메인 특화 데이터를 답변에 반영합니다.
- `Streamlit`은 프로토타입 UI를 빠르게 만들 수 있고, `Cloud Run`은 해당 애플리케이션을 관리형 서버리스 환경에 배포하는 경로를 제공합니다.
- 프로덕션 배포 전에는 검색 결과 품질, 프롬프트 주입, 민감 정보 노출, 인증·권한, 비용 및 지연 시간을 별도로 검증해야 합니다.

> 공식 Codelab은 시작점입니다. 실제 서비스에서는 문서 접근 권한 필터링과 검색 근거 검증을 추가하지 않으면 사용자가 권한 없는 정보나 부정확한 답변을 받을 수 있습니다.

---

## 📅 버전 / 출시 일정
해당 없음

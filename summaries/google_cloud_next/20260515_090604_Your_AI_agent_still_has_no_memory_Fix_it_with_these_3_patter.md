# Your AI agent still has no memory? Fix it with these 3 patterns

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=9ebzuW5PMW4
- **요약 일시**: 2026-05-15 09:06:04

---

## 🔑 핵심 요약
- **AI 에이전트 메모리 6가지 패턴** 중 후반부 3가지(**콜백**, **커스텀 툴**, **멀티모달 메모리**)를 다룬 영상
- 단순 LLM·툴 호출만으로는 부족하며, **메모리 설계**가 진짜 똑똑한 에이전트를 만든다는 것이 핵심 메시지
- **Vertex AI Agent Engine Memory Bank**로 이미지·영상·오디오까지 기억하는 멀티모달 에이전트 구현 가능

---

## 📣 주요 발표 내용

### 1. 콜백(Callbacks) 패턴 — 자동 메모리 업데이트
- 에이전트가 **자기 자신을 더 복잡하게 만들지 않고** 대화 컨텍스트를 저장하는 방법
- 에이전트 라이프사이클의 훅 지점에 커스텀 로직 삽입 가능:
  - 에이전트 실행 **before / after**
  - 모델 호출 **before / after**
  - 툴 호출 **before / after**
- 예시: 여행 플래너에서 `after_tool_callback`으로 활동 타입(`cultural`, `food`, `outdoor`)을 컨텍스트에 기록 → 박물관 추천 후에는 박물관 전문가 에이전트 차단

### 2. 커스텀 툴(Custom Tools) 패턴 — 구조화된 메모리
- 비정형 채팅 로그가 아닌 **구조화된 사용자 프로필**에 기록
- 두 개의 툴을 도입:
  - `save_user_preference` — dict 객체를 받아 DB에 새 레코드 저장
  - `recall_user_preferences` — 저장된 레코드를 다시 읽음
- 에이전트 지시문(instruction)에서 **시작 시 recall 먼저 호출**, 사용자가 선호 언급하면 **save 호출**
- 결과: "비건이에요" 한 번 말하면 다음 세션부터 묻지 않고 비건 식당 추천

### 3. 멀티모달 메모리 — 이미지·영상·오디오 기억
- **Vertex AI Agent Engine Memory Bank**에 사진·영상·오디오 세션을 통째로 저장
- 에이전트에 `preload_memory` 툴을 제공해 메모리 뱅크에서 대화로 로드
- 예시: 사진/영상/오디오 업로드 → "이걸 보고 어디로 여행 가야 할까?" 질문 → 미디어 간 맥락을 이어 추천

---

## 💡 개발자 포인트

> **"AI 지능 = 모델 + 툴"이라는 사고에서 벗어나야 한다.** 모델만큼 메모리 설계가 중요하며, 메모리 없는 에이전트는 매 대화가 백지 상태로 시작된다.

- 콜백은 **에이전트 코드를 건드리지 않고** 자동 기록 로직을 주입할 수 있어, 분석·개인화 로직 분리에 적합
- 구조화 데이터가 필요할 땐 **비정형 텍스트 기억 대신 커스텀 툴** 사용 — LLM이 긴 로그를 매번 파싱하는 비용 절감
- 멀티모달 메모리는 ADK + Vertex AI Agent Engine 조합에서 즉시 활용 가능 — 단순 텍스트 RAG로 해결 안 되던 시나리오를 풀 수 있음
- 6가지 패턴 정리:
  1. Session State (이전 영상)
  2. Multi-agent State (이전 영상)
  3. Persistent Memory (이전 영상)
  4. **Callbacks** (이번 영상)
  5. **Custom Tools** (이번 영상)
  6. **Multi-modal Memory** (이번 영상)

---

## 📅 버전 / 출시 일정
해당 없음 (개념·패턴 소개 영상, 별도 릴리스 일정 언급 없음. **Vertex AI Agent Engine Memory Bank**는 현재 사용 가능)


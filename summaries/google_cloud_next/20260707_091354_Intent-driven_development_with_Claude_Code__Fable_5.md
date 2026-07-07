# Intent-driven development with Claude Code & Fable 5

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=6ERUGFurDHY
- **요약 일시**: 2026-07-07 09:13:54

---

## 🔑 핵심 요약
- **Anthropic**과 `Claude Code Tips` 저장소(GitHub 8,000+ 스타) 저자가 함께 **"Intent-driven development"**(의도 중심 개발) 워크플로우를 시연
- `Claude Code`를 **Google Cloud (Vertex AI)** 위에서 엔터프라이즈 규모로 실행하는 셋업 데모 포함
- 3D 슬링샷 게임을 `Three.js` + 물리 엔진으로 만드는 실전 데모를 통해 음성 입력 기반 프롬프팅 방식 소개

---

## 📣 주요 발표 내용
- 많은 개발자가 놓치고 있는 기능으로 **`auto mode`**를 꼽음
- **Intent-driven development**란 정확한 프롬프트 문구보다 **자신의 의도를 명확히 인지하고 표현하는 것**이 핵심이라는 개념
- 의도를 빠르게 표현하기 위한 팁으로 **음성 입력(voice mode)**을 적극 권장 — 오타나 문법 실수는 괜찮으니 속도를 우선
- `plan mode`, 이미지 첨부 등은 모두 **"verification"**(검증)의 일종으로 소개됨
- Google Cloud 위에 `Claude Code`를 셋업하는 절차:
  - `gcloud SDK` 설치
  - `Project ID` 설정
  - `Vertex AI API` 활성화
  - Vertex AI 연동을 위한 환경 변수 설정 후 `claude` 실행 → Vertex AI 모델로 구동
- 데모: 3D 슬링샷 게임 제작 시 `Three.js` + 물리 라이브러리(`cannon` 대신 `ammo`/`rapier` 계열) 선택 과정을 음성으로 에이전트와 대화하며 진행

---

## 💡 개발자 포인트
- 넓은 질문(아키텍처, 라이브러리/프레임워크 선택)으로 시작한 뒤 점점 구체화하는 방식을 추천
- 최신 정보가 필요하면 에이전트에게 **직접 리서치를 요청**해 더 나은 아키텍처 결정을 내리도록 유도
- **`git`, `gh`(GitHub CLI) 등 CLI 명령어 숙달**을 강력 추천 — CLI 자체가 매우 강력한 도구
- 여러 프로젝트를 한 폴더 아래 모아두면 에이전트가 프로젝트 간 요소를 조합하기 편리
- 실무에서는 `plan mode`를 명시적으로 켜기보다 **동료에게 말하듯 자연스럽게 대화**하는 방식으로 사용한다는 의견 공유

> 별도의 Breaking Change나 마이그레이션 주의사항은 언급되지 않음

---

## 📅 버전 / 출시 일정
해당 없음


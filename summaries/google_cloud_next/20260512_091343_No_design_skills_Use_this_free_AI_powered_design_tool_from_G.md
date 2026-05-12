# No design skills? Use this free AI powered design tool from Google | The Agent Factory

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=hNHE301qF1A
- **요약 일시**: 2026-05-12 09:13:43

---

## 🔑 핵심 요약
- Google이 공개한 무료 AI UI 생성 도구 **Stitch**로 디자인 지식 없이도 완성도 높은 UI를 빠르게 만들 수 있다
- 코딩 에이전트가 "테크 리드"라면, **Stitch는 디자인 에이전트**이며 사용자는 "크리에이티브 디렉터" 역할로 방향을 잡는다
- **콘텐츠 기반 프롬프트**(실제 헤딩·이름·목적)를 미리 정의하면 결과 품질이 크게 올라간다

---

## 📣 주요 발표 내용
- **Stitch 소개**: `stitch.withgoogle.com`에서 동작하는 Google Labs의 AI 기반 UI 생성 툴
- AI 에이전트에 **Stitch를 연동**하여 즉석에서 UI를 생성하도록 만들 수 있음 (Agent Factory 시리즈 컨셉)
- 데모: "메릴랜드 체사피크 베이 크래빙 투어 사이트" 프롬프트로 사이트 디자인 생성 과정 시연
- **프롬프트 작성 패턴**
  - 사이트의 **대상 청중**과 **목적**을 명시 (예: "투어 회사용", "초보 크래버용")
  - **원하지 않는 것**을 제거하는 방식으로 제약을 좁히기
  - **테마(light/dark)**, **컬러 팔레트**, **접근성 대비**를 사전에 고려
- Gemini와 함께 사용해 콘텐츠 시드를 먼저 생성한 뒤 Stitch에 투입하는 워크플로우 소개

---

## 💡 개발자 포인트
- AI 코딩 에이전트에 UI 생성 기능을 붙이고 싶다면 **Stitch를 design subagent**로 통합하는 패턴이 유효
- "디자인을 잘 모르겠다"는 개발자도 **디자인 어휘**(motion, tonal layering, aesthetic 일관성 등)를 익히면 결과물 평가가 가능
- **콘텐츠가 디자인을 주도한다(content-driven design)**: 더미 텍스트가 아닌 실제 콘텐츠를 넣어야 레이아웃·시각화 공간이 의미 있게 잡힘

> **주의:** Stitch 결과물에 막연한 불만이 있다면 "무엇이 싫은지" 언어화하는 것이 핵심이다. "라인이 모션을 암시해서 차분한 분위기와 충돌" 같은 구체적 지적이 가능해야 반복 개선이 빨라진다.

> **접근성 체크포인트:** 강한 브랜드 컬러(예: 메릴랜드 깃발의 빨강/검정/노랑)를 화이트 배경에 그대로 쓰면 대비 문제 발생. **saturation up + brightness down**으로 톤 다운한 변형을 활용.

---

## 📅 버전 / 출시 일정
해당 없음 (`Stitch`는 `stitch.withgoogle.com`에서 무료 공개 중)


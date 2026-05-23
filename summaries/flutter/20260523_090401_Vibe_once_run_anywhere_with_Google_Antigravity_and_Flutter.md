# Vibe once, run anywhere with Google Antigravity and Flutter

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=UNdQhnpm8GY
- **요약 일시**: 2026-05-23 09:04:01

---

## 🔑 핵심 요약
- **Google Antigravity**는 Gemini 3 기반의 **AI 네이티브 개발 환경**으로, *Plan → Act → Verify* 피드백 루프를 통해 에이전트 기반 개발을 가속화
- **Flutter + Dart**는 단일 코드베이스(**Vibe Once, Run Anywhere**) + 강타입 시스템 + Hot Reload 덕분에 LLM이 가장 효율적으로 다룰 수 있는 크로스플랫폼 스택
- 실제 사례로 **Dash Lander** 게임(Procedural 레벨, 커스텀 셰이더, 파티클)을 에이전트와 함께 제작하며 코드뿐 아니라 음악·에셋·마케팅 자료까지 통합 제작

---

## 📣 주요 발표 내용
- **Antigravity 개요**
  - 2025년 9월 출시된 Google의 AI 네이티브 IDE, **Gemini 3**를 출시 첫날부터 통합
  - 핵심 워크플로우: **Planning → Acting → Verifying** 피드백 루프
  - **Multimodal**: 이미지 생성, 스크린샷, 비디오 녹화로 작업 검증
  - **Chrome 브라우저 통합**으로 실제 앱을 실행하고 버튼 클릭·테스트 자동 수행
  - 작업 완료 후 구현 내용과 결정 근거를 담은 **walkthrough 문서** 자동 생성

- **Flutter가 AI 에이전트에 적합한 이유**
  - **단일 소스 오브 트루스(Single Source of Truth)**: iOS/Android/Web을 각각 작성할 필요 없음 → Whack-A-Mole 회피
  - **Dart의 강타입 시스템**: 함수 시그니처 불일치·클래스 형태 차이 등 객관적 사실을 LLM에 명확히 전달
  - **Stateful Hot Reload**: 1초 이내 리빌드로 에이전트 반복 속도 극대화
  - Dart는 네이티브에서 **머신 코드**, 웹에서 **JavaScript/Wasm**으로 컴파일 → 네이티브 성능 보장

- **Dash Lander 게임 제작 사례**
  - 소행성에 달 착륙선을 안착시키는 게임
  - 실시간 멀티플레이 대신 **과거 세션과의 대결(Historical Sessions)** 방식 채택 → 복잡한 백엔드 회피
  - 백엔드는 **Firebase Hosting**으로 단순화하여 자동 스케일링
  - 배경음악 생성에 Google **Lyria** 활용

---

## 💡 개발자 포인트
- **역할이 흐려진다**: 개발자·PM·디자이너 모두 새로운 모자를 쓰게 되며, 디자이너가 프로토타입을 넘기고 개발자가 디자인 초안을 만드는 등 협업 방식이 바뀜

> **"If a picture is worth a thousand words, then a prototype can save a thousand meetings."** — 프로토타입 제작 속도가 빨라지면서 비전 설명 시간이 극적으로 줄어듦

- **Fail Fast 전략**: 6개월~1년 걸리던 prototype 단계를 며칠~몇 주로 단축. 잘못된 결정을 빠르게 내고 폐기하는 것이 핵심
- **에이전트는 여전히 실수한다** → 사람은 루프의 중심에서 비전·디자인에 집중하고, 세부 구현은 에이전트가 담당
- Flutter 프로젝트의 **analysis server**가 에이전트에게 정적 분석 신호를 즉시 제공 → 오류 자동 수정 사이클이 더 정확해짐
- 코드 외에도 **마케팅 자료·에셋·팀 협업**까지 에이전트 워크플로우에 통합 가능

---

## 📅 버전 / 출시 일정

| 항목 | 시점 |
|------|------|
| **Antigravity** 출시 | 2025년 9월 |
| **Gemini 3** Antigravity 통합 | 출시 첫날부터 |
| Google 모델 역량 도약 | 2025년 12월경 (Gemini 3 출시 시점) |
| Dart 최초 공개 | 2011년 |


# How we built a Flutter-powered AI coffee shop

- **컨퍼런스**: Flutter
- **출처**: https://blog.flutter.dev/how-we-built-a-flutter-powered-ai-coffee-shop-878c60a11f1a
- **요약 일시**: 2026-06-23 09:04:20

---

## 🔑 핵심 요약
- Flutter 팀이 **Flutter 앱으로 시작해 실제 카푸치노 한 잔으로 끝나는** AI 라떼아트 데모를 제작 (Cloud Next의 `GenLatte`, Google I/O의 `Antigravity Coffee Co.`)
- 사용자에게 몇 가지 질문 → 개인화된 프롬프트 생성 → **`Nano Banana`** 이미지 모델이 맞춤 라떼아트 생성 → 프린터가 우유 거품 위에 직접 출력
- **Flutter**(동적 레이아웃·커스텀 셰이더) + **Firebase**(배포·확장·리액티브 데이터 바인딩) + **Gemini/Nano Banana**(이미지 생성) 조합으로 풀스택 구현

---

## 📣 주요 발표 내용
- 단순 주문·전달이 아닌 **개인적이고 재미있는 경험**을 목표로 설계
- **`Gemini`** 와 **`Nano Banana`** 가 사용자의 "행복한 순간(happy place)" 프롬프트를 환상적인 아트로 변환
- **`Nano Banana`** 는 보기 좋은 구도를 위해 최적화됨 — 피사체로 향하는 **"leading S curve"** 를 적용 (도로·강·언덕·해안선 등으로 회전 사용)
- **Generative UI** 와 **`A2UI` 프로토콜**을 Flutter와 결합해 실시간으로 변하는 **적응형 인터페이스** 구현
- Flutter의 **커스텀 셰이더(custom shaders)** 와 동적 레이아웃으로 위트 있는 UI를 손쉽게 제작

---

## 💡 개발자 포인트
- **Firebase**가 배포·스케일링 부담을 흡수하고 **리액티브 풀스택 데이터 바인딩**을 제공 → 백엔드 구성이 간결
- AI 이미지 생성을 단발성이 아닌 **질문→프롬프트→생성→물리적 출력**의 파이프라인으로 엮은 점이 핵심 패턴
- **Generative UI + A2UI**로 UI를 정적으로 짜지 않고 **런타임에 동적으로 생성**하는 접근 — 적응형 UX 설계에 참고
> 핵심 아이디어: 모델 출력을 그대로 쓰지 않고, 구도(leading S curve 등) 같은 **디자인 제약을 프롬프트에 주입**해 일관된 결과 품질을 확보.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| ---- | ---- |
| 데모명 (Cloud Next) | `GenLatte` |
| 데모명 (Google I/O) | `Antigravity Coffee Co.` |
| 작성자 | Craig Labenz (Flutter 팀) |
| 게시 | 2026년 6월 |


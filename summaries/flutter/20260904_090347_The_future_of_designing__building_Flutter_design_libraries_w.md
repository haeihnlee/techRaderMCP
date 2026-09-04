# The future of designing & building Flutter design libraries with Widgetbook | Lucas Josefiak

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=sWSXWrrqOAY
- **요약 일시**: 2026-09-04 09:03:47

---

## 🔑 핵심 요약
- **Widgetbook V4** 출시로 코딩 에이전트가 UI 피드백 루프를 자체적으로 수행할 수 있는 기반 마련
- **Figma MCP 서버** 연동으로 디자인-코드 완전 자동 검증 워크플로우 실현
- **접근성 회귀 테스트** 기능 추가로 European Accessibility Act 대응 지원

---

## 📣 주요 발표 내용
- **Widgetbook V4** 첫 메이저 버전 출시
  - 위젯 스토리 내 테스트 시나리오 정의 가능 → Flutter 테스트와 통합
  - 코딩 에이전트가 `Widgetbook` 테스트를 로컬에서 실행하여 오버플로우 등 사전 감지
- **Figma MCP 서버 + Widgetbook** 통합
  - 스크린샷 비교를 넘어 위젯 속성까지 디자인과 완전 일치 검증
  - 접근성 테스트까지 자동화 파이프라인에 포함
- **Widgetbook 스킬** 설정으로 에이전트에게 커스텀 디자인 시스템 학습 가능
  - 하드코딩된 값 방지, 앱 전용 컴포넌트 강제 사용 등 규칙 적용
- **접근성 회귀 테스트** (Widgetbook Cloud)
  - 위젯 트리 + 의미론적 트리 스냅샷을 PR별로 비교 분석
  - 의도치 않은 접근성 변경 자동 감지
- **Gen UI 가이드** 공개 — `Widgetbook`을 Gen UI 카탈로그 테스트에도 활용 사례 발표
- 오픈 소스 패키지 50% 이상 성장, 클라우드 부문은 더 큰 폭 성장

---

## 💡 개발자 포인트
- 코딩 에이전트 시대에 **커스텀 디자인 시스템**이 필수 자산으로 부상
  - 에이전트 환각 방지 및 브랜드 일관성 유지를 위해 `Widgetbook` 스킬 활용 권장
- 전형적인 에이전트 워크플로우:
  1. `Widgetbook` 스킬로 에이전트에게 디자인 시스템 학습
  2. Figma에서 컴포넌트 빌드 완료 후 Flutter 테스트 실행
  3. Widgetbook Cloud에서 시각적·접근성 변경 자동 검토

> **접근성 회귀 테스트**: 일단 접근성 수준을 확보해도 이후 배포에서 의도치 않게 떨어지는 현상이 발생할 수 있음. 위젯 트리 + 의미론적 트리 비교만으로 모든 회귀를 감지할 수 있도록 설계됨.

> **European Accessibility Act** 시행으로 유럽 기업은 접근성 있는 앱 구축이 법적 의무화. Flutter용 접근성 도구는 여전히 제한적이므로 `Widgetbook` 활용 가치 높음.

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| Widgetbook V4 | 컨퍼런스 시점 최근 출시 (첫 메이저 버전) |
| 접근성 회귀 테스트 | 컨퍼런스 이전 Widgetbook Cloud에 출시 |
| Gen UI 가이드 | 컨퍼런스 당일 아침 공개 |


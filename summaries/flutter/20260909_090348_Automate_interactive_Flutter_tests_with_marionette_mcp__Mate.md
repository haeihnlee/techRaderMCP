# Automate interactive Flutter tests with marionette_mcp | Mateusz Wojtczak

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=JQMx58kw_Wo
- **요약 일시**: 2026-09-09 09:03:48

---

## 🔑 핵심 요약
- `marionette_mcp`는 AI 에이전트가 Flutter 앱을 **직접 보고 조작**할 수 있게 해주는 오픈소스 MCP 패키지
- 스크린샷 캡처, 위젯 트리 탐색, 탭·스크롤 상호작용을 통해 AI가 런타임에서 앱을 실시간 검증 가능
- `Patrol MCP`와 결합하면 AI 탐색 후 결정론적인 Dart 테스트 코드까지 자동 생성 가능

---

## 📣 주요 발표 내용
- **`marionette_mcp`**: AI 에이전트를 위한 Flutter 앱 런타임 검증 도구
  - **Playwright MCP**의 Flutter 버전 — 브라우저 앱 조작처럼 Flutter 앱 조작 가능
  - 제공 기능: 스크린샷, Flutter 로그 수집, 탭/스크롤 인터랙션, 인터랙티브 위젯 요소 트리 추출
  - Figma MCP와 연동: 디자인 스크린샷 vs 실제 앱 스크린샷 자동 비교 후 불일치 수정 루프
- **`Patrol MCP`**: `marionette_mcp`와 연동되는 E2E 테스트 프레임워크 MCP
  - AI가 앱 탐색 후 Dart로 작성된 결정론적 테스트 코드 생성
  - `hot restart` 기능으로 특정 테스트 단위 재실행 가능
- Lean Code 내부 프로젝트로 시작 → X(Twitter) 게시물 계기로 오픈소스 공개 (2026년 초)
- pub.dev 월 **12만 다운로드** 달성, Flutter 활성 개발자 **200만 명** 돌파

---

## 💡 개발자 포인트
- 전체 위젯 트리는 AI 컨텍스트 크기 문제로 제공하지 않음 — **인터랙티브 요소만** 선택적으로 전달
- AI가 단순히 "괜찮다"고 말하는 수준이 아닌, **커밋 가능한 테스트 코드**를 확보할 수 있음이 핵심 가치

> **Breaking Point**: AI 에이전트 검증만으로는 부족 — `Patrol MCP`와 함께 사용해야 결정론적 테스트 코드(Dart)가 보장됨

- Figma MCP + `marionette_mcp` 조합 워크플로우:
  1. Figma 디자인 스크린샷 제공
  2. 코드 작성 후 앱 실행
  3. `marionette_mcp`로 스크린샷 캡처 및 비교
  4. 불일치 발견 시 자동 수정 후 재검증

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| `marionette_mcp` 오픈소스 공개 | 2026년 초 |
| pub.dev 월간 다운로드 | 12만 건 |
| Flutter 활성 개발자 수 | 200만 명 이상 |
| 내부 개발 → 오픈소스 전환 기간 | 약 2주 |


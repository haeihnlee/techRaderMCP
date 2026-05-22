# How to write really good Flutter code

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=O0UjId1VoRU
- **요약 일시**: 2026-05-22 09:06:06

---

## 🔑 핵심 요약
- **Flutter 팀이 제안하는 7가지 코드 품질 기법** — 반응형 UI, DevTools, 위젯 재사용, MVVM, Repository 패턴, 멀티 플랫폼 대응, AI 보조 개발
- **DevTools + Dart/Flutter MCP 서버**로 레이아웃 오류·런타임 에러를 AI 에이전트가 직접 분석/수정 가능
- **Flutter 공식 Skills 저장소**(GitHub)에서 검증된 AI 에이전트 지침을 가져와 본인 프로젝트에 바로 적용

---

## 📣 주요 발표 내용
- **기법 1: 제약 기반 UI 설계** — 고정 크기 대신 `LayoutBuilder`·`MediaQuery.sizeOf` 사용. 절차는 **abstract → measure → branch**
- **기법 2: DevTools 활용** — Inspector가 overflow 위젯을 하이라이트, `Get Runtime Errors`·`Get Widget Tree` 툴로 AI 에이전트가 자동 수정
- **기법 3: 재사용 가능한 위젯** — 비즈니스 로직은 콜백 파라미터로 분리. 위젯이 DB/네트워크/저수준 라이브러리를 import하면 재사용 불가 신호
  - **Widget Previews** 도구로 앱 전체 실행 없이 다양한 상태의 UI를 미리 검증
- **기법 4: 레이어드 아키텍처(MVVM)** — View(위젯) + ViewModel(`ChangeNotifier`) + Data Layer
  - ViewModel 3대 역할: 데이터 변환, 데이터 레이어 호출, UI 리빌드 트리거(`notifyListeners()`)
- **기법 5: Repository 패턴** — 데이터 소스별 단일 진실 공급원. 외부 데이터(서버/DB/플러그인) 접근을 한 곳에 격리
- **기법 6: 모든 플랫폼 대응** — `pub.dev`의 플러그인으로 네이티브 기능(Kotlin/Swift) 추상화. MCP 서버가 pub.dev 실시간 검색으로 최신 API 코드 생성
- **기법 7: AI 보조 개발** — `github.com/flutter/evals`로 Skills·MCP·모델 변경 영향을 데이터 기반으로 검증(오픈소스)

---

## 💡 개발자 포인트
- **위젯 설계 규칙**: 위젯은 `렌더링`과 `사용자 이벤트 수신`만 담당. 데이터 가공/외부 호출은 ViewModel·Repository로 위임
  
> **핵심 원칙**: 위젯이 `import`하는 것이 저수준 라이브러리·HTTP 클라이언트·DB라면 재사용성이 깨진 것. 콜백 파라미터로 빼야 함

- **Dart/Flutter MCP 서버** 설치 시 Antigravity/IDE의 AI 에이전트가:
  - 실행 중인 앱의 런타임 에러를 직접 읽음
  - `hot reload`·위젯 트리 조회로 수정 결과 자체 검증
  - `pub.dev` 최신 패키지 문서를 실시간 fetch → **AI의 학습 데이터 시점 한계를 우회**
- **Flutter Skills 활용**: 공식 저장소의 Skill을 그대로 사용하면 에이전트가 위젯 프리뷰 생성·MVVM 구조 적용을 자동 수행
- **검증된 패턴 우선**: Flutter 팀이 `evals` 프레임워크로 Skill을 회귀 검증 중이므로 자체 프롬프트보다 공식 Skill 신뢰성 ↑

---

## 📅 버전 / 출시 일정
해당 없음 (아키텍처 가이드/도구 소개 세션)

| 리소스 | 위치 |
|---|---|
| Flutter Skills 저장소 | GitHub (Flutter 공식 레포) |
| Evals 오픈소스 | `github.com/flutter/evals` |
| 플러그인 카탈로그 | `pub.dev` |
| MCP 서버 | Dart and Flutter MCP server |


# Flutter notable commits - July 2026

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=auiTKREzsXA
- **요약 일시**: 2026-08-27 09:04:03

---

## 🔑 핵심 요약
- **Flutter Core Packages** 신규 저장소 생성 — 순수 Dart 패키지를 분리해 버그픽스·기능 업데이트 속도 향상
- **Impeller** OpenGL 스타트업 성능 개선 (Samsung Tizen 팀 기여) — Android, Windows, Linux 공통 적용
- **Material UI / Cupertino UI** 패키지 분리 중 호환성 브릿지 제공, 점진적 마이그레이션 가능

---

## 📣 주요 발표 내용

### 패키지 / SDK 구조
- `flutter_core_packages` 신규 레포: 순수 Dart 패키지를 Flutter SDK와 독립적으로 관리
- `listen` 패키지 도입: Riverpod 등 상태관리 라이브러리가 Flutter 의존 없이 통합 가능
- `material_ui` / `cupertino_ui` 패키지 분리 + 구버전 컴포넌트 호환 브릿지 제공
- `add_example` 지시어: pub 패키지에서 실행 가능한 코드 샘플을 API 문서에 내장 가능

### Android
- **이메일 OTP 자동완성** 지원 (`autofillHints`: email OTP code) — MFA 플로우 UX 개선
- 스크롤 가능한 리스트에 native Android platform view 내장 시 iOS에서 발생하던 **클리핑 버그** 수정

### iOS / macOS
- Objective-C → **Swift** 마이그레이션 지속: Engine Swift 코드 IDE 분석 완전 지원
- `KeyboardInsetManager` Swift로 완전 재작성
- CocoaPods 없이 Swift Package Manager 전용 구성 시 **Runner.xcodeproj** 직접 열기 가능
- macOS에서 native 플러그인 간 **상태 값 공유** 기능 추가 (iOS와 동등)

### Impeller (렌더링 엔진)
- OpenGL 임베더 초기화 작업을 **멀티 스레드**로 분산 → 스타트업 성능 향상
- Desktop에서 **획 굵기 / 투명도 렌더링 버그** 수정
- **Firefox** 에서 발생하던 크리티컬 크래시 수정

### 웹
- 모바일 Safari에서 embedded platform view에 터치 제스처 **포인터 추적 버그** 수정
- CJK(한·중·일) 문자 렌더링 폰트 폴백 처리 수정

### 데스크톱
- **멀티윈도우**: `WindowController.isDestroyed` 프로퍼티 추가 — 윈도우 닫힘 감지
- Windows: 클립보드에 잘못된 문자 포함 시 텍스트 잘림 버그 수정
- **Linux에서 Flavors 지원** 추가 — 환경별 리소스 분리 가능

### UI / 애니메이션
- `BoxDecoration`에서 border 속성 **애니메이션** 네이티브 지원 (색상·굵기·스타일 lerp)
- `RawImage` / `RenderImage`에 `blendMode` 파라미터 추가 — 추가 위젯 없이 픽셀 합성 제어
- `AnchoredDraggable` 겹친 드롭 타겟 hit-testing 버그 수정
- `BoxDecoration` / `RenderPhysicalModel` 기하 연산 최적화
- **Tree Sliver** expand/collapse 애니메이션 중 자식 위젯 클리핑 개선
- 양방향 텍스트(RTL+LTR) 선택 핸들 버그 수정

---

## 💡 개발자 포인트

> **Breaking potential**: `material_ui` / `cupertino_ui` 패키지 분리 진행 중. 마이그레이션 전 호환 브릿지를 활용하되, 최종적으로는 신규 패키지로 전환 필요.

> **CocoaPods 제거 시**: Swift Package Manager 전용 구성에서는 `Runner.xcodeproj`를 바로 열 수 있으나, CocoaPods 플러그인이 남아 있으면 기존대로 `.xcworkspace`를 사용해야 함.

- `listen` 패키지 도입으로 Riverpod 등 순수 Dart 패키지의 Flutter 의존성 제거 경로 마련
- Impeller OpenGL 스타트업 개선은 Android 기본 임베더에도 적용 — 별도 작업 불필요
- Flutter 공식 블로그([flutter.dev](https://flutter.dev)) 오픈 — **Jaspr**(Dart 웹 프레임워크)로 구축
- Git worktree를 활용한 멀티 브랜치 기여 가이드 공개 — 스태시 없이 병렬 작업 가능

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|---|---|
| 해당 영상 | Flutter Notable Commits — July 2026 |
| 체험 채널 | Flutter **main** 채널 (stable 릴리스 전 미리 테스트 가능) |
| Flutter 공식 블로그 | 신규 오픈 (flutter.dev, Jaspr 기반) |


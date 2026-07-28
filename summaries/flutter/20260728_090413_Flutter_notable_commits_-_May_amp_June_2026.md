# Flutter notable commits - May &amp; June 2026

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=NR4F9y8uTvw
- **요약 일시**: 2026-07-28 09:04:13

---

## 🔑 핵심 요약
- **Flutter Notable Commits** 월간 영상 시리즈 첫 화 — stable 릴리즈 전에 `main` 브랜치에 랜딩된 주요 변경사항을 미리 소개
- **Material / Cupertino 디자인 라이브러리 분리** 착수: 67만 6천 줄 규모의 mega PR로 코어 프레임워크에서 독립 패키지로 이동
- **Impeller가 전 데스크톱 플랫폼에서 기본 활성화** — 셰이더 컴파일 jank 제거
- **접근성(a11y) 대규모 개선**: Web 핀치 줌 허용, Android TalkBack 네이티브 role 매핑, iOS heading 시맨틱 수정
- 올해 기준 Flutter 프로젝트 누적 컨트리뷰터 **1,700명** 돌파

---

## 📣 주요 발표 내용

### 코어 프레임워크
- **Material / Cupertino 디코플링 mega PR 머지** — 유닛 테스트·예제·수정 포함 **676,000줄**이 메인 레포에서 분리. 두 디자인 라이브러리가 독립 패키지로서 코어와 무관하게 빠르게 진화할 기반 마련
- **hit test 트리를 traversal 트리와 정렬** — traversal parent가 없는 노드를 필터링해, 스크린리더·키보드 내비게이션이 보이지 않는 노드에서 갇히는 **focus trap** 해소
- **커스텀 physics 애니메이션 안전성 개선** — cubic 평가에서 범위를 벗어난 progress 입력이 무한 루프나 렌더링 크래시를 유발하던 버그 수정. 커스텀 spring simulation·bounce 애니메이션이 의도대로 동작
- **root pop 정리** — `Navigator.pop` / `Navigator.maybePop`에 잘못된 타입을 반환하면 모호한 casting exception 대신 **명확한 type mismatch 메시지**를 출력

### 애니메이션 / 스타일링
- `ShapeDecoration`에서 **gradient ↔ 단색(flat color)** 간 morphing 시 발생하던 크래시 수정
- **shape border interpolation이 완전 대칭(symmetric)** 으로 동작 — 역방향 트랜지션도 정방향과 동일하게 매끄럽게 렌더링
- **아랍어 로컬라이제이션 수정** — Calendar·날짜 포맷 위젯에서 숫자 `0`이 사라지던 문제 해결

### Impeller & Flutter GPU
- **Impeller가 모든 데스크톱 플랫폼에서 기본 활성화** — 셰이더 컴파일 jank 제거
- **macOS에서 wide color gamut 기본 활성화** — 지원 하드웨어에서 더 풍부하고 정확한 색 렌더링
- **Flutter GPU에 instance draw 지원** 추가 + 모든 Impeller 백엔드에 instance rendering 도입 → 파티클·나무 등 동일 지오메트리 수천 개를 **단일 GPU draw call**로 렌더링
- **셰이더 번들 hot reload 지원** — 앱 재시작 없이 실행 중 커스텀 셰이더를 편집·재컴파일하고 결과를 즉시 확인
- 3D 경험 관련 업데이트는 연중 지속 예고 (`flutter_scene` 패키지 / Flutter GPU)

### 툴링
- **보안 패치**: Flutter tools의 아카이브 추출기가 `..` 같은 상대 경로로 대상 디렉터리를 벗어나는 zip/tar 파일을 **명시적으로 거부** (path traversal 방어)
- **Windows에서 flavor 지원** 추가 — 빌드마다 코드 파일을 수동 수정하지 않고 환경별 리소스를 분리·설정
- **Widget Preview 도구 개선**: Zoom 슬라이더 추가, 위젯 트리 전체로 preview 스케일링, 서버 사이드 서브프로세스 크래시 방어

### Swift Package Manager
- **federated 플러그인의 기본 패키지를 플랫폼 구현별로 오버라이드** 가능 — 로컬 플랫폼 수정 테스트에 유용
- **add-to-app 문서**에 SPM 셋업 단계별 가이드 추가 (`docs.flutter.dev`)
- **빌드 로그 위생 개선** — SPM 경고가 iOS·macOS 빌드로 제한되어, Android·web 타겟에서는 자동 필터링

### 접근성 (Accessibility)
- **Flutter Web viewport meta 태그를 WCAG 가이드라인에 맞게 수정** — 사용자가 웹 페이지를 **핀치 줌 / 스케일** 할 수 있게 됨 (저시력 사용자 대응)
- **Android**: 프레임워크 semantic role을 네이티브 Android 클래스에 직접 매핑 → **Google TalkBack**이 커스텀 Flutter 컴포넌트를 자연스럽게 읽고 상호작용
- `blockSubtree`로 접근성이 차단된 위젯 서브트리는 **키보드 포커스도 자동 차단** — 숨겨진 모달·배경 콘텐츠에서 키보드 사용자가 포커스를 잃는 문제 방지
- **iOS**: Flutter header 시맨틱을 `UIAccessibilityTraitHeader`에 매핑 — 잘못된 `banner` 안내를 대체
- `obscureText: true`일 때 **spell check 자동 비활성화** — 비밀번호·PIN 등 민감 정보가 외부 스펠체크 서비스나 커스텀 사전으로 유출되지 않도록 보장

---

## 💡 개발자 포인트

- **Material / Cupertino 패키지 분리는 장기적으로 import 경로와 의존성 관리에 영향을 줄 변경**입니다. 이번 PR은 "기반 작업(groundwork)" 단계이므로 지금 당장 앱 코드를 바꿀 필요는 없지만, 향후 릴리즈 노트를 주의 깊게 확인하는 것이 좋습니다.

> ⚠️ **동작 변경 주의**: `Navigator.pop` / `maybePop`의 반환 타입 검증이 강화되어, 기존에 조용히 넘어가던 잘못된 타입 반환이 이제 **명확한 type mismatch 에러**로 드러납니다. 기존 코드에 잠재된 타입 오류가 있었다면 업그레이드 후 표면화될 수 있습니다.

> ⚠️ **Web 접근성 변경**: viewport meta 태그가 핀치 줌을 허용하도록 바뀌었습니다. 줌을 막는 것에 의존한 고정 레이아웃이 있다면 **레이아웃 검증이 필요**합니다.

- **데스크톱 앱 개발자는 지금 `main` 채널에서 테스트를 권장**합니다. Impeller가 기본값이 되었으므로, stable에 도달하기 전에 렌더링 회귀를 발견해 이슈를 제출하는 것이 좋습니다.
- **Flutter GPU 셰이더 hot reload**는 셰이더 작성 생산성을 크게 높입니다 — 재시작 없이 렌더링 변경을 즉시 확인 가능.
- **instance rendering**은 파티클 시스템·대량 반복 오브젝트 렌더링의 성능 병목을 해결하는 핵심 기능입니다.
- **보안**: 아카이브 추출기의 path traversal 취약점이 패치되었으므로, Flutter tools를 최신으로 유지하세요.
- **비밀번호 필드에는 반드시 `obscureText: true`를 사용**하세요 — 이제 스펠체크 유출까지 함께 막아줍니다.
- **접근성 개선 다수가 자동 적용**됩니다 (TalkBack role 매핑, iOS heading, focus trap 해소). 별도 코드 변경 없이 혜택을 받지만, 커스텀 시맨틱을 직접 구현했다면 동작 검증을 권장합니다.

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
| --- | --- |
| 다루는 기간 | **2026년 5월 ~ 6월** (첫 에피소드는 2개월 통합) |
| 발표 주기 | **월 1회** 영상 시리즈 |
| 현재 이용 채널 | `main` 채널 (stable 릴리즈 전) |
| stable 반영 시점 | **다음 stable 릴리즈** (구체 날짜 미발표) |
| 누적 컨트리뷰터 | 올해 기준 **1,700명** |

> 📌 소개된 모든 기능은 **지금 `main` 채널에서 사용 가능**합니다. `flutter channel main` 후 테스트하고 GitHub에 피드백·버그를 제출할 수 있습니다.


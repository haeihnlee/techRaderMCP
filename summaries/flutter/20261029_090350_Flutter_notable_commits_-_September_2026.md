# Flutter notable commits - September 2026

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=mZatSBeh_24
- **요약 일시**: 2026-10-29 09:03:50

---

## 🔑 핵심 요약
- 2026년 9월 Flutter `main` 채널 주요 커밋 정리. 이번 달은 **더 부드러운 스크롤**, **웹 텍스트 선명도**, **Android 보안 강화** 등 완성도 개선이 중심
- `ListView.separated` 의 `itemExtentBuilder` 지원, Impeller 할당 제거 등 **코드 변경 없이 얻는 성능 향상**이 많음
- Android 에서 외부 인텐트로 Dart 진입점·엔진 인수를 바꿀 수 없게 막은 **Breaking Change** 가 있고, Material/Cupertino 지역화 클래스는 **deprecated** 됨

---

## 📣 주요 발표 내용

### 프레임워크 / 위젯
- `DecorationImage` 가 **placeholder** 를 지원해서 이미지 로딩 중 빈 상자 대신 지정한 이미지가 보임
- `FadeInImage` 에 새 `FadeInImageTransition` enum 추가: 순차 전환(placeholder 페이드아웃 → 이미지 페이드인)과 `fadeInOver`(placeholder 위로 바로 페이드인) 중 선택 가능
- `RawScrollbar` 에 마우스 커서 속성이 생겨 데스크톱·웹에서 hover 시 커서 지정 가능
- `ListView.separated` 가 `itemExtentBuilder` 를 지원해서, 항목을 빌드·측정하지 않고 계산만으로 스크롤 위치를 구함. 구분선 있는 긴 목록 스크롤이 부드러워짐
- `MaterialApp.router` / `CupertinoApp.router` 의 라우트가 **FocusScope** 로 감싸져서, 웹에서 자동완성 같은 오버레이가 포커스를 유지함
- `BouncingScrollPhysics` 에 전용 **rubber band 스프링**이 적용돼 iOS 네이티브와 비슷한 오버스크롤 감각
- `TextPainter` 가 라인 메트릭을 캐시해서 가운데·오른쪽 정렬 텍스트 필드에서 ↑/↓ 캐럿 이동이 정확해지고 할당도 줄어듦
- 선택 핸들을 위로 드래그할 때 뷰포트가 하단으로 튕기지 않고 커서를 따라감

### 접근성
- **Escape** 키로 열린 툴팁을 닫을 수 있음 (**WCAG 1.4.13** 충족에 도움)
- `Slider` 에 전용 **semantics role** 이 부여돼 모든 플랫폼 스크린 리더가 올바르게 인식
- 접근성 평가(작은 탭 대상 등)를 테스트 환경뿐 아니라 **라이브 앱**에서도 기능 플래그 없이 실행 가능. 앞으로 DevTools 에서도 지원 예정
- `OverlayPortal` 안의 semantics 경계 문제를 수정해서 메뉴·팝오버를 스크린 리더가 올바르게 강조하고 읽음

### 엔진 / 그래픽
- 그라데이션 + 블러 + 회전이 함께 쓰인 도형이 잘리던 버그 수정
- Cupertino 시트 라우트에서 `BackdropFilter` 와 Material ink decoration 을 함께 쓸 때 모서리가 직각으로 보이던 문제 수정
- **Impeller** 가 원·도형을 그릴 때마다 메모리를 할당하지 않아서 래스터 스레드 부하가 줄어듦
- 불투명 → 투명으로 바뀌는 **애니메이션 WebP/GIF** 디코딩 수정 (5년 된 이슈 해결)
- **Flutter GPU** 가 **2D 텍스처 배열**을 지원해서 여러 레이어를 단일 텍스처로 묶을 수 있음
- 공유 backdrop key 로 여러 배경 필터를 그룹화할 때 생기던 충돌 수정
- 일부 Android GPU 용 밉맵 우회 처리를 영향받는 텍스처에만 적용해서, Adreno 기기에서 축소 이미지가 더 선명해짐

### 웹
- `flutter build web` 의 **웹 콘텐츠 해시 플래그** 공개: 모든 에셋이 콘텐츠 기반 파일명을 가져서 캐시된 구버전 문제가 사라짐
- 브라우저 **safe area inset** 을 view padding 으로 읽음 (노치 폰, 설치형 웹앱)
- iOS Safari 에서 semantics 텍스트 입력란을 **16px** 로 맞춰 탭할 때 페이지가 확대되지 않음
- 글리프를 정수 픽셀 단위로 스냅해서 텍스트 흐림·잘림을 해결하고 래스터 캐싱도 유지
- 이미지가 가끔 검은 상자로 보이던 문제 수정
- 브라우저가 WebAssembly 빌드를 실행할 수 없으면 **JavaScript 로 자동 폴백**

### Android
- 다른 앱이 조작된 **Intent** 로 Dart 진입점·엔진 인수를 바꾸지 못하도록 막음 (보안 개선)
- 지도·웹뷰 같은 **Platform View** 에서 손가락 좌표가 서로 바뀌던 멀티터치 버그 수정
- 제스처를 제어할 때 Android 에 **unbuffered touch event** 를 요청해서 네이티브 뷰 위 스크롤이 부드러워짐 (API 변경 없음)
- 새 프로젝트 템플릿이 **AGP 9.3.1** 과 업데이트된 Kotlin/Gradle 을 사용해 **Android 17** 에 바로 대응
- 시작 중 플러그인이 카메라·비디오 텍스처를 등록할 때 생기던 크래시 수정
- Flutter CLI 가 **launcher activity alias** 를 감지해서 동적 아이콘 앱도 `flutter run` 으로 실행됨 (2019년 이슈)

### iOS
- 하드웨어 키보드로 입력한 **악센트 문자**(프랑스어·스페인어·터키어) 지원
- 엔진이 Apple **Translation API** 를 지원해서 선택한 텍스트 번역 기능의 기반 마련
- 엔진을 뷰 컨트롤러 간에 옮길 때 accessibility bridge 를 다시 바인딩해서 VoiceOver 가 계속 동작
- 엔진 실행 오류 검사를 추가해서 오류 메시지 개선

### 데스크톱 (실험적 Windowing API)
- **macOS**: 창이 콘텐츠에 맞춰 크기를 조절하고, 첫 프레임까지 기다려서 빈 창이 번쩍이지 않음
- **Linux**: 창 장식을 제어하는 새 실험적 API 추가 (커스텀 장식, 투명 배경, 코드로 드래그·리사이즈)
- **Linux Wayland**: 툴팁·팝업이 검은 상자로 보이던 문제와 팝업 리사이즈 시 컴포지터 크래시 수정
- **Windows**: 다중 창 앱에서 **hot restart** 지원, 팝업 위치 변경 크래시 수정, IME 조합(composing) 범위 보존

### 도구 / DX
- 제약 조건이 없을 때 Widget Preview 가 단언문 대신 크기 매개변수를 안내하는 상세 오류를 보여줌
- 플러그인이 알파벳순이 아니라 **의존성 순서**로 등록돼 초기화 순서 버그를 막음
- FFI: **동적 라이브러리 code asset** 지원. 빌드 훅에서 만든 네이티브 라이브러리를 asset ID 로 로드하고 hot reload 도 유지
- 플랫폼 API 가 필요한 새 플러그인 템플릿이 raw MethodChannel 대신 **Pigeon**(타입 안전) 사용
- 앱 생성 템플릿이 분리된 **Material UI 패키지**를 import
- CLI 가 매번 Android SDK 를 스캔하지 않고 필요할 때만 확인해서 일상 명령이 빨라짐
- `flutter analyze` 출력에서 중복 항목 제거
- 대화형 프롬프트에서 디바이스를 고르면 `-d` 플래그 사용을 제안 (2020년부터 요청됨)
- 웹 대상 **golden test** 를 로컬에서 실행 가능
- Chrome 대상 `flutter drive` 가 멈추던 문제 수정

---

## 💡 개발자 포인트
> ⚠️ **Breaking Change (Android)**: 외부 Intent 로 Dart 진입점이나 엔진 인수를 바꿀 수 없게 됐습니다. 이 동작에 의존하는 앱은 마이그레이션 가이드를 확인하세요.

> ⚠️ **Deprecation**: Material·Cupertino 지역화 클래스가 Material UI·Cupertino UI 패키지로 대체될 예정입니다. `dart fix --apply` 로 자동 마이그레이션할 수 있습니다.

- 구분선 있는 긴 목록은 `ListView.separated` + `itemExtentBuilder` 로 스크롤 성능을 개선할 수 있음
- 웹 배포 시 콘텐츠 해시 플래그를 쓰면 캐시 무효화 문제를 해결할 수 있음
- Impeller 할당 감소, unbuffered touch, 웹 글리프 스냅은 **코드 변경 없이** 적용됨
- 새 템플릿이 AGP 9.3.1·Pigeon·Material UI 패키지를 쓰므로, 기존 프로젝트와 설정이 달라지는 부분을 확인할 것
- 플러그인 등록 순서가 의존성 순서로 바뀌었으니, 기존 초기화 순서에 의존하던 코드는 점검 필요
- 이번 기능들은 모두 `main` 채널에서 사용할 수 있으며 stable 릴리스 전 미리보기 성격

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| 대상 기간 | 2026년 9월 커밋 |
| 제공 채널 | `main` (stable 릴리스 전) |
| Android Gradle Plugin (템플릿) | 9.3.1 |
| 대응 Android 버전 | Android 17 |
| 해결된 오래된 이슈 | 애니메이션 WebP/GIF (5년), launcher alias (2019년), `-d` 제안 (2020년) |


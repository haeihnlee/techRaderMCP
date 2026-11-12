# Latest updates, Google AI Edge Eloquent, & much more

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=Qd-SY_16amU
- **요약 일시**: 2026-11-12 09:06:50

---

## 🔑 핵심 요약
- **Flutter Create** 이벤트에서 **Flutter 3.50 / Dart 3.14** 릴리스 발표 (자동 자막 기준, 버전 표기가 3.5/3.50으로 섞여 나옴)
- **Dart native interop 정식 stable**: `ffigen`·`jnigen`·Pigeon 기반으로 네이티브 API에 타입 안전하게 바로 접근 가능
- `material`·`cupertino` 번들 라이브러리 **deprecated** → 별도 패키지 `material_ui`·`cupertino_ui`로 분리, `dart fix`로 자동 마이그레이션
- Canonical이 주도하는 **실험적 멀티 윈도우 데스크톱 API** 공개, **Genkit Dart 1.0**, **MediaPipe pub 패키지** 등 AI 생태계도 확장

---

## 📣 주요 발표 내용
- **Dart 3.14**
  - 새 **Dart migrate 도구**: SDK constraint 갱신, `pubspec` 하한 버전 올리기, 코드 스타일 정리 fix를 자동으로 적용
  - **Analyzer 성능 개선**: 파일 탐색과 시작 속도가 빨라졌고 find references·document color preview 추가 → 대규모 코드베이스에서도 IDE와 에이전트 응답이 빠름
  - **클라이언트 사이드 DartPad** 프리뷰: 브라우저에서 pub 패키지 사용 가능
- **Native interop**
  - Dart native interop 툴체인이 **production ready (stable)**
  - `record_use` 패키지로 **네이티브 바인딩 tree shaking**: 쓰지 않는 바인딩을 제거해 바이너리 크기 감소
- **프레임워크 / 위젯**
  - 번들된 Material·Cupertino deprecated → `material_ui`, `cupertino_ui` 패키지로 분리해 독립 배포
  - 새 **sliver clip 위젯**: sliver 자식을 사각형이나 둥근 모서리로 클립
  - `ListView.separated`에서 `itemExtentBuilder` 지원: 모든 자식을 빌드하지 않고 필요할 때 레이아웃 크기 계산
  - `BoxDecoration`: 주 이미지가 로드되기 전까지 **fallback placeholder 이미지** 표시
- **데스크톱**
  - **실험적 windowing API**: 멀티 윈도우, 윈도우 컨트롤, 라이프사이클 업데이트 (Canonical 설계·구현, Google 리뷰)
  - Canonical은 Flutter의 첫 **governance partner**이자 Linux embedder 주 메인테이너
- **iOS**
  - **Xcode 27 / iOS 27** 이후 첫 stable 릴리스, 새 Apple 요구사항 대응
  - Android 폴더블 경험을 **iPhone duo**에도 적용
  - `flutter screenshot` 명령이 iOS 기기에서 다시 동작 → 에이전트가 변경 전후 UI 확인 가능
- **Android**
  - release 빌드에서 route entry point를 무시하고, cached engine에는 외부 intent extras를 전달하지 않도록 **기본 보안 강화**
  - beta 채널에서 **Hybrid Composition 기본 활성화**: 스크롤 tearing 방지, 텍스트 입력 개선
- **Engine / 그래픽**
  - custom embedder에서 **Vulkan external texture** 지원
  - **Impeller** SDF 렌더링이 선, 얇은 사각형, 그라디언트까지 지원
  - embedder가 메모리 부족을 엔진에 알려 Impeller offscreen 캐시를 비울 수 있음
  - **Flutter GPU**: 2D texture array 지원, 잘못된 pipeline에 명확한 Dart 에러 표시
- **생태계**
  - **Genkit Dart 1.0 stable**: Dart로 풀스택·멀티모달 에이전트 앱 개발 (genkit.dev)
  - AI Edge 팀: Flutter용 **LiteRT / LiteRT-LM** 공식 지원
  - 새 **MediaPipe pub 패키지**: vision, audio, text, decision making, retrieval 등 **20개 태스크**
  - **AdMob 배너 recycling**: iOS 벤치마크에서 **23%** 성능 향상
  - Play Store의 Flutter 앱이 **100만 개** 돌파, 엔터프라이즈 백서 공개
- **세션 예고**: Pigeon 기반 native interop, Google AI Edge Eloquent 사례, **A2UI 1.0**, LG TV용 **webOS SDK** 및 Dart WebAssembly, Dart·Flutter DX 로드맵

---

## 💡 개발자 포인트
> ⚠️ **CocoaPods가 2026년 12월에 read-only로 전환됩니다.** 이번 릴리스부터 Swift Package Manager를 꺼두면 모든 명령에서 경고가 나옵니다. 지금 **SPM으로 옮기세요**.

> ⚠️ Android 플러그인에서 **Kotlin Gradle plugin을 직접 적용하면 곧 빌드가 실패**합니다. built-in Kotlin으로 마이그레이션하세요.

> ⚠️ **Intel Mac** 빌드 시 CLI가 경고를 표시합니다. 이후 릴리스에서 지원이 제거되고 Apple Silicon 전용이 됩니다.

> ⚠️ `material`·`cupertino` import는 deprecated입니다. `dart fix`를 실행하면 `material_ui`·`cupertino_ui` 패키지가 추가되고 import가 자동으로 바뀝니다.

- Hybrid Composition 조건: **Android 14 (API 34) 이상**, **Impeller on Vulkan**. 조건을 충족하지 않으면 기존 platform view 방식으로 자동 fallback
- Hybrid Composition은 앞으로 기본값이 되므로 beta 채널에서 미리 테스트 권장
- 윈도잉 API는 **experimental**이라 바뀔 수 있음. 프로덕션 도입 전에 피드백용으로 먼저 써보기
- 패키지 유지보수자는 Dart migrate 도구로 SDK constraint 갱신 작업을 자동화할 수 있음
- 온디바이스 AI는 LiteRT-LM과 MediaPipe 패키지 조합으로 Eloquent 앱과 같은 스택을 바로 쓸 수 있음
- 업그레이드: `flutter upgrade`

---

## 📅 버전 / 출시 일정
| 항목 | 버전 / 일정 | 비고 |
|------|-------------|------|
| Flutter | 3.50 (stable) | Xcode 27 / iOS 27 대응 |
| Dart | 3.14 | migrate 도구, analyzer 개선 |
| Dart native interop | Stable | `record_use` tree shaking |
| Genkit Dart | 1.0 stable | genkit.dev |
| A2UI | 1.0 | 별도 세션 |
| CocoaPods | 2026년 12월 read-only | SPM 전환 필요 |
| Hybrid Composition | beta 채널 기본 활성화 | Android 14+ / Vulkan |
| Windowing API | Experimental | Canonical 주도 |
| MediaPipe pub 패키지 | 신규 출시 | 20개 태스크 |
| AdMob 배너 recycling | iOS 23% 향상 | 벤치마크 기준 |

> 참고: 자동 자막과 12,000자 절단 때문에 키노트와 윈도잉 세션 도입부까지만 요약에 반영했습니다.


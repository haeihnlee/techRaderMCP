# Flutter at Google I/O 2026 in 5 minutes

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=vNwCw6uVyTg
- **요약 일시**: 2026-05-29 09:03:54

---

## 🔑 핵심 요약
- **Flutter 3.44** 및 **Dart 3.12** 정식 출시, Google I/O 2026에서 발표
- **AI/Agent 통합** 대폭 강화: `agentic hot reload`, Dart/Flutter 에이전트 스킬, On-device Gemma 모델 지원
- **아키텍처 대전환**: Material/Cupertino 라이브러리가 코어 프레임워크에서 분리(deprecate 예정)

---

## 📣 주요 발표 내용

### 🎯 Dart 3.12
- **Firebase Cloud Functions**에서 Dart 공식 지원 → HTTP/Callable Functions를 Dart로 작성 가능
- **Private named parameters**: named constructor 인자로 private 필드 직접 초기화
- **Primary constructors**(experimental): 클래스 헤더에서 인스턴스 변수 직접 선언

### 🛠️ 개발자 경험
- **Widget Previews** (3.35 도입) → **Flutter Inspector** 풀 지원 추가
- **Dart/Flutter Agent Skills** 출시: 코딩 에이전트용 단계별 베스트 프랙티스 지침
- **Agentic Hot Reload**: 별도 설정 없이 코딩 에이전트와 자동 연동

### 🤖 AI 통합
- **`flutter_drama` 패키지**에 Full LiteRT 지원 예정 → **Gemma** 등 모델을 **온디바이스**에서 GPU/NPU 가속으로 실행
- **Dart**(신규 오픈소스 프레임워크): 서버/클라이언트 양쪽에서 동작하는 production-ready agentic 앱용
- **Generative UI SDK**: AI가 텍스트 대신 실시간 UI를 구성/응답하는 패러다임

### 📱 플랫폼별 개선
- **Android**: Hybrid Composition으로 OS 네이티브 레이어 컴포지팅 → 복잡한 네이티브 뷰 렌더링 성능 향상
- **iOS**: **Swift Package Manager**가 모든 프로젝트의 기본값으로 전환 (**Breaking Change 주의**)
- **Web**: WebAssembly 렌더 패스에 **frame arenas** 도입 → jank 제거, **최대 40% 성능 향상**
- **Desktop**: Canonical(Ubuntu) 협업으로 **멀티 윈도우 지원**, 툴팁/별도 다이얼로그 윈도우 네이티브 지원
- **Impeller 엔진**: Signed Distance Functions 도입으로 복잡한 도형의 안티앨리어싱 품질 개선

### 🚗 새 플랫폼 사례
- **Toyota 2026 RAV4** 멀티미디어 시스템에 Flutter 채택
- **LG webOS SDK** 공개 예정 → Firebase, 비디오 플레이어, 게임패드 플러그인 지원

---

## 💡 개발자 포인트

> ⚠️ **Breaking Change**: `material` / `cupertino` 라이브러리가 코어 프레임워크에서 **분리**됩니다. 다음 릴리스에서 기존 라이브러리는 **deprecated** 처리되며, `dart fix`를 통한 마이그레이션이 제공됩니다. Flutter 역사상 가장 큰 아키텍처 전환 중 하나이므로 마이그레이션 계획을 미리 세워야 합니다.

> ⚠️ **iOS 빌드**: Swift Package Manager가 기본값으로 전환되어 기존 CocoaPods 기반 프로젝트는 영향을 받을 수 있습니다.

- **Coding Agent 사용자**라면 새로운 `Flutter Agent Skills`와 `agentic hot reload`를 적극 활용 가능 — 별도 설정 불필요
- **온디바이스 AI**가 필요하면 `flutter_drama` + LiteRT 조합으로 Gemma 모델을 GPU/NPU 가속 실행
- **Web 성능**이 중요한 앱은 새 WASM 렌더러 적용 시 jank 감소 + **최대 40% 성능 부스트** 기대 가능
- **Desktop Flutter**의 lead maintainer가 **Canonical**로 전환 — 장기 로드맵 신뢰도 상승

---

## 📅 버전 / 출시 일정

| 항목 | 버전 / 상태 |
|------|-------------|
| Flutter | **3.44** (Stable) |
| Dart | **3.12** (Stable) |
| Material/Cupertino 분리 | 다음 릴리스에서 deprecated 예정 |
| LG webOS SDK | Coming Soon |
| LiteRT Full Support (`flutter_drama`) | Coming Soon |
| Toyota RAV4 (Flutter 멀티미디어) | **2026년식** 출시 |
| Primary Constructors (Dart) | Experimental |


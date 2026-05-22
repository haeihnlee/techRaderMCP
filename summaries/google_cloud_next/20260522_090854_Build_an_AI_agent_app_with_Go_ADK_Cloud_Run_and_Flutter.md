# Build an AI agent app with Go ADK, Cloud Run, and Flutter

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=zuYmRY4X0rg
- **요약 일시**: 2026-05-22 09:08:54

---

## 🔑 핵심 요약
- **Flutter 앱 + Go 백엔드 + ADK(Agent Development Kit)** 조합으로 가상 피팅룸·스타일링 에이전트 앱(Thread Count) 구현 사례
- **Gemini 2.5 Flash Image** 모델을 활용해 사용자 사진에 의류를 합성하는 Virtual Try-On 기능 제공
- **다중 에이전트 협업**: `Catalog Agent`, `Fitting Room Agent`, `Stylist Agent`가 ADK의 세션·상태·아티팩트로 조율됨

---

## 📣 주요 발표 내용
- **아키텍처 구성**
  - **프론트엔드**: Flutter 크로스 플랫폼 앱 (Web/iOS/Android)
  - **백엔드**: Go 단일 바이너리, **Cloud Run** 배포, 전체가 **ADK Go**로 작성
  - 통신은 평문 HTTP, ADK가 노출하는 **REST API** 사용

- **에이전트 구성 (4개)**
  - `Catalog Agent` — `list_products`, `GetProductImage` 툴로 상품 카탈로그 조회 (YAML 기반, DB/API 교체 가능)
  - `Fitting Room Agent` — `fitting_tool`로 **Gemini 2.5 Flash Image** 호출해 사용자 사진에 의류 합성
  - `Stylist Agent` — 위치/상황 텍스트 기반 코디 추천, 이미지 생성 툴 직접 호출 가능
  - 각 에이전트는 자체 Go 패키지 디렉터리로 분리

- **3단계 호출 패턴**
  1. **Session** 생성 (Fitting Room은 매번 새 세션, Stylist는 sessionId 재사용해 피드백 누적)
  2. **POST `/run`** — `appName`, `sessionId`, `newMessage` 전달. `parts` 배열에 `text` + `inlineData`(Base64 이미지) 포함
  3. **Artifact GET** — 생성 이미지는 **Google Cloud Storage**에 저장되고 응답은 reference name만 반환 → 별도 GET으로 조회

- **ADK 핵심 기능**
  - 툴 호출(Tool Calling), 멀티에이전트 조율, 세션/메모리, **Dev Web UI**(채팅·이벤트 검사·아티팩트 뷰)
  - **Agent 타입**: `LLMAgent`(표준), `CustomAgent`, **Workflow Agent**(`Sequential`/`Parallel`/`Loop`)
  - **Callback** 훅(`before/after run`, `after model response`) — 본 데모는 업로드 이미지 자동 아티팩트 저장에 활용

- **코드 패턴**
  - `main.go`에서 모든 에이전트 생성 후 ADK launcher에 등록
  - 긴 프롬프트는 `instruction.md`로 분리, Go `embed` 패키지로 코드에 주입

---

## 💡 개발자 포인트
- **왜 ADK인가**: Gemini API 직접 호출만으로는 상품 조회·이미지 생성 같은 실제 워크플로우를 구조화하기 어려움. ADK는 **production-ready 시스템**과 단순 모델 호출 사이의 격차를 메워줌
- **상태 공유 패턴**: 에이전트끼리 직접 통신하지 않고 세션의 **key-value state**를 통해 협업
  > 예: Fitting Room이 생성한 이미지의 artifact name을 state에 저장 → Stylist가 그 값을 읽어 사용. 에이전트 결합도를 낮추는 핵심 패턴
- **아티팩트 분리 응답**: 큰 이미지를 응답 body에 직접 싣지 않고 GCS 참조만 반환 → 응답이 가볍고 빠르며 예측 가능
- **툴 시그니처가 곧 LLM 인터페이스**: Go 함수의 입출력 구조체(`ListProductsArgs`/`ListProductsResult`)가 그대로 LLM이 인식하는 스키마가 됨
- **워크플로우 에이전트 선택**: 대부분의 경우 `LLMAgent`로 충분하며, 명확한 순서/병렬/반복 제어가 필요할 때만 Workflow Agent 사용

---

## 📅 버전 / 출시 일정
| 항목 | 값 |
|------|-----|
| 이미지 모델 | `Gemini 2.5 Flash Image` |
| 프레임워크 | ADK Go (Agent Development Kit, 오픈소스) |
| 배포 환경 | Cloud Run |
| 프론트엔드 | Flutter (Web/iOS/Android) |


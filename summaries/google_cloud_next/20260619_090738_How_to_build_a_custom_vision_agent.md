# How to build a custom vision agent

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=U1MQ9RZ0wC4
- **요약 일시**: 2026-06-19 09:07:38

---

## 🔑 핵심 요약
- Mac 웹캠의 **실시간 프레임**을 캡처해 이미지 변환·영상 생성까지 처리하는 **Vision Agent**를 **Google Gemini 생태계**로 구축한 사례
- 표준 Python 앱이 아닌 **Kubernetes 위에서 동작하는 오픈소스 `kagent`** 로 만들어 Cloud-native 마이크로서비스로 오케스트레이션
- **`Nano Banana`(이미지 변환)** → **`Veo 3`(영상+오디오 생성)** 파이프라인을 자연어 한 줄로 호출

---

## 📣 주요 발표 내용
- **실시간 카메라 통합**: 정적 업로드 대신 Mac/iPhone 등 로컬 카메라의 **개별 프레임을 즉시 멀티모달 모델로 전달**
- **`MCP`(Model Context Protocol)** 로 모델에 컨텍스트 전달 → **`fast MCP server`** 에 카메라 제어·AI 엔진을 **callable tool** 로 등록
- 에이전트가 하드웨어 감지(subprocess/MCP tool) → Cloud API 호출 시점 결정까지 **스스로 추론(reasoning)**
- **`Nano Banana`**: 단순 필터가 아닌 **딥 리즈닝 기반 스타일 트랜스퍼**. 얼굴·배경 분석 후 초현실주의 미감 적용하며 **캐릭터 일관성 유지** (`Gemini 3 Pro Image` 기반, **one-shot identity lock**)
- **`Veo 3`**: 변환된 이미지를 시작 프레임으로 **8초 HD 시네마틱 영상** 생성. 물리·모션·**내러티브 오디오**까지 생성(약 2분 소요)
- 드롭다운에 갇히지 않는 **자연어 에이전트** — "make a cinematic video from my latest image" 한 줄로 카메라→Nano Banana→Veo 3 오케스트레이션
- 추가로 **미국 수어(ASL) 실시간 해석 모드**, 가족·개인 사진 업로드 지원

---

## 💡 개발자 포인트
- 단순 Python 앱 대신 **에이전트 아키텍처**를 택한 이유: **자동화 워크플로우 통합**과 **Cloud-native 확장성** 확보
- **`MCP` + `fast MCP server`** 패턴으로 하드웨어(카메라) 제어를 LLM이 직접 호출하는 tool 로 추상화하는 방식 참고 가치 높음
- 복잡한 멀티모달 핸드오프(카메라 ↔ 이미지 생성 ↔ 영상 생성)를 **단일 스케일러블 마이크로서비스**로 묶는 설계
> **`Veo 3` 영상 생성은 프레임당 약 2분**의 추론 시간이 필요 — 실시간 UX가 아닌 비동기 처리 전제로 설계할 것
- 전체 구현이 **오픈소스**로 공개되어 있어 빠르게 시작 가능

---

## 📅 버전 / 출시 일정
| 구성요소 | 모델/기술 | 비고 |
| --- | --- | --- |
| 이미지 변환 | `Nano Banana` (`Gemini 3 Pro Image`) | one-shot identity lock |
| 영상 생성 | `Veo 3` | 8초 HD, 오디오 포함, ~2분 소요 |
| 컨텍스트 전달 | `MCP` / `fast MCP server` | 카메라·AI 엔진 tool 등록 |
| 실행 환경 | `kagent` (Kubernetes) | 오픈소스, Cloud-native |

*구체적 출시 날짜는 영상에서 언급되지 않음*

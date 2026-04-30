# dart_mcp (Package of the Week)

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=tSWu58CX3Ic
- **요약 일시**: 2026-04-30 09:03:27

---

## 🔑 핵심 요약
- `dart_mcp` 패키지는 **Model Context Protocol(MCP)** 서버 및 클라이언트를 구축하기 위한 프레임워크
- **MCP**는 AI 모델을 리소스, 도구, 커스텀 워크플로우에 연결하는 표준 프로토콜
- Dart **Mixin** 기반으로 서버 기능을 쉽게 구성하고, `CallToolRequest`로 도구를 호출하는 구조

---

## 📣 주요 발표 내용

### MCP의 3가지 핵심 구성 요소

- 📦 **Resources** : 로컬 파일, 구조화된 데이터 등 모델에 추가 컨텍스트를 제공
- 🔧 **Tools** : 모델이 특정 액션을 실행하거나 정보를 가져올 수 있도록 지원
- 💬 **Prompts** : 사용자가 미리 정의된 경로를 따라 상호작용하도록 유도

### MCP 서버 구현 방법

- 📌 서버 기능은 **Dart Mixin** 형태로 제공
- 📌 도구 정의 시 `name`, `description`, `inputSchema` 를 지정
- 📌 도구 핸들러 함수는 `CallToolRequest`를 받아 `Future<CallToolResult>` 반환
- 📌 `CallToolRequest.arguments`로 입력 데이터에 접근
- 📌 반환 콘텐츠 타입: **텍스트**, **이미지**, **오디오**, **임베디드 리소스**
- 📌 도구 정의와 구현을 연결하려면 반드시 **도구 등록(register)** 필요

### MCP 클라이언트 사용 방법

- 🔗 `dart run`으로 MCP 서버를 **별도 프로세스**로 실행
- 🔗 `MCP Client` 생성자로 클라이언트 인스턴스 생성 후 서버에 연결
- 🔗 동일 머신: **콘솔 입출력 채널(stdio)** 사용
- 🔗 원격 머신 간 통신: **Stream Channel** (양방향 지속 연결 파이프) 사용
- 🔗 통신 전 반드시 **핸드셰이크(initialize)** 를 통해 프로토콜 선언 및 기능 탐색 수행
- 🔗 `CallToolRequest`에 `toolName`과 `arguments Map`을 담아 서버의 `callTool()` 메서드로 전송

---

## 💡 개발자 포인트

- `inputSchema`의 `properties` 목록과 `CallToolRequest.arguments`의 키가 **반드시 일치**해야 함
- 도구 정의 후 **등록(register) 누락 시** 도구가 동작하지 않으므로 주의

> ⚠️ **주의**: 서버와 클라이언트가 통신하기 전에 반드시 `initialize` 핸드셰이크를 수행해야 합니다. 이 단계를 생략하면 사용 가능한 Tools/Resources/Prompts를 탐색할 수 없어 정상 동작이 불가능합니다.

- 로컬 환경에서는 **stdio 채널**, 원격 환경에서는 **Stream Channel** 을 선택적으로 사용 가능하여 유연한 배포 구성 지원
- 실제 활용 예시: **단위 변환기(imperial ↔ metric)** 도구를 MCP 서버로 구현

---

## 📅 버전 / 출시 일정

해당 없음 (영상 내 구체적인 버전 및 출시 일정 정보 없음)

> 📎 추가 정보: [pub.dev](https://pub.dev) 에서 `dart_mcp` 패키지 및 관련 패키지 확인 가능

# He built a voice controlled drone to avoid using a remote! 🤯✈️

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=afUQpY5oYcw
- **요약 일시**: 2026-09-03 09:08:29

---

## 🔑 핵심 요약
- **Drone Copilot**은 리모컨 대신 음성으로 드론을 제어하는 프로젝트다.
- 실시간 대화형 제어에는 `Gemini Live API`를 사용하고, 프레임의 세부 정보를 확인하는 검사 모드에는 `Gemini Flash`를 사용한다.
- 백엔드는 **Google Cloud Run**에서 실행되며, 실시간 상호작용을 위한 응답성이 핵심 설계 목표다.

---

## 📣 주요 발표 내용
- `Gemini Live API`를 통해 사용자가 드론과 자연스럽게 대화하며 비행 명령을 전달할 수 있다.
- `Gemini Flash`는 드론 카메라 프레임을 더 자세히 분석하는 검사 모드에 활용된다.
- 서버 측 애플리케이션은 `Google Cloud Run`에 배포되어 클라우드 기반으로 동작한다.
- 이 프로젝트는 **Gemini Live Agent Challenge**의 라이브 에이전트 부문 우승작으로 소개됐다.

---

## 💡 개발자 포인트
- 음성 기반 하드웨어 제어에서는 일반적인 챗봇보다 짧은 지연 시간과 안정적인 실시간 상호작용이 중요하다.
- 모든 요청에 하나의 모델만 사용하지 않고, 대화 응답과 시각적 세부 분석에 서로 다른 Gemini 모델을 배치해 기능별로 최적화했다.
- `Cloud Run`은 에이전트 백엔드를 운영하는 간단한 배포 선택지지만, 실제 드론 제어에 적용할 때는 네트워크 지연·명령 검증·안전 정지 로직을 별도로 고려해야 한다.

> 실제 비행 제어에 음성 명령을 연결할 경우 오인식이나 지연이 곧 안전 문제로 이어질 수 있으므로, 위험한 명령에 대한 확인 절차와 수동 제어 fallback을 함께 설계해야 한다.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|---|---|
| 행사 | Google Cloud Next 26, 라스베이거스 |
| 프로젝트 | Drone Copilot |
| 백엔드 | `Google Cloud Run` |
| AI 모델 | `Gemini Live API`, `Gemini Flash` |
| 출시 일정 | 해당 없음 |

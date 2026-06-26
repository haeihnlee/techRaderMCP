# What's new in Cloud Run

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=AoisAy_LGpI
- **요약 일시**: 2026-06-26 09:09:47

---

## 🔑 핵심 요약
- **Cloud Run**을 *바이브 코딩 앱*, *AI 에이전트*, *확장형 앱* 3가지 워크로드의 런타임으로 포지셔닝 (인프라 관리 0, **scale-to-zero**, 사용량 기반 과금)
- 비용 폭주 방지를 위한 **Spend Caps**(월 지출 상한, 초과 시 리소스 자동 일시정지)와 **공식 Cloud Run MCP 서버** 신규 발표
- 2025년 Cloud Run의 외부 월간 활성 개발자·앱 수가 **2배**로 증가, Replit은 Cloud Run 기반 활성 배포가 15만 → **120만** 건으로 성장

---

## 📣 주요 발표 내용
- **AI Studio → Cloud Run 원클릭 배포**: Gemini로 바이브 코딩한 풀스택 앱(React/Three.js)을 `Publish` 버튼만으로 프로덕션 빌드·배포, **HTTPS 엔드포인트** 자동 발급
- **WebSockets 기본 지원**: `socket.io` 기반 멀티플레이어 앱이 별도 설정 없이 동작 (데모에서 600명+ 동시 접속)
- **Spend Caps** 도입: 월 지출 한도를 지정하면 청구액 도달 시 Cloud 리소스 **자동 일시정지** → 바이브 코더의 예산 예측성 확보
- **공식 Cloud Run MCP 서버**(fully managed) 출시
  - AI 개발 도구·에이전트에 연결해 Cloud Run 앱을 배포·관리
  - **container image / zip 파일 / 즉석 파일 콘텐츠** 형태로 배포 가능
  - 데모: **Claude Code**에 공식 Cloud Run remote MCP 서버를 연결, Node.js Hello World 앱을 컨테이너·zip 생성 없이 *파일 콘텐츠 그대로* 전달해 배포
- **AI 에이전트 런타임**으로서의 Cloud Run: harness(brain) + 영속 메모리 + 로컬/원격(MCP) 툴 + **샌드박스**(에이전트 전용 컴퓨터, full Linux 호환) 호스팅에 적합

---

## 💡 개발자 포인트
- 인스턴스 하나로 **동시에 2개 요청 처리**가 가능하고 요청 시간 기반 과금이라, 저비용 실험과 대규모 프로덕션을 같은 플랫폼에서 커버
- AI 에이전트의 코드 실행·파일 조작·컴파일을 위한 **격리된 on-demand 컴퓨터(샌드박스)** 용도로 적합 — full Linux 호환 강조

> ⚠️ 바이브 코딩 앱이 바이럴로 트래픽이 급증하면 비용이 예측 불가해질 수 있음. **Spend Caps**를 설정해 월 지출 상한을 걸어두면 한도 도달 시 리소스가 자동 정지되므로 반드시 활용 권장.

> 💡 에이전트/AI 개발 도구에서 배포 자동화가 필요하다면, 컨테이너를 직접 빌드하지 않고 **공식 Cloud Run MCP 서버**의 *deploy from file content* 경로로 소스를 즉석 전달해 배포할 수 있음.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| ---- | ---- |
| Spend Caps | 신규 발표(launching) |
| 공식 Cloud Run MCP 서버 | 신규 발표(fully managed) |
| AI Studio → Cloud Run 배포 | 데모 시연 |
| 2025 활성 개발자·앱 | 전년 대비 2배 증가 |
| Replit 활성 배포 | 약 15만 → 약 120만 건 (1년) |

(구체적 GA 날짜·버전 번호는 영상에서 언급되지 않음)

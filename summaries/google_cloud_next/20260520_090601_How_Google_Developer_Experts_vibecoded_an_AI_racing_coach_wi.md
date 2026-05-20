# How Google Developer Experts vibecoded an AI racing coach with Gemini

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=VSgKWy2iRWE
- **요약 일시**: 2026-05-20 09:06:01

---

## 🔑 핵심 요약
- **GDE 팀**이 4~6주 만에 **Gemini 기반 AI 레이싱 코치**를 바이브 코딩으로 구현한 사례
- **Gemini Nano(온디바이스)** + **Gemini 3 Pro(서버)** 의 **Hot path / Cold path 이중 구조** 채택
- 주요 개발 도구는 **AI Studio Build Mode**(프로토타입)와 **Antigravity**(IDE 기반 vibe coding)

---

## 📣 주요 발표 내용
- **레이싱 코치 앱 아키텍처**
  - **Hot path**: 주행 중 실시간 피드백 → `Gemini Nano` (오프라인, Chrome 내장)로 "Brake!", "Throttle!" 등 즉시 음성 코칭
  - **Cold path**: 랩 종료 후 패독 복귀 시 → `Gemini 3 Pro`가 전체 주행 데이터 분석 및 다음 랩 코칭 생성
  - **코치 페르소나** 시스템으로 동기부여 톤을 다양화

- **개발 워크플로우**
  - 1단계: **AI Studio**에 텔레메트리 로그 업로드 → Lat/Long, throttle, GPS 좌표 등 데이터 의미 학습
  - 2단계: **AI Studio Build Mode**로 GPS 시각화·UI 프로토타입 제작 → **원클릭 Deploy**로 팀원 공유
  - 3단계: **Antigravity**로 본격 구현 — GPS 센서 드라이버 자동 다운로드/설치 및 Python 추출 코드 작성까지 자동화

- **하드웨어 구성 (v1)**
  - 노트북을 백팩에 넣어 차량 시트에 고정
  - 웹앱 형태로 구동
  - **v2**에서는 **Pixel 폰**으로 이전 + 더 강력한 온디바이스 모델 활용 예정

---

## 💡 개발자 포인트
- **레이싱 같은 환경에서는 Wi-Fi가 끊기므로** `Gemini Nano` 같은 **온디바이스 모델**이 저지연 피드백의 핵심 — 네트워크 의존 UX는 비현실적

> **Antigravity의 강점**: 웹에서 디바이스 매뉴얼을 직접 찾아 드라이버를 설치하고 데이터 추출 코드까지 작성. 임베디드/하드웨어 연동 작업의 진입 장벽을 크게 낮춤.

- **AI Studio Build Mode**의 **원클릭 Deploy + 이메일 공유**는 GitHub 클론·셋업 단계를 생략하게 해 협업 마찰 감소
- **에이전트 평가(Evaluation)는 빌드보다 어려운 문제** — 단순 빌드 이후 평가 파이프라인 설계가 핵심 역량
- **입문자 권장 경로**
  - 비-IDE 사용자 → **AI Studio Build Mode** (갤러리에서 유사 앱 fork)
  - IDE 친숙 사용자 → **Antigravity** 또는 `Gemini CLI`
- 도구 선택 과잉으로 마비되지 말고 **일단 만들어 보는 학습법** 강조

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| v1 (현재) | 웹앱 + 노트북, `Gemini Nano` + `Gemini 3 Pro` |
| v2 (개발 예정) | **Google I/O 이후 시작**, **Pixel 폰** 기반으로 이전 |
| 제작 기간 | 4~6주 (멤버 전원 본업 병행, 저녁·주말 작업) |


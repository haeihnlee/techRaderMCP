# Vibe coding an AI racing coach in 2 weeks

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=3MeM5_s-6Bw
- **요약 일시**: 2026-05-28 09:04:33

---

## 🔑 핵심 요약
- Google **Antigravity** AI 에이전트 하나로 비전문가 GDE 2명이 **단 2주** 만에 AI 레이싱 코치 앱 `Pit Wall`을 제작한 실전 사례
- 클라우드/웹 배경 개발자가 **Kotlin·Android 경험 없이** Antigravity와 대화하며 네이티브 앱(Jetpack Compose)을 0→80%까지 빠르게 완성
- **하드웨어 연동의 진입장벽 제거**: 차량 OBD/`CAN` 버스, GPS 장치를 노트북에 연결하고 Antigravity가 실시간 데이터를 sniffing하며 통신 방법을 직접 알려줌

---

## 📣 주요 발표 내용
- **풀 Google 스택** 구성: **Gemini**, **Gemma 4**, **Jetpack Compose**, **Pixel 10**, **TPU** 칩까지 활용
- 앱 `Pit Wall`은 실제 **Sonoma Raceway** 트랙을 시뮬레이션하며 코너 진입·브레이킹 타이밍을 음성으로 코칭
- **Antigravity**는 단순 코딩 도구가 아닌 범용 **harness** — 앱 개발뿐 아니라 "레이스 엔지니어는 이 문제를 어떻게 생각하는가" 같은 비기술 리서치에도 Google Search 등 툴을 활용해 응답
- 동일 프로젝트를 **PWA → Kotlin 앱 → Jetpack Compose** 여러 버전으로 빠르게 반복 제작 (`Android CLI` 연동)
- 코치 **페르소나** 커스터마이징: 실제 코치 영상을 Antigravity에 넘겨 분석시켜 해당 코치처럼 행동하는 페르소나 생성
- 레이스 전후 **대화형 피드백**(이전 주행 기억, 강·약점 분석) 기능 확장 중

---

## 💡 개발자 포인트
- **전문 분야가 아니어도 제작 가능**: "내가 잘하는 것과 못하는 것"을 솔직히 에이전트에 알려주면, 격차를 메워주며 *동시에* 개발자를 성장시킴 (왜 이렇게 하는지 설명해 줌)
- 하드웨어 디바이스 연동 시 매뉴얼을 일주일 읽을 일을, 에이전트가 **implementation plan**을 먼저 제시 → 검토만 하면 통신 구조 파악 완료
> "0→80%는 매우 빠르다. **80→100%의 폴리싱·파인튜닝이 가장 어려운 구간**이며, 사람들이 가장 고전하는 곳이다."
- 에이전트에게 프로젝트 목표·디바이스·하드웨어·스택을 **먼저 명확히 컨텍스트로 설정**하는 것이 성공/실패를 가른 핵심 ("the unlock")
- TPU SDK 등 신기술 조기 접근은 **GDE 프로그램** 혜택 — 실제 디바이스에서의 검증은 이번 주말 실차 테스트로 이어짐

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 개발 기간 | 약 2주 (few weeks) |
| 프로젝트 시작 | 2025년 10월 (웹 GDE Hammet 합류) / 4월 (클라우드 GDE Simon 합류) |
| 실차 테스트 | Google I/O 주간 토요일, Sonoma Raceway |
| 제작 버전 | PWA → Kotlin 앱 → Jetpack Compose (다중 버전) |


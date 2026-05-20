# Stop over engineering your AI dev setup and just start

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=nupw_OHAL9I
- **요약 일시**: 2026-05-20 09:04:59

---

## 🔑 핵심 요약
- **AI 개발 도구 셋업을 과도하게 최적화하지 말고**, 작은 승리(win)를 쌓으며 점진적으로 확장하라는 조언
- **CLI는 즉답형 질문**, **IDE는 장기 작업**처럼 도구별 사용 시나리오를 분리하면 효율이 올라감
- Google **Developer Knowledge API**가 Cloud/Go/Firebase 등 최신 문서를 통합 제공해 **knowledge cut-off 문제 해소**
- **Antigravity + Stitch + Browser** 같은 에이전트 협업으로 프론트엔드 약점도 극복 가능

---

## 📣 주요 발표 내용
- **Richard Seroter(Google Cloud)** 가 Next 컨퍼런스 GDE 라운지에서 자신의 AI 개발 도구 활용기를 공유
- **CLI 활용 패턴**: 하루 종일 열어두고 일회성 질문에 사용 (예: `Cloud Run worker pools` 배포 방법 즉문즉답)
- **IDE 활용 패턴**: 긴 호흡의 작업, **MCP** 플러그인 연결, 목표 기반 작업에 사용
- **Developer Knowledge API**: 단순 Cloud Docs가 아닌 **Go Docs, Firebase 등 9개 doc set**을 통합 — 개발자는 출처를 신경 쓸 필요 없이 신뢰 가능한 최신 정보 획득
- **에이전트 협업 데모**: `Antigravity`(IDE) + `Stitch`(디자인) + `Browser`(리서치) 조합으로 브랜드 컬러/폰트 리서치 → 디자인 생성 → 앱 빌드까지 단일 프롬프트로 처리
- **언어/프레임워크 진입장벽 붕괴**: 한 달 만에 Flutter, Angular, Go 등 평소 어렵게 느끼던 프레임워크 3~4개로 실제 앱 빌드

---

## 💡 개발자 포인트
- **결과(outcome) 중심 사고로 전환**: "어떻게 만들까"가 아닌 "무엇을 원하는가"에 집중. 점진적 빌드(emergent)의 시간 창이 거의 0으로 수렴
- **학습 루프 가속**: 잘못된 시도를 **4일이 아니라 20분 만에** 폐기 가능 → 더 과감한 실험 가능
- **개인화 학습**: 기본 Hello World 튜토리얼이 아닌 **실제로 만들고 싶은 앱**을 빌드한 뒤 에이전트에게 "어떻게 동작하는지" 질문하며 학습
- **언어 제약 해소**: Python, Go 등 익숙하지 않은 언어도 부담 없이 선택 가능 — 라이브러리/패키지 가용성에 따라 자유롭게 결정

> ⚠️ **흔한 함정**: SNS의 화려한 도구 셋업을 따라 하다 보면 "정작 만든 것은 없음" 상태에 빠짐. 일단 만들고, 승리 경험을 쌓은 뒤 셋업을 키워가는 것이 정답.

- **권장 시작 경로 (웹앱 기준)**:
  - 아이디어 단계 → **Google AI Studio** (인텐트만 입력 → 구현, Firebase Auth/DB 박스 추가 가능)
  - 시스템/애플리케이션 단계 → **IDE (Antigravity 등)** 또는 CLI

---

## 📅 버전 / 출시 일정
해당 없음 (대담 형식 영상으로 구체적 버전/일정 미공개)


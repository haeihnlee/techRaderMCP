# Introducing the TPU agent suite (preview): Open source agents for PyTorch on Cloud TPU

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=hK3xqW_HrP0
- **요약 일시**: 2026-10-29 09:04:52

---

## 🔑 핵심 요약
- Google이 Cloud TPU에서 PyTorch 모델을 온보딩·튜닝·서빙하는 **오픈소스 에이전트 묶음 TPU agent suite**를 **공개 프리뷰**로 출시
- **Torch TPU**로 PyTorch가 TPU에서 네이티브로 돌아가며, 많은 모델은 device를 TPU로 바꾸는 것만으로 실행할 수 있음
- 하나의 **프런트엔드 에이전트**가 요청을 전문 하위 에이전트(온보딩·진단·커널 개발·지식 베이스)로 넘기는 구조이며, 작업은 **근거 기반·범위 제한·검증** 원칙을 따름

---

## 📣 주요 발표 내용
- **TPU agent suite**: 기존 코딩 에이전트에 붙여 쓰는 방식이며, 출시 시점에는 **Claude Code**(자막상 "Cloud Code")와 **Antigravity**를 지원하고 다른 에이전트도 추가될 예정
- 실행 대상: **TPU VM** 또는 **GKE 클러스터**의 Cloud TPU
- 하위 에이전트 구성:
  - **TPU Model Onboarding**: 모델 실행·벤치마크·서빙
  - **TPU Diagnostics**: 모델을 느리게 만드는 병목 찾기
  - **TPU Kernel Development**: 핵심 연산용 커스텀 커널 작성
  - **TPU Knowledge Base**: 하드웨어 관련 질문에 확인 가능한 출처와 함께 답변
- 두 가지 목표: ① 모델을 **실행 가능하게**(서빙 엔진 선택, 메모리 적합성, 출력 정확도) ② 모델을 **빠르게**(병목 분석, 커스텀 커널)
- 온보딩 전에 검색한 내용과 실행 계획을 먼저 보여 주고, 사용자가 진행 방식을 고름
- 공개 위치: GitHub **Google PyTorch** 조직의 `torch TPU`와 함께 제공

---

## 💡 개발자 포인트
- 서빙 온보딩은 매번 같은 체크리스트를 따름:
  1. TPU 확인 및 모델이 메모리에 맞는지 확인
  2. Torch TPU 위에서 `vLLM`을 먼저 시도
  3. `vLLM`이 안 되면 Torch TPU 위의 **기본 PyTorch**로 서빙
  4. 서빙 코드 작성 → 배포 → 상태가 healthy가 될 때까지 대기
  5. **TPU 결과와 CPU 원본 PyTorch 결과를 비교 검증(parity check)** 한 뒤에 엔드포인트 반환
- 커널 튜닝은 **한 번에 하나씩** 진행하고, 결과를 기록하며, **정해진 횟수만큼 시도한 뒤 멈춤**. 시도 내역과 최적 버전을 표로 보여 주고, 다음 단계는 사용자가 결정함
- 사용법: Claude Code나 터미널에 설치한 뒤 TPU를 지정하고 원하는 모델로 바로 테스트

> 아직 **공개 프리뷰** 단계이므로 운영 환경에 쓰기 전에 parity check 결과와 커널 튜닝 결과를 직접 검토하는 것이 좋음

---

## 📅 버전 / 출시 일정
| 항목 | 상태 |
|---|---|
| TPU agent suite | 공개 프리뷰 (오픈소스, GitHub) |
| 지원 코딩 에이전트 | Claude Code, Antigravity (추가 예정) |
| 실행 환경 | Cloud TPU (TPU VM / GKE) |


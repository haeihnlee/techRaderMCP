# Building GPU-accelerated multi-agent apps with Google ADK and Gemma 4

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=vIyhQGBkn34
- **요약 일시**: 2026-05-13 09:05:09

---

## 🔑 핵심 요약
- **Google ADK** 오케스트레이터 + **NVIDIA GPU 가속 추론** + **Milvus 정책 검색** + **Cloud Run 서버리스** 조합으로 멀티에이전트 지속가능성 인텔리전스 앱을 구축
- 위성 이미지·실시간 센서 텔레메트리·정책 문서를 통합하여 의사결정 가능한 리스크 리포트를 즉시 생성하는 시나리오 시연
- 신규 **G4 VM**(NVIDIA RTX Pro 6000 Blackwell 기반) 출시 — 이전 세대 **G2(L4)** 대비 **7배 성능, 4배 GPU 메모리, 3배 호스트 메모리**

---

## 📣 주요 발표 내용
- **AI Hypercomputer 스택** 3계층 구조 소개
  - 목적 특화 하드웨어 (Hopper → Blackwell → Vera Rubin)
  - 오픈 소프트웨어 플랫폼
  - 유연한 소비 모델
- **Cloud Run GPU 서비스**로 실시간 멀티모달 추론 수행 가능
  - `Gemma 4` 모델로 센서 데이터·정책 추천·실시간 텔레메트리 통합 처리
  - 챗봇, IT 지원 에이전트, 이미지 생성 등 다양한 워크로드 지원
- 두 가지 핵심 디자인 패턴 제시
  - **온디맨드 추론 패턴**: Cloud CDN → API → Cloud Run Job → Cloud Storage(LLM weights) → VPC → Cloud Run GPU
  - **파인튜닝/배치 추론 패턴**: `Gemma` 모델을 도메인 특화 데이터로 추가 학습
- **PEFT(Parameter Efficient Tuning)** 기법인 **LoRA** 활용 권장
  - 원본 가중치 동결, 경량 어댑터 레이어만 학습 → 메모리·연산량 대폭 절감

---

## 💡 개발자 포인트
- AI 에이전트 배포 시 직면하는 **3대 인프라 과제**
  - **레이턴시/스루풋**: 가속기 용량 제약 속에서 탄력적 스케일 + 레이턴시 최적화
  - **컴퓨트 효율성**: 유휴 리소스 감소, 밀집도 향상
  - **보안/거버넌스**: 장기 실행 태스크의 감사 추적성·디버깅 가능성 확보

> ⚠️ **에이전트 워크로드는 untrusted로 취급하라.** 버스티 트래픽·레이턴시 민감·장기 실행·유휴 사이클·메모리 집약적 특성이 인프라 취약점을 노출시킬 수 있음

- **Cloud Run**은 서버리스 특성상 에이전트 백그라운드 잡, 미디어 서빙, 비동기 추론에 특히 적합
- **G4 VM**은 멀티 GPU 워크로드 최적화 — 풀 VM에서 **2.2배 NCCL collective 성능** 향상, **프랙셔널 GPU**(1/4/8 GPU) 선택 가능
- **파인튜닝 활용 시나리오**: 도메인 특화 지식 주입(예: SEC 파일링), 태스크 특화 행동, 페르소나/스타일 학습(예: NPC 캐릭터)

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| **G4 VM** | 2026년 초 출시 (NVIDIA RTX Pro 6000 Blackwell 기반) |
| **이전 세대 비교** | G2(L4) 대비 성능 7x, GPU 메모리 4x, 호스트 메모리 3x |
| **CPU** | AMD Turin |
| **GPU 구성** | 1/4/8 GPU 프랙셔널 옵션 + 풀 VM |
| **모델** | Gemma 4 (멀티모달) |


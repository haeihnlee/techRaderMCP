# Google I/O 2025 키노트

- **컨퍼런스**: Google I/O 2025
- **출처**: https://www.youtube.com/watch?v=o8NiE3XMPrM
- **요약 일시**: 2026-04-06 14:40:02

---

## 핵심 요약 (3줄)
- Gemini 2.5 Pro/Flash 성능 대폭 향상, 코딩·추론·멀티모달 전 영역에서 LMArena 리더보드 1위 석권
- 에이전트(Agent) 생태계 확장: 컴퓨터 사용(Computer Use), MCP 호환, 멀티태스킹 에이전트 모드 개발자 공개
- 700만+ 개발자가 Gemini API 활용 중, 1년간 토큰 처리량 50배(9.7조→480조) 급증

---

## Gemini / AI 주요 발표

### 모델 업데이트
- **Gemini 2.5 Pro** (업데이트): LMArena 전 카테고리 1위, WebDev Arena 1위, 코딩 Elo +142점
- **Gemini 2.5 Flash** 신버전: 추론·코드·긴 컨텍스트 벤치마크 개선, LMArena 2위 / 6월 초 정식 출시 예정
- **2.5 Flash-Lite**: 현재 Google 최속 모델, 곧 더 빠른 버전 출시 예정
- **Gemini 2.5 Pro Deep Think**: 병렬 사고 기법 적용, USAMO·LiveCodeBench 최상위권 / 현재 신뢰할 수 있는 테스터 대상 API 제공 중, 정식 출시 준비 중

### 추론 / 사고 기능
- **사고 예산(Thinking Budget)**: 2.5 Flash에 이어 **2.5 Pro에도 도입** (몇 주 내 출시), 사고 토큰 수 세밀 제어 및 비활성화 가능
- **사고 요약(Thought Summaries)**: 모델 추론 과정을 구조화된 형식으로 제공, Gemini API·Vertex AI 지원 → 디버깅·투명성 향상
- 사고 효율성 22% 개선 (동일 성능 대비 사용 토큰 감소)

### 네이티브 오디오 (TTS)
- **2.5 Flash 기반 네이티브 오디오** 오늘 출시 (Gemini API)
- **2화자(Two-speaker) TTS** 최초 지원
- 24개 이상 언어 지원, 언어 간 실시간 전환
- 속삭임 등 미세한 감정 표현 가능
- **Live API**에 네이티브 오디오 대화 기능 오늘 출시, 화자/주변인 음성 구분 가능

### Gemini Diffusion
- 텍스트에 확산(Diffusion) 기법 적용한 실험적 모델
- 현재 최속 모델인 2.5 Flash-Lite보다 **생성 속도 5배** 빠름
- 코딩·수학 성능 동등, 병렬 생성으로 낮은 레이턴시
- 현재 소규모 테스터 그룹 대상 테스트 중

### 보안
- 간접 프롬프트 인젝션(Indirect Prompt Injection) 방어 강화
- Gemini 2.5 → 현재까지 공개된 모델 중 가장 안전

### 월드 모델 / 미래 연구
- **Genie 2**: 단일 이미지 프롬프트로 상호작용 3D 시뮬레이션 환경 생성
- **Veo**: 물리 법칙(중력·빛·물체 상호작용) 이해 수준의 동영상 모델
- **Gemini Robotics**: 로봇 파인튜닝 모델, 물체 파악·지시 수행·새 작업 즉시 적응

---

## Android / 플랫폼 업데이트

### Gemini Live (모바일)
- 카메라·화면 공유 기반 실시간 시각 대화 기능
- **오늘부터 Android·iOS 전체 사용자 무료 제공**

### 개인적 맥락 (Personal Context)
- 사용자 동의 기반으로 Gmail·Drive·Docs 등 Google 앱 전반의 맥락 활용
- **맞춤형 스마트 답장(Gmail)**: 사용자 말투·자주 쓰는 표현·기존 문서 참조하여 답변 자동 생성 → Gmail 구독자 대상 여름 출시 예정
- 검색·Docs·Gemini 앱 등으로 확대 예정

### Google Beam (구 Project Starline)
- AI 기반 2D→3D 영상 변환 플랫폼
- 6개 카메라 + AI 합성 + 60fps 3D 라이트필드 디스플레이, 밀리미터 단위 헤드 트래킹
- **HP와 협업**, 일부 고객 대상 올해 내 도입 예정

### Google Meet 실시간 통역
- 현재 영어·스페인어 지원 (구독자 대상), 수 주 내 추가 언어 지원
- 기업용 실시간 번역 올해 내 제공 예정

### TPU Ironwood (7세대)
- 포드당 42.5 엑사플롭, 전세대 대비 성능 10배 향상
- 추론·사고 특화 설계, 올해 Google Cloud 고객 제공 예정

---

## 개발자 도구 / SDK

### Gemini API 신기능
| 기능 | 상태 |
|---|---|
| 2.5 Flash 네이티브 오디오 TTS (2화자) | 오늘 출시 |
| Live API 네이티브 오디오 대화 | 오늘 출시 |
| 사고 요약 (Pro·Flash) | 출시 중 |
| 사고 예산 - 2.5 Pro | 수 주 내 |
| Computer Use (Project Mariner) | 올 여름 일반 개발자 제공 |
| 2.5 Flash 정식 | 6월 초 |
| 2.5 Pro 정식 | Flash 이후 |

### MCP (Model Context Protocol) 호환
- **Gemini SDK가 Anthropic MCP 도구와 공식 호환** 발표
- 에이전트가 외부 서비스에 접근하는 표준 인터페이스 지원

### Agent-to-Agent 프로토콜
- 개방형 에이전트 간 통신 프로토콜 (Cloud Next 발표)
- 60개 이상 기술 파트너 참여 중

### Project Mariner (Computer Use)
- 브라우저·소프트웨어 제어 가능한 컴퓨터 사용 에이전트
- **멀티태스킹**: 최대 10개 작업 동시 처리
- **Learn & Repeat**: 1회 시연으로 유사 작업 자동 학습
- Automation Anywhere·UiPath 이미 활용 중
- Gemini API를 통해 개발자 제공 (올 여름)

### Jules (비동기 코딩 에이전트)
- GitHub 통합, 백그라운드 자율 코딩 에이전트
- 버그 수정·의존성 업데이트·대규모 코드베이스 리팩토링 처리
- **공개 베타 오늘 발표** → [jules.google](https://jules.google) 가입 가능

### Google AI Studio 개선
- 스케치 이미지 → 코드 직접 변환 (멀티모달 코딩)
- 프로토타입 완성 후 Gemini API 키와 함께 즉시 배포 가능

### 지원 플랫폼
- Android Studio, Firebase Studio, Gemini Code Assist, Cursor 등 주요 IDE에서 2.5 Pro 사용 가능

---

## 기타 주요 발표

- **AI 검색 (AI Overview)**: 월 15억 명+ 사용, AI 모드 차세대 핵심 기능으로 추진
- **Gemini 앱 에이전트 모드**: Zillow 등 외부 사이트 자율 탐색·필터링·일정 예약까지 처리 / 구독자 대상 실험 버전 곧 출시
- **Gemini 앱 MAU**: 4억 명+ (2.5 Pro 사용량 45% 증가)
- **LearnLM 통합**: 교육 전문가 설계 학습 모델이 2.5 Pro에 통합, 학습 분야 LMArena 1위

---

## 개발자에게 중요한 포인트

1. **지금 바로 사용 가능한 것**
   - Gemini API: 네이티브 오디오 TTS (2화자), Live API 오디오 대화, 사고 요약
   - AI Studio: 멀티모달 코딩 프로토타이핑
   - Jules 공개 베타 가입
   - Gemini Live (카메라·화면 공유) Android·iOS 무료 개방

2. **6월~여름 내 출시 예정**
   - 2.5 Flash 정식 (6월 초), 2.5 Pro 정식
   - 2.5 Pro 사고 예산 제어 기능
   - Computer Use API 일반 개발자 공개
   - Gemini 앱 에이전트 모드 (구독자)

3. **비용·성능 트레이드오프 제어 강화**
   - 사고 예산으로 추론 깊이(=비용·레이턴시) 직접 설정 가능
   - Flash-Lite → Flash → Pro → Deep Think 계층별 선택 가능

4. **에이전트 개발 표준화**
   - MCP 호환으로 외부 서비스 연동 간소화
   - Agent

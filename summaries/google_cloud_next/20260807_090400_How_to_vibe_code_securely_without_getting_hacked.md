# How to vibe code securely (without getting hacked)

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=WsNABV2QQXI
- **요약 일시**: 2026-08-07 09:04:00

---

## 🔑 핵심 요약
- **"누가/무엇이 코드를 썼는가"에서 "코드가 얼마나 안정적·안전한가"로 초점을 이동**하는 것이 AI 시대 보안의 핵심
- 코딩 에이전트는 **"똑똑한 인턴"** — 잠재력은 높지만 가이드라인 없이 전권을 주지 않음
- 안전한 AI 코딩 워크플로우 4단계: **Small Batches → Context Engineering → Access Control & Sandboxing → External Verification**
- 에이전트는 기존 프로세스의 **증폭기(amplification)** — 좋은 프로세스든 나쁜 프로세스든 그대로 확대됨

---

## 📣 주요 발표 내용

### 1️⃣ Small Batches (작은 단위 작업)
- **DORA 리서치** 기준, small batch가 코드 안정성의 핵심
- 얻는 것 2가지: **집중된 리뷰**(사람/에이전트 모두 쉬움) + **명확한 의도와 테스트 커버리지**
- 커밋 1개당 사용자 행동을 반영하는 **테스트 1개**
- 에이전트가 작성한 코드도 **반드시 리뷰** — 커밋 전 개발자 또는 에이전트가 검토
- 커밋 전 리팩터링이 가능해져 **PR 부담이 줄고 trunk-based development가 현실적**으로 됨
- 테스트는 에이전트의 **초점을 좁히는 장치** — 무엇을 해결해야 하는지 명시
- 에이전트는 기능/수정 요청을 **red-green-refactor 루프**로 자동 분해

### 2️⃣ Context Engineering (컨텍스트 설계)
- 긴 시스템 프롬프트가 아니라 **프로젝트 전반의 "교전 규칙(rules of engagement)"** 정의
- AI 인턴에게 주는 **스타일 가이드 + 보안 요구사항 + 프로젝트 맥락**
- 예: `Always validate inputs`, `sanitize SQL`
- > **컨텍스트는 식사와 같다** — 영양가 있고 적당한 양이어야 한다. 너무 적거나 너무 많으면 **context collapse**와 과도한 토큰 소비를 유발한다.
- 두 가지 기법:
  - **디렉터리별 컨텍스트 파일** (`GEMINI.md` 등) → 해당 디렉터리의 "로컬 하우스 룰"
    - `auth/` → 세션 처리 규칙 / `payment/` → 서드파티 API 사용 규칙
  - **Skills** → 관련 작업에서만 트리거되는 **모듈형 명령 플러그인**
- 팀 단위로 접근법을 표준화하려면 **Skill이 특히 유용**

### 3️⃣ Access Control & Sandboxing
> **⚠️ 많은 플랫폼이 "샌드박스"라 부르는 것은 사실 그냥 Docker 컨테이너이며, 보안 통제 수단이 아니다.**

- **컨테이너는 user space만 격리** — 호스트 커널로 syscall이 다수 통과 가능 → 컨테이너 탈출 후 호스트 커널 접근 위험
- 진짜 샌드박스: **`gVisor` (Sentry)** — 대다수 syscall을 격리된 실행 계층으로 우회 처리
- 프롬프트와 컨테이너만으로는 부족 → **defense in depth**(에이전트 외부 통제):
  - **granular OAuth scopes**로 최소 권한 원칙(least privilege) 적용
  - 민감한 터미널 명령은 **개발자 확인 요구**
  - 에이전트가 쓰는 **skill과 코드 자체가 악성이 아닌지 검증**

### 4️⃣ External Verification (외부 검증)
- 에이전트가 자기 테스트를 쓰는 것과는 **다른 개념** — 외부 시스템의 peer review
- **결정적(deterministic) 분석**: 기존 도구 여전히 필수
  - **SAST** — 코드 라인 단위 분석
  - **SCA** — 의존성 검사 (외부 라이브러리를 에이전트가 직접 스캔하는 건 비효율)
  - `CI` 파이프라인 또는 `IDE`에서 자동 실행
- **확률적(probabilistic) 분석**: 라인 단위로 찾기 어려운 취약점 대응
  - **business logic 결함**, **authorization bypass** 등
  - 에이전트에게 **적대자(adversary) 역할을 지시** → 단순 취약점 스캔이 아닌 **red teaming**
  - 개별 취약점을 넘어 **아키텍처 전체의 악용 가능성** 확인

---

## 💡 개발자 포인트

- **에이전트를 썼다고 기존 프로세스를 버리지 말 것** — 에이전트는 프로세스의 증폭기일 뿐
- 리뷰 주체는 **개발자 → 에이전트**로 점진적 이행 (에이전트 역량에 익숙해질수록)
- Small batch + 좋은 테스트 커버리지가 있으면, **AI가 만든 보안 패치가 다른 기능을 깨뜨렸는지 즉시 알 수 있음** (실제로 자주 발생하는 문제)
- SAST/SCA의 한계: **"취약점처럼 보인다"만 알려주고 실제 exploit 가능 여부는 판단 못 함** → false positive 다수 → 개발자 마찰(friction) 발생
- 발견된 취약점은 코딩 에이전트에게 수정 지시 가능
- 컨텍스트 파일은 **루트 하나가 아니라 디렉터리별로 분산 배치**하는 편이 토큰 효율과 정확도 모두 유리

> 최종 격언: **"Code with vibes, but verify with tools."**

---

## 📅 버전 / 출시 일정

해당 없음 — 특정 제품 출시가 아닌 보안 워크플로우 방법론 논의

| 언급된 도구/리서치 | 역할 |
| --- | --- |
| **DORA research** | small batch ↔ 안정성 상관관계 근거 |
| **gVisor (Sentry)** | 진짜 syscall 격리 샌드박스 |
| **Docker container** | ⚠️ 사고 방지용, 보안 경계 아님 |
| **SAST** | 코드 라인 단위 정적 분석 |
| **SCA** | 의존성/서드파티 라이브러리 취약점 검사 |
| **GEMINI.md / Skills** | 디렉터리별·모듈형 컨텍스트 주입 |


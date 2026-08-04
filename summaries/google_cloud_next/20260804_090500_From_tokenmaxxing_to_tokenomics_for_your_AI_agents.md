# From tokenmaxxing to tokenomics for your AI agents

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=6LQNHQ7-IcI
- **요약 일시**: 2026-08-04 09:05:00

---

## 🔑 핵심 요약
- **Linux Foundation**이 **Tokenomics Foundation**을 새로 출범 — AI 토큰 비용/가치를 다루는 오픈소스 표준화 조직이며, `FinOps`·`ITAM`·`FOCUS`(Cloud 빌링 스펙)와 같은 "tech value" 우산 아래에 들어간다.
- 초대 수장은 **JR Storment**(FinOps Foundation 창립자). 인터뷰 진행은 Luke.
- 업계가 **"token maxxing"**(토큰 많이 쓰기 경쟁, 사내 리더보드까지 운영) 시대를 지나 **"great token panic"**(예산 초과 → 하드 캡) 국면에 진입했다는 것이 이 세션의 문제 의식이다.

---

## 📣 주요 발표 내용

**Tokenomics Foundation 출범**
- Linux Foundation은 약 **1,200개** 오픈소스 프로젝트를 호스팅. `Linux 커널`, `Kubernetes`(Google 기부), **`MCP`**(Anthropic이 만들어 기부) 등이 대표 사례.
- Tokenomics Foundation은 그중 **tech value** 영역에 속하며, 아직 **정의 자체가 미확립** 상태 — 그래서 표준을 만들려는 것.
- Linux Foundation의 강력한 **antitrust(반독점) 정책** 덕에 경쟁사들을 한자리에 모아 **pre-competitive**(경쟁 이전 단계) 공통 primitive를 합의할 수 있다는 점을 조직의 강점으로 제시.

**"장님과 코끼리" 비유**
- tokenomics를 들으면 대부분 "토큰 비용" 한 조각만 떠올리지만, 그건 코끼리 코만 만진 것.
- 목표는 CNCF Landscape처럼 **전체 그림(whole picture)**을 그려서 서로 다른 관점을 가진 사람들을 모으는 것.

**Gen AI 시대 구분 (발표자 관점)**
- **before times** — FinOps Foundation 콘퍼런스 시작(2022, Austin), OpenAI 첫 모델 출시 직전.
- **old days of Gen AI** — 챗봇이 말을 알아듣고 LLM이 꽤 괜찮은 코드를 쓰기 시작한 시기.
- **good old days of AI** — 신모델 대량 출시 이후. **구독제 / all-you-can-eat AI / token maxxing**의 시대.
- **great token panic** — 예산 초과가 현실화되며 **guardrails**와 **hard cap**이 등장한 현재.

**현장 에피소드**
- Fortune 50 기업의 글로벌 CIO가 직접 *"토큰 예산은 무제한"*이라고 말한 사례.
- **Linus Torvalds**가 처음엔 "vibe coding은 중요한 일에 쓰지 말라"고 공개 발언했다가, 신모델 출시 후 불과 몇 달 뒤 **본인의 첫 코딩 프로젝트를 공개**하며 입장을 바꾼 사례.
- 30년간 매일(주말 포함) 코드를 쓴 principal engineer가 이 시점부터 **직접 코딩을 멈추고 "코드를 관리"하는 역할로 전환**했다는 증언.

---

## 💡 개발자 포인트

- **무한 루프는 돈을 태우는 가장 쉬운 방법이다.** 에이전트에 루프를 허용할 때 반드시 종료 조건과 반복 상한을 걸어야 한다.
- 측정 지표가 곧 행동을 만든다 — 발표자의 표현대로 *"깨진 창문 개수로 평가하면 창문이 많이 깨진다."* **토큰 사용량을 KPI로 삼으면 낭비가 KPI가 된다.**

> ⚠️ 실제 관측된 진행 패턴: **CTO "예산이 터졌다" → CEO "이 지출에서 가치가 나오는지 모르겠다" → 하드 캡 도입.** 캡이 걸리기 전에 사용량 계측과 가치 측정 체계를 먼저 갖춰두는 편이 낫다.

- 그렇다고 **전면 중단은 답이 아니다.** AI가 실제로 워크플로를 크게 개선한 영역이 분명히 존재하므로, "다 끄기"와 "매출 전부를 토큰에 쓰기" 사이에서 선을 그어야 한다.
- 실무 과제는 결국 **guardrails 설계** — 사용량 가시성, 예산 forecast, 팀별 한도, 그리고 "이 토큰이 실제 가치를 냈는가"를 판정하는 기준.
- `value`는 정의하기 어려운 단어라는 점을 인터뷰어도 지적 — 조직마다 가치 정의를 먼저 합의하지 않으면 tokenomics 논의가 공허해진다.

---

## 📅 버전 / 출시 일정

| 시점 | 내용 |
| --- | --- |
| 2022 | FinOps Foundation 콘퍼런스 시작 (Austin, Texas) — "before times" |
| 2023-01 ~ 2025-11 | "old days of Gen AI" — 챗봇/코드 생성이 쓸 만해진 시기 |
| 2025-11 | 주요 프로바이더 신모델 대량 출시로 품질이 "pretty good → really good"으로 전환 |
| 2025-11 | Linus Torvalds 공개 발언: *"vibe coding, 중요한 일에는 쓰지 말라"* |
| 2026-01경 | Linus Torvalds가 첫 코딩 프로젝트 공개 (입장 전환) |
| 2026-04경 | "great token panic" 시작 — 토큰 사용량 급증 |
| 2026-06 | 다수 기업의 토큰 지출이 forecast 초과, 하드 캡 도입 사례 등장 |
| 인터뷰 기준 "지난주" | **Tokenomics Foundation** 공식 출범 |

> ℹ️ 원본 자막이 중간에 잘려 있어(글로벌 토큰 성장 그래프 설명 부분에서 종료) 후반부 내용은 이 요약에 포함되지 않았습니다.


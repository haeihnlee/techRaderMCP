# Google Cloud Live: Next '26 Developer keynote deep dive

- **컨퍼런스**: 기타
- **출처**: https://www.youtube.com/watch?v=JemyjTlOvy0&pp=0gcJCQMLAYcqIYzv
- **요약 일시**: 2026-05-07 10:18:58

---

## 🔑 핵심 요약
- **Google Cloud Next '26** Day 2 개발자 키노트 후속 라이브 방송. **Replit**의 **Michele Catasta** (President & Head of AI)가 게스트로 출연
- 핵심 메시지: **"개발자는 에이전트의 매니저가 된다"** — IDE에서 코드를 응시하는 시대가 끝나고, 자연어로 에이전트 무리를 지휘하는 **"vibe coding"**이 주류
- **Replit Agent + Google Cloud** 통합 가속 — 사용자가 인지하지 못하는 사이 `Cloud SQL`, `BigQuery` 등 GCP 인프라가 백엔드로 붙는 방향

---

## 📣 주요 발표 내용

- **Replit Agent 회고**: 1.5년 전 첫 버전은 내부 도구를 만들 만큼도 안 됐지만, 현재 회사 내부 업무 시간의 **50% 이상**이 Replit으로 만든 사내 도구에서 처리됨 (도그푸딩)
- **Gemini의 두 가지 강점**:
  - **멀티모달리티**: 이미지·비디오를 raw로 던져도 의도 파악
  - **대형 컨텍스트 윈도우**: "Swiss army knife"로 표현
- **Agentic Canvas**: Gemini로 디자인 → 코드 생성을 한 캔버스에서 처리
- **GCP 네이티브 통합 로드맵**: AWS는 이미 네이티브 레이어로 제공, DB는 GCP 직접 액세스. 앞으로 **모든 GCP 제품을 사용자 모르게 백엔드로 자동 연결**
- **Auth는 의견 있는 디폴트로 처리**: 보안의 기초 요소이므로 Replit이 강한 디폴트를 가져가고 GCP 베스트프랙티스로 유도
- **엔터프라이즈 트렌드**: SaaS 벤더에서 솔루션을 사기보다 Replit으로 사내 도구 직접 빌드하는 패턴 부상

---

## 💡 개발자 포인트

- **IDE → 에이전트 인터페이스 전환은 진행 중인 사실**. 코드를 직접 응시하지 않는 "빌더" 사용자가 주류가 되고 있고, 이들에게 IDE는 **올바른 product surface가 아님**
- > "Frontier 모델 발전 속도가 너무 빨라서 18개월 로드맵을 세우는 게 무의미하다 — 3개월 앞도 야심찬 수준" — Replit의 제품 전략 발언이지만 모든 AI 제품 팀에 시사점이 큼
- 사내 도구 빌드 비용이 SaaS 구독을 대체할 만큼 떨어지면 **enterprise SaaS 시장 구조가 흔들릴 가능성** — "build vs buy" 균형이 build 쪽으로 이동
- > **Auth·DB·serverless 같은 high-stakes 영역은 의견 있는 빌더(Replit·GCP)가 책임지고, 사용자는 모르고 써도 enterprise-grade 보안을 받는 모델** — 이것이 "vibe coding"이 가능해진 전제 조건
- Gemini 3 발표 이후 전체 코드베이스 컨텍스트 이해·디자인 생성 능력이 한 단계 도약했다는 평가

---

## 📅 버전 / 출시 일정

해당 없음 (대담 포맷, 구체적 출시 일정 미공개)


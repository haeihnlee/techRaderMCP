# How to build and scale multi-agent AI systems on GKE

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=zI8KUvtHMvU
- **요약 일시**: 2026-08-27 09:06:23

---

## 🔑 핵심 요약
- **GKE(Google Kubernetes Engine)** 위에서 멀티 에이전트 AI 시스템을 구축·운영하는 3가지 실습 랩 공개
- **Agentspace CLI** (`agi` 명령)를 활용해 Kubernetes 인프라 트러블슈팅을 AI 에이전트로 자동화
- AI 컨텍스트 사다리 개념 — 0 컨텍스트 → 로컬 컨텍스트 → MCP 서버 연동으로 단계적으로 에이전트 능력 향상

---

## 📣 주요 발표 내용
- **Lab 1** — AI 에이전트로 GKE 인프라 트러블슈팅 및 신규 인프라 배포 자동화
- **Lab 2** — GKE 위에서 AI 에이전트가 생성한 **신뢰할 수 없는 코드(untrusted code)를 안전하게 실행**하는 방법 (샌드박싱)
- **Lab 3** — 대규모 개인 데이터를 정리·분석하여 **Knowledge Graph** 구축
- `agentspace CLI`(단축 명령 `agi`)는 **Gemini 3.7 Flash** 기반, 로컬 파일/디렉터리 컨텍스트와 터미널 명령 실행 툴 내장
- 모든 명령 실행 전 사용자 동의 프롬프트(`proceed once / always / not at all`) 표시 → 안전한 자율 실행
- **MCP 서버**와 스킬/에이전트 플러그인 연동으로 컨텍스트 확장 가능
- 랩 자료는 기간 제한 없이 온라인 공개 예정

---

## 💡 개발자 포인트
- 일반 웹 AI 어시스턴트(Gemini Web 등)는 프로젝트 컨텍스트가 없어 막연한 답변만 제공 → `agentspace CLI`는 로컬 파일/환경을 직접 읽어 **정확한 원인 진단** 가능
- `kubectl describe`, `kubectl logs` 등 읽기 전용 명령은 AI가 자동 실행하고 결과를 분석하여 Root Cause 파악
- Untrusted 코드 실행 시 GKE 샌드박스 기능을 활용해 인프라 피해를 차단
> **Breaking Change 아님**: `agentspace CLI`는 신규 도구이므로 기존 워크플로우에 추가적으로 도입 가능. 단, 터미널 명령 실행 권한 동의 정책을 팀 내 가이드라인으로 정의할 것을 권장.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 발표 시점 | Google Cloud Next 2025 (5~6월 오프라인 투어 후 온라인 공개) |
| 사용 모델 | Gemini 3.7 Flash |
| 랩 제공 기간 | 무기한 (온라인 공개) |


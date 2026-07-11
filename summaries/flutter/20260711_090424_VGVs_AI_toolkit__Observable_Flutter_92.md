# VGV's AI toolkit | Observable Flutter #92

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=zhiK0YLLIp0
- **요약 일시**: 2026-07-11 09:04:24

---

## 🔑 핵심 요약
- **VGV**(Very Good Ventures)가 만든 두 개의 **Claude Code 플러그인**을 소개: `flutter` 플러그인과 `wingspan` 플러그인
- `flutter` 플러그인은 Flutter/Dart 전용, VGV의 오피니언 있는 아키텍처·베스트 프랙티스를 담음
- `wingspan`은 **기술 비종속(tech-agnostic)** 플러그인으로, 브레인스토밍·계획(planning)·기능 분리 등 기술 스택과 무관한 개발 워크플로우를 지원

---

## 📣 주요 발표 내용
- VGV는 오랫동안 Flutter 생태계에 오픈소스 패키지·CLI·분석 도구를 제공해온 팀으로, 이번엔 그 내부 지식을 AI 플러그인 형태로 정리
- `wingspan`에는 **brainstorming skill**, **planning skill** 등이 포함되어, 개발자가 작업을 시작하기 전에 요구사항을 쪼개고 계획을 리포지토리에 먼저 커밋해 다른 팀원과 공유 가능
- `wingspan`은 프로젝트 내 `pubspec.yaml` 같은 파일을 감지해 **Flutter 프로젝트임을 자동으로 인식**하면, `flutter` 플러그인 설치를 추천하는 **recommended plugins** 메커니즘을 가짐 (JSON 설정으로 다른 플러그인을 참조)
- `wingspan`은 Flutter가 아닌 프로젝트(예: Astro 리포지토리)에서도 정상 동작 — 브레인스토밍/플래닝 프로세스 자체가 기술 비종속이기 때문
- `flutter` 플러그인에는 VGV 방식의 **아키텍처 가이드**가 포함되어 있어, `wingspan`으로 계획 단계를 진행할 때 Flutter 프로젝트라면 이 아키텍처 규칙까지 함께 반영됨

---

## 💡 개발자 포인트
- 두 플러그인은 **함께 설치 시 시너지**: `wingspan`이 프로젝트 컨텍스트를 감지해 `flutter` 플러그인의 스킬을 자동으로 끌어다 씀
- AI 에이전트가 큰 기능을 한 번에 처리하지 못하는 문제를 막기 위해, **기능을 작은 단위로 쪼개는 습관**(브레인스토밍 → 플래닝 → 빌드)을 플러그인 스킬로 구조화한 점이 핵심
- 팀 협업 관점에서, 계획을 코드가 아닌 **리포지토리에 문서로 먼저 남기는 방식**은 여러 개발자가 같은 기능을 동시에 작업할 때 컨텍스트 공유에 유용

> VGV는 향후 recommended plugins 목록을 확장해 다른 기술 스택(웹, 네이티브 등)에 대한 감지·추천도 추가할 계획이라고 언급함 — 아직은 Flutter/Dart 감지만 지원.

---

## 📅 버전 / 출시 일정
해당 없음 (플러그인 저장소/설치 방법은 영상 내 별도 데모에서 다룸)


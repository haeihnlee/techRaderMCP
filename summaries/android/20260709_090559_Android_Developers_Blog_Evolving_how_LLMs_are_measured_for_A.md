# Android Developers Blog: Evolving how LLMs are measured for Android: the next era of Android Bench

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/07/android-bench-llm-measurement.html
- **요약 일시**: 2026-07-09 09:05:59

---

## 🔑 핵심 요약
- Google이 **Android Bench**(안드로이드 개발 작업 기반 LLM 리더보드)를 **Harbor 프레임워크**로 전면 개편하고, 평가 에이전트를 교체해 전체 모델을 재측정했다.
- 이번 7월 릴리스에서 `Claude Fable 5`, `Claude Sonnet 5`, `Claude Opus 4.8`, `GLM 5.2`, `Kimi K2.7 Code`, `MiniMax M3`, `Qwen 3.7 Plus`, `Qwen 3.7 Max` 등 신규 모델 8종이 리더보드에 추가되었다.
- 이제 커뮤니티가 직접 **벤치마크 태스크를 제출**하거나 **자체 평가 결과를 공유**할 수 있도록 개방되었다.

---

## 📣 주요 발표 내용
- 기존에는 범용 벤치마킹 에이전트인 **mini-swe-agent v1**을 안드로이드 개발에 맞게 커스터마이징해 사용했으나, 이번에 **Harbor 프레임워크**로 표준화하며 평가 에이전트도 함께 업데이트됨.
- Harbor는 누구나 벤치마크를 실행·평가·공유할 수 있는 표준/통합 체계를 제공해 투명성을 높임.
- 전체 모델을 새 방법론으로 **재실행(re-run)** 하여 새로운 기준선(baseline)을 수립.
- 리더보드 순위(주요 모델):

| 순위 | 모델 | 점수 |
| --- | --- | --- |
| 1 | `Claude Fable 5` | 84.5 |
| 2 | `GPT 5.5` | 80.2 |
| 3 | `Claude Sonnet 5` | 76.2 |

- Open-weight 모델 중에서는 `GLM 5.2`(72.2)가 1위, `Kimi K2.7 Code`(70.4)가 2위.
- 평가 항목에는 **Jetpack Compose 마이그레이션**, **웨어러블 네트워킹**, **플랫폼 API 업데이트** 등 안드로이드 특화 시나리오가 포함됨.

---

## 💡 개발자 포인트
- 안드로이드 개발 워크플로우에 AI 어시스턴트/에이전트를 도입할 때, Android Bench 리더보드를 참고해 **작업 성격에 맞는 모델**을 선택할 수 있다.
- 개발자 커뮤니티가 직접 참여 가능한 두 가지 방법이 새로 열림:
  - 자신의 안드로이드 개발 시나리오를 **태스크로 제출**해 벤치마크 데이터셋 확장에 기여
  - `Harbor Hub`에서 데이터셋을 활용해 원하는 모델로 **직접 평가 실행 및 결과 공유**

> ⚠️ 평가 방법론(Harbor 도입)이 바뀌면서 **점수 체계에 소폭 변동(minor shift in scoring)** 이 발생했다. 과거 점수와 직접 비교 시 주의가 필요하며, 이전 기록은 웹사이트의 archive에서 별도로 확인 가능하다.

---

## 📅 버전 / 출시 일정

| 시점 | 내용 |
| --- | --- |
| 2026년 3월 | Android Bench 최초 공개 |
| 2026년 7월 (이번 릴리스) | Harbor 프레임워크 도입, 신규 모델 8종 추가, 커뮤니티 기여 오픈 |


# Android Developers Blog: Tinder cuts app cold starts by 47% with new R8 Configuration Analyzer

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/08/tinder-app-cold-start-r8-configuration-analyzer.html
- **요약 일시**: 2026-08-19 09:07:23

---

## 🔑 핵심 요약
- **R8 Configuration Analyzer**를 활용해 Tinder가 앱 콜드 스타트를 **47% 단축**
- 과도하게 넓은 keep rule을 제거하여 R8 최적화 점수를 28% → 50%로 향상
- APK 다운로드 크기 **28.98% 감소** (86.6MB → 61.5MB), 사용자 인식 ANR 오류 **28% 감소**

---

## 📣 주요 발표 내용
- **R8 Configuration Analyzer**: 코드 축소(shrinking), 최적화(optimization), 난독화(obfuscation) 점수를 추적하여 최적화 가능한 영역을 시각화
- Tinder는 인하우스 라이브러리에 아래와 같은 광범위한 keep rule이 있었음을 발견:
  ```
  -keep public class * {
      public protected *;
  }
  ```
  이 규칙이 전체 앱의 모든 public 클래스 최적화를 차단하고 있었음
- Analyzer가 제공하는 주요 지표:
  - **Shrinking Score**: R8 코드 축소 가능 비율
  - **Optimization Score**: 메서드 인라이닝·클래스 병합 등 최적화 가능 비율
  - **Obfuscation Score**: 클래스·메서드·필드 리네이밍 가능 비율
- DEX 파일 수 17개 → 11개 (스타트업 전용 파일 3개 → 2개)로 감소
- CI/CD 파이프라인에 최적화 통계 변화 리포팅 작업을 추가하여 지속적 모니터링

---

## 💡 개발자 포인트
- 내부 라이브러리의 keep rule도 반드시 감사(audit)할 것 — 잘 알려진 서드파티 라이브러리와 달리, 사내 "안정적" 라이브러리가 오히려 광범위한 규칙으로 최적화를 막는 경우가 많음
- reflection이 실제로 필요한 특정 클래스·메서드에만 keep rule을 적용하도록 범위를 좁힐 것
- 사용하지 않는 규칙(zero match), 중복 규칙, 이미 상위 규칙에 포함된 규칙(subsumed)을 제거

> **Breaking point**: 과도한 keep rule은 단순한 크기 증가에 그치지 않고 ANR 증가와 직접 연결됨. 저사양 기기가 많은 신흥 시장에서 사용자 이탈의 핵심 원인이 됨.

- **R8 Analyzer skill**이 배포되어 agentic 개발 워크플로우에서 자동으로 최적화 리포트 요약 가능

---

## 📅 버전 / 출시 일정

| AGP 버전 | 사용 방법 |
|---|---|
| **AGP 9.3+** | 릴리스 빌드 시 자동 생성 (`build/outputs/mapping/release/configanalyzer.html`) |
| **AGP 9.3+ (단독)** | `./gradlew :app:analyzeReleaseR8Config` — 전체 릴리스 빌드 없이 리포트 생성 |
| **AGP 9.3 미만** | R8 버전을 `9.3.7-dev` 이상으로 독립 업그레이드 후 `-Dcom.android.tools.r8.dumpkeepradiushtmltodirectory=<dir>` 플래그로 실행 |

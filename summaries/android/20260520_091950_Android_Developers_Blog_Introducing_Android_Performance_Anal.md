# Android Developers Blog: Introducing Android Performance Analyzer : The Next Evolution in Profiling for Android

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/introducing-android-performance-analyzer.html
- **요약 일시**: 2026-05-20 09:19:50

---

## 🔑 핵심 요약
- **Android Performance Analyzer (APA)** 오픈 베타 출시 — Android 앱·게임 성능 분석을 위한 차세대 프로파일러
- **Perfetto** 기반 System Profiler로 CPU/GPU/메모리/전력 통합 분석, **Vulkan** 게임 엔진 최적화에 특화
- **Android Studio Panda 4 canary** 통합 + **Windows/MacOS/Linux** 크로스플랫폼 standalone 데스크탑 앱 동시 제공

---

## 📣 주요 발표 내용
- **두 가지 배포 형태**
  - 독립 데스크탑 앱: Android Studio·Gradle 없이 사용 가능, 내장 Vulkan 레이어 + 심층 GPU 카운터 분석 지원
  - Android Studio의 **System Trace viewer** 업데이트 형태로 통합 (Panda 4 canary 이상)
- **개발 파트너십**: Samsung Austin Research Center(SARC) + LunarG 공동 개발, 그래픽 캡처/재생은 LunarG의 **GFXReconstruct** 사용
- **딥다이브 시스템 분석**
  - CPU 코어 주파수·스케줄링, 프로세스/스레드 활동 검사
  - **Qualcomm, Arm, Imagination, Samsung** 하드웨어 전반의 GPU 퍼포먼스 카운터 데이터 제공
  - `SurfaceFlinger` 이벤트로 렌더링·디스플레이 컴포지션 파이프라인 가시성 확보
- **워크플로우 기능**
  - 탭 인터페이스 & split window로 trace 간 비교
  - 프로젝트 기반 워크플로우로 A/B 테스트·종단 테스트 결과 통합 관리
  - 성능 오버헤드 없이 trace 중 스크린샷 캡처 → 타임라인 시각적 스크러빙
- **AI 에이전트 통합**
  - **Perfetto SQL skill** 제공 — AI 에이전트로 custom SQL 쿼리 생성
  - **Perfetto Analysis skill** — "왜 앱 시작이 느린가?" 같은 고수준 질문에 Gemini가 분석
- **Vulkan 디버그 마커**: 코드베이스의 Render Pass 이름을 trace 트랙에 직접 표시
- **속도 개선**: trace 렌더링이 Android GPU Inspector 대비 **6x ~ 26x 빠름**, 대용량 trace 안정성 향상

---

## 💡 개발자 포인트
- Vulkan 사용 게임 엔진 개발자에게 특히 유용 — **GPU 카운터 + 렌더 스테이지**를 세밀하게 추적 가능
- 기존 `Perfetto` trace 파일을 그대로 열 수 있어 마이그레이션 부담 최소화
- `vkCmdBindDescriptorSets` 배칭 같은 실전 최적화 사례 제공 (The Forge: CPU 설정 비용 **~50% 절감**, 발열 **2-3x 감소**)
- NetMarble *Seven Deadly Sins: Origin* 사례: 셰이더 정밀도 조정·업스케일링으로 일부 씬 GPU 비용 **최대 90% 절감**
- AI 스킬을 활용하면 **Perfetto SQL 스키마/문법 암기 없이도** 커스텀 분석 가능

> ⚠️ **베타 소프트웨어**입니다. 버그 발생 시 `Help Menu > Submit a bug report`로 리포트 권장.

> 📌 **Android 12+** 디바이스에서 시스템 전반 성능 캡처 및 GPU 카운터·렌더 스테이지를 가장 잘 지원합니다. 그 이하 버전은 일부 기능 제한 가능.

---

## 📅 버전 / 출시 일정
| 항목 | 정보 |
| --- | --- |
| 발표일 | 2026년 5월 19일 |
| 발표 행사 | Google I/O 2026 |
| 상태 | 오픈 베타 |
| Standalone 다운로드 | `developer.android.com/android-performance-analyzer` |
| Android Studio 통합 | **Panda 4 canary** 빌드 이상 |
| 지원 OS | Windows, MacOS, Linux |
| 권장 Android 버전 | **Android 12+** (시스템 전체 성능 캡처 최적화) |


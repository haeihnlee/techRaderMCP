# From notebook to production: Serving JAX at scale

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=EMwtNr7qTHE
- **요약 일시**: 2026-08-27 09:08:47

---

## 🔑 핵심 요약
- **JAX 모델을 프로덕션에 서빙**할 때 선택할 수 있는 4가지 패턴(`jax.jit`, AOT 컴파일, `jax.export`, `jax2tf`)을 소개
- 노트북에서 잘 동작하던 모델도 서빙 시 첫 호출 **컴파일 스파이크**가 발생할 수 있으며, 이를 해결하는 방법을 단계별로 설명
- 핵심 정신 모델: **JAX traces → XLA compiles → NVIDIA stack runs** (4계층을 기억하면 이슈 디버깅이 쉬워짐)

---

## 📣 주요 발표 내용
- **`jax.jit`** — 가장 간단한 인프로세스 방식, Python 서비스에 적합하지만 첫 호출 시 컴파일 발생 → 실 트래픽 전 **웜업 필수**
- **AOT(Ahead-of-Time) 컴파일** — `lower()`로 stable HLO 생성 후 `compile()`로 실행 파일 생성, 이후 `execute()`는 컴파일 없이 호출 가능
- **`jax.export`** — Stable HLO 기반 이식성 있는 아티팩트 직렬화, JAX 런타임 플랫폼 대상의 **이식성 높은 방법**
- **`jax2TF`** — TensorFlow 인프라를 사용하는 경우 SaveModel 형식으로 변환, `native_serialization` 옵션 활용
- **Stable HLO** — 새로운 모델이 아니라 컴파일러가 보는 최저 수준의 프로그램, 디버깅·검증용으로 활용

---

## 💡 개발자 포인트

배포 대상에 따른 패턴 선택 가이드:

| 배포 대상 | 권장 패턴 |
|---|---|
| Python 서비스 | `jax.jit` + 웜업 |
| JAX 런타임 (AOT 지원) | Ahead-of-Time 컴파일 |
| 이식성 필요 (JAX runtime) | `jax.export` |
| TensorFlow 인프라 | `jax2TF` + SaveModel |

> **주의:** 배치 크기(shape)가 달라지면 별도 컴파일이 발생합니다. shape을 고정하거나, 큰 배치를 사용해 오버헤드를 분산시키는 전략이 필요합니다.

**성능 최적화 팁:**
- GPU shape이 안정화되었는지 반드시 확인
- 추측 전에 **타임라인 blocking 프로파일**로 병목 파악
- 불필요한 **호스트(CPU) 전송** 발생 방지

---

## 📅 버전 / 출시 일정
해당 없음

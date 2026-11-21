# How to run and scale JAX on NVIDIA GPUs (Step-by-Step)

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=1bpRQlLVDjU
- **요약 일시**: 2026-11-21 09:03:52

---

> ⚠️ 이 영상은 자막을 가져올 수 없어 **영상 설명만** 보고 요약했습니다. 세부 내용은 원본 영상에서 확인하세요.

## 🔑 핵심 요약
- **JAX는 TPU 전용이 아님**: NVIDIA GPU에서 JAX AI 스택 전체를 실행하고 확장하는 방법을 다루는 Google Cloud Live 에피소드
- 설치 없이 바로 쓰는 **컨테이너**부터 **멀티 GPU 데이터 병렬 학습**, **커널 수준 프로파일링**까지 단계별로 설명
- 발표자: Ivan Nardini (Google Cloud AI Engineer), Katya Sirazitdinova (NVIDIA Developer Advocate)

---

## 📣 주요 발표 내용
- JAX의 기반 개념 소개: **JIT 컴파일**(`jax.jit`), **Autograd**(`jax.grad`), **XLA** 컴파일러
- NVIDIA가 매달 업데이트하는 JAX 컨테이너로 별도 환경 설정 없이 GPU에서 JAX 실행
- 단일 GPU에서 멀티 GPU **데이터 병렬(data-parallel) 학습**으로 확장하는 방법
- 커널 수준까지 내려가는 **프로파일링**으로 성능 병목 찾기

---

## 💡 개발자 포인트
- NVIDIA 하드웨어에서 JAX 코드가 생각보다 느리다면 이 영상이 다루는 프로파일링 흐름이 참고가 됨
- 직접 CUDA/cuDNN 환경을 맞추는 대신 NVIDIA가 관리하는 JAX 컨테이너를 쓰면 설정 부담을 줄일 수 있음
- TPU용으로 짠 JAX 코드를 GPU 클러스터로 옮길 때 데이터 병렬 확장 패턴을 확인할 것

> 영상 설명이 중간에 잘려 있어, 구체적인 API·플래그·컨테이너 태그는 원본에서 확인 필요

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| NVIDIA JAX 컨테이너 | 매월 업데이트 (영상 설명 기준) |


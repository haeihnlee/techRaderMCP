# Getting started with JAX on NVIDIA GPUs

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=CxTUFiWCVjk
- **요약 일시**: 2026-08-27 09:10:58

---

## 🔑 핵심 요약
- **JAX**는 NumPy 스타일로 작성하지만, GPU 위에서 XLA 컴파일을 통해 실행되는 고성능 ML 프레임워크
- `jit`, `grad`, `vmap` 3가지 핵심 트랜스폼으로 컴파일·미분·배치를 처리
- GPU 활용 여부 확인 → 셰이프 고정 → 비동기 타이밍 주의가 JAX 성능 최적화의 핵심 체크리스트

---

## 📣 주요 발표 내용
- **JAX 실행 스택**: Python 코드 → JAX AI 트레이싱 → **XLA 컴파일** → NVIDIA GPU 런타임
- `nvidia-smi` 및 `jax.devices()`, `jax.default_backend()`로 GPU 인식 여부 확인 필수
- JAX 배열은 GPU(device)에 상주하며, NumPy 배열(host)과 위치가 다름
- `jit`, `grad`, `vmap` — 각각 **컴파일**, **자동미분**, **배치처리** 담당
- JIT 컴파일은 **셰이프+dtype 시그니처**가 동일할 때 재사용; 셰이프 변경 시 재컴파일 발생
- 제어 흐름에는 `jnp.where`, `lax.cond`, `lax.scan` 사용 (Python 분기문 사용 불가)

---

## 💡 개발자 포인트
> JIT 내부에서 배열 값은 **traced value**이므로 Python의 `if/else`로 분기할 수 없음. `lax.cond` 또는 `jnp.where`를 사용할 것.

> JAX는 GPU 작업을 **비동기**로 실행함. 타이머가 block하지 않으면 실제 GPU 연산 시간이 아닌 Python dispatch 시간을 측정하게 됨 — 정확한 프로파일링 필수.

- 핫 루프 내 `float()` 또는 `int()` 변환은 데이터를 host로 끌어내려 **device sync를 유발** → 프로덕션 코드에서 제거 필요
- 가변 시퀀스 길이로 인한 셰이프 변화를 막으려면 **패딩 + 마스크** 전략 적용
- 성능 이상 시 체크 항목: 컴파일 빈도, host↔device 전송, GPU 유휴 갭, 소규모 커널 난립, 배치 사이즈 효과, 메모리 압박

---

## 📅 버전 / 출시 일정
해당 없음

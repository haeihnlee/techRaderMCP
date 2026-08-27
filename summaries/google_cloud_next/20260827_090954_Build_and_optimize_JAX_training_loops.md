# Build and optimize JAX training loops

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=jHon1u6xt-4
- **요약 일시**: 2026-08-27 09:09:54

---

## 🔑 핵심 요약
- **JAX 학습 루프**는 순수 함수(pure function)로 설계해야 컴파일 재사용이 가능
- **Attention 구현 시** 나이브 방식은 시퀀스 길이²로 메모리가 증가하므로 `cuDNN` 퓨전 연산 사용 권장
- 학습 루프에서 **디바이스 상태를 유지**하고 로깅·블로킹을 최소화해야 성능 저하 방지

---

## 📣 주요 발표 내용
- JAX 학습 스텝은 파라미터·옵티마이저 상태·배치를 입력받아 새 파라미터·상태·메트릭을 반환하는 **순수 함수** 구조
- 데이터 전처리 시 **고정 배치 크기(fixed batch size)** 를 유지해야 `jit` 컴파일 스텝 재사용 가능
- `jax.value_and_grad`로 손실값과 그래디언트 트리를 동시에 반환
- **Optax AdamW** 옵티마이저를 통해 그래디언트 계산 → 옵티마이저 상태 업데이트 → 파라미터 업데이트
- `jax.jit`으로 전체 학습 스텝을 GPU에 스테이징
- Attention 구현: Score Q·K → Scale → Softmax → Mix V 순서
- NVIDIA GPU에서 `implementation="cudnn"` 옵션으로 **cuDNN 퓨전 Attention** (BF16/FP16) 활성화
- Decoder 모델에 필요한 **Causal Attention**: MHA, GQA, MQA는 출력 형상 동일하나 KV 캐시 비용 상이

---

## 💡 개발자 포인트
- 학습 루프에서 매 스텝마다 텐서를 Python 값으로 변환하면 성능 급감

> ⚠️ `loss.item()` 같은 Python 변환을 매 스텝 호출하면 GPU 디바이스 동기화가 발생해 루프 전체가 느려집니다. 로깅은 **간헐적**으로, 블로킹은 **의도적**으로만 수행하세요.

- 나이브 Attention은 **시퀀스 길이²** 크기의 행렬을 메모리에 모두 올림 → 긴 시퀀스에서 latency 급증
- XLA가 연산을 자동 퓨전하도록 두거나, NVIDIA GPU에서는 `implementation="cudnn"` 명시
- 평가 시 **고정 테스트 배치**에서 예측값과 Confusion Matrix를 직접 확인해 모델 동작을 파악

---

## 📅 버전 / 출시 일정
해당 없음

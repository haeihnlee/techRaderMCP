# Scale JAX models to multi-GPU systems

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=Ujwm_CCCn3s
- **요약 일시**: 2026-08-27 09:07:33

---

## 🔑 핵심 요약
- **JAX**에서 멀티 GPU 학습은 코드를 재작성하는 것이 아니라 **배열의 배치(placement)**만 변경하는 방식으로 동작
- 데이터 병렬화(`data parallelism`)는 배치를 GPU별로 분할하고 그래디언트를 평균 내어 모델 복사본을 동기화
- `Mesh`, `PartitionSpec`, `NamedSharding`, `device_put` 네 가지 개념으로 멀티 GPU 분산 학습 구성

---

## 📣 주요 발표 내용
- **데이터 병렬화 기본 흐름**: 배치를 GPU 수만큼 분할 → 각 GPU에서 그래디언트 계산 → `psum`/`pmean`으로 평균화 → 모델 동기화
- **4가지 핵심 개념**:
  - `Mesh`: 물리 디바이스 구성 정의
  - `PartitionSpec`: 배열을 어느 축으로 분할할지 기술
  - `NamedSharding`: Mesh + PartitionSpec 조합으로 분산 계획 생성
  - `device_put`: 실제로 배열을 디바이스에 배치
- **자동 샤딩 vs 수동 제어**: 실험 단계에선 자동 샤딩 사용, 디버깅·세밀한 제어에는 `shard_map` 사용
- **Tiny Transformer 구현**: `NNX` 기반 멀티헤드 어텐션, Pre-norm 블록 구조, Tiny Shakespeare 데이터셋으로 byte-level 언어모델 학습
- **모델 저장 및 추론**: `orbax`로 가중치 저장/복원, 고정 최대 길이(`max_length`) 패딩으로 재컴파일 방지

---

## 💡 개발자 포인트
- `JAX debug visualizer`의 `array_sharding`으로 배치 분할 및 가중치 복제 상태를 시각적으로 검증할 것
- 배치가 너무 작으면 통신 오버헤드 때문에 오히려 성능이 떨어질 수 있음

> **주의**: 멀티 GPU 확장이 항상 처리량을 높이지는 않습니다. 디바이스당 충분한 작업량이 있어야 통신 오버헤드를 상쇄할 수 있습니다.

- 추론 시 `pad to fixed max length` 패턴을 적용하지 않으면 토큰마다 `jit` 재컴파일이 발생하여 심각한 성능 저하 유발
- `shard_map` 내에서 `jax.lax.pmean`을 명시적으로 호출하면 그래디언트 평균화 과정을 직접 제어 가능

---

## 📅 버전 / 출시 일정
해당 없음

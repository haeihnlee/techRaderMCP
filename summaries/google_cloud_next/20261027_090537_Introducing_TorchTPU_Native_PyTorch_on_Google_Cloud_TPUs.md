# Introducing TorchTPU: Native PyTorch on Google Cloud TPUs

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=u4n558Ul6w0
- **요약 일시**: 2026-10-27 09:05:37

---

## 🔑 핵심 요약
- Google과 Meta PyTorch 팀이 함께 만든 **TorchTPU**가 오픈 소스로 공개됨. 이제 Cloud TPU가 PyTorch의 **네이티브 장치**로 동작함
- 기존 PyTorch 코드에서 장치만 `tpu`로 바꾸면 실행되고, Eager 모드 · `torch.compile` · `torch.distributed`를 평소처럼 쓸 수 있음
- 내부적으로는 PyTorch 디스패처에 연결된 **C++ 백엔드**임. 연산을 **StableHLO**로 낮춘 뒤 **XLA 컴파일러**로 컴파일함

---

## 📣 주요 발표 내용
- **TorchTPU 오픈 소스 공개**: GitHub(Google PyTorch 조직)에 공개되어 누구나 사용 가능
- **장치 전환만으로 실행**: `torch.device`를 TPU로 지정하거나, PyTorch에 현재 가속기를 묻고 프로세스 그룹이 백엔드를 고르게 하면 같은 파일이 여러 장치에서 실행됨
- **두 가지 실행 방식**
  - **Eager 모드**: 연산을 하나씩 TPU로 보냄 (디버깅용)
  - **`torch.compile` + TPU 백엔드**: 첫 스텝에서 전체 그래프를 하나의 TPU 프로그램으로 컴파일하고, 이후 스텝은 그 프로그램을 재사용함
- **분산 학습**: 표준 PyTorch 프로세스 그룹 API 수준에서 TPU collective를 구현함. 그래서 `DTensor`, `FSDP2`, `DDP`가 다른 가속기와 똑같이 동작하고, 단일 칩에서 멀티 호스트 슬라이스까지 같은 코드로 확장됨
- **생태계 호환**
  - 모델: **Hugging Face Hub** 인기 모델
  - 대규모 학습: **TorchTitan** (TPU용 레시피와 모델 최적화 플레이북 제공)
  - 서빙: **vLLM**, **SGLang**
  - 오케스트레이션: **Ray** (호스트 간 학습/서빙), **llm-d** (Kubernetes 플릿 서빙)
- **커스텀 커널**: **Pallas**로 TPU 커널을 작성해 일반 PyTorch 함수처럼 호출할 수 있음. 실험적 옵션(자막상 "Helium", **Helion**으로 추정)은 곧 제공 예정
- **프로파일링 / 디버깅**: `torch.profiler` 트레이스를 **XProf**에서 열 수 있음. 런타임·컴파일러 오류 메시지는 바로 조치할 수 있는 형태로 출력됨
- 데모: **Trillium** TPU 칩 1개에서 Eager와 `torch.compile`의 스텝 시간을 비교함

> 자막은 자동 번역본이라 일부 고유명사(Pallas, Helion, llm-d, DTensor)는 문맥으로 추정해 표기했습니다. 정확한 이름은 공식 문서에서 확인하세요.

---

## 💡 개발자 포인트
- 기존 PyTorch 코드베이스를 거의 그대로 TPU로 옮길 수 있음. 장치 지정 부분만 바꾸면 됨
- 장치를 하드코딩하지 말고 현재 가속기를 조회하는 방식으로 짜 두면, 같은 스크립트를 GPU와 TPU에서 함께 쓸 수 있음
- 권장 흐름: **Eager 모드로 디버깅** → **`torch.compile`로 가속** → **`torch.distributed`(FSDP2/DDP)로 확장**
- `torch.compile` 사용 시 **첫 스텝에 전체 그래프 컴파일 시간**이 걸림. 벤치마크할 때는 워밍업 스텝을 빼고 측정해야 함

> TPU에서 최고 성능을 내려면 기본 설정 외에 **추가 튜닝**이 필요할 수 있음. TorchTitan for TPU의 최적화 플레이북을 참고할 것

- 성능 병목은 `torch.profiler`로 수집해 XProf에서 분석하면 됨
- 서빙 스택(vLLM, SGLang)과 K8s 기반 서빙(llm-d)이 지원되므로, 학습부터 추론까지 TPU에서 한 번에 구성할 수 있음

---

## 📅 버전 / 출시 일정
| 항목 | 상태 |
|------|------|
| TorchTPU | 오픈 소스 공개 (발표 당일부터 GitHub에서 이용 가능) |
| Pallas 커스텀 커널 | 지원 |
| Helion(추정) 실험적 옵션 | 곧 제공 예정 |
| 데모 하드웨어 | Trillium TPU (단일 칩) |


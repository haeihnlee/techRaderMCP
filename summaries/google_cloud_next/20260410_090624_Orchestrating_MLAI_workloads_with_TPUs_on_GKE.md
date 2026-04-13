# Orchestrating ML/AI workloads with TPUs on GKE

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=coP5_SmE4AI
- **요약 일시**: 2026-04-10 09:06:24

---

## 🔑 핵심 요약
- **TPU**는 행렬 연산에 특화된 Google의 커스텀 ASIC 칩으로, `MXU(Matrix Multiply Unit)` 기반의 대규모 AI 학습/추론 워크로드에 최적화되어 있음
- **GKE(Google Kubernetes Engine)** 위에서 TPU를 운용하면 단일 칩부터 수만 개 칩까지 **단일 원자 단위(Atomic Unit)** 로 프로비저닝·스케줄링 가능
- **Ironwood(7세대 TPU)** 는 단일 Pod에 최대 **9,216 chips** 를 연결할 수 있으며, 이전 세대 대비 T-Flops 및 HBM 대역폭이 비약적으로 향상됨

---

## 📣 주요 발표 내용

### 🧠 TPU 아키텍처 핵심 개념
- ⚡ `MXU(Matrix Multiply Unit)`: 이미지 하나 인식에 수십억 번의 행렬 곱셈을 단일 스텝에 처리
- 💾 **HBM(High Bandwidth Memory)**: 대용량 모델·배치를 칩 위에서 직접 처리해 데이터 전송 병목 최소화
- 🔗 **ICI(Inter-Chip Interconnect)** + **광학 회로 스위칭 네트워크**: 수백~수천 개 칩 간 고속 연결

### 📐 TPU 슬라이스 구조 (GKE 노드 관점)

| 구성 | 설명 | 칩 수 규모 | 주요 용도 |
|------|------|-----------|----------|
| **Single-Host TPU** | VM 1개, 칩 1~8개, 칩 간 zero 네트워크 레이턴시 | 1~8 chips | 파인튜닝, 개발, 고성능 추론 |
| **Multi-Host TPU** | 단일 노드풀 내 여러 VM, **ICI 링크**로 상호 연결 | 최대 ~9,216 chips | 대규모 학습/추론 |
| **Multi-Slice TPU** | 여러 노드풀을 **데이터센터 네트워크**로 연결 | 50K~100K+ chips | 초대규모 프론티어 모델 학습 |

### 🚀 GKE TPU 핵심 기능
- 🎯 **Atomic Provisioning**: TPU 슬라이스를 단일 원자 단위로 프로비저닝·스케줄링·장애조치
- 💰 **Custom Compute Class**: On-Demand → Reservation → `DWS Flex` → Spot 간 자동 폴백으로 비용 효율화
- 📦 **동적 워크로드 스케줄러(DWS)**: 유연한 용량 확보 및 비용 최적화
- 🔧 오픈소스 AI 서빙 오케스트레이터 **vLLM**, **QBRE** 등 통합 지원
- 📊 통합 대시보드 및 옵저버빌리티 도구 내장

### 🔢 지원 프레임워크
- ✅ **JAX**
- ✅ **TensorFlow**
- ✅ **PyTorch**

---

## 💡 개발자 포인트

### 🏗️ 슬라이스 선택 기준
- **단순 추론 / 파인튜닝** → `Single-Host` 노드풀로 시작, HPA(Horizontal Pod Autoscaler)로 수평 확장
- **중대형 학습** → `Multi-Host` 단일 노드풀, ICI 링크 활용
- **프론티어 모델 학습** → `Multi-Slice` + 데이터센터 네트워크 연결

> ⚠️ **Multi-Host** 구성에서 노드풀 내 모든 VM은 ICI로 연결되지만, **Multi-Slice** 간 통신은 데이터센터 네트워크를 경유하므로 레이턴시 특성이 달라짐. 워크로드 설계 시 통신 패턴을 반드시 고려할 것.

> ⚠️ TPU 슬라이스는 **하나의 원자 단위**로 스케줄링됨. 슬라이스 일부만 사용하는 부분 점유 방식은 지원되지 않으므로, 슬라이스 크기 선정이 비용에 직결됨.

### 💸 비용 최적화 전략
- `Custom Compute Class` 를 활용해 용량 부족 시 자동으로 저렴한 용량 타입으로 폴백 설정 권장
- 단발성·중단 허용 워크로드 → **Spot** 활용
- 장기 안정 워크로드 → **Reservation** 또는 **Calendar** 모드 고려

### 🔗 연동 생태계
- `GKE` + `Vertex AI` + `Cloud TPU API` 세 가지 진입점 모두 지원
- 스토리지·로드밸런서·모니터링 등 GKE 풀 에코시스템 그대로 활용 가능
- **GKE 최대 지원 노드 수**: **130,000 nodes** (대규모 TPU 칩을 단일 클러스터로 운용 가능)

---

## 📅 버전 / 출시 일정

| TPU 세대 | 코드명 | 주요 특징 | 상태 |
|---------|--------|----------|------|
| 7세대 | **Ironwood** | 단일 Pod 9,216 chips, 대폭 향상된 T-Flops (BF16/FP8) | 신규 발표 |
| 6세대 | **Trillium** | 전세대 대비 성능 향상 | 출시됨 (작년) |
| 5세대 | **V5P** | 고성능 학습 특화 | 출시됨 |
| 4세대 | **V4** | 대규모 학습 지원 | 출시됨 |

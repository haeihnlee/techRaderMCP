# Google Cloud Live: Accelerate data science and analytics with GPUs

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=yBxRoYj-i28
- **요약 일시**: 2026-04-08 16:06:38

---

## 핵심 요약 (3줄)
- GPU를 활용한 NVIDIA의 오픈소스 Python 라이브러리(cuDF, cuML)를 통해 기존 pandas/scikit-learn 코드를 **코드 변경 없이** 대폭 가속화할 수 있다.
- 실제 데모에서 3억 4천만 건의 기상 데이터를 GPU로 쿼리 시 **약 90ms** 소요된 반면, CPU(pandas)는 동일 작업에 **약 9~10초** 소요되어 약 100배 성능 차이를 보였다.
- Google Cloud의 **Cloud Run에 GPU를 붙이는 방식**으로 서버리스 환경에서도 GPU 가속 데이터 분석이 가능하다.

---

## 주요 발표 내용

- **GPU 가속 데이터 분석 데모**
  - 3억 4천만 건의 NOAA 글로벌 기후 데이터(Global Climatology Network)를 GPU 메모리에 올려 실시간 쿼리
  - NVIDIA L4 GPU + cuDF를 사용한 Cloud Run 인스턴스에서 동작

- **CPU vs GPU 성능 비교**
  - CPU(pandas): 1억 1,300만 건 처리, 약 9~10초 소요
  - GPU(cuDF): 3억 4,000만 건 처리, 약 80~95ms 소요
  - **데이터 3배 많음에도 약 100배 빠른 성능**, 더 많은 데이터 처리로 분석 정확도도 향상

- **NVIDIA CUDA 스택 소개**
  - 물리적 GPU → CUDA(C/C++ API) → CUDA-X(Python 고수준 라이브러리) 3계층 구조
  - **cuDF**: pandas, Polars, SQL, Apache Spark 가속
  - **cuML**: scikit-learn 가속
  - **cuGraph**: NetworkX 가속 (그래프 분석)

- **Cloud Run GPU 지원**
  - Google Cloud의 Cloud Run 서비스에 GPU를 연결하여 서버리스 방식으로 GPU 워크로드 실행 가능

---

## 개발자에게 중요한 포인트

- **코드 변경 불필요**: cuDF, cuML은 pandas, scikit-learn과 동일한 API를 제공하므로 기존 코드를 거의 수정하지 않고 GPU 가속 적용 가능
  ```python
  # 기존 pandas 코드
  import pandas as pd
  
  # GPU 가속으로 전환 (API 동일)
  import cudf as pd  # drop-in replacement
  ```

- **대용량 데이터 처리 패러다임 전환**: 메모리 부족으로 인한 데이터 샘플링 없이 전체 데이터셋을 GPU 메모리에 올려 처리 가능 → **분석 정확도 향상**

- **서버리스 GPU 활용**: Cloud Run에 GPU를 attach하여 별도 인프라 관리 없이 GPU 가속 API/서비스 배포 가능

- **오픈소스 라이브러리**: cuDF, cuML, cuGraph 모두 오픈소스로 로컬 개발 환경에서도 테스트 가능

- **적용 대상 워크로드**:
  - 대규모 DataFrame 연산 (pandas 대체)
  - 머신러닝 모델 학습/추론 (scikit-learn 대체)
  - 그래프 분석 (NetworkX 대체)
  - SQL 쿼리, Apache Spark 워크로드

---

## 출시 일정 / 버전 정보

- **해당 없음** (특정 버전 출시일 언급 없음)
  - 단, cuDF, cuML, cuGraph는 현재 사용 가능한 오픈소스 라이브러리
  - Cloud Run GPU 지원은 데모 시점 기준 이미 사용 가능한 상태로 시연됨

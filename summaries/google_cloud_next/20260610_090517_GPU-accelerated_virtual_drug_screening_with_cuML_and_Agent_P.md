# GPU-accelerated virtual drug screening with cuML and Agent Platform

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=k7HrSreatII
- **요약 일시**: 2026-06-10 09:05:17

---

## 🔑 핵심 요약
- **GPU 가속 라이브러리** `cuML`·`cuDF`로 전통적인 **tabular 데이터 사이언스**(scikit-learn/pandas) 워크플로우를 그대로 가속하는 사례
- 코드 **상단 1~2줄만 추가**하면 기존 scikit-learn/pandas 코드를 수정 없이 GPU에서 실행 (`290만 행` 분자 스캔)
- 약물-단백질 결합 예측 앱 데모: 약물 이름 입력 → `EGFR` 수용체 결합 여부를 **subsecond(97ms)** 추론
- 신약 탐색 예시지만 동일 원리가 **금융 사기탐지·제조 설비예측·리테일 이탈예측**에 그대로 적용 가능

---

## 📣 주요 발표 내용
- **무엇을 푸는가**: 전통적 신약 탐색은 단백질(lock)에 맞는 분자(key)를 찾는 **검색 문제**. 실험실 in-vitro 스크리닝은 분자당 수일·연 1,000개 한계 → 이를 **in silico(가상)** 로 대체
- **데이터셋**: `ChEMBL` 공개 DB 사용. 각 분자는 `canonical SMILES`(분자 구조의 텍스트 표현) 문자열로, 라벨은 `IC50`(억제 농도, **값이 낮을수록 강한 결합**)
- **실행 환경**: `Google Colab Enterprise` + GPU 위에서 노트북 실행, 전부 **오픈소스**(데이터·`cuML`·`cuDF`)
- **백엔드 루프 전체 시연**: 모델 학습 → 배포 → GPU 엔드포인트 → 앱 추론까지 end-to-end
- **앱 동작**: 약물명을 `PubChem`으로 해석 → 2D 구조·디지털 fingerprint 변환 → GPU 엔드포인트 호출 → 결합 여부 반환 (예: `caffeine`·`aspirin`·`ibuprofen`·water = 비결합, EGFR 폐암 표적 약물 = 결합)

---

## 💡 개발자 포인트
- **핵심 가치**: CPU 기반 `pandas`·`scikit-learn`은 대용량 데이터에서 한계 → GPU 도입으로 **학습 시간 1자릿수 배수(order of magnitude) 단축**
- 기존 코드를 **재작성할 필요 없음** — import 전에 두 줄만 추가하면 동일한 워크플로우가 GPU에서 돌아감

> ⚠️ "주어진 데이터에서 학습 시간 단축보다 더 중요한 건 **개발자의 시간을 돌려주는 것**" — 같은 pandas/scikit-learn 패턴으로 빠르게 반복 실험 가능

- **운영(MLOps) 관점**: subsecond 추론 + **continuous drift monitoring**(지속적 드리프트 감시)이 함께 제공되어 프로덕션 적용에 유리
- **도메인 무관 적용성**: 모델 학습·MLOps·배포 원리가 금융(fraud detection)·제조(설비 고장 예측)·리테일(고객 churn 예측) 등 전 산업에 동일 적용

---

## 📅 버전 / 출시 일정
해당 없음 (제품 버전·출시일 언급 없음. 사용 기술: `cuML`, `cuDF`, `Google Colab Enterprise`, `ChEMBL`, NVIDIA BioNeMo — 모두 데모 시점 가용)


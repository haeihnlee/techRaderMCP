# GPU-accelerated virtual drug screening with cuML and Agent Platform

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=k7HrSreatII
- **요약 일시**: 2026-06-09 09:10:12

---

## 🔑 핵심 요약
- **GPU는 LLM 전용이 아니다** — 정형(tabular) 데이터 사이언스, 특히 **신약 가상 스크리닝(virtual drug screening)** 가속에 활용
- **Google Cloud + NVIDIA** 공동 라이브 세션으로, 분자 예측 파이프라인을 **프로토타입에서 프로덕션까지** end-to-end로 시연
- 핵심 스택은 NVIDIA **`cuML`**(RAPIDS GPU 가속 ML 라이브러리) + Google Cloud **Agent Platform**

> ⚠️ 이 영상은 **자막이 제공되지 않아**, 아래 요약은 공개된 영상 설명(description) 기반으로 작성되었습니다. 상세 데모 내용은 실제 영상 시청 필요.

---

## 📣 주요 발표 내용
- **GPU 가속 가상 신약 스크리닝**을 라이브 데모로 처음부터 끝까지 분해 설명
- NVIDIA **`cuML`** 을 사용해 정형 데이터 기반 분자 예측 모델을 GPU로 가속
- Google Cloud **Agent Platform** 과 결합해 모델을 **프로덕션 서비스**로 배포하는 흐름 시연
- **인터랙티브 라이브 데모**: 채팅창에 일상적인 화합물(compound)을 입력하면 실시간으로 예측 결과 확인
- 발표 진행: **Tilde**(호스트), **Jeff Nelson**, **William Hill**, **Dr. Saee Paliwal** (Google Cloud & NVIDIA 전문가)

---

## 💡 개발자 포인트
- LLM에만 쏠려 있던 GPU 활용을 **전통적 ML / 정형 데이터 워크로드**로 확장하는 사례 — `cuML`은 scikit-learn 호환 API로 기존 ML 코드를 큰 수정 없이 GPU 가속 가능
- 모델 학습(`cuML`)부터 에이전트 기반 서빙(**Agent Platform**)까지 **MLOps 파이프라인 전 구간**을 다루므로, 연구용 노트북을 프로덕션으로 옮기려는 팀에 참고 가치

> 💊 적용 도메인이 신약 발굴(drug discovery)이지만, **GPU 가속 정형 데이터 ML + 에이전트 서빙** 패턴 자체는 금융·추천·이상탐지 등 다른 도메인에도 이식 가능

---

## 📅 버전 / 출시 일정
해당 없음 (제품 버전·출시일 정보는 영상 설명에 포함되지 않음)

# From hackathon project to helping transplant surgeons

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=6WjdZZL-FEI
- **요약 일시**: 2026-11-05 09:03:55

---

## 🔑 핵심 요약
- 해커톤 프로토타입 **Doctor Cloud**가 장기 이식 전문의 2명과의 협업으로 이어져, **신장 이식 수용 여부 결정**을 돕는 앱으로 발전 중
- **Cloud Run 서버리스 GPU**로 VM·Kubernetes 클러스터 없이 AI 모델/앱을 배포하고 자동 확장
- 사전 제작된 Docker 이미지(Deep Learning VM, Gemma, Llama)를 기반으로 앱 코드만 바꿔 빠르게 배포 가능

---

## 📣 주요 발표 내용
- **서버리스 GPU**: 확장성·유연성·비용 최적화와 함께, 단일 엔드포인트로 다수 고객에게 모델/앱 서빙
- Python, React, JavaScript 등 언어와 무관하게 **Docker 컨테이너로 패키징**하면 `Cloud Run`에 배포 가능
- `Cloud Run`이 트래픽 증가에 맞춰 인스턴스와 **GPU 확장을 자동 처리**
- 사례: 독감을 앓던 중 사람들이 WebMD에서 근거 없는 정보를 '둠스크롤링'하는 문제를 보고 **Doctor Cloud** 개발 → 해커톤을 계기로 이식 전문의와 협업

---

## 💡 개발자 포인트
- 기존 방식(전용 GPU VM, GKE 클러스터)은 인프라 구축과 **NVIDIA CUDA 드라이버** 관리를 직접 해야 하지만, `Cloud Run`에서는 이 과정이 추상화됨
- ML 모델이나 LLM을 GPU와 함께 `Cloud Run`에 올릴 땐 **사전 제작 Docker 이미지** 사용을 권장
  - Deep Learning VM 이미지
  - **Gemma** / **Llama** 컨테이너
- 베이스 이미지 위에 **애플리케이션 코드 경로**와 `requirements.txt` 같은 요구사항 파일만 교체하면 배포 완료
- 해커톤 수준의 프로토타입도 서버리스 GPU로 실사용 단계까지 빠르게 키울 수 있음

> 의료 의사결정(이식 수용 여부)처럼 민감한 도메인은 전문의 검증과 협업이 필수라는 점을 사례가 보여줌

---

## 📅 버전 / 출시 일정
해당 없음


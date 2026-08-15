# What is Spanner Omni?

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=qSofdwoow2c
- **요약 일시**: 2026-08-15 09:03:47

---

## 🔑 핵심 요약
- **Spanner Omni**는 Google Cloud Spanner를 사용자 자체 인프라(VM, 컨테이너, Kubernetes)에서 실행할 수 있는 다운로드 가능한 버전
- 클라우드와 동일한 멀티모델 기능(그래프, 벡터 검색, 운영 분석 등)을 온프레미스·하이브리드 환경에서 활용 가능
- Docker로 로컬 개발 환경을 빠르게 구축하고, 클라우드 배포 전 로컬 테스트 가능

---

## 📣 주요 발표 내용
- **Spanner Omni** 공개: 기존 Google Cloud Spanner의 모든 기능을 자체 인프라에서 실행
- 지원 환경: 가상 머신(VM), 컨테이너, **Kubernetes** 클러스터
- 자동 샤딩 및 읽기/쓰기 수평 확장성 제공
- 컴퓨트와 스토리지를 독립적으로 확장 가능
- 지원 쿼리 언어: **Google SQL**, **PostgreSQL**, 그래프 쿼리 언어(GQL)
- 멀티모델 기능: **그래프(Graph)**, **벡터 검색(Vector Search)**, **운영 분석(Operational Analytics)** 지원
- Kubernetes 배포용 **Helm chart** 예제 제공

---

## 💡 개발자 포인트
- **로컬 Docker 배포** 빠른 시작 흐름:
  1. 최소 요구사항 확인 및 Docker 설치
  2. 이미지·CLI 다운로드
  3. `Docker volume` 생성 (컨테이너 삭제 후에도 데이터 유지)
  4. 컨테이너 시작 → 데이터베이스 생성 → 즉시 사용 가능
- 샘플 테이블·데이터를 로드해 빠른 실험 가능

> **데이터 주권(Data Sovereignty) 규정** 또는 **엄격한 크로스클라우드/하이브리드 전략**이 필요한 비즈니스에 특히 적합

- VM·Kubernetes 고급 배포는 영상 설명란의 Helm chart 예제 참고

---

## 📅 버전 / 출시 일정
해당 없음

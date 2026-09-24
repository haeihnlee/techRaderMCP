# Modernize Enterprise Apps on GKE: Getting Started with Online Boutique

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=0nYah54M3HY
- **요약 일시**: 2026-09-24 09:04:42

---

## 🔑 핵심 요약
- **GKE(Google Kubernetes Engine)**를 처음 시작하는 개발자를 위한 엔드 투 엔드 샘플 앱 **Online Boutique** 소개
- 5가지 언어(`Python`, `Java`, `C#`, `Golang`, `Node.js`)로 구성된 **11개 마이크로서비스** 아키텍처 실습 가능
- **GKE Autopilot** + `kubectl apply`만으로 몇 분 내 완전한 소매점 샘플 앱 배포 가능

---

## 📣 주요 발표 내용
- **Online Boutique**: GKE 학습용 오픈소스 샘플 애플리케이션 (GitHub 공개)
  - `GKE`, `Cloud Service Mesh`, `Cloud Monitoring` 등 Google Cloud 제품 통합 데모
  - 프런트엔드 + **부하 생성기(Load Generator)** 포함 — 실제 트래픽 시뮬레이션 가능
  - 백엔드 데이터 스토어: **Redis**
- 선택적 구성 요소(optional components)로 다양한 사용 사례 테스트 가능
- **빠른 배포 절차**:
  1. GKE Autopilot 클러스터 생성
  2. Google Cloud Shell에서 저장소 `git clone`
  3. `kubectl apply`로 Kubernetes 매니페스트 적용

---

## 💡 개발자 포인트
- Online Boutique는 단일 앱이 아닌 **폴리글랏 마이크로서비스** 예제 — 실제 프로덕션 패턴 학습에 적합
- **GKE Autopilot** 사용으로 노드 관리 불필요 — 인프라보다 앱 배포 흐름 학습에 집중 가능

> ⚠️ Online Boutique는 학습/데모용 앱으로, 프로덕션 보안 설정 없이 배포됨. 실제 서비스에 그대로 사용 금지.

- GitHub 저장소에 **퀵스타트 가이드 및 상세 문서** 포함 — 추가 구성 실험 시 참고 필수

---

## 📅 버전 / 출시 일정
해당 없음


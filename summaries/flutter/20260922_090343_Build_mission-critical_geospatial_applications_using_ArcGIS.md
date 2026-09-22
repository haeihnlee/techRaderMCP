# Build mission-critical geospatial applications using ArcGIS Maps SDK for Flutter | Martino Yovo

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=rvtSUH3WGaA
- **요약 일시**: 2026-09-22 09:03:43

---

## 🔑 핵심 요약
- **ArcGIS Maps SDK for Flutter**는 Esri가 개발한 Flutter용 지리공간(GIS) SDK로, 고급 지도 기능을 Flutter 앱에 통합 가능
- 소비자용 지도(Google/Apple Maps)를 넘어선 **오프라인 지원**, 비공개 경로, 위기대응 등 미션 크리티컬 워크플로우 제공
- `pub.dev`에서 `arcgis_maps`로 설치 가능, 공식 문서 및 toolkit repo 오픈

---

## 📣 주요 발표 내용
- **ArcGIS Maps SDK for Flutter** 소개: Esri의 핵심 GIS 엔진 위에 Flutter API를 래핑한 SDK
- 주요 기능:
  - 데이터 **시각화** (커스텀 레이어, 지도 레이어 중첩)
  - **라우팅** 및 **지오코딩**
  - **공간 분석** (Spatial Analysis)
  - **오프라인 맵** (지도 사전 다운로드 후 연결 없이 사용)
- 설치: `pub.dev`에서 `arcgis_maps` 패키지로 설치
- 문서: `developers.google.com/wallet/flutter` (Flutter용 ArcGIS 공식 문서)
- **toolkit repo**: 지도 관련 UI 컴포넌트, 인증 워크플로우 등 오픈소스 제공

---

## 💡 개발자 포인트
- GIS는 단순 지도가 아닌 **지도 뒤의 인텔리전스 시스템** — 위치 기반 쿼리, 공간 분석, 의사결정 지원
- 주요 활용 사례:
  - 유틸리티 기업의 **전력선 관리**
  - 재난 대응 시 **자원 배분 최적화**
  - **농업** 분야 필드 구획 설정 및 작물 계획
  - 교통사 **도로 공사 모니터링**
- 개인 위치 데이터를 SDK에 넣어 **커스텀 맵** 구축 가능 (공개 지도 서비스 불필요)
- 드론 이미지 등 **다중 해상도 레이어** 중첩 지원

> **오프라인 모드**: 네트워크가 없는 환경(항공 구급대, 재난 현장 등)에서도 작동하는 오프라인 지도를 Flutter 앱에서 구현 가능

---

## 📅 버전 / 출시 일정
해당 없음

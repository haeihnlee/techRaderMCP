# Architecting production-ready AI apps with Google Cloud & Firebase

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=_KQmsFIZVYw
- **요약 일시**: 2026-08-14 09:08:35

---

## 🔑 핵심 요약
- **Flutter + Firebase + Cloud Run** 조합으로 AI 앱의 프로덕션 아키텍처를 구성하는 방법 소개
- **Model Garden**을 통해 Gemini, Claude 등 여러 모델을 단일 API로 사용해 벤더 종속 없이 모델 선택 가능
- 보안(**Model Armor**, **Firebase App Check**)과 서버리스 확장(**Cloud Run**, **Firebase**)을 3대 축으로 설계

---

## 📣 주요 발표 내용
- **Flutter**: iOS/Android 단일 코드베이스로 모바일 앱 구현. `firebase_ai` Logic SDK for Dart·Flutter로 클라이언트에서 직접 Gemini API 호출 가능
- **Model Garden**: Google Gemini, Anthropic Claude, 오픈소스 모델을 **단일 API**로 접근 — 모델 교체 시 코드 변경 최소화
- **Model Armor**: 프롬프트 인젝션, 데이터 유출, 유해 콘텐츠 방지
- **Firebase App Check**: 요청이 정상 디바이스의 정식 앱에서만 발생하는지 검증
- **Firebase Authentication + Identity Platform**: Google/Facebook/Apple SSO, 전화번호 인증 지원, **99.95% SLA**
- **Firebase 부가 서비스**: `Crashlytics`(크래시 추적), Performance Monitoring, Remote Config(앱 재배포 없이 설정 변경), Cloud Messaging
- **Google Apigee**: 모든 백엔드의 통합 진입점 — API 설계·보안·모니터링·스케일링
- **Cloud Run**: 서버 관리 없는 서버사이드 로직. **Dart 런타임 지원** 추가로 Flutter 풀스택 개발 가능
- **Cloud Operations Suite**: Cloud Run 오류, API 레이턴시, 모델 성능을 단일 뷰에서 통합 모니터링

---

## 💡 개발자 포인트
> **Flutter → Firebase AI Logic SDK → Model Garden** 경로로 클라이언트에서 직접 LLM 호출이 가능해졌으나, 프로덕션에서는 반드시 **Model Armor + Firebase App Check** 를 함께 적용해야 한다.

- **Cloud Run이 이제 Dart를 지원** — Flutter 앱과 동일한 언어로 백엔드 작성 가능, 풀스택 Dart 아키텍처 구현 가능
- Model Garden은 Gemini·Claude·오픈소스 모두 동일 API 형태로 제공 → 모델 A/B 테스트나 교체가 쉬움
- `Remote Config`를 활용하면 앱스토어 심사 없이 AI 모델 설정·프롬프트 등을 동적으로 업데이트 가능
- Firebase 프로젝트 = Google Cloud 프로젝트이므로 두 플랫폼의 서비스를 자유롭게 조합 가능

---

## 📅 버전 / 출시 일정
해당 없음

# Introducing Genkit Dart

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=QO30-W3b_vw
- **요약 일시**: 2026-05-22 09:07:51

---

## 🔑 핵심 요약
- **Genkit이 Dart를 공식 지원**하여 Flutter 개발자가 프론트엔드·백엔드 모두 Dart로 풀스택 개발 가능
- **Firebase App Check + 커스텀 인증 클레임 + Rate Limiter + 캐싱**으로 Genkit API 엔드포인트를 다층 보안
- **프롬프트 인젝션 방지**를 위해 URL 직접 입력 대신 Product ID만 받아 서버에서 조회하는 패턴 권장

---

## 📣 주요 발표 내용
- **Genkit Dart 지원 시작**: `dart create -t server-shelf vto-dart` 명령으로 shelf 서버 생성 후 Genkit 의존성 추가하면 백엔드 구축 완료
- **Flow 구조**: input/output 스키마 정의 → Genkit 플러그인 초기화(원하는 모델) → 비즈니스 로직(예: 제품 SKU → 이미지) Flow 정의
- **Firebase App Check 통합**: shelf Handler 통합으로 `X-Firebase-AppCheck` 헤더에서 limited-use 토큰을 추출·검증
  - 토큰 유효 시간: **5분**, 1회만 사용 가능 (`consume` 옵션으로 재사용 방지)
- **플랫폼별 디바이스 검증 제공자**:
  - Web: **reCAPTCHA Enterprise**
  - Android: **Play Integrity**
  - iOS: **App Attest**
  - Desktop: 커스텀 attestation provider 지원
- **사용자 권한 검증**: `authorization` 헤더에서 토큰 추출 → custom claim(`isPremiumUser` 등) 확인 → DB 추가 조회 없이 권한 판단
- **Rate Limiting**: 사용자 컬렉션에 요청 시각 기록 → aggregation query로 최근 1시간 요청 수 카운트 (1000건당 1 read)
- **결과 캐싱**: generate 호출 결과 이미지를 버킷에 저장 → 동일 제품 재요청 시 캐시 반환으로 API 비용 절감

---

## 💡 개발자 포인트
> **⚠️ Breaking 보안 패턴 변경**: 사용자 입력으로 URL을 직접 받지 말고 **Product ID만 받은 뒤 서버 측 Firestore/Storage에서 조회**할 것. URL을 받으면 프롬프트 인젝션으로 의도하지 않은 제품 이미지가 생성될 수 있음.

- **풀스택 Dart 가능**: Flutter 앱과 Genkit 백엔드 모두 동일 언어로 작성 → 타입 공유·생산성 향상
- **App Check는 디바이스 신뢰성만 보장**, 사용자 권한은 별도 인증 토큰으로 검증해야 함 (둘 다 필요)
- **Custom Claims 활용**: Firestore 추가 read 없이 premium 여부 등을 토큰 검증 단계에서 판단 가능 → 비용·지연 절감
- **다층 방어 전략**: 디바이스 검증(App Check) → 사용자 인증(custom claims) → Rate Limiting → 결과 캐싱 → 입력 sanitization 순으로 적용
- **shelf Handler 패턴**: Dart `shelf` 미들웨어로 토큰 검증 Handler를 체이닝하여 재사용 가능

---

## 📅 버전 / 출시 일정
해당 없음 (Genkit Dart 공식 지원 발표)


# Full-stack Dart: Cloud Functions for Firebase & Flutter Demo

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=0P17edjvTSw
- **요약 일시**: 2026-05-06 15:00:59

---

## 🔑 핵심 요약
- **Dart 언어**를 백엔드(`Firebase Cloud Functions`)에서도 사용 가능 — 풀스택 Dart 개발 시대 도래
- 프론트엔드와 **비즈니스 로직 공유**, **타입 안정성**, **AOT 컴파일 기반 near-instant cold start** 확보
- 서버 코드도 **Hot Reload**로 즉시 반영 — 운영 중인 함수 로직을 실시간 변경 가능

---

## 📣 주요 발표 내용
- **Google Cloud Next '26**에서 공개된 Full-stack Dart 데모
- `Firebase Cloud Functions`에 **Dart 런타임 지원** 추가
- Flutter 클라이언트(Android 등)와 동일 언어로 서버 함수 작성
- 데모 시나리오: **Flutter Clicker** (멀티플레이어 카운터 앱)
  - 클라이언트 버튼 텍스트를 `increment` → `decrement`로 변경 시 클라이언트만 Hot Reload되어 표시는 바뀌지만 서버 동작은 그대로
  - **서버측 Cloud Function 로직**을 `increment` → `decrement`로 수정 → 즉시 반영되어 클릭 시 값이 감소
- `Node.js`/`Python` 런타임 대비 **콜드 스타트 속도** 우위 강조

---

## 💡 개발자 포인트
- **AOT 컴파일된 실행 파일**로 배포되어 `Node`/`Python` 런타임 부팅 비용이 없음 → **서버리스 콜드 스타트 최적화**
- 동일 모델·DTO·Validation 코드를 **클라이언트와 서버에서 재사용** 가능 → 코드 중복·타입 불일치 제거
- 서버 Hot Reload 지원으로 **개발 루프(dev loop) 가속** — Firestore 등 백엔드 상태를 유지한 채 함수 로직 갱신
- Flutter 단일 스택으로 **모바일/웹/서버**까지 커버 가능한 구조

> **참고**: Dart on Firebase Functions는 커뮤니티가 2011년부터 기다려온 기능이라고 발표자가 언급할 만큼 오랜 숙원이었음. 기존 `firebase-functions` (Node.js) 프로젝트와의 공존·마이그레이션 전략 확인 필요.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 발표 행사 | Google Cloud Next '26 |
| 기능 | Dart 지원 Firebase Cloud Functions |
| 정식 출시일 | 영상 내 명시되지 않음 (데모 단계) |


# Full-stack Dart: Cloud Functions for Firebase & Flutter Demo

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=0P17edjvTSw
- **요약 일시**: 2026-05-06 14:46:54

---

## 🔑 핵심 요약
- **Dart**를 `Firebase Cloud Functions` 백엔드 언어로 사용해 **풀스택 Dart** 개발이 가능해짐
- 프론트엔드(Flutter)뿐 아니라 **서버 코드도 Hot Reload**로 즉시 반영되는 데모 시연
- **AOT 컴파일** 덕분에 Node.js·Python 대비 **콜드 스타트가 거의 즉시**에 가까운 속도

---

## 📣 주요 발표 내용
- **Google Cloud Next 26**에서 공개된 Flutter × Firebase 풀스택 데모
- 멀티플레이어 카운터 앱(`Flutter clicker`)으로 시연 — 사용자별 카운트와 전역 총합을 실시간 동기화
- 서버 측 로직을 **`increment` → `decrement`** 으로 즉시 변경하는 Hot Reload 시연
- **Dart 단일 언어**로 클라이언트·서버 비즈니스 로직 공유 + 타입 안전성 확보
- **AOT 컴파일된 실행 파일**로 Cloud Functions 실행 → 런타임 부팅 오버헤드 제거

---

## 💡 개발자 포인트
- Flutter 앱과 백엔드 함수를 **하나의 언어·하나의 타입 시스템**으로 통합 가능
- 서버 로직 변경이 빌드/배포 사이클 없이 거의 즉시 반영되어 **iteration 속도 대폭 개선**
- `Firestore` 등 Firebase 서비스와 자연스럽게 결합

> **콜드 스타트 측면**: Node·Python 기반 Cloud Functions 대비 Dart는 AOT 컴파일된 네이티브 바이너리로 실행되어, 서버리스 환경에서 가장 빠른 부팅 속도를 보임. 지연 민감한 API 게이트웨이용으로 강력한 선택지.

> 커뮤니티가 **2011년부터** 기다려 온 기능 — 발표자들도 오랜 숙원이었다고 언급

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|------|------|
| 발표 행사 | Google Cloud Next 26 |
| 공개일 | 2026-05-05 |
| 대상 플랫폼 | Firebase Cloud Functions (Dart 런타임) |
| 클라이언트 | Flutter (Android 데모) |


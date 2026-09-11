# Contiuing the Flutter starter app | Observable Flutter #96

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=tdGc22xrcSk
- **요약 일시**: 2026-09-11 09:04:34

---

## 🔑 핵심 요약
- **Observable Flutter #96**: Craig가 지난 주에 이어 재사용 가능한 Flutter 스타터 앱을 계속 개발하는 라이브 스트림
- 백엔드는 **ServerPod 4.0 pre-release**, 라우팅은 **Kaisle**, 상태관리는 **Bloc Signal**을 사용하는 스택 탐구
- `Kaisle 1.1` 정식 릴리스 확인, `Bloc Signal`의 `GenUI` 지원도 곧 출시 예정

---

## 📣 주요 발표 내용
- **Kaisle 1.1** 릴리스 - 이전 `go_router` 대비 경로를 클래스 단위로 관리하는 API 방식 소개
- **Bloc Signal**이 스트림 없이도 중복 상태 감지(rebuild 방지) 지원 확인
- `Bloc Signal`의 **GenUI** 통합 기능 곧 출시 예정 (`listenable` 트리거 편의성 향상)
- **ServerPod 4.0 pre-release** 사용 중 - 백엔드 API 서버와 Flutter 앱 연동
- Mason brick 대신 AI 스킬로 스타터 템플릿 생성하는 방향 논의 중

---

## 💡 개발자 포인트
- **Kaisle 라우팅 패턴**: `KaisleRoute`를 상속받아 커스텀 부모 클래스를 만들고, 개별 경로를 클래스로 정의. `router` 빌더에서 현재 route → screen 변환 로직을 중앙화
- **가드(Guard) + 리다이렉션**: `KaisleGuard` 타입으로 현재 route와 이동할 route를 받아 조건부 리다이렉션 처리 가능
- **Bloc Signal vs Flutter Bloc**: Bloc Signal은 스트림 미사용 → 중복 상태 emit 시 UI rebuild를 core 레벨에서 차단 (디바운싱과 유사)

> **주의**: 스타터 앱에 ServerPod boilerplate가 포함되어 있어, Mason brick으로 배포 시 ServerPod 의존성을 어떻게 처리할지 아직 미결. 현재 Craig의 GitHub(`starter_flutter_app`)에서 소스 확인 가능.

---

## 📅 버전 / 출시 일정

| 패키지 | 버전 | 비고 |
|---|---|---|
| `kaisle` | 1.1 | 정식 릴리스 완료 |
| `serverpod` | 4.0 (pre-release) | 현재 사용 중 |
| `bloc_signal` | - | GenUI 통합 곧 출시 예정 |


# Widget previews are FINALLY stable in Flutter 3.47! 🔍

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=Tovm9bWNGpE
- **요약 일시**: 2026-10-02 09:03:37

---

## 🔑 핵심 요약
- **Flutter 3.47**에서 **Widget Previews(위젯 미리보기)**가 공식 **Stable**로 승격
- 앱 전체를 실행하지 않고 개별 위젯을 실시간으로 설계·검사·수정 가능
- Apple 플랫폼: **Swift PM** 파이프라인 개선으로 빌드 시간 단축, iOS 코드 서명 정보 표시 개선

---

## 📣 주요 발표 내용
- **Widget Previews Stable**
  - 버튼 하나 확인하려고 앱 전체를 빌드·실행할 필요가 없음
  - 개별 위젯 단위로 실시간 설계·검사·수정 지원
- **Swift Package Manager 파이프라인 개선**
  - 빌드 초기 단계에서 불필요한 패키지 스키마(scheme)를 걸러냄
  - 결과적으로 Apple 플랫폼 빌드 시간 단축
- **iOS 코드 서명 투명성 향상**
  - 인증서 선택 시 **Team ID**와 **Team 이름**을 함께 표시

---

## 💡 개발자 포인트
- 업그레이드: `flutter upgrade` 실행 후 3.47로 전환
- UI 컴포넌트 개발 시 Widget Previews로 **반복 주기(iteration)를 크게 단축** 가능 — 디자인 시스템/공통 위젯 작업에 특히 유용
- 여러 Apple 개발자 팀에 속한 경우, 코드 서명 시 Team ID + 이름 표시 덕분에 잘못된 인증서 선택 실수 감소

> Widget Previews가 Stable이 되었으므로, 이전 실험(experimental) 단계에서 사용하던 프로젝트는 3.47 기준 API/설정을 다시 확인하는 것을 권장

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|---|---|
| Flutter 버전 | **3.47** |
| Widget Previews | Stable |
| 설치 방법 | `flutter upgrade` |


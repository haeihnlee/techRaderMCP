# Is there an update on liquid glass implementation?

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=ZXahZAdYfDY
- **요약 일시**: 2026-11-20 09:03:32

---

## 🔑 핵심 요약
- Flutter 팀이 **Liquid Glass** 공식 구현 작업에 **이미 착수**했습니다
- Cupertino 위젯을 프레임워크에서 별도 패키지(`cupertino_ui`)로 분리하면서 이 작업을 시작할 수 있게 됐습니다
- 서드파티 Liquid Glass 위젯·렌더러 개발자들과 협력해 고품질 셰이더 로직을 공식 패키지로 가져올 예정입니다

---

## 📣 주요 발표 내용
- #FlutterCreate 커뮤니티 질문에 대한 답변입니다: "서드파티 Liquid Glass 패키지는 프레임 속도가 낮은데, 공식 업데이트는 언제 나오나?"
- Cupertino UI 위젯이 Flutter 프레임워크 코어에서 **별도 패키지로 분리**됐습니다
- pub.dev에는 이미 Liquid Glass 구현 패키지가 **30개 이상** 있습니다
- 프레임워크 팀은 **liquid glass widgets / liquid glass renderer** 패키지 개발자들과 긴밀히 협력하고 있습니다
- 커뮤니티가 만든 고품질 초기 **셰이더**를 프레임워크, 특히 **Cupertino UI 패키지**에 통합할 계획입니다
- 진행 상황은 **매주 업데이트**로 공개될 예정입니다

---

## 💡 개발자 포인트
- 현재 서드파티 Liquid Glass 패키지는 **프레임 드랍** 등 성능 이슈가 있을 수 있습니다. 프로덕션에 도입할 때는 프로파일링이 필요합니다
- 공식 구현은 Cupertino UI 패키지 쪽에서 나올 가능성이 높으므로, 해당 패키지의 릴리스와 주간 업데이트를 지켜보는 것이 좋습니다
- 공식 구현이 커뮤니티 셰이더를 바탕으로 만들어지므로, 지금 쓰는 liquid glass renderer 계열 패키지에서 나중에 옮겨가기가 비교적 수월할 수 있습니다

> Cupertino 위젯이 별도 패키지로 분리됐기 때문에, 앞으로 iOS 스타일 위젯 업데이트는 Flutter SDK 릴리스가 아니라 **패키지 버전**을 따라 배포될 수 있습니다. 의존성 관리에 유의하세요.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| 공식 Liquid Glass 출시 일정 | 발표되지 않음 (작업 진행 중) |
| 진행 상황 공유 | 매주 업데이트 예정 |
| pub.dev 서드파티 구현 수 | 30개 이상 |


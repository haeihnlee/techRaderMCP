# Android Developers Blog: Land your apps on Googlebook with adaptive development

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/09/adaptive-development-scale-app-googlebook.html
- **요약 일시**: 2026-09-23 09:05:55

---

## 🔑 핵심 요약
- **Googlebook**: HP, Dell, Lenovo, Acer, Asus 등 파트너사의 Android 기반 신형 노트북 카테고리로, 모바일 편의성과 데스크탑 성능을 결합
- 기존 **Adaptive Layout** 코드베이스를 활용해 별도 앱 빌드 없이 Googlebook 최적화 가능
- Google Play에서 최적화 앱에 **전용 배지·큐레이션 컬렉션·검색 우선 노출** 혜택 제공

---

## 📣 주요 발표 내용
- **Googlebook** 소개: OLED 터치스크린, 전용 키보드, 정밀 트랙패드, 하루 종일 배터리, Gemini Intelligence 내장
- Google Play에서 최적화 앱을 위한 **전용 배지(badging)**, 향상된 검색, 큐레이션 홈페이지 피처 제공
- **Apps Experience Program** 연계: 비즈니스 성장을 위한 새로운 요금 카드 프로그램 참여 가능
- Android 폰으로 Googlebook 초기 설정 시 최적화 앱이 **Day-1 전송 대상**으로 우선 표시
- `Navigation 3`의 `ListDetailSceneStrategy`, `SupportingPaneSceneStrategy`로 멀티 패인 레이아웃 구현
- `Grid`, `FlexBox`, 실험적 `MediaQuery`·`Styles APIs`로 데스크탑 레이아웃 구성
- `contextual cursors`, 우클릭 컨텍스트 메뉴, 호버 상태, `Keyboard Shortcuts Helper` 지원
- `multi-instance support`로 독립 창 동시 실행, `drag and drop`으로 창 간 콘텐츠 이동
- `Continue On` / `HandoffActivityData`로 폰·태블릿·Googlebook 간 태스크 이어받기
- **Android Studio Canary**에서 데스크탑 에뮬레이터로 자유 창 리사이즈·멀티 인스턴스 테스트 가능
- `adaptive skill`을 Android CLI로 설치하면 AI 에이전트가 모바일 레이아웃을 Compose 반응형 컨테이너로 자동 리팩토링

---

## 💡 개발자 포인트
- **Window size classes 기반** 레이아웃을 이미 구현한 앱이라면 Googlebook 최적화 비용 최소화
- 모바일 UI를 단순히 확대하지 말고, `multi-pane architecture`로 콘텐츠를 기능 그룹으로 재배치
- 레이아웃 결정은 물리적 디스플레이 크기가 아닌 **window size classes** 기준으로 처리

> **주의:** 자유 창(free-form windowing) 환경에서는 앱 창이 언제든 동적으로 리사이즈됩니다. 물리 화면 크기 기반 로직은 예상치 못한 레이아웃 오류를 유발할 수 있으니 반드시 window size classes를 사용하세요.

- Caption header bar를 커스텀 배경, 검색바, 탭으로 스타일링 가능 (`header bar styling`)
- Notability 사례: 태블릿·폴더블용 코드가 그대로 Googlebook에 적용, `Continue On`과 사이드바이사이드 경험에만 추가 개발 투자

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| 포스트 게시일 | 2026년 9월 22일 |
| Android Studio 데스크탑 에뮬레이터 | Canary 버전에서 현재 사용 가능 |
| `adaptive skill` (Android CLI) | 현재 설치 가능 |
| `Navigation 3` | 현재 사용 가능 (멀티 패인 지원) |
| 실험적 `MediaQuery`·`Styles APIs` | 출시 예정(soon) |

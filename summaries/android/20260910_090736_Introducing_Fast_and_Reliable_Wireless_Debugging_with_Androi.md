# Introducing Fast and Reliable Wireless Debugging with Android Debug Bridge (ADB) Wi-Fi 2.0

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/09/wireless-debugging-adb-wifi-2.html
- **요약 일시**: 2026-09-10 09:07:36

---

## 🔑 핵심 요약
- **ADB Wi-Fi 2.0** 출시로 무선 디버깅의 연결 안정성·속도가 대폭 향상
- 자동 연결 성공률 **32% 향상**, 연결 속도 **66% 개선** (90th percentile 기준)
- **Android 17** + **Android SDK Platform-Tools 37.0.0** + **Android Studio Quail 3** 이상에서 사용 가능

---

## 📣 주요 발표 내용
- **새로운 adb 서버 스택**: Bonjour와 레거시 mDNS를 모두 새 mDNS 스택으로 교체
  - 네트워크 구성 변경이나 기기 재시작 시 연결이 끊기던 문제 해결
- **스마트 네트워크 처리 (adbd)**: 신뢰할 수 없는 네트워크 감지 시 ADB Wi-Fi 자동 비활성화, 허용된 네트워크 복귀 시 자동 재활성화
- **Android Studio 페어링 UI 개선**: 기기에서 무선 디버깅 활성화 시 **Device Manager**에 자동으로 표시
- 지원 폼팩터: 휴대폰, 태블릿, **Wear OS**, **TV**

---

## 💡 개발자 포인트
> **Android 17**, **SDK Platform-Tools 37.0.0**, **Android Studio Quail 3** 이상으로 업데이트해야 ADB Wi-Fi 2.0을 사용할 수 있습니다.

- 워크스테이션과 Android 기기가 **동일한 Wi-Fi 네트워크**에 연결되어 있어야 합니다
- 기기의 **개발자 옵션**에서 무선 디버깅 활성화 → Android Studio Device Manager에서 `pair over Wi-Fi` 아이콘 클릭 → QR 코드 스캔 또는 페어링 코드 입력

---

## 📅 버전 / 출시 일정

| 컴포넌트 | 최소 버전 |
|---|---|
| Android OS | Android 17 |
| SDK Platform-Tools | 37.0.0 |
| Android Studio | Quail 3 |


# Bring your Android game to the car screen today

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/09/bring-android-game-to-car-screen.html
- **요약 일시**: 2026-09-22 09:06:27

---

## 🔑 핵심 요약
- **Android Auto** 및 **Android Automotive OS** 의 게임 카테고리가 베타에서 **정식 출시(GA)** 로 졸업
- 기존 Android 게임을 차량 화면에 배포하려면 매니페스트 설정과 **주차 상태(parked state)** 처리가 핵심
- Google Play의 오픈 테스트·프로덕션 트랙에 게임을 정식 게시 가능

---

## 📣 주요 발표 내용
- **게임 카테고리 GA 출시**: 이전 얼리 액세스 파트너에만 열려 있던 차량용 게임이 이제 모든 개발자에게 개방
- **Android Auto 지원**: Android 15 이상 기기에서 동작
- **지원 플랫폼 2종**:
  - `Android Auto` — 스마트폰 연결 방식
  - `Android Automotive OS (Google built-in)` — 차량 내장 OS
- **게임 컨트롤러 지원 선언** 가능 (`android.hardware.gamepad` 피처 선언 시 Play Store 노출 가중)
- **다양한 화면 비율 지원** 필수 (세로형 및 와이드 가로형 포함, 레터박스·필러박스 금지)

---

## 💡 개발자 포인트

### 매니페스트 설정 요약

| 항목 | 설정 |
|---|---|
| 앱 카테고리 선언 | `android:appCategory="game"` |
| Android Auto 지원 | `<category android:name="android.intent.category.CAR_LAUNCHER" />` |
| Android Automotive OS 지원 | `<uses-feature android:name="android.hardware.type.automotive" android:required="false" />` |
| 게임 컨트롤러 지원 | `<uses-feature android:name="android.hardware.gamepad" android:required="false"/>` |

### 주차 상태(parked state) 처리

> **중요**: 게임은 주차 중에만 실행 가능한 "parked app"으로 분류됩니다.  
> 주행 중 게임이 실행되지 않도록 `distractionOptimized` 메타데이터를 액티비티에 **절대 추가하지 마세요**.

- 차량이 움직이기 시작하면 **게임 오디오 반드시 정지** 및 재개 불가 처리 필요
- 앱 재실행 시 **이전 상태를 최대한 복원**해야 함 (프리징·스터터링 없이)

### 배포 트랙 선택 시 주의

> `android:required="false"` 설정은 모바일 트랙 배포 시 필수입니다.  
> Android Automotive OS 전용 트랙 배포 시에는 `"true"` 또는 미설정도 가능 (미설정 = `"true"` 동일 효과).

### 테스트 도구
- **Desktop Head Unit (DHU)**: Android Auto 호환성 테스트
- **Android Automotive OS 에뮬레이터**: 차량 내장 OS 테스트
- **번들 하드웨어 프로파일**: 에뮬레이터에서 표준 화면 크기 테스트

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|---|---|
| Android Auto 지원 최소 버전 | Android 15 이상 |
| 게임 카테고리 GA 출시일 | 2026년 9월 21일 |
| 이전 상태 | 베타 (얼리 액세스 파트너 한정) |


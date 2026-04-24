# Boosting user privacy and business protection with updated Play policies

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/04/giving-users-clearer-choice-and-everyone-a-safer-more-trusted-app-ecosystem.html
- **요약 일시**: 2026-04-16 09:04:33

---

## 🔑 핵심 요약
- **Google Play** 정책 업데이트로 연락처·위치 접근 방식이 새로운 표준으로 전환됨
- 앱 내 연락처/위치 권한 사용 방식을 변경하지 않으면 **앱 심사 거절** 가능
- 계정 소유권 이전은 반드시 **공식 Play Console 기능**을 통해서만 가능

---

## 📣 주요 발표 내용

### 📇 Android Contact Picker (연락처 접근 정책 변경)
- **Android Contact Picker**가 연락처 접근의 새로운 표준으로 도입
- 사용자가 원하는 **특정 연락처만 선택**해서 공유하는 방식으로 전환
- `READ_CONTACTS` 권한은 해당 권한 없이는 앱 자체가 동작 불가한 경우에만 예외적으로 허용
- **Sharesheet** 등 프라이버시 중심 대안도 허용

### 📍 Location Button (위치 접근 정책 변경)
- 일회성 정밀 위치 접근을 위한 **새로운 위치 버튼** 도입
- 복잡한 권한 다이얼로그 → **단일 탭**으로 대체
- 일회성 위치 사용 앱은 반드시 이 버튼을 사용해야 함
- 매니페스트에 `onlyForLocationButton` 플래그 추가로 구현

### 🔐 Account Transfer (계정 소유권 이전)
- Play Console 내 **공식 계정 이전 기능** 정식 출시
- 제3자 마켓플레이스를 통한 계정 매매 등 **비공식 이전은 전면 금지**
- 모든 이전에 **7일 보안 유예 기간** 의무 적용

---

## 💡 개발자 포인트

### 연락처 권한 대응
- **Android 17 이상** 타겟팅 시, 공유/초대 기능에서 `READ_CONTACTS` 제거 필수
- 전체 연락처 목록에 지속적인 접근이 필요한 경우, **Play Developer Declaration** 제출 필요

> ⚠️ **Breaking Change**: `READ_CONTACTS` 권한을 단순 공유·초대 용도로 계속 사용하면 정책 위반으로 앱 심사 통과 불가

### 위치 권한 대응
- **Android 17 이상** 타겟팅 시, 일회성 정밀 위치 사용 앱은 `onlyForLocationButton` 플래그 구현 필수
- 지속적인 정밀 위치가 필요한 경우 **Play Developer Declaration** 제출로 예외 사유 소명 필요

> ⚠️ **Breaking Change**: 일회성 위치 접근에 기존 권한 다이얼로그 방식을 유지하면 정책 위반 처리 가능

### 계정 이전 대응

> 🚨 **주의**: 2025년 5월 27일 이후 로그인 정보 공유, 제3자 플랫폼을 통한 계정 매매 등 비공식 이전은 **정책 위반**으로 처리됨

- 향후 모든 계정 소유권 변경은 Play Console → **"Users and permissions"** 페이지에서만 진행

### 🛠️ 사전 점검 도구 (10월 이후 제공)
- **Android Studio** 내 Play Policy Insights: 정책 위반 가능성 사전 탐지
- **Play Console** 사전 심사 체크: 제출 전 연락처·위치 권한 이슈 자동 플래그 처리

---

## 📅 버전 / 출시 일정

| 날짜 | 내용 |
|------|------|
| **2026년 5월 27일** | 공식 계정 이전 기능 의무화 (비공식 이전 전면 금지) |
| **2026년 10월** | Play Console 내 Play Developer Declaration 양식 제공 시작 |
| **2026년 10월** | Android Studio Play Policy Insights 기능 제공 |
| **2026년 10월 27일** | Play Console 사전 심사(Pre-review) 체크 기능 활성화 |
| **Android 17 이상 타겟팅 시** | `READ_CONTACTS` 제거 및 `onlyForLocationButton` 플래그 적용 필수 |

# Building the Cloud Next demo (yet again) | Observable Flutter #87

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=feN_LXbwrlk
- **요약 일시**: 2026-04-08 16:00:41

---

## 🔑 핵심 요약
- **Google Cloud Next** 및 **Google I/O** 행사용 Flutter 키오스크 데모 앱을 라이브로 개발 중인 에피소드
- **Gemini** 기반 이미지 생성 + **에디블 잉크 라테 프린터** 연동 데모 앱 구현 작업
- **Firebase Cloud Functions** 호출 오류 디버깅 및 **WebAssembly(Wasm)** 모드 첫 테스트 진행

---

## 📣 주요 발표 내용

- 🎯 데모 앱 개요: 사용자가 Flutter 키오스크에서 "행복한 장소"를 텍스트로 입력 → **AI 이미지 생성** → 에디블 잉크로 커피 위에 인쇄
- 🧠 **Gen UI** 기능: 생성된 이미지를 4가지 질문(디테일, 피사체 종류, 조명, 줌 레벨)으로 수정 가능
- 🔒 **콘텐츠 모더레이션**: 이미지에 사람을 포함하지 못하도록 프롬프트 제어 중 (`do not put people` 반복 지시)
- 🌐 **Wasm 모드** (`--wasm` 플래그)로 앱을 빌드하여 브라우저에서 실행 테스트 (포트 `8080`)
- ⚠️ `generateRevisedImages` **Cloud Function** 호출 시 `Unable to establish connection` 오류 발생

---

## 💡 개발자 포인트

- `generateRevisedImagesstaging` 함수가 Firebase Console에 정상 배포되어 있음에도 클라이언트에서 연결 실패
- 빌드 히스토리는 모두 ✅ 초록불이나 실제 함수 동작 불가 → **배포 성공 ≠ 함수 정상 동작** 임을 주의

> ⚠️ **Breaking 주의**: 환경 변수(Firebase 프로젝트 환경)가 코드 내 하드코딩(`dependency_injection.dart`)되어 있어, Wasm 모드 등 다른 실행 환경에서 함수 엔드포인트 연결이 실패할 가능성 있음. 환경 설정 외부화가 필수 TO-DO 항목으로 언급됨.

- **Wasm 모드**에서 일부 로컬 에셋이 렌더링되지 않는 문제 발견 (에러 메시지 없이 에셋 누락)
- **DI(Dependency Injection)** 파일에 환경 설정을 직접 작성하는 구조는 임시방편이며 리팩토링 필요
- Cloud Logging에서 "현재 시간" 기준 로그 필터링 버튼이 직관적이지 않아 디버깅 난이도 상승

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| **Google Cloud Next** | 라스베이거스, 약 2주 후 (촬영 시점 기준) |
| **Google I/O** | Cloud Next 이후 (동일 데모 리스킨 버전 전시) |
| **Observable Flutter** | 에피소드 #87 (4회차 연속 데모 개발 시리즈) |
| **호스트 생일** | 촬영 기준 2일 후 (만 40세) |

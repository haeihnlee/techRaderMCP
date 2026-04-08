# firebase_ai (Package of the Week)

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=tp7Ojf7dPVI
- **요약 일시**: 2026-04-08 16:01:33

---

## 핵심 요약 (3줄)
- `firebase_ai` 패키지는 Flutter 앱에서 Gemini 및 Imagen API를 서버리스로 직접 호출할 수 있는 올인원 패키지다.
- 텍스트 생성, 이미지 생성/편집, 실시간 스트리밍(Live API), 멀티턴 대화(Chat) 등 다양한 AI 기능을 지원한다.
- Firebase 프로젝트 연동 후 몇 줄의 코드만으로 Gemini 모델을 Flutter 앱에 통합할 수 있다.

---

## 주요 발표 내용

- **패키지 구성**: `firebase_core` + `firebase_ai` 두 패키지 추가 및 `FlutterFire Configure` 명령으로 Firebase 프로젝트 연동
- **지원 모델 타입 3가지**
  - `GenerativeModel` : 텍스트 등 일반 콘텐츠 생성 (싱글턴 인터랙션)
  - `LiveModel` : Gemini Live API를 통한 입출력 실시간 스트리밍
  - `ImagenModel` : 이미지 생성 및 편집 (Imagen API)
- **프롬프트 구성**: 텍스트, 이미지, 영상, 오디오, 문서 등 멀티모달 입력 지원
- **이미지 생성 모델** (Gemini Flash Image, 코드명 "Nano Banana"):
  - `GenerationConfig`에서 응답 타입을 `text + image`로 명시 필요
  - 응답에서 `inlineData` 파트로 이미지 데이터 추출
- **멀티턴 대화**: `model.startChat()` 호출 후 `sendMessage()`로 대화 진행, Firebase AI Logic이 자동으로 채팅 히스토리 관리

---

## 개발자에게 중요한 포인트

- **Firebase Console 설정 필수**: 프로젝트 생성 후 *Gemini Developer in Firebase AI Logic APIs* 명시적 활성화 필요
- **모델 초기화 시 Provider 지정**: `GeminiDeveloperApiProvider` + 모델명을 명시적으로 전달해야 함
- **이미지 응답 파싱 주의**: 일반 텍스트 응답과 달리 이미지 생성 시 `response.inlineDataParts`에서 별도 추출 로직 필요
- **멀티턴 대화 구현 간소화**: 직접 히스토리 배열을 관리할 필요 없이 `startChat()` + `sendMessage()` 패턴으로 SDK가 자동 처리
- **서버리스 구조**: 별도 백엔드 없이 Flutter 클라이언트에서 직접 Gemini/Imagen API 호출 가능 → 빠른 프로토타이핑에 유리
- **pub.dev 참고**: 추가 모델 옵션 및 상세 API 문서는 [pub.dev](https://pub.dev) 확인 권장

---

## 출시 일정 / 버전 정보

해당 없음 (영상 내 특정 버전 번호 또는 출시 예정일 언급 없음)

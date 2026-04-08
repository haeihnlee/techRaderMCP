# Building the Cloud Next demo (yet again) | Observable Flutter #87

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=feN_LXbwrlk
- **요약 일시**: 2026-04-08 16:00:41

---

## 핵심 요약 (3줄)
- Flutter 앱을 활용한 Google Cloud Next / Google I/O 전시용 인터랙티브 커피 라테 아트 데모를 실시간으로 개발 중
- 사용자가 "행복한 장소"를 텍스트로 입력하면 AI(Gemini)가 이미지를 생성하고, 식용 잉크 프린터로 커피 위에 인쇄하는 플로우 구현
- Cloud Functions 호출 오류 발생으로 디버깅을 시도했으나 원인을 특정하지 못하고, Firestore 수동 데이터 입력으로 작업 방향을 전환

## 주요 발표 내용
- **데모 앱 전체 플로우**: 키오스크 UI → 이름/음료 옵션 입력 → 행복한 장소 텍스트 입력 → AI 이미지 생성 → 이미지 수정(Gen UI 질문 4가지) → 라테 프린터 전송
- **Gen UI(생성형 UI)**: 이미지 수정 단계에서 디테일 수준, 피사체 종류, 조명, 카메라 줌 등 4가지 동적 질문을 통해 프롬프트를 재구성하는 방식 적용
- **콘텐츠 모더레이션**: 이미지에 사람(인물)을 포함하지 않도록 프롬프트 수준에서 제한 적용 중 (레드팀 테스트 시연)
- **WebAssembly(WASM) 빌드**: Flutter Web을 WASM 모드로 실행 시도 (`--wasm` 플래그 사용), 일부 에셋 로딩 문제 확인
- **Firebase 활용**: Cloud Functions(generate revised images staging), Firestore(이미지 컬렉션 배치), Firebase Console 로그 탐색 등 Firebase 풀스택 구성
- **의존성 주입(DI) 파일**: Cloud Functions 엔드포인트 URL이 여전히 하드코딩 되어 있어 환경변수화가 미완료 상태임을 언급

## 개발자에게 중요한 포인트
- **Cloud Functions 디버깅**: `Unable to establish connection` 오류 발생 시 배포 히스토리(Build history)와 Cloud Logging을 먼저 확인하는 접근법 시연 — 단, 이번 케이스는 로그에서도 원인 미확인
- **WASM 빌드 시 에셋 문제**: Flutter Web을 WASM 모드로 전환할 때 일반 Web과 에셋 로딩 동작이 다를 수 있으므로 별도 검증 필요
- **하드코딩된 환경 설정 주의**: Functions URL, 포트 번호 등을 DI 파일에 하드코딩하는 패턴은 환경별(dev/staging/prod) 분리가 안 되므로 환경변수 또는 설정 파일로 분리 필요 (발표자 본인도 TO-DO로 인식 중)
- **Firestore 수동 시딩**: Cloud Functions가 정상 동작하지 않는 상황에서 Firestore 콘솔을 통해 직접 문서를 추가하는 임시 우회 방법 활용
- **콘텐츠 안전 처리**: 생성 이미지에 특정 콘텐츠(인물 등)를 제외할 때 프롬프트 레벨 제한만으로는 완전하지 않으며, 별도 모더레이션 레이어 고려 필요

## 출시 일정 / 버전 정보
- **Google Cloud Next (라스베이거스)**: 방송 시점 기준 약 2주 후 전시 예정
- **Google I/O**: Cloud Next 이후 동일 데모를 리스킨하여 전시 예정
- Flutter/Dart 특정 버전 정보는 언급 없음

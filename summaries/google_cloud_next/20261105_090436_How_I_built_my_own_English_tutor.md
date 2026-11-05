# How I built my own English tutor

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=f0Fwl5EsZNQ
- **요약 일시**: 2026-11-05 09:04:36

---

## 🔑 핵심 요약
- 발표자는 영어가 모국어가 아니라서 일상 대화로 연습할 수 있는 **개인 영어 튜터** 앱을 직접 만들었습니다.
- 대화 엔진은 **Gemini Live API**로 실시간 대화를 처리하고, 요청하면 문법·표현 피드백도 줍니다.
- 백엔드는 **Cloud Run**에 올려 **0까지 축소(scale-to-zero)**되도록 했고, 소규모 프로젝트에서 비용 효율이 좋습니다.

---

## 📣 주요 발표 내용
- 기존 영어 학습 앱은 대부분 기초부터 가르쳐서, 일상 대화·문제 해결·브레인스토밍 같은 **자유 대화형 튜터**를 직접 만들었습니다.
- 대화 중 언어 사용·문법·개선점을 요청하면 모델이 사용자가 놓치는 부분을 짚어 줍니다.
- **Cloud Run**: 시작이 간편하고, 트래픽이 없으면 0까지 줄어들며, 수요에 따라 거의 무제한으로 늘어납니다.
- Cloud Run은 **Agent Platform** 등 Google Cloud 서비스와 바로 연동됩니다.
- Gemini API 키는 **Secret Manager**에 보관해 코드에 하드코딩하지 않았습니다.
- 데이터 저장은 **Firestore**, 사용자 인증은 **Firebase Authentication**(Google 계정 로그인)을 썼습니다.
- `Dockerfile`을 **Cloud Build**로 보내면 컨테이너를 빌드해 **Artifact Registry**에 저장하고 Cloud Run에 배포합니다.

---

## 💡 개발자 포인트
- 사용자가 적은 사이드 프로젝트는 scale-to-zero를 지원하는 **Cloud Run**을 쓰면 유휴 시간에 컴퓨팅 비용이 들지 않습니다.
- API 키 같은 민감 정보는 **Secret Manager**와 Cloud Run 연동으로 주입하는 것이 좋습니다.
> ⚠️ API 키를 애플리케이션 코드에 직접 넣지 마세요. Secret Manager로 분리해야 합니다.
- 인증은 **Firebase Authentication**을 쓰면 클릭 몇 번으로 Google 로그인을 붙일 수 있어 개발 시간이 줄어듭니다.
- 빌드·저장·배포 파이프라인(Cloud Build → Artifact Registry → Cloud Run)은 `gcloud` 명령 3~4개로 끝납니다.
- 실시간 음성·대화형 AI 앱이라면 **Gemini Live API**를 검토해 볼 만합니다.

---

## 📅 버전 / 출시 일정
해당 없음


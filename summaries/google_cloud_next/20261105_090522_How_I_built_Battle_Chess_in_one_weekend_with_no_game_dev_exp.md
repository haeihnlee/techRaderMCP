# How I built Battle Chess in one weekend… with no game dev experience

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=z5gmcYsdfyo
- **요약 일시**: 2026-11-05 09:05:22

---

## 🔑 핵심 요약
- 게임·클라우드 개발 경험이 없는 25년차 **네트워크 엔지니어**가 주말 며칠 만에 1988년 고전 게임 **Battle Chess**를 웹 게임으로 다시 만든 사례
- `Gemini CLI` + **Nano Banana**(이미지) + **Veo 3**(영상)로 코드·말 그래픽·애니메이션을 모두 생성 (Python 기반 **바이브 코딩**)
- 로컬에서만 돌던 게임을 **Google Cloud Run**과 GitHub 저장소를 연결해 클릭 몇 번으로 웹에 배포

---

## 📣 주요 발표 내용
- 발표자 배경: 캐나다 의회·Cisco 등에서 약 25년 IT 경력, 네트워크 자동화용 Python만 다룰 줄 알고 게임/클라우드 개발은 초보
- 개발 환경: **VS Code** 하단 터미널에 `Gemini CLI`를 붙여 Gemini 모델로 전체 코드 생성
- 에셋 생성: IDE 안에서 **Nano Banana**·**Veo** API에 프롬프트를 보내고, 체스 말 이미지와 캡처 애니메이션 결과를 바로 받아서 확인
- 배포 문제 해결: 로컬호스트에서 AI 대전까지 됐지만 웹 공개가 가장 큰 벽이었음 → **Cloud Run**을 GitHub 저장소에 연결(발표자 기억으로는 "클릭 세 번 정도")해 따로 공부하지 않고 배포
- 오픈소스 공개: **Battle Chess 9000** 저장소를 clone해서 Nano Banana/Veo로 나만의 **테마 파일**을 만들어 PR을 보내면 병합해 준다고 안내

---

## 💡 개발자 포인트
- 생성형 AI 도구 체인(`Gemini CLI` + 이미지/영상 생성 API)을 **IDE 하나에 모으면** 코드와 에셋을 같은 루프 안에서 빠르게 반복 개선할 수 있음
- 클라우드 경험이 없어도 **Cloud Run + GitHub 연동**(소스 기반 배포)으로 로컬 Python 앱을 바로 공개 서비스로 올릴 수 있음
- 도메인 지식이 없는 분야도 AI를 "전문가처럼" 다루면 프로토타입까지 갈 수 있다는 메시지
- 디버깅 마인드셋: "가장 좋은 에러 메시지는 **새로운** 에러 메시지" — 에러가 바뀌었다면 진전이 있다는 뜻

> 주의: 자막이 자동 생성/번역본이라 "Vyo", "VO"로 표기된 부분은 **Veo**로 해석함. 정확한 저장소 URL과 배포 설정은 발표 영상에 나오지 않음

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
| --- | --- |
| 원작 Battle Chess | 1988년 (발표자가 어린 시절 플레이) |
| 개발 기간 | 주말 며칠 |
| 사용 모델/도구 | `Gemini CLI`, Nano Banana, Veo 3, Google Cloud Run |


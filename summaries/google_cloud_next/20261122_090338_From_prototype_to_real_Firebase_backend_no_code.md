# From prototype to real Firebase backend (no code)

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=0aUIWT6W_oU
- **요약 일시**: 2026-11-22 09:03:38

---

## 🔑 핵심 요약
- **Build It** 시리즈 에피소드로, **Google Antigravity** 안의 **Gemini 에이전트**가 직접 코드를 짜지 않고 AI 개인 트레이너 앱에 **Firebase 백엔드(Firestore + Authentication)**를 붙이는 과정을 보여줌
- Gemini는 약 **14분** 동안 Firebase 통합 코드를 작성하고 검증했으며, 콘솔 설정은 개발자에게 **한 번에 한 단계씩** 안내함
- 마지막에 Firestore에 운동 **41개**를 시드하고, Google 로그인부터 주간 운동 계획 저장까지 실제로 동작하는 것을 확인함

---

## 📣 주요 발표 내용
- **사전 점검 프롬프트**: 작업 전에 Gemini에게 "Firestore 연동에 필요한 skills나 MCP 서버가 있는가"를 물어 에이전트용 규칙·가이드라인을 미리 갖춤
- **1단계 – 프로젝트 생성**: Firebase 콘솔에서 프로젝트 생성 (Gemini 활성화, Google Analytics는 사용 안 함)
- **2단계 – 웹 앱 등록**: 웹 앱을 등록해 config 키를 받고, Gemini가 준 템플릿에 맞춰 로컬 env 파일에 입력 (Firebase Hosting은 설정 안 함)
- **3단계 – 인증 제공업체 활성화**: `Authentication`에서 **이메일/비밀번호**와 **Google** 로그인을 켬
- **4단계 – Firestore 생성**: Standard 에디션, 기본 DB ID와 기본 위치, **프로덕션 모드**로 생성 (요금제 업그레이드는 필요 없었음)
- **5단계 – 보안 규칙 게시**: Gemini가 만든 **Firestore Security Rules**를 `Rules` 탭에 붙여 넣고 게시 (서버 측 접근 제어)
- **6단계 – 서비스 계정 키 발급**: 프로젝트 설정 → 서비스 계정 → **Firebase Admin SDK (Node.js)** → "새 비공개 키 생성"으로 JSON을 받아 env 파일에 넣음
- **데이터 시드**: Gemini가 스크립트 실행 권한을 요청한 뒤 `exercises` 컬렉션에 운동 41개(카테고리, 자세 팁, 지침 포함)를 시드
- **최종 검증**: Gemini가 서버 로그로 **ID 토큰 검증 → 세션 인증 → 프로필의 Firestore 연결**을 확인한 뒤 Git에 커밋해 체크포인트를 남김
- **다음 에피소드**: 앱 배포

---

## 💡 개발자 포인트
- 에이전트에게 "**한 단계씩만 알려줘, 끝나면 알려줄게**"라고 요청하면 콘솔 작업을 순서대로 확실하게 진행할 수 있음
- 에이전트가 안내하는 콘솔 메뉴 위치가 실제 UI와 다를 수 있음 (예: `Build`가 아니라 `Security > Authentication`, `Database & Storage > Firestore`에 있었음)
- Firestore는 **프로덕션 모드**로 시작하고, 보안 규칙을 바로 게시해 허가된 사용자만 읽고 쓰게 하는 흐름을 권장함
- 서비스 계정 JSON은 내용을 통째로 env 파일에 붙여 넣거나 **파일 경로만 지정**하는 두 가지 방법 중 고를 수 있음
- 결과 데이터 구조: `exercises` 컬렉션과 `users` 컬렉션(사용자별 프로필 문서, 주간 채팅, 주간 계획)
- 슬래시 명령어로 "이 단계가 무슨 일을 하는지" 설명을 요청해 이해한 뒤 진행할 수 있음

> ⚠️ 서비스 계정 비공개 키(JSON)는 서버 전체 권한을 가진 자격 증명입니다. env 파일이 Git에 커밋되지 않도록 `.gitignore`를 꼭 확인하세요.

> ⚠️ 에이전트가 프로젝트가 이미 있다고 가정하고 코드를 먼저 작성할 수 있습니다. 실제 자격 증명을 넣기 전까지는 연결이 검증되지 않은 상태입니다.

---

## 📅 버전 / 출시 일정
| 항목 | 내용 |
|---|---|
| Gemini Firebase 통합 작업 시간 | 약 14분 |
| 시드한 운동 데이터 | 41개 (`exercises` 컬렉션) |
| Firestore 에디션 | Standard, 프로덕션 모드 |
| 다음 에피소드 | 배포 (날짜 미정) |


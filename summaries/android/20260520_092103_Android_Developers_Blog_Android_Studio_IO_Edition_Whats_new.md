# Android Developers Blog: Android Studio I/O Edition: What's new in Android Developer tools

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/whats-new-android-developer-tools.html
- **요약 일시**: 2026-05-20 09:21:03

---

## 🔑 핵심 요약
- Android Studio가 **Agentic 개발 시대**로 전환 — 단순 AI 어시스턴트를 넘어 자율 에이전트가 코드 작성·테스트·디버깅까지 수행
- **Agent Skills**, **Android CLI**, **병렬 대화**, **Firebase 풀스택 통합** 등 에이전트 워크플로우를 위한 신기능 대거 추가
- `Gemma 4` 로컬 모델 IDE 내장 다운로드 지원, `Gemini`/`GPT`/`Claude` 등 **BYOM**(Bring Your Own Model) 가능

---

## 📣 주요 발표 내용

### 🤖 1. Agent에게 맡기기 (Let your agent handle it)
- **Agent Skills**: LLM을 특정 워크플로우·도메인 지식에 그라운딩하는 모듈형 명령 세트. 최신 Canary 빌드에 Android/Firebase 공식 skill 번들 포함
  - XML→Compose 마이그레이션, Edge-to-edge, **Navigation 3**, Android XR(`Glimmer` Compose) 등 커버
- **Firebase 풀스택 빌드**: Agent Mode에서 `Auth`, `Firestore` 등 Firebase 서비스를 직접 활성화/구성
- **병렬 대화(Parallel conversations)**: 한 세션에서 테스트 실행, 다른 세션에서 신규 기능 플래닝, 또 다른 세션에서 문서 작성 동시 진행
- **New Project Agent 강화**: 멀티스텝 실행 플랜 + 자율 "generation loop"로 빌드 에러 자가 수정, 대형 화면(태블릿/폴더블/노트북) 스캐폴딩 지원

---

### 🌐 2. 어디서든, 어떤 AI 제공자든 (Any AI provider, anywhere)
- **Google AI Studio**에서 풀 Android 앱 개발 가능 — 내장 에뮬레이터 프리뷰, ADB over USB로 실기기 배포, **Google Play 내부 테스트 트랙 직접 게시**, ZIP export로 Android Studio 이관
- **Android CLI**: 어떤 에이전트/LLM/툴에서도 Android 앱 빌드 가능. Android Knowledge Base + Skills 그라운딩으로 토큰 사용량 절감. **Google Antigravity 2.0** 공식 지원
- **Google AI Pro/Ultra 플랜** 연동 — Android Studio의 Gemini에서 전용 캐패시티·높은 레이트 리밋 사용
- **Gemma 4**: SOTA 로컬 모델, IDE에서 직접 다운로드·실행 (외부 서버 불필요). 프라이버시·오프라인·쿼터 이슈에 적합
- **BYOM**: `Gemini`, `GPT`, `Claude`, `Gemma 4` 등 자유롭게 선택
- **Android Bench**: 오픈 모델까지 평가 리더보드에 추가, 장시간(여러 날 소요) 태스크 벤치마크 도입 예정

---

### ⚡ 3. 성능 & 품질 개선
- **Android Emulator 네트워킹 스택** 개편 — 동일 호스트 내 가상 디바이스 간 **zero-config P2P 연결**, 포트 포워딩 불필요 (로컬 멀티플레이, 파일 공유, 컴패니언 앱 테스트)
- **ADB Wi-Fi 2.0** (`Platform Tools v37` + Android 17): 네트워크 전환·머신 셧다운 후에도 연결 유지, Device Manager에 자동 노출
- **Google Play 게시 통합**: Signed App Bundle 생성 마지막 단계에서 "Publish for Testing" 옵션으로 Play Console 테스트 트랙 직접 업로드
- **Android Developer Verification**: 서명 번들/APK 생성 시 앱 등록 상태 표시
- **LeakCanary Profiler Task**: 메모리 누수 트레이스를 모바일 기기가 아닌 데스크탑 IDE에서 분석, "Go to declaration"으로 코드베이스 즉시 매핑

---

## 💡 개발자 포인트

> ⚠️ **Breaking / 필수 대응**: **Android Developer Verification** 요구사항이 **2026년 9월**부터 인증된 Android 기기에 적용됩니다. Android Studio의 등록 상태 표시로 사전에 점검하세요.

- **Agent Skills 도입 권장**: 팀의 아키텍처 패턴·라이브러리 워크플로우를 skill로 정의하면, LLM이 일관된 best practice를 따르도록 강제 가능
- **`Android CLI`는 IDE 비종속**: Cursor/Antigravity/터미널 등 본인의 에이전트 환경에서도 Android 전용 지식과 툴을 활용 가능 — 토큰 효율도 ↑
- **로컬 vs 원격 모델 선택**: 데이터 프라이버시·오프라인·쿼터 제약 시 `Gemma 4` 로컬 모델이 유효한 옵션. IDE에서 바로 다운로드 가능해 진입장벽 ↓
- **병렬 에이전트 활용**: 긴 빌드/테스트 대기 시간을 신규 기능 플래닝·문서화에 동시 활용해 생산성 극대화
- **풀스택 개발 단축**: Firebase Agent Skills로 백엔드 설정까지 IDE 안에서 처리 → 단일 프롬프트로 풀스택 앱 구축 가능
- **멀티 디바이스 테스트 단순화**: Emulator P2P로 멀티플레이·컴패니언 앱 시나리오를 별도 설정 없이 검증

---

## 📅 버전 / 출시 일정

| 항목 | 버전 / 일정 |
|---|---|
| 블로그 게시일 | 2026-05-19 |
| Android Studio | **Quail** (Canary 빌드에서 신기능 제공) |
| Android Platform Tools | **v37** (ADB Wi-Fi 2.0) |
| Android OS | **Android 17** (ADB Wi-Fi 2.0 안정 동작 대상) |
| Google Antigravity | **2.0** (Android CLI 공식 지원) |
| 로컬 모델 | **Gemma 4** |
| Android Bench 결과 기준일 | 2026-05-18 |
| Android Developer Verification 시행 | **2026년 9월** (인증 Android 기기 대상) |


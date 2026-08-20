# Why you should be building with Full-stack Dart with Serverpod's Viktor Lidholt

- **컨퍼런스**: Flutter
- **출처**: https://www.youtube.com/watch?v=ZcXFRzilDxk
- **요약 일시**: 2026-08-20 09:04:56

---

## 🔑 핵심 요약
- **Serverpod 4.0**이 2026년 9월 GA 예정이며, Flutter Hot Reload 경험을 백엔드 전체 스택으로 확장
- 풀스택 **Hot Reload** 지원: 서버 코드, DB 마이그레이션, Flutter 클라이언트 코드를 동시에 리로드
- **MCP 서버** 통합으로 AI 에이전트가 로그 조회·DB 마이그레이션·Hot Restart까지 자동화 수행 가능

---

## 📣 주요 발표 내용
- **Full-stack Hot Reload**: 서버 실행 중 `database migration` 적용, 데이터 모델 갱신, Flutter 앱 패치 동시 진행
- **MCP 서버 추가**: AI 에이전트가 `read_logs`, `read_fatal_logs`, `read_support_logs`, `hot_restart` 등의 툴을 통해 개발 루프 자동화
- **AI Skills 제공**: Anthropic, Cursor, Claude Code 등 다양한 에이전트 환경에서 MCP 서버를 즉시 사용 가능하게 하는 사전 정의된 스킬 셋
- **오프라인 퍼스트 동기화**: 18개월 개발 끝에 `SQLite` 기반 클라이언트와 서버 DB를 타입 세이프하게 동기화 (Dart ORM 공유)
- **벡터 DB 내장**: 시맨틱 검색·RAG 구현을 위한 벡터 데이터베이스 API 기본 제공
- **Serverpod Cloud**: `serverpod_cloud launch` 명령 한 줄로 3분 내 DB·로드밸런서·CDN 포함 전체 인프라 배포

---

## 💡 개발자 포인트
- **풀스택 Dart 생산성**: 서버와 Flutter 앱이 동일한 타입 세이프 ORM을 공유하여 데이터 모델 불일치 없음
- `serverpod_cloud launch` 한 번으로 프로덕션 배포 가능 (멀티 리전은 미지원, 로드맵에 있음)

> **Breaking/주의**: Serverpod 4는 현재 **베타** 상태. GA는 2026년 9월 예정이므로 프로덕션 도입 전 안정성 확인 필요.

- Dart 생태계의 클라우드 SDK 부족 문제는 AI 에이전트를 통한 코드 생성으로 점차 해소 중
- `Llama Dart`, `Flutter Gemma` 등 온디바이스 LLM 지원도 커뮤니티 기여로 성장 중

---

## 📅 버전 / 출시 일정

| 버전 | 상태 | 예정일 |
|------|------|--------|
| Serverpod 4.0 | Beta | 현재 진행 중 |
| Serverpod 4.0 GA | 정식 출시 | 2026년 9월 |

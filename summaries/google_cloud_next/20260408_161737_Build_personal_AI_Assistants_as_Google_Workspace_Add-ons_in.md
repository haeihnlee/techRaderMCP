# Build personal AI Assistants as Google Workspace Add-ons, in Gmail, Calendar, etc

- **컨퍼런스**: Google Cloud Next
- **출처**: https://www.youtube.com/watch?v=h7nYnzGQp9k
- **요약 일시**: 2026-04-08 16:17:37

---

## 핵심 요약 (3줄)
- Google Workspace Add-on 하나로 Gmail, Calendar, Drive, Chat 등 주요 Workspace 앱 전체에서 동작하는 AI 에이전트를 구축할 수 있다
- Cloud Run으로 HTTP 엔드포인트를 배포하고, Vertex AI Agent Engine(ADK)과 연동하는 아키텍처로 구현한다
- 동일한 에이전트가 컨텍스트를 유지한 채 Gmail 사이드바와 Google Chat 모두에서 작동한다

## 주요 발표 내용
- **Workspace Add-on의 통합 범위 확장**: Chat, Gmail, Calendar, Drive, Docs 등 대부분의 Workspace 앱에서 단일 Add-on 동작 지원
- **AI 에이전트 연동**: Google ADK(Agent Development Kit) + Vertex AI Agent Engine을 백엔드로 활용하는 패턴 시연
- **멀티모달 지원**: Gemini 기반으로 텍스트뿐 아니라 이미지 포함 메시지 처리 가능
- **Google Search 그라운딩**: 에이전트가 실시간 검색 결과를 참조하고 출처 링크를 함께 제공
- **컨텍스트 유지**: Gmail에서 시작한 대화를 Chat으로 이어가도 동일 에이전트가 이전 대화 맥락 기억
- **활용 사례 두 가지 카테고리**:
  - **2P (자체 구축)**: 내부 인시던트 조사 보조, 고객 이메일 대응 자동화 등
  - **3P (외부 배포)**: ServiceNow 가상 에이전트, Figma Chat 앱 알림/댓글 관리 등
- **관리자 일괄 배포**: 도메인 관리자가 조직 전체에 Add-on 자동 설치 가능

## 개발자에게 중요한 포인트

### 아키텍처 구조
```
User (Chat/Gmail) → Google Workspace Add-on
→ Cloud Run (HTTP Endpoint)
→ Vertex AI Agent Engine (ADK App)
```

### 구현 핵심 사항
- **트리거 분기 처리**: 이벤트 페이로드에 `chat` 프로퍼티 존재 여부로 Chat/Gmail 이벤트 구분
- **Workspace 컨텍스트 주입**: 사용자가 선택한 이메일의 제목/본문을 `extract_email_contents()`로 추출하여 에이전트 프롬프트에 추가
- **Chat API 설정**: Cloud Console에서 Google Chat API 활성화 후 앱 이름, 아바타, 설명, Cloud Run 엔드포인트 URL 등록 필요
- **배포 방식**: Cloud Run으로 서비스 배포 → Cloud Console에서 Add-on 엔드포인트 등록 → 테스트/배포 접근 권한 설정
- **배포 범위 선택**:
  - 내부 테스트: Cloud Console에서 접근 권한 설정
  - 조직 내부 배포: 내부 마켓플레이스 퍼블리싱
  - 외부 공개: 공개 마켓플레이스 퍼블리싱 프로세스 진행
- **에이전트 플랫폼 유연성**: Vertex AI 외에도 다른 에이전트 플랫폼과 연동 가능
- 코드 샘플 및 튜토리얼이 공개되어 있어 참고 가능 (영상 설명란 링크)

## 출시 일정 / 버전 정보
- 현재 이미 사용 가능한 기능으로, 특정 신규 출시 일정은 별도 언급 없음
- 다만 비자 관련 에이전트 응답 중 **2026년 말부터 특정 입국 허가 요건이 생길 예정**이라는 실사용 예시 언급 (기능 출시와 무관한 내용)

# Android Developers Blog: Media3 1.11 - What's new?

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/08/media3-1-11-whats-new.html
- **요약 일시**: 2026-08-12 09:04:17

---

## 🔑 핵심 요약
- **Media3 1.11** 출시 — Jetpack Compose UI 모듈 대폭 확장, 커스터마이즈 가능한 Player 레이아웃 및 제스처 지원 추가
- 숏폼 영상 피드를 위한 `PlayerPool` + `rememberPooledPlayer` 도입으로 다중 플레이어 관리 자동화
- **MediaSession 보안 강화** — `onConnect`/`onConnectAsync` 미구현 시 비신뢰 컨트롤러에 세션 데이터 기본 차단

---

## 📣 주요 발표 내용

**Compose UI 확장**
- `Player` Composable에 `topControls`, `centerControls`, `bottomControls`, `errorOverlay` 슬롯 추가 및 `PlayerDefaults`로 기본 UI 제공
- `FocusRequester` 통합으로 Android TV·폴더블·데스크톱 D-pad/키보드 내비게이션 지원
- `PlaybackSpeedState`에 빠른 감기/슬로우모션 API 추가 — 롱프레스·더블탭 제스처 연동
- `MiniController` Composable 추가 — 제목·아티스트·아트워크·진행바 + 재생 컨트롤, Material3 Dynamic Color 지원
- 새 state holder: `rememberCurrentMediaItemState`, `rememberPlaylistState`, `rememberErrorState`

**PlayerPool — 숏폼 영상 프리로딩**
- `PlayerPool`(`common-ktx`)과 `rememberPooledPlayer`(`ui-compose`)로 ExoPlayer 인스턴스 재사용·프리로딩 자동화
- `ShortFormPlayerScreen` 데모로 수직 스크롤 피드 구현 예제 제공

**Cast 통합 현대화**
- `CastParams.Builder`로 Cast 확장 프로그래밍 구성 가능
- `setShowSystemOutputSwitcherOnCastButtonClick(true)` 설정 시 OS 레벨 SystemUI Output Switcher 연동
- Compose용 `MediaRouteButton` 추가 — Cast 상태 자동 구독

**코어 재생 개선**
- **Eclipsa Video HAGC** (ST 2094-50) 동적 HDR 메타데이터 지원 (API 37+), 하위 기기는 표준 HDR 폴백
- 새 `media3-datasource-ktor` 모듈 — Kotlin 코루틴 친화적 `KtorDataSource` 제공
- `MediaSession.Callback.onConnectAsync()` 추가 — 비동기 컨트롤러 인증 처리 지원

**Muxer & 컨테이너 파싱**
- `OggMuxer` (OPUS/VORBIS → `.ogg`) 및 `WavMuxer` (비압축·부동소수점 PCM `.wav`) 신규 추가
- `Mp4Muxer.addTrackReference`로 보조 트랙 연결 지원
- MP4·Matroska 챕터 메타데이터 추출 지원 (오디오북·팟캐스트 내비게이션)

---

## 💡 개발자 포인트

> **Breaking Change (보안):** `MediaSession.Callback`에서 `onConnect` 또는 `onConnectAsync`를 재정의하지 않은 앱은 이제 비신뢰(비시스템·알림 접근 없는) 컨트롤러에게 세션 데이터가 기본 차단됩니다. 기존 동작을 유지하려면 명시적으로 콜백을 구현해야 합니다.

- `PlayerPool` 활용 시 `rememberPooledPlayer`만으로 플레이어 풀 관리 — 직접 `ExoPlayer` 생명주기 관리 불필요
- Eclipsa Video HAGC는 **API 37+** 기기에서만 동작; 하위 기기는 자동 폴백되므로 별도 분기 처리 불필요
- `media3-datasource-ktor`는 기존 OkHttp/Cronet 모듈의 Kotlin-first 대안 — 코루틴 기반 네트워크 스택 선호 프로젝트에 적합
- `onConnectAsync`는 인증 처리를 비동기화하면서도 즉시 결과가 필요하면 `Futures.immediateFuture(ConnectionResult)` 사용 가능

---

## 📅 버전 / 출시 일정

| 항목 | 내용 |
|------|------|
| 릴리즈 버전 | Media3 **1.11** |
| 발표일 | 2026년 8월 11일 |
| Eclipsa Video HAGC 최소 API | API 37+ |
| 전체 릴리즈 노트 | [release notes](https://github.com/androidx/media/releases)

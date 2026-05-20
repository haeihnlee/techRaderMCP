# Android Developers Blog:  Increasing app discovery and engagement on Google TV

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/increase-google-tv-app-discovery.html
- **요약 일시**: 2026-05-20 09:14:02

---

## 🔑 핵심 요약
- **Google TV/Android TV** 월간 활성 디바이스 **3억대 돌파** — 거실은 더 이상 부가 채널이 아닌 독립적 성장 플랫폼
- **Gemini** 음성 어시스턴트가 앱 메타데이터를 활용해 콘텐츠 디스커버리 엔진 역할 수행
- **포인터 리모컨(Pointer Remote)** 시대 대비 필요 — `hover`, `scroll`, `cursor click` 지원 및 `AndroidManifest.xml` 신규 메타데이터 선언 필수
- 기존 **Watch Next API**는 2027년 하반기 지원 종료 → **Engage SDK**로 마이그레이션 필요

---

## 📣 주요 발표 내용
- **Gemini on TV 강화**: 시각·영상·텍스트가 결합된 응답으로 사용자 검색 의도에 맞춰 콘텐츠 노출, 스트리밍 파트너 앱 메타데이터에서 콘텐츠를 끌어옴
- **포인터 리모컨 지원 가이드**: 모션 컨트롤 입력을 위한 3단계 준비 — UI 라이브러리 적응 → 마우스로 테스트 → Google Play에 선언
- **`AndroidManifest.xml` 신규 태그**: `android.software.leanback.supports_touch` 메타데이터로 포인터 리모컨 지원 여부 선언
- **Jetpack Compose 권장**: 멀티 모달(hover/scroll/click) 입력을 코어 컴포넌트가 기본 지원 → 코드 재사용성·유지보수 비용 절감
- **Engage SDK (구 Video Discovery API)**: 3가지 핵심 기능 제공
  - `Resumption` — 'Continue Watching' 행에 일시정지된 영상 노출
  - `Entitlements` — 앱 콘텐츠와 사용자 구독 자격 자동 매칭
  - `Recommendations` — 시청 기록 기반 개인화 추천

---

## 💡 개발자 포인트
- **포커스 상태와 호버 상태는 다르다**: 모든 포커서블 요소(버튼, 포스터, 토글)에 별도의 **hover 시각 피드백** 추가 필요. 포커스보다 미묘하지만 사용자 인지에 필수
- **거리 차이 고려한 디자인**: 마우스는 정밀하지만 포인터 리모컨은 10피트 거리에서 거친 제스처 → **hover 타겟을 크게** 설계해야 함
- **클릭 동작 재정의**: 기존 D-pad OKAY 버튼 클릭만 처리하던 앱은 **D-pad 포커스와 무관한 호버 클릭** 처리 추가 필요 (마우스 클릭과 유사)
- **AndroidManifest 선언 예시**:
  ```xml
  <uses-feature android:name="android.software.leanback" android:required="true|false" />
  <uses-feature android:name="android.hardware.touchscreen" android:required="false" />
  <meta-data android:name="android.software.leanback.supports_touch" android:value="true|false"/>
  ```
- **즉시 테스트 가능**: USB/Bluetooth 마우스를 Google TV에 연결하면 hover/scroll/click 동작 검증 가능

> ⚠️ **Breaking Change**: 레거시 **Watch Next API**는 2027년 하반기 지원 종료 예정. 'Continue Watching' 기능이 깨지지 않으려면 지금부터 **Engage SDK** 온보딩 시작 필요 (`goo.gle/engage-tv`)

---

## 📅 버전 / 출시 일정

| 항목 | 일정 | 비고 |
|------|------|------|
| Google TV/Android TV MAU | 현재 | 3억대 이상 |
| Watch Next API 지원 종료 | **2027년 하반기** | Engage SDK로 마이그레이션 필요 |
| Gemini on TV | 작년 출시 후 지속 개선 | 응답 품질 강화 |
| 발표 출처 | Google I/O 2026 | `io.google` 참조 |


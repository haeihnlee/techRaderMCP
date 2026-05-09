# Android Developers Blog: Gratitude saw 25% higher retention for widget users

- **컨퍼런스**: Android
- **출처**: https://android-developers.googleblog.com/2026/05/how-gratitude-widgets-boosted-user-retention-25-percent.html
- **요약 일시**: 2026-05-09 09:05:04

---

## 🔑 핵심 요약
- **Gratitude 앱**(누적 600만 다운로드)이 위젯을 도입해 위젯 사용자 **리텐션 25% 상승**, 주간 위젯 저널 입력 약 1,000건 기록
- 기존 **XML 기반 RemoteViews** 위젯을 **Jetpack Glance**로 마이그레이션, 개발 시간 약 **50% 단축**
- 앱 내부에서 **in-app widget pinning** (`requestPinGlanceAppWidget`)을 활용해 위젯 발견성 강화, 전체 DAU의 **10%가 위젯 채택**

---

## 📣 주요 발표 내용
- Gratitude는 마음챙김 저널 앱으로, 홈 스크린 위젯에 **저널 프롬프트, 어퍼메이션, 비전 보드 이미지, 메트릭**을 노출해 사용자 진입 장벽을 낮춤
- 기존 **XML RemoteViews** 구현은 Material 3 디자인 시스템과 정렬이 어려웠고, 시각 변경마다 수동 XML 작업 필요
- **Jetpack Glance**(Compose 기반 선언형 프레임워크)로 마이그레이션해 **dynamic colors**, 유연한 **resizing**, 확장된 configuration 옵션 구현
- **Generated Widget Previews**를 적용해 사용자가 개인화된 미리보기 확인 가능
- 위젯 패키지 리팩토링 시 receiver 경로가 변경되어 위젯이 삭제되는 이슈 발생 → 저장된 사용자 플래그로 위젯 사용자를 식별하고 `requestPinGlanceAppWidget`로 재설치 유도

---

## 💡 개발자 포인트
- **`AppWidgetProvider` → `GlanceAppWidgetReceiver` 마이그레이션 시**: Android Manifest의 클래스명·패키지명을 동일하게 유지해야 기존 위젯 설치 보존
  > 클래스명/패키지를 변경할 수밖에 없다면 in-app pinning으로 사용자에게 위젯 복구를 유도하라
- Generated Previews는 배터리 보호를 위해 **rate limit** 적용 → 테스트 시 다음 adb 명령으로 우회:
  ```
  adb shell device_config put systemui generated_preview_api_reset_interval_ms 0
  ```
- Glance는 기존 Compose 컴포넌트 재사용·자연스러운 위젯 레이아웃 표현·빠른 UI 이터레이션이 가능
- 다양한 **OEM 런처에서의 레이아웃 일관성 테스트** 필수
- 위젯 디자인은 [Widgets on Android 디자인 페이지](https://developer.android.com/design/ui/widget) 및 **canonical widget layouts** 참고 권장

---

## 📅 버전 / 출시 일정
| 항목 | 값 |
|---|---|
| 게시일 | 2026년 5월 8일 |
| Gratitude 다운로드 | 600만+ |
| 5성 평점 | 15만+ |
| 위젯 마이그레이션 기간 | 1개월 미만 |
| 개발 시간 절감 | 약 50% |
| 위젯 사용자 리텐션 증가 | 25% |
| 위젯 채택 DAU 비중 | 10% |

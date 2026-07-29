"""server.py 회귀 테스트.

표준 라이브러리만 사용한다 — 공유받은 사람이 pip install 없이 돌릴 수 있어야 한다.

실행:
    python3 -m unittest test_server -v
    또는  .venv/bin/python -m unittest test_server

네트워크에 접속하지 않는다. 실제 URL 대신 관측된 응답 본문을 상수로 고정했다.
"""
import unittest

from server import _MIN_CONTENT_CHARS, _detect_unusable_content


# 2026-07-29 platform.claude.com 문서에서 실제로 관측된 응답.
# 131자, 12줄 전부 동일. 이것이 성공으로 통과해 빈 요약이 저장·푸시됐다.
OBSERVED_JS_SKELETON = "Loading...\n" * 12

# 정상 본문의 형태: 길이가 충분하고 줄이 서로 다르다.
# (실측 비교군은 5,225자 / 고유줄 91% 였다)
VALID_ARTICLE = "\n".join(
    f"문단 {i}: 이 줄에는 실제 내용이 담겨 있습니다." for i in range(100)
)

# YouTube 자막이 없을 때 영상 설명만으로 요약한 정상 사례.
# summaries/ 에 실제로 존재하므로("자막이 제공되지 않아 … 영상 설명 기준으로 정리")
# 차단되면 오탐이다.
#
# 길이는 실측 표본(영상 5건)에서 가져왔다: description 은 330~500자이고
# server.py 가 500자로 절단한다. 표본 중 345자 영상은 웹페이지 하한(400자)에서
# 차단되고 YouTube 하한(120자)에서 통과했다 — 하한 분리가 실제로 필요한 근거다.
YOUTUBE_DESCRIPTION_ONLY = "[자막 없음] 영상 설명:\n" + (
    "이번 세션에서는 멀티 에이전트 AI 로 SAP 주문·수금(order-to-cash) 프로세스를 "
    "자동화하는 방법을 다룹니다. Google Agent Development Kit 으로 주문 검증, "
    "재고 확인, 인보이스 발행을 담당하는 에이전트를 각각 구성하고, 이들이 "
    "서로 상태를 주고받으며 사람 개입 없이 처리하는 흐름을 시연합니다. "
    "실제 도입 사례와 비용 절감 수치도 함께 공유합니다. "
    "예제 코드와 슬라이드는 설명란 링크에서 받을 수 있습니다."
)
YOUTUBE_MIN_CHARS = 120


class DetectUnusableContentTest(unittest.TestCase):
    """차단해야 하는 본문 — 각 신호가 독립적으로 동작하는지 확인한다."""

    def assertBlocked(self, content, expected_substring, min_chars=None):
        kwargs = {} if min_chars is None else {"min_chars": min_chars}
        reason = _detect_unusable_content(content, **kwargs)
        self.assertIsNotNone(reason, "차단돼야 하는데 통과했다")
        self.assertIn(expected_substring, reason)

    def assertAllowed(self, content, min_chars=None):
        kwargs = {} if min_chars is None else {"min_chars": min_chars}
        reason = _detect_unusable_content(content, **kwargs)
        self.assertIsNone(reason, f"통과돼야 하는데 차단됐다: {reason}")

    # ── 신호 1: 자리표시자 문구 ──────────────────────────────────────────

    def test_observed_js_skeleton_is_blocked(self):
        """실제 발생한 회귀 케이스. 이 테스트가 깨지면 빈 요약이 다시 저장된다."""
        self.assertBlocked(OBSERVED_JS_SKELETON, "자리표시자")

    def test_javascript_required_notice_is_blocked(self):
        self.assertBlocked("Please enable JavaScript to continue", "자리표시자")

    def test_cloudflare_interstitial_is_blocked(self):
        self.assertBlocked(
            "Just a moment...\nChecking your browser before accessing",
            "자리표시자",
        )

    def test_bot_block_page_is_blocked(self):
        self.assertBlocked("Access Denied\n403 Forbidden", "자리표시자")

    def test_korean_placeholder_is_blocked(self):
        self.assertBlocked("로딩 중입니다\n잠시만 기다려 주세요", "자리표시자")

    def test_placeholder_word_inside_real_article_is_allowed(self):
        """오탐 방지: 정상 기사에 'loading' 이 한 줄 섞여도 통과해야 한다.

        전체 줄이 자리표시자일 때만 차단하는 설계를 고정한다.
        """
        content = VALID_ARTICLE + "\nLazy loading 을 적용하면 성능이 개선된다."
        self.assertAllowed(content)

    # ── 신호 2: 동일 문구 반복 ──────────────────────────────────────────

    def test_repeated_lines_are_blocked(self):
        """자리표시자 목록에 없는 문구라도 반복만 하면 실질 내용이 없다."""
        self.assertBlocked("표시할 항목이 없습니다\n" * 8, "동일 문구 반복")

    def test_few_repeated_lines_fall_through_to_length_check(self):
        """줄이 5개 미만이면 반복 검사를 건너뛰고 길이 검사로 넘어간다."""
        reason = _detect_unusable_content("같은 줄\n같은 줄")
        self.assertIsNotNone(reason)
        self.assertIn("너무 짧음", reason)

    # ── 신호 3: 길이 하한 ───────────────────────────────────────────────

    def test_short_content_is_blocked(self):
        self.assertBlocked("가" * 300, "너무 짧음")

    def test_length_boundary(self):
        """하한 경계에서 판정이 뒤집히는 지점을 고정한다."""
        # 줄 반복 검사에 걸리지 않도록 한 줄로 만든다.
        self.assertBlocked("가" * (_MIN_CONTENT_CHARS - 1), "너무 짧음")
        self.assertAllowed("가" * _MIN_CONTENT_CHARS)

    # ── 빈 본문 ────────────────────────────────────────────────────────

    def test_empty_content_is_blocked(self):
        self.assertBlocked("", "비어 있음")

    def test_whitespace_only_is_blocked(self):
        self.assertBlocked("   \n\t\n  ", "비어 있음")

    # ── 정상 본문 ──────────────────────────────────────────────────────

    def test_valid_article_is_allowed(self):
        self.assertAllowed(VALID_ARTICLE)


class YouTubeThresholdTest(unittest.TestCase):
    """YouTube 는 하한이 낮다 — 웹페이지 기준을 적용하면 오탐이 난다."""

    def test_description_only_summary_is_allowed(self):
        """자막 없이 설명문만으로 요약한 정상 사례 (summaries/ 에 실재)."""
        reason = _detect_unusable_content(
            YOUTUBE_DESCRIPTION_ONLY, min_chars=YOUTUBE_MIN_CHARS
        )
        self.assertIsNone(reason, f"정상 사례가 차단됐다: {reason}")

    def test_same_content_would_be_blocked_at_webpage_threshold(self):
        """하한 분리가 실제로 필요한지 확인한다.

        이 테스트가 실패하면 (= 웹페이지 하한에서도 통과하면) YouTube 예외는
        불필요하다는 뜻이므로 호출부를 단순화할 수 있다.
        """
        # 120자 이상 400자 미만 — 두 하한 사이에 놓아야 분기를 확인할 수 있다.
        short_description = (
            "[자막 없음] 영상 설명:\n"
            "이번 세션에서는 Flutter 의 렌더링 파이프라인을 처음부터 훑어보고, "
            "실제 앱에서 프레임 드랍이 발생하는 지점을 프로파일러로 찾는 방법을 "
            "다룹니다. 예제 프로젝트는 설명란 링크에 있습니다."
        )
        self.assertGreaterEqual(len(short_description), YOUTUBE_MIN_CHARS)
        self.assertLess(len(short_description), _MIN_CONTENT_CHARS)
        self.assertIsNone(
            _detect_unusable_content(short_description, min_chars=YOUTUBE_MIN_CHARS)
        )
        self.assertIsNotNone(
            _detect_unusable_content(short_description)  # 기본 400자 하한
        )

    def test_placeholder_still_blocked_at_lower_threshold(self):
        """하한을 낮춰도 자리표시자 검사는 그대로 동작해야 한다."""
        reason = _detect_unusable_content(
            OBSERVED_JS_SKELETON, min_chars=YOUTUBE_MIN_CHARS
        )
        self.assertIsNotNone(reason)


if __name__ == "__main__":
    unittest.main(verbosity=2)

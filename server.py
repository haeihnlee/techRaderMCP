#!/usr/bin/env python3
"""
Conference Summarizer MCP Server
모니터링 대상: Google I/O, Flutter, Apple WWDC, 기타 컨퍼런스
기능: 새 콘텐츠 감지 → 자동 요약 → 파일 저장
"""

import json
import os
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse, parse_qs

import anthropic
import feedparser
import httpx
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from googleapiclient.discovery import build
from mcp.server.fastmcp import FastMCP
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

load_dotenv()

# ── 설정 ──────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
CONFIG_FILE = BASE_DIR / "config.json"
SUMMARIES_DIR = BASE_DIR / "summaries"
LAST_CHECK_FILE = BASE_DIR / ".last_check.json"
SUMMARIES_DIR.mkdir(exist_ok=True)

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

mcp = FastMCP("Conference Summarizer")


# ── 내부 유틸 ─────────────────────────────────────────────────────────────────

def load_config() -> dict:
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    return {"conferences": []}


def save_config(cfg: dict) -> None:
    CONFIG_FILE.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")


def load_last_check() -> dict:
    if LAST_CHECK_FILE.exists():
        return json.loads(LAST_CHECK_FILE.read_text(encoding="utf-8"))
    return {}


def save_last_check(data: dict) -> None:
    LAST_CHECK_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def extract_youtube_id(url: str) -> str | None:
    """YouTube URL에서 video ID 추출"""
    patterns = [
        r"(?:v=|youtu\.be/|/embed/|/v/)([A-Za-z0-9_-]{11})",
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    return None


def get_youtube_transcript(video_id: str) -> str | None:
    """YouTube 자막 가져오기 (한국어 → 영어 순서로 시도)"""
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        for lang in ["ko", "en", "en-US"]:
            try:
                t = transcript_list.find_transcript([lang])
                entries = t.fetch()
                return " ".join(e.text for e in entries)
            except Exception:
                continue
        # 자동 생성 자막 시도
        try:
            t = transcript_list.find_generated_transcript(["en", "ko"])
            entries = t.fetch()
            return " ".join(e.text for e in entries)
        except Exception:
            pass
    except (TranscriptsDisabled, NoTranscriptFound):
        pass
    return None


def fetch_webpage_text(url: str) -> str:
    """웹페이지 본문 텍스트 추출"""
    with httpx.Client(timeout=20, follow_redirects=True) as client:
        headers = {"User-Agent": "Mozilla/5.0 (Conference-MCP-Bot/1.0)"}
        resp = client.get(url, headers=headers)
        resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    # 불필요한 태그 제거
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()
    # 메인 콘텐츠 추출
    main = soup.find("main") or soup.find("article") or soup.find("body")
    if main:
        text = main.get_text(separator="\n", strip=True)
        # 연속 빈 줄 제거
        lines = [l for l in text.splitlines() if l.strip()]
        return "\n".join(lines)
    return soup.get_text(separator="\n", strip=True)


def summarize_with_claude(content: str, title: str, source_url: str, conference_name: str) -> str:
    """Claude API로 컨퍼런스 콘텐츠 요약"""
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    # 토큰 절약을 위해 최대 12000자로 자르기
    content_truncated = content[:12000] + ("..." if len(content) > 12000 else "")

    prompt = f"""다음은 '{conference_name}' 컨퍼런스/발표 콘텐츠입니다.

제목: {title}
출처: {source_url}

콘텐츠:
{content_truncated}

위 내용을 개발자 관점에서 한국어로 요약해주세요. 다음 형식으로 작성하세요:

## 핵심 요약 (3줄)
- (핵심 내용 1)
- (핵심 내용 2)
- (핵심 내용 3)

## 주요 발표 내용
(중요한 발표, 신기능, 변경사항을 bullet point로 정리)

## 개발자에게 중요한 포인트
(실제 개발에 영향을 주는 내용 중심으로 정리)

## 출시 일정 / 버전 정보
(발표된 버전, 출시 예정일 등이 있으면 정리. 없으면 "해당 없음")
"""

    message = client.messages.create(
        model="asf/sonnet-4.6",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def save_summary(conference: str, title: str, url: str, summary: str) -> Path:
    """요약을 마크다운 파일로 저장"""
    conf_dir = SUMMARIES_DIR / conference.replace(" ", "_").lower()
    conf_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_title = re.sub(r'[^\w\s-]', '', title)[:60].strip().replace(" ", "_")
    filename = f"{timestamp}_{safe_title}.md"
    filepath = conf_dir / filename

    content = f"""# {title}

- **컨퍼런스**: {conference}
- **출처**: {url}
- **요약 일시**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

---

{summary}
"""
    filepath.write_text(content, encoding="utf-8")
    return filepath


def get_youtube_video_info(video_id: str) -> dict:
    """YouTube Data API로 영상 메타데이터 가져오기"""
    if not YOUTUBE_API_KEY:
        return {}
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    resp = youtube.videos().list(part="snippet", id=video_id).execute()
    items = resp.get("items", [])
    if not items:
        return {}
    s = items[0]["snippet"]
    return {
        "title": s.get("title", ""),
        "published_at": s.get("publishedAt", ""),
        "channel_title": s.get("channelTitle", ""),
        "description": s.get("description", "")[:500],
    }


def fetch_channel_videos(channel_id: str, published_after: str) -> list[dict]:
    """채널의 최신 영상 목록 조회 (publishedAfter 이후)"""
    if not YOUTUBE_API_KEY:
        return []
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    resp = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        type="video",
        order="date",
        publishedAfter=published_after,
        maxResults=10,
    ).execute()
    results = []
    for item in resp.get("items", []):
        s = item["snippet"]
        results.append({
            "video_id": item["id"]["videoId"],
            "title": s.get("title", ""),
            "published_at": s.get("publishedAt", ""),
            "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            "channel": s.get("channelTitle", ""),
        })
    return results


def fetch_rss_items(feed_url: str, published_after: datetime) -> list[dict]:
    """RSS 피드에서 새 항목 가져오기"""
    feed = feedparser.parse(feed_url)
    results = []
    for entry in feed.entries:
        # 날짜 파싱
        pub = None
        for attr in ("published_parsed", "updated_parsed"):
            if hasattr(entry, attr) and getattr(entry, attr):
                import time
                pub = datetime.fromtimestamp(time.mktime(getattr(entry, attr)), tz=timezone.utc)
                break
        if pub is None or pub < published_after.replace(tzinfo=timezone.utc):
            continue
        results.append({
            "title": entry.get("title", "제목 없음"),
            "url": entry.get("link", ""),
            "published_at": pub.isoformat(),
        })
    return results


# ── MCP 도구들 ────────────────────────────────────────────────────────────────

@mcp.tool()
def check_new_content(days: int = 7, auto_summarize: bool = False) -> str:
    """
    모든 컨퍼런스에서 최근 N일간 새 콘텐츠를 확인합니다.

    Args:
        days: 확인할 기간 (기본값: 7일)
        auto_summarize: True면 발견된 콘텐츠를 자동으로 요약해 파일 저장
    """
    if not YOUTUBE_API_KEY:
        return "오류: YOUTUBE_API_KEY 환경변수가 설정되지 않았습니다."

    cfg = load_config()
    cutoff = datetime.now(tz=timezone.utc) - timedelta(days=days)
    cutoff_iso = cutoff.strftime("%Y-%m-%dT%H:%M:%SZ")

    found_items = []
    errors = []

    for conf in cfg["conferences"]:
        name = conf["name"]

        # YouTube 채널 확인
        for ch_id in conf.get("youtube_channels", []):
            try:
                videos = fetch_channel_videos(ch_id, cutoff_iso)
                for v in videos:
                    found_items.append({**v, "conference": name, "type": "youtube"})
            except Exception as e:
                errors.append(f"{name} 채널({ch_id}): {e}")

        # RSS 피드 확인
        for rss_url in conf.get("rss_feeds", []):
            try:
                items = fetch_rss_items(rss_url, cutoff)
                for item in items:
                    found_items.append({**item, "conference": name, "type": "rss"})
            except Exception as e:
                errors.append(f"{name} RSS({rss_url}): {e}")

    if not found_items and not errors:
        return f"최근 {days}일간 새 콘텐츠가 없습니다."

    # 자동 요약
    saved_files = []
    if auto_summarize and found_items:
        if not ANTHROPIC_API_KEY:
            return "오류: ANTHROPIC_API_KEY가 설정되지 않아 자동 요약을 실행할 수 없습니다."
        for item in found_items[:5]:  # 한 번에 최대 5개만 요약
            try:
                if item["type"] == "youtube":
                    transcript = get_youtube_transcript(item["video_id"])
                    content = transcript or item.get("title", "")
                else:
                    content = fetch_webpage_text(item["url"])
                summary = summarize_with_claude(content, item["title"], item["url"], item["conference"])
                fp = save_summary(item["conference"], item["title"], item["url"], summary)
                saved_files.append(str(fp))
            except Exception as e:
                errors.append(f"요약 실패 ({item['title'][:40]}): {e}")

    # 결과 포맷
    lines = [f"## 최근 {days}일간 새 콘텐츠 ({len(found_items)}건)\n"]
    for item in found_items:
        emoji = "▶" if item["type"] == "youtube" else "📰"
        lines.append(f"{emoji} [{item['conference']}] {item['title']}")
        lines.append(f"   {item['url']}")
        lines.append(f"   게시: {item.get('published_at', '날짜 불명')}\n")

    if saved_files:
        lines.append(f"\n## 저장된 요약 파일 ({len(saved_files)}개)")
        for f in saved_files:
            lines.append(f"  - {f}")

    if errors:
        lines.append(f"\n## 오류 ({len(errors)}건)")
        for e in errors:
            lines.append(f"  - {e}")

    return "\n".join(lines)


@mcp.tool()
def summarize_url(url: str, conference_name: str = "기타", save: bool = True) -> str:
    """
    YouTube URL 또는 웹페이지 URL을 요약합니다.

    Args:
        url: 요약할 URL (YouTube 영상 또는 웹페이지)
        conference_name: 컨퍼런스 이름 (저장 폴더 분류용)
        save: True면 요약 결과를 파일로 저장
    """
    if not ANTHROPIC_API_KEY:
        return "오류: ANTHROPIC_API_KEY 환경변수가 설정되지 않았습니다."

    title = url
    content = ""

    # YouTube 영상 처리
    video_id = extract_youtube_id(url)
    if video_id:
        info = get_youtube_video_info(video_id)
        title = info.get("title", url)
        if not title:
            title = url

        transcript = get_youtube_transcript(video_id)
        if transcript:
            content = transcript
        elif info.get("description"):
            content = f"[자막 없음] 영상 설명:\n{info['description']}"
        else:
            return f"오류: 자막을 가져올 수 없습니다. (video_id: {video_id})"
    else:
        # 일반 웹페이지 처리
        try:
            content = fetch_webpage_text(url)
            # 페이지 제목 추출
            with httpx.Client(timeout=15, follow_redirects=True) as client:
                resp = client.get(url, headers={"User-Agent": "Mozilla/5.0"})
                soup = BeautifulSoup(resp.text, "html.parser")
                t = soup.find("title")
                if t:
                    title = t.get_text(strip=True)
        except Exception as e:
            return f"웹페이지를 가져오지 못했습니다: {e}"

    if not content.strip():
        return "콘텐츠를 가져올 수 없습니다."

    summary = summarize_with_claude(content, title, url, conference_name)

    result_lines = [f"# {title}\n", summary]

    if save:
        fp = save_summary(conference_name, title, url, summary)
        result_lines.append(f"\n---\n저장 위치: `{fp}`")

    return "\n".join(result_lines)


@mcp.tool()
def list_conferences() -> str:
    """현재 모니터링 중인 컨퍼런스 목록을 반환합니다."""
    cfg = load_config()
    if not cfg["conferences"]:
        return "모니터링 중인 컨퍼런스가 없습니다. add_conference 도구로 추가하세요."

    lines = ["## 모니터링 중인 컨퍼런스\n"]
    for i, conf in enumerate(cfg["conferences"], 1):
        lines.append(f"**{i}. {conf['name']}**")
        if conf.get("youtube_channels"):
            lines.append(f"  - YouTube 채널: {', '.join(conf['youtube_channels'])}")
        if conf.get("rss_feeds"):
            lines.append(f"  - RSS: {', '.join(conf['rss_feeds'])}")
        if conf.get("websites"):
            lines.append(f"  - 웹사이트: {', '.join(conf['websites'])}")
        lines.append("")
    return "\n".join(lines)


@mcp.tool()
def add_conference(
    name: str,
    youtube_channel_ids: str = "",
    rss_feeds: str = "",
    websites: str = "",
) -> str:
    """
    모니터링할 새 컨퍼런스를 추가합니다.

    Args:
        name: 컨퍼런스 이름 (예: "PyCon Korea")
        youtube_channel_ids: YouTube 채널 ID들 (쉼표로 구분)
        rss_feeds: RSS 피드 URL들 (쉼표로 구분)
        websites: 웹사이트 URL들 (쉼표로 구분)
    """
    cfg = load_config()

    # 중복 체크
    for conf in cfg["conferences"]:
        if conf["name"].lower() == name.lower():
            return f"'{name}'은(는) 이미 등록되어 있습니다."

    new_conf = {
        "name": name,
        "youtube_channels": [x.strip() for x in youtube_channel_ids.split(",") if x.strip()],
        "rss_feeds": [x.strip() for x in rss_feeds.split(",") if x.strip()],
        "websites": [x.strip() for x in websites.split(",") if x.strip()],
    }

    cfg["conferences"].append(new_conf)
    save_config(cfg)

    return f"'{name}' 컨퍼런스가 추가되었습니다.\n{json.dumps(new_conf, ensure_ascii=False, indent=2)}"


@mcp.tool()
def remove_conference(name: str) -> str:
    """
    모니터링 목록에서 컨퍼런스를 제거합니다.

    Args:
        name: 제거할 컨퍼런스 이름
    """
    cfg = load_config()
    before = len(cfg["conferences"])
    cfg["conferences"] = [c for c in cfg["conferences"] if c["name"].lower() != name.lower()]

    if len(cfg["conferences"]) == before:
        return f"'{name}'을(를) 찾을 수 없습니다."

    save_config(cfg)
    return f"'{name}' 컨퍼런스가 목록에서 제거되었습니다."


@mcp.tool()
def get_summaries(conference: str = "", limit: int = 10) -> str:
    """
    저장된 요약 파일 목록을 반환합니다.

    Args:
        conference: 특정 컨퍼런스 이름으로 필터링 (비워두면 전체)
        limit: 최대 반환 개수
    """
    if conference:
        search_dir = SUMMARIES_DIR / conference.replace(" ", "_").lower()
        dirs = [search_dir] if search_dir.exists() else []
    else:
        dirs = [d for d in SUMMARIES_DIR.iterdir() if d.is_dir()]

    files = []
    for d in dirs:
        for f in d.glob("*.md"):
            files.append(f)

    if not files:
        msg = f"'{conference}'에 대한 " if conference else ""
        return f"{msg}저장된 요약이 없습니다."

    # 최신순 정렬
    files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
    files = files[:limit]

    lines = [f"## 저장된 요약 ({len(files)}개)\n"]
    for f in files:
        mtime = datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        lines.append(f"- `{f}` ({mtime})")

    return "\n".join(lines)


@mcp.tool()
def read_summary(file_path: str) -> str:
    """
    저장된 요약 파일 내용을 읽습니다.

    Args:
        file_path: get_summaries로 확인한 파일 경로
    """
    fp = Path(file_path)
    if not fp.exists():
        return f"파일을 찾을 수 없습니다: {file_path}"
    if not fp.is_relative_to(SUMMARIES_DIR):
        return "summaries 디렉토리 내의 파일만 읽을 수 있습니다."
    return fp.read_text(encoding="utf-8")


if __name__ == "__main__":
    mcp.run()

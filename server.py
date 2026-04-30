#!/usr/bin/env python3
"""
Conference Summarizer MCP Server
모니터링 대상: Google I/O, Flutter, Apple WWDC, 기타 컨퍼런스
기능: 새 콘텐츠 감지 → 자동 요약 → 파일 저장
"""

import json
import os
import re
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse, parse_qs

import feedparser
import httpx
import imageio_ffmpeg
import whisper
import yt_dlp
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from googleapiclient.discovery import build
from mcp.server.fastmcp import FastMCP
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

_whisper_model = None


def _get_whisper_model():
    global _whisper_model
    if _whisper_model is None:
        _whisper_model = whisper.load_model("base")
    return _whisper_model

load_dotenv()

# ── 설정 ──────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
CONFIG_FILE = BASE_DIR / "config.json"
SUMMARIES_DIR = BASE_DIR / "summaries"
LAST_CHECK_FILE = BASE_DIR / ".last_check.json"
SUMMARIES_DIR.mkdir(exist_ok=True)

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

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
    """YouTube 자막 가져오기 — API 우선, 실패 시 Whisper 폴백"""
    # 1단계: YouTube Transcript API
    try:
        transcript_list = YouTubeTranscriptApi().list(video_id)
        for lang in ["ko", "en", "en-US"]:
            try:
                t = transcript_list.find_transcript([lang])
                entries = t.fetch()
                return " ".join(e.text for e in entries)
            except Exception:
                continue
        try:
            t = transcript_list.find_generated_transcript(["en", "ko"])
            entries = t.fetch()
            return " ".join(e.text for e in entries)
        except Exception:
            pass
    except Exception:
        pass

    # 2단계: Whisper 폴백
    return get_transcript_via_whisper(video_id)


def _get_ffmpeg_dir() -> str:
    """imageio_ffmpeg 바이너리에 'ffmpeg' 심링크를 만들고 그 디렉토리를 반환"""
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    bin_dir = BASE_DIR / "bin"
    bin_dir.mkdir(exist_ok=True)
    symlink = bin_dir / "ffmpeg"
    if not symlink.exists():
        symlink.symlink_to(ffmpeg_exe)
    return str(bin_dir)


def get_transcript_via_whisper(video_id: str) -> str | None:
    """yt-dlp로 오디오 다운로드 후 Whisper로 음성 인식"""
    url = f"https://www.youtube.com/watch?v={video_id}"

    with tempfile.TemporaryDirectory() as tmp_dir:
        audio_path = os.path.join(tmp_dir, "audio.mp3")
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": os.path.join(tmp_dir, "audio.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "64",
            }],
            "ffmpeg_location": _get_ffmpeg_dir(),
            "quiet": True,
            "no_warnings": True,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception:
            return None

        if not os.path.exists(audio_path):
            return None

        try:
            model = _get_whisper_model()
            # Whisper가 시스템 PATH에서 ffmpeg를 찾으므로 bin 디렉토리를 PATH에 추가
            env_path = os.environ.get("PATH", "")
            os.environ["PATH"] = _get_ffmpeg_dir() + os.pathsep + env_path
            result = model.transcribe(audio_path)
            os.environ["PATH"] = env_path
            return result["text"]
        except Exception:
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


# ── 트렌딩 소스 fetcher ──────────────────────────────────────────────────────

def fetch_github_trending(limit: int = 10) -> list[dict]:
    """GitHub 트렌딩 레포지토리 (오늘 기준) 스크래핑"""
    headers = {"User-Agent": "Mozilla/5.0 (Conference-MCP-Bot/1.0)"}
    with httpx.Client(timeout=20, follow_redirects=True) as client:
        resp = client.get("https://github.com/trending", headers=headers)
        resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    repos = []
    for article in soup.select("article.Box-row")[:limit]:
        h2 = article.select_one("h2 a")
        if not h2:
            continue
        repo_path = h2.get("href", "").strip("/")
        if not repo_path:
            continue

        desc_el = article.select_one("p")
        description = desc_el.get_text(strip=True) if desc_el else ""

        lang_el = article.select_one("[itemprop='programmingLanguage']")
        language = lang_el.get_text(strip=True) if lang_el else ""

        stars_el = article.find(string=re.compile(r"stars? today", re.I))
        stars_today = stars_el.strip() if stars_el else ""

        repos.append({
            "title": repo_path,
            "url": f"https://github.com/{repo_path}",
            "description": description,
            "language": language,
            "stars_today": stars_today,
            "source": "github",
        })

    return repos


def fetch_hackernews_top(limit: int = 10) -> list[dict]:
    """Hacker News 상위 스토리 (Firebase API)"""
    with httpx.Client(timeout=20) as client:
        resp = client.get("https://hacker-news.firebaseio.com/v0/topstories.json")
        resp.raise_for_status()
        ids = resp.json()[: limit + 5]

    stories = []
    with httpx.Client(timeout=10) as client:
        for story_id in ids:
            if len(stories) >= limit:
                break
            try:
                resp = client.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
                item = resp.json()
                if not item or item.get("type") != "story" or not item.get("title"):
                    continue
                stories.append({
                    "title": item["title"],
                    "url": item.get("url", f"https://news.ycombinator.com/item?id={story_id}"),
                    "score": item.get("score", 0),
                    "comments": item.get("descendants", 0),
                    "hn_url": f"https://news.ycombinator.com/item?id={story_id}",
                    "source": "hackernews",
                })
            except Exception:
                continue

    return stories


def fetch_devto_trending(limit: int = 10) -> list[dict]:
    """Dev.to 트렌딩 기사 (최근 7일)"""
    with httpx.Client(timeout=20) as client:
        resp = client.get(
            "https://dev.to/api/articles",
            params={"top": "7", "per_page": str(limit)},
            headers={"User-Agent": "Mozilla/5.0 (Conference-MCP-Bot/1.0)"},
        )
        resp.raise_for_status()

    articles = []
    for item in resp.json()[:limit]:
        articles.append({
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "reactions": item.get("public_reactions_count", 0),
            "comments": item.get("comments_count", 0),
            "tags": ", ".join(item.get("tag_list", [])[:4]),
            "source": "devto",
        })

    return articles


def fetch_reddit_top(subreddit: str = "programming", limit: int = 10) -> list[dict]:
    """Reddit 서브레딧 오늘의 상위 게시글"""
    headers = {"User-Agent": "conference-mcp/1.0 (automated bot)"}
    with httpx.Client(timeout=20, follow_redirects=True) as client:
        resp = client.get(
            f"https://www.reddit.com/r/{subreddit}/top.json",
            params={"t": "day", "limit": str(limit)},
            headers=headers,
        )
        resp.raise_for_status()

    posts = []
    for child in resp.json().get("data", {}).get("children", [])[:limit]:
        d = child.get("data", {})
        if d.get("is_self") and not d.get("selftext"):
            continue
        posts.append({
            "title": d.get("title", ""),
            "url": d.get("url", f"https://reddit.com{d.get('permalink', '')}"),
            "score": d.get("score", 0),
            "comments": d.get("num_comments", 0),
            "reddit_url": f"https://reddit.com{d.get('permalink', '')}",
            "subreddit": subreddit,
            "source": "reddit",
        })

    return posts


def fetch_geeknews_top(limit: int = 10) -> list[dict]:
    """GeekNews(news.hada.io) 최신글 RSS"""
    feed = feedparser.parse("https://feeds.feedburner.com/geeknews-feed")
    items = []
    for entry in feed.entries[:limit]:
        items.append({
            "title": entry.get("title", ""),
            "url": entry.get("link", ""),
            "author": entry.get("author", ""),
            "published": entry.get("published", ""),
            "source": "geeknews",
        })
    return items


# ── MCP 도구들 ────────────────────────────────────────────────────────────────

@mcp.tool()
def get_trending(
    sources: str = "github,hackernews,devto,geeknews",
    limit: int = 10,
) -> str:
    """
    개발 트렌딩 콘텐츠를 가져옵니다.
    GitHub 트렌딩 레포, Hacker News 상위 기사, Dev.to 트렌딩, Reddit 인기글, GeekNews(news.hada.io)를 조회합니다.

    Args:
        sources: 쉼표로 구분된 소스 (github, hackernews, devto, reddit, geeknews)
        limit: 각 소스별 최대 항목 수 (기본값: 10)
    """
    source_list = [s.strip().lower() for s in sources.split(",") if s.strip()]
    today = datetime.now().strftime("%Y-%m-%d")
    lines = [f"# 🔥 개발 트렌딩 — {today}\n"]
    all_items: list[dict] = []
    errors: list[str] = []

    if "github" in source_list:
        try:
            repos = fetch_github_trending(limit)
            lines.append("## ⭐ GitHub Trending (오늘)\n")
            for r in repos:
                lang = f" #{r['language']}" if r["language"] else ""
                stars = f" · {r['stars_today']}" if r["stars_today"] else ""
                lines.append(f"- **[{r['title']}]({r['url']})**{lang}{stars}")
                if r["description"]:
                    lines.append(f"  {r['description']}")
            lines.append("")
            all_items.extend(repos)
        except Exception as e:
            errors.append(f"GitHub Trending: {e}")

    if any(s in source_list for s in ("hackernews", "hn")):
        try:
            stories = fetch_hackernews_top(limit)
            lines.append("## 🟠 Hacker News Top Stories\n")
            for s in stories:
                lines.append(
                    f"- **[{s['title']}]({s['url']})** (⬆{s['score']} 💬{s['comments']}) — [HN]({s['hn_url']})"
                )
            lines.append("")
            all_items.extend(stories)
        except Exception as e:
            errors.append(f"Hacker News: {e}")

    if "devto" in source_list:
        try:
            articles = fetch_devto_trending(limit)
            lines.append("## 💻 Dev.to Trending (7일)\n")
            for a in articles:
                tags = (" " + " ".join(f"#{t.strip()}" for t in a["tags"].split(",") if t.strip())) if a["tags"] else ""
                lines.append(
                    f"- **[{a['title']}]({a['url']})** (❤️{a['reactions']} 💬{a['comments']}){tags}"
                )
            lines.append("")
            all_items.extend(articles)
        except Exception as e:
            errors.append(f"Dev.to: {e}")

    if any(s in source_list for s in ("geeknews", "hada")):
        try:
            items = fetch_geeknews_top(limit)
            lines.append("## 🇰🇷 GeekNews (news.hada.io)\n")
            for it in items:
                author = f" — {it['author']}" if it.get("author") else ""
                lines.append(f"- **[{it['title']}]({it['url']})**{author}")
            lines.append("")
            all_items.extend(items)
        except Exception as e:
            errors.append(f"GeekNews: {e}")

    if "reddit" in source_list:
        for sub in ["programming", "webdev"]:
            try:
                posts = fetch_reddit_top(sub, limit // 2 or 5)
                lines.append(f"## 👾 r/{sub} Top (오늘)\n")
                for p in posts:
                    lines.append(
                        f"- **[{p['title']}]({p['url']})** (⬆{p['score']} 💬{p['comments']})"
                    )
                lines.append("")
                all_items.extend(posts)
            except Exception as e:
                errors.append(f"Reddit r/{sub}: {e}")

    if errors:
        lines.append("## ⚠️ 오류\n")
        for e in errors:
            lines.append(f"- {e}")
        lines.append("")

    return "\n".join(lines)


@mcp.tool()
def check_new_content(days: int = 7) -> str:
    """
    모든 컨퍼런스에서 최근 N일간 새 콘텐츠를 확인합니다.
    발견 결과만 반환하며, 요약은 슬래시 커맨드(/add-link) 또는 cron이 별도로 처리합니다.

    Args:
        days: 확인할 기간 (기본값: 7일)
    """
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

    # 결과 포맷
    lines = [f"## 최근 {days}일간 새 콘텐츠 ({len(found_items)}건)\n"]
    for item in found_items:
        emoji = "▶" if item["type"] == "youtube" else "📰"
        lines.append(f"{emoji} [{item['conference']}] {item['title']}")
        lines.append(f"   {item['url']}")
        lines.append(f"   게시: {item.get('published_at', '날짜 불명')}\n")

    if errors:
        lines.append(f"\n## 오류 ({len(errors)}건)")
        for e in errors:
            lines.append(f"  - {e}")

    return "\n".join(lines)


@mcp.tool()
def extract_url_content(url: str, conference_name: str = "기타") -> str:
    """
    YouTube 영상 또는 웹페이지에서 raw 콘텐츠(자막/본문)를 추출해 반환합니다.
    요약은 호출 측(슬래시 커맨드의 Claude Code 또는 cron이 띄운 헤드리스 Claude)이 직접 작성합니다.

    Args:
        url: 추출할 URL (YouTube 영상 또는 웹페이지)
        conference_name: 컨퍼런스 이름 (메타데이터, 저장 폴더 분류용)

    Returns:
        다음 형식의 마크다운:
        ## 메타
        - title: ...
        - source_url: ...
        - conference_name: ...
        - type: youtube | webpage

        ## 본문
        <transcript 또는 webpage 본문 텍스트, 12000자 절단>
    """
    title = url
    content = ""
    content_type = "webpage"

    video_id = extract_youtube_id(url)
    if video_id:
        content_type = "youtube"
        info = get_youtube_video_info(video_id)
        title = info.get("title") or url

        transcript = get_youtube_transcript(video_id)
        if transcript:
            content = transcript
        elif info.get("description"):
            content = f"[자막 없음] 영상 설명:\n{info['description']}"
        else:
            return f"오류: 자막을 가져올 수 없습니다. (video_id: {video_id})"
    else:
        try:
            content = fetch_webpage_text(url)
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

    truncated = content[:12000] + ("..." if len(content) > 12000 else "")

    return (
        "## 메타\n"
        f"- title: {title}\n"
        f"- source_url: {url}\n"
        f"- conference_name: {conference_name}\n"
        f"- type: {content_type}\n\n"
        "## 본문\n"
        f"{truncated}"
    )


@mcp.tool()
def save_summary_text(
    conference_name: str,
    title: str,
    source_url: str,
    summary_markdown: str,
) -> str:
    """
    이미 작성된 요약 마크다운을 받아 summaries/<conference>/<timestamp>_<title>.md 로 저장합니다.

    Args:
        conference_name: 컨퍼런스 이름 (저장 폴더 분류용)
        title: 콘텐츠 제목
        source_url: 원본 URL
        summary_markdown: 요약 마크다운 본문 (## 🔑 핵심 요약 등 섹션 4개)

    Returns:
        저장된 파일의 절대 경로
    """
    fp = save_summary(conference_name, title, source_url, summary_markdown)
    return f"✅ 저장 완료: {fp}"


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

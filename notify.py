"""
Conference Summarizer — Teams & Email notifier
Usage: python notify.py "<summary_text>"
Reads TEAMS_WEBHOOK_URL, EMAIL_* from .env
"""
import os
import sys
import smtplib
import json
import re
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from datetime import datetime

# ─── .env loader ─────────────────────────────────────────────────────────────

def _load_env():
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                if v:
                    os.environ.setdefault(k.strip(), v.strip())

_load_env()

_PROJECT_DIR = str(Path(__file__).parent)
_CLAUDE_BIN = os.environ.get("CLAUDE_BIN", "claude")


def _call_claude_cli(prompt: str, timeout: int = 180) -> str:
    """헤드리스 Claude Code CLI 호출 (Max 구독으로 처리). 실패 시 빈 문자열."""
    try:
        result = subprocess.run(
            [
                _CLAUDE_BIN, "--print",
                "--no-session-persistence",
                "--max-budget-usd", "0.50",
                prompt,
            ],
            capture_output=True, text=True, timeout=timeout,
            cwd=_PROJECT_DIR,
        )
        if result.returncode != 0:
            print(f"[notify] claude CLI 실패 (rc={result.returncode}): {result.stderr[:300]}")
            return ""
        return result.stdout.strip()
    except Exception as e:
        print(f"[notify] claude CLI 예외: {e}")
        return ""


# ─── Parse result text ────────────────────────────────────────────────────────

def parse_items(text: str) -> list[dict]:
    """Extract new content items from check_new_content() output."""
    items = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("▶") or line.startswith("📰"):
            icon = "▶" if line.startswith("▶") else "📰"
            content = line[1:].strip()
            url = ""
            parts = content.rsplit(" ", 1)
            if len(parts) == 2 and parts[1].startswith("http"):
                url = parts[1]
                content = parts[0]
            items.append({"icon": icon, "title": content, "url": url})
    return items


def parse_saved_files(text: str) -> list[Path]:
    """Extract saved summary file paths from check_new_content() output."""
    files = []
    in_section = False
    for line in text.splitlines():
        if "저장된 요약 파일" in line:
            in_section = True
            continue
        if in_section:
            stripped = line.strip().lstrip("- ").strip()
            if stripped.endswith(".md") and Path(stripped).exists():
                files.append(Path(stripped))
            elif not stripped:
                pass
            elif stripped.startswith("##") or stripped.startswith("오류"):
                break
    return files


# ─── Teams helpers ────────────────────────────────────────────────────────────

GITHUB_REPO_URL = "https://github.com/haeihnlee/techRaderMCP"
_BASE_DIR = Path(__file__).parent


def _github_file_url(filepath: Path) -> str:
    try:
        rel = filepath.relative_to(_BASE_DIR)
        return f"{GITHUB_REPO_URL}/blob/main/{rel}"
    except ValueError:
        return ""


def _post_to_teams(payload: dict) -> bool:
    webhook_url = os.environ.get("TEAMS_WEBHOOK_URL", "").strip()
    if not webhook_url:
        print("[notify] TEAMS_WEBHOOK_URL not set, skipping Teams")
        return False
    try:
        import httpx
        resp = httpx.post(webhook_url, json=payload, timeout=10)
        if resp.status_code < 300:
            return True
        print(f"[notify] Teams 오류: {resp.status_code} {resp.text[:200]}")
        return False
    except Exception as e:
        print(f"[notify] Teams 예외: {e}")
        return False


def _adaptive_card(body: list, actions: list = None) -> dict:
    card = {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.4",
        "body": body,
        "msteams": {"width": "Full"},
    }
    if actions:
        card["actions"] = actions
    return {
        "type": "message",
        "attachments": [{
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": card,
        }]
    }


# ─── Trending: parse & Teams card ────────────────────────────────────────────

def parse_trending(text: str) -> dict:
    """get_trending() 마크다운 출력을 구조화된 dict로 파싱."""
    # 혼합 출력(컨퍼런스 + 트렌딩)에서 트렌딩 섹션만 추출
    marker = "===== 트렌딩 ====="
    idx = text.find(marker)
    if idx != -1:
        text = text[idx + len(marker):]

    github, hn, devto, geeknews = [], [], [], []
    current_section = None
    lines = text.splitlines()

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if "GitHub Trending" in line:
            current_section = "github"
        elif "Hacker News" in line:
            current_section = "hn"
        elif "Dev.to" in line:
            current_section = "devto"
        elif "GeekNews" in line:
            current_section = "geeknews"
        elif stripped.startswith("- **[") and current_section:
            if current_section == "github":
                m = re.match(r"- \*\*\[(.+?)\]\((.+?)\)\*\*(.*)", stripped)
                if m:
                    rest = m.group(3)
                    lang_m = re.search(r"`([^`]+)`", rest)
                    stars_m = re.search(r"([\d,]+)\s*stars? today", rest, re.I)
                    desc = ""
                    if i + 1 < len(lines):
                        nxt = lines[i + 1]
                        if nxt.startswith("  ") and not nxt.strip().startswith("-"):
                            desc = nxt.strip()
                    github.append({
                        "title": m.group(1), "url": m.group(2),
                        "language": lang_m.group(1) if lang_m else "",
                        "stars_today": stars_m.group(1) if stars_m else "",
                        "description": desc,
                    })
            elif current_section == "hn":
                m = re.match(
                    r"- \*\*\[(.+?)\]\((.+?)\)\*\*\s*\(⬆(\d+)\s*💬(\d+)\)(?:.*\[HN\]\((.+?)\))?",
                    stripped,
                )
                if m:
                    hn.append({
                        "title": m.group(1), "url": m.group(2),
                        "score": int(m.group(3)), "comments": int(m.group(4)),
                        "hn_url": m.group(5) or m.group(2),
                    })
            elif current_section == "devto":
                m = re.match(
                    r"- \*\*\[(.+?)\]\((.+?)\)\*\*\s*\(❤️(\d+)\s*💬(\d+)\)(.*)",
                    stripped,
                )
                if m:
                    tags_m = re.findall(r"#(\w+)", m.group(5))
                    devto.append({
                        "title": m.group(1), "url": m.group(2),
                        "reactions": int(m.group(3)), "comments": int(m.group(4)),
                        "tags": " ".join(f"#{t}" for t in tags_m),
                    })
            elif current_section == "geeknews":
                m = re.match(r"- \*\*\[(.+?)\]\((.+?)\)\*\*(?:\s*—\s*(.+))?", stripped)
                if m:
                    geeknews.append({
                        "title": m.group(1), "url": m.group(2),
                        "author": (m.group(3) or "").strip(),
                    })
        i += 1

    return {"github": github, "hn": hn, "devto": devto, "geeknews": geeknews}


def _get_webos_picks(data: dict, korean: dict) -> list[dict]:
    """트렌딩 항목 중 webOS 개발에 도움이 될 항목을 Claude로 선별.
    [{"title": ..., "url": ..., "reason": ...}] 반환 (최대 3개)."""
    items = []
    for r in data.get("github", []):
        ko = korean.get(r["url"], {})
        desc = ko.get("desc", "") if isinstance(ko, dict) else r.get("description", "")
        items.append(f"[github] {r['url']} | {r['title']} | {desc}")
    for s in data.get("hn", []):
        ko = korean.get(s["url"], {})
        desc = ko.get("desc", "") if isinstance(ko, dict) else ""
        items.append(f"[hn] {s['url']} | {s['title']} | {desc}")
    for a in data.get("devto", []):
        ko = korean.get(a["url"], {})
        desc = ko.get("desc", "") if isinstance(ko, dict) else ""
        items.append(f"[devto] {a['url']} | {a['title']} | {desc}")
    for g in data.get("geeknews", []):
        ko = korean.get(g["url"], {})
        desc = ko.get("desc", "") if isinstance(ko, dict) else ""
        items.append(f"[geeknews] {g['url']} | {g['title']} | {desc}")

    if not items:
        return []

    prompt = (
        "아래는 오늘의 개발 트렌딩 항목들입니다.\n"
        "webOS 앱/플랫폼 개발자(JavaScript, TypeScript, React/Enact, 웹 기술, TV UI/UX, 성능 최적화, 미디어, 임베디드 웹)에게 "
        "도움이 될 항목을 최대 3개 골라주세요.\n"
        "없으면 빈 응답을 반환하세요.\n"
        "반드시 'URL | 추천 이유(한국어 20자 이내)' 형식으로만, 한 줄씩 응답하세요. 다른 설명·서두·결론은 쓰지 마세요.\n\n"
        + "\n".join(items)
    )

    response = _call_claude_cli(prompt)
    if not response:
        return []

    picks = []
    all_items = {r["url"]: r for r in data.get("github", [])}
    all_items.update({s["url"]: s for s in data.get("hn", [])})
    all_items.update({a["url"]: a for a in data.get("devto", [])})
    all_items.update({g["url"]: g for g in data.get("geeknews", [])})
    for line in response.splitlines():
        if " | " in line:
            url, _, reason = line.partition(" | ")
            url = url.strip()
            reason = reason.strip()
            if url.startswith("http") and reason and url in all_items:
                picks.append({"title": all_items[url]["title"], "url": url, "reason": reason})
    return picks[:3]


def _get_korean_descriptions(data: dict) -> dict:
    """항목들의 한국어 한 줄 설명과 키워드를 Claude로 일괄 생성.
    {url: {"desc": 한글설명, "tags": "#tag1 #tag2"}} 반환."""
    lines = []
    for r in data.get("github", []):
        hint = r.get("description", "")[:80]
        lines.append(f"[github] {r['url']} | {r['title']} | {hint}")
    for s in data.get("hn", []):
        lines.append(f"[hn] {s['url']} | {s['title']}")
    for a in data.get("devto", []):
        lines.append(f"[devto] {a['url']} | {a['title']} | tags: {a.get('tags', '')}")
    for g in data.get("geeknews", []):
        author = f" | by {g['author']}" if g.get("author") else ""
        lines.append(f"[geeknews] {g['url']} | {g['title']}{author}")

    if not lines:
        return {}

    prompt = (
        "아래 각 항목에 대해 개발자 관점의 한국어 한 줄 설명(15~30자)과 관련 키워드 2~3개를 작성하세요.\n"
        "반드시 'URL | 한글설명 | #keyword1 #keyword2 #keyword3' 형식으로만, 각 항목당 딱 한 줄씩 응답하세요. 다른 설명·서두·결론은 쓰지 마세요.\n\n"
        + "\n".join(lines)
    )

    response = _call_claude_cli(prompt)
    if not response:
        return {}

    result = {}
    for line in response.splitlines():
        parts = [p.strip() for p in line.split(" | ")]
        if len(parts) >= 2 and parts[0].startswith("http"):
            result[parts[0]] = {
                "desc": parts[1],
                "tags": parts[2] if len(parts) >= 3 else "",
            }
    return result


def send_trending_to_teams(trending_text: str) -> bool:
    data = parse_trending(trending_text)
    if not any(data.values()):
        print("[notify] 트렌딩 데이터 없음, 스킵")
        return False

    korean = _get_korean_descriptions(data)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    body: list[dict] = [
        {"type": "TextBlock", "text": "🔥  개발 트렌딩",
         "size": "Large", "weight": "Bolder"},
        {"type": "TextBlock", "text": now, "isSubtle": True, "spacing": "Small"},
    ]

    # ── GitHub Trending ──────────────────────────────────────────────────────
    if data["github"]:
        body.append({
            "type": "TextBlock", "text": "⭐  GitHub Trending (오늘)",
            "weight": "Bolder", "color": "Warning",
            "separator": True, "spacing": "Medium",
        })
        for r in data["github"][:5]:
            lang = f"\n#{r['language']}" if r["language"] else ""
            stars = f" · ⭐ {r['stars_today']}" if r["stars_today"] else ""
            body.append({
                "type": "TextBlock",
                "text": f"[{r['title']}]({r['url']}){stars}{lang}",
                "wrap": True, "spacing": "Small",
            })
            ko = korean.get(r["url"], {})
            ko_desc = ko.get("desc", "") if isinstance(ko, dict) else ko or r.get("description", "")
            if ko_desc:
                body.append({
                    "type": "TextBlock", "text": ko_desc,
                    "wrap": True, "isSubtle": True, "size": "Small", "spacing": "None",
                })
        body.append({
            "type": "ActionSet", "spacing": "Small",
            "actions": [{"type": "Action.OpenUrl", "title": "⭐ GitHub Trending 바로가기",
                         "url": "https://github.com/trending"}],
        })

    # ── Hacker News ──────────────────────────────────────────────────────────
    if data["hn"]:
        body.append({
            "type": "TextBlock", "text": "🟠  Hacker News Top Stories",
            "weight": "Bolder", "color": "Warning",
            "separator": True, "spacing": "Medium",
        })
        for s in data["hn"][:5]:
            ko = korean.get(s["url"], {})
            ko_tags = ko.get("tags", "") if isinstance(ko, dict) else ""
            body.append({
                "type": "TextBlock",
                "text": f"[{s['title']}]({s['url']})  ⬆{s['score']} 💬{s['comments']}" + (f"\n{ko_tags}" if ko_tags else ""),
                "wrap": True, "spacing": "Small",
            })
            ko_desc = ko.get("desc", "") if isinstance(ko, dict) else ko or ""
            if ko_desc:
                body.append({
                    "type": "TextBlock", "text": ko_desc,
                    "wrap": True, "isSubtle": True, "size": "Small", "spacing": "None",
                })
        body.append({
            "type": "ActionSet", "spacing": "Small",
            "actions": [{"type": "Action.OpenUrl", "title": "🟠 Hacker News Top 바로가기",
                         "url": "https://news.ycombinator.com/"}],
        })

    # ── Dev.to ───────────────────────────────────────────────────────────────
    if data["devto"]:
        body.append({
            "type": "TextBlock", "text": "💻  Dev.to Trending (7일)",
            "weight": "Bolder", "color": "Warning",
            "separator": True, "spacing": "Medium",
        })
        for a in data["devto"][:5]:
            tags = f"\n{a['tags']}" if a["tags"] else ""
            body.append({
                "type": "TextBlock",
                "text": f"[{a['title']}]({a['url']})  ❤️{a['reactions']}{tags}",
                "wrap": True, "spacing": "Small",
            })
            ko = korean.get(a["url"], {})
            ko_desc = ko.get("desc", "") if isinstance(ko, dict) else ko or ""
            if ko_desc:
                body.append({
                    "type": "TextBlock", "text": ko_desc,
                    "wrap": True, "isSubtle": True, "size": "Small", "spacing": "None",
                })
        body.append({
            "type": "ActionSet", "spacing": "Small",
            "actions": [{"type": "Action.OpenUrl", "title": "💻 Dev.to Trending 바로가기",
                         "url": "https://dev.to/top/week"}],
        })

    # ── GeekNews (news.hada.io) ──────────────────────────────────────────────
    if data.get("geeknews"):
        body.append({
            "type": "TextBlock", "text": "🇰🇷  GeekNews (news.hada.io)",
            "weight": "Bolder", "color": "Warning",
            "separator": True, "spacing": "Medium",
        })
        for g in data["geeknews"][:5]:
            author = f"  · {g['author']}" if g.get("author") else ""
            body.append({
                "type": "TextBlock",
                "text": f"[{g['title']}]({g['url']}){author}",
                "wrap": True, "spacing": "Small",
            })
            ko = korean.get(g["url"], {})
            ko_desc = ko.get("desc", "") if isinstance(ko, dict) else ko or ""
            if ko_desc:
                body.append({
                    "type": "TextBlock", "text": ko_desc,
                    "wrap": True, "isSubtle": True, "size": "Small", "spacing": "None",
                })
        body.append({
            "type": "ActionSet", "spacing": "Small",
            "actions": [{"type": "Action.OpenUrl", "title": "🇰🇷 GeekNews 바로가기",
                         "url": "https://news.hada.io/"}],
        })

    # ── 주목할 만한 항목 ─────────────────────────────────────────────────────
    notables: list[str] = []
    if data["github"]:
        top = max(data["github"],
                  key=lambda x: int(x["stars_today"].replace(",", "") or "0"))
        ko = korean.get(top["url"], {})
        ko_desc = ko.get("desc", "") if isinstance(ko, dict) else ko or top.get("description", "")
        desc = f" — {ko_desc[:60]}" if ko_desc else ""
        notables.append(f"• ⭐ [{top['title']}]({top['url']}){desc}")
    if data["hn"]:
        top = max(data["hn"], key=lambda x: x["score"])
        ko = korean.get(top["url"], {})
        ko_desc = ko.get("desc", "") if isinstance(ko, dict) else ko or ""
        desc = f" — {ko_desc}" if ko_desc else ""
        notables.append(f"• 🟠 [{top['title']}]({top['url']})  ⬆{top['score']}{desc}")
    if data["devto"]:
        top = max(data["devto"], key=lambda x: x["reactions"])
        ko = korean.get(top["url"], {})
        ko_desc = ko.get("desc", "") if isinstance(ko, dict) else ko or ""
        desc = f" — {ko_desc}" if ko_desc else ""
        notables.append(f"• 💻 [{top['title']}]({top['url']})  ❤️{top['reactions']}{desc}")
    if data.get("geeknews"):
        top = data["geeknews"][0]
        ko = korean.get(top["url"], {})
        ko_desc = ko.get("desc", "") if isinstance(ko, dict) else ko or ""
        desc = f" — {ko_desc}" if ko_desc else ""
        notables.append(f"• 🇰🇷 [{top['title']}]({top['url']}){desc}")

    if notables:
        body.append({
            "type": "TextBlock", "text": "🔎  주목할 만한 항목",
            "weight": "Bolder", "color": "Warning",
            "separator": True, "spacing": "Medium",
        })
        for n in notables:
            body.append({"type": "TextBlock", "text": n, "wrap": True, "spacing": "Small"})

    webos_picks = _get_webos_picks(data, korean)
    if webos_picks:
        body.append({
            "type": "TextBlock", "text": "📺  webOS 개발자 추천",
            "weight": "Bolder", "color": "Accent",
            "separator": True, "spacing": "Medium",
        })
        for p in webos_picks:
            body.append({
                "type": "TextBlock",
                "text": f"[{p['title']}]({p['url']})\n{p['reason']}",
                "wrap": True, "spacing": "Small",
            })

    payload = _adaptive_card(body)
    ok = _post_to_teams(payload)
    if ok:
        print("[notify] Teams 트렌딩 전송 완료")
    return ok


# ─── Teams: daily digest ──────────────────────────────────────────────────────

def send_teams(items: list[dict], full_text: str) -> bool:
    count = len(items)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    rows = []
    for item in items[:20]:
        icon = "🎬" if item["icon"] == "▶" else "📰"
        text = f"{icon}  [{item['title'][:72]}]({item['url']})" if item["url"] \
               else f"{icon}  {item['title'][:72]}"
        rows.append({"type": "TextBlock", "text": text, "wrap": True,
                     "spacing": "Small", "size": "Small"})
    if len(items) > 20:
        rows.append({"type": "TextBlock",
                     "text": f"_... 외 {len(items)-20}개_",
                     "isSubtle": True, "size": "Small", "spacing": "Small"})

    body = [
        {"type": "TextBlock", "text": "🎉  새 컨퍼런스 콘텐츠",
         "size": "Large", "weight": "Bolder"},
        {"type": "TextBlock", "text": f"{now}  ·  **{count}개** 발견",
         "isSubtle": True, "spacing": "Small"},
        *([{**rows[0], "separator": True, "spacing": "Medium"}, *rows[1:]] if rows else []),
    ]

    payload = _adaptive_card(body)
    ok = _post_to_teams(payload)
    if ok:
        print(f"[notify] Teams 전송 완료 ({count}개)")
    return ok


# ─── Teams: single summary file ───────────────────────────────────────────────

def _clean_for_teams(text: str) -> str:
    """Adaptive Card TextBlock에서 지원하지 않는 마크다운 제거"""
    lines = []
    for line in text.splitlines():
        line = line.lstrip("> ")                            # blockquote 제거
        line = re.sub(r"`([^`]+)`", r"\1", line)           # backtick 코드 제거
        line = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)    # bold 마커 제거 (내용 유지)
        line = re.sub(r"\*([^*]+)\*", r"\1", line)         # italic 마커 제거 (내용 유지)
        line = re.sub(r"^#+\s*", "", line)                  # 헤더 # 제거
        line = re.sub(r"\|.*\|", "", line)                  # 테이블 행 제거
        line = re.sub(r"^[-=]{3,}$", "", line)              # 구분선 제거
        lines.append(line)
    return "\n".join(l for l in lines if l.strip())


def _table_to_facts(text: str) -> list[dict]:
    """마크다운 테이블을 FactSet facts 리스트로 변환"""
    facts = []
    for line in text.splitlines():
        line = line.strip()
        if not (line.startswith("|") and line.endswith("|")):
            continue
        if re.match(r"^\|[\s\-:|]+\|$", line):  # separator row skip
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 2 and cells[0] and cells[1]:
            facts.append({"title": cells[0], "value": cells[1]})
    return facts


def _extract_section(text: str, keyword: str) -> str:
    """heading에 keyword가 포함된 ## 섹션 추출 (이모지 있어도 매칭)"""
    result = []
    in_section = False
    for line in text.splitlines():
        if line.startswith("## ") and keyword in line:
            in_section = True
            continue
        if in_section:
            if line.startswith("## "):
                break
            result.append(line)
    return "\n".join(result).strip()


def _get_webos_picks_from_doc(text: str) -> list[str]:
    """요약 문서에서 webOS 개발자에게 도움이 될 포인트를 Claude로 추출.
    ['• 포인트 (이유)', ...] 반환 (최대 3개). 없으면 빈 리스트."""
    prompt = (
        "아래는 개발 컨퍼런스/아티클 요약입니다.\n"
        "webOS 앱/플랫폼 개발자(JavaScript, TypeScript, React/Enact, 웹 기술, TV UI/UX, 성능 최적화, 미디어, 임베디드 웹)에게 "
        "직접적으로 도움이 될 내용을 최대 3개 골라주세요.\n"
        "관련 내용이 없으면 빈 응답을 반환하세요.\n"
        "반드시 '• 포인트 내용 — 이유(15자 이내)' 형식으로만, 한 줄씩 응답하세요. 다른 설명·서두·결론은 쓰지 마세요.\n\n"
        + text[:3000]
    )

    response = _call_claude_cli(prompt)
    if not response:
        return []

    picks = [
        line.strip()
        for line in response.splitlines()
        if line.strip().startswith("•")
    ]
    return picks[:3]


def post_file_to_teams(filepath: str | Path) -> bool:
    filepath = Path(filepath).resolve()
    if not filepath.exists():
        print(f"[notify] 파일 없음: {filepath}")
        return False

    text = filepath.read_text(encoding="utf-8", errors="ignore")
    lines = text.strip().splitlines()

    # 메타 파싱
    title = lines[0].lstrip("# ").strip() if lines else filepath.stem
    conference, source_url, summary_date = "", "", ""
    for line in lines:
        if line.startswith("- **컨퍼런스**:"):
            conference = line.split(":", 1)[1].strip()
        elif line.startswith("- **출처**:"):
            source_url = line.split(":", 1)[1].strip()
        elif line.startswith("- **요약 일시**:"):
            summary_date = line.split(":", 1)[1].strip()[:10]

    # 섹션 추출
    summary_3   = _extract_section(text, "핵심 요약")
    main_points = _extract_section(text, "주요 발표")
    dev_points  = _extract_section(text, "개발자")
    schedule    = _extract_section(text, "출시 일정") or _extract_section(text, "버전")

    # 핵심 요약 → 항목별 TextBlock (최대 5줄)
    summary_bullet_lines = [
        "• " + l.lstrip("- ").strip()
        for l in _clean_for_teams(summary_3).splitlines() if l.strip().lstrip("- ")
    ][:5]

    # 주요 내용 → ### 소제목은 bold, 항목은 bullet, 하위항목은 ↳
    main_point_blocks = []
    for raw in main_points.splitlines():
        if not raw.strip():
            continue
        stripped = raw.strip()
        if stripped.startswith("###"):
            content = re.sub(r"^#+\s*", "", stripped)
            content = re.sub(r"`([^`]+)`", r"\1", content)
            if content:
                main_point_blocks.append({
                    "type": "TextBlock", "text": content,
                    "wrap": True, "weight": "Bolder", "size": "Medium", "spacing": "Large",
                })
        else:
            is_sub = raw != raw.lstrip()
            line = raw.lstrip("> ")
            line = re.sub(r"`([^`]+)`", r"\1", line)
            line = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)
            line = re.sub(r"\*([^*]+)\*", r"\1", line)
            content = line.strip().lstrip("- ").strip()
            if not content:
                continue
            main_point_blocks.append({
                "type": "TextBlock",
                "text": "  ↳ " + content if is_sub else "• " + content,
                "wrap": True, "spacing": "Small",
            })

    # 개발자 포인트 → 항목별 TextBlock (줄바꿈 보장)
    dev_bullet_lines = [
        "• " + l.lstrip("- ").strip()
        for l in _clean_for_teams(dev_points).splitlines() if l.strip().lstrip("- ")
    ]

    icon = "🎬" if source_url and "youtube" in source_url else "📰"
    conf_label = f"{icon}  {conference}" if conference else icon

    body = [
        # 헤더
        {"type": "TextBlock", "text": conf_label,
         "size": "Small", "color": "Warning", "weight": "Bolder"},
        {"type": "TextBlock", "text": title,
         "size": "Large", "weight": "Bolder", "wrap": True, "spacing": "Small"},
        {"type": "TextBlock", "text": summary_date,
         "isSubtle": True, "size": "Small", "spacing": "Small"},
        # 핵심 요약
        {"type": "TextBlock", "text": "📌  핵심 요약",
         "weight": "Bolder", "color": "Warning", "size": "Large", "separator": True, "spacing": "Large"},
        *[
            {"type": "TextBlock", "text": line, "wrap": True, "spacing": "Small"}
            for line in summary_bullet_lines
        ],
    ]

    if main_point_blocks:
        body += [
            {"type": "TextBlock", "text": "📋  주요 발표 내용",
             "weight": "Bolder", "color": "Warning", "size": "Large", "separator": True, "spacing": "Large"},
            *main_point_blocks,
        ]

    if dev_bullet_lines:
        body += [
            {"type": "TextBlock", "text": "💡  개발자 포인트",
             "weight": "Bolder", "color": "Warning", "size": "Large", "separator": True, "spacing": "Large"},
            *[
                {"type": "TextBlock", "text": line, "wrap": True, "spacing": "Small"}
                for line in dev_bullet_lines
            ],
        ]

    if schedule:
        sched_facts = _table_to_facts(schedule)
        sched_text = _clean_for_teams(schedule)[:400]
        body.append({"type": "TextBlock", "text": "📅  버전 / 출시 일정",
                     "weight": "Bolder", "color": "Warning", "size": "Large", "separator": True, "spacing": "Large"})
        if sched_facts:
            body.append({"type": "FactSet", "facts": sched_facts, "spacing": "Small"})
        elif sched_text:
            body.append({"type": "TextBlock", "text": sched_text,
                         "wrap": True, "spacing": "Small", "isSubtle": True})

    webos_picks = _get_webos_picks_from_doc(text)
    if webos_picks:
        body.append({
            "type": "TextBlock", "text": "📺  webOS 개발자 추천",
            "weight": "Bolder", "color": "Accent",
            "separator": True, "spacing": "Large", "size": "Large",
        })
        for p in webos_picks:
            body.append({"type": "TextBlock", "text": p, "wrap": True, "spacing": "Small"})

    actions = []
    if source_url:
        actions.append({
            "type": "Action.OpenUrl",
            "title": "▶  원본 보기",
            "url": source_url,
        })
    github_url = _github_file_url(filepath)
    if github_url:
        actions.append({
            "type": "Action.OpenUrl",
            "title": "📄  자세히 보기",
            "url": github_url,
        })

    payload = _adaptive_card(body, actions)
    ok = _post_to_teams(payload)
    if ok:
        print(f"[notify] Teams 게시 완료: {title}")
    return ok


# ─── Email ────────────────────────────────────────────────────────────────────

def send_email(items: list[dict], full_text: str) -> bool:
    smtp_host = os.environ.get("EMAIL_SMTP_HOST", "").strip()
    smtp_port = int(os.environ.get("EMAIL_SMTP_PORT", "587"))
    email_from = os.environ.get("EMAIL_FROM", "").strip()
    email_password = os.environ.get("EMAIL_PASSWORD", "").strip()
    email_to = os.environ.get("EMAIL_TO", "").strip()

    if not all([smtp_host, email_from, email_to]):
        print("[notify] EMAIL_* not configured, skipping email")
        return False

    count = len(items)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Build HTML body
    rows = ""
    for item in items:
        icon = "🎬" if item["icon"] == "▶" else "📰"
        title_cell = (
            f'<a href="{item["url"]}" style="color:#4A9EFF;text-decoration:none;">{item["title"]}</a>'
            if item["url"] else item["title"]
        )
        rows += f"<tr><td style='padding:6px 4px;font-size:13px;'>{icon}</td><td style='padding:6px 4px;font-size:13px;'>{title_cell}</td></tr>"

    html = f"""
<!DOCTYPE html>
<html>
<body style="margin:0;padding:0;background:#f5f5f5;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
  <div style="max-width:600px;margin:24px auto;background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,.1);">
    <div style="background:linear-gradient(135deg,#1a1f2e,#16213e);padding:24px 28px;">
      <div style="color:#fff;font-size:20px;font-weight:700;">🎉 컨퍼런스 새 콘텐츠</div>
      <div style="color:#8899aa;font-size:13px;margin-top:4px;">{now} &nbsp;·&nbsp; {count}개 발견</div>
    </div>
    <div style="padding:24px 28px;">
      <table style="width:100%;border-collapse:collapse;">
        <tbody>{rows}</tbody>
      </table>
    </div>
    <div style="padding:12px 28px 20px;color:#aaa;font-size:11px;border-top:1px solid #eee;">
      Conference Summarizer MCP
    </div>
  </div>
</body>
</html>
"""

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"[컨퍼런스] 새 콘텐츠 {count}개 — {now}"
    msg["From"] = email_from
    msg["To"] = email_to
    msg.attach(MIMEText(html, "html", "utf-8"))

    try:
        if smtp_port == 465:
            with smtplib.SMTP_SSL(smtp_host, smtp_port, timeout=15) as s:
                if email_password:
                    s.login(email_from, email_password)
                s.sendmail(email_from, email_to.split(","), msg.as_string())
        else:
            with smtplib.SMTP(smtp_host, smtp_port, timeout=15) as s:
                s.ehlo()
                s.starttls()
                if email_password:
                    s.login(email_from, email_password)
                s.sendmail(email_from, email_to.split(","), msg.as_string())
        print(f"[notify] 이메일 전송 완료 → {email_to}")
        return True
    except Exception as e:
        print(f"[notify] 이메일 예외: {e}")
        return False


# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python notify.py '<check_result_text>'   # daily digest + trending")
        print("  python notify.py --file <path.md>        # single summary")
        print("  python notify.py --trending '<text>'     # trending only")
        sys.exit(1)

    if sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("파일 경로를 지정하세요: python notify.py --file <path.md>")
            sys.exit(1)
        post_file_to_teams(sys.argv[2])

    elif sys.argv[1] == "--trending":
        if len(sys.argv) < 3:
            print("트렌딩 텍스트를 지정하세요: python notify.py --trending '<text>'")
            sys.exit(1)
        send_trending_to_teams(sys.argv[2])

    else:
        text = sys.argv[1]

        # 1) 컨퍼런스 새 콘텐츠 다이제스트
        items = parse_items(text)
        if items:
            send_teams(items, text)
            send_email(items, text)
            saved = parse_saved_files(text)
            for fp in saved:
                post_file_to_teams(fp)
        else:
            print("[notify] 새 컨퍼런스 콘텐츠 없음, 컨퍼런스 알림 스킵")

        # 2) 트렌딩 알림 (GitHub Trending 섹션이 있으면 항상 전송)
        if "GitHub Trending" in text or "Hacker News" in text:
            send_trending_to_teams(text)

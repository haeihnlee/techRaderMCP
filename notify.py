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


def post_file_to_teams(filepath: str | Path) -> bool:
    filepath = Path(filepath)
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

    # 주요 내용 → 항목별 TextBlock (들여쓰기 하위항목 포함)
    main_point_lines = []
    for raw in _clean_for_teams(main_points).splitlines():
        if not raw.strip():
            continue
        is_sub = raw != raw.lstrip()  # 들여쓰기 여부
        content = raw.strip().lstrip("- ").strip()
        if not content:
            continue
        main_point_lines.append("  ↳ " + content if is_sub else "• " + content)

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
         "size": "Small", "color": "Accent", "weight": "Bolder"},
        {"type": "TextBlock", "text": title,
         "size": "Large", "weight": "Bolder", "wrap": True, "spacing": "Small"},
        {"type": "TextBlock", "text": summary_date,
         "isSubtle": True, "size": "Small", "spacing": "Small"},
        # 핵심 요약
        {"type": "TextBlock", "text": "📌  핵심 요약",
         "weight": "Bolder", "color": "Accent", "size": "Large", "separator": True, "spacing": "Large"},
        *[
            {"type": "TextBlock", "text": line, "wrap": True,
             "spacing": "Small" if i == 0 else "None"}
            for i, line in enumerate(summary_bullet_lines)
        ],
    ]

    if main_point_lines:
        body += [
            {"type": "TextBlock", "text": "📋  주요 발표 내용",
             "weight": "Bolder", "color": "Accent", "size": "Large", "separator": True, "spacing": "Large"},
            *[
                {"type": "TextBlock", "text": line, "wrap": True,
                 "spacing": "Small" if i == 0 else "None"}
                for i, line in enumerate(main_point_lines)
            ],
        ]

    if dev_bullet_lines:
        body += [
            {"type": "TextBlock", "text": "💡  개발자 포인트",
             "weight": "Bolder", "color": "Accent", "size": "Large", "separator": True, "spacing": "Large"},
            *[
                {"type": "TextBlock", "text": line, "wrap": True,
                 "spacing": "Small" if i == 0 else "None"}
                for i, line in enumerate(dev_bullet_lines)
            ],
        ]

    if schedule:
        sched_facts = _table_to_facts(schedule)
        sched_text = _clean_for_teams(schedule)[:400]
        body.append({"type": "TextBlock", "text": "📅  버전 / 출시 일정",
                     "weight": "Bolder", "color": "Accent", "size": "Large", "separator": True, "spacing": "Large"})
        if sched_facts:
            body.append({"type": "FactSet", "facts": sched_facts, "spacing": "Small"})
        elif sched_text:
            body.append({"type": "TextBlock", "text": sched_text,
                         "wrap": True, "spacing": "Small", "isSubtle": True})

    actions = []
    if source_url:
        actions.append({
            "type": "Action.OpenUrl",
            "title": "▶  원본 보기",
            "url": source_url,
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
        print("  python notify.py '<check_result_text>'   # daily digest")
        print("  python notify.py --file <path.md>        # single summary")
        sys.exit(1)

    if sys.argv[1] == "--file":
        if len(sys.argv) < 3:
            print("파일 경로를 지정하세요: python notify.py --file <path.md>")
            sys.exit(1)
        post_file_to_teams(sys.argv[2])
    else:
        text = sys.argv[1]
        items = parse_items(text)
        if not items:
            print("[notify] 새 콘텐츠 없음, 알림 스킵")
            sys.exit(0)

        # 1) 새 콘텐츠 목록 다이제스트
        send_teams(items, text)
        send_email(items, text)

        # 2) 저장된 요약 파일 각각 개별 게시
        saved = parse_saved_files(text)
        for fp in saved:
            post_file_to_teams(fp)

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
            # Try to extract URL (last token starting with http)
            url = ""
            parts = content.rsplit(" ", 1)
            if len(parts) == 2 and parts[1].startswith("http"):
                url = parts[1]
                content = parts[0]
            items.append({"icon": icon, "title": content, "url": url})
    return items


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
        {
            "type": "Container",
            "style": "emphasis",
            "bleed": True,
            "items": [
                {"type": "TextBlock", "text": "🎉  새 컨퍼런스 콘텐츠",
                 "size": "Large", "weight": "Bolder"},
                {"type": "TextBlock",
                 "text": f"{now}  ·  **{count}개** 발견",
                 "isSubtle": True, "spacing": "Small"},
            ]
        },
        {"type": "Container", "spacing": "Medium", "items": rows},
    ]

    payload = _adaptive_card(body)
    ok = _post_to_teams(payload)
    if ok:
        print(f"[notify] Teams 전송 완료 ({count}개)")
    return ok


# ─── Teams: single summary file ───────────────────────────────────────────────

def _extract_section(text: str, heading: str) -> str:
    result = []
    in_section = False
    for line in text.splitlines():
        if line.strip().startswith(f"## {heading}"):
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
    main_points = _extract_section(text, "주요 발표 내용")
    dev_points  = _extract_section(text, "개발자에게 중요한 포인트")
    schedule    = _extract_section(text, "출시 일정")

    # 핵심 요약 → bullet TextBlock
    bullets = "\n".join(
        "• " + l.lstrip("- ").strip()
        for l in summary_3.splitlines() if l.strip().lstrip("- ")
    )

    # 주요 내용 → FactSet
    facts = []
    for line in main_points.splitlines():
        line = line.strip().lstrip("- ")
        if not line:
            continue
        if "**" in line:
            parts = line.split("**", 2)
            if len(parts) >= 3:
                facts.append({"title": parts[1], "value": parts[2].lstrip(":").strip()})
                continue
        if facts:
            facts[-1]["value"] += " " + line
        else:
            facts.append({"title": "•", "value": line})

    # 개발자 포인트 → bullet TextBlock
    dev_bullets = "\n".join(
        "• " + l.lstrip("- ").strip()
        for l in dev_points.splitlines() if l.strip().lstrip("- ")
    )

    icon = "🎬" if source_url and "youtube" in source_url else "📰"
    conf_label = f"{icon}  {conference}" if conference else icon

    body = [
        # 헤더
        {
            "type": "Container",
            "style": "emphasis",
            "bleed": True,
            "items": [
                {"type": "TextBlock", "text": conf_label,
                 "size": "Small", "color": "Accent", "weight": "Bolder", "spacing": "None"},
                {"type": "TextBlock", "text": title,
                 "size": "Large", "weight": "Bolder", "wrap": True, "spacing": "Small"},
                {"type": "TextBlock",
                 "text": summary_date,
                 "isSubtle": True, "size": "Small", "spacing": "Small"},
            ]
        },
        # 핵심 요약
        {
            "type": "Container",
            "spacing": "Medium",
            "items": [
                {"type": "TextBlock", "text": "📌  핵심 요약",
                 "weight": "Bolder", "color": "Accent"},
                {"type": "TextBlock", "text": bullets,
                 "wrap": True, "spacing": "Small"},
            ]
        },
    ]

    if facts:
        body += [
            {"type": "Separator"},
            {
                "type": "Container",
                "items": [
                    {"type": "TextBlock", "text": "📋  주요 발표 내용", "weight": "Bolder"},
                    {"type": "FactSet", "facts": facts[:8], "spacing": "Small"},
                ]
            },
        ]

    if dev_bullets:
        body += [
            {"type": "Separator"},
            {
                "type": "Container",
                "style": "warning",
                "items": [
                    {"type": "TextBlock", "text": "💡  개발자 포인트", "weight": "Bolder"},
                    {"type": "TextBlock", "text": dev_bullets,
                     "wrap": True, "spacing": "Small"},
                ]
            },
        ]

    if schedule:
        body += [
            {"type": "Separator"},
            {
                "type": "Container",
                "items": [
                    {"type": "TextBlock", "text": "📅  출시 일정", "weight": "Bolder"},
                    {"type": "TextBlock", "text": schedule[:300],
                     "wrap": True, "spacing": "Small", "isSubtle": True},
                ]
            },
        ]

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
        send_teams(items, text)
        send_email(items, text)

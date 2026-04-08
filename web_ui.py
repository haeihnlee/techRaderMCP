"""
Conference Summaries Web UI
Run: .venv/bin/uvicorn web_ui:app --reload --port 8000
"""
import os
import re
from pathlib import Path
from datetime import datetime

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from jinja2 import Environment, BaseLoader
from markdown_it import MarkdownIt

BASE_DIR = Path(__file__).parent
SUMMARIES_DIR = BASE_DIR / "summaries"

md = MarkdownIt()

# ─── Templates ────────────────────────────────────────────────────────────────

INDEX_TEMPLATE = """
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Conference Summaries</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0f1117;
      color: #e2e8f0;
      min-height: 100vh;
    }
    header {
      background: linear-gradient(135deg, #1a1f2e 0%, #16213e 100%);
      border-bottom: 1px solid #2d3748;
      padding: 24px 32px;
      display: flex;
      align-items: center;
      gap: 16px;
    }
    header h1 { font-size: 1.5rem; font-weight: 700; color: #fff; }
    header .subtitle { font-size: 0.85rem; color: #718096; margin-top: 2px; }
    .badge {
      background: #3182ce;
      color: #fff;
      border-radius: 12px;
      padding: 2px 10px;
      font-size: 0.75rem;
      font-weight: 600;
    }
    main { max-width: 1100px; margin: 0 auto; padding: 32px 24px; }
    .search-bar {
      width: 100%;
      padding: 12px 16px;
      background: #1a202c;
      border: 1px solid #2d3748;
      border-radius: 10px;
      color: #e2e8f0;
      font-size: 0.95rem;
      margin-bottom: 32px;
      outline: none;
      transition: border-color .2s;
    }
    .search-bar::placeholder { color: #4a5568; }
    .search-bar:focus { border-color: #3182ce; }
    .conference-section { margin-bottom: 40px; }
    .conference-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 16px;
      padding-bottom: 10px;
      border-bottom: 1px solid #2d3748;
    }
    .conference-name {
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      text-transform: capitalize;
    }
    .conf-badge {
      background: #2d3748;
      color: #a0aec0;
      border-radius: 8px;
      padding: 2px 8px;
      font-size: 0.75rem;
    }
    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 16px;
    }
    .card {
      background: #1a202c;
      border: 1px solid #2d3748;
      border-radius: 12px;
      padding: 18px 20px;
      text-decoration: none;
      color: inherit;
      transition: border-color .2s, transform .15s, box-shadow .2s;
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .card:hover {
      border-color: #3182ce;
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(49,130,206,.15);
    }
    .card-title {
      font-size: 0.92rem;
      font-weight: 600;
      color: #e2e8f0;
      line-height: 1.4;
    }
    .card-date {
      font-size: 0.78rem;
      color: #4a5568;
    }
    .card-preview {
      font-size: 0.82rem;
      color: #718096;
      line-height: 1.5;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    .empty { color: #4a5568; font-size: 0.9rem; padding: 16px 0; }
    footer {
      text-align: center;
      padding: 24px;
      color: #4a5568;
      font-size: 0.8rem;
      border-top: 1px solid #1a202c;
      margin-top: 32px;
    }
  </style>
</head>
<body>
  <header>
    <div>
      <h1>Conference Summaries</h1>
      <div class="subtitle">{{ total }}개의 요약 저장됨</div>
    </div>
    <span class="badge">{{ conf_count }} conferences</span>
  </header>
  <main>
    <input class="search-bar" type="text" id="search"
           placeholder="제목 검색..." oninput="filterCards()">
    {% for conf in conferences %}
    <section class="conference-section" data-conf="{{ conf.name }}">
      <div class="conference-header">
        <span class="conference-name">{{ conf.display_name }}</span>
        <span class="conf-badge">{{ conf.entries|length }}개</span>
      </div>
      <div class="cards">
        {% for item in conf.entries %}
        <a class="card" href="/summary/{{ conf.name }}/{{ item.filename }}" data-title="{{ item.title }}">
          <div class="card-date">{{ item.date }}</div>
          <div class="card-title">{{ item.title }}</div>
          {% if item.preview %}
          <div class="card-preview">{{ item.preview }}</div>
          {% endif %}
        </a>
        {% endfor %}
      </div>
    </section>
    {% endfor %}
    {% if not conferences %}
    <div class="empty">저장된 요약이 없습니다. MCP 도구로 콘텐츠를 먼저 요약하세요.</div>
    {% endif %}
  </main>
  <footer>Conference Summarizer MCP &mdash; {{ now }}</footer>
  <script>
    function filterCards() {
      const q = document.getElementById('search').value.toLowerCase();
      document.querySelectorAll('.card').forEach(card => {
        const title = (card.dataset.title || '').toLowerCase();
        card.style.display = (!q || title.includes(q)) ? '' : 'none';
      });
      document.querySelectorAll('.conference-section').forEach(sec => {
        const visible = [...sec.querySelectorAll('.card')].some(c => c.style.display !== 'none');
        sec.style.display = visible ? '' : 'none';
      });
    }
  </script>
</body>
</html>
"""

DETAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ title }}</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #0f1117;
      color: #e2e8f0;
      min-height: 100vh;
    }
    header {
      background: #1a1f2e;
      border-bottom: 1px solid #2d3748;
      padding: 16px 32px;
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .back-btn {
      color: #63b3ed;
      text-decoration: none;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 6px;
      white-space: nowrap;
    }
    .back-btn:hover { color: #90cdf4; }
    .header-title {
      font-size: 1rem;
      font-weight: 600;
      color: #e2e8f0;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    main {
      max-width: 820px;
      margin: 40px auto;
      padding: 0 24px 60px;
    }
    .meta {
      display: flex;
      gap: 12px;
      align-items: center;
      margin-bottom: 28px;
      flex-wrap: wrap;
    }
    .meta-badge {
      background: #2d3748;
      color: #a0aec0;
      border-radius: 8px;
      padding: 3px 10px;
      font-size: 0.8rem;
    }
    /* Markdown styles */
    .content h1 { font-size: 1.7rem; font-weight: 700; color: #fff; margin: 28px 0 14px; border-bottom: 1px solid #2d3748; padding-bottom: 8px; }
    .content h2 { font-size: 1.3rem; font-weight: 700; color: #e2e8f0; margin: 24px 0 10px; }
    .content h3 { font-size: 1.1rem; font-weight: 600; color: #cbd5e0; margin: 18px 0 8px; }
    .content p { color: #cbd5e0; line-height: 1.75; margin-bottom: 14px; }
    .content ul, .content ol { color: #cbd5e0; line-height: 1.75; margin: 10px 0 14px 24px; }
    .content li { margin-bottom: 4px; }
    .content strong { color: #e2e8f0; }
    .content em { color: #a0aec0; }
    .content code {
      background: #2d3748;
      color: #68d391;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: "JetBrains Mono", "Fira Code", monospace;
      font-size: 0.88em;
    }
    .content pre {
      background: #1a202c;
      border: 1px solid #2d3748;
      border-radius: 8px;
      padding: 16px;
      overflow-x: auto;
      margin-bottom: 16px;
    }
    .content pre code { background: none; padding: 0; color: #e2e8f0; }
    .content blockquote {
      border-left: 4px solid #3182ce;
      padding: 8px 16px;
      margin: 14px 0;
      color: #a0aec0;
      background: #1a202c;
      border-radius: 0 6px 6px 0;
    }
    .content a { color: #63b3ed; }
    .content hr { border: none; border-top: 1px solid #2d3748; margin: 24px 0; }
    .content table { border-collapse: collapse; width: 100%; margin-bottom: 16px; }
    .content th, .content td { border: 1px solid #2d3748; padding: 8px 12px; text-align: left; }
    .content th { background: #1a202c; color: #e2e8f0; }
    .content td { color: #cbd5e0; }
  </style>
</head>
<body>
  <header>
    <a class="back-btn" href="/">&#8592; 목록으로</a>
    <span class="header-title">{{ title }}</span>
  </header>
  <main>
    <div class="meta">
      <span class="meta-badge">{{ conference }}</span>
      <span class="meta-badge">{{ date }}</span>
    </div>
    <div class="content">{{ body|safe }}</div>
  </main>
</body>
</html>
"""

jinja_env = Environment(loader=BaseLoader())


# ─── Helpers ──────────────────────────────────────────────────────────────────

def _parse_filename(filename: str):
    """Returns (date_str, title) from filenames like 20250514_some_title.md"""
    stem = Path(filename).stem
    m = re.match(r"^(\d{8})_(.*)", stem)
    if m:
        raw_date, rest = m.group(1), m.group(2)
        try:
            date_str = datetime.strptime(raw_date, "%Y%m%d").strftime("%Y-%m-%d")
        except ValueError:
            date_str = raw_date
        title = rest.replace("_", " ").strip()
    else:
        date_str = ""
        title = stem.replace("_", " ").strip()
    return date_str, title


def _get_preview(filepath: Path, chars: int = 160) -> str:
    """Extract first meaningful text from a markdown file."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="ignore")
        # Strip front matter / headings / blank lines
        lines = []
        for line in text.splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and not stripped.startswith("---"):
                lines.append(stripped)
            if len(" ".join(lines)) >= chars:
                break
        preview = " ".join(lines)[:chars]
        return preview + ("…" if len(preview) >= chars else "")
    except Exception:
        return ""


def _load_conferences():
    conferences = []
    total = 0
    if not SUMMARIES_DIR.exists():
        return conferences, total
    for conf_dir in sorted(SUMMARIES_DIR.iterdir()):
        if not conf_dir.is_dir():
            continue
        md_files = sorted(conf_dir.glob("*.md"), reverse=True)
        if not md_files:
            continue
        items = []
        for f in md_files:
            date_str, title = _parse_filename(f.name)
            items.append({
                "filename": f.name,
                "title": title,
                "date": date_str,
                "preview": _get_preview(f),
            })
        total += len(items)
        conferences.append({
            "name": conf_dir.name,
            "display_name": conf_dir.name.replace("_", " ").title(),
            "entries": items,
        })
    return conferences, total


# ─── Routes ───────────────────────────────────────────────────────────────────

async def index(request: Request):
    conferences, total = _load_conferences()
    tmpl = jinja_env.from_string(INDEX_TEMPLATE)
    html = tmpl.render(
        conferences=conferences,
        total=total,
        conf_count=len(conferences),
        now=datetime.now().strftime("%Y-%m-%d %H:%M"),
    )
    return HTMLResponse(html)


async def detail(request: Request):
    conference = request.path_params["conference"]
    filename = request.path_params["filename"]

    # Security: only allow alphanumeric + underscore/hyphen/dot for path components
    if not re.match(r"^[\w\-]+$", conference) or not re.match(r"^[\w\-\.]+$", filename):
        return HTMLResponse("<h1>Not Found</h1>", status_code=404)

    filepath = SUMMARIES_DIR / conference / filename
    if not filepath.exists() or filepath.suffix != ".md":
        return HTMLResponse("<h1>Not Found</h1>", status_code=404)

    # Confirm path is within SUMMARIES_DIR (no traversal)
    try:
        filepath.resolve().relative_to(SUMMARIES_DIR.resolve())
    except ValueError:
        return HTMLResponse("<h1>Forbidden</h1>", status_code=403)

    raw = filepath.read_text(encoding="utf-8", errors="ignore")
    body = md.render(raw)
    date_str, title = _parse_filename(filename)

    tmpl = jinja_env.from_string(DETAIL_TEMPLATE)
    html = tmpl.render(
        title=title,
        conference=conference.replace("_", " ").title(),
        date=date_str,
        body=body,
    )
    return HTMLResponse(html)


# ─── App ──────────────────────────────────────────────────────────────────────

app = Starlette(
    debug=False,
    routes=[
        Route("/", index),
        Route("/summary/{conference}/{filename}", detail),
    ],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web_ui:app", host="0.0.0.0", port=8000, reload=True)

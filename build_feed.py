#!/usr/bin/env python3
"""Build full-text Atom + RSS feeds from markdown drafts for Inoreader Free."""
from __future__ import annotations

import hashlib
import html
import re
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
DRAFTS = ROOT / "drafts"
OUT_ATOM = ROOT / "feeds" / "newspaper.xml"
OUT_RSS = ROOT / "feeds" / "newspaper.rss"
FEED_ID = "https://codemwk.github.io/aipaper-newspaper"
FEED_TITLE = "AiPaper 뉴스 — 미니 신문"
FEED_SUBTITLE = "최근 며칠분. 전문 읽기용 해설 기사 (양보다 질)"
AUTHOR = "AiPaper 뉴스"
RSS_SELF = "https://codemwk.github.io/aipaper-newspaper/feeds/newspaper.rss"

FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.S)


def parse_draft(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    m = FRONT_MATTER.match(text)
    if not m:
        return None
    meta_raw, body = m.group(1), m.group(2).strip()
    meta: dict[str, str] = {}
    for line in meta_raw.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    if not meta.get("title") or not meta.get("date"):
        return None
    return {
        "title": meta["title"],
        "date": meta["date"],
        "category": meta.get("category", "일반"),
        "summary": meta.get("summary", ""),
        "slug": meta.get("slug") or path.stem,
        "body_md": body,
    }


def md_to_simple_html(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    in_ul = False
    in_p = False
    in_table = False
    table_rows: list[list[str]] = []

    def close_p():
        nonlocal in_p
        if in_p:
            out.append("</p>")
            in_p = False

    def close_ul():
        nonlocal in_ul
        if in_ul:
            out.append("</ul>")
            in_ul = False

    def flush_table():
        nonlocal in_table, table_rows
        if not in_table:
            return
        close_p(); close_ul()
        out.append("<table>")
        for i, row in enumerate(table_rows):
            tag = "th" if i == 0 else "td"
            # skip markdown separator row
            if i == 1 and all(set(c.strip()) <= set("-: ") and "-" in c for c in row):
                continue
            out.append("<tr>" + "".join(f"<{tag}>{inline(c.strip())}</{tag}>" for c in row) + "</tr>")
        out.append("</table>")
        in_table = False
        table_rows = []

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush_table()
            close_p()
            close_ul()
            continue
        if "|" in line and line.strip().startswith("|"):
            close_p(); close_ul()
            cells = [c for c in line.strip().strip("|").split("|")]
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(cells)
            continue
        else:
            flush_table()
        if line.startswith("### "):
            close_p(); close_ul()
            out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("## "):
            close_p(); close_ul()
            out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("# "):
            close_p(); close_ul()
            out.append(f"<h2>{inline(line[2:])}</h2>")
        elif line.startswith("- "):
            close_p()
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline(line[2:])}</li>")
        elif re.match(r"^\d+\. ", line):
            close_p()
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline(re.sub(r'^\d+\. ', '', line))}</li>")
        else:
            close_ul()
            if not in_p:
                out.append("<p>")
                in_p = True
            else:
                out.append("<br/>")
            out.append(inline(line))
    flush_table()
    close_p(); close_ul()
    return "\n".join(out)


def inline(s: str) -> str:
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[(.+?)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def parse_date(s: str) -> datetime:
    s = s.strip()
    if len(s) == 10 and s[4] == "-":
        return datetime.strptime(s, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    if s.endswith("Z"):
        return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    if len(s) >= 25 and (s[-6] in "+-") and s[-3] == ":":
        ss = s[:-3] + s[-2:]
        return datetime.strptime(ss, "%Y-%m-%dT%H:%M:%S%z")
    return datetime.now(timezone.utc)


def atom_date(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def entry_id(slug: str, date: str) -> str:
    h = hashlib.sha1(f"{slug}:{date}".encode()).hexdigest()[:12]
    return f"{FEED_ID}/{slug}-{h}"


def entry_path(slug: str, date: str) -> str:
    """Relative path segment used in public article URLs (no .html)."""
    h = hashlib.sha1(f"{slug}:{date}".encode()).hexdigest()[:12]
    return f"{slug}-{h}"


def entry_link(slug: str, date: str) -> str:
    # Stable shareable web document URL on GitHub Pages
    return f"{FEED_ID}/{entry_path(slug, date)}/"


def content_html(d: dict) -> str:
    body_html = md_to_simple_html(d["body_md"])
    header = f'<p><em>{html.escape(d["summary"])}</em></p>\n' if d["summary"] else ""
    return (
        f"{header}"
        f'<p><strong>분류:</strong> {html.escape(d["category"])}</p>\n'
        f"{body_html}"
        f'<hr/><p>이 글은 AiPaper 뉴스가 직접 쓴 해설 기사입니다. '
        f"원문 사이트로 나가지 않아도 이 화면에서 끝까지 읽을 수 있게 전문을 넣었습니다.</p>"
    )



def article_page_html(d: dict) -> str:
    dt = parse_date(d["date"])
    from datetime import timedelta
    seoul = dt.astimezone(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M KST")
    body = content_html(d)
    title = html.escape(d["title"])
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>{title} — AiPaper 뉴스</title>
  <meta name="description" content="{html.escape(d.get('summary') or d['title'])}"/>
  <style>
    body{{font-family:system-ui,-apple-system,sans-serif;max-width:40rem;margin:2rem auto;padding:0 1.25rem 3rem;line-height:1.65;color:#111;background:#fafafa}}
    header{{margin-bottom:1.5rem}}
    .meta{{color:#555;font-size:0.95rem}}
    a{{color:#06c}}
    h1{{font-size:1.45rem;line-height:1.35;margin:0.4rem 0 0.6rem}}
    h2{{font-size:1.15rem;margin-top:1.4rem}}
    h3{{font-size:1.05rem}}
    code{{background:#eee;padding:0.1em 0.3em;border-radius:3px}}
    hr{{border:none;border-top:1px solid #ddd;margin:1.5rem 0}}
    footer{{margin-top:2rem;font-size:0.9rem;color:#666}}
  </style>
</head>
<body>
  <header>
    <div class="meta"><a href="../">AiPaper 뉴스</a> · {html.escape(d['category'])} · {seoul}</div>
    <h1>{title}</h1>
  </header>
  <article>
{body}
  </article>
  <footer>
    <p><a href="../">← 목록</a> · <a href="../feeds/newspaper.rss">RSS</a></p>
  </footer>
</body>
</html>
"""


def write_article_pages(drafts: list[dict]) -> list[Path]:
    """Write one GitHub Pages HTML document per draft (shareable web URL)."""
    written: list[Path] = []
    # Remove previous generated article dirs (slug-hash folders at repo root)
    skip = {"drafts", "feeds", "templates", ".git", "__pycache__", "node_modules"}
    for child in ROOT.iterdir():
        if not child.is_dir() or child.name in skip or child.name.startswith('.'):
            continue
        # generated article dirs look like slug-12hex
        if re.fullmatch(r".+-[0-9a-f]{12}", child.name):
            for f in child.glob("*"):
                f.unlink()
            child.rmdir()
    for d in drafts:
        rel = entry_path(d["slug"], d["date"])
        folder = ROOT / rel
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / "index.html"
        path.write_text(article_page_html(d), encoding="utf-8")
        written.append(path)
    return written


def write_index(drafts: list[dict]) -> Path:
    rows = []
    from datetime import timedelta
    seoul_tz = timezone(timedelta(hours=9))
    for d in drafts:
        dt = parse_date(d["date"]).astimezone(seoul_tz)
        href = entry_path(d["slug"], d["date"]) + "/"
        rows.append(
            f'<li><a href="{href}">{html.escape(d["title"])}</a>'
            f'<div class="meta">{html.escape(d["category"])} · {dt.strftime("%Y-%m-%d")}</div></li>'
        )
    html_doc = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8"/>
  <title>AiPaper 뉴스 — 미니 신문</title>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <style>
    body{{font-family:system-ui,sans-serif;max-width:40rem;margin:2rem auto;padding:0 1rem 3rem;line-height:1.5;color:#111}}
    code{{background:#f4f4f4;padding:.1em .3em;border-radius:3px}}
    a{{color:#06c}}
    .meta{{color:#666;font-size:0.9rem}}
    li{{margin:0.85rem 0}}
  </style>
</head>
<body>
  <h1>AiPaper 뉴스</h1>
  <p>최근 며칠분 전문 해설. Inoreader / 웹문서 / 공유 모두 같은 본문입니다.</p>
  <p>RSS: <code>https://codemwk.github.io/aipaper-newspaper/feeds/newspaper.rss</code>
     · <a href="feeds/newspaper.rss">열기</a></p>
  <h2>최근 기사</h2>
  <ol>
{chr(10).join(rows)}
  </ol>
</body>
</html>
"""
    path = ROOT / "index.html"
    path.write_text(html_doc, encoding="utf-8")
    return path


def seoul_today():
    # Asia/Seoul = UTC+9 (no DST)
    from datetime import timedelta
    return (datetime.now(timezone.utc) + timedelta(hours=9)).date()


def load_drafts(*, keep_days: int = 3) -> list[dict]:
    """Load drafts for a rolling Seoul-date window.

    keep_days=3: today + previous 2 days — enough catch-up if the reader was busy,
    without accumulating the full archive.
    """
    from datetime import timedelta
    drafts = []
    today = seoul_today()
    oldest = today - timedelta(days=max(keep_days, 1) - 1)
    seoul_tz = timezone(timedelta(hours=9))
    for path in sorted(DRAFTS.glob("*.md")):
        d = parse_draft(path)
        if not d:
            continue
        local = parse_date(d["date"]).astimezone(seoul_tz).date()
        if local < oldest or local > today:
            continue
        drafts.append(d)
    drafts.sort(key=lambda d: parse_date(d["date"]), reverse=True)
    return drafts


def build_atom(drafts: list[dict]) -> Path:
    updated = atom_date(parse_date(drafts[0]["date"])) if drafts else atom_date(datetime.now(timezone.utc))
    parts = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom">',
        f"<title>{escape(FEED_TITLE)}</title>",
        f"<subtitle>{escape(FEED_SUBTITLE)}</subtitle>",
        f'<link href="{FEED_ID}/feeds/newspaper.xml" rel="self" type="application/atom+xml"/>',
        f'<link href="{FEED_ID}/" rel="alternate" type="text/html"/>',
        f"<id>{FEED_ID}</id>",
        f"<updated>{updated}</updated>",
        f"<author><name>{escape(AUTHOR)}</name></author>",
    ]
    for d in drafts[:40]:
        dt = parse_date(d["date"])
        content = content_html(d)
        link = entry_link(d["slug"], d["date"])
        parts += [
            "<entry>",
            f"<title>{escape(d['title'])}</title>",
            f"<id>{entry_id(d['slug'], d['date'])}</id>",
            f'<link href="{link}" rel="alternate" type="text/html"/>',
            f"<updated>{atom_date(dt)}</updated>",
            f"<published>{atom_date(dt)}</published>",
            f'<category term="{escape(d["category"])}"/>',
        ]
        if d["summary"]:
            parts.append(f"<summary>{escape(d['summary'])}</summary>")
        parts += [
            f'<content type="html">{escape(content)}</content>',
            "</entry>",
        ]
    parts.append("</feed>")
    OUT_ATOM.parent.mkdir(parents=True, exist_ok=True)
    OUT_ATOM.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return OUT_ATOM


def build_rss(drafts: list[dict]) -> Path:
    now = datetime.now(timezone.utc)
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom">',
        "<channel>",
        f"<title>{escape(FEED_TITLE)}</title>",
        f"<link>{FEED_ID}/</link>",
        f"<description>{escape(FEED_SUBTITLE)}</description>",
        "<language>ko</language>",
        f'<atom:link href="{RSS_SELF}" rel="self" type="application/rss+xml"/>',
        f"<lastBuildDate>{format_datetime(now)}</lastBuildDate>",
        f"<managingEditor>{escape(AUTHOR)}</managingEditor>",
    ]
    for d in drafts[:40]:
        dt = parse_date(d["date"])
        link = entry_link(d["slug"], d["date"])
        content = content_html(d)
        parts += [
            "<item>",
            f"<title>{escape(d['title'])}</title>",
            f"<link>{link}</link>",
            f'<guid isPermaLink="false">{entry_id(d["slug"], d["date"])}</guid>',
            f"<pubDate>{format_datetime(dt.astimezone(timezone.utc))}</pubDate>",
            f"<category>{escape(d['category'])}</category>",
        ]
        if d["summary"]:
            parts.append(f"<description>{escape(d['summary'])}</description>")
        else:
            parts.append(f"<description>{escape(d['title'])}</description>")
        parts += [
            f"<content:encoded><![CDATA[{content}]]></content:encoded>",
            "</item>",
        ]
    parts += ["</channel>", "</rss>"]
    OUT_RSS.parent.mkdir(parents=True, exist_ok=True)
    OUT_RSS.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return OUT_RSS


def build():
    drafts = load_drafts()
    pages = write_article_pages(drafts)
    index = write_index(drafts)
    atom = build_atom(drafts)
    rss = build_rss(drafts)
    return atom, rss, pages, index


if __name__ == "__main__":
    atom, rss, pages, index = build()
    print(f"Wrote {atom} ({atom.stat().st_size} bytes)")
    print(f"Wrote {rss} ({rss.stat().st_size} bytes)")
    print(f"Wrote {len(pages)} article pages + {index}")

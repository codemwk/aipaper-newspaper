#!/usr/bin/env python3
"""Build a full-text Atom feed from markdown drafts for Inoreader Free."""
from __future__ import annotations

import hashlib
import html
import re
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent
DRAFTS = ROOT / "drafts"
OUT = ROOT / "feeds" / "newspaper.xml"
FEED_ID = "https://codemwk.github.io/aipaper-newspaper"
FEED_TITLE = "AiPaper 뉴스 — 미니 신문"
FEED_SUBTITLE = "양보다 질. 전문 읽기용 해설 기사"
AUTHOR = "AiPaper 뉴스"

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

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            close_p()
            close_ul()
            continue
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
        else:
            close_ul()
            if not in_p:
                out.append("<p>")
                in_p = True
            else:
                out.append("<br/>")
            out.append(inline(line))
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
    # +09:00 style
    if len(s) >= 25 and (s[-6] in "+-") and s[-3] == ":":
        ss = s[:-3] + s[-2:]
        return datetime.strptime(ss, "%Y-%m-%dT%H:%M:%S%z")
    return datetime.now(timezone.utc)


def atom_date(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def entry_id(slug: str, date: str) -> str:
    h = hashlib.sha1(f"{slug}:{date}".encode()).hexdigest()[:12]
    return f"{FEED_ID}/{slug}-{h}"


def build() -> Path:
    drafts = []
    for p in sorted(DRAFTS.glob("*.md")):
        d = parse_draft(p)
        if d:
            drafts.append(d)
    drafts.sort(key=lambda d: parse_date(d["date"]), reverse=True)
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

    for d in drafts[:30]:
        dt = parse_date(d["date"])
        body_html = md_to_simple_html(d["body_md"])
        header = f'<p><em>{html.escape(d["summary"])}</em></p>\n' if d["summary"] else ""
        content = (
            f"{header}"
            f'<p><strong>분류:</strong> {html.escape(d["category"])}</p>\n'
            f"{body_html}"
            f'<hr/><p>이 글은 AiPaper 뉴스가 직접 쓴 해설 기사입니다. '
            f"원문 사이트로 나가지 않아도 이 화면에서 끝까지 읽을 수 있게 전문을 넣었습니다.</p>"
        )
        parts += [
            "<entry>",
            f"<title>{escape(d['title'])}</title>",
            f"<id>{entry_id(d['slug'], d['date'])}</id>",
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
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(parts) + "\n", encoding="utf-8")
    return OUT


if __name__ == "__main__":
    path = build()
    print(f"Wrote {path} ({path.stat().st_size} bytes)")

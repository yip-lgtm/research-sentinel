#!/usr/bin/env python3
"""人性化練習哨兵 — 靜態站建置器（GitHub Pages）

由 sentinel repo 的 reports/ + knowledge/ 生成 yip-lgtm.github.io/R&D/ 靜態站：
  R&D/index.html              — 報告索引（最新在前）
  R&D/reports/<stamp>.html    — 每份報告獨立頁
  R&D/knowledge/index.html    — 知識庫章節索引
  R&D/knowledge/<slug>.html   — 每個知識庫章節
  R&D/feed.json               — 機器可讀索引

設計原則：
  - 決定性輸出：同樣輸入 → 同樣 bytes（避免無謂 diff）
  - 只讀 sentinel repo，唔改任何報告正文
  - 冇 markdown 依賴就用內建 mini renderer（表格、粗體、連結、程式碼）
"""
import html
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

HERMES_HOME = Path(os.environ.get("HERMES_HOME", "/root/.hermes"))
REPO = HERMES_HOME / "sentinel"
PAGES_REPO = Path(os.environ.get("PAGES_REPO", "/root/gh-pages"))
OUT = PAGES_REPO / "R&D"

REPORTS = REPO / "reports"
KNOWLEDGE = REPO / "knowledge"
SECTIONS = KNOWLEDGE / "sections"
INDEX_JSON = REPORTS / "index.json"
TOPICS_JSON = KNOWLEDGE / "topics.json"

# ── 樣式：沿用 yipmma 嘅黑底卡片風格 ───────────────────────────────
CSS = """
*{box-sizing:border-box}
html,body{margin:0;background:#000;color:#fff;font-family:-apple-system,BlinkMacSystemFont,"Noto Sans TC","PingFang HK",sans-serif;-webkit-font-smoothing:antialiased}
a{color:#fff}
.wrap{max-width:42rem;margin:0 auto;padding:24px 16px 80px}
.kicker{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:#8a8a8a;margin:0}
h1{font-size:32px;margin:6px 0 8px;letter-spacing:-.03em;font-weight:600;line-height:1.2}
h2{font-size:20px;margin:0 0 4px;letter-spacing:-.01em}
h3{font-size:15px;margin:28px 0 8px;color:#d8d8d8;font-weight:600;letter-spacing:.02em}
.lead,.en{color:#9a9a9a;font-size:14px;line-height:1.65}
.card{border:1px solid #222;border-radius:18px;padding:18px;margin:14px 0;background:#0c0c0c;display:block;text-decoration:none}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.meta{font-size:12px;color:#6e6e6e;margin:2px 0 0}
.tag{display:inline-block;font-size:10px;letter-spacing:.08em;text-transform:uppercase;border:1px solid #2a2a2a;border-radius:999px;padding:2px 9px;color:#8a8a8a;margin-right:6px}
.tag.ok{border-color:#1e4d2b;color:#5fd08a}
.tag.warn{border-color:#4a3a1e;color:#d0a85f}
.tag.bad{border-color:#4d1e1e;color:#d05f5f}
.chips{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.chip{border:1px solid #222;border-radius:14px;padding:12px;background:#0c0c0c}
.chip b{display:block;font-size:12px;color:#8a8a8a;font-weight:500;margin-bottom:3px}
.rule{height:1px;background:#1c1c1c;margin:28px 0}
ol,ul{padding-left:1.15em;margin:10px 0}
li{margin:7px 0;line-height:1.7;font-size:15px}
p{line-height:1.75;margin:10px 0}
strong{color:#fff;font-weight:600}
em{color:#b8b8b8}
code{background:#161616;border:1px solid #242424;border-radius:6px;padding:1px 6px;font-size:13px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
pre{background:#0a0a0a;border:1px solid #222;border-radius:12px;padding:14px;overflow:auto}
pre code{background:none;border:0;padding:0}
blockquote{border-left:2px solid #333;margin:12px 0;padding:2px 0 2px 14px;color:#aaa}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:13px}
th,td{border:1px solid #242424;padding:7px 9px;text-align:left;line-height:1.5}
th{background:#111;color:#cfcfcf;font-weight:600}
td:nth-child(n+2){font-variant-numeric:tabular-nums}
hr{border:0;height:1px;background:#1c1c1c;margin:26px 0}
.src{font-size:12.5px;line-height:1.6;color:#9a9a9a;word-break:break-word}
.src a{color:#7fb0ff;text-decoration:none}
.src a:hover{text-decoration:underline}
.nav{position:fixed;left:0;right:0;bottom:0;background:rgba(0,0,0,.94);backdrop-filter:blur(8px);border-top:1px solid #1e1e1e;display:grid;grid-template-columns:repeat(3,1fr);text-align:center;padding:8px 0 14px;font-size:11px}
.nav a{color:#888;text-decoration:none;padding:6px}
.nav a.on{color:#fff}
@media(max-width:480px){.chips{grid-template-columns:1fr}h1{font-size:27px}}
"""


def esc(s) -> str:
    return html.escape(str(s), quote=False)


def esc_url(u: str) -> str:
    """URL 入面嘅 & 必須 escape 成 &amp;，否則 HTML 驗證器會當成壞 markup。"""
    return html.escape(str(u), quote=True)


def md_to_html(md: str) -> str:
    """極簡 markdown → HTML。支援表格、標題、粗體、斜體、連結、程式碼、清單、引用。

    刻意唔用外部 markdown lib（避免 Pages build 環境依賴），而且輸出要決定性。
    """
    lines = md.split("\n")
    out = []
    i = 0
    in_list = None  # 'ul' | 'ol'

    def close_list():
        nonlocal in_list
        if in_list:
            out.append(f"</{in_list}>")
            in_list = None

    def inline(t: str) -> str:
        # 先抽 inline code，避免被後續規則搞壞
        codes = []

        def stash(m):
            codes.append(m.group(1))
            return f"\x00CODE{len(codes) - 1}\x00"

        t = re.sub(r"`([^`]+)`", stash, t)
        t = esc(t)
        t = re.sub(r"\[([^\]]+)\]\((https?://[^\s)]+)\)", lambda m: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (esc_url(m.group(2)), m.group(1)), t)
        t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", t)
        t = re.sub(r"(?<![\w/])(https?://[^\s<>\"')]+)", lambda m: '<a href="%s" target="_blank" rel="noopener">%s</a>' % (esc_url(m.group(1)), m.group(1)), t)
        for idx, c in enumerate(codes):
            t = t.replace(f"\x00CODE{idx}\x00", f"<code>{esc(c)}</code>")
        return t

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # code fence
        if stripped.startswith("```"):
            close_list()
            i += 1
            buf = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append("<pre><code>" + esc("\n".join(buf)) + "</code></pre>")
            continue

        # table
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1]):
            close_list()
            header = [c.strip() for c in stripped.strip("|").split("|")]
            i += 2
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append("<table><thead><tr>" + "".join(f"<th>{inline(h)}</th>" for h in header) + "</tr></thead><tbody>")
            for r_ in rows:
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r_) + "</tr>")
            out.append("</tbody></table>")
            continue

        # headings
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            close_list()
            lvl = min(len(m.group(1)), 6)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            i += 1
            continue

        # hr
        if re.match(r"^(-{3,}|\*{3,})$", stripped):
            close_list()
            out.append("<hr>")
            i += 1
            continue

        # blockquote
        if stripped.startswith(">"):
            close_list()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append("<blockquote>" + inline(" ".join(buf)) + "</blockquote>")
            continue

        # list
        m_ul = re.match(r"^[-*+]\s+(.*)$", stripped)
        m_ol = re.match(r"^\d+[.)]\s+(.*)$", stripped)
        if m_ul or m_ol:
            want = "ol" if m_ol else "ul"
            if in_list != want:
                close_list()
                out.append(f"<{want}>")
                in_list = want
            out.append(f"<li>{inline((m_ul or m_ol).group(1))}</li>")
            i += 1
            continue

        close_list()
        if stripped:
            out.append(f"<p>{inline(stripped)}</p>")
        i += 1

    close_list()
    return "\n".join(out)


BUILD_STAMP = "—"


def page(title: str, body: str, nav_active: str = "") -> str:
    nav_items = [("home", "研究"), ("reports", "報告"), ("knowledge", "知識庫")]
    nav = ""
    for key, label in nav_items:
        href = "/R&amp;D/" if key == "home" else f"/R&amp;D/{key}/"
        cls = " class=\"on\"" if key == nav_active else ""
        nav += f'<a href="{href}"{cls}>{label}</a>'
    return f"""<!doctype html>
<html lang="zh-HK">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{esc(title)}</title>
<meta name="theme-color" content="#000000" />
<meta property="og:title" content="{esc(title)}" />
<meta property="og:type" content="website" />
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
{body}
</div>
<nav class="nav">{nav}</nav>
</body>
</html>
"""


def parse_report_meta(text: str) -> dict:
    """抽報告標題與時間。

    標題行喺唔同報告有唔同寫法，全部要支援：
      - `## 標題：X`   /  `**標題：X**`  /  `標題：X`
      - `# Title: Y`    /  `**Title: Y**`
    之前淨係匹配 `^## 標題：` 同 `^# Title:`，令用粗體寫標題嘅報告
    （例如 2026-10-23-00）title_zh/title_en 全部抽唔到 → 站上標題同
    feed.json 顯示為空字串。
    """
    meta = {"title_zh": "", "title_en": "", "stamp": "", "body": text}

    def _find(pattern: str) -> str:
        m = re.search(pattern, text, re.M)
        return m.group(1).strip() if m else ""

    # 標題：中文 —— 容許 ## / # / ** / 空白 前綴
    meta["title_zh"] = _find(r"^[ \t]*(?:#{1,3}[ \t]*)?\*{0,2}[ \t]*標題[ \t]*[：:][ \t]*(.+?)[ \t]*\*{0,2}[ \t]*$")
    # Title: 英文
    meta["title_en"] = _find(r"^[ \t]*(?:#{1,3}[ \t]*)?\*{0,2}[ \t]*Title[ \t]*[：:][ \t]*(.+?)[ \t]*\*{0,2}[ \t]*$")
    # `> 主題：X` / `> Topic: Y`（引用格式標題，早期報告用）
    if not meta["title_zh"]:
        meta["title_zh"] = _find(r"^[ \t]*>[ \t]*\*{0,2}[ \t]*主題[ \t]*[：:][ \t]*(.+?)[ \t]*\*{0,2}[ \t]*$")
    if not meta["title_en"]:
        meta["title_en"] = _find(r"^[ \t]*>[ \t]*\*{0,2}[ \t]*Topic[ \t]*[：:][ \t]*(.+?)[ \t]*\*{0,2}[ \t]*$")
    # `# 科研哨兵報告｜2026-10-22 14:00 UTC` 呢類通用標題 → 抽內嵌嘅主題行
    if not meta["title_zh"] or meta["title_zh"].startswith("科研哨兵報告"):
        m2 = _find(r"^[ \t]*>[ \t]*\*{0,2}[ \t]*主題[ \t]*[：:][ \t]*(.+?)[ \t]*\*{0,2}[ \t]*$")
        if m2:
            meta["title_zh"] = m2
    if not meta["title_en"]:
        m2 = _find(r"^[ \t]*>[ \t]*\*{0,2}[ \t]*Topic[ \t]*[：:][ \t]*(.+?)[ \t]*\*{0,2}[ \t]*$")
        if m2:
            meta["title_en"] = m2

    m = re.search(r"（(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\s*UTC）", text)
    if m:
        meta["stamp"] = m.group(1)
    if not meta["title_zh"]:
        m = re.search(r"^#\s+(.+)$", text, re.M)
        if m:
            meta["title_zh"] = m.group(1).strip()
    return meta


def report_body_md(text: str) -> str:
    """報告頁模板已經渲染 kicker/h1/lead/meta，正文唔應該重複標題區。

    規則：從第一個 `### ` 小節開始；如果冇，就剝走最前面嘅 `#` 標題行同分隔線。
    """
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith("### "):
            return "\n".join(lines[i:]).strip()
    # fallback：剝走開頭連續嘅標題行 / 分隔線 / 空行
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s == "" or s.startswith("#") or re.match(r"^(-{3,}|\*{3,})$", s):
            i += 1
            continue
        break
    return "\n".join(lines[i:]).strip()


def report_slug(path: Path) -> str:
    return path.stem


def load_index() -> dict:
    if INDEX_JSON.exists():
        try:
            return json.loads(INDEX_JSON.read_text())
        except Exception:
            pass
    return {"reports": {}}


def load_topics() -> list:
    if TOPICS_JSON.exists():
        try:
            data = json.loads(TOPICS_JSON.read_text())
            return data.get("topics", [])
        except Exception:
            pass
    return []


def build_index(reports: list, topics: list, state: dict) -> str:
    cards = []
    for r in reports:
        g = r["gate"]
        if g.get("pass"):
            tag = '<span class="tag ok">通過</span>'
        elif g.get("fails"):
            tag = '<span class="tag bad">未過閘</span>'
        else:
            tag = '<span class="tag warn">未評</span>'
        stamp = r["stamp"]
        cards.append(f"""<a class="card" href="/R&amp;D/reports/{esc(stamp)}.html">
  <div class="row"><h2>{esc(r['title_zh'] or stamp)}</h2>{tag}</div>
  <p class="meta">{esc(stamp)} UTC · {r['cjk']} 中文字 · {r['bytes']} bytes · {r['sources']} 來源</p>
  <p class="lead">{esc(r['title_en'])}</p>
</a>""")

    topic_chips = []
    for t in topics:
        cov = t.get("coverage", 0)
        pct = int(round(float(cov) * 100)) if isinstance(cov, (int, float)) else 0
        status = t.get("status", "")
        topic_chips.append(f"""<div class="chip"><b>{esc(t.get('title', ''))}</b>{esc(t.get('domain', ''))} · 覆蓋 {pct}% · {esc(status)}</div>""")

    lvl = state.get("level", "?")
    hrs = state.get("lifespan_hours", "?")
    topics_json = json.dumps(topics, ensure_ascii=False, indent=1)
    topics_body = md_to_html("```json\n" + topics_json + "\n```")

    body = f"""<p class="kicker">RESEARCH &amp; DEVELOPMENT</p>
<h1>科研哨兵 · R&D</h1>
<p class="sub">人性化練習哨兵 — 每小時一次判斷與表達的練習</p>
<p class="lead">每小時一份可追溯的科研報告。主題涵蓋工程、能源、健康暴露、公共政策與基礎設施。<br>All findings are traceable to primary sources.</p>

<div class="chips" style="margin-top:20px">
  <div class="chip"><b>報告</b>{len(reports)} 份</div>
  <div class="chip"><b>知識庫</b>{len(list(SECTIONS.glob('*.md')))} 章</div>
  <div class="chip"><b>等級</b>L{esc(str(lvl))}</div>
  <div class="chip"><b>剩餘壽命</b>{esc(str(hrs))} 小時</div>
</div>

<div class="rule"></div>

<p class="kicker">最新報告 / LATEST</p>
{''.join(cards[:6])}

<p style="margin-top:24px"><a href="/R&amp;D/reports/" style="font-size:14px;color:#7fb0ff;text-decoration:none">睇全部 {len(reports)} 份報告 →</a></p>

<div class="rule"></div>

<p class="kicker">知識庫 / KNOWLEDGE</p>
<div class="chips">
{''.join(topic_chips)}
</div>
<p style="margin-top:24px"><a href="/R&amp;D/knowledge/" style="font-size:14px;color:#7fb0ff;text-decoration:none">打開知識庫 →</a></p>

<div class="rule"></div>

<p class="kicker">覆蓋登記 / TOPIC REGISTRY</p>
{topics_body}

<p class="meta" style="margin-top:30px">最後更新：{esc(BUILD_STAMP)} UTC · 自動建置，勿手改</p>"""
    return page("科研哨兵 · R&D", body, nav_active="home")


def build_report_page(r: dict) -> str:
    stamp = r["stamp"]
    meta = r["meta"]
    g = r["gate"]
    gate_line = "通過品質閘" if g.get("pass") else ("未過品質閘：" + "；".join(g.get("fails", [])) if g.get("fails") else "未評")
    body = f"""<p class="kicker">報告 / REPORT · {esc(stamp)}</p>
<h1>{esc(meta['title_zh'] or stamp)}</h1>
<p class="lead">{esc(meta['title_en'])}</p>
<p class="meta">{esc(meta.get('stamp', ''))} UTC · {r['cjk']} 中文字 · {r['bytes']} bytes · {r['sources']} 來源 · {esc(gate_line)}</p>
<div class="rule"></div>
{r['html']}
<div class="rule"></div>
<p><a href="/R&amp;D/reports/" style="font-size:14px;color:#7fb0ff;text-decoration:none">← 返回報告索引</a></p>
<p class="meta" style="margin-top:30px">自動建置於 {esc(stamp)} UTC · 來源：research-sentinel/reports/{esc(stamp)}.md</p>"""
    return page(f"{meta['title_zh'] or stamp} · 科研哨兵", body, nav_active="reports")


def build_reports_index(reports: list) -> str:
    cards = []
    for r in reports:
        g = r["gate"]
        tag = '<span class="tag ok">通過</span>' if g.get("pass") else ('<span class="tag bad">未過閘</span>' if g.get("fails") else '<span class="tag warn">未評</span>')
        cards.append(f"""<a class="card" href="/R&amp;D/reports/{esc(r['stamp'])}.html">
  <div class="row"><h2>{esc(r['title_zh'] or r['stamp'])}</h2>{tag}</div>
  <p class="meta">{esc(r['stamp'])} UTC · {r['cjk']} 中文字 · {r['bytes']} bytes · {r['sources']} 來源</p>
  <p class="lead">{esc(r['title_en'])}</p>
</a>""")
    body = f"""<p class="kicker">ARCHIVE / 報告索引</p>
<h1>全部報告</h1>
<p class="lead">共 {len(reports)} 份，按時間倒序。新報告每小時自動上架。</p>
<div class="rule"></div>
{''.join(cards) if cards else '<p class="lead">未有報告。</p>'}
<div class="rule"></div>
<p><a href="/R&amp;D/" style="font-size:14px;color:#7fb0ff;text-decoration:none">← 返回首頁</a></p>"""
    return page("報告索引 · 科研哨兵", body, nav_active="reports")


def build_knowledge_index(sections: list) -> str:
    cards = []
    for s in sections:
        cards.append(f"""<a class="card" href="/R&amp;D/knowledge/{esc(s['slug'])}.html">
  <div class="row"><h2>{esc(s['title'])}</h2><span class="tag">{esc(s['bytes'])} B</span></div>
  <p class="meta">{esc(s['h2'])} 個小節</p>
  <p class="lead">{esc(s['desc'])}</p>
</a>""")
    body = f"""<p class="kicker">KNOWLEDGE BASE / 知識庫</p>
<h1>知識庫</h1>
<p class="lead">長期累積的研究筆記。每章節都係持久化落磁碟，唔依賴單次對話記憶。</p>
<div class="rule"></div>
{''.join(cards) if cards else '<p class="lead">未有章節。</p>'}
<div class="rule"></div>
<p><a href="/R&amp;D/" style="font-size:14px;color:#7fb0ff;text-decoration:none">← 返回首頁</a></p>"""
    return page("知識庫 · 科研哨兵", body, nav_active="knowledge")


def build_knowledge_page(s: dict) -> str:
    body = f"""<p class="kicker">KNOWLEDGE / 章節</p>
<h1>{esc(s['title'])}</h1>
<p class="meta">{esc(s['bytes'])} bytes · {esc(s['h2'])} 個小節</p>
<div class="rule"></div>
{s['html']}
<div class="rule"></div>
<p><a href="/R&amp;D/knowledge/" style="font-size:14px;color:#7fb0ff;text-decoration:none">← 返回知識庫</a></p>
<p class="meta" style="margin-top:30px">自動建置於 {esc(BUILD_STAMP)} UTC · 來源：research-sentinel/knowledge/sections/{esc(s['slug'])}.md</p>"""
    return page(f"{s['title']} · 知識庫", body, nav_active="knowledge")


def collect_reports(index: dict) -> list:
    reports = []
    for path in sorted(REPORTS.glob("*.md")):
        if path.name == "index.md":
            continue
        stamp = path.stem
        g = index.get("reports", {}).get(stamp, {})
        # 未過品質閘嘅草稿唔上架（archived / gate_pass=False）
        if g.get("archived") or (g and g.get("gate_pass") is False):
            continue
        text = path.read_text(errors="ignore")
        meta = parse_report_meta(text)
        if "pass" not in g and "gate_pass" in g:
            g = dict(g)
            g["pass"] = bool(g["gate_pass"])
        cjk = sum(1 for ch in text if "\u4e00" <= ch <= "\u9fff")
        srcs = len(re.findall(r"https?://", text))
        reports.append({
            "stamp": stamp,
            "title_zh": meta["title_zh"],
            "title_en": meta["title_en"],
            "meta": meta,
            "gate": g,
            "cjk": cjk,
            "bytes": len(text.encode("utf-8")),
            "sources": srcs,
            "html": md_to_html(report_body_md(text)),
        })
    reports.sort(key=lambda r: r["stamp"], reverse=True)
    return reports


def collect_sections() -> list:
    out = []
    if not SECTIONS.is_dir():
        return out
    for path in sorted(SECTIONS.glob("*.md")):
        text = path.read_text(errors="ignore")
        title = path.stem
        m = re.search(r"^#\s+(.+)$", text, re.M)
        if m:
            title = m.group(1).strip()
        desc = ""
        for line in text.split("\n"):
            s = line.strip()
            if s and not s.startswith("#") and not s.startswith("|") and not s.startswith("```"):
                desc = s
                break
        out.append({
            "slug": path.stem,
            "title": title,
            "desc": desc[:180],
            "bytes": len(text.encode("utf-8")),
            "h2": len(re.findall(r"^##\s+", text, re.M)),
            "html": md_to_html(text),
        })
    return out


def write_if_changed(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(errors="ignore") == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    if not REPO.is_dir():
        print(f"SKIP: sentinel repo not found at {REPO}")
        return 0
    OUT.mkdir(parents=True, exist_ok=True)

    index = load_index()
    topics = load_topics()
    state = {}
    sp = REPO / "state.json"
    if sp.exists():
        try:
            state = json.loads(sp.read_text())
        except Exception:
            state = {}

    reports = collect_reports(index)
    sections = collect_sections()
    global BUILD_STAMP
    BUILD_STAMP = reports[0]["stamp"] if reports else "—"

    changed = []

    # 主索引
    p = OUT / "index.html"
    if write_if_changed(p, build_index(reports, topics, state)):
        changed.append(str(p))

    # 報告索引 + 各報告頁
    p = OUT / "reports" / "index.html"
    if write_if_changed(p, build_reports_index(reports)):
        changed.append(str(p))
    for r in reports:
        p = OUT / "reports" / f"{r['stamp']}.html"
        if write_if_changed(p, build_report_page(r)):
            changed.append(str(p))

    # 知識庫
    p = OUT / "knowledge" / "index.html"
    if write_if_changed(p, build_knowledge_index(sections)):
        changed.append(str(p))
    for s in sections:
        p = OUT / "knowledge" / f"{s['slug']}.html"
        if write_if_changed(p, build_knowledge_page(s)):
            changed.append(str(p))

    # 清 stale 頁面：reports/*.html 對應唔返任何 .md 就刪（測試報告殘留）
    rep_dir = OUT / "reports"
    if rep_dir.is_dir():
        live = {f"{r['stamp']}.html" for r in reports} | {"index.html"}
        for old in rep_dir.glob("*.html"):
            if old.name not in live:
                old.unlink()
                changed.append(f"{old} (removed stale)")

    # feed.json（機器可讀）
    feed = {
        "generated_utc": BUILD_STAMP,
        "reports": [
            {
                "stamp": r["stamp"],
                "title_zh": r["title_zh"],
                "title_en": r["title_en"],
                "url": f"/R&D/reports/{r['stamp']}.html",
                "cjk": r["cjk"],
                "bytes": r["bytes"],
                "sources": r["sources"],
                "gate_pass": bool(r["gate"].get("pass")),
            }
            for r in reports
        ],
        "knowledge": [
            {"slug": s["slug"], "title": s["title"], "url": f"/R&D/knowledge/{s['slug']}.html", "bytes": s["bytes"]}
            for s in sections
        ],
    }
    p = OUT / "feed.json"
    if write_if_changed(p, json.dumps(feed, ensure_ascii=False, indent=1) + "\n"):
        changed.append(str(p))

    print(f"build_site: {len(reports)} reports, {len(sections)} knowledge sections, {len(changed)} files changed")
    for c in changed[:20]:
        print("  changed:", c)
    return 0


if __name__ == "__main__":
    sys.exit(main())

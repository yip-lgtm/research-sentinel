#!/usr/bin/env python3
"""Multi-backend web search: duckduckgo html, bing, mojeek, brave."""
import sys, urllib.request, urllib.parse, re, html, gzip, io, os, json

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

def get(url, timeout=25):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate",
    })
    with urllib.request.urlopen(req, timeout=timeout) as r:
        data = r.read()
        if r.headers.get("Content-Encoding") == "gzip":
            data = gzip.decompress(data)
        return data.decode("utf-8", "replace")

def ddg(q):
    u = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q)
    t = get(u)
    out = []
    for m in re.finditer(r'<a[^>]+class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', t, re.S):
        link, title = m.group(1), re.sub(r"<[^>]+>", "", m.group(2))
        out.append((html.unescape(title).strip(), html.unescape(link)))
    if not out:
        for m in re.finditer(r'<a[^>]+class="result-link"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', t, re.S):
            out.append((re.sub(r"<[^>]+>", "", m.group(2)).strip(), m.group(1)))
    return out

def ddglite(q):
    u = "https://lite.duckduckgo.com/lite/?q=" + urllib.parse.quote(q)
    t = get(u)
    out = []
    for m in re.finditer(r'<a[^>]+class="result-link"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', t, re.S):
        out.append((re.sub(r"<[^>]+>", "", m.group(2)).strip(), html.unescape(m.group(1))))
    if not out:
        for m in re.finditer(r'href="(http[^"]+)"[^>]*class="result-link"', t):
            out.append(("", html.unescape(m.group(1))))
    return out

def mojeek(q):
    u = "https://www.mojeek.com/search?q=" + urllib.parse.quote(q)
    t = get(u)
    out = []
    for m in re.finditer(r'<a[^>]+class="ob"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', t, re.S):
        out.append((re.sub(r"<[^>]+>", "", m.group(2)).strip(), html.unescape(m.group(1))))
    return out

def bing(q):
    u = "https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&count=20"
    t = get(u)
    out = []
    for m in re.finditer(r'<h2><a[^>]+href="([^"]+)"[^>]*>(.*?)</a></h2>', t, re.S):
        out.append((re.sub(r"<[^>]+>", "", m.group(2)).strip(), html.unescape(m.group(1))))
    return out

def brave(q):
    u = "https://search.brave.com/search?q=" + urllib.parse.quote(q)
    t = get(u)
    out = []
    for m in re.finditer(r'<a[^>]+href="(https?://[^"]+)"[^>]*class="[^"]*result-header[^"]*"', t):
        out.append(("", html.unescape(m.group(1))))
    if not out:
        for m in re.finditer(r'href="(https?://(?!search\.brave)[^"]+)"[^>]*>\s*<div[^>]*class="[^"]*title', t):
            out.append(("", html.unescape(m.group(1))))
    return out

BACKENDS = {"ddg": ddg, "ddglite": ddglite, "mojeek": mojeek, "bing": bing, "brave": brave}

if __name__ == "__main__":
    q = sys.argv[1]
    order = sys.argv[2].split(",") if len(sys.argv) > 2 else ["ddg", "ddglite", "mojeek", "bing", "brave"]
    for name in order:
        try:
            res = BACKENDS[name](q)
        except Exception as e:
            print(f"[{name}] ERR {e}")
            continue
        print(f"[{name}] {len(res)} results")
        for t, l in res[:12]:
            print(f"  - {t[:110]} :: {l[:180]}")
        if res:
            break

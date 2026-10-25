import sys, urllib.parse, requests, re, html, time
q = " ".join(sys.argv[1:])
H = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
     "Accept-Language":"en-US,en;q=0.9"}
def clean(t):
    t = re.sub(r'<[^>]+>','',t); return html.unescape(t).strip()
# Mojeek
try:
    r = requests.get("https://www.mojeek.com/search?q="+urllib.parse.quote(q), headers=H, timeout=30)
    items = re.findall(r'<a class="ob"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', r.text, re.S)
    snips = re.findall(r'<p class="s">(.*?)</p>', r.text, re.S)
    print("=== MOJEEK", r.status_code, len(items))
    for i,(u,t) in enumerate(items[:12]):
        print(f"[M{i+1}] {clean(t)}\n    {u}\n    {clean(snips[i])[:250] if i<len(snips) else ''}\n")
except Exception as e:
    print("MOJEEK ERR", e)

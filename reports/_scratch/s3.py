import sys, urllib.parse, requests, re, html
q = " ".join(sys.argv[1:])
H = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
     "Accept-Language":"en-US,en;q=0.9"}
def clean(t):
    t = re.sub(r'<[^>]+>','',t); return html.unescape(t).strip()
r = requests.get("https://www.bing.com/search?q="+urllib.parse.quote(q)+"&count=30", headers=H, timeout=30)
print("=== BING", r.status_code, len(r.text))
blocks = re.findall(r'<li class="b_algo".*?</li>', r.text, re.S)
for i,b in enumerate(blocks[:14]):
    m = re.search(r'<h2>.*?<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', b, re.S)
    if not m: continue
    u, t = m.group(1), clean(m.group(2))
    sn = re.search(r'<p class="[^"]*b_lineclamp[^"]*"[^>]*>(.*?)</p>', b, re.S)
    s = clean(sn.group(1))[:300] if sn else ""
    print(f"[B{i+1}] {t}\n    {u}\n    {s}\n")

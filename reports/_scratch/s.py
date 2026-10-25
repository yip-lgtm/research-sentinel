import sys, urllib.parse, requests, re, html
q = " ".join(sys.argv[1:])
url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(q)
h = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}
try:
    r = requests.get(url, headers=h, timeout=30)
except Exception as e:
    print("ERR", e); sys.exit()
t = r.text
res = re.findall(r'result__a" href="([^"]+)"[^>]*>(.*?)</a>', t, re.S)
snip = re.findall(r'result__snippet"[^>]*>(.*?)</a>', t, re.S)
import urllib.parse as up
for i,(u,ti) in enumerate(res[:15]):
    u = html.unescape(u)
    m = re.search(r'uddg=([^&]+)', u)
    if m: u = up.unquote(m.group(1))
    ti = re.sub(r'<[^>]+>','',ti); ti = html.unescape(ti).strip()
    s = ""
    if i < len(snip):
        s = re.sub(r'<[^>]+>','',snip[i]); s = html.unescape(s).strip()
    print(f"[{i+1}] {ti}\n    {u}\n    {s[:300]}\n")

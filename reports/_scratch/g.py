import sys, urllib.parse, requests, re, html
q = " ".join(sys.argv[1:])
H = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
     "Accept-Language":"en-US,en;q=0.9","Accept":"text/html,application/xhtml+xml"}
r = requests.get("https://www.google.com/search?q="+urllib.parse.quote(q)+"&num=30&hl=en", headers=H, timeout=30)
t = r.text
print("STATUS", r.status_code, len(t))
# extract /url?q= links and titles
blocks = re.split(r'<div class="MjjYud"', t)
out=[]
for b in blocks:
    m = re.search(r'<a href="(https?://[^"]+)"[^>]*>.*?<h3[^>]*>(.*?)</h3>', b, re.S)
    if not m: continue
    u = m.group(1)
    if 'google.com' in u: continue
    ti = re.sub(r'<[^>]+>','',m.group(2)); ti=html.unescape(ti).strip()
    # snippet
    sn = re.sub(r'<[^>]+>',' ', b)
    sn = html.unescape(sn)
    sn = re.sub(r'\s+',' ',sn)
    out.append((ti,u,sn[:400]))
print("RESULTS", len(out))
for i,(ti,u,sn) in enumerate(out[:15]):
    print(f"[{i+1}] {ti}\n    {u}\n    {sn}\n")

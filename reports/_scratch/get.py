import sys, requests, re, html
url = sys.argv[1]
H = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
     "Accept-Language":"en-US,en;q=0.9"}
try:
    r = requests.get(url, headers=H, timeout=50)
except Exception as e:
    print("ERR", e); sys.exit()
print("STATUS", r.status_code, "LEN", len(r.text), "FINAL", r.url, file=sys.stderr)
t = r.text
t = re.sub(r'(?is)<(script|style|noscript|svg|head)[^>]*>.*?</\1>', ' ', t)
t = re.sub(r'(?is)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>|</tr>|</td>', '\n', t)
t = re.sub(r'(?s)<[^>]+>', ' ', t)
t = html.unescape(t)
t = re.sub(r'[ \t\xa0]+', ' ', t)
t = re.sub(r'\n\s*\n+', '\n', t)
print(t)

import sys, requests, re, html
url = sys.argv[1]
h = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"}
try:
    r = requests.get(url, headers=h, timeout=45)
except Exception as e:
    print("ERR", e); sys.exit()
print("STATUS", r.status_code, "LEN", len(r.text), "FINAL", r.url)
t = r.text
t = re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>', ' ', t)
t = re.sub(r'(?is)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>', '\n', t)
t = re.sub(r'(?s)<[^>]+>', ' ', t)
t = html.unescape(t)
t = re.sub(r'[ \t\xa0]+', ' ', t)
t = re.sub(r'\n\s*\n+', '\n', t)
print(t)

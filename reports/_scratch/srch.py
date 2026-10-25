import sys, urllib.parse, urllib.request, re, html
def search(q, n=12):
    url = "https://www.bing.com/search?format=rss&count=30&q=" + urllib.parse.quote(q)
    req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'})
    try:
        data = urllib.request.urlopen(req, timeout=45).read().decode('utf-8','replace')
    except Exception as e:
        print("ERR", e); return
    items = re.findall(r'<item>(.*?)</item>', data, re.S)
    print("=== QUERY:", q, "(%d results)" % len(items))
    for it in items[:n]:
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        d = re.search(r'<description>(.*?)</description>', it, re.S)
        print("-", html.unescape(t.group(1)) if t else '')
        print("  ", html.unescape(l.group(1)) if l else '')
        if d: print("   ", re.sub('<[^>]+>','',html.unescape(d.group(1)))[:220])
for q in sys.argv[1:]:
    search(q)

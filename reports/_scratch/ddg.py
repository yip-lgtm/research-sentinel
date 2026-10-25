import sys, urllib.parse, urllib.request, re, html
def search(q):
    url="https://html.duckduckgo.com/html/?q="+urllib.parse.quote(q)
    req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'})
    try:
        t=urllib.request.urlopen(req,timeout=45).read().decode('utf-8','replace')
    except Exception as e:
        print("ERR",e); return
    res=re.findall(r'class="result__a"[^>]*href="(.*?)".*?>(.*?)</a>', t, re.S)
    print("=== ",q,len(res))
    for u,ti in res[:12]:
        u=html.unescape(u)
        m=re.search(r'uddg=([^&]+)',u)
        if m: u=urllib.parse.unquote(m.group(1))
        print("-",re.sub('<[^>]+>','',html.unescape(ti))[:120])
        print("  ",u)
for q in sys.argv[1:]: search(q)

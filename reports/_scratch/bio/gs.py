import sys,urllib.request,urllib.parse,re,html,json,time
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.9','Accept':'text/html,application/xhtml+xml'}
def fetch(u,t=25):
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=t)
        return r.read().decode('utf-8','replace')
    except Exception as e: return "ERR:"+str(e)
def google(q,n=10):
    u="https://www.google.com/search?num=%d&q=%s"%(n,urllib.parse.quote(q))
    h=fetch(u)
    if h.startswith("ERR:"): print(h); return
    # extract result links + titles
    seen=set()
    for m in re.finditer(r'<a href="(/url\?q=[^"]+|https?://[^"]+)"[^>]*>(.*?)</a>',h,re.S):
        raw=html.unescape(m.group(1)); ti=re.sub('<[^>]+>','',m.group(2)); ti=html.unescape(ti).strip()
        if raw.startswith('/url?q='): raw=raw[7:].split('&')[0]
        if not raw.startswith('http'): continue
        if 'google.com' in raw or len(ti)<12: continue
        if raw in seen: continue
        seen.add(raw)
        print('-',ti[:130]); print('  ',raw[:180]); print()
if __name__=="__main__":
    for q in sys.argv[1:]:
        print("#### ",q); google(q); time.sleep(1)

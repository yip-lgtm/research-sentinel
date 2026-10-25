import sys, urllib.request, re, html
def fetch(pmcid, name):
    url=f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/"
    req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'})
    try:
        t=urllib.request.urlopen(req,timeout=60).read().decode('utf-8','replace')
    except Exception as e:
        print("ERR",pmcid,e); return
    t=re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>',' ',t)
    t=re.sub(r'(?is)<br[^>]*>','\n',t)
    t=re.sub(r'(?is)</(p|div|h[1-6]|li|tr|section|td|th)>','\n',t)
    t=re.sub(r'(?is)<[^>]+>',' ',t)
    t=html.unescape(t); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    open(name,'w').write(t)
    print(name, len(t))
for a in sys.argv[1:]:
    pmcid,name=a.split('=')
    fetch(pmcid,name)

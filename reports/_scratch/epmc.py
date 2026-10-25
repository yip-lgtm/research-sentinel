import sys, urllib.request, re, html, time
def fetch(pmcid):
    url=f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
    req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    try:
        t=urllib.request.urlopen(req,timeout=60).read().decode('utf-8','replace')
    except Exception as e:
        print("ERR",pmcid,e); return
    t=re.sub(r'(?is)<(table-wrap|fig)\b.*?</\1>',' [FIG/TABLE OMITTED] ',t)
    t=re.sub(r'(?is)<[^>]+>',' ',t)
    t=html.unescape(t); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    out=pmcid+".epmc.txt"
    open(out,'w').write(t)
    print(out,len(t))
for p in sys.argv[1:]:
    fetch(p); time.sleep(2)

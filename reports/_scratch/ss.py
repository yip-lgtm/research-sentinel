import sys, urllib.request, urllib.parse, json
def s2(q, limit=10):
    url=f"https://api.semanticscholar.org/graph/v1/paper/search?query={urllib.parse.quote(q)}&limit={limit}&fields=title,year,venue,externalIds,abstract,openAccessPdf,publicationDate"
    req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    try:
        d=json.loads(urllib.request.urlopen(req,timeout=60).read())
    except Exception as e:
        print("ERR",e); return
    print("== S2:",q)
    for p in d.get('data',[]):
        print("-",p['title'],'|',p.get('venue'),p.get('publicationDate'),'|',p.get('externalIds'))
        if p.get('openAccessPdf'): print("   PDF:",p['openAccessPdf'].get('url'))
        if p.get('abstract'): print("   ",p['abstract'][:400].replace('\n',' '))
for q in sys.argv[1:]:
    s2(q)

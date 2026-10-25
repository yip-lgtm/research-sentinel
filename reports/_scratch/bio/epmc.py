import sys, json, urllib.parse, urllib.request, re, time
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36'}
def get(url, t=30):
    try:
        req=urllib.request.Request(url, headers=UA)
        return urllib.request.urlopen(req, timeout=t).read().decode('utf-8','replace')
    except Exception as e:
        return "ERR:"+str(e)
def search(q, n=10, extra=""):
    url="https://www.ebi.ac.uk/europepmc/webservices/rest/search?query="+urllib.parse.quote(q)+"&format=json&pageSize=%d&resultType=core"%n+extra
    d=json.loads(get(url))
    out=[]
    for r in d.get('resultList',{}).get('result',[]):
        out.append(dict(id=r.get('id'),pmid=r.get('pmid'),doi=r.get('doi'),title=r.get('title'),
            auth=r.get('authorString'),j=r.get('journalTitle'),year=r.get('pubYear'),
            oa=r.get('isOpenAccess'),ftc=r.get('inEPMC'),pmcid=r.get('pmcid'),abs=(r.get('abstractText') or '')[:600]))
    print("HITS:", d.get('hitCount'))
    for o in out:
        print("-"*90)
        print("ID",o['id'],"| PMID",o['pmid'],"|",o['j'],o['year'],"| OA",o['oa'],"| inEPMC",o['ftc'],"| PMCID",o['pmcid'])
        print("T:",o['title'])
        print("A:",o['auth'])
        print("DOI:",o['doi'])
        print("ABS:",re.sub('<[^>]+>','',o['abs'])[:500])
    return out
def fulltext(pmcid):
    u="https://www.ebi.ac.uk/europepmc/webservices/rest/%s/fullTextXML"%pmcid
    x=get(u,60)
    if x.startswith("ERR:"): return x
    x=re.sub(r'<(ref-list|back)\b.*?</\1>','',x,flags=re.S)
    return re.sub(r'<[^>]+>',' ',x)
if __name__=="__main__":
    cmd=sys.argv[1]
    if cmd=="s": search(sys.argv[2], int(sys.argv[3]) if len(sys.argv)>3 else 10)
    elif cmd=="f":
        t=fulltext(sys.argv[2]); open(sys.argv[3],'w').write(t); print("LEN",len(t),"->",sys.argv[3])
    elif cmd=="g":
        print(get(sys.argv[2]))

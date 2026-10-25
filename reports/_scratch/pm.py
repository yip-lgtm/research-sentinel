import sys, urllib.parse, urllib.request, json, time
def esearch(term, retmax=20):
    url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&retmax=%d&retmode=json&term=%s"%(retmax,urllib.parse.quote(term))
    r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=45).read()
    return json.loads(r)['esearchresult']['idlist']
for term in sys.argv[1:]:
    ids=esearch(term)
    print("TERM:",term,"->",ids)
    if ids:
        s="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pmc&retmode=json&id="+",".join(ids)
        d=json.loads(urllib.request.urlopen(urllib.request.Request(s,headers={'User-Agent':'Mozilla/5.0'}),timeout=45).read())['result']
        for i in ids:
            it=d.get(i,{})
            print("   PMC%s | %s | %s | %s"%(i, it.get('pubdate',''), it.get('fulljournalname',''), it.get('title','')[:150]))
    time.sleep(1)

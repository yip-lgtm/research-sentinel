import sys, urllib.request, urllib.parse, json, re, html
def get(doi):
    url=f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    req=urllib.request.Request(url, headers={'User-Agent':'research-bot/1.0 (mailto:research@example.org)'})
    try:
        d=json.loads(urllib.request.urlopen(req,timeout=60).read())['message']
    except Exception as e:
        print("ERR",doi,e); return
    print("###", d.get('title',[''])[0])
    print("   DOI:",doi,"|",d.get('container-title',[''])[0] if d.get('container-title') else '', "| issued:", d.get('issued',{}).get('date-parts'), "| type:", d.get('type'))
    ab=d.get('abstract','')
    ab=re.sub(r'<[^>]+>',' ',html.unescape(ab)); ab=re.sub(r'\s+',' ',ab)
    if ab: print("   ABS:", ab[:1500])
    print()
for d in sys.argv[1:]:
    get(d)

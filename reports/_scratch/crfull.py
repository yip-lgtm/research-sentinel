import sys, urllib.request, urllib.parse, json, re, html
for doi in sys.argv[1:]:
    url=f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    req=urllib.request.Request(url, headers={'User-Agent':'research-bot/1.0 (mailto:research@example.org)'})
    try:
        d=json.loads(urllib.request.urlopen(req,timeout=60).read())['message']
    except Exception as e:
        print("ERR",doi,e); continue
    print("###", d.get('title',[''])[0], "|", d.get('container-title',[''])[0] if d.get('container-title') else '', "|", d.get('issued',{}).get('date-parts'))
    ab=d.get('abstract','')
    ab=re.sub(r'<[^>]+>',' ',html.unescape(ab)); ab=re.sub(r'\s+',' ',ab)
    print(ab)
    print("URL:", d.get('URL'))
    print("="*80)

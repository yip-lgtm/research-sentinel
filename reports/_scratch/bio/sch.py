import sys,urllib.request,urllib.parse,re,html,time
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36','Accept-Language':'en-US,en;q=0.9'}
def fetch(u,t=25):
    try:
        return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=t).read().decode('utf-8','replace')
    except Exception as e: return "ERR:"+str(e)
def sch(q):
    h=fetch("https://scholar.google.com/scholar?num=20&q="+urllib.parse.quote(q))
    if h.startswith("ERR:"): print(h); return
    if 'not a robot' in h or 'unusual traffic' in h: print("BLOCKED-ROBOT"); return
    for m in re.finditer(r'<div class="gs_r gs_or gs_scl">(.*?)</div>\s*</div>\s*</div>',h,re.S):
        b=m.group(1)
        t=re.search(r'<h3[^>]*class="gs_rt"[^>]*>(.*?)</h3>',b,re.S)
        ti=html.unescape(re.sub('<[^>]+>','',t.group(1))) if t else '?'
        ln=re.search(r'<div class="gs_a">.*?<h3.*?<a href="([^"]+)"',b,re.S)
        sn=re.search(r'<div class="gs_rs">(.*?)</div>',b,re.S)
        snip=html.unescape(re.sub('<[^>]+>','',sn.group(1))) if sn else ''
        au=re.search(r'<div class="gs_a">(.*?)</div>',b,re.S)
        au=html.unescape(re.sub('<[^>]+>','',au.group(1))) if au else ''
        print('*',ti[:170])
        print('   ',au[:150])
        if ln: print('   URL:',html.unescape(ln.group(1))[:200])
        if snip: print('   ',snip[:400])
        print()
for q in sys.argv[1:]:
    print("####",q); sch(q); time.sleep(2)

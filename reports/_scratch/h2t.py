import sys,re,html
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8',errors='replace').read()
    t=re.sub(r'(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>',' ',t)
    t=re.sub(r'(?is)<br[^>]*>','\n',t)
    t=re.sub(r'(?is)</(p|div|h[1-6]|li|tr|section|td|th)>','\n',t)
    t=re.sub(r'(?is)<[^>]+>',' ',t)
    t=html.unescape(t); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    out=f.replace('.html','.txt')
    open(out,'w').write(t)
    print(out,len(t))

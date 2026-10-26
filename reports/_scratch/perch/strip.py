#!/usr/bin/env python3
import sys, re, html
def strip(path, out=None):
    t = open(path, encoding="utf-8", errors="replace").read()
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S | re.I)
    t = re.sub(r'<style.*?</style>', ' ', t, flags=re.S | re.I)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = html.unescape(t)
    t = re.sub(r'[ \t\xa0]+', ' ', t)
    t = re.sub(r'\n\s*\n+', '\n', t)
    if out:
        open(out, "w").write(t)
    return t
if __name__ == "__main__":
    t = strip(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    print(t)

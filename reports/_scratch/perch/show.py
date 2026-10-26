#!/usr/bin/env python3
import sys, os, time, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fetch, search

def show(tag, greps=None, maxn=100):
    arts = fetch.parse(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"pm_{tag}.xml"))
    n = 0
    for a in arts:
        blob = (a["title"] + " " + a["abstract"]).lower()
        if greps and not any(g.lower() in blob for g in greps):
            continue
        n += 1
        if n > maxn:
            break
        print("=" * 110)
        print(f"PMID {a['pmid']} | {a['date']} | {a['journal']} | DOI {a['doi']}")
        print(f"TITLE: {a['title']}")
        print(f"AUTH: {', '.join(a['authors'][:5])}{' et al.' if len(a['authors'])>5 else ''}")
        print(f"AFFIL: {a['affiliation'][:220]}")
        print(f"URL: {a['url']}")
        print(f"ABS: {a['abstract']}")
    print(f"--- shown {n} of {len(arts)}")

if __name__ == "__main__":
    tag = sys.argv[1]
    greps = sys.argv[2].split("|") if len(sys.argv) > 2 and sys.argv[2] else None
    show(tag, greps)

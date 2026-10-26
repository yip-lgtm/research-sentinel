#!/usr/bin/env python3
import sys, json, urllib.request, urllib.parse, os, time

OUT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def esearch(term, retmax=30, db="pubmed"):
    url = BASE + f"esearch.fcgi?db={db}&term={urllib.parse.quote(term)}&retmode=json&retmax={retmax}&sort=relevance"
    with urllib.request.urlopen(url, timeout=40) as r:
        d = json.load(r)
    return d["esearchresult"].get("idlist", []), int(d["esearchresult"].get("count", 0))

if __name__ == "__main__":
    term = sys.argv[1]
    rm = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    ids, count = esearch(term, rm)
    tag = sys.argv[3] if len(sys.argv) > 3 else "s"
    print(f"COUNT={count}")
    print(",".join(ids))
    if ids:
        import fetch
        fetch.fetch(ids, tag)

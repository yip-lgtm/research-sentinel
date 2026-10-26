#!/usr/bin/env python3
"""Fetch PubMed abstracts for a list of PMIDs via E-utilities."""
import sys, json, urllib.request, urllib.parse, time, os, re

OUT = os.path.dirname(os.path.abspath(__file__))

def fetch(pmids, tag):
    if isinstance(pmids, str):
        pmids = [pmids]
    ids = ",".join(pmids)
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
           f"?db=pubmed&id={ids}&retmode=xml")
    try:
        with urllib.request.urlopen(url, timeout=40) as r:
            data = r.read().decode("utf-8", "replace")
    except Exception as e:
        print(f"ERR {tag}: {e}")
        return
    path = os.path.join(OUT, f"pm_{tag}.xml")
    with open(path, "w") as f:
        f.write(data)
    print(f"OK {tag} -> {path} ({len(data)} bytes)")

def parse(path):
    import xml.etree.ElementTree as ET
    tree = ET.parse(path)
    root = tree.getroot()
    out = []
    for art in root.iter("PubmedArticle"):
        pmid = art.findtext(".//PMID")
        ti = "".join(art.find(".//ArticleTitle").itertext()) if art.find(".//ArticleTitle") is not None else ""
        jour = art.findtext(".//Journal/ISOAbbreviation") or art.findtext(".//Journal/Title") or ""
        # date
        pd = art.find(".//JournalIssue/PubDate")
        date = ""
        if pd is not None:
            date = "-".join(x for x in [pd.findtext("Year"), pd.findtext("Month"), pd.findtext("Day")] if x)
            if not date:
                MedlineDate = pd.findtext("MedlineDate")
                if MedlineDate: date = MedlineDate
        ab = " ".join("".join(a.itertext()) for a in art.iter("AbstractText"))
        doi = ""
        for eid in art.iter("ELocationID"):
            if eid.get("EIdType") == "doi":
                doi = eid.text or ""
        if not doi:
            for aid in art.iter("ArticleId"):
                if aid.get("IdType") == "doi":
                    doi = aid.text or ""
        authors = []
        for a in art.iter("Author"):
            ln = a.findtext("LastName"); ini = a.findtext("Initials")
            if ln: authors.append(f"{ln} {ini or ''}".strip())
        aff = art.findtext(".//AffiliationInfo/Affiliation") or ""
        ptypes = [p.text for p in art.iter("PublicationType")]
        out.append(dict(pmid=pmid, title=ti, journal=jour, date=date, doi=doi,
                        authors=authors, affiliation=aff, ptypes=ptypes,
                        abstract=ab, url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"))
    return out

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "fetch":
        fetch(sys.argv[2], sys.argv[3])
    elif mode == "show":
        arts = parse(os.path.join(OUT, f"pm_{sys.argv[2]}.xml"))
        filt = sys.argv[3] if len(sys.argv) > 3 else None
        for a in arts:
            if filt and filt.lower() not in (a["title"]+" "+a["abstract"]).lower():
                continue
            print("="*100)
            print(f"PMID {a['pmid']} | {a['date']} | {a['journal']} | DOI {a['doi']}")
            print(f"TITLE: {a['title']}")
            print(f"AUTHORS: {', '.join(a['authors'][:6])}{' et al.' if len(a['authors'])>6 else ''}")
            print(f"AFFIL: {a['affiliation'][:300]}")
            print(f"PTYPES: {a['ptypes']}")
            print(f"URL: {a['url']}")
            print(f"ABSTRACT: {a['abstract']}")

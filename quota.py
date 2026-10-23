#!/usr/bin/env python3
"""科研哨兵 — 領域配額計算器 (Domain Quota)

用戶 2026-10-23 指示：主要做 (AI工程/機械工程/軍事工程/土木工程) 科研 80%，
其他工程科研 20%。

本模組：
  1. 為每個已報告主題計算 domain_code 歸屬（核心 4 域 vs 其他）
  2. 以 4:1 循環配額決定「下一題必須屬於邊個領域」
  3. 輸出一行「配額行」供 cron prompt 直接引用，避免 LLM 靠感覺選題

配額窗口：QUOTA_START_UTC 之後的報告（歷史題目視為基線，不追補）。
循環規則：每 4 份核心報告之後，容許 1 份其他領域報告 → 穩態 80/20。

用法:
  python3 quota.py            # 人類可讀輸出 + 配額行
  python3 quota.py --json     # JSON
  python3 quota.py --stamp    # 只輸出配額行（供 shell 嵌入）
"""
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
TOPICS = os.path.join(HERE, "knowledge", "topics.json")
STATE = os.path.join(HERE, "state.json")

# 配額窗口起點：用戶指示方向調整嘅時刻
QUOTA_START_UTC = "2026-10-23T05:00:00Z"

# 核心 4 域（80%）
CORE = {
    "ai": "AI 工程",
    "mech": "機械工程",
    "mil": "軍事工程",
    "civil": "土木工程",
}
# 其他領域（20%）
OTHER = {
    "elec": "電子／電氣工程",
    "mat": "材料工程",
    "energy": "能源／動力工程",
    "env": "環境工程",
    "chem": "化學／化工",
    "bio": "醫療／生物工程",
    "agri": "農業／食品工程",
    "edu": "工程教育",
    "other": "公共政策／其他",
}
ALL_DOMAINS = {**CORE, **OTHER}

# 歷史主題 → 領域歸屬
DOMAIN_MAP = {
    "edu-path-overview": "edu",
    "edu-bachelor-branches": "edu",
    "edu-graduate-levels": "edu",
    "energy-retail-price-affordability": "energy",
    "occupational-heat-health-burden": "other",
    "low-carbon-cement-lc3": "mat",
    "amr-burden-age-divergence": "other",
    "hearing-loss-cognitive-intervention": "bio",
    "perovskite-tandem": "mat",
    "nitrogen-nitrogen-use-efficiency": "other",
    "malaria-vaccine-mortality-mechanism": "other",
    "pfas-drinking-water-mcl": "env",
    "coastal-bangladesh-salinity-health": "civil",
}

CYCLE_CORE = 4          # 每 4 份核心 → 1 份其他
CYCLE_OTHER = 1
CORE_RATIO_TARGET = 0.80


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def in_window(last_report: str) -> bool:
    """last_report 格式 'YYYY-MM-DD-HH' → 與窗口起點比較。"""
    if not last_report:
        return False
    try:
        ts = datetime.strptime(last_report, "%Y-%m-%d-%H").replace(tzinfo=timezone.utc)
    except ValueError:
        return False
    start = datetime.strptime(QUOTA_START_UTC, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    return ts >= start


def compute(topics_doc):
    topics = topics_doc.get("topics", [])
    counts = Counter()
    legacy = Counter()
    for t in topics:
        dc = t.get("domain_code") or DOMAIN_MAP.get(t.get("id", ""), "other")
        t["domain_code"] = dc
        if in_window(t.get("last_report", "")):
            counts[dc] += 1
        else:
            legacy[dc] += 1
    return counts, legacy, topics


def pick_domain(counts: Counter):
    """決定下一題領域。回傳 (code, name, reason)。"""
    core_done = sum(counts.get(c, 0) for c in CORE)
    other_done = sum(counts.get(c, 0) for c in OTHER)
    other_allowed = core_done // CYCLE_CORE

    if other_done < other_allowed:
        # 核心配額未夠 → 必須核心；揀計數最少嘅核心域（次序固定保證均衡）
        code = sorted(CORE, key=lambda c: (counts.get(c, 0), list(CORE).index(c)))[0]
        return code, CORE[code], (
            f"窗口內核心 {core_done} 份、其他 {other_done} 份，核心配額未滿 "
            f"（每 {CYCLE_CORE} 份核心先容許 {CYCLE_OTHER} 份其他）→ 本題必須核心域")

    # 核心已達標 → 可以做其他域；揀其他域中計數最少者
    code = sorted(OTHER, key=lambda c: (counts.get(c, 0), list(OTHER).index(c)))[0]
    return code, OTHER[code], (
        f"窗口內核心 {core_done} 份、其他 {other_done} 份，核心配額已滿 "
        f"→ 本題可做其他域，維持 80/20 長期比例")


def main() -> int:
    if not os.path.exists(TOPICS):
        print(f"ERROR: 搵唔到 {TOPICS}", file=sys.stderr)
        return 1
    doc = load(TOPICS)
    counts, legacy, topics = compute(doc)
    code, name, reason = pick_domain(counts)

    core_done = sum(counts.get(c, 0) for c in CORE)
    other_done = sum(counts.get(c, 0) for c in OTHER)
    total = core_done + other_done
    ratio = (core_done / total) if total else 0.0

    quota_line = (
        f"[配額] 窗口 {QUOTA_START_UTC} 起：核心 {core_done} / 其他 {other_done}"
        f"（核心佔 {ratio:.0%}，目標 {CORE_RATIO_TARGET:.0%}）→ 下一題領域 = "
        f"{name}（domain_code={code}）；理由：{reason}"
    )

    if "--json" in sys.argv:
        print(json.dumps({
            "quota_start_utc": QUOTA_START_UTC,
            "window_counts": dict(counts),
            "legacy_counts": dict(legacy),
            "core_done": core_done,
            "other_done": other_done,
            "core_ratio": round(ratio, 3),
            "target_core_ratio": CORE_RATIO_TARGET,
            "next_domain_code": code,
            "next_domain_name": name,
            "reason": reason,
            "quota_line": quota_line,
        }, ensure_ascii=False, indent=2))
        return 0

    if "--stamp" in sys.argv:
        print(quota_line)
        return 0

    print("=== 領域配額 / Domain Quota ===")
    print(f"窗口起點：{QUOTA_START_UTC}")
    print(f"窗口內：核心 {core_done} 份、其他 {other_done} 份 → 核心佔 {ratio:.0%}"
          f"（目標 {CORE_RATIO_TARGET:.0%}）")
    print("\n-- 窗口內各域計數 --")
    for c in list(CORE) + list(OTHER):
        tag = "核心" if c in CORE else "其他"
        n = counts.get(c, 0)
        mark = " ← 下一題" if c == code else ""
        print(f"  {c:7s} {ALL_DOMAINS[c]:14s} [{tag}] {n}{mark}")
    print(f"\n-- 歷史基線（窗口前，不追補）--")
    for c in list(CORE) + list(OTHER):
        if legacy.get(c):
            print(f"  {c:7s} {ALL_DOMAINS[c]:14s} {legacy[c]}")
    print(f"\n{quota_line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

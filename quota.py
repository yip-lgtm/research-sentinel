#!/usr/bin/env python3
"""人性化練習哨兵 — 領域配額計算器 (Domain Quota)

用戶 2026-10-23 指示：主要做 (AI工程/機械工程/軍事工程/土木工程) 科研 80%，
其他工程科研 20%。同日補充：AI 題目勝率最高，核心域內部對 AI 加權。

本模組：
  1. 為每個已報告主題計算 domain_code 歸屬（核心 4 域 vs 其他）
  2. 以 4:1 循環帳本決定「下一題必須屬於邊個領域」
  3. 核心域內按勝率加權選域（AI 權重最高）
  4. 輸出一行「配額行」供 cron prompt 直接引用，避免 LLM 靠感覺選題

配額窗口：QUOTA_START_UTC 之後的報告（歷史題目視為基線，不追補）。

配額帳本（唔靠 LLM 感覺）：
  other_allowed = core_done // 4      每 4 份核心先開 1 個「其他」名額
  other_done <  other_allowed  → 本題做「其他」（有名額未用）
  other_done >  other_allowed  → 本題做「核心」（其他超支，要拉回）
  other_done == other_allowed  → 本題做「核心」（剛用完一輪，開新一輪）

⚠️ 2026-10-23 修正：舊版 pick_domain 將 first 分支條件寫反
   （other_done < other_allowed 時返回 CORE），令「其他 20%」名額永遠
   用唔到——other_done 恆為 0 而 other_allowed 隨 core 增長，條件恆真。
   結果 80/20 目標實際變成 100/0。本版已掉轉並加佔比糾偏閘。

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

# 核心域內加權：用戶反饋 AI 題目勝率最高 → AI 權重最高，
# 揀域時用 count/weight 最低者（權重高 → 分母大 → 更容易被揀）。
CORE_WEIGHTS = {
    "ai": 3.0,
    "mech": 2.0,
    "civil": 2.0,
    "mil": 1.0,
}

# 歷史主題 → 領域歸屬（topics.json 有 domain_code 時以嗰個為準）
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
    "pm25-low-exposure-mortality-burden": "other",
    "ai-datacentre-grid-power-quality": "ai",
    "offshore-wind-monopile-cathodic-protection": "mech",
    "copper-price-supply-mechanism": "mat",
    "ev-charging-transformer-ageing": "elec",
    "am-fatigue-surface-vs-porosity": "mech",
}

CYCLE_CORE = 4          # 每 4 份核心 → 1 份其他
CYCLE_OTHER = 1
CORE_RATIO_TARGET = 0.80

# 核心佔比糾偏閘：實際佔比嚴重偏離目標時強制拉回（防止分類錯或帳本失衡）
FORCE_OTHER_MIN_RATIO = 0.95   # 核心佔比高過呢個 → 太核心化
FORCE_CORE_MAX_RATIO = 0.65    # 核心佔比低過呢個 → 其他超支
RATIO_GUARD_MIN_TOTAL = 4      # 樣本太細唔啟動糾偏閘


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


def _pick_weighted(counts: Counter, group: dict, weights: dict | None = None):
    """揀組內最需要做嘅域：count/weight 最低者；同分用固定次序保證均衡。"""
    order = list(group)
    def score(c):
        w = (weights or {}).get(c, 1.0) or 1.0
        return (counts.get(c, 0) / w, order.index(c))
    return sorted(order, key=score)[0]


def pick_domain(counts: Counter):
    """決定下一題領域。回傳 (code, name, reason, detail)。"""
    core_done = sum(counts.get(c, 0) for c in CORE)
    other_done = sum(counts.get(c, 0) for c in OTHER)
    total = core_done + other_done
    ratio = (core_done / total) if total else 1.0
    other_allowed = core_done // CYCLE_CORE

    # (A) 週期帳本（主規則，自糾偏）
    if other_done < other_allowed:
        group, ledger = OTHER, "other"
        ledger_note = (f"「其他」名額未用盡（已做 {other_done}，可用 {other_allowed}）"
                       f"→ 本題做其他域")
    elif other_done > other_allowed:
        group, ledger = CORE, "core"
        ledger_note = (f"「其他」名額超支（已做 {other_done}，可用 {other_allowed}）"
                       f"→ 本題做核心域拉回比例")
    else:
        group, ledger = CORE, "core"
        ledger_note = (f"剛好用完一輪（其他 {other_done}/{other_allowed}）"
                       f"→ 本題開新一輪核心域")

    # (B) 核心佔比糾偏閘（保護）：實際佔比嚴重偏離目標時，蓋過帳本
    forced = None
    if total >= RATIO_GUARD_MIN_TOTAL:
        if ratio > FORCE_OTHER_MIN_RATIO and ledger == "core":
            forced, group = "other", OTHER
            ledger_note += (f"；糾偏閘介入：核心佔比 {ratio:.0%} > "
                            f"{FORCE_OTHER_MIN_RATIO:.0%} → 強制改做其他域")
        elif ratio < FORCE_CORE_MAX_RATIO and ledger == "other":
            forced, group = "core", CORE
            ledger_note += (f"；糾偏閘介入：核心佔比 {ratio:.0%} < "
                            f"{FORCE_CORE_MAX_RATIO:.0%} → 強制改做核心域")

    if group is CORE:
        code = _pick_weighted(counts, CORE, CORE_WEIGHTS)
        weights_note = f"核心域加權（AI 權重 {CORE_WEIGHTS['ai']:.0f} 最高，AI 勝率最高）"
    else:
        code = _pick_weighted(counts, OTHER)
        weights_note = "其他域按已覆蓋數最少者均衡"

    name = ALL_DOMAINS[code]
    reason = (f"窗口內核心 {core_done} / 其他 {other_done}"
              f"（核心佔 {ratio:.0%}，目標 {CORE_RATIO_TARGET:.0%}）；{ledger_note}；{weights_note}")
    detail = {
        "core_done": core_done,
        "other_done": other_done,
        "total": total,
        "core_ratio": round(ratio, 4),
        "other_allowed": other_allowed,
        "ledger": ledger,
        "forced_by_ratio_guard": forced,
        "group": "core" if group is CORE else "other",
    }
    return code, name, reason, detail


def main() -> int:
    if not os.path.exists(TOPICS):
        print(f"ERROR: 搵唔到 {TOPICS}", file=sys.stderr)
        return 1
    doc = load(TOPICS)
    counts, legacy, topics = compute(doc)
    code, name, reason, detail = pick_domain(counts)

    core_done = detail["core_done"]
    other_done = detail["other_done"]
    total = detail["total"]
    ratio = detail["core_ratio"]

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
            "total": total,
            "core_ratio": ratio,
            "target_core_ratio": CORE_RATIO_TARGET,
            "core_weights": CORE_WEIGHTS,
            "next_domain_code": code,
            "next_domain_name": name,
            "reason": reason,
            "detail": detail,
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
    print(f"帳本：其他名額 已用 {other_done} / 可用 {detail['other_allowed']}"
          f"；糾偏閘：{'觸發（' + str(detail['forced_by_ratio_guard']) + '）' if detail['forced_by_ratio_guard'] else '未觸發'}")
    print("\n-- 窗口內各域計數 --")
    for c in list(CORE) + list(OTHER):
        tag = "核心" if c in CORE else "其他"
        n = counts.get(c, 0)
        mark = " ← 下一題" if c == code else ""
        w = f"（權重 {CORE_WEIGHTS[c]:.0f}）" if c in CORE_WEIGHTS else ""
        print(f"  {c:7s} {ALL_DOMAINS[c]:14s} [{tag}] {n}{w}{mark}")
    print("\n-- 歷史基線（窗口前，不追補）--")
    for c in list(CORE) + list(OTHER):
        if legacy.get(c):
            print(f"  {c:7s} {ALL_DOMAINS[c]:14s} {legacy[c]}")
    print(f"\n{quota_line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

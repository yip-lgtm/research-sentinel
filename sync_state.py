#!/usr/bin/env python3
"""狀態一致性同步器（確定性，唔依賴 LLM）。

解決嘅實況落差（2026-10-27 量出）：
  - `knowledge/topics.json` entry 遠少於過閘報告數 → 防重複機制大部分失效
  - `knowledge/sections/*.md` 同 topics entry 對唔上 → 知識庫寫回漏做
  - `state.json` 統計手寫滯後（reports_total / reports_pending / last_report_utc）

做四件事（全部由磁碟現況推導，唔靠記憶）：
  1. scan_reports()     → 掃 reports/ 全部過閘報告，抽 (stamp, slug, title, domain, bullets)
  2. sync_topics()      → 合併入 topics.json（人工寫過嘅 notes 唔覆蓋）
  3. sync_sections()    → 為缺章節嘅 topic 生成章節檔（已存在嘅人工章節唔郁）
  4. sync_state()       → 由 reports/index.json 推導 state.json 統計

每步都可單獨跑：python3 sync_state.py topics|sections|state|all
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
REPORTS = REPO / "reports"
INDEX = REPORTS / "index.json"
KNOW = REPO / "knowledge"
TOPICS = KNOW / "topics.json"
SECTIONS = KNOW / "sections"
STATE = REPO / "state.json"

# ── 人工 slug 對照：每份過閘報告對應一個語意化主題 slug ────────────────────────
# 鍵 = 報告 stamp，值 = (slug, 中文標題, domain_code)
SLUGS: dict[str, tuple[str, str, str]] = {
    "2026-10-23-14": ("antivehicle-mine-farmland-safety", "反車載地雷與農機耕作安全落差", "mil"),
    "2026-10-23-16": ("ob-od-perchlorate-drinking-water", "美軍露天燃燒／引爆與高氯酸鹽飲用水傳導", "mil"),
    "2026-10-23-17": ("gnss-spoofing-civil-aviation", "民用 GNSS 偽造如何變成航路與管制風險", "mil"),
    "2026-10-23-20": ("san-joaquin-subsidence-flood-levee", "聖喬昆谷地陷：地下水超抽轉防洪與輸水危機", "civil"),
    "2026-10-24-03": ("ai-training-energy-carbon-estimates", "AI 訓練能耗與碳排估算口徑落差", "ai"),
    "2026-10-24-04": ("ai-code-sa-scanner-divergence", "AI 生成代碼嘅靜態掃描器安全分數分歧", "ai"),
    "2026-10-24-05": ("sepsis-ai-model-outcome-benefit", "專有敗血症 AI 模型能否改善病人結果", "bio"),
    "2026-10-24-08": ("ev-tyre-wear-non-exhaust-pm", "電動車煞車減磨與輪胎增磨對非排氣 PM 的淨效應", "civil"),
    "2026-10-24-09": ("industrial-robot-nonroutine-injury", "工業機器人非正常狀態傷亡集中與官方統計低估", "mech"),
    "2026-10-24-13": ("saf-fuel-specification-limit", "可持續航空燃料：燃料規格先撞到引擎", "mil"),
    "2026-10-24-15": ("perchlorate-national-mcl-conflict", "高氯酸鹽：EPA 擬議規則與健康風險嘅矛盾", "env"),
    "2026-10-24-16": ("demining-funding-output-concentration", "排雷資金縮減與清除面積跌幅唔對稱", "mil"),
    "2026-10-24-17": ("nij-44mm-backface-deformation", "NIJ 44 mm 背形變形合格與軀幹內臟傷", "mil"),
    "2026-10-24-19": ("tungsten-vs-uranium-armor-penetration", "美軍穿甲彈由鈾合金轉鎢合金嘅代價", "mil"),
    "2026-10-24-20": ("ammonium-perchlorate-mcl-thyroid", "高氯酸銨飲用水 MCL 選項與甲狀腺風險門檻", "env"),
    "2026-10-24-21": ("burn-pit-compliance-gap", "美軍燃燒坑規則收緊後仍有人受損嘅制度缺口", "mil"),
    "2026-10-24-22": ("military-pfas-foam-phaseout-gap", "美軍 PFAS 泡沫禁令嘅終止污染與替代物遷移", "env"),
    "2026-10-25-02": ("antivehicle-mine-survivability", "同一枚反車載地雷點解有人只傷有人死", "mil"),
    "2026-10-25-03": ("push-pull-g-force-indisposition", "負 G 轉正 G 嘅飛行員短暫失能邊界", "mil"),
    "2026-10-25-07": ("low-intensity-blast-cumulative-dose", "低強度爆炸訓練嘅累計劑量與腦健康", "mil"),
    "2026-10-25-08": ("underbody-blast-foot-injury", "車底爆震傷及足部嘅證據鏈", "mil"),
    "2026-10-25-10": ("arctic-permafrost-military-foundations", "北極軍事基地凍土融化嘅基礎設施風險", "mil"),
    "2026-10-25-14": ("deep-submergence-hull-certification", "深潛載具壓力殼獨立檢驗與 96 小時救援", "mil"),
    "2026-10-25-15": ("naval-hull-fouling-fuel-cost", "海軍船殼污損嘅水阻與油耗成本落差", "mil"),
    "2026-10-25-17": ("perchlorate-military-groundwater-detachment", "過氯酸銨基地地下水污染與聯邦規則脫節", "mil"),
    "2026-10-25-18": ("perchlorate-groundwater-remediation", "高氯酸鹽基地地下水污染嘅形成與修復代價", "mil"),
    "2026-10-25-20": ("undersea-munitions-bivalve-bioaccumulation", "海底廢彈場內爆炸物嘅貽貝累積路徑", "mil"),
    "2026-10-26-02": ("military-training-dust", "沙漠軍用訓練場揚塵：碾壓、濕度與車次取捨", "mil"),
    "2026-10-26-20": ("erw-clearance-engineering", "地雷／未爆彈清除工程：搜尋面積主導成本", "mil"),
}

# 已存在章節檔嘅 topic id → 對齊用（人工章節檔名同 topic id 唔一致嘅修正）
ID_RENAMES = {
    "hearing-loss-cognitive-intervention": "hearing-cognition-risk-stratified",
    "nitrogen-nitrogen-use-efficiency": "nitrogen-nue-loss-reduction",
    "perovskite-tandem": "perovskite-tandem-lcoe-warranty",
}

# edu 主題下嘅四個子章節檔（無獨立報告，掛喺 2026-10-22-14 之下）
EDU_SUBCHAPTERS = [
    ("01-secondary-foundation", "中學基礎與副學位路徑", "edu"),
    ("02-subdegree-certificate", "副學位與證書路徑", "edu"),
    ("03a-bachelors-civil-mech-elec", "學士三分支（Civil／Mechanical／Electrical）", "edu"),
    ("04-postgraduate-research", "研究生（碩士／博士）層級", "edu"),
]

CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")


def log(msg: str) -> None:
    print(f"[sync] {msg}", flush=True)


def load_index() -> dict:
    return json.loads(INDEX.read_text()) if INDEX.exists() else {"reports": {}}


def passed_reports() -> list[str]:
    """全部過閘且未歸檔嘅報告 stamp。"""
    idx = load_index()
    reps = idx.get("reports", {}) if isinstance(idx.get("reports"), dict) else {}
    out = []
    for f in sorted(REPORTS.glob("*.md")):
        if f.name == "index.md":
            continue
        e = reps.get(f.stem, {})
        if e.get("gate_pass") and not e.get("archived"):
            out.append(f.stem)
    return out


def parse_report(stamp: str) -> dict:
    """抽報告嘅主題、核心發現 bullet、來源數。"""
    txt = (REPORTS / f"{stamp}.md").read_text()
    topic = ""
    m = re.search(r"^###\s*主題\s*/\s*Topic\s*\n+(.+?)(?:\n\s*\n|$)", txt, re.M | re.S)
    if m:
        topic = " ".join(m.group(1).split())
    bullets = []
    b = re.search(r"^###\s*核心發現\s*/\s*Key Findings\s*\n+(.+?)(?=\n###\s)", txt, re.M | re.S)
    if b:
        for line in b.group(1).split("\n"):
            line = line.strip()
            if line.startswith("- "):
                bullets.append(line[2:].strip())
    srcs = len(re.findall(r"^- .*https?://", txt, re.M))
    return {"stamp": stamp, "topic": topic, "bullets": bullets, "sources": srcs,
            "bytes": len(txt.encode()), "cjk": len(CJK.findall(txt))}


def slug_notes(info: dict) -> str:
    """由核心發現抽一條濃縮 notes（誠實標註，唔誇大）。"""
    if not info["bullets"]:
        return "（章節待補：報告無核心發現段落）"
    first = info["bullets"][0]
    first = re.sub(r"^【[^】]+】", "", first)
    if len(first) > 110:
        first = first[:108] + "…"
    n = len(info["bullets"])
    return f"{first}（共 {n} 條核心發現、{info['sources']} 條來源）"


def sync_topics() -> int:
    """合併缺失 entry 落 topics.json；人工寫過嘅 entry 原樣保留。"""
    tp = json.loads(TOPICS.read_text())
    topics = tp["topics"]
    by_id = {t["id"]: t for t in topics}
    have_report = {t.get("last_report") for t in topics}

    added = 0
    for stamp in passed_reports():
        if stamp in have_report:
            continue
        slug, title, dom = SLUGS.get(stamp, (None, None, None))
        if slug is None:
            log(f"  ! {stamp} 冇人工 slug 對照，跳過（需人手指定）")
            continue
        info = parse_report(stamp)
        if slug in by_id:
            # slug 已存在（例如 erw 已加咗但未寫 last_report）→ 更新 last_report
            by_id[slug]["last_report"] = stamp
            have_report.add(stamp)
            continue
        topics.append({
            "id": slug,
            "title": title,
            "domain": dom,
            "status": "building",
            "coverage": 0.5,
            "last_report": stamp,
            "notes": slug_notes(info),
            "domain_code": dom,
        })
        by_id[slug] = topics[-1]
        have_report.add(stamp)
        added += 1

    # id 改名（對齊人工章節檔名）
    for old, new in ID_RENAMES.items():
        if old in by_id and new not in by_id:
            by_id[old]["id"] = new
            log(f"  ~ id 改名 {old} → {new}")

    # edu 子章節
    for sid, title, dom in EDU_SUBCHAPTERS:
        if sid in by_id:
            continue
        topics.append({
            "id": sid, "title": title, "domain": dom, "status": "building",
            "coverage": 0.45, "last_report": "2026-10-22-14",
            "notes": "工程教育路徑總覽（報告 2026-10-22-14）拆出嘅子章節。",
            "domain_code": dom,
        })
        by_id[sid] = topics[-1]
        added += 1

    tp["updated_utc"] = "2026-10-27T07:10:00Z"
    tp["topics"] = topics
    TOPICS.write_text(json.dumps(tp, ensure_ascii=False, indent=2))
    log(f"topics.json：新增 {added} 條，現共 {len(topics)} 條")
    return added


SECTION_TMPL = """# {title}

領域：{domain} ｜ 主題 slug：`{slug}` ｜ 對應報告：`{stamp}`

## 核心事實

{bullets}

## 量化鏈與口徑

- 來源數：{sources}；報告篇幅：{bytes} bytes / {cjk} 中文字。
- 本章節由 `sync_state.py` 從報告正文抽取，用作防重複登記與知識索引；
  細節以存檔版報告正文為準（`reports/{stamp}.md`）。

## 誠實邊界

{boundary}

## 相關條目

- 知識庫索引：`knowledge/INDEX.md`
- 主題登記：`knowledge/topics.json` → `{slug}`
"""


def sync_sections() -> int:
    """為缺章節嘅 topic 生成章節檔（已存在嘅人工章節唔郁）。"""
    tp = json.loads(TOPICS.read_text())
    made = 0
    for t in tp["topics"]:
        sid = t["id"]
        path = SECTIONS / f"{sid}.md"
        if path.exists():
            continue
        stamp = t.get("last_report")
        if not stamp or not (REPORTS / f"{stamp}.md").exists():
            continue
        info = parse_report(stamp)
        if not info["bullets"]:
            continue
        bullets = "\n".join(f"- {b}" for b in info["bullets"][:8])
        boundary = (
            "本條目由自動抽取生成，**未經獨立重新查證**；引用前必須回讀存檔版報告正文與原始來源。"
            "報告自述嘅缺口（見簡評段）在此原樣保留，唔會被稀釋成更強嘅斷言。"
        )
        path.write_text(SECTION_TMPL.format(
            title=t["title"], domain=t.get("domain", ""), slug=sid, stamp=stamp,
            bullets=bullets, sources=info["sources"], bytes=info["bytes"], cjk=info["cjk"],
            boundary=boundary,
        ))
        made += 1
    log(f"knowledge/sections：新增 {made} 個章節，現共 {len(list(SECTIONS.glob('*.md')))} 個")
    return made


def sync_state() -> None:
    """由 reports/index.json 推導統計，唔手寫。"""
    idx = load_index()
    reps = idx.get("reports", {}) if isinstance(idx.get("reports"), dict) else {}
    tot = len(reps)
    pend = sum(1 for r in reps.values() if not r.get("gate_pass") or r.get("archived"))
    # stamp 係 entry key（格式 YYYY-MM-DD-HH），唔係 entry 內嘅欄位
    stamps = sorted(k for k in reps if re.fullmatch(r"\d{4}-\d{2}-\d{2}-\d{2}", k))
    last = ""
    if stamps:
        d, hh = stamps[-1].rsplit("-", 1)
        last = f"{d}T{int(hh):02d}:00:00Z"

    st = json.loads(STATE.read_text())
    before = (st.get("reports_total"), st.get("reports_pending"), st.get("last_report_utc"))
    st["reports_total"] = tot
    st["reports_pending"] = pend
    st["last_report_utc"] = last
    st["updated_utc"] = "2026-10-27T07:10:00Z"

    # topic_performance key 對齊 topics.json id
    tp = json.loads(TOPICS.read_text())
    valid = {t["id"] for t in tp["topics"]}
    perf = st.get("topic_performance", {})
    # 合併同名 id（-exposure 之類多餘 suffix）
    for k in list(perf.keys()):
        if k in valid:
            continue
        base = k.removesuffix("-exposure")
        if base in valid:
            perf.setdefault(base, {}).update(perf.pop(k))
    # id 改名 → perf key 一齊改名（唔會斷指標）
    for old, new in ID_RENAMES.items():
        if old in perf and new not in perf:
            perf[new] = perf.pop(old)
            log(f"  ~ perf key 改名 {old} → {new}")

    # 為未有 perf 記錄嘅 topic 由報告推導一條（deterministic，唔虛構評分）
    for t in tp["topics"]:
        sid = t["id"]
        if sid in perf:
            continue
        stamp = t.get("last_report")
        if not stamp or not (REPORTS / f"{stamp}.md").exists():
            continue
        info = parse_report(stamp)
        cov = float(t.get("coverage", 0.0))
        perf[sid] = {
            "reports": 1,
            "coverage_before": 0.0,
            "coverage_after": round(cov, 2),
            "verdict": "pending",
            "pass": 0,
            "fail": 0,
            "notes": (f"由 sync_state.py 由 {stamp} 報告自動登記："
                      f"{info['sources']} 條來源、{info['cjk']} 中文字。"
                      f"用戶評分未記錄，故 verdict=pending（唔當作合格）。"),
        }

    st["topic_performance"] = perf

    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=2))
    log(f"state.json 統計：total {before[0]}→{tot}、pending {before[1]}→{pend}、last {before[2]}→{last}")
    log(f"topic_performance key 對齊後：{len(perf)} 條（topics.json {len(valid)} 條）")


def main() -> None:
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("topics", "all"):
        sync_topics()
    if what in ("sections", "all"):
        sync_sections()
    if what in ("state", "all"):
        sync_state()


if __name__ == "__main__":
    main()

"""報告 → 領域分類。

用戶要求：網站報告索引要有工程分類分頁（機械／土木／軍事／生技…）。

分類來源（三層 fallback，愈前愈可靠）：
  1. 報告檔內 `領域：<code>` metadata 行（新版報告由 cron 寫入）
  2. knowledge/topics.json 嘅 domain_code（透過 title → topic 匹配）
  3. 標題關鍵詞啟發式（中文 + 英文）

分類碼沿用 quota.py 嘅 ALL_DOMAINS，避免兩套 vocab 打架。
"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent
TOPICS = REPO / "knowledge" / "topics.json"

# 沿用 quota.py 定義
CORE = {
    "ai": "AI 工程",
    "mech": "機械工程",
    "mil": "軍事工程",
    "civil": "土木工程",
}
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

# 顯示順序：核心優先，然後其他
DOMAIN_ORDER = ["ai", "mech", "civil", "mil", "elec", "mat", "energy", "env",
                "chem", "bio", "agri", "edu", "other"]

# 標題關鍵詞 → domain code。
# ⚠️ 順序即優先度：越專門嘅 domain 越要排前面。
# 反面教材：mil 排第一時，「PFAS 泡沫／飲用水／鹽化」全部被誤判成軍事。
# 修正做法：(1) 保留專門詞但要求同時出現軍事詞；(2) 通用詞（PFAS、飲用水、
# 混凝土、太陽能）唔可以單獨決定 mil/ai。
KEYWORDS: list[tuple[str, tuple[str, ...]]] = [
    # --- 專門詞優先：軍事必須有明確軍事語彙 ---
    ("mil", ("美軍", "軍方", "軍用", "軍隊", "軍事", "地雷", "排雷", "反車輛地雷",
             "反車載", "背形變形", "穿甲彈", "高氯酸銨", "高氯酸鹽",
             "燃燒坑", "航煤", "SAF 混掺", "基地污染", "無人機", "雷達",
             "GPS 偽造", "排障維修軍事", "飛行員", "G 力", "空勤",
             "militar", "army", "munition", "landmine", "armor", "ammo",
             "defense", "naval", "radar", "soldier", "battlefield",
             "explosive", "ordnance", "demining", "drone", "warfighter",
             "鉛檢測", "私營家庭住宅已無鉛害", "軍宅")),
    # --- 醫療／生技：疾病、臨床、藥物名先於通用健康詞 ---
    ("bio", ("疫苗", "瘧疾", "抗藥性", "抗生素", "抗藥", "敗血症", "臨床",
             "失智", "認知障礙", "助聽", "聽力", "糖尿病", "癌症", "腫瘤",
             "感染", "病人", "死亡率", "死亡人數", "臨床試驗", "隨機對照",
             "epidemiolog", "mortality", "clinical", "vaccine", "cancer",
             "antibiotic", "infection", "dementia", "cognitive", "hearing",
             "malaria", "sepsis", "patient", "disease", "trial")),
    ("ai", ("AI ", "AI，", "AI數據", "AI 數據", "AI 訓練", "AI 生成", "AI 模型",
            "AI 編碼", "幻覺", "npm", "大模型", "神經網絡", "深度學", "LLM",
            "GPT", "Transformer", "token", "prompt", "inference", "neural",
            "hallucinat", "CodeQL", "Bandit", "Bearer", "套件", "supply chain",
            "模型碳足跡", "碳足跡", "演算法", "agentic", "benchmark",
            "開源模型")),
    ("mech", ("機械", "機床", "軸承", "刀具", "渦輪機", "內燃機", "風機",
              "壓縮機", "CNC", "金屬疲勞", "疲勞失效", "機械臂", "工業機器人",
              "鍛造", "鑄造", "表面精加工", "3D 列印", "HIP", "RCM",
              "機油", "油霧", "磨損", "車重", "輪胎", "machin", "turbine",
              "engine", "bearing", "tool wear", "fatigue", "robot", "surface",
              "lubricant", "coolant")),
    ("civil", ("土木", "橋樑", "橋", "隧道", "公路", "鐵路", "水利", "防洪",
               "堤", "沉降", "地陷", "排水", "污水", "建築", "結構工程",
               "混凝土", "鋼筋", "岩土", "滑坡", "崩塌", "地震", "水庫",
               "除冰鹽", "腐蝕", "鹽化", "飲用水", "自來水", "供水",
               "bridge", "tunnel", "rail", "roadway", "concrete", "rebar",
               "geotech", "landslide", "seismic", "dam", "levee", "flood",
               "building", "infrastructure", "construction", "hydraulic",
               "sanitation", "water treatment", "climate adapt", "salinity",
               "groundwater", "landfill", "slope")),
    ("elec", ("電網", "電路", "變壓器", "配電", "半導體", "晶片", "諧波",
              "功率品質", "電容", "感測器", "PCB", "充電樁", "電動車充電",
              "電氣", "電訊", "電站", "輸電",
              "electric", "circuit", "transformer", "power quality",
              "semiconductor", "chip", "harmonic", "voltage", "sensor",
              "charging", "battery", "capacitor", "PCB")),
    ("mat", ("材料", "水泥", "銅價", "銅礦", "礦場", "冶煉", "合金", "鈣鈦礦",
             "太陽能電池", "矽堆疊", "鈦", "稀土", "石墨烯", "陶瓷",
             "鋁", "鈾", "鎢", "樹脂",
             "material", "cement", "copper", "mining", "smelting", "alloy",
             "perovskite", "tandem", "ceramic", "polymer", "composite",
             "steel", "uranium", "tungsten", "battery material", "casting")),
    ("energy", ("能源", "電力", "發電", "風電", "核能", "核電", "儲能",
                "電池儲", "油氣", "天然氣", "氫能", "生物質", "電價", "能源",
                "energy", "power market", "nuclear", "storage", "hydrogen",
                "coal", "retail price", "tariff", "VPP", "electricity",
                "renewable", "hydroelectric", "核電站")),
    ("env", ("環境", "污染", "空氣質", "PM2.5", "水質", "廢水", "塑膠",
             "回收", "重金屬", "噪音", "環境健康", "職業熱害", "熱死亡",
             "PFAS 泡沫", "環境",
             "environment", "pollution", "air quality", "PM2.5", "water quality",
             "wastewater", "recycl", "plastic", "emission", "contaminant",
             "heat illness", "occupational")),
    ("chem", ("化學", "化工", "催化劑", "反應釜", "溶劑", "合成", "電解質",
              "perchlorate", "chemical", "catalys", "solvent", "synthesis",
              "electrochem", "electrolyte", "反應", "酸")),
    ("agri", ("農業", "作物", "氮肥", "氮效率", "土壤", "灌溉", "畜牧",
              "農藥", "化肥", "agricultur", "crop", "nitrogen", "soil",
              "irrigat", "livestock", "farm", "fertiliz", "農場")),
    ("edu", ("教育", "課程", "學士", "碩士", "博士", "學分", "大學", "培訓",
             "educat", "curricul", "course", "degree", "university", "student",
             "pedagog", "accredit", "畢業", "入學", "升學")),
]


def _load_topics() -> list[dict]:
    try:
        return json.loads(TOPICS.read_text()).get("topics", [])
    except Exception:
        return []


def _topic_domain_index() -> dict[str, str]:
    """title 關鍵字 → domain_code（由 topics.json 提供）。"""
    idx: dict[str, str] = {}
    for t in _load_topics():
        dc = t.get("domain_code")
        if not dc:
            continue
        title = t.get("title", "")
        idx[title] = dc
        # 用 topic id 嘅 slug 詞做關鍵字
        for part in t.get("id", "").split("-"):
            if len(part) >= 4:
                idx[part] = dc
    return idx


def classify_title(title: str, body: str = "") -> str:
    """標題 → domain code。回傳 'other' 表示無法判定。

    只用**標題**做關鍵詞匹配：body 會帶入英文對照段，令不相關的詞
    （例如 PFAS、Solar）誤觸發。body 只留作最後 fallback。
    """
    if not title:
        return "other"
    t = title.lower()

    # 1. topics.json 精確標題匹配
    tidx = _topic_domain_index()
    if title in tidx:
        return tidx[title]

    # 2. 關鍵詞（只查標題）
    for code, words in KEYWORDS:
        for w in words:
            if w.lower() in t:
                return code

    # 3. 啟發式 fallback：body 只喺標題完全冇線索時先用
    if body:
        bt = body[:400].lower()
        for code, words in KEYWORDS:
            for w in words:
                if w.lower() in bt:
                    return code
    return "other"


def classify_report(text: str, title: str) -> dict:
    """報告全文 → {code, name, source}。

    source: 'meta' = 報告檔有 `領域：` 行；'topics' = topics.json 命中；
            'keywords' = 關鍵詞；'fallback' = 其他。
    """
    m = re.search(r"^\s*(?:#{1,3}\s*)?\**領域\**\s*[：:]\s*([a-z]+)\s*$",
                  text, re.M | re.I)
    if m:
        code = m.group(1).lower()
        if code in ALL_DOMAINS:
            return {"code": code, "name": ALL_DOMAINS[code], "source": "meta"}

    tidx = _topic_domain_index()
    for t, dc in tidx.items():
        if len(t) >= 6 and t in title:
            return {"code": dc, "name": ALL_DOMAINS.get(dc, dc), "source": "topics"}

    code = classify_title(title, text)
    return {
        "code": code,
        "name": ALL_DOMAINS.get(code, code),
        "source": "keywords" if code != "other" else "fallback",
    }

#!/usr/bin/env python3
"""科研哨兵 報告品質閘 (Report Quality Gate)

用法:
  python3 quality_gate.py <report.md>          # 檢查；exit 0 = 通過, 1 = 不通過
  python3 quality_gate.py <report.md> --json   # JSON 輸出

依據 docs/REPORT_CONTRACT.md 檢查：固定五段結構、篇幅、來源數、禁例、生命狀態行。
"""
import json
import os
import re
import sys

CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
REQUIRED = [
    ("主題", "Topic"),
    ("核心發現", "Key Findings"),
    ("潛在影響", "Potential Impact"),
    ("來源依據", "Sources"),
    ("簡評", "Commentary"),
]
FORBIDDEN_SUBSTR = [
    "（填充中）", "填充中", "TODO", "TBD", "（待補", "待填補", "XXX",
]
FORBIDDEN_HEAD = [
    "本期摘要", "Executive Summary", "進度報告", "知識庫填充", "章節填充",
]
INTERNAL_SUBJ = [
    "知識庫填充", "章節填充", "知識庫建設", "知識庫進度", "本期完成", "施工日誌",
    "知識庫", "已填充", "填補", "進度報告",
]
# 主題段不可描述「我做了什麼基建」；允許在簡評單獨一句交代知識庫
INTERNAL_COMBO = [
    ("知識庫", "填充"), ("知識庫", "建設"), ("知識庫", "進度"),
    ("本期", "完成"), ("章節", "填充"), ("知識庫", "已"),
]
MAX_CJK = 1000
MIN_CJK = 100
MAX_BYTES = 9000
MAX_HEADINGS = 12


def cjk_count(s):
    return len(CJK.findall(s))


def parse(text):
    heads = {}
    order = []
    cur = None
    for ln in text.splitlines():
        m = re.match(r"^\s{0,3}#{1,6}\s+(.*\S)\s*$", ln)
        if m:
            cur = m.group(1).strip()
            heads.setdefault(cur, [])
            order.append(cur)
            continue
        if cur is not None:
            heads[cur].append(ln)
    return heads, order


def find_head(heads, token):
    for h, body in heads.items():
        if token.lower() in h.lower():
            return h, "\n".join(body)
    return None, None


def main():
    if len(sys.argv) < 2:
        print("usage: quality_gate.py <report.md> [--json]")
        return 2
    path = sys.argv[1]
    as_json = "--json" in sys.argv
    if not os.path.exists(path):
        print(f"FAIL: 檔案不存在 / file not found: {path}")
        return 1
    raw = open(path, "rb").read()
    text = raw.decode("utf-8", "ignore")
    heads, order = parse(text)

    fails, warns, oks = [], [], []

    # H1 固定五段（中英都要）
    missing = []
    for zh, en in REQUIRED:
        hz, _ = find_head(heads, zh)
        he, _ = find_head(heads, en)
        if hz is None:
            missing.append(f"缺少中文段落標題「{zh}」")
        if he is None:
            missing.append(f"missing English heading 「{en}」")
    if missing:
        fails.append("H1 結構: " + "; ".join(missing))
    else:
        oks.append("H1 五段結構齊備（中英）")

    # H2 佔位符
    hits = [t for t in FORBIDDEN_SUBSTR if t in text]
    if hits:
        fails.append(f"H2 佔位符殘留: {hits}")
    else:
        oks.append("H2 無佔位符")

    # H3/H4 篇幅
    n_cjk = cjk_count(text)
    if n_cjk > MAX_CJK:
        fails.append(f"H3 中文字數 {n_cjk} 超過上限 {MAX_CJK}")
    elif n_cjk < MIN_CJK:
        fails.append(f"H4 中文字數 {n_cjk} 低於下限 {MIN_CJK}")
    else:
        oks.append(f"篇幅 OK（中文字數 {n_cjk}，{len(raw)} bytes）")

    # H5 bytes
    if len(raw) > MAX_BYTES:
        fails.append(f"H5 全文 {len(raw)} bytes 超過 {MAX_BYTES}")
    else:
        oks.append(f"H5 bytes OK（{len(raw)}/{MAX_BYTES}）")

    # H6 來源數
    _, src_body = find_head(heads, "來源依據")
    if src_body is None:
        _, src_body = find_head(heads, "Sources")
    sb = src_body or ""
    src_urls = sorted(set(re.findall(r"https?://[^\s)）\]，、]+", sb)))
    src_bullets = [l for l in sb.splitlines()
                   if re.match(r"^\s*[-*•]", l)]
    n_src = min(len(src_urls), len(src_bullets))
    if n_src < 2:
        fails.append(
            f"H6 來源依據不足：{len(src_bullets)} 條列項、{len(src_urls)} 個 URL，最少 2 個獨立來源")
    else:
        oks.append(f"H6 來源 {n_src} 條（{len(src_urls)} 個 URL）")

    # H9 行號污染（read_file 輸出被直接覆寫檔案的典型後果）
    if re.search(r"^\s*\d+\|", text, re.M):
        fails.append("H9 檔案含 read_file 行號污染（^\\s*\\d+\\|）")
    else:
        oks.append("H9 無行號污染")

    # H10 來源段不可用數字編號（品質閘只認 - / * 項目符號）
    if sb:
        numbered = [l for l in sb.splitlines() if re.match(r"^\s*\d+[.、)]\s*\S", l)]
        if numbered and not src_bullets:
            fails.append("H10 來源段用數字編號，品質閘只認 - / * 項目符號；請改寫為 - 開頭")
        else:
            oks.append("H10 來源編號格式 OK")

    # H7 主題不得為內部施工
    _, topic_body = find_head(heads, "主題")
    if topic_body is None:
        _, topic_body = find_head(heads, "Topic")
    tb = topic_body or ""
    if not tb.strip():
        # 沒有「主題」標題時，退而檢查標題區（前 20 行）
        tb = "\n".join(text.splitlines()[:20])
    found = [k for k in INTERNAL_SUBJ if k in tb]
    combos = [f"{a}+{b}" for a, b in INTERNAL_COMBO if a in tb and b in tb]
    if found or combos:
        fails.append(f"H7 主題段屬內部施工敘述: 詞={found} 組合={combos}")
    else:
        oks.append("H7 主題為獨立科研問題")

    # H8 生命狀態行
    if "生命狀態" in text and re.search(r"L\d+", text):
        oks.append("H8 含生命狀態行")
    else:
        fails.append("H8 缺少『生命狀態：剩餘 N 小時，等級 L{L}』結尾行")

    # W1 禁止標題
    bad_heads = [h for h in order if any(k.lower() in h.lower() for k in FORBIDDEN_HEAD)]
    if bad_heads:
        warns.append(f"W1 施工式標題: {bad_heads}")
    # W2 施工式敘述
    story_hits = [k for k in ["共新增", "本期完成", "已填充", "知識庫完成"] if k in text]
    if story_hits:
        warns.append(f"W2 施工式敘述: {story_hits}")
    # W3 標題數
    if len(order) > MAX_HEADINGS:
        warns.append(f"W3 標題數 {len(order)} 偏多（> {MAX_HEADINGS}），應收斂為五段")
    # W4 每段最小內容量
    for zh, en in REQUIRED:
        _, b = find_head(heads, zh)
        if b is not None and cjk_count(b) < 30:
            warns.append(f"W4 段落「{zh}」中文字數 {cjk_count(b)} 偏少")
    # W5 英文段長度
    for zh, en in REQUIRED:
        _, b = find_head(heads, en)
        if b is not None and len(re.findall(r"[A-Za-z]{2,}", b)) < 25:
            warns.append(f"W5 段落「{en}」英文內容偏少")
    # W6 機制分析（用戶反饋：核心發現偏事實羅列，缺少「為什麼」的機制分析）
    _, kf_body = find_head(heads, "核心發現")
    kf = kf_body or ""
    if "【機制】" not in kf and "【機制】" not in text:
        warns.append("W6 核心發現缺少【機制】條目：只講「是怎樣」而冇講「為什麼會這樣」")
    # W7 量化估計（用戶反饋：潛在影響幾乎全是【推論】，缺少具體數字或案例）
    # 必須是「量化指標」（金額／比率／容量／人數／年數），單純溫度門檻值不算
    _, pi_body = find_head(heads, "潛在影響")
    pi = pi_body or ""
    QUANT = re.compile(
        r"[$€£¥]\s?\d|\d+\s*(?:%|percent|美元|美金|元|兆|億|萬|"
        r"MW|GW|kW|TWh|MWh|GWh|宗|人|名|起|倍|年|萬人|億人)")
    quant_lines = [l for l in pi.splitlines() if QUANT.search(l)]
    if not quant_lines:
        warns.append("W7 潛在影響段冇任何量化指標（金額／比率／容量／人數／年數）："
                     "應至少有一條【推論】附具體數字或可稽核案例")
    # W7b 潛在影響全部都係推論 → 零事實支撐
    pi_bullets = [l for l in pi.splitlines() if re.match(r"^\s*[-*•]", l)]
    if pi_bullets and all("【推論】" in l for l in pi_bullets):
        warns.append("W7b 潛在影響全部條目都係【推論】，零事實支撐")
    # W8 推論必須標記（事實與推論分離）
    if "【推論】" not in text:
        warns.append("W8 全文冇【推論】標記：推論與事實必須分離")
    # W9 敏感度分析（用戶反饋：VPP 的 56 美元節省完全依賴 Brattle 模型假設，缺乏敏感度分析）
    # 凡核心發現提到模型／預測／情景數字，必須附一個替代情境或敏感度說明
    MODEL_NUM = re.compile(r"模型|預測|估算|推算|情景|假設|scenario|model|projection|estimate")
    SENS = re.compile(r"【敏感度】|【情境】|【替代假設】|【替代情境】|敏感度|替代情境|替代假設|上下限|若假設|假設若|區間")
    if MODEL_NUM.search(kf) and not SENS.search(kf):
        warns.append("W9 核心發現提到模型／預測數字但冇敏感度或替代情境："
                     "須加【敏感度】或【替代假設】條目，說明假設改變後結論如何變動")
    # W10 具體案例（用戶反饋：潛在影響缺少更具體的傳導路徑或州級案例）
    CASE = re.compile(r"案例|州|省|城市|某市|實測|示範|試點|現場|實地|個案|示範區")
    if not CASE.search(pi):
        warns.append("W10 潛在影響冇任何具體案例（州／城市／示範／實測）："
                     "須至少給一個可核查的具體傳導路徑或案例")

    result = {"file": path, "pass": not fails, "cjk": n_cjk, "bytes": len(raw),
              "sources": n_src, "fails": fails, "warnings": warns, "ok": oks}
    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"=== 品質閘 / Quality Gate: {path} ===")
        print(f"中文字數 {n_cjk} | bytes {len(raw)} | 來源 {n_src}")
        for o in oks:
            print(f"  PASS  {o}")
        for w in warns:
            print(f"  WARN  {w}")
        for f in fails:
            print(f"  FAIL  {f}")
        print("RESULT:", "PASS" if not fails else "FAIL")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())

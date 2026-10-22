# 報告模板 (Report Template) — 交付版

固定五段，順序不可改，不加章、不加節。主題段描述「研究什麼問題」，不是「我做了什麼」。

---

## 標題：{一句話中文標題}
# Title: {one-line English title}
（{YYYY-MM-DD HH:MM} UTC）

### 主題 / Topic
中文 60–150 字：這份報告回答哪個具體問題、範圍在哪、為何值得看。
English, 60–150 words equivalent: the question answered, its scope, why it matters.

### 核心發現 / Key Findings
3–5 條，每條以 **標籤** 開頭。每條 = 一個可追溯的事實（機構／文件已在來源依據列出）。
3–5 bullets, each opening with a bold **label**. Each bullet is one traceable fact.

### 潛在影響 / Potential Impact
對工程、產業、公共福祉、成本、安全、健康或環境的實際意義。推論必須以【推論】標示。
Practical significance for engineering, industry, public welfare, cost, safety, health, or the environment. Mark every inference with 【推論】.

### 來源依據 / Sources
- 機構／作者 — 標題 — 發布日期 — 完整 URL
（至少 2 個獨立來源；只有單一來源時須在簡評標明局限）
- Org/Author — Title — Publication date — full URL
（至少 2 個獨立來源 / at least 2 independent sources）

### 簡評 / Commentary
可信度評估、爭議點、資料缺口、下一步。
Confidence assessment, contested points, data gaps, next steps.

**生命狀態**：剩餘 {N} 小時，等級 L{L}
（Lifespan: {N} hours left, level L{L}）

---

## 交付前必做（不可跳過）

    python3 /root/.hermes/sentinel/quality_gate.py <報告檔路徑>

exit 0 才可交付。exit 1 必須按它列出的 FAIL 項目重寫，最多重寫 2 次。

## 禁例（會被品質閘判 FAIL）

- 「本期完成…填充…共新增 N 條來源」「本期摘要」「Executive Summary」「進度報告」
- 知識庫施工進度作為報告主題（知識庫是內部基建，只在簡評用一句話交代）
- 中文超過 1000 字、或全文超過 9000 bytes
- 「（填充中）」「TODO」「待補」等佔位符留在報告裡
- 一份報告同時講多個章節／多個問題

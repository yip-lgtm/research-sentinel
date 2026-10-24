# 知識庫索引

科研哨兵的持久化知識體系。所有內容寫入磁碟，不依賴單次對話記憶。

## 目錄

| 檔案 | 內容 | 狀態 |
|---|---|---|
| `amr-burden-age-divergence.md` | 抗藥性死亡負擔的年齡分化與治理槓桿（GRAM 2024、WHO 管線、丹麥黃卡、污水 ARG） | 建設中 |
| `engineering-education-path.md` | 工程教育路徑（中學 → 副學位 → 學士 → 碩博 → 地區差異 → 認證） | 建設中（頭兩小時） |
| `perovskite-tandem-lcoe-warranty.md` | 鈣鈦礦—矽堆疊：LCOE 門檻（29%→>21 年、32%→19 年）、CRF 融資年限敏感度、IEA 劣化機制、Oxford PV 保固落差 | 建設中 |
| `hearing-cognition-risk-stratified.md` | 助聽干預：ACHIEVE 總體陰性 vs 風險分層 61.6% 有效、中介路徑斷點、WHO HEAR ROI 所得梯度 | 建設中 |
| `nitrogen-nue-loss-reduction.md` | 氮效率：452 縣示範減氮增產、反應性氮流失機制、N2O 因子敏感度、經濟最佳率 vs 農藝最佳率 | 建設中 |
| `malaria-vaccine-mortality-mechanism.md` | 瘧疾疫苗：36% 效力 vs 13% 死亡下降的分母稀釋鏈、抗原多樣性、肯亞分母陷阱、交付成本結構 | 建設中 |
| `pfas-drinking-water-mcl.md` | PFAS 飲用水 MCL 4.0 ng/L：受監測超標人口、15.49 億美元成本、10.0 ng/L 敏感度、監測選擇偏差 | 建設中 |
| `coastal-bangladesh-salinity-health.md` | 海岸孟加拉飲用水鹽度：WHO「無基準值」的條件式失效、鈉負荷劑量—反應、健康成本與遷移風險傳導 | 建設中 |
| `domains/` | 各研究領域的長期累積筆記 | 依需求建立 |

## 覆蓋登記

已充分覆蓋的主題記錄在 `topics.json`，避免重複產出。目前 13 個主題，最高覆蓋率 0.78（edu-bachelor-branches）。

### 近期新增章節（2026-10-23）
- `perovskite-tandem-lcoe-warranty.md` ← 報告 `2026-10-22-21`（用戶評「合格」）
- `hearing-cognition-risk-stratified.md` ← 報告 `2026-10-22-22`（用戶評「合格」）
- `nitrogen-nue-loss-reduction.md` ← 報告 `2026-10-23-00`（未評分）
- `malaria-vaccine-mortality-mechanism.md` ← 報告 `2026-10-23-02`（品質閘 PASS）
- `pfas-drinking-water-mcl.md` ← 報告 `2026-10-23-01`（品質閘 PASS）
- `coastal-bangladesh-salinity-health.md` ← 報告 `2026-10-23-04`（用戶評「合格」）

### 品質閘修正記錄（2026-10-23 03:00）
- `2026-10-23-01`：H6 失敗（來源用 `1.` `2.` 數字編號，品質閘只認 `-`/`*` 項目符號）→ 改為 `-` 開頭
- `2026-10-23-02`：H5 失敗（9076 bytes > 9000）→ 精簡英文段落至 8998 bytes
- 教訓：報告結尾只留一行 `生命狀態：…`（中英雙寫會多佔約 40 bytes 且無增益）

## 原則

- 每份報告至少有一條新知識寫回知識庫（否則該報告只是噪音）
- 來源必須可追溯：URL + 發布日期 + 機構
- 發現與推論分開標註
- 覆蓋率低的主題優先；覆蓋率高的主題需有新進展才再寫
- 報告雙語化會令 bytes 翻倍：撰寫時直接用**中英分段散文**（非逐條鏡像），
  品質閘上限 9000 bytes／1000 中文字，中文段保留全部數字、英文段只留要點與數字
- ⚠️ 教訓：不要用 read_file 的輸出直接覆寫檔案（會把行號 `N|` 寫進檔案）。
  覆寫前必須確認內容不含 `^\s*\d+\|`；改檔用 patch／execute_code 讀原檔再用 write_file 寫回

### 品質閘修正記錄（2026-10-23 05:10）
- `2026-10-23-04`：初稿由 cron 輸出自動存檔，已過閘；手動修正流程陳述（刪「未存檔未過閘」過時敘述）、
  更新生命狀態行至 L6/44h → 重驗 PASS（738 中文字、8365 bytes、7 來源）
- **流程教訓**：cron `script` 欄位（finalize.py）保證存檔+閘+commit+push，
  即使 LLM 步驟撞工具上限都會自動完成 → 報告正文可以寫「未存檔」而實際已存檔，
  **下一輪要檢查 `reports/index.json` 確認實際狀態，唔好照抄 LLM 稿內嘅流程自述**

- 軍事工程與公共衛生｜mil｜美軍住宅兒童血鉛暴露（檢測率下降 vs 暴露源受控）｜building 0.5｜2026-10-23-19
- 土木工程／地質災害｜civil｜城市山泥傾瀉預警門檻：工程主導 vs 氣候主導｜building 0.5｜2026-10-23-21
  章節：`urban-landslide-thresholds-engineering-vs-climate.md`（品質閘 PASS，1000 中文字／6426 bytes／5 來源）

- 土木工程｜city-landslide-alert-thresholds｜building｜2026-10-24
- AI 工程｜ai-hallucinated-package-attack-surface｜building｜2026-10-24
- 土木工程｜rcm-field-durability-gap｜building｜2026-10-24
- 土木工程｜deicing-salt-bridge-safety｜building｜2026-10-24

- AI 工程｜ai-dev-productivity-rct-divergence｜building 0.5｜2026-10-24-07
  章節：`ai-dev-productivity-rct-divergence.md`（品質閘 PASS，912 中文字／8512 bytes／4 來源）
  METR 兩輪 RCT 與 Cui 等人《Management Science》三場現場實驗的量度分歧（耗時 vs 任務數）

- 機械工程｜mech｜metalworking-fluid-mist-oel-gap｜金屬切削液油霧：暴露限值落差與工程控制｜building 0.5｜2026-10-24-12
  章節：`metalworking-fluid-mist-oel-gap.md`（品質閘 PASS，997 中文字／8896 bytes／8 來源）
  OSHA 5 mg/m³（僅 straight oil）vs NIOSH 0.5 mg/m³ 的 10 倍落差；霧由流體＋刀具運動生成（轉速 2 與 3.5 次方）；
  HP 劑量—反應 4%/19%/34%；控制降幅 80%/87%；低於 REL 仍有皮膚炎 PR 2.59、工作相關哮喘 PR 2.10

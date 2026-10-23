# 城市山泥傾瀉預警門檻：工程主導 vs 氣候主導

- 首次寫入：2026-10-23 21:30 UTC
- 主題 id：urban-landslide-thresholds-engineering-vs-climate
- 狀態：building（coverage 0.5）
- domain：土木工程／地質災害（civil）

## 已驗證核心事實

1. **全球城市山泥傾瀉門檻「收斂」**：編纂 1,216 宗雨量觸發城市山泥傾瀉、涵蓋 26 城，以分層分位數回歸估算各城
   雨量強度—歷時門檻；**77% 城市的門檻中位數與全球平均無法區分**；**31% 的山泥傾瀉發生在年度降雨極值以下**
   （即中等暴雨即足以觸發）。作者推論：城市化把雨量門檻「同質化」，覆蓋了自然變異。
   來源：Luna, L.V. 等（2024）"Urban landslides triggered under similar rainfall intensities in cities globally",
   ESSOAr 預印本 — https://doi.org/10.22541/essoar.172745685.54713106/v1
   （摘要經 Crossref API 核對：https://api.crossref.org/works/10.22541/essoar.172745685.54713106/v1 ）

2. **Aburrá 谷地（Medellín）城市／郊區對比**：城市山泥傾瀉發生在**較平緩、較低海拔**的坡面，
   郊區則分布在較陡地形；雨量事件數與滑坡密度**無直接空間對應**；作者指出大量報告無對應強降雨，
   推測人為因素（無規管建築、開挖、排水系統破壞）比降雨本身更主導。**夜間報告更多**，
   指向持續低強度降雨而非雨峰；強度 ≥15 mm/h 的降雨事件只佔樣本約 **5%**，令雨量—滑坡相關性偏向低強度類別。
   來源：Aristizábal, E.V. 等 "Landslide timing and rainfall regimes in a rapidly urbanizing tropical mountain
   valley in Colombia", Natural Hazards（2026）— https://doi.org/10.1007/s11069-026-08028-6

3. **城市暴露規模（129 城普查）**：可辨識 **1,085 個現有人居住的大型滑坡（>0.1 km²）**；
   **1985–2015 年其上建成區面積倍增**，快過整體城市增長率；估計**至少 50 萬人住在滑坡上**，
   30 年平均建成區增 **12%**；**10% 城市暴露不成比例地高**；山區暴露增速快過通勤區，與國民收入無關。
   來源：Ferrer, L. 等（2025）"Exposure to Large Landslides in Cities Outpaces Urban Growth",
   Geophysical Research Letters 52 — https://doi.org/10.1029/2025GL115170（摘要經 Crossref 核對）

4. **Medellín 非正式聚落致死率**：非正式區（Informal I–III）平均位於坡度 **>19°** 山坡，正式區 **<13°**；
   非正式區每平方公里死亡人數是**最危險正式區的 2–3.5 倍**，而非正式區 2023 年只佔市區面積約 **9%**。
   1930 年代至 2023 年人口由約 12 萬增至 **250 萬**，面積由 **9 km² 增至 107 km²**；
   期間錄得 **206 宗致命滑坡、1,045 人死亡**。1987 年 Villatina 滑坡約 5 萬 m³ 殘土覆蓋多個街區，
   官方死亡人數從未確立，只尋回 199 具遺體、逾 300 人宣告失蹤。
   來源：Nieto, Aristizábal & Ozturk（2025）"Coupled evolution of a city and landslides",
   Environmental Research Letters 20, 054001 — https://doi.org/10.1088/1748-9326/adc4d8

5. **事前防治成本效益（單一集水區案例）**：義大利 pre-Alps（Vicenza, Marosticano 區，2010 年 11 月暴雨事件）：
   - Carrè 滑坡：事後整治 **€57,000** vs 事前排水溝 **€17,652** + 每年 **€400** 維護／檢查
   - 20 年政策期、**1.6% 折現率** → 事前措施**淨省 30%**（相對整治總成本）
   - 大尺度：無土體保護下 Vicenza 當局面對 **€3 億整治開支 + 約 €10 億基建與建築損失**；
     區域層面事前措施最多可省 **€300 萬**（約 50% 整治成本）
   - 低成本分析顯示 **2010 年事件後近 50% 的滑坡本可預見**
   來源：Salbego, G. 等（2015）"Detailed and large-scale cost/benefit analyses of landslide prevention vs.
   post-event actions", NHESS 15, 2461–2472 — https://nhess.copernicus.org/articles/15/2461/2015/

## 口徑陷阱

- **「77% 收斂」不等於「氣候不再影響城市滑坡」**：該結論只覆蓋**雨量觸發**記錄；開挖、地震、
  人工抽水等觸發機制被排除在樣本外，收斂只描述雨量觸發這一子集。
- **門檻數值本身未取得**：Luna 等的 q10/q50/q90 具體門檻值只在 ESSOAr 全文表格內，
  該站被 Cloudflare 阻擋（HTTP 403），本次未取得 → **不可引用任何具體 mm/h 或 mm/day 門檻值**。
- **城市／郊區口徑不一致**：Aburrá 谷地的城市判定同時使用「DAGRD 緊急求助名錄」與「Google Earth
  影像辨識名錄」，兩者對「城市」定義未必一致；Frequency Ratio 宜讀作**方向**而非精確比例。
- **報告偏差**：DAGRD 名錄來自緊急求助電話，天然偏向「已有住戶受影響處」，
  會高估人口密集區的滑坡密度。
- **30% 節省不可外推**：屬單一集水區、單一事件、20 年政策期、1.6% 折現率、特定排水溝設計。
  「事前比事後便宜 20 倍」之類說法**不屬本文結論**，勿引用。
- **「官方死亡人數從未確立」**：Villatina 事件的 199 具遺體／300+ 失蹤是**記錄缺口**，非確切死亡人數。

## 未解缺口（下一步工作）

- Luna 等的全球 q10/q50/q90 門檻值與逐城中位數（需繞過 ESSOAr 阻擋：查作者機構版、
  Zenodo、EGU24 幻燈片、或後續期刊版）
- 任何「採用城市專屬門檻前後死亡人數／經濟損失變化」的前後對照研究（本題完全空白）
- 不同城市的市政退界線（retreat line）執行率與其與滑坡暴露的關聯
- 排水基建失效率（blocked drainage / 無設計暴雨溢流）在城市滑坡名錄中的可量化佔比
- 129 城暴露普查的底層城市清單與分類標準（built-up area 判定規則）
- 非正式聚落坡度 >19° 與「低於 13°」的統計口徑（平均？中位？面積加權？）

# 農業氨（NH3）→ 二次 PM2.5 → 健康負擔：量化研究筆記

> 狀態：研究中（資料蒐集與量化，非報告）。所有數字附完整 URL 與來源機構。
> 最後更新：2026-10-22

## 0. 來源清單與核實狀態

| # | 機構 | 標題 | 日期 | URL | 已抓取原文 |
|---|---|---|---|---|---|
| S1 | EEA (歐洲環境署) | EMEP/EEA air pollutant emission inventory guidebook 2023, Ch.3.D Crop production and agricultural soils (NFR 3.D) | 2023 | https://www.eea.europa.eu/en/analysis/publications/emep-eea-guidebook-2023/part-b-sectoral-guidance-chapters/3-agriculture/3-d-agricultural-soils-2023/@@download/file | ✅ PDF 已下載解析 |
| S2 | EEA | Ammonia emissions from agriculture and other sources (Zero Pollution Dashboard Indicator) | 2025-03-03 (mod. 2025-04-24) | https://www.eea.europa.eu/en/european-zero-pollution-dashboards/indicators/ammonia-emissions-from-agriculture-and-other-sources-indicator | ✅ |
| S3 | EEA | Premature deaths due to exposure to fine particulate matter in Europe (indicator) | 2025-11-30 | https://www.eea.europa.eu/en/analysis/indicators/health-impacts-of-exposure-to | ✅ |
| S4 | EEA | Air quality status in Europe 2026 – Particulate matter, PM2.5 | 2026-04-30 | https://www.eea.europa.eu/en/analysis/publications/air-quality-status-report-2026/particulate-matter-pm2.5 | ✅ |
| S5 | WHO | Ambient (outdoor) air pollution and health (fact sheet) | 2024-10-24 | https://www.who.int/news-room/fact-sheets/detail/ambient-(outdoor)-air-quality-and-health | ✅ |
| S6 | Wyer et al. (J. Environ. Manage.) | Ammonia emissions from agriculture and their contribution to fine particulate matter: A review of implications for human health | 2022 | https://doi.org/10.1016/j.jenvman.2022.116285 | ✅ 摘要（Europe PMC）|
| S7 | Tomlinson et al. (ESSD) | A framework for gridded estimates of ammonia emissions from agriculture (SAARC) | 2026 | https://essd.copernicus.org/articles/18/2349/2026/essd-18-2349-2026.pdf | ✅ PDF |
| S8 | Zhan et al. (ES&T) / IIASA preprint | Improved Estimates of Ammonia Emissions from Global Land Surface | 2020/2021 | https://pubs.acs.org/doi/10.1021/acs.est.0c05149 | 摘要（檢索片段，PDF 未取）|
| S9 | UNEP | Global Ammonia Assessment 2022 | 2022 | https://wedocs.unep.org/handle/20.500.11822/35997 | ❌ Cloudflare 403，PDF 未能取得 |

## 1. 全球氨排放結構：農業／氮肥佔比

### 1.1 全球總排放量與農業佔比
### 1.2 氮肥施用量（全球 N）
### 1.3 每公斤氮的氨排放因子（kg NH3-N per kg N）

**一手來源：EEA, EMEP/EEA air pollutant emission inventory guidebook 2023, Ch.3.D + Annex 1 (A1.1.2)**
URL: https://www.eea.europa.eu/en/analysis/publications/emep-eea-guidebook-2023/part-b-sectoral-guidance-chapters/3-agriculture/3-d-agricultural-soils-2023/@@download/file
（PDF 已下載：/workspace/raw2/eea_guidebook_agsoils.pdf → eea_gb.txt）

**Tier 2 肥料別排放因子（Table 3-2，單位 g NH3 per kg N applied；normal pH ≤7.0 / high pH >7.0）**

| 肥料 | g NH3/kg N（normal pH） | g NH3/kg N（high pH） | 換算 NH3-N % of N applied（normal/high） | EEA 分組 |
|---|---|---|---|---|
| **Urea（尿素）** | **195** | **206** | **16.1 / 17.0** | urea+ |
| N solutions (UAN) | 87 | 161 | 7.2 / 13.3 | UAN |
| Ammonium phosphate (AP)、AS、NPK、NP | 84 | 187 | 6.9 / 15.4 | ammonium+1 |
| AN (硝酸銨)、CAN、NK、Other straight N | 24 | 52 | 2.0 / 4.3 | ammonium+2 |
| **Anhydrous ammonia (AH，液氨直接施用)** | **20** | **20** | 20 g NH3/kg N（Annex 1 缺資料採此值） | — |

**Tier 1 預設 EF（Table 3-1）：NH3 from N fertiliser = 0.085 kg NH3 per kg fertiliser N applied（95% CI: NC / not calculated）**
- 其他 Tier 1：NH3 from sewage sludge = 0.0066 或 0.13 kg NH3 capita⁻¹；其他有機廢棄物 0.08 kg NH3 per kg waste N applied；作物殘留 0.034 kg NH3 per kg crop N residue（留在地表 >3 天）。
- Tier 1 加權平均 EF（Annex 表）：**Tier 1 EF = 84.6 g NH3/kg N**（肥料結構比例表：urea 20%、AN 28%、AS 4%、CAN 15%、N solutions 13%、Other N straight 4%、AP 4%、NPK 10%、NP 2%；高 pH 農地比例 pH>7.0 = 0.093）。

### 1.4 尿素最高／氨肥最低的具體係數（實測範圍，同上來源 §2.2.1）

- **尿素 NH3 排放佔施用 N 的 6–47 %**（most variable），高度依賴土壤類型、天氣與施用量。
- **硝酸銨 (AN) 與 CAN 實測排放從不超過施用 N 的 4 %**。
- EEA 文字結論（原文）："emissions from urea are the most variable, ranging from 6 to 47 % of applied N"；"measured emissions from ammonium nitrate (AN) (and calcium AN (CAN)) are much smaller, never exceeding 4 % of applied N"。
- 補充：無水氨 (AH) 僅 20 g NH3/kg N（Annex 1 說明：anhydrous 與 aqueous NH3 資料不足，採 20 g NH3 per kg N applied）。

### 1.5 不確定性區間

- EEA Tier 1 表中 NH3 from N fertiliser 的 95% CI 標為 **NC（not calculated）**；Tier 2 EF 由 31 種肥料、數百筆試驗的 meta-analysis 導出，隨機/異質性未在此章給出信賴區間（見 A3.3.1 "Emission factor uncertainties"）。
- 尿素實測區間 6–47 % of applied N（9.1 倍變異）；AN/CAN ≤4 %。
- 其他顯著不確定性來源（EEA 原文）：土壤 pH（>7.0 為高 pH 區）、施用方式（broadcast / sprayed / injected）、量測方法（micrometeorological / 15N / closed chamber / wind tunnel）、作物覆蓋、施用後 7–10 天內的冠層排放無法與直接施用排放區分。

### 本節缺口
- 未取得 UNEP Global Ammonia Assessment 2022 原文 PDF（Cloudflare 403），全球農業氨佔比與全球氮肥施用量數字尚未以該一手來源核實。
- 未取得 IPCC 2019 Refinement / Zhu et al. (1999) 肥料 EF 原始表格作交叉比對。
- 全球尺度「kg NH3-N per kg N」加權值（跨國、跨作物）尚未取得可引用的單一數字。

## 2. 大氣化學機制鏈：NH3 → NH4+ 氣膠 → 二次 PM2.5

### 2.1 中和反應（NH3 + HNO3 / H2SO4）
### 2.2 氣膠生成與成核生長
### 2.3 二次 PM2.5 佔歐洲／亞洲 PM2.5 的官方比例
### 本節缺口

## 3. 健康負擔量化

### 3.1 Sofiev et al. (One Earth 2021)
### 3.2 其他區域／其他年份估計（Lancet Planet Health、Nature 系列）
### 3.3 方法學要點（暴露模型、RR 函數、歸屬方式）
### 本節缺口

## 4. 機制與替代解釋（歸因邊界）

### 4.1 氨路徑 vs NOx 二次 PM2.5
### 4.2 vs SO2／硫酸鹽
### 4.3 vs 薪柴／家庭固體燃料
### 4.4 vs 交通尾氣（NOx、尾氣 PM）
### 4.5 溫度本身的影響（熱浪、臭氧、EC）
### 4.6 明確排除的替代解釋
### 本節缺口

## 5. 具體地區案例（可核查、有數字）

### 5.1 案例選定
### 5.2 排放實績與 PM2.5 變化
### 5.3 核查數字
### 本節缺口

## 6. 敏感度／替代情境參數範圍

### 6.1 排放因子敏感度
### 6.2 暴露人口劑量反應斜率（RR 函數）敏感度
### 6.3 背景氨水平敏感度
### 6.4 綜合健康負擔區間
### 本節缺口

## 7. 可直接用於報告的最強事實（8 條內）

## 8. 全域缺口清單

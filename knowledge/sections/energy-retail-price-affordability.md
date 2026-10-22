# 領域筆記：電力零售價格與家庭負擔 (Retail Power Prices & Household Affordability)

首次寫入：2026-10-22 16:00 UTC
主題 id：`energy-retail-price-affordability`
狀態：building

## 已驗證核心事實（附來源）

### LBNL《Retail Electricity Prices 2026》
- 2025 全行業平均零售電價：vs 2024 名義 +5.3%、實質 +2.6%
- 2019→2025：名義 +29%、實質 +3%；2010→2025：名義 +39%、實質 −6%
- 住宅 vs 商用 vs 工業（2019→2025 名義）：+33% / +26% / +27%
- 2024→2025 單年：住宅 +5.0%、商用 +5.2%、工業 +6.0%
- 住宅電費佔個人支出 1.25%（2025，近歷史低位，較 2024 微升）；佔總收入 1.0%
- 電氣成本近年貢獻總體通脹 3–4%（LBNL 依 BLS 數據自算）
- 2024→2025：43 個州/DC 零售價上升；2019→2025：29 個州下降
- 2025 年住宅平均電價最高：HI、CA、美東、Alaska
- 欠繳（arrearages）2025 年 5 月達 210 億美元
- 來源：https://eta-publications.lbl.gov/sites/default/files/2026-10/lbnl-2026-retail-electricity-prices.pdf

### Brattle 虚拟發電廠（VPP）負擔能力研究
- 美國住宅平均電費率 2019→2025 名義 +33%
- 近期天然氣發電容量成本近乎翻倍，供不應求源自供應鏈短缺
- 模型：無 VPP 時五年後平均家庭年度賬單 +98 美元（2026 幣值）；有 VPP 時 −56 美元
- 假設：performance payment 均值 75 美元/kW-年；規模 10 GW → 35 GW；系統峰值減 4%
- 全美住宅 VPP 能力中位數約 4%，現有能力 16%
- 來源：https://brattle.com/white-papers/virtual-power-plants-mitigating-rising-retail-electric-bills-and-affordability-challenges

### NREL Cole et al.《Cost Projections for Utility-Scale Battery Storage: 2025 Update》
- 四小時系統總過夜資本成本（2024$/kWh）：2035 年低/中/高 = 147 / 243 / 339；2050 年 = 108 / 178 / 307
- 2025 更新與 2023 報告的「低」預測最接近，主因當前電池系統成本估計下修
- 口徑警示：$/kWh 為過夜資本成本，與 BNEF 之 $/MWh 項目成本不可直接相減比較
- 來源：https://www.nrel.gov/docs/fy25osti/93301.pdf

## 口徑陷阱（重要）
1. LBNL「電費佔收入比」= 全體經濟合計數字；Brattle「負擔」= 問卷式度量。不可混用。
2. 儲能成本：過夜資本成本（$/kWh）vs 全生命週期平準化成本（LCOE）vs 項目成本（$/MWh）—— 三者不可直接比較。
3. BNEF 為業界機構，部分方法論專有；其數字非官方統計。

## 未解缺口
- 無官方文件記載某座具體燃氣調峰機組因電池競爭而退役／取消
- 無 EIA 對零售賬單節省的官方量化
- VPP 效果全部為模型推算，無實測驗證

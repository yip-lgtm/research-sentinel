# 領域筆記：綠氫電解槽硬件通縮與 LCOH 傳導 (Electrolyser Hardware Deflation & LCOH Pass-Through)

領域：能源 ｜ 主題 slug：`energy-electrolyser-hardware-deflation`
首次寫入：2026-11-07 21:00 UTC（人工補做，因 cron 撞 Token Plan 429）
主題 id：`energy-electrolyser-hardware-deflation`
狀態：building
- domain：能源（energy）

## 已驗證核心事實（附來源）

### IEA《Global Hydrogen Review 2026》
- 全球電解槽年製造產能：2024 年 46 GW/yr → 2025 年近 58 GW/yr；2025 年實際產出估計不足 5 GW
- 已裝機電解槽 CAPEX（2025，含 BoP/EPC/不可預見費）：中國 US$820/kW、其他地區 US$2,200/kW（約 2.7 倍）
- 中國電解槽製造產能逾 35 GW/yr；2025 年訂單 4.7 GW，其中逾 90%（4.4 GW）內銷
- 中國 2025 年新裝機佔全球近四分之三，期末佔全球已裝機約三分之二
- 58 GW/yr 產能中約 36% 屬只做氫能的公司（需求波動敞口最高）
- 2025 年新進入中國市場者中得標不足三分之一
- 電解槽項目管線至 2030 年近 320 GW（較 GHR-25 低約 30%）；約 240 GW（佔全球管線 75%）投產機會低或不明朗
- 已承諾 + 高潛力項目由 10 Mt 降至 2030 年略高於 6 Mt
- 2030 STEPS 中國電解槽 CAPEX 降至 US$680/kW（其他地區 US$1,700/kW）
- 2026 年 3 月國富氫因虧損警示增發股本（增發折價）
- 來源：https://iea.blob.core.windows.net/assets/af4b6218-0311-4963-91ab-903cb18ca0ca/GlobalHydrogenReview2026.pdf
  （官方報告頁 https://www.iea.org/reports/global-hydrogen-review-2026 回 HTTP 403，必須用 blob storage URL 取全文）

### World Bank / ESMAP《Electrolyzers for Hydrogen Production: Technical and Economic Characteristics》(P506220, 2026-02)
- 基準：52 kWh/kg H2 + $50/MWh PPA → 電力成本單項約 $2.60/kg；PPA 每升 $10/MWh → LCOH +$0.52/kg
  （自算核對：52 × 50 ÷ 1000 = 2.60；52 × 10 ÷ 1000 = 0.52）
- 電力佔 LCOH 50–70%（電解槽最大成本驅動因素）
- 現況典型 50–55 kWh/kg；研發路徑目標改善 20–30%；熱力學極限 33.4 kWh/kg（LHV）／39.4 kWh/kg（HHV）
- 堆疊不足總 CAPEX 的一半；最大降本空間在 BoP、施工與系統整合
- BoP 佔直接 CAPEX 30–60%，均值約 40%
- 堆疊更換成本 = 原堆疊的 30–60%
- 中石化鄂爾多斯 2025 年 9 月招標：48 套鹼性堆疊，每套 1,000–1,500 Nm³/h（約 5–7 MW），均價約 $75/kW（含稅、不含 BoP），較 2022 年低 60%；中標者隆基、三一、華電工程
- 庫車項目實際輸出僅約預期三分之一（Sinopec Kuqa）
- 中國健康發展倡議：終止低於成本價格戰、避免誇大效率聲稱
- 來源：https://documents1.worldbank.org/curated/en/099022326123011297/pdf/P506220-b45b0865-8706-4862-8792-d8cc71f84569.pdf

### IRENA《Green Hydrogen Cost Reduction》(2020-12)
- 電價是綠氫現場生產的最大成本項；投資成本、運營成本與運行小時數共同決定
- 運行小時數低時投資成本主導（用棄電或純光伏無儲能時尤甚）
- 3,000–4,000 小時/年已足以令投資成本貢獻大幅下降；最佳地點混合光伏風電容量因子可達 5,000 小時以上
- 來源：https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2020/Dec/IRENA_Green_hydrogen_cost_2020.pdf

### Hydrogen Insight（業界二手，用作倡議佐證）
- 2025-11-20：40 家中國電解槽製造商承諾終止「混亂及惡劣」行為（低於成本定價、虛假聲稱）
- 2025-03-21：中國綠氫拍賣得標價兩年腰斬
- 來源：https://www.hydrogeninsight.com/electrolysers/forty-chinese-electrolyser-makers-vow-to-end-chaotic-and-vicious-behaviour-such-as-below-cost-pricing-and-false-claims/2-1-1903701

## 口徑陷阱（重要）
1. IEA「58 GW/yr」對 World Bank「61 GW（2025 年中）」：統計時點 + 是否含氯鹼工業用槽不同，不可混用或相減。
2. 堆疊報價（$/kW，不含 BoP）≠ 已裝機 CAPEX（$/kW，含 BoP/EPC/不可預見費）。鄂爾多斯 $75/kW 與 IEA $820/kW 相差逾 10 倍，正係口徑差異。
3. kWh/kg 必須註明電制（直流 DC 47 vs 交流 AC 51）與 HHV/LHV 口徑。
4. 47 kWh/kg 級目標來自單一 OEM（Nel）訪談，非量產實測；敏感度改用可核對的 20% 效率紅利。

## 缺口
- 庫車「三分之一」產量無公開運營數據可獨立稽核
- 中國項目層面電價與容量因子實測值未公開
- 2026 年 3 月後投標價走勢無一手數據
- 未做容量因子 → 每公斤 CAPEX 傳導的完整量化（下一步）

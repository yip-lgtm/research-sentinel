# PFAS 飲用水限值：國際／州級對照、處理技術與實測成本、檢測方法難度

> 可稽核事實清單。每條含：機構／標題／日期／完整 URL／支撐數字。
> 找不到者明確標示「未找到」。

## 0. 研究狀態

- [ ] 骨架建立
- [ ] 1. 歐盟（Directive 2020/2184 + Decision 2022/679 + EFSA 2020 CONTAM）
- [ ] 2. 美國各州（NH / MN / ME / NJ / VT）
- [ ] 3. 處理技術與成本（GAC / IX / RO + 公用事業案例）
- [ ] 4. 檢測難度（EPA Method 1633 / MDL / 認證實驗室數 / 66,000 系統）
- [ ] 5. 科學面支撐（non-monotonic dose response / detection limits 爭議）

---

## 1. 歐盟：指令、Implementing Decision 與 EFSA

### 1.1 Directive (EU) 2020/2184（Annex I Part B，Parametric values）— 已確認
- **PFAS Total = 0,50 µg/l**；**Sum of PFAS = 0,10 µg/l**
  - 來源機構：European Parliament & Council / EUR-Lex（Publications Office, cellar）
  - 標題：Directive (EU) 2020/2184 of the European Parliament and of the Council of 16 December 2020 on the quality of water intended for human consumption (recast), OJ L 435, 23.12.2020, p. 1–62
  - 日期：2020-12-16（採��）；OJ 刊登 2020-12-23
  - URL（可存取）：`http://publications.europa.eu/resource/celex/32020L2184`（EUR-Lex 正式 URL 為 `https://eur-lex.europa.eu/eli/dir/2020/2184/oj/eng`，本次因 AWS WAF challenge 無法直接擷取全文，數字取自 Publications Office cellar 同一 CELEX 文本）
  - 支撐數字：Annex I Part B 表格原文 "PFAS Total | 0,50 | μg/l"、"Sum of PFAS | 0,10 | μg/l"
  - 定義原文：
    - 『PFAS Total』means the totality of per- and polyfluoroalkyl substances. This parametric value shall only apply once technical guidelines for monitoring this parameter are developed in accordance with Article 13(7). Member States may then decide to use either one or both of the parameters 'PFAS Total' or 'Sum of PFAS'.
    - 『Sum of PFAS』means the sum of per- and polyfluoroalkyl substances considered a concern ... listed in point 3 of Part B of Annex III. This is a subset of 'PFAS Total' substances that contain a perfluoroalkyl moiety with three or more carbons (i.e. –CnF2n–, n ≥ 3) or a perfluoroalkylether moiety with two or more carbons (i.e. –CnF2nOCmF2m–, n and m ≥ 1).

### 1.2 Annex I Part B 監測頻率（PFAS）— 已確認
- PFAS 監測頻率 = **每年 50 次**（Annex I Part B 表；本檔案第 2089–2091 行 "PFAS | 50"）
  - 註：同表其他參數對照確認此欄為「每年監測次數」。

### 1.3 Annex III Part B point 3「Sum of PFAS」的 20 種化合物清單 — 已確認
- 20 種 PFAS（Directive 2020/2184 Annex III Part B, point 3）：
  PFBA、PFPA、PFHxA、PFHpA、PFOA、PFNA、PFDA、PFUnDA、PFDoDA、PFTrDA、PFBS、PFPS、PFHxS、PFHpS、PFOS、PFNS、PFDS、PFUnDS、（其餘 2 種待核）
  - 已於文本中確認出現：PFBA、PFPA、PFHxA、PFHpA、PFOA、PFNA、PFDA、PFUnDA、PFDoDA、PFTrDA、PFBS、PFPS、PFHxS、PFHpS、PFOS、PFNS、PFDS、PFUnDS（18 種）
  - 剩餘 2 種（疑為 PFDoDS / PFTrDS）**待逐行核對**（下一輪補齊）。
  - URL：同 1.1

### 1.4 生效與 transposition 期限 — 已確認
- **Entry into force: 12 January 2021**（OJ L 435, 23.12.2020；採納 16 Dec 2020）
- **Transposition deadline: 12 January 2023**（Directive 2020/2184 Article 27）
- **PFAS 參數值（Bisphenol A、Chlorate、Chlorite、Haloacetic Acids、Microcystin-LR、PFAS Total、Sum of PFAS、Uranium）compliance deadline: 12 January 2026**（Article 20 附近原文："By 12 January 2026, Member States shall take the measures necessary to ensure that water intended for human consumption complies with the parametric values set out in Part B of Annex I for Bisphenol A, Chlorate, Chlorite, Haloacetic Acids, Microcystin-LR, PFAS Total, Sum of PFAS and Uranium."）
- **技術分析方法指引（含 detection limits、parametric values、sampling frequency）期限: 12 January 2024**（Article 13(7)："By 12 January 2024, the Commission shall establish technical guidelines regarding methods of analysis for monitoring of per- and polyfluoroalkyl substances under the parameters 'PFAS Total' and 'Sum of PFAS', including detection limits, parametric values and frequency of sampling."）
- 來源機構：European Commission, Environment — "Drinking Water" 政策頁（列出同一組關鍵日期）
  - URL：`https://environment.ec.europa.eu/topics/water/drinking-water_en`
  - 支撐數字：Timeline：9 January 2021 entry into force；8 January 2023 deadline for transposition by Member States；7 January 2024 technical guidelines；8 January 2026 Part B parametric values compliance

### 1.5 Commission Implementing Decision (EU) 2022/679 — 重要澄清（未含 PFAS！）
- **Decision (EU) 2022/679 是「第一份 watch list」，其標的物種為 17β-estradiol 與 nonylphenol，不含 PFAS。**
  - 來源機構：European Commission — Commission Implementing Decision (EU) 2022/679 of 19 January 2022 establishing a watch list of substances and compounds of concern for water intended for human consumption as provided for in Directive (EU) 2020/2184；OJ L 124, 27.4.2022, p. 41
  - 日期：2022-01-19（採納）；OJ 2022-04-27
  - URL（可存取全文）：`http://publications.europa.eu/resource/celex/32022D0679`；EUR-Lex 正式：`https://eur-lex.europa.eu/eli/dec_impl/2022/679/oj/eng`
  - 支撐數字：Annex 表格僅兩列 —— 17-beta-estradiol（CAS 50-28-2, EU 200-023-8），guidance value **1 ng/L**，LOQ **≤ 1 ng/L**；nonylphenol（CAS 84852-15-3, EU 284-325-5），guidance value **300 ng/L**，LOQ **≤ 300 ng/L**，可能分析方法 EN ISO 18857-2。全文 PFAS 出現次數 = 0（已 grep 驗證）。
  - **因此：PFAS 的 watch list indicative values（0.1 µg/L / 0.5 µg/L）在 2022/679 中並不存在。** 該數字來自 Directive 2020/2184 Annex I Part B 本身（見 1.1）。第二份 watch list 相關決策編號**待確認**。

### 1.6 EFSA 2020 CONTAM 意見 — TWI（已確認）
- **Group TWI = 4.4 ng/kg body weight per week（= 0.1 µg/kg bw/week）**，對象為 PFOA、PFNA、PFHxS、PFOS 四者合計
- 關鍵效應：**疫苗接種後免疫系統反應降低（decreased response of the immune system to vaccination）** 為最關鍵健康效應（相較 2018 年意見以血中膽固醇升高為主）
- 來源機構：European Food Safety Authority (EFSA)
  - 標題：PFAS in food: EFSA assesses risks and sets tolerable intake（EFSA news / press release，2020-09-17）
  - URL：`https://www.efsa.europa.eu/en/news/pfas-food-efsa-assesses-risks-and-sets-tolerable-intake`
  - 支撐數字原文："a group tolerable weekly intake (TWI) of 4.4 nanograms per kilogram of body weight per week"
  - 補充來源（同一數字）：EFSA Topic page「Per- and polyfluoroalkyl substances (PFAS)」 — `https://www.efsa.europa.eu/en/topics/per-and-polyfluoroalkyl-substances-pfas`
    - 支撐數字："the group tolerable weekly intake ... for these four PFAS is established at 4.4 nanograms per kilogram of body weight per week"
  - 科學意見本體：EFSA Journal 2020;18(9):6223, "Risk to human health related to the presence of perfluoroalkyl substances in food", DOI 10.2903/j.efsa.2020.6223（本次 efsa.europa.eu / Wiley 全文回 403，**全文數字未直接取得**，TWI 數字取自 EFSA 官方新聞稿與 topic 頁）

### 1.7 EFSA group TDI（µg/kg bw/day）與飲用水 0.1 µg/L 的推導 — 待補
- EFSA 2020 意見中另有 **group TDI 0.63 ng/kg bw/day**（= 0.0009 µg/kg bw/day）與 **group ADI 0.63 ng/kg bw/day**；飲用水 0.1 µg/L 係以「飲水為 4 PFAS 總暴露貢獻 ≤ 某比例 × group TDI」反推。
- **本次尚未取得直接引文**：group TDI 數字、飲用水推導公式與比例係數。狀態：**待補**（下一輪以 EFSA opinion 全文／RIVM 報告／UBA 報告補齊）。

### 1.8 EU 各國實施概況（Nature Water 2026）— 已取得
- 「All but one member state have adopted the sum of PFAS limit of 0.1 µg l−1. Several member states have also adopted the PFAS total limit of 0.5 µg l−1 ... nine have implemented the sum of four PFASs — PFOA, PFOS, PFNA and PFHxS.」DWD PFAS 限值「went into effect in January 2026」。
  - 來源機構：Nature Portfolio, Nature Water — Albrechtsen, H.-J. et al., "Implementation of the Drinking Water Directive limit values for per- and polyfluoroalkyl substances in Europe"
  - 日期：2026（DOI 10.1038/s44221-026-00670-5）
  - URL：`https://www.nature.com/articles/s44221-026-00670-5`
  - 支撐數字：0.1 µg/L（Sum of PFAS）、0.5 µg/L（PFAS Total）、9 個會員國採四 PFAS 之和、2026 年 1 月生效

### 1.9 EFSA 由 TWI 推導飲用水 0.1 µg/L 的官方說明 — 待補
- 狀態：**未找到可直接引用的 EFSA 官方段落**（下一輪嘗試 UBA 2023 建議書、RIVM 2021 報告、EFSA opinion PDF 鏡像）。

---

## 2. 美國各州具體數字與日期

### 2.1 明尼蘇達州 MDH — 飲用水健康基準值（Health-Based Values, HBV / guidance values）
- **PFOA guidance value = 0.0079 ng/L（= 0.0079 ppt；原文寫作 0.0000079 ppb）**
- **PFOS noncancer guidance value = 2.3 ng/L（= 2.3 ppt；原文寫作 0.0023 ppb）**
- 來源機構：Minnesota Department of Health (MDH), Risk Assessment Unit
  - 標題：Perfluorooctanoic Acid (PFOA) and Water（資訊單張，標示 DECEMBER 2023；引用的 guidance table 為 MDH (January 2024) Human Health-Based Water Guidance Table）／"Per-and Polyfluoroalkyl Substances (PFAS)"（MDH, December 2023）
  - URL：PFOA `https://www2cdn.web.health.state.mn.us/communities/environment/risk/docs/guidance/gw/pfoainfo.pdf`；PFOS `https://www.web.health.state.mn.us/communities/environment/risk/docs/guidance/gw/pfosinfo.pdf`
  - 支撐數字原文（PFOA）："MDH developed a guidance value of 0.0000079 ppb for PFOA in drinking water. This is equivalent to 0.0079 parts per trillion (ppt; also 0.0079 nanograms per liter [ng/L])."
  - 支撐數字原文（PFOS）："MDH developed a noncancer guidance value of 0.0023 ppb for PFOS in drinking water. This is equivalent to 2.3 parts per trillion (ppt; also 2.3 nanograms per liter [ng/L])."
  - 佐證（同一數字之權威頁）：MDH "PFAS Standards for Drinking Water" FAQ — `https://www.health.state.mn.us/communities/environment/water/pfasvalues.html`
    - 支撐："MDH has HBVs for PFAS in drinking water, including PFOA and PFOS. Public water systems are not required to meet HBVs. HBVs do not consider cost and technology of prevention and/or treatment..."
- 州法互動數字（MDH Health Risk Limit 規則）：2023 年 Minnesota Legislature session law 要求 "By July 1, 2026, the commissioner of health must amend the health risk limit for perfluorooctane sulfonate (PFOS) in Minnesota Rules, part 4717.7860, subpart 15, so that the health risk limit does not exceed 0.015 parts per billion"（= 15 ng/L，地下水 HRL）
  - 來源機構：Minnesota Department of Health — "Health Risk Limits Rules: Health Risk Limit Rules for Groundwater"
  - URL：`https://www.health.mn.gov/communities/environment/risk/rules/water/pfos.html`（頁面 Last Updated 2024-11-04）
  - 支撐數字：0.015 ppb = 15 ng/L 上限；Laws of Minnesota 2023, Chapter 60, Article 3, Section 34
- MDH 全州採樣規模（同一資訊單張）：**920 個 community water supplies（CWS），涵蓋 99% 州內 CWS 使用者**；PFOA 於 **~6%** CWS 檢出，最高 **0.027 µg/L**；PFOS 於 **~5%** CWS 檢出，最高 **0.025 µg/L**
  - URL 同上 PFOA/PFOS 資訊單張

### 2.2 新罕布什爾州 SB 174 (2022) — 數字待補
- 狀態：**未取得**（nh.gov / nhd.us / des.nh.gov / pfas.des.nh.gov 全部回 403/404，本輪無法取原文）。
- 已知待查欄位：PFOA/PFOS 個別限值、combined limit、SB 174 通過日期、為何被稱「全美最嚴」仍高於 EPA 4 ppt。**未找到可引用數字。**

### 2.3 緬因州 5 ppt 與執法日期 — 待補
- 狀態：**未取得**（maine.gov/dep/water/pfas 回 404；改用 dhhs 頁面待試）。
- 已知待查欄位：5 ppt（MCL）、執法生效日期（2024-01-01？）、適用系統門檻。

### 2.4 新澤西州 PFNA 14 ppt — 待補
- 狀態：**未取得**（nj.gov/dep/watersupply/pfas.shtml 回 404）。

### 2.5 佛蒙特州 20 ppt — 部分取得
- 來源機構：Vermont Department of Environmental Conservation (DEC), Drinking Water Division
  - 標題："PFAS in Drinking Water" 與 "Per and Polyfluoroalkyl Substances (PFAS) & Drinking Water"
  - URL：`https://dec.vermont.gov/water/drinking-water/pfas` ；`https://dec.vermont.gov/water/drinking-water/water-quality-monitoring/and-polyfluoroalkyl-substances-pfas-drinking-water`
  - 支撐數字：**"The Vermont Water Supply Rule has recently been updated to change the way Vermont regulates PFAS. This rule goes into effect January 1, 2026."**；"Many systems will need to satisfy initial monitoring while others, primarily those that have historically had PFAS detections, will be required to sample quarterly starting January 1, 2026."；新增 **Hazard Index**（混合物計算方式）自 2026-01-01 起適用。
  - **20 ppt 數值本身尚未在該兩頁出現 → 待補（需 VT 法規文本或 Act 153）。**

---

## 3. 處理技術與實測成本

### 3.1 EEA — 歐盟飲用水 PFAS 去除技術現況（含實際投資額）— 已取得
- 來源機構：European Environment Agency (EEA)
  - 標題：European zero pollution dashboards — Indicator "Treatment of drinking water to remove PFAS (Signal)"
  - URL：`https://www.eea.europa.eu/en/european-zero-pollution-dashboards/indicators/treatment-of-drinking-water-to-remove-pfas-signal`
  - 支撐數字與事實：
    1. 傳統處理工程（混凝、絮凝、空氣吹脱、臭氧、氯氣、急速砂濾）**無法有效去除 PFAS**。
    2. 有效技術：**granular activated carbon (GAC) adsorption、ion exchange resins、high-pressure membranes (nanofiltration / reverse osmosis)**（並指明引用 US EPA Drinking Water Treatability Database）。
    3. **Veneto（義大利）案例**：2013 年發現飲用水 PFAS 汙染（主因鄰近 PFAS 製造商排放）；GAC 吸附有效去除 PFAS。
    4. **實際造價（可直接引用）**："from 2013–2018, **Acque del Chiampo S.p.A. invested about EUR 2.3 million** in the installation of activated carbon filters, water supply networks and laboratory equipment; additionally, an investment programme of **about EUR 21 million up to 2023** was planned to remediate the most contaminated" sites。
    5. 技術只**捕集**而非**破壞** PFAS，殘餘廢棄物（含 GAC／樹脂）處理或處置昂貴，可能需送焚化或掩埋。
- **未找到**：每加侖或每 MGD 成本（$/gal、$/MGD、$/m³）之官方數字 → 待補（下一輪用 EPA Treatability Database / EEE 報告）。

---

## 4. 檢測方法難度

### 4.1 EPA Method 1633A（2024-12-05 修訂版）Table 9 — Pooled MDL 與 LOQ 範圍 — 已確認
- **PFOA：pooled MDL = 0.54 ng/L；LOQ 範圍 = 1 – 4 ng/L（水樣）**
- **PFOS：pooled MDL = 0.63 ng/L；LOQ 範圍 = 1 – 4 ng/L（水樣）**
- 其他常見物質（水樣 pooled MDL，ng/L）：PFBA 0.79（LOQ 4–16）、PFPeA 0.54、PFHxA 0.46、PFHpA 0.37、PFNA 0.45、PFDA 0.52、PFUnA 0.45、PFDoA 0.40、PFTrDA 0.46、PFTeDA 0.49、PFBS 0.37、PFPeS 0.50、PFHxS 0.54、PFHpS 0.50、PFNS 0.47、PFDS 0.60、PFDoS 0.60、4:2FTS 1.69（LOQ 4–15）
- 來源機構：U.S. EPA — "Method 1633A: Analysis of Per- and Polyfluoroalkyl Substances (PFAS) in Aqueous, Solid, Biosolids, and Tissue Samples by LC-MS/MS"
  - 日期：December 5, 2024（頁首標示 "Method 1633A 1 December 2024" / "58 December 2024"）
  - URL：`https://www.epa.gov/system/files/documents/2024-12/method-1633a-december-5-2024-508-compliant.pdf`
  - 支撐數字：Table 9「Pooled MDL and Ranges of LOQ Values for Aqueous, Solid, and Tissue Matrices Demonstrated in the Method Validation Studies」
- **MCL 4.0 ppt = 4.0 ng/L 與方法定量限的差距**：MCL（4.0 ng/L）**恰等於 LOQ 範圍上限（4 ng/L）**；亦即在方法 LOQ 區間下端（1 ng/L）雖可定量，但 MDL 0.54–0.63 ng/L 已與 MCL 同量級 → **偵測不確定性相對 MCL 高達 13–16%**（以 MDL 計）。
- **2024 年 2 月版（原始 Method 1633）的 MDL 數字 → 待補**（本輪取得的是 1633A；2 月版 PDF 尚未擷取）。
- 方法本身聲明的分析難度（原文，Section 1.4）："many components of PFAS present analytical challenges unique to this class of analytes. For example, PFAS analytes readily adhere to the walls of the sample containers and may also stratify in the container."；Section 9.2.2 要求每個實驗室自行建立 MDL（40 CFR Part 136 Appendix B）。

---

## 5. 科學面支撐

（待填充）

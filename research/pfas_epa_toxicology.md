# EPA PFAS 飲用水最終法規與毒理學依據 — 可稽核事實清單

> 狀態：研究中（骨架已建立，內容增量填充）
> 目標：逐項坐實「4.0 ppt」數字背後的科學假設與不確定性，區分「危害認定」與「風險外推」。

## 0. 資料結構說明
- 每一條事實格式：**數字／事實 → 機構 / 標題 / 日期 / 完整 URL**
- 找不到者明確標記「未找到」。

## 1. Final Rule (2024-04-26) 的具體 MCL 與合規期限

來源（所有引文均出自同一份文件）：
- 機構/標題：U.S. EPA, "PFAS National Primary Drinking Water Regulation; Final Rule", 89 FR 32532, published 2024-04-26, FR Doc 2024-07773, Docket EPA-HQ-OW-2022-0114, RIN 2040-AG18
- URL（HTML）: https://www.federalregister.gov/documents/2024/04/26/2024-07773/pfas-national-primary-drinking-water-regulation
- URL（全文）: https://www.federalregister.gov/documents/full_text/text/2024/04/26/2024-07773.txt
- URL（PDF）: https://www.govinfo.gov/content/pkg/FR-2024-04-26/pdf/2024-07773.pdf
- 生效日 2024-06-25；MCL 合規期限 2029-04-26；初始監測期限 2027-04-26。

**1.1 MCL 一覽（89 FR 32532–32533, 40 CFR 141.61(c) Table 4）**
| Contaminant | MCLG | MCL | 備註 |
|---|---|---|---|
| PFOA | 0 (zero) | **4.0 ng/L (= 4.0 ppt)** | 表 4 列 (39): MCL 0.0000040 mg/L |
| PFOS | 0 (zero) | **4.0 ng/L (= 4.0 ppt)** | 表 4 列 (40): MCL 0.0000040 mg/L |
| PFHxS | 10 ng/L | **10 ng/L** | HBWC 0.00001 mg/L |
| PFNA | 10 ng/L | **10 ng/L** | HBWC 0.00001 mg/L |
| HFPO-DA (GenX) | 10 ng/L | **10 ng/L** | HBWC 0.00001 mg/L |
| PFBS | (deferred 個別判定) | 無個別 MCL | 僅進 HI |
| Hazard Index (HI) | 1 (unitless) | **1** | 組成四種：PFHxS、PFNA、HFPO-DA、PFBS |

**1.2 Hazard Index 組成與 HBWC（89 FR 32533）**
- 四種 PFAS：**PFHxS、PFNA、HFPO-DA、PFBS**（PFOA/PFOS **不納入** HI，因其 MCLG=zero，量測值一旦 >4.0 ng/L 即視為 HI 超標）
- HBWC：PFHxS = 10 ng/L；PFNA = 10 ng/L；HFPO-DA = 10 ng/L；**PFBS = 2,000 ng/L**
- HI 計算：HI = Σ (measured ng/L ÷ 該 PFAS 之 HBWC ng/L)；HI ≤ 1 = 可接受；HI > 1 = 超標

**1.3 HBWC 所依據的 chronic reference value（89 FR 32560 附近，section IV.B）**
- PFHxS：chronic reference value **2E-06 mg/kg-day**（= 2 ng/kg-day），甲狀腺濾泡上皮肥大/增生；DWI-BW 0.034 L/kg-day；**RSC = 0.20** → HBWC 10 ng/L
- PFNA：chronic reference value **3E-06 mg/kg-day**（= 3 ng/kg-day），母鼠暴露後子代體重增加受損與發育延遲；DWI-BW 0.0469 L/kg-day（哺乳婦女）；**RSC = 0.20** → HBWC 10 ng/L
- HFPO-DA：肝臟效應為最敏感非致癌終點；HBWC 10 ng/L
- PFBS：基於 Feng et al. (2017) 甲狀腺效應 chronic RfD，信心度 Low（無慢性暴露期間哺乳類研究，額外施加 UF=10 資料庫限制）

**1.4 ★ 關鍵：4.0 ng/L 的真正決定因素 = PQL（分析定量極限），不是 CSF**
89 FR 32577–32578（section V.A.3 Final Rule）原文：
> "Since limits of analytical measurement for PFOA and PFOS require the MCL to be set at some level greater than the MCLG, the agency has determined that **4.0 ng/L (the PQL for each contaminant) represents the closest feasible level to the MCLG**…"
- 4.0 ng/L 來自 **UCMR 5 minimum reporting level**，同時被定為本規則的 PQL。
- 89 FR 32576：「The MCLs for PFOA and PFOS were also set at 4.0 ng/L as a result of the **analytical capability assessment under the minimum reporting level setting study for UCMR 5**, as well as consideration of other factors (e.g., treatment, costs) as required under SDWA.」
- 47/53 個申請 UCMR 5 認證的實驗室（89%）以 Method 533 可確認 ≤ 2 ng/L（= MCL 的一半）。
- 2023-03 proposal 曾要求 comment 5.0 / 10.0 ng/L 替代方案，最終定於 4.0 ng/L。
- ⇒ **MCL 4.0 ng/L 是「分析可測性下限」決定的，不是毒理學 CSF 直接換算的結果**；毒理學只決定了 MCLG = 0。

## 2. 2021 SRA (EPA/600/R-21/146) 癌症斜率因子與外推假設
（進行中）

## 3. 對照組：2016 SRA (EPA/600/R-16/146F) CSF
（進行中）

## 4. 非致癌路徑：2017 interim RfD 換算飲用水當量
（待填）

## 5. 效益與成本估算（final rule economic analysis vs. 2025 proposed extension reanalysis）
（待填）

## 6. 2025-05-14 延長合規期限提案；2026-06 case-by-case 豁免提案
（待填）

## 7. GAO-25-107897 (2025-07-30) 批評
（待填）

## 8. 美國人群血清 PFAS 背景暴露 vs. 癌症 point of departure
（待填）

## 9. 來源索引 (Sources)
（待填）

# 案例研究（Case Study）：愛爾蘭數據中心（Data Centre）電力需求 — CRU/2025236 ＋ EirGrid 數據中心政策文件組

> **研究主題**：AI 運算每查詢能耗急降，是否被使用量增長抵銷（反彈效應／Jevons 悖論）？
> **本案例的論證角色**：這不是「效率提升」案例，而是一個**反彈效應的直接量測現場**——愛爾蘭的電網規劃者完全不採用「每查詢能耗」作預測變數。他們的預測變數是**已簽約的機電容量（MVA / GW）**，並且在 CRU 自己的文件裡明確寫出數據中心需求增長是「在建容量」驅動的。這正是本報告要說的：當需求端的每單位效率改善 33 倍時，總需求反而由建置速度決定。

> **完成時間**：2026-10-23 07:45 UTC
> **所有標示「已載入 HTTP 200」的來源，均由本人以 curl 實際抓取並逐字擷取原文。**

---

## 0. 一句話總結

愛爾蘭全國只有 **7.5 GW** 尖峰負載的小型同步電力系統，數據中心已佔 **2024 年全國用電的 22%**；已簽約 **2 GW** 機電容量，市場意向再來 **6 GW**（若全部實現將令系統尖峰**翻倍**）；而 CRU 在 2025 年 12 月 12 日最終拍板的新接駁政策，用**「80% 愛爾蘭本土可再生能源＋100% MIC 對應的可調度發電／儲能」**作為入場費——把「效率」直接轉化成「你必須自己蓋發電機」。

---

## 1. 選定案例：愛爾蘭（Ireland）— CRU 大型用電戶（LEU）接駁政策 CRU/2025236

### 1.1 為何選這個案例（與研究主題的因果對應）

| AI 側變數 | 愛爾蘭電網側實際使用的變數 |
|---|---|
| 每提示能耗（Wh/prompt）、每 token 效率 | **Maximum Import Capacity (MIC, MVA)** — 已簽約的機電取電容量 |
| 推理請求量、模型規模 | **已簽約數據中心項目數 × 建置率（ramp）** |
| PUE（機房效率） | **是否自備可調度發電＋儲能、可再生能源匹配度** |

**關鍵論點**：電網完全不計算「每一次查詢用多少電」。它計算的是「有多少 MW 已經簽約並接上來」。因此 AI 效率提升 33 倍（Google 官方數據，見同目錄 `verified_core.md` F1/F2）對愛爾蘭 2034 年的電力預測**貢獻為零**；反而是**建造速度**決定了 31% 的全國用電。

---

## 2. 硬數字（5 條，每條附來源 URL 與逐字原文）

### 數字 ①：數據中心佔愛爾蘭全國用電 22%（2024），用電量 10 年增長逾 460%

- **機構**：Commission for Regulation of Utilities (CRU)，愛爾蘭
- **標題**：CRU/2025236 *Large Energy User connection policy decision paper*
- **日期**：2025-12-12
- **URL**：https://cruie-live-96ca64acab2247eca8a850a7e54b-5b34f62.divio-media.com/documents/CRU2025236_Large_Energy_User_connection_policy_decision_paper.pdf
- **載入狀態**：**HTTP 200**（PDF，134 頁，全文已抽取）
- **逐字原文**：
  > "Total electricity demand has grown by 30% over the past 10 years, with data centre demand having significantly contributed to this level of growth, with **data centre demand up over 460%** over the same period. It also shows that the share of total electrical consumption in Ireland represented by data centres **increased from circa 5% in 2015 to circa 22% in 2024**."
  >
  > "Between 2023 and 2024 annual data centre electricity consumption grew by **633 GWh**. This growth would be the equivalent of **circa 150,000 households'** annual electricity demand. Since 2015 annual data centre electricity consumption grew by **5,731 GWh**. This level of consumption growth is equivalent to **1.36 million households'** annual electricity demand."（註：愛爾蘭平均家庭年用電 4,200 kWh）

### 數字 ②：EirGrid 預測數據中心用電 9.41 TWh（2025）→ 14.56 TWh（2034），佔全國 27% → 31%

- **機構**：EirGrid and SONI
- **標題**：*All-Island Resource Adequacy Assessment 2025-2034*（AIRAA 2025-2034）
- **日期**：2025
- **URL**：https://www.eirgrid.ie/sites/default/files/publications/AIRAA-2025-2034.pdf （landing page：https://www.eirgrid.ie/all-island-resource-adequacy-assessment-2025-2034）
- **載入狀態**：**HTTP 200**（PDF，168 頁，24.7 MB，全文已抽取）
- **逐字原文（Figure 4.8）**：
  > "The proportion of demand for each sector for 2025 and 2034 are estimated as follows:
  > **2025 → 2034**
  > 37.73 TWh → 49.52 TWh
  > Residential 24% → 19%
  > Commercial 25% → 17%
  > Industrial 20% → 15%
  > Electric Vehicles 1% → 8%
  > Heat Pumps 3% → 10%
  > **Data centres and new tech loads 27% → 31%**"
- **逐字原文（第 13 頁）**：
  > "The largest growth comes from data centres and new technology load (**68% of the growth forecast in 2025**), and increased uptake of electric vehicles and heat pumps, particularly later in the decade (**46% of the growth in 2030**). Also notable is that **by 2030, 29% of all electricity demand is expected to come from data centres and new technology loads**."
- **逐字原文（第 13 頁）**：
  > "In the median scenario, **electricity demand is forecasted to increase by 45% by 2034 from 2023 levels**. The largest growth comes from data centres and new technology loads (NTLs) which will form **31% of all electricity demand by 2030**."
- **CRU 引用同一組數字的表格（Table 3, AIRAA 2025-2034）**：
  > "Data Centres & New Tech Loads **9.41 | 27%** | **14.56 | 31%**；Total **35.32 | 46.49**"

### 數字 ③：已簽約 2,000 MVA（傳輸層）+ 300 MVA（110 kV 配電層）；16 個傳輸層項目 + 5 個配電層項目

- **機構**：EirGrid and SONI
- **標題**：*All-Island Resource Adequacy Assessment 2025-2034*，§4.2.3（PDF 第 45／47 頁）
- **日期**：2025
- **URL**：https://www.eirgrid.ie/sites/default/files/publications/AIRAA-2025-2034.pdf
- **載入狀態**：**HTTP 200**
- **逐字原文**：
  > "In Ireland, there is currently approximately **2000 MVA of demand capacity that is contracted to data centres and other new technology loads at the transmission level**, and approximately **a further 300 MVA contracted at the 110 kV distribution level** (ESB)."
  >
  > "The current demand forecast considers **sixteen data centre projects at transmission level, and five at 110 kV distribution level**, that are either connected or have a signed connection agreement."
  >
  > "**As of the freeze date for this study, there have been no new data centres contracted that meet the CRU Direction.** As such, this study only considers data centres with an existing contract."

### 數字 ④：市場意向再來 6 GW（會令系統尖峰翻倍）；CRU 稱中期潛力「約 5.8 GW」

- **機構**：EirGrid（Constrained Area Overview）；CRU（決策文件）
- **標題**：*Data Centre Constrained Area Overview*（2026-05 文件組）／CRU/2025236
- **日期**：2026-05（EirGrid）／2025-12-12（CRU）
- **URL（EirGrid）**：https://www.eirgrid.ie/sites/default/files/publications/Data-Centre-Constrained-Area-Overview-May-2026.pdf
  **URL（CRU）**：https://cruie-live-96ca64acab2247eca8a850a7e54b-5b34f62.divio-media.com/documents/CRU2025236_Large_Energy_User_connection_policy_decision_paper.pdf
- **載入狀態**：兩者皆 **HTTP 200**（PDF 全文字元擷取）
- **逐字原文（EirGrid，第 7 頁）**：
  > "With an All-Ireland peak demand of approximately **7.5 GW**, the power system on the island of Ireland is considered a relatively small power system in comparison with countries in Europe and elsewhere in the world."
  >
  > "Ireland has **2 GW of contracted data centres** mostly located in the greater Dublin area. This will represent **nearly a third of the entire demand in Ireland** once all of the contracted data centres connect and utilise their full contracted demand."
  >
  > "As requested by the CRU, EirGrid recently completed a **Market Intelligence Exercise** which identified that there was a **continued interest in the development of a further 6 GW of data centre demand in Ireland**. If all of this potential interest was to materialise in the current Irish power system, **it would double the current system peak**."
- **逐字原文（EirGrid，第 9 頁）**：
  > "Ireland has successfully managed to provide connection contracts for **over 2 GW of data centre demand without significant network reinforcements**."
- **逐字原文（CRU 決策文件，第 5 頁及第 109 頁）**：
  > "Initial feedback from this market intelligence exercise suggests that there is potential for **in the order of 5.8GW additional demand capacity required for the data centre sector in Ireland in the medium term**. This is in addition to demand already contracted and would require consideration of a bespoke or plan-led approach to infrastructure development in Ireland."

### 數字 ⑤：接入門檻＝100% MIC 的自備可調度發電／儲能（≥10 MVA）＋ 80% 愛爾蘭本土可再生能源；30 MVA 例子需 34.8 MW 燃氣輪機

- **機構**：EirGrid（DCCOPP Version 3）／CRU（CRU/2025236）
- **標題**：*Data Centre Connection Offer Process and Policy, Version 3*（DCCOPP V3, IOO-CC-001-R3）／CRU/2025236 §3.5.3
- **日期**：2026-05-20（EirGrid）／2025-12-12（CRU）
- **URL（EirGrid）**：https://www.eirgrid.ie/sites/default/files/publications/Data-Centre-Connection-Offer-Process-and-Policy-V3-May-2026.pdf
  **URL（CRU）**：https://cruie-live-96ca64acab2247eca8a850a7e54b-5b34f62.divio-media.com/documents/CRU2025236_Large_Energy_User_connection_policy_decision_paper.pdf
- **載入狀態**：兩者皆 **HTTP 200**
- **逐字原文（EirGrid DCCOPP V3，第 12 頁）**：
  > "To maintain the continuity, security, and quality of electricity supply, and to ensure system security standards are consistently met, **data centres with a MIC greater than or equal to 10 MVA will be required to provide dispatchable onsite or proximate generation and/or storage capacity equal to their MIC**, subject to applicable derating requirements."
  >
  > "A data centre application **cannot be progressed if it is in a constrained area**."
- **逐字原文（EirGrid DCCOPP V3，第 10-11 頁）**：
  > "The customer must demonstrate the capability to meet **at least 80% of their annual electricity demand** through the provision or procurement of **additional, indigenous renewable electricity**."
  >
  > "If, after the six-year glide path, the 80% target is not met, EirGrid may **reduce the data centre's MIC** to the level that has been met and/or **terminate the Connection Agreement**."
- **逐字原文（CRU/2025236，第 64-65 頁，Table 4 完整數字）**：
  > "**Data centre capacity (MVA) 30**
  > **Installed dispatchable generation requirement (MW) 34.8** — Prior to renewable generation being taken into account
  > **Annual data centre electricity demand (GWh) 210** — Assumes 80% utilisation of demand connection
  > **Annual 80% Renewable Electricity contribution (GWh) 168**
  > **Equivalent installed onshore wind capacity (MW) 54.9** — Based on 35% capacity factor
  > **De-rated capacity for onshore wind (MW) 3.1** — De-rating factor of 0.056 from CRM
  > **Remaining dispatchable generation requirement (MW) 26.9** — de-rated
  > **Installed dispatchable generation requirement (MW) 31.2** — De-rating factor of 0.863 from CRM"

### 數字 ⑥（補強）：MVA 預測三情景 — 867 MVA（2023）→ 1289／1680／2067 MVA（2034）

- **機構**：EirGrid and SONI，*AIRAA 2025-2034* Table 4.2
- **URL**：https://www.eirgrid.ie/sites/default/files/publications/AIRAA-2025-2034.pdf （**HTTP 200**）
- **逐字原文**：
  > "Table 4.2 Forecasted data centre and new technology load demand by 2034. **2023 demand 867 MVA.**
  > | Forecast Scenario | Growth from 2023 – 2034 (MVA) | 2034 Demand (MVA) |
  > |---|---|---|
  > | Low | 422 | 1289 |
  > | **Median** | **813** | **1680** |
  > | High | 1200 | 2067"
- **峰值負荷**：2025 年 6133 MW → 2034 年 7124 MW；數據中心＋新技術負載佔峰值 19%（2025）→ **24%（2034）**（同 PDF，第 56 頁 Figure 4.9）

---

## 3. 數字總表

| # | 指標 | 數值 | 單位 | 期間 | 來源 | 載入 |
|---|---|---|---|---|---|---|
| ① | 數據中心佔全國用電 | 5 → 22 | % | 2015 → 2024 | CRU/2025236 | HTTP 200 |
| ①a | 數據中心用電量年增 | 633 | GWh | 2023→2024 | CRU/2025236 | HTTP 200 |
| ①b | 數據中心用電量十年累增 | 5,731 | GWh | 2015→2024 | CRU/2025236 | HTTP 200 |
| ①c | 十年數據中心需求增幅 | >460 | % | 2015→2024 | CRU/2025236 | HTTP 200 |
| ①d | 全國總用電十年增幅 | 30 | % | 2015→2024 | CRU/2025236 | HTTP 200 |
| ② | 數據中心＋新技術負載用電量 | 9.41 → 14.56 | TWh | 2025→2034 | AIRAA 2025-2034 | HTTP 200 |
| ②a | 佔全國總用電（TER） | 27 → 31 | % | 2025→2034 | AIRAA 2025-2034 | HTTP 200 |
| ②b | 佔全國用電（2030 中位情景） | 29 | % | 2030 | AIRAA 2025-2034 | HTTP 200 |
| ②c | 全國總用電（TER）中位情景 | 37.73 → 49.52 | TWh | 2025→2034 | AIRAA 2025-2034 | HTTP 200 |
| ②d | 全國用電中位情景增幅 | +45 | % | 2023→2034 | AIRAA 2025-2034 | HTTP 200 |
| ②e | 數據中心＋NTL 佔全國需求增長比重 | 68 / 46 | % | 2025 / 2030 | AIRAA 2025-2034 | HTTP 200 |
| ②f | 數據中心＋NTL 佔峰值需求 | 19 → 24 | % | 2025→2034 | AIRAA 2025-2034 | HTTP 200 |
| ③ | 已簽約數據中心＋NTL（傳輸層） | ~2,000 | MVA | 2025 | AIRAA 2025-2034 | HTTP 200 |
| ③a | 已簽約（110 kV 配電層） | ~300 | MVA | 2025 | AIRAA 2025-2034 | HTTP 200 |
| ③b | 已簽約項目數（傳輸／配電） | 16 / 5 | 個 | 2025 | AIRAA 2025-2034 | HTTP 200 |
| ③c | 2023 年數據中心＋NTL 需求 | 867 | MVA | 2023 | AIRAA 2025-2034 | HTTP 200 |
| ③d | 2034 需求（低／中／高） | 1,289 / 1,680 / 2,067 | MVA | 2034 | AIRAA 2025-2034 | HTTP 200 |
| ④ | 全愛爾蘭系統尖峰 | ~7.5 | GW | 2026 | EirGrid Constrained Area Overview | HTTP 200 |
| ④a | 已簽約數據中心 | 2 | GW | 2026 | EirGrid Constrained Area Overview | HTTP 200 |
| ④b | 市場意向進一步需求 | 6 | GW | 2026 | EirGrid Constrained Area Overview | HTTP 200 |
| ④c | CRU 所述中期潛力 | ~5.8 | GW | 2025 | CRU/2025236 | HTTP 200 |
| ⑤ | 自備可調度發電門檻 | ≥10 MVA → 100% MIC | MVA | 2026 | EirGrid DCCOPP V3 | HTTP 200 |
| ⑤a | 可再生能源匹配要求 | ≥80 | % of annual demand | 2026 | EirGrid DCCOPP V3 | HTTP 200 |
| ⑤b | 可再生能源寬限期 | 6 | 年 | 2026 | EirGrid DCCOPP V3 | HTTP 200 |
| ⑤c | 30 MVA 範例：需裝機可調度發電 | 34.8 | MW | 2025 | CRU/2025236 | HTTP 200 |
| ⑤d | 30 MVA 範例：年用電（80% 使用率） | 210 | GWh | 2025 | CRU/2025236 | HTTP 200 |
| ⑤e | 30 MVA 範例：需裝機陸上風電 | 54.9 | MW | 2025 | CRU/2025236 | HTTP 200 |
| ⑤f | 30 MVA 範例：燃氣輪機裝機 | 31.2 | MW | 2025 | CRU/2025236 | HTTP 200 |
| ⑤g | 都柏林以外可容納的新數據中心 | 150–300（單點 50–100） | MW | 2026 | EirGrid Constrained Area Overview | HTTP 200 |
| ⑥ | 愛爾蘭數據中心佔歐洲城市集中度 | 97（都柏林）；次位阿姆斯特丹 44 | % | 2025 (ICIS) | CRU/2025236 | HTTP 200 |

---

## 4. 政策機制：為什麼數字會是這個數字？（反彈效應的制度證據）

### 4.1 機制一：電網的預測模型裡，**根本沒有「每查詢能耗」這個變數**

EirGrid 的 AIRAA §4.2.3 逐字說明數據中心需求如何被預測：

> "EirGrid accounts for a range of factors that will drive growth from each site: these include **historical demand growth rates from existing sites, contracted positions from companies and their growth potential, financial close, planning permission**, etc. This process creates three credible scenarios that drive demand across the low, median, and high forecast scenarios."

並且明文把 **AI 效率變數排除在外**：

> "**In forecasting future demand, EirGrid assumes data centres have a flat demand profile across the day, with a gradual ramp throughout the year to their forecasted demand. This has been observed in real time data.**"

→ **AI 效率提升 33 倍，對 2034 年愛爾蘭電力預測的影響係數是 0。** 預測的輸入只有：已簽約容量 × 建置率 × 分區用電。可再生能源、電動車、熱泵、家庭節能（EU Energy Efficiency Directive）這些「效率/轉型」變數全部被納入，但**沒有任何一個「AI 推理效率」變數**。這是本報告最強的制度性證據：**需求端每單位能耗的改善，在電網規劃層面被結構性地忽略，因為它不影響已簽約的 MW 數。**

### 4.2 機制二：入場費把「效率」轉化成「你必須自己蓋發電機」——效率收益被制度性截留

CRU/2025236 的核心設計：新數據中心要接駁電網，**必須自備或就近提供 100% MIC 對應的可調度發電／儲能**，外加 **80% 愛爾蘭本土新增可再生能源**。

- 30 MVA 範例（CRU Table 4）：210 GWh/年用電 → 168 GWh 需由本土可再生能源覆蓋 → 需裝機 54.9 MW 陸上風電（35% 容量因子），其去評級貢獻僅 3.1 MW → 剩餘 26.9 MW 去評級需求 → 需 **31.2 MW 燃氣輪機**（去評級係數 0.863）。
- **反彈的制度含義**：AI 查詢效率提升 → 每 MW 的算力產出上升 → 同一批工程師會用「更少、更高效的機櫃」填滿同樣的 MIC，或反過來在已簽約的 2 GW 內追求更高密度（更高的機櫃功率密度 = 更高的實際功耗，因為 PUE 改善被 IT 負載增長吃掉）。
- 寬限期只有 **6 年**，第 7 年評估；不達標 → **EirGrid 可削減 MIC 或終止接駁協議**。→ 這直接把「效率」變成一個**帶罰則的容量合約**，而非一個可以自動分享給社會的紅利。

### 4.3 機制三：物理約束（Dublin 短路、220 kV 裕度）讓需求無法用效率「消化」

EirGrid *Data Centre Constrained Area Overview*（2026-05）第 9-11 頁逐字：

> "**Dublin, in particular, is experiencing significant short circuit challenges.** To mitigate short circuit issues, the transmission system in the greater Dublin area needs to be reinforced with a comprehensive level of 400 kV network. ... In advance of these works, **generator connections on the 220 kV and 110 kV network cannot be accommodated in the greater Dublin region and this will restrict developments that include new generation capacity such as new data centres.**"

> "**The greater Dublin region is considered fully constrained.** This is due to the fact that the required nominated conventional generators accompanying any potential data centre developments would increase the already compromised short circuit levels in the area."

> "many 220 kV substations already have significant programs of refurbishment, maintenance and connections laid out for them over the coming years. It is prudent to assume that these areas will only be able to facilitate new connections from the **mid-2030s**."

→ 也就是說：**新增 6 GW 意向在 Dublin 之外最多只能容納 150–300 MW**（Galway／Limerick／Cork 各 50–100 MW）。也就是說，**效率改善帶來的新需求完全無法靠重新分配消化**，只能靠「更多 MW ＋ 更多自備發電」硬吃下去。

### 4.4 機制四：AI 專屬的電網穩定性問題——效率手段反而傷害電網

EirGrid 同份文件第 9-10 頁：

> "**Recent fault ride-through issues have occurred on the power system due to data centres rapidly reducing their demand in response to voltage fluctuations.** The impact of these large demand reductions is an imbalance of supply and demand which results in a frequency deviation that is experienced by the whole power system."

> "**The oscillating demand characteristics of Artificial Intelligence data centres could also pose a risk to the stability of the Irish system.**"

CRU/2025236 同一問題（第 36 頁）：

> "EirGrid's observations are that the collective response of data centres to system faults (fault ride through capability) is **exacerbating disturbances on the power system** via disconnection and automatic reconnection of their demand."

→ **這是效率的另一面**：AI 數據中心為了效率／成本而做的負載調節（快速降載、快速爬升），在 7.5 GW 的同步島上會造成全系統頻率偏移。**「每查詢更省電」並不等於「對電網更友善」**——反而可能更糟，因為調度頻率更高。CRU 因此要求強制 Grid Code 故障穿越（fault ride-through）標準。

### 4.5 機制五：成本外部性——數據中心的成本被攤到其他用電戶

CRU/2025236 §5.1.6 "Cost burden & Tariff review" 逐字：

> "**A number of respondents raised concerns relating to the associated cost impacts on consumers of requiring new dispatchable generation.** It was stated that the consequence of this may be to increase costs for all consumers."
>
> "the CRU notes that all electricity market charges and a significant percentage of electricity network charges are levied on SEM demand on a **€/MWh basis**. Any new data centre demand would contribute towards these costs through their energy payments."
>
> "the CRU notes that **additional large demand connections would increase the charging base for tariffs/charges. This means that the costs captured by the tariffs/charges are being spread over a larger volume of demand**, which has the potential to lower costs on a per unit basis."

→ **這就是反彈效應的財政版本**：數據中心每單位的技術效率再高，其接入成本與自備發電的機會成本都由 SEM 全體用電戶按 €/MWh 分攤。**這是一個明確的「私人效率收益、社會成本」結構。**

---

## 5. 未驗證／無法取得的項目（Unverified / Unavailable）

| 項目 | 狀態 | 說明 |
|---|---|---|
| DSCC（Datacentre Services and Connectivity Centre）2022 報告《Data Centre Infrastructure and Energy Use in Ireland》 | **unavailable** | `dscc.ie` 與 `www.dscc.ie` 在本環境 **DNS 無法解析**（curl exit code 6, "Could not resolve host"）。未取得，**不得引用其任何數字**。 |
| 電網加固的具體金額（€ million）／每 MW 接駁成本 | **not found** | CRU/2025236 與三份 EirGrid 2026-05 PDF 中均無明確歐元金額。唯一相關陳述是 EirGrid 的「2 GW 是在『without significant network reinforcements』的情況下簽約的」，與 CRU 的「€/MWh 網費攤分」論述。**沒有確認的成本數字。** |
| 「已排隊申請」的確切 GW 數（EirGrid 公開的 connection queue volume） | **not found as an exact published queue figure** | 可確認的一級來源數字是 **6 GW**（EirGrid Market Intelligence Exercise 的「continued interest」）與 **5.8 GW**（CRU 所述「potential for ... in the order of 5.8GW additional demand capacity」）。兩者是**市場意向／潛力**（market-sounding 結果），**不是**已遞交申請的排隊量，**不可混為一談**。 |
| 「EirGrid 2024/2025：數據中心 2030 年將達 27% 愛爾蘭需求」 | **未以此措辭確認** | 一級來源實際給出的是：**22%（2024）→ 27%（2025，中位情景）→ 29%（2030）→ 31%（2034）**（AIRAA 2025-2034）。27% 確實出現，但對應年份是 **2025**，不是 2030。此為重要的**年份修正**。 |
| 新加坡 IMDA *Green Data Centre Roadmap*（2024-01）一級來源數字 | **未取得** | `imda.gov.sg` 全部回 **HTTP 202 + `x-amzn-waf-action: challenge`（AWS WAF JS 挑戰）**，body 僅 2,407 bytes 的 WAF script；`ema.gov.sg` 回 200 但 body 僅 212 bytes 的 Incapsula 質詢頁；`mnd.gov.sg` 同樣 202。**未載入任何 IMDA 原文，因此本報告不引用任何新加坡數字。** |
| IEA（iea.org） | **blocked (403 Cloudflare)** | 依指示未嘗試。 |
| web.archive.org | **timeout** | 依指示未嘗試。 |
| Google 校園 PUE 表（Singapore 1.12 / Dublin 1.08） | **本會話未重驗** | 由同目錄另一子任務驗證，見 `verified_core.md` F7（HTTP 200）。**注意：Dublin PUE 1.08 可與本案例並用，說明「機房效率（PUE）遠好」與「全國用電佔比 22–31%」可以同時成立——這正是 Jevons 悖論的教科書式並置。** |

---

## 6. 給主報告的可用結論（可直接引用）

1. **效率在電網層面是無效的變數。** EirGrid 的 10 年用電預測模型輸入是「已簽約 MVA × 建置率」，其明文假設數據中心負載「flat demand profile across the day」，**完全沒有 AI 推理效率項**。AI 每提示能耗降 33 倍（Google 官方，2025-08-21），對愛爾蘭 2034 年用電預測的影響為零。
2. **反彈在容量市場上被完整記錄。** 已簽約 2,000 MVA ＋ 意向 6 GW，對上一個只有 7.5 GW 尖峰的系統而言，意味著「意向若全部實現，系統尖峰翻倍」。這正是 Jevons 悖論的量化版本：**更便宜的算力 → 更多算力 → 更多 MW 接入 → 更多總用電**，而物理電網（Dublin 短路、220 kV 裕度、150–300 MW 的都柏林以外容量）根本無法吸收這一波。
3. **政策層面，效率收益被制度性轉移。** 80% 本土可再生能源要求＋100% MIC 自備可調度發電＋6 年寬限期＋不達標即削減 MIC／終止合約 → 數據中心必須**自建發電**，把「節省下來的電」變成「自己造一台機」。這是把效率紅利從社會收回、把成本轉給 SEM 用電戶的制度機制。
4. **AI 特有的副作用可能反噬。** EirGrid 記錄數據中心故障穿越（fault ride-through）行為正在「exacerbating disturbances on the power system」；AI 數據中心的「oscillating demand characteristics」被點名為穩定性風險。**效率手段（快速降載／爬升）在小型同步系統上會造成全系統頻率偏移。**
5. **可與 Google 的 PUE 1.09（2025 車隊平均）並列**：機房工程效率已達全球最優（Doubla 校區 1.08、Singapore 1.12），但愛爾蘭全國用電佔比仍從 5%（2015）升到 22%（2024）、預測 31%（2034）。**技術效率與總需求脫鈎，是本案例最乾淨的示範。**

---

## 7. 完整來源清單

| # | 機構 | 標題 | 日期 | URL | 載入狀態 |
|---|---|---|---|---|---|
| S1 | CRU (愛爾蘭) | CRU/2025236 *Large Energy User connection policy decision paper* | 2025-12-12 | https://cruie-live-96ca64acab2247eca8a850a7e54b-5b34f62.divio-media.com/documents/CRU2025236_Large_Energy_User_connection_policy_decision_paper.pdf | **HTTP 200**（134 頁 PDF，全文抽取） |
| S2 | CRU (愛爾蘭) | The CRU Publishes its Decision on New Electricity Connection Policy for Data Centres（新聞稿） | 2025-12-12 | https://www.cru.ie/en-ie/about-us/news/the-cru-publishes-its-decision-on-new-electricity-connection-policy-for-data-centres/ | **HTTP 200**（全文抽取） |
| S3 | CRU (愛爾蘭) | New Electricity Connection Policy for Data Centres（建議決定稿新聞稿） | 2025-02-18 | https://www.cru.ie/en-ie/about-us/news/new-electricity-connection-policy-for-data-centre/ | **HTTP 200**（全文抽取） |
| S4 | EirGrid | *Data Centre Connection Offer Process and Policy*, Version 3（IOO-CC-001-R3） | 2026-05-20 | https://www.eirgrid.ie/sites/default/files/publications/Data-Centre-Connection-Offer-Process-and-Policy-V3-May-2026.pdf | **HTTP 200**（31 頁 PDF，全文抽取） |
| S5 | EirGrid | *Data Centre Constrained Area Overview* | 2026-05 | https://www.eirgrid.ie/sites/default/files/publications/Data-Centre-Constrained-Area-Overview-May-2026.pdf | **HTTP 200**（12 頁 PDF，全文抽取） |
| S6 | EirGrid | *Data Centre Technical Assessment* | 2026-05 | https://www.eirgrid.ie/sites/default/files/publications/Data-Centre-Technical-Assessment-May-2026.pdf | **HTTP 200**（16 頁 PDF，全文抽取） |
| S7 | EirGrid | *Data Centre Consultation*（文件組 landing page） | 2026-05 | https://www.eirgrid.ie/data-centre-consultation | **HTTP 200** |
| S8 | EirGrid & SONI | *All-Island Resource Adequacy Assessment 2025-2034* | 2025 | https://www.eirgrid.ie/sites/default/files/publications/AIRAA-2025-2034.pdf | **HTTP 200**（168 頁 PDF，24.7 MB，全文抽取） |
| S9 | EirGrid & SONI | AIRAA 2025-2034（landing page） | 2025 | https://www.eirgrid.ie/all-island-resource-adequacy-assessment-2025-2034 | **HTTP 200** |

機器可讀版本：`/root/.hermes/sentinel/research/ai-energy-rebound/case_sources.json`

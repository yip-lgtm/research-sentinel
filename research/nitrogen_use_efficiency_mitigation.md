# 氮肥用量削減與 NUE 提升的量化效益：研究筆記（資料蒐集，非報告）

> 狀態：in-progress 研究筆記。所有數字必須附來源 URL；未查到的寫入本節缺口，不以「一般來說」填空。
> 單位約定：美制 (lb/acre, $/acre, $/ton) 與公制 (kg/ha, $/t) 均標明。

---

## 1. 全球與主要作物 NUE 現況與趨勢（%）

### 1.1 各研究口徑與數字

| 研究 | 口徑 | NUE 數字 | 趨勢 | 來源 URL |
|---|---|---|---|---|
| **Lassaletta et al. 2014, Environ. Res. Lett. 9 105011**（註：題目給的「Nature Geoscience」有誤；此篇發表於 ERL，另有 Nature 期刊相關文獻為 Zhang 2015） | 聚合／國家（Y/F，Y=收穫蛋白質含氮 kgN/ha/yr；F=合成肥+糞肥+生物固氮+沉降 總 N 投入） | 全球：1961 年 **68%** → 1980 年 **45%** → 近 30 年穩定在 **47%**；結論句「目前只有 47% 的活性氮被轉成收穫產品，相較 1960 年代初的 68%，同期合成氮肥投入增加 9 倍」 | 1961–1980 明顯下降，之後 30 年持平 ~47% | https://iopscience.iop.org/article/10.1088/1748-9326/9/10/105011 （DOI 10.1088/1748-9326/9/10/105011） |
| **Zhang et al. 2015, Nature 528:51-59**（Perspective「Managing nitrogen for sustainable development」） | 歷史 NUE + 區域/作物目標 | 待補（受 paywall，僅取得摘要） | 摘要載：提出 2050 年需求下按區域與作物類型的 N 目標 | https://www.nature.com/articles/nature15743 |
| **Chen et al. 2014, Nature 514:486-489**（"Producing more grain with lower environmental costs"，中國） | 中國 153 個 site-year 田間試驗（水稻/小麥/玉米） | 不直接給 NUE%，但給基準產量與處理後產量（見 §4.1） | — | https://www.nature.com/articles/nature13609 |
| **Zhang et al. 2017, Nature 553:61-64**（"Pursuing sustainable productivity with millions of smallholder farmers"，CHINA） | 大規模推廣示範（2005–2015，452 縣，20.9M 農民，37.7M ha 累積） | 處理後：反應性 N 損失 **4.5–4.7 kg N/Mg** 產品 vs 未處理 **6.0–6.4 kg N/Mg** | 產量 +10.8–11.5%；施氮 **−14.7~−18.1%**（省 1.2 Mt N）；經濟效益 US$12.2 billion | GHG：處理後 玉米 328 / 水稻 812 / 小麥 434 kg CO2e/Mg vs 未處理 422 / 941 / 549 kg CO2e/Mg | https://www.nature.com/articles/nature25770 |
| Sela et al. 2018（題目稱 Nat Commun，待核實到底刊） | 待填 | 待填 | 待填 | 待填 |
| 其他（IFA/FAO/World Bank） | 待填 | 待填 | 待填 | 待填 |

### 1.1a Lassaletta 2014 的具體分類與理論曲線（機制）
- 四種國家軌跡：**type I**（中國、埃及、印度）：施肥持續增加、產量反應逐漸下降 → NUE 規律下降；**type II**（美國、巴西、孟加拉）：1980 年代前後 Ymax 換軌、NUE 穩定或上升；**type III**（法國、荷蘭、希臘等歐洲）：1960–75 增產增肥，1980 年後減肥不減產 → NUE 上升（荷蘭施氮量回到 1960 年代水準但產量翻倍，與歐盟環保管制直接相關）；**type IV**：見原文。
- 產量函數（fitted yield curve）：**Y = Ymax·F/(F+Ymax)**（Michaelis–Menten 型超曲線，擬合優於負指數 Y = Ymax[1−exp(−F/Ymax)]）。此即「邊際效益遞減」的量化證據（見 §6.3）。Ymax 同時代表飽和產量與達到 0.5 倍飽和產量所需施肥量。
- 全球 Ymax 由 ~70 kgN/ha/yr（1961–80）提升到 ~110 kgN/ha/yr（1980s 換軌後）。
- N 限制程度指標 (Ymax−Y)/Ymax：北美、澳洲、多數歐洲、許多撒哈拉以南國家 >0.75（表示還有增產空間）；中國、印度、巴基斯坦、中美與北非多數國家 <0.3（單純加 N 無益）。
- N 盈餘（損失潛力）：歐洲、中東、美國、中美、印度、中國多數 >50 kgN/ha/yr；撒哈拉以南、獨立國家聯盟、澳洲多數平均 <25 kgN/ha/yr。高盈餘 → 低 NUE。
- NUE 與氮來源結構：共生固氮佔比越高 NUE 越高；合成肥佔比越高 NUE 越低。

### 1.2 口徑差異原因（為何數字不同）
| # | 口徑差異原因 | 具體說明 | 可核查來源 |
|---|---|---|---|
| 1 | **NUE 定義不同（Y/F vs 其他）** | Lassaletta 2014 用 Y/F（收穫蛋白質含氮 kgN/ha/yr ÷ 合成肥+糞肥+生物固氮+沉降總 N 投入）；而 Zhang 2015、Chen 2014 等使用 AE-NUE（作物吸氮 ÷ 施氮）或 partial factor productivity（PFP = 產量 ÷ N 投入，不計固氮與沉降）。分母是否含固氮/沉降會讓同一國家數字差 10–20 個百分點。 | Lassaletta 2014 ERL: https://iopscience.iop.org/article/10.1088/1748-9326/9/10/105011 ；Chen 2014 Nature: https://www.nature.com/articles/nature13609 |
| 2 | **時間粒度不同（年度 vs 季節 vs 單季試驗）** | Lassaletta 為 1961–2019 國家年度序列；Chen 2014 為中國 153 個 site-year 單季；Zhang 2017 為 2005–2015 縣級推廣累積（37.7M ha）。單季試驗通常排除前茬殘留 N 與土壤累積，NUE 偏低且波動更大。 | 同上 |
| 3 | **是否計入生物固氮與沉降** | Lassaletta 分母含共生固氮與大氣沉降（type I 國家固氮比重大 → NUE 被稀釋）；若只算合成肥分母（如 ISU 的 lb N/bu grain 0.83），則數字明顯較高。 | Lassaletta 2014；ISU/INI: https://www.agronext.iastate.edu/soilfertility/info/The%20Iowa%20Nitrogen%20Initiative.pdf |
| 4 | **作物與產量定義** | Chen 2014 中國以稻穀/麥粒/玉米粒的**穀物產量**計；Zhang 2017 以「產品」（Mg）計反應性 N 損失（kg N/Mg）。同一 N 投入在不同產量基準下 NUE 不同。 | Chen 2014；Zhang 2017: https://www.nature.com/articles/nature25770 |
| 5 | **「optimum」的經濟 vs 農藝定義** | AONR（最大產量）與 EONR（最大淨利）不同：Purdue 166 trials 中 Indiana 各區 AONR 211–254 lb N/ac，而 EONR 在 $0.75–1.00/lb N 下為 159–210 lb N/ac（差 20–30%）。引用「最佳氮率」時未說明是 AONR 或 EONR，會造成 20–30% 差距。 | Purdue Nitrogen Management Update (PDF)：https://www.extension.purdue.edu/extmedia/AY/AY-203-W.pdf （本檔 §6.1 完整抄錄 Tables 2–4） |
| 6 | **氮價與玉米價情境不同** | EONR 隨 N 價與玉米價變動：Purdue Table 2 中，N 價由 $0.60 → $1.65/lb N（+175%），$5.00 玉米價下 EONR 由 200 → 143 lb N/ac（−28.5%）；玉米價由 $4.50 → $7.50（+67%）在 $1.00/lb N 下 EONR 由 184 → 197（+7%）。 | 同上 |
| 7 | **試驗設計：示範 strip vs 隨機化多處理** | Iowa Nitrogen Initiative 每試驗 5 處理 × 5 重複 × 25 plots（0.25–0.33 ac），用混合效應 quadratic-plateau 模型（MLRA 與輪作為固定效果、各試驗為隨機效果）估計，與 MRTN 逐試驗線性/quadratic 擬合不同 → EONR 估計有系統差異。 | Iowa Nitrogen Initiative (Agronext): https://www.agronext.iastate.edu/soilfertility/info/The%20Iowa%20Nitrogen%20Initiative.pdf |
| 8 | **土壤/氣候條件差異** | INI 2023 結果顯示 EONR 呈東→西梯度（由降雨梯度驅動）：Northwest Iowa 平均 182±50 lb N/ac，Des Moines Lobe 203±28 lb N/ac；同期全州平均 190 lb N/ac、範圍 100–337 lb N/ac。 | 同上 |
| 9 | **N2O 排放係數的測量邊界** | 只計 direct（IPCC 2019 default 1.0% of N input）vs 加 indirect（leaching 0.011、NH3 volatilization 0.006 等）會讓同一措施降幅從 ~10% 變成 ~30–40%。 | IPCC 2019 Refinement Ch.4.5: https://www.ipcc-nggip.iges.or.jp/public/gp/bgp/4_5_N2O_Agricultural_Soils.pdf （§5.1） |

### 本節缺口
- 上游 §1.1 的 Zhang 2015 (Nature 528:51-59) 仍只有摘要，具體表格數字未取得（paywall）。
- Sela et al. 2018 的出刊與數字仍待核實。
- IFA/FAO/World Bank 的 NUE 官方序列未直接抓取。

---

## 2. 干預措施量化效益（每項需田間試驗／大規模示範）

### 2.1 施用時機與位置優化（split application、deep placement、site-specific）
| 措施 | 地點/年份 | N 節省 | 產量變化 | $/acre | N2O 降幅 | 來源 |
|---|---|---|---|---|---|---|
| 待填 | | | | | | |

### 2.2 精準施氮（variable-rate、Y-drop）
| 措施 | 地點/年份 | N 節省 | 產量變化 | $/acre | N2O 降幅 | 來源 |
|---|---|---|---|---|---|---|
| 待填 | | | | | | |

### 2.3 脲酶抑制劑／尿素塗層（NBPT、AGROTAIN）
| 措施 | 地點/年份 | N 節省 | 產量變化 | $/acre | N2O 降幅 | 來源 |
|---|---|---|---|---|---|---|
| 待填 | | | | | | |

### 2.4 硝化抑制劑
| 措施 | 地點/年份 | N 節省 | 產量變化 | $/acre | N2O 降幅 | 來源 |
|---|---|---|---|---|---|---|
| 待填 | | | | | | |

### 本節缺口
- 待填

---

## 3. 成本基準

| 項目 | 數值 | 日期 | 單位 | 來源 |
|---|---|---|---|---|
| 氮肥價格 $/ton N | 待填 | | | |
| 尿素價格 $/ton urea | 待填 | | | |
| 磷肥價格 | 待填 | | | |
| 尿素塗層增量成本 | 待填 | | | |
| 農場平均淨收益 $/acre | 待填 | | | |

### 本節缺口
- 待填

---

## 4. 可稽核具體案例（具名、具地點、具年份、處置組 vs 對照組）

### 4.1 案例
| 案例 | 機構 | 地點/年份 | 設計 | 處理組 vs 對照組數字 | 來源 URL |
|---|---|---|---|---|---|
| 待填 | | | | | |

### 本節缺口
- 待填

---

## 5. 外部效益量化

### 5.1 N2O
- **農業 N2O 佔 anthropogenic N2O 比例：74%**（近十年）—「Agricultural production (due to the use of nitrogen fertilizers and animal manure) contributed **74% of the total anthropogenic N2O emissions** in the last decade.」來源：Global Carbon Project, *Global Nitrous Oxide Budget 2024* (June 2024) briefing。https://www.globalcarbonproject.org/nitrousoxidebudget/24/files/NitrousOxideBudget2024_MediaHighlights.pdf
- 過去四十年 anthropogenic N2O 排放增加 **40%（每年 +3 Mt N2O）**；大氣 N2O 濃度 2022 年達 **336 ppb**，比工业化前高 **25%**；N2O 的 100 年 GWP = **273× CO2**；anthropogenic N2O 佔溫室氣體有效輻射強迫的 **6.4%**，造成約 **0.1°C** 增溫。來源同上。
- Top-5 anthropogenic N2O 排放國（2020）：中國 16.7%、印度 10.9%、美國 5.7%、巴西 5.3%、俄羅斯 4.6%。人均 kg N2O：美國 1.7、中國 1.3、印度 0.8。來源同上。
- 中國 anthropogenic N2O 近五年下降，原因是 **NUE 提升**（「China's anthropogenic N2O emissions have been declining for the past five years owing to increased nitrogen use efficiency」）；EU 因直接肥料與糞肥施用減少而減排 31%。來源同上。
- 全球年化學氮肥用量四十年增加 **47.3 Mt N/yr**（1980→2020）。來源同上。
- IPCC 2019 預設排放因子（direct N2O-N，% N input）：direct **1.0%**（溫帶土壤 0.3–1.0）；leaching/volatile indirect：NO3 leaching 0.011、NH3 volatilization 0.006、deposited NH3 0.006、direct deposition 0.006、leached N₂O 0.004。來源：IPCC 2019 Refinement, *N2O: Direct Emissions from Agricultural Soils*, Chapter 4.5. https://www.ipcc-nggip.iges.or.jp/public/gp/bgp/4_5_N2O_Agricultural_Soils.pdf
- 合成 N 肥（N 投入 100 kg N/ha）的 N2O 直接排放 ≈ **1.0 kg N2O-N/ha**（= 1.0%）；換算成 N2O 分子量 ≈ **1.28 kg N2O/ha**（×44/28），即每 **kg N 投入 ≈ 1.28 g N2O**（僅 direct）；加上 indirect 後 IPCC 總係數 (direct+indirect) 在高降雨區可達 **~2%**（約 2.56 g N2O / kg N）。
- **機制（為什麼會這樣）**：N2O 來自土壤中硝化（NH₄⁺→NO₂⁻）與脫硝（NO₂⁻→N₂O）中間步驟的副產物，屬於「氮越多、土壤過濕越多，N₂O 越多」的非線性關係；Zhang et al. 2017 Extended Data Fig.2 直接以指數模型擬合 N₂O–N 與施氮速率的關係（玉米 n=417、水稻 n=740、小麥 n=395），與 IPCC 模型對照。

### 5.2 硝酸鹽與飲用水／健康
- EPA MCL：硝酸鹽 **10 mg/L（as NO₃-N）**，為保護嬰兒 methemoglobinemia（Blue Baby Syndrome）而設；WHO guideline 亦為 50 mg/L NO₃（=11.3 mg/L NO₃-N）。來源：Iowa Environmental Health & Safety Research Center, *Nitrate & Health* Fact Sheet (Sept 2024)。https://ehsrc.public-health.uiowa.edu/wp-content/uploads/2024/09/Nitrate-Environmental-Health-and-Cancer-Fact-Sheet.pdf
- APHA 1951 調查（Walton 1951）：美國 **>270 例**嬰兒 methemoglobinemia 報告，其中 214 例有飲用水硝酸鹽數據；**NO₃-N < 10 mg/L 未觀察到病例**。來源：Lack 1998, *Drinking-Water Nitrate, Methemoglobinemia, and Global Burden of Disease: A Discussion*, Environ Health Perspect 106(12). https://pmc.ncbi.nlm.nih.gov/articles/PMC1247562/
- **重要反證（機制）**：Lack (WHO) 1998 指出，以 >50 mg/L NO₃ 為暴露基準，**無法辨識出飲用水硝酸鹽濃度與 methemoglobinemia 的暴露反應關係**；硝酸鹽可能是複雜病因中的「共同因子 (co-factor)」之一；因此「以硝酸鹽水準連結疾病率」在方法上不成立。原始 1945 年 Comly 報告僅 2 例。
- IARC 已將食物與水中硝酸鹽分類為 **"probably carcinogenic to humans" (Group 2A)**（IARC Monographs Vol. 94, 2006）。
- **Iowa 地區性量化**：Iowa 研究顯示飲用水硝酸鹽暴露與**大腸癌**（colorectal cancer）有「一致 (consistent) 的關聯」，且部分研究檢視暴露量達 MCL 一半（5 mg/L）以上；低於 MCL 仍見正相關的癌別包含**甲狀腺、卵巢、腎臟**。來源同上（引 Iowa Environmental Council 2024 與 Brender et al. 2013, EHP 121(9):1083–1089）。
- **Iowa 出生缺陷**：Brender et al. 2013（National Birth Defects Prevention Study）— 孕期硝酸鹽攝入與**脊柱裂 (spina bifida)、肢體缺失 (limb deficiencies)、唇顎裂 (cleft palate)** 風險增加相關。來源同上。
- 私人井風險：Iowa 私人井不強制檢測硝酸鹽；淺井（<50 ft）風險不成比例地高；2019 年 EWG 資料顯示 Iowa 私人井硝酸鹽與細菌污染情形。來源同上。

### 5.3 氨對 PM2.5 的貢獻
- 待補（§5.3 缺口）

### 本節缺口
- §5.3 氨→PM2.5 量化尚未取得一手來源（僅有二手搜尋結果）。
- 每噸 N 的 N2O 排放因子需以 IPCC 2019 原文表格逐項核對，目前只取得章節 PDF 網址，具體係數值未逐一從表 4.2 抄錄。
- 缺「每噸 N 施用 = US$ 的 N2O 社會成本」官方數字（尚未取得 EPA/GWP×social cost of carbon 的官方 $/tCO2e）。
- 缺 Iowa 硝酸鹽與癌症的具體相對風險數值（RR/OR），目前只有定性「consistent association」敘述。

---

## 6. 敏感度／替代情境參數

### 6.1 尿素價格波動
- 待填

### 6.2 late-season N 上限（移除 late-season N 的產量損失）
- 待填

### 6.3 NUE 提升的邊際遞減（fitted yield curve 證據）
- 待填

### 本節缺口
- 待填

---

## 附錄：來源清單
（見同名 JSON）

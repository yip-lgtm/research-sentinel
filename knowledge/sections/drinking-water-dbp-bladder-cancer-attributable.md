# 飲用水消毒副產物（DBP）：劑量鏈、可歸因病例與換消毒劑的代價

領域：健康暴露 ｜ 主題 slug：`drinking-water-dbp-bladder-cancer-attributable`

- 首次寫入：2026-11-03 21:00 UTC
- 主題 id：drinking-water-dbp-bladder-cancer-attributable
- 狀態：building（coverage 0.5）
- domain：健康暴露（health）

## 已驗證核心事實

1. **DBP 生成機制（化學層）**：Cl₂ 在水中水解成次氯酸 HOCl；HOCl 遇溴離子被氧化成親電性更強的 HOBr；
   HOCl/HOBr 鹵化天然有機物（腐殖質、芳香酮酸），經三鹵甲基酮中間體生成三鹵甲烷（THM），
   經氧化裂解生成鹵乙酸（HAA）。溴／碘比例越高，產物越偏溴代／碘代，而溴代物毒性更高。
   這解釋了為何 EPA 把 BDCM、溴仿、DCAA 的 MCLG 設為 0（氯仿 0.07 mg/L）。
   來源：US EPA — National Primary Drinking Water Regulations —
   https://www.epa.gov/ground-water-and-drinking-water/national-primary-drinking-water-regulations

2. **劑量—風險斜率（合併分析）**：6 個美歐 case–control 研究（2,806 病例／5,254 對照）合併得
   THM4 斜率 0.00427（95% CI 0.00164–0.00626），即每升多 10 µg/L，膀胱癌 OR ≈ 1.044。
   來源：Villanueva CM 等／Epidemiology — Disinfection byproducts and bladder cancer: a pooled analysis（2004）—
   https://doi.org/10.1097/01.ede.0000121380.02594.fc
   來源：Costet N 等／Occup Environ Med — Disinfection by-products and bladder cancer: European specificity?（2011）—
   https://doi.org/10.1136/oem.2010.062703

3. **歸因病例數與暴露分布**：把上述斜率套上 SYR3 2011 實測分布（42 州、2.694 億人服務人口），
   得美國每年約 79,000 例膀胱癌新發病中約 8,000 例（10%）可歸因於氯消毒 DBP；
   其中 **74% 落在服務人口逾 10,000 的地表水系統**。
   按 THM4 平均濃度分層：**40–80 µg/L 段服務 7,570 萬人**，**≤40 µg/L 段服務 1.154 億人**——
   即人數較少的一層承擔主要可歸因負荷。
   來源：Evans S 等／Environ Health Perspect — National exposures and bladder cancer cases from chlorination DBPs（2022）—
   https://pmc.ncbi.nlm.nih.gov/articles/PMC9342685/

4. **換消毒劑的經濟代價（Stage 2 最終規則）**：受規管用戶年成本平均增 **$0.62**；
   需增設處理的 **1,016 萬戶**平均 **$5.53**、第 90 百分位 **$10.04**；
   服務人口不足 10,000 的小型地表水廠平均 **$43.05**、第 90 百分位 **$173.53**。
   來源：US EPA／Federal Register — Stage 2 Disinfectants and DBPs Rule（71 FR 388，2006）—
   https://www.federalregister.gov/documents/2006/01/04/06-3/national-primary-drinking-water-regulations-stage-2-disinfectants-and-disinfection-byproducts-rule

5. **換氯胺＝把 THM 換成 NDMA**：IRIS 10⁻⁶ 風險水平 **0.7 ng/L**、加州公共衛生目標 **3 ng/L**；
   UCMR2 在 **1,198 個公共供水系統、18,098 個樣本**中檢出 NDMA 的比例為 **10%**，MRL 2 ng/L。
   美國至今**無強制 N‑nitrosamine 限值**（由各州自訂）。
   來源：Riedinger KA 等／Environ Sci Water Res Technol — Low-level N-nitrosamine in disinfected drinking water（2025）—
   https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12571223/fullTextXML

6. **「消毒不能只談化學」的反向案例（密爾沃基 1993）**：淨水廠濁度 3 月 23 日異常上升、4 月 9 日關廠，
   五縣約 **40.3 萬人**腹瀉；疾病總成本 **9,620 萬美元**（醫療 3,170 萬、生產力損失 6,460 萬）。
   來源：Mac Kenzie WR 等／NEJM — A massive cryptosporidium outbreak, Milwaukee（1994）—
   https://doi.org/10.1056/NEJM199407213310304
   來源：CDC／Emerg Infect Dis — Cost of illness, 1993 Cryptosporidium outbreak, Milwaukee（2003）—
   https://pubmed.ncbi.nlm.nih.gov/12702221/

7. **臭氧消毒的 DALY 結算**：C. parvum 中位感染風險 10⁻³ person-year；臭氧化使基線風險降約 **7 倍**；
   bromate 誘發腎細胞癌的損失被 **>10 倍**健康效益抵銷，淨約 **1 DALY／百萬人年**。
   來源：Howard JB 等／Environ Health Perspect — Balancing risks and benefits of water disinfection（2000）—
   https://doi.org/10.1289/ehp.00108315

## 口徑陷阱

- **「8,000 例」係歸因推算，唔係觀察到嘅因果**：整條鏈只靠一條觀察性斜率 0.00427 撐住。
  用 CI 下限 0.00164，OR 由 1.044 降到 1.016，歸因數明顯回落。
- **EPA 自己嘅 attributable fraction 由 Stage 1 前 17.1% 降至 Stage 1 後 11.5%**，用 SYR3 再算更低；
  Stage 2 經濟分析明言**因果未確立、風險下界可低至零**。
- **溴化副產物與 THM4 反向相關**：低暴露組（<5 µg/L 參考）可能已帶毒性更高的溴系暴露 → 用 THM4 當總負荷代理有系統偏差。
- **AML 端口徑極弱**：2025 年氯仿與白血病 meta-analysis 的 AML pooled OR 1.98（1.31–3.00）
  實際只來自**單一研究**（64 例 AML、31,228 對照），且暴露代理係**環境空氣中的氯仿**，唔係飲水劑量比較。
  唔可以同膀胱癌證據並列引用。
- **「全面改 UV」並無現實反事實**：UV 只消毒不阻擋後續管網內再生成的 DBPs，唔等於風險歸零。

## 未解缺口

- 全美 THM4／HAA5 的 median 與 90 百分位（多個 EPA／CDC 頁面阻擋自動存取）。
- 常被引用的 20,000 例 AML 歸因數字（同上，來源未取得）。
- 「全面改 UV」的具體病例與成本。
- 全美換氯胺的總成本（只有 Stage 2 規則的分層估算）。
- full-scale 廠實際 THM 降幅百分比（只拿到模型與規則層面數字）。

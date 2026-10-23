# 主 agent 逐條複核後嘅已驗證核心事實 (2026-10-23 07:xx UTC)

每條均已由主 agent 用 curl 實際載入頁面/PDF 複核並逐字擷取。

## F1 — Google 官方：每提示能源 12 個月降 33x、碳降 44x；2024 用電仍增 27%
- 機構：Google（Ben Gomes, Chief Technologist, Learning & Sustainability）
- 標題：Our approach to energy innovation and AI's environmental footprint
- 日期：2025-08-21
- URL：https://blog.google/company-news/outreach-and-initiatives/sustainability/google-ai-energy-efficiency/
- 載入：HTTP 200，逐字命中
- 原文："Over a 12-month period, while delivering higher-quality responses, the median energy consumption and carbon footprint per Gemini Apps text prompt decreased by factors of 33x and 44x, respectively."
- 原文："the energy consumed per median prompt is equivalent to watching television for less than nine seconds"
- 原文："In 2024, for example, we reduced our data center energy emissions by 12% even as electricity consumption grew by 27% year-over-year, driven by the expansion of our business and services."

## F2 — arXiv 技術報告：median Gemini prompt 0.24 Wh / 0.26 mL；narrow 法只有 0.10 Wh
- 機構：Google（Elsworth, Huang, Patterson, Schneider, Sedivy, Goodman, Townsend, Ranganathan, Dean, Vahdat, Gomes, Manyika）
- 標題：Measuring the environmental impact of delivering AI at Google Scale
- 日期：2025-08-21
- URL：https://arxiv.org/abs/2508.15734
- 載入：HTTP 200，abs 頁逐字命中
- "the median Gemini Apps text prompt consumes 0.24 Wh of energy"
- "33x reduction in energy consumption and a 44x reduction in carbon footprint for the median Gemini Apps text prompt over one year"
- "uses less energy than watching nine seconds of television (0.24 Wh) and consumes the equivalent of five drops of water (0.26 mL)"
- 能量拆解（comprehensive）：active accelerator 0.14 Wh（58%）、host CPU&DRAM 0.06 Wh（25%）、provisioned idle 0.02 Wh（10%）、PUE overhead 0.02 Wh（8%）
- "The comprehensive approach reveals a total energy consumption that is 2.4 times greater than the estimate from the existing approach"；scaling factor 1.72 vs 文獻常用 2x

## F3 — AI Index 2025：推論成本 18 個月降 280 倍；硬體成本 -30%/年、效率 +40%/年
- 機構：Stanford HAI
- 標題：2025 AI Index Report（Chapter 1 Research and Development）
- 日期：2025-04
- URL：https://hai.stanford.edu/ai-index/2025-ai-index-report
- 載入：PDF 全文抽取，line 339-341 逐字命中
- "The cost of querying an AI model that scores the equivalent of GPT-3.5 (64.8) on MMLU ... dropped from $20.00 per million tokens in November 2022 to just $0.07 per million tokens by October 2024 (Gemini-1.5-Flash-8B)—a more than 280-fold reduction in approximately 18 months."
- "Depending on the task, LLM inference prices have fallen anywhere from 9 to 900 times per year."（Epoch AI）
- line 356："performance has improved, with costs dropping 30% per year, while energy efficiency has increased by 40% annually."
- 方法學：3:1 加權 input/output token 價格；固定 GPT-3.5 (64.8) MMLU 門檻；Epoch AI + Artificial Analysis 定價資料

## F4 — AI Index 2025：訓練功率年年翻倍，遠快過硬體效率
- 同 F3 出處，line 3045-3066
- "the original Transformer, introduced in 2017, consumed an estimated 4,500 watts. In contrast, PaLM ... had a power draw of 2.6 million watts—almost 600 times that of the Transformer."
- "Llama 3.1-405B ... required 25.3 million watts, consuming over 5,000 times more power than the original Transformer."
- "According to Epoch AI, the power required to train frontier AI models is doubling annually."

## F5 — AI Index 2026：模型規模增長快過效率改善
- 機構：Stanford HAI
- 標題：2026 AI Index Report（Chapter 1）
- 日期：2026
- URL：https://hai.stanford.edu/ai-index/2026-ai-index-report
- 載入：PDF 全文抽取，line 1597-1601 逐字命中
- "Leading chips deliver about 10 times more computation per watt than those available a decade ago ... However, models have scaled faster than efficiency has improved, so total power required to train frontier systems has continued to increase."
- line 1601-1603："Grok 3 and Llama 4 Behemoth, required upward of 100 million watts during training."
- line 1420-1422："Total AI data center power capacity reached approximately 29.6 GW by Q4 2025, enough to power all of New York state at peak demand ... AI chip power, measured by thermal design power, accounted for roughly 11.8 GW of the total, with the remainder attributed to cooling, networking, and other data center infrastructure."
- line 1518："In 2025, the United States led by a wide margin, with 5,427 data centers, more than 10 times any other"（國家）

## F6 — DOE/LBNL：美國資料中心用電 4.4% → 6.7–12%（2028）
- 機構：US Department of Energy（研究由 Lawrence Berkeley National Laboratory 製作）
- 標題：DOE Releases New Report Evaluating Increase in Electricity Demand from Data Centers
- 日期：2024-12-20
- URL：https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers
- 載入：HTTP 200，逐字命中
- "data centers consumed about 4.4% of total U.S. electricity in 2023 and are expected to consume approximately 6.7 to 12% of total U.S. electricity by 2028"
- "total data center electricity usage climbed from 58 TWh in 2014 to 176 TWh in 2023"
- "data center load growth has tripled over the past decade and is projected to double or triple by 2028"

## F7 — Google 資料中心效率頁：2025 車隊平均 PUE 1.09 vs 行業 1.54
- 機構：Google
- 標題：Data Center Efficiency（datacenters.google/efficiency）
- 日期：2026 年頁面（內含 2025 年度數據）
- URL：https://datacenters.google/efficiency/
- 載入：HTTP 200，逐字命中
- "In 2025, the average annual power usage effectiveness for our global fleet of data centers was 1.09."
- "our data centers ... using 83% less overhead energy than the industry average"（Uptime Institute 2025 Global Data Center Survey 行業平均 PUE 1.54）
- "In 2025, our data centers delivered over 3 times more compute performance per unit of energy than five years ago"
- 園區 PUE 表（2025）：Singapore 1.12、Singapore (2nd facility) 1.14、Dublin 1.08、Mesa AZ 1.22、Omaha 1.05

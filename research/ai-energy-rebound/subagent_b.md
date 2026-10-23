# Subagent B — AI 電力：效率面 vs 使用量（反彈）面 — 證據彙整

> 研究子代理 B（科研哨兵 / Research Sentinel）。本檔案僅收錄**可驗證**證據，含完整 URL、日期、精確數字與單位，以及「頁面是否真的載入（HTTP 200）」標記。
> 最後更新：見 git/工作區時間戳。

---

## (1) 已驗證事實（Verified facts）

### A. 效率面：Google 每提示（per-prompt）能源／水耗

**Fact B1 — Google 官方部落格：每提示能源/碳排 12 個月內降 33x / 44x**
- 機構：Google（作者 Ben Gomes, Chief Technologist, Learning & Sustainability）
- 標題：*Our approach to energy innovation and AI's environmental footprint*
- 日期：2025-08-21
- URL: https://blog.google/company-news/outreach-and-initiatives/sustainability/google-ai-energy-efficiency/
- 載入狀態：**HTTP 200（已載入正文並逐字擷取）**
- 精確數字與原文：
  - "Over a 12-month period, while delivering higher-quality responses, the **median energy consumption and carbon footprint per Gemini Apps text prompt decreased by factors of 33x and 44x**, respectively."
  - "the energy consumed per median prompt is **equivalent to watching television for less than nine seconds**."
  - "In 2024, for example, we reduced our data center energy emissions by **12%** even as **electricity consumption grew by 27% year-over-year**, driven by the expansion of our business and services."
  - 連結至技術報告 arXiv:2508.15734。

**Fact B2 — 技術報告（primary source, arXiv）：median prompt 0.24 Wh、0.26 mL**
- 機構/作者：Google；Cooper Elsworth, Keguo Huang, David Patterson, Ian Schneider, Robert Sedivy, Savannah Goodman, Ben Townsend, Parthasarathy Ranganathan, Jeff Dean, Amin Vahdat, Ben Gomes, James Manyika
- 標題：*Measuring the environmental impact of delivering AI at Google Scale*
- 日期：[Submitted on 21 Aug 2025]
- URL（abs）：https://arxiv.org/abs/2508.15734 ；PDF：https://arxiv.org/pdf/2508.15734v1 ；DOI：https://doi.org/10.48550/arXiv.2508.15734
- 載入狀態：**HTTP 200（abs 頁 + PDF 687 KB 全文已抽取為文字）**
- 精確數字：
  - "the **median Gemini Apps text prompt consumes 0.24 Wh** of energy"
  - "**33x reduction in energy consumption** and a **44x reduction in carbon footprint** for the median Gemini Apps text prompt over one year"
  - "uses less energy than watching **nine seconds of television (0.24 Wh)** and consumes the equivalent of **five drops of water (0.26 mL)**"
  - Table 2（May 2025, median Gemini Apps text prompt）：
    | 指標 | Existing（narrow）Approach | Comprehensive Approach |
    |---|---|---|
    | Energy (Wh/prompt) | **0.10** | **0.24** |
    | Emissions (gCO2e/prompt, Scope 2 MB) | 0.02 (0.016) | 0.03 (0.023) |
    | Emissions (gCO2e/prompt, Scope 1+3) | (0.007) | (0.010) |
    | Water (mL/prompt) | **0.12** | **0.26** |
  - 能量拆解（comprehensive）：Active AI Accelerator **0.14 Wh（58%）**、host CPU & DRAM **0.06 Wh（25%）**、provisioned idle machines **0.02 Wh（10%）**、data-center overhead (PUE) **0.02 Wh（8%）**。
  - 量化方法差異："The comprehensive approach reveals a total energy consumption that is **2.4 times greater** than the estimate from the existing approach"；相對既有估計的 scaling factor = **1.72**（vs 既有文獻常用的 2x）。
  - Figure 4：12 個月內 Scope 2 MB 排放降 **47x**、Scope 1+3 降 **36x**、合計 **44x**。

> ⚠️ **重要更正（與任務簡報相反）**：任務簡報稱「average ~0.24 Wh、median ~0.10 Wh」。**實際相反**：arXiv 論文明確 median = **0.24 Wh**（comprehensive 完整機櫃／全棧測量），**0.10 Wh** 是「narrow / existing approach」的數字（只算 active accelerator + 較高利用率的機器）。論文原句："when applying a methodology aligned with a more narrow, existing approach, the calculated energy consumption is **only 0.10 Wh per prompt**"。Google 部落格與論文摘要一律引用 **0.24 Wh**。詳見「(3) Contradictions」。

**Fact B3 — 同期其他機構的每提示估算（全部經 arXiv 論文引用，該論文本身已載入）**
- URL 同上：https://arxiv.org/abs/2508.15734
- 載入狀態：**HTTP 200**
- 精確數字（原文引述）：
  - **Sam Altman, June 2025 部落格**：平均 ChatGPT prompt 約 **0.34 Wh** 能源、水 **0.000085 gallons（0.3 mL）**。Google 批評：「provides no explanation of the measurement boundary or methodology」。
  - **Mistral AI / ADEME / Carbone 4（2025，peer-reviewed LCA）**：Mistral Large 2，Le Chat 一般 **400-token** 回覆，marginal impact **1.14 g CO2e**、水 **45 mL**。
  - **Epoch.AI（2025）**：以 GPT-4o（MoE，約 100B active params，NVIDIA H100）估算典型 ChatGPT prompt ≈ **0.3 Wh**。
  - **EcoLogits**：50 output-token prompt，區間 **1.83–6.95 Wh**。
  - **De Vries (2023)**：單一 GPT-3.5 prompt ≈ **3 Wh**。
  - **Li et al. (2025)**：Microsoft 美國資料中心的 GPT-3 推論，每 **10–50** 個 prompt 耗掉 **500 mL** 一瓶水。
  - **Luccioni et al. (2022)**：BLOOM，無 batch 推論 18 天平均 **4 Wh/prompt、1.5 gCO2e/prompt**。
  - **Samsi et al. (2023)**：LLaMA-65B 約 **0.3 Wh**／每次回覆。
- Google 自己的總結：「There is an **order-of-magnitude of variability** in the estimated energy per chat prompt」。

---

## (2) Unverified or unavailable

（待補）

---

## (3) Contradictions

（待補）

---

## (4) Best case study

（待補）

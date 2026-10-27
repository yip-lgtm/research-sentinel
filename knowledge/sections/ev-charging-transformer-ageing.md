# 午夜後充電會更快燒老配電變壓器

領域：電氣工程／配電網／電動車 ｜ 主題 slug：`ev-charging-transformer-ageing` ｜ 對應報告：`2026-10-23-11`

## 核心事實

- **【機制】** IEEE C57.91 動態熱模型：25 kVA 桿上變壓器服務 12 戶兼 6 車時，不受控交流 Level 2 充電令年等效老化 FEQA 達 9.79；佛蒙特同條件只有 2.34。
- **【機制】** 兩地行程與充電排程相同，差異源自環境溫度與繞組熱點升溫，非充電電量。熱點升溫加速絕緣紙劣化；曾短暫接近「每年老化 50 年」。
- **【機制】** 午夜後充電令 FEQA 由 9.79 升至 10.81、2.34 升至 2.91。低價窗把多車同步，令同一變壓器出現窄時段高負荷；論文指分時收費可造成同類反效果。
- **【敏感度】** 情境一：佛蒙特 2.34，溫度回饋減 4.8 倍，充電成功率逾 97%。情境二：鳳凰城 9.79，回饋減 6.3 倍，p<10⁻³。情境三：NLR 指多數公用事業平均負載低於 30%、峰值低於 60%，若餘裕充足，增量老化可不重要——結論由「有害」變「不重大」，不會翻正。
- **【事實】** Ofgem 2026-06-11 決定：架空低壓服務單位費 0.35→1.44 千英鎊，地下 1.60→2.65 千英鎊；相關開支 ex ante 額度 26.4 億英鎊。
- **【Mechanism】** An IEEE C57.91 dynamic thermal model: on a 25 kVA pole-mounted transformer serving 12 homes and 6 plug-in EVs, uncontrolled AC Level 2 charging drove annual factor of equivalent ageing (FEQA) to 9.79, versus 2.34 in Burlington under the same setup.
- **【Mechanism】** Travel and charging schedules were identical in both cities, so the difference comes from ambient temperature and winding hot-spot rise, not energy charged. Hot-spot heating accelerates cellulose-insulation ageing; one uncontrolled hot-day case briefly approached 50 years of ageing per year.
- **【Mechanism】** After-midnight charging raised FEQA from 9.79 to 10.81 and from 2.34 to 2.91. A cheap window synchronises vehicles, creating a narrow high-load spike on one transformer; the authors warn time-of-use pricing can cause the same effect.

## 量化鏈與口徑

- 來源數：7；報告篇幅：8414 bytes / 798 中文字。
- 本章節由 `sync_state.py` 從報告正文抽取，用作防重複登記與知識索引；
  細節以存檔版報告正文為準（`reports/2026-10-23-11.md`）。

## 誠實邊界

本條目由自動抽取生成，**未經獨立重新查證**；引用前必須回讀存檔版報告正文與原始來源。報告自述嘅缺口（見簡評段）在此原樣保留，唔會被稀釋成更強嘅斷言。

## 相關條目

- 知識庫索引：`knowledge/INDEX.md`
- 主題登記：`knowledge/topics.json` → `ev-charging-transformer-ageing`

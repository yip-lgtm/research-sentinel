# 海上風電單樁陰極保護：塗層升級省 79.8% 陽極，能否「順便」降低氫脆風險？

領域：材料工程／海洋工程／陰極保護 ｜ 主題 slug：`offshore-wind-monopile-cathodic-protection` ｜ 對應報告：`2026-10-23-09`

## 核心事實

- **【量化】** Taskiran（IJECE, 2022）模型：平均電流需求無塗層 893.69 A、I 級 861.79 A、II 級 364.86 A、III 級 180.95 A。鋁陽極則為 108,732、104,851、44,391、22,016 kg。III 級省 79.8%，I 級只省 3.6%。
- **【機制】** DNV 以 fc=k1+k2·t/2 描述塗層劣化；0–30 m 平均 fc 為 I 級封頂 1、II 級 0.425、III 級 0.2075。四種方案共用同一幾何、水深與水溫，差異只來自 fc，故節省不是環境假設造成。
- **【機制】** 塗層是電流側槓桿，氫是電位側槓桿。DNV-RP-B401（2021）指出，-0.80 至 -1.10 V 區間原子氫產量隨電位更負而指數上升；過保護只指低於 -1.15 V。故多塗一層不等於可採用更負電位。
- **【機制】** DNV 對鐵素體鋼以 SMYS ≤500 MPa 且焊接硬度 ≤350 HV 作 CP 相容門檻；高強度材料則採較嚴電位上限。故氫脆判定必須連接母材、HAZ 硬度與電位紀錄，單憑「有裂縫」不足。
- **【替代解釋】** 海水本身會加速焊接試樣裂紋增速，疲勞與氫可能是並行機制。Havtil 2024 報告調查高強度自升式平台腿與樁靴過渡段氫致裂紋，但其公開頁只列機制範圍，未披露裂縫尺寸或受影響腿數。疲勞與氫的分離仍待材料證據。
- **【敏感度】** 鋁電容量由 2,000 降至 1,500 再至 720 Ah/kg，III 級陽極變 22,016、29,354、61,154 kg；壽命 25→30 年使 fc 由 0.2075 升至 0.245（+18%）；平均電流密度若放大 25%，質量同比例上升。方向不變，只有當 fc ≥1（I 級情況）時「塗層省料」結論失效。
- **【Quantified】** Taskiran's 2022 model gives mean current demand of 893.69 A (uncoated), 861.79 A (Cat I), 364.86 A (Cat II) and 180.95 A (Cat III), with standoff aluminium anode masses of 108,732, 104,851, 44,391 and 22,016 kg. Category III saves 79.8%; Category I saves only 3.6%.
- **【Mechanism】** DNV models coating breakdown as fc=k1+k2·t/2: mean fc at 0–30 m is 1 (capped) for Cat I, 0.425 for Cat II and 0.2075 for Cat III. Geometry, depth and temperature are identical across cases, so only fc drives the saving.

## 量化鏈與口徑

- 來源數：5；報告篇幅：8682 bytes / 870 中文字。
- 本章節由 `sync_state.py` 從報告正文抽取，用作防重複登記與知識索引；
  細節以存檔版報告正文為準（`reports/2026-10-23-09.md`）。

## 誠實邊界

本條目由自動抽取生成，**未經獨立重新查證**；引用前必須回讀存檔版報告正文與原始來源。報告自述嘅缺口（見簡評段）在此原樣保留，唔會被稀釋成更強嘅斷言。

## 相關條目

- 知識庫索引：`knowledge/INDEX.md`
- 主題登記：`knowledge/topics.json` → `offshore-wind-monopile-cathodic-protection`

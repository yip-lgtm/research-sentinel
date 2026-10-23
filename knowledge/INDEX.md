# 知識庫索引

科研哨兵的持久化知識體系。所有內容寫入磁碟，不依賴單次對話記憶。

## 目錄

| 檔案 | 內容 | 狀態 |
|---|---|---|
| `amr-burden-age-divergence.md` | 抗藥性死亡負擔的年齡分化與治理槓桿（GRAM 2024、WHO 管線、丹麥黃卡、污水 ARG） | 建設中 |
| `engineering-education-path.md` | 工程教育路徑（中學 → 副學位 → 學士 → 碩博 → 地區差異 → 認證） | 建設中（頭兩小時） |
| `perovskite-tandem-lcoe-warranty.md` | 鈣鈦礦—矽堆疊：LCOE 門檻（29%→>21 年、32%→19 年）、CRF 融資年限敏感度、IEA 劣化機制、Oxford PV 保固落差 | 建設中 |
| `hearing-cognition-risk-stratified.md` | 助聽干預：ACHIEVE 總體陰性 vs 風險分層 61.6% 有效、中介路徑斷點、WHO HEAR ROI 所得梯度 | 建設中 |
| `nitrogen-nue-loss-reduction.md` | 氮效率：452 縣示範減氮增產、反應性氮流失機制、N2O 因子敏感度、經濟最佳率 vs 農藝最佳率 | 建設中 |
| `domains/` | 各研究領域的長期累積筆記 | 依需求建立 |

## 覆蓋登記

已充分覆蓋的主題記錄在 `topics.json`，避免重複產出。目前 10 個主題，最高覆蓋率 0.78（edu-bachelor-branches）。

### 近期新增章節（2026-10-23）
- `perovskite-tandem-lcoe-warranty.md` ← 報告 `2026-10-22-21`（用戶評「合格」）
- `hearing-cognition-risk-stratified.md` ← 報告 `2026-10-22-22`（用戶評「合格」）
- `nitrogen-nue-loss-reduction.md` ← 報告 `2026-10-23-00`（未評分）

## 原則

- 每份報告至少有一條新知識寫回知識庫（否則該報告只是噪音）
- 來源必須可追溯：URL + 發布日期 + 機構
- 發現與推論分開標註
- 覆蓋率低的主題優先；覆蓋率高的主題需有新進展才再寫
- 報告雙語化會令 bytes 翻倍：撰寫時直接用**中英分段散文**（非逐條鏡像），
  品質閘上限 9000 bytes／1000 中文字，中文段保留全部數字、英文段只留要點與數字
- ⚠️ 教訓：不要用 read_file 的輸出直接覆寫檔案（會把行號 `N|` 寫進檔案）。
  覆寫前必須確認內容不含 `^\s*\d+\|`；改檔用 patch／execute_code 讀原檔再用 write_file 寫回

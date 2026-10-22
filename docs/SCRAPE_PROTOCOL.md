# 爬取執行協議（Protocol v2）— 所有 subagent 必讀

## 為何改版
v1 太慢：subagent 在「抓取」階段用盡 tool-call 上限，導致檔案從未寫入。
v2 規則：**先建檔，再增量填充**。任何時候被截斷，已寫入的內容都保留。

## 硬性規則（違反 = 任務失敗）

1. **第一個 tool call 必須寫入目標 markdown 檔的骨架**（含所有章節標題），之後每抓到一批內容就用 patch/append 填充。
   絕對不要「先抓完全部資料才開始寫」。
2. **JSON 檔也要早寫**：第一個 tool call 同時寫入含 `sources: []` 的合法 JSON，之後用 patch 追加來源條目。
3. **每 8–10 次 tool call 就要落盤一次**（patch 寫入已確認的內容），不要累積在腦中。
4. **max_iterations 已提高到 150**，足夠。但仍要遵守 1–3 條。
5. **禁止重試已知被封的網域**（浪費 tool call）：
   - www.hkqf.edu.hk → TCP timeout，改用 HKCAAVQ 站
   - web.archive.org → timeout
   - www.ncees.org → 520，改用 fe board / state board 站
   - www.ice.org.uk → 403，改用 ICE 其他路徑或 engineeringcouncil/ICE 新站
   - ibo.org → 403，改用 www.ibo.org 的替代路徑 或 大學/政府轉述頁
6. **優先用 curl 直抓**（比 MCP 抽取省 token）：
   ```bash
   curl -sS -k -L --max-time 30 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36" \
     -H "Accept-Language: en-US,en;q=0.9" "URL" -o /workspace/raw2/NAME.html
   ```
   然後用 `/workspace/html2txt.py`（已存在）轉純文字，或 `grep -o` 抽關鍵段落。
7. **PDF**：下載到 `/workspace/pdf2/`，用 `/workspace/pdftext.py` 抽文字（已存在）。
8. **不要重寫已抓到的原始檔**。已下載的原料在 `/workspace/raw/`（HKU syllabus 文字檔、MIT degree chart HTML）。

## 可用的現成工具（在 /workspace）
- `html2txt.py FILE [-max N]` → HTML 轉可讀文字
- `pdftext.py FILE [maxchars]` → PDF 抽文字
- `fetch.py URL [maxchars]` → 直接抓網址並轉文字
- `links.py URL [regex]` → 列出頁面內連結
- `search.py "query" [n]` → Bing 搜尋（用 curl）
- `srch.py "query"` → Bing 搜尋另一實作
- `s2.py "query"` → Bing 搜尋第三實作
- `ddg.py "query"` → DuckDuckGo 搜尋
> 三個搜尋工具都試過：Bing 可用但結果雜；DuckDuckGo html 端點也可用。
> **搜尋只是找 URL 的手段，找到後必須 fetch 原始頁面才算數。**

## 已核實可達網域（可直接抓）
vtc.edu.hk, ive.edu.hk, polyu.edu.hk, hku.hk, cityu.edu.hk, hkust.edu.hk, cuhk.edu.hk
uwe.ac.uk, bbk.ac.uk, engc.org.uk, qaa.ac.uk, ofqual.gov.uk, heacademy.org, nces.ed.gov
abet.org, acenet.edu, gov.uk, open.ac.uk, hkeaa.edu.hk, jupas.edu.hk, thei.edu.hk
hkcaavq.edu.hk, mit.edu, stanford.edu, purdue.edu, illinois.edu, umich.edu, gatech.edu
cam.ac.uk, imperial.ac.uk, manchester.ac.uk, birmingham.ac.uk, leeds.ac.uk

## 寫作格式（嚴格）
- 繁體中文為主，技術術語保留英文原文
- 大量表格
- 每節末「本節缺口」
- 【事實】/【推論】/【缺口】標註
- 目標 2000–3500 字；寧可精確不要灌水
- 沒來源的數字 → 刪掉，不要「一般來說」「通常」

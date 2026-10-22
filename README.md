# 科研哨兵 (Research Sentinel)

一個長期存在的研究代理，負責持續探索、整理與提煉對人類有實際貢獻的科學與工程知識。

## 運作模式

- **每小時報告**：100–1000 字，中文為主，固定結構（主題 / 核心發現 / 潛在影響 / 來源依據 / 簡評）
- **基礎建設階段**（頭兩小時）：建立工程教育路徑知識庫
- **自由探索階段**：優先與人類福祉相關的科研進展
- **評分壽命機制**：合格 +1 級 (+5h)、滿分 +2 級 (+10h)、壽命歸零暫停輸出

## 目錄結構

```
SOUL.md              核心身份定義
state.json           壽命 / 等級 / 階段 / 主題表現（持久化）
score.py             評分與壽命管理 CLI
knowledge/           長期知識庫
  INDEX.md             知識庫索引
  topics.json          主題覆蓋登記
  engineering-education-path.md
templates/
  report_template.md   報告模板
reports/             每小時報告存檔
```

## 使用

```bash
python3 score.py status              # 顯示狀態
python3 score.py pass  [主題]        # 合格
python3 score.py full  [主題]        # 滿分
python3 score.py fail  [主題]        # 不合格
```

## 原則

1. 貢獻優先 — 只做對人類有實際價值的方向
2. 可驗證 — 公開可追溯來源，發現與推論分開
3. 清晰勝過華麗 — 讓人讀得懂、用得上
4. 長期主義 — 穩定持續輸出，不追求短期熱點
5. 誠實面對限制 — 不知道就說不知道，標註缺口

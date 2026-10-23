# 金屬積層製造（AM）零件疲勞機制：結構化研究筆記

> Section: `am-fatigue-mechanism` ｜ 狀態：骨架已建立，內容增量填充中
> 規則：【事實】= 來源直接陳述；【推論】= 綜合判斷；【缺口】= 未取得

---

## 0. 骨架：機制鏈箭頭圖

```
[AM 製程特有缺陷]
  ├─ (A) as-built 表面粗糙度 Ra/Sa 高
  ├─ (B) 內部孔隙：gas porosity / lack-of-fusion (LOF)
  ├─ (C) 顯微組織：柱狀晶/織構/α-lamellar、缺陷堆積
  └─ (D) 殘餘應力（多為 tensile）＋ 位錯密度
        ↓
[局部應力集中因子 Kt 上升]
        ↓
[裂紋萌生位置]
  ├─ 表面萌生 (surface-initiated) ← 粗糙度峰值 → notch effect
  └─ 內部萌生 (internal / subsurface-initiated) ← 孔隙/LOF
        ↓
[壽命消耗機制：短裂紋階段主導]
  ├─ Kitagawa–Takahashi 門檻 (a*)
  └─ Murakami √area 缺陷當量 → 疲勞極限推估
        ↓
[AM vs machined 差距]
  ├─ 疲勞極限下降 %、N_f 壽命倍數差
  └─ S–N 曲線整體左移
        ↓
[後處理回收手段]
  ├─ HIP（消除孔隙，不改表面）
  ├─ 表面加工 / 機加工余量 0.2–0.3 mm（降 Ra）
  ├─ Shot peening（引入 compressive residual stress）
  ├─ Stress relief / 去應力退火
  └─ 抛光 / 電解加工 / 激光表面熔覆重熔
```

## 0.1 數據表欄位（骨架）

### 表 1：量化數據表
| 牌號 | 狀態 (as-built / machined / HIP / machined+HIP) | Ra (µm) | 孔隙率 (%) | 測試條件 (RT/高溫, R, 減少截面, 頻率) | 疲勞極限 (MPa) | 對 machined 下降 (%) | N_f 差距 | 來源 URL |

### 表 2：表面粗糙度與疲勞強度表
| 牌號 | 表面處理 | Ra/Sa (µm) | 疲勞極限 (MPa) | 提升 (%) | 來源 |

### 表 3：孔隙率門檻表
| 牌號 | 孔隙率 (%) | 缺陷類型 | 失效模式 (表面/內部) | 壽命/極限變化 | 來源 |

### 表 4：Kitagawa–Takahashi 試算表
| 情境 | 缺陷當量 area (µm²) | sqrt(sqrt(area)) | σ_w = 1.58·HV + 0.1025·X (MPa) | 與 machined 差距 |

---

## 1. 機制鏈細節

### 1.1 NASA MSFC 的一次「受控拆解」實驗（最關鍵的對照設計）
【事實】Lambert (NASA MSFC, 20160006998) 的設計刻意把「表面」與「內部」解耦：所有試片**都做過 HIP + 均質化 + 溶液時效處理（AMS 5663M）**，因此孔隙率在 AB 與 LSG 兩組間相同；兩組唯一差別是**表面狀態**（AB as-built vs LSG low-stress ground，額外加料機加工至 ≤ 4 µin RMS）。
- 【事實】試驗標準：ASTM E647-13A，R = 0.12，40 Hz，試片軸向 = build direction (z)。試驗溫度：RT / 800°F / 1000°F / 1200°F（1000°F 變異過大被排除）。
- 【事實】AB 平均表面粗糙度（RMS, µin）：RT 247 ± 39、800°F 267 ± 43、1200°F 243 ± 42、1000°F 245 ± 67；LSG 為「優於 4 µin」。
- 【事實】線性近似法（S–N 曲線上取相同壽命點比對 Smax,norm）：
  - RT：N=80,863 → AB 0.62 / LSG 0.91 → **knockdown 32%**；N=1,574,926 → AB 0.43 / LSG 0.62 → **knockdown 31%**
  - 800°F：N=43,551 → 0.66 / 0.96 → **36%**；N=47,505 → 0.62 / 0.97 → **36%**
  - 1200°F：N=32% / N=31%（表中兩組值）
  - 結論：**as-built 表面相對 low-stress ground 需以約 2/3 的最大應力才能達到相同壽命，即 knockdown ≈ 1/3 (33%)**。
- 【事實】KP 法（pseudo-stress intensity factor Kp = Smax,norm·√f，f 為 RMS 粗糙度 µm）：RT knockdown 隨壽命上升：N=5e4 → 19%；1e5 → 24%；1e6 → 37%；4e6 → 43%。800°F：N=3.2e4 → 26%；5.4e4 → 32%。1200°F 反向：N=4e4 → 15%；1e5 → 14%；1e6 → 11%；1.25e6 → 11%。
- 【事實】作者結論：**N < 1e6 cycles 時保守 knockdown ≈ 1/3；N > 1e6 時 knockdown 增大，不建議外推**。1200°F 趨勢反常原因未知（推測為 overaging）。
- 【推論】這是「排除替代解釋 (i) 孔隙」的最強證據之一：兩組都已 HIP，孔隙相同，差距仍達 32–36%。

### 1.2 KT 與 El-Haddad / Murakami √area 模型在 AM 上的應用
【事實】Nur Mohammed, Awd, Walther et al., *Materials* 16:6334 (2023) — "Comparison of Various Intrinsic Defect Criteria to Plot Kitagawa–Takahashi Diagrams in Additively Manufactured AlSi10Mg"（TU Dortmund, WPT）。用 4 種 intrinsic defect length 方法建 KT 與 El-Haddad 圖，並以 Paris law 推壽命再與實驗比對。
- 【事實】Intrinsic crack length 公式（式 6/7）：a₀ = 1.56·HV + 120/(1.60·HV)，σ_w = 1.56·HV + 120·a^(1/6)。
- 【事實】試驗：SLM 250 HL AlSi10Mg，相對密度 > 99.54%；20 Hz 與 20 kHz（超聲）疲勞，R = −1，100/120/140 MPa；試片軸向 90° 垂直於建造平台。
- 【事實】結果：batch A（無平台加熱）疲勞壽命明顯低於 batch B（平台加熱至 200 °C），同一應力下壽命增加；SEM 斷口顯示**裂紋由次表面（subsurface）缺陷萌生**。
- 【事實】最佳方法誤差：batch A 120 MPa → 5.8%；batch B 120 MPa → 0.29%；batch A 100 MPa → 6.66%；batch A 140 MPa → 0.5%。
- 【事實】該文引用的關鍵 AM 疲勞文獻：Masuo et al. (Int J Fatigue 2018, 117:163-179)「defects, surface roughness and HIP」；Sanaei & Fatemi (MSE A 2020, 785:139385)「internal defects on fatigue performance」；Beretta & Romano (Int J Fatigue 2017, 94:178-191)「fatigue strength sensitivity to defects for materials manufactured by AM or traditional processes」；Pessard et al. (Int J Fatigue 2021, 149:106206)「pores and tested volume size」；Benedetti et al. (Int J Fatigue 2018, 107:96-109)「mean stress and defect sensitivity」。



## 2. 量化數據

（填充中）

## 3. 敏感度與 Kitagawa–Takahashi 試算

（填充中）

## 4. 替代解釋與對照實驗設計

（填充中）

## 5. 來源清單

（填充中）

## 本節缺口（累計）

（填充中）

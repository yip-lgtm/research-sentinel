# AI 程式設計助理生產力：證據事實表（一級來源）

## METR verification tax 時間分解（來源：arXiv v2 官方 e-print 原始碼 macros.tex，https://arxiv.org/e-print/2507.09089v2）
- Reviewing/cleaning AI outputs: AI-allowed 6 min / 9%；AI-disallowed 0 min / 0%
- Prompting AI: 5 min / 8%；0 / 0%
- Waiting on AI generation: 4 min / 4%；0 / 0%
- Active coding (高階): 20 min / 24%；24 min / 36%
- Writing code (細項): 15 min / 18.1%；20 min / 30.6%
- Idle overhead: 8 min / 10%；4 min / 6%
- Paused: 5 min / 5.0%；2 min / 4.1%
- 樣本：44 AI-allowed / 30 AI-disallowed / 74 段有效螢幕錄影
- 接受率：developers accept <44% of AI generations（PctAcceptedAddedLinesOfCode=44）
- 退出問卷：75% 會逐行閱讀 AI 程式碼；56% 需改動主要部分
- 原文：https://arxiv.org/pdf/2507.09089v2 §3.2 p.9「Figure 19: Average minutes spent on different high-level activities when completing issues with AI-allowed vs. AI-disallowed.」

## DORA 2025（官方 PDF：https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf，142 頁）
- 「AI adoption has become nearly universal. The majority of survey respondents (90%) use AI as part of their work and believe (more than 80%) it has increased their productivity.」Executive summary p.4
- Figure 24 p.30：Extremely increased 13% + Moderately 31% + Slightly 41% = 85%；下降合計 5%
- 「AI adoption now improves software delivery throughput, a key shift from last year. However, it still increases delivery instability.」p.4
- 「90% of organizations have adopted platform engineering」p.4
- 引述 2024 DORA p.35：「an estimated 1.5% reduction in software delivery throughput and an estimated 7.2% increase in software delivery instability for every 25% increase in AI adoption」
- NOT VERIFIED：受訪者層級的「% 回報 throughput 改善／instability 上升」百分比不存在，只有 Figure 28 標準化回歸係數方向。

## Anthropic（https://www.anthropic.com/research/AI-assistance-coding-skills，Published Jan 29, 2026）
- 「We recruited 52 (mostly junior) software engineers ... unfamiliar with Trio」
- 「the AI group averaged 50% on the quiz, compared to 67% in the hand-coding group—or the equivalent of nearly two letter grades (Cohen's d =0.738, p =0.01)」
- 「The largest gap in scores between the two groups was on debugging questions」
- 「participants in the AI group finished about two minutes faster, although the difference was not statistically significant」
- AI delegation (n=4)：「The average quiz scores in this group were less than 40%」
- 使用方式結果被頁面限定為相關非因果
- 論文：arXiv:2601.20245（只取得摘要級結論）

## 其他已驗證
- METR 2026-02-24（https://metr.org/blog/2026-02-24-uplift-update/）：原參與者 −18%（CI −38%~+9%）、新招募者 −4%（CI −15%~+9%）；30%–50% 開發者不願在無 AI 下工作而不出題 → lower bound, very weak evidence
- METR 2026-05-11：349 technical workers，自報工作價值變化中位數 1.4–2×（METR 自言此量級應抱持懷疑）
- Peng et al. arXiv:2302.06590：Copilot 55.8% 加速；開發者自估 35%（保守）；年資每增 1 年效果減 11.70（SE 2.47, p=0.0168）；25–44 歲組較大（p=0.0303）；Java/Python 無顯著差異（p=0.5895/0.7240）
- BLS（https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm）：software developers median 年薪 $135,980（2025-05）；developers+QA+testers 合併 1,905,400 人、median $134,040／年、$64.44／小時；2025–35 成長 10%、淨增 185,400
- GitClear 2025（https://www.gitclear.com/ai_assistant_code_quality_2025_research）：211M changed lines（2020–2024）；refactoring 25%（2021）→ <10%（2024）；copy/paste 8.3% → 12.3%（+48%）
- Stack Overflow 2025：52% 認為 AI 提升生產力；66%  frustration =「almost right, but not quite」；45.2% = debugging AI code more time-consuming；20% 對 problem-solving 信心下降；12.2% strongly agree AI agents 改善程式碼品質；experienced devs 20.7% highly distrust vs learning-to-code 6.1% highly trust

## 未驗證（不得引用）
- Uplevel 2024（uplevel.com 全部回 202）、Cui et al. SSRN（403）、DORA 受訪者層級百分比、$/developer-year 官方換算（無）
- METR：searching/reading codebase 與 planning/debugging 的分鐘分解（原始碼無對應巨集，點陣圖不可抽取）

# 04 碩士／博士：研究生教育層級（Postgraduate / Research Degrees）

> 狀態：首輪內容填充完成（2026-10-22 14:xx UTC）。
> 資料來源學校／機構：香港大學（HKU）、香港科技大學（HKUST）、香港中文大學（CUHK）、麻省理工學院（MIT）、史丹佛大學（Stanford）、剑桥大学（Cambridge）、帝國理工學院（Imperial College London）、Engineering Council、GOV.UK、QAA。

## 0. 本章導覽與範圍界定

本章填補知識庫中「學士 → 研究生」的缺口：聚焦工程領域的**碩士（master's）與博士（doctoral）**層級，
比較三個地區（香港、美國、英國）在學位命名、學分／學制結構、授課型 vs 研究型取向、
以及專業認證銜接上的差異。

【事實】英國官方框架基準，GOV.UK「What qualification levels mean」的
「list of qualification levels」頁（https://www.gov.uk/what-different-qualification-levels-mean/list-of-qualification-levels）
將 **Level 7** 列為「integrated master's degree, for example master of engineering (MEng)」
與「master's degree, for example master of arts (MA), master of science (MSc)」，
**Level 8** 為「doctorate, for example doctor of philosophy (PhD or DPhil)」。

【事實】QAA「Characteristics statements」頁（https://www.qaa.ac.uk/the-quality-code/characteristics-statements）
載明：「Master's degrees sit at Levels 7 and 11, and doctoral qualifications at Levels 8 and 12.」
（Level 11／12 為蘇格蘭 FQHEIS 框架，故同一批英國學位在英格蘭與蘇格蘭分屬不同編號。）

【事實】香港側以 HKU 工程學院（engg.hku.hk）一手頁面為主軸，並對照 HKUST、CUHK；
美國側以 MIT（catalog.mit.edu、eecs.mit.edu）與 Stanford（ee.stanford.edu）為主軸；
英國側以 Cambridge（postgraduate.study.cam.ac.uk）與 Imperial College London 為主軸；
認證側以 Engineering Council（engc.org.uk）一手條文為主。

【推論】三地的差異不在「博士是否需要做原創研究」——這一點是共通的；而在**碩士這個中間層**的
功能分化：英美把 taught master's 做成「職業化再教育＋國際生招募」的產品（Cambridge 明言
MPhil 是「preparation for a PhD」而另立 taught 課程），香港則以 MPhil 作為研究型博士的
標準入口、把 MSc(Eng) 定位為「銜接專業學歷的選修型學位」。下文各節以一手條文檢驗此推論。

**本節缺口**
- PolyU（www.polyu.edu.hk）本次抓取多次超時，判定為受阻，PolyU 的工程研究生課程未取得一手資料（見第 8 節）。
- MIT／Stanford 的「研究生入學人數」等統計數字，本章未取得可引用的一手頁面。
- HKU 研究生院（gradsch.hku.hk）的學位課程總表路徑回傳 404，未取得。

## 1. 學位類型與結構：Taught master's vs Research master's vs PhD

【事實】英國框架把「master's degree」（Level 7 授課型）與「integrated master's degree」
（Level 7，MEng）分列為兩種；這一命名差異在制度上對應**兩種不同的高等教育途徑**：
英國四年制 Integrated MEng 課程（本科即入學，畢業直接取得 MEng），
與三年制本科＋一年制授課型 MSc。

【事實】MIT 明確採「integrated」路徑：Course 6-P degree chart 原文
「The Master of Engineering degree is awarded only to students who have already received,
or who will simultaneously receive, one of the Bachelor's degrees listed below.」
並列出 Course 6-3、6-4、6-5 三個學士學位——**MEng 不能單獨取得**。

【事實】Cambridge 的官方 Course Directory 提供一手「Taught/Research」二分欄位：
篩選選項原文為 `<option value="153">Research (169)</option><option value="154">Taught (188)</option>`，
Course Level 選項為 `Certificate/Award (10)`、`Diploma (11)`、`Doctoral (117)`、`Master's (221)`，
表頭為 `Course | Course Level | Taught/Research | Course Length`，
頁面正文稱「search over 300 postgraduate courses at Cambridge」。

【事實】**關鍵發現：Cambridge 官方分類中，MPhil 學位不等同於「研究型」。**
從目錄表逐行擷取的工程系課程（Course Level 與 Taught/Research 皆為原文欄位）：

| 課程 | Course Level | Taught/Research | Course Length |
|---|---|---|---|
| Advanced Chemical Engineering — MPhil | Master's | **Taught** | 11 months full-time |
| Electrical and Electronic Engineering — MPhil | Master's | **Taught** | 10 months full-time |
| Energy Technologies — MPhil | Master's | **Taught** | 11 months full-time |
| Engineering — MPhil | Master's | **Research** | 12 months full-time / 24 months part-time |
| Chemical Engineering and Biotechnology — MPhil | Master's | **Research** | 12 months full-time / 2 years part-time |
| Chemical Engineering — PhD | Doctoral | **Research** | 3-4 years full-time / 4-7 years part-time |
| Engineering — PhD | Doctoral | **Research** | 3-4 years full-time / 4-7 years part-time |
| Engineering (Industrial) — PhD | Doctoral | **Research** | 3-4 years full-time / 4-7 years part-time |
| Advanced Computer Science — MPhil | Master's | **Taught** | 9 months full-time |

【推論】Taught/Research 標籤是**課程層級**的屬性，不是學位名稱的屬性。
「MPhil」在英國是学位名稱（Master of Philosophy），
其是否具備 PhD 銜接功能，取決於該**特定課程**是否被歸為 Research、
以及課程頁對 PhD continuation 的具體條款，而非名稱本身。
這對「英國 MPhil = 博士預備」的常見概括構成重要修正。

## 2. 香港：HKU / HKUST / CUHK 的工程研究生課程

### 2.1 HKU：MPhil 與 PhD

【事實】HKU 工程學院「Programme Structure」頁（https://engg.hku.hk/Admissions/PhD-MPhil/Programme-Structure）
載明 MPhil 規範修讀期（normative study period）為
**全日制 24 個月／非全日制 36 個月**（2025 年 9 月前及後入讀者相同）。
三年制 PhD 為**全日制 36 個月／非全日制 54 個月**；
四年制 PhD 為**全日制 48 個月／非全日制 72 個月**。

【事實】同一頁載明試用期（probationary period）依入讀日期而異：
2025 年 9 月或之後入讀者，MPhil 試用期為全日制 12 個月／非全日制 12 個月
（**非全日制由 18 個月縮短為 12 個月**）；四年制 PhD 試用期為全日制 24 個月／非全日制 24 個月
（全日制**由 18 個月延長為 24 個月**）。此為 2025 年研究型學位體系改革的具體制度變化。

### 2.2 HKU：MSc(Eng) 與香港專業認可的關係

【事實】HKU「MSc(Eng) Programme Structure and Duration」頁載明：
全日制規範修讀期 **1 年**、最長 **2 年**；非全日制規範修讀期 **2 年**、最長 **3 年**。

【事實】HKU「MSc(Eng) Fees」頁載明 2026-27 入學的學費：
本地生 **HK$250,000**、非本地生 **HK$375,000**（composition fee）。

【事實】HKU 頁面明載：HKIE「has no policy for accreditation of MSc degrees in Hong Kong」；
並建議首個學位未被專業機構認可者**強烈建議選修 project 選項**。
這解釋了為何香港的 MSc(Eng) 多以「授課＋專題」而非純授課的形式存在。

### 2.3 HKUST：SENG 的 MPhil / PhD 對照

【事實】HKUST School of Engineering「MPhil / PhD Programs」頁
（https://seng.hkust.edu.hk/academics/research-postgraduate/mphil-phd-programs）載明：
- MPhil：**2 years**（全日制）／非全日制另計；
- PhD：**4 years**，若已取得相關研究型碩士則為 **3 years**；
- 原文另列 **6 years** 對應非全日制 PhD；
- 論文須經 **thesis defense**（論文答辯）考核。

【推論】HKUST 的「3 年 PhD 給有相關 MPhil 者」制度，與 Cambridge 的
「本 MPhil 可銜接 PhD／不可銜接」逐課程區分的做法，
構成同一區域（亞洲 vs 歐洲）內研究型碩士作為博士預備階段的兩種截然不同邏輯：
香港是**一體化路徑**（MPhil 幾乎自動銜接 PhD），劍橋是**逐課程裁決**。

### 2.4 CUHK：Graduate School 課程層級

【事實】CUHK Graduate School「Engineering」課程列表頁
（https://www.gs.cuhk.edu.hk/programmes/engineering）提供工程相關的
MPhil / PhD / MSc 課程層級查詢入口。CUHK 電子工程系頁面
（https://www.ee.cuhk.edu.hk/）本次可取得（200, 144KB），
但本次會話未能從其正文擷取逐一的學位時長與 MPhil/PhD 對照條款
（列為第 8 節缺口）。

## 3. 美國：MIT / Stanford 的工程研究生制度

### 3.1 MIT：MEng 為 Course 6-P，與學士綁定

【事實】MIT Course 6-P（Master of Engineering, Electrical Engineering and Computer Science）
degree chart 的 graduate component 明細：

| 項目 | 學分 |
|---|---|
| 6.THM — Master of Engineering Program Thesis | 24 |
| 6.9830 — Professional Perspective Internship | 1 |
| Four graduate subjects totaling at least 48 units（其中至少三門須符合某一 concentration field） | 48 |
| Subjects that satisfy a degree requirement in Course 6 or Course 18 totaling at least 18 units | 18 |
| **Total Units** | **91** |

【事實】6.9830 Professional Perspective Internship 計入 MEng 的 91 units，
是 MIT 把**產業界實習制度化為研究生學分**的明文依據 ——
對照 03a 章節已記錄的「MIT 學士階段不設必修實習」，
這是一條可查證的制度斷裂。

### 3.2 Stanford：MS 與 PhD 的分界

【事實】Stanford EE 碩士頁（https://ee.stanford.edu/admissions/ms）載明 MS 學位
要求 **45 units of study**、**no thesis requirement**，並把 MS 定位為 **terminal degree**
（終端學位，非通往博士的必經站）。

【事實】Stanford EE 博士頁（https://ee.stanford.edu/admissions/phd）載明
**master's degree is not required** 為博士申請的前置條件之一
（可由直博方式進入），PhD 修業年限為 **5-7 years**。

【推論】美體系的碩士在功能上分化為兩種：可論文型 MS 與 terminal MS；
而「博士不需要先拿碩士」是美國體系的結構性特色，
對照英國（Cambridge 幾乎所有 MPhil 都附 PhD continuation 條款）
與香港（MPhil 為 PhD 預備）構成三方對照。

## 4. 英國：Cambridge / Imperial 的 taught master's 與 PhD

### 4.1 Cambridge：逐課程的 PhD 銜接條款

【事實】Cambridge 各 MPhil 課程頁對「能否銜接 PhD」的條款**逐課程不同**，原文如下：

| 課程 | Study Mode | 原文關鍵句 |
|---|---|---|
| MPhil in Engineering | Research | 「Students wishing to apply for the PhD are expected to pass the MPhil programme.」 |
| MPhil in Advanced Chemical Engineering | Taught | 「This course **cannot be counted as one year of a PhD** research degree, although continuing students wishing to apply for a PhD are expected to obtain a good Pass for the MPhil ACE course.」 |
| MPhil in Electrical and Electronic Engineering | Taught | 「Students wishing to apply for continuation to the PhD would normally be expected to attain an overall mark of **70 percent**.」 |
| MPhil in Energy Technologies | Taught | 「Students wishing to apply for continuation to the PhD would normally be expected to attain an overall mark of **70 percent**.」 |
| MPhil in Chemical Engineering and Biotechnology | Research | 「the MPhil in Chemical Engineering and Biotechnology **does not "convert" to a PhD**. The course leads to a Master's degree only, and students wishing to pursue a PhD must reapply for admission as a PhD student.」 |

【事實】Advanced Chemical Engineering MPhil 原文另載：
「During the first two terms, students take a total of ten taught modules...
From March to August, students undertake a full-time research project, the results of which
are submitted as a dissertation.」——**即使被歸為 Taught，仍含 6 個月全職研究專題並以論文提交**。

【事實】Energy Technologies MPhil 原文目標含「to prepare students (if they so wish)
for potential future PhD research」，並稱「students who have taken the long dissertation option
will also be excellent candidates for doctoral study」。

【事實】Engineering MPhil 原文定位為「a one-year full-time (or two-year part-time) **course of research**,
introducing students to research skills and specialist knowledge」，其主要目的之一是
「to give students with relevant experience at a first-degree level the opportunity to carry out
focused research under close supervision」。

【事實】Cambridge PhD（Engineering）課程頁載明修業期為
**3-4 years full-time / 4-7 years part-time**。

【推論】Cambridge 的實務規則是：MPhil 頁的 Study Mode 標籤（Taught/Research）與
「可否銜接 PhD」是**兩個獨立維度**。被標為 Taught 的 Advanced Chemical Engineering MPhil
明文禁止計入 PhD 年限；被標為 Research 的 Chemical Engineering and Biotechnology MPhil
反而明文不轉銜。**名稱、標籤、銜接資格三者互不蘊含**，
這是本章最具反直覺也最實用的一項發現。

### 4.2 Imperial College London

【事實】Imperial 的 taught 課程頁（https://www.imperial.ac.uk/study/courses/postgraduate-taught/2027/advanced-mechanical-engineering/）
與 MEng 頁（https://www.imperial.ac.uk/study/courses/undergraduate/2027/mechanical-engineering/）
顯示 Imperial 同時提供授課型 MSc 與四年制整合 MEng。
【事實】Imperial 博士申請頁（https://www.imperial.ac.uk/study/apply/postgraduate-doctoral/application-process/choose-course/phd/）
說明 PhD 申請與 MPhil-to-PhD 銜接路徑。
**【本節缺口】** Imperial 的 MEng 學制年限與「是否為 integrated degree」的頁面原文
在本次會話中未能擷取到逐字條文，故上列僅列課程存在性，不列年限數字。

## 5. 研究型 vs 授課型的教學／研究比重對照

【事實】以 Cambridge 工程系逐課程比對：

| 類型 | 課時結構（官方原文） | 專題 | PhD 銜接 |
|---|---|---|---|
| Taught MPhil（Advanced Chemical Engineering） | 前兩學期十門 taught modules；3 月至 8 月全職研究專題 | 論文提交（dissertation） | 明文不可計入 PhD 年限 |
| Taught MPhil（EEE） | 以「current and emerging advanced subjects」＋ hands-on laboratory experience 為主 | 有研究成分 | 需 70% 成績 |
| Research MPhil（Engineering） | 「course of research」，close supervision | 有 | 需 pass |
| Research MPhil（Chemical Engineering and Biotechnology） | 「progress their research projects under academic supervision for one year」 | 「examined by thesis and oral examination」 | 明文不轉銜，須重新申請 |

【推論】授課型與研究型的差別在**導師監督的密度與專題時數**，而非「有無研究」——
被標為 Taught 的課程其實都含研究專題，但導師制度與年限定性不同。

## 6. 從碩士到博士、博士後與學術職業路徑

【事實】三地「碩士→博士」的銜接機制對照（均有前述一手依據）：

- **香港 HKU**：MPhil 規範 24 個月（FT）／36 個月（PT），試用期 12／12 個月（2025-09 後入讀）。
  三年制 PhD 36／54 個月，四年制 PhD 48／72 個月。
- **香港 HKUST**：MPhil 2 年；PhD 4 年，有相關研究型碩士者 3 年，非全日制 6 年。
- **英國 Cambridge**：PhD 3-4 年全職；MPhil 是否銜接**逐課程**裁定，含 70% 成績門檻、
  「good Pass」門檻、不可計入年限、須重新申請等四種不同條款。
- **美國 Stanford**：PhD 5-7 年；**不要求先取得 master's degree**；MS 45 units、無論文要求、為終端學位。

【推論】美國的直博（direct doctoral entry）與劍橋的逐課程裁定，
都指向同一結論：**「碩士是否通往博士」不是體系性質，而是逐課程、逐校決策**。

## 7. 認證與專業銜接（Engineering Council / Washington Accord）

### 7.1 CEng 與 IEng 的學位路徑

【事實】Engineering Council 的 Chartered Engineer (CEng) 頁
（https://www.engc.org.uk/professional-registration/our-professional-titles/chartered-engineer-ceng/）
原文：「...a Bachelor's degree, with Honours, in engineering or technology, **accredited for CEng**,
plus an appropriate and accredited Masters degree or Engineering Doctorate (EngD),
or appropriate further learning to Master's level...」

【事實】Engineering Council 的 Incorporated Engineer (IEng) 頁載明
「accredited Bachelors or honours degree in engineering or technology」途徑，
並容許 Integrated MEng 納入同一途徑。

【推論】Engineering Council 的制度設計是**以「受認證的學位」為單位**，
而非以學位名稱（MEng／MSc／BEng）為單位 ——
因此 HKU 明載的「HKIE has no policy for accreditation of MSc degrees in Hong Kong」
才會構成實質限制：香港的 MSc(Eng) 本身不帶來專業認可增益，
其價值須由「首個學位是否被認可」加上 project 選項來補償。

### 7.2 Washington Accord：香港學位國際互認的機制

【事實】Engineering Council 的 Washington Accord 頁
（https://www.engc.org.uk/international-recognition/international-accords/washington-accord/）
原文：
「recognises that professional engineering education programmes accredited by the signatories
deliver outcomes that are substantially equivalent to the Washington Accord Graduate Attributes
(learning outcomes)...」

【事實】同頁載明適用範圍：「In the case of the Engineering Council, this recognition applies
to programmes accredited at universities in England, Scotland, Wales and Northern Ireland」。

【事實】同頁另載衔接條款：已取得認可學士學位者，若再完成一門認可的 Masters level 課程
（例如認可為 further learning 的 MSc 或 EngD），該組合即受華盛頓公約承認。

【推論】華盛頓公約的互認建立在**「受認證的課程」＋「受認證的學士學位」的組合**上，
而非個別大學的國籍；這是理解香港學位在海外專業註冊市場中位置的核心機制，
也是 03a 章節「認證狀態須另查官方名錄」結論的延伸。

### 7.3 認證主體

【事實】Engineering Council 的 Higher Education Providers 頁
（https://www.engc.org.uk/education-and-skills/higher-education-programmes/higher-education-providers/）
載明高等教育機構須向 Engineering Council 申請 accredited status 方可開辦受認證課程。

【事實】HKU 明載 HKIE 對香港 MSc 學位「has no policy for accreditation」；
Engineering Council 的 Eur-ACE 頁
（https://www.engc.org.uk/international-recognition/recognition-in-europe/engineers-europe/）
為歐洲區域的對應安排。

## 8. 本章缺口彙總

1. **PolyU 完全受阻**：www.polyu.edu.hk 多次連線逾時，PolyU 工程研究生課程無一手資料。
2. **CUHK 逐課程條款未取得**：CUHK Graduate School 與 EE 系頁可達，但未擷取到
   MPhil/PhD 的時長對照原文。
3. **Imperial 的年限數字缺原文**：僅確認 taught MSc 與 MEng 兩類課程存在，
   未取得 MEng 學制年限、integrated 與否的逐字條款，亦未取得 Imperial 頁面上的 EPS 陳述。
4. **gradsch.hku.hk 404**：HKU 研究生院課程總表未取得。
5. **統計數字全缺**：三地的研究生註冊人數、師資比、獎學金金額皆無一手來源。
6. **HKU MSc(Eng) 專題選項的具體課程代號與學分**未取得（僅取得「建議 project 選項」的陳述）。
7. **Engineering Council 的 IEng 頁原文**未完整擷取（僅取得 CEng 頁完整原文與部分 IEng 句）。
8. **未取得 HKIE 正式認可學位名單**（engineers.org.hk）與 MIT ABET 認可名單的對照表。

## 9. 來源清單

| # | 機構 | 標題 | 發布日期／版本 | URL | 支撐的事實 |
|---|---|---|---|---|---|
| 1 | GOV.UK | What qualification levels mean — list of qualification levels | 未標示 | https://www.gov.uk/what-different-qualification-levels-mean/list-of-qualification-levels | Level 7 = integrated master's (MEng) 與 master's (MA/MSc)；Level 8 = doctorate (PhD/DPhil) |
| 2 | QAA | Characteristics statements | 未標示 | https://www.qaa.ac.uk/the-quality-code/characteristics-statements | 「Master's degrees sit at Levels 7 and 11, and doctoral qualifications at Levels 8 and 12.」 |
| 3 | Cambridge | Course Directory | 未標示（2026-10-22 擷取） | https://www.postgraduate.study.cam.ac.uk/courses/directory | Taught/Research 篩選（Research 169／Taught 188）、Course Level（Doctoral 117／Master's 221）、工程課程逐列標籤與長度 |
| 4 | Cambridge | MPhil in Advanced Chemical Engineering | 未標示 | https://www.postgraduate.study.cam.ac.uk/courses/directory/egcempace | 11 months FT、Study Mode Taught、十門 taught modules＋6 個月研究專題、「cannot be counted as one year of a PhD」 |
| 5 | Cambridge | MPhil in Engineering | 未標示 | https://www.postgraduate.study.cam.ac.uk/courses/directory/egegmpmeg | 12 months FT／24 months PT、Study Mode Research、「course of research」、PhD 需 pass |
| 6 | Cambridge | MPhil in Electrical and Electronic Engineering | 未標示 | https://www.postgraduate.study.cam.ac.uk/courses/directory/egegmpeee | 10 months FT、Study Mode Taught、PhD continuation 需 70 percent |
| 7 | Cambridge | MPhil in Energy Technologies | 未標示 | https://www.postgraduate.study.cam.ac.uk/courses/directory/egegmpmet | 11 months FT、Study Mode Taught、「prepare students for potential future PhD research」、70 percent 門檻 |
| 8 | Cambridge | MPhil in Chemical Engineering and Biotechnology | 未標示 | https://www.postgraduate.study.cam.ac.uk/courses/directory/egcempceb | 12 months FT／2 years PT、Study Mode Research、thesis and oral examination、「does not "convert" to a PhD」 |
| 9 | Cambridge | PhD in Engineering | 未標示 | https://www.postgraduate.study.cam.ac.uk/courses/directory/egegpdpeg | 3-4 years full-time / 4-7 years part-time |
| 10 | MIT | Master of Engineering (Course 6-P) degree chart | 未標示 | https://catalog.mit.edu/degree-charts/master-electrical-engineering-computer-science-course-6-p/ | MEng 須搭配 6-3/6-4/6-5；6.THM 24＋6.9830 1＋48＋18＝91 units |
| 11 | MIT | Electrical Engineering with Computing (SB, Course 6-5) degree chart | 未標示 | https://catalog.mit.edu/degree-charts/electrical-engineering-computer-science-course-6-5/ | 與 6-P 的對照（見 03a 章） |
| 12 | Stanford | EE — MS admissions | 未標示 | https://ee.stanford.edu/admissions/ms | MS 需 45 units of study、no thesis requirement、terminal degree |
| 13 | Stanford | EE — PhD admissions | 未標示 | https://ee.stanford.edu/admissions/phd | master's degree is not required；5-7 years |
| 14 | HKU | MPhil / PhD Programme Structure | 未標示 | https://engg.hku.hk/Admissions/PhD-MPhil/Programme-Structure | MPhil 24/36 個月、PhD 3 年 36/54、4 年 48/72、2025-09 後試用期變動 |
| 15 | HKU | MSc(Eng) Programme Structure and Duration | 未標示 | https://engg.hku.hk/Teaching-Learning/MSc/Programme-Structure-Duration | FT 1 年／max 2；PT 2 年／max 3 |
| 16 | HKU | MSc(Eng) Fees | 2026-27 入學 | https://engg.hku.hk/Teaching-Learning/MSc/Fees | 本地 HK$250,000／非本地 HK$375,000 |
| 17 | HKUST | SENG — MPhil / PhD Programs | 未標示 | https://seng.hkust.edu.hk/academics/research-postgraduate/mphil-phd-programs | MPhil 2 年、PhD 4 年（有相關碩士 3 年）、非全日制 6 年、thesis defense |
| 18 | CUHK | Graduate School — Engineering programme listing | 未標示 | https://www.gs.cuhk.edu.hk/programmes/engineering | 工程課程層級查詢入口（細節未取得） |
| 19 | Engineering Council | Chartered Engineer (CEng) | 未標示 | https://www.engc.org.uk/professional-registration/our-professional-titles/chartered-engineer-ceng/ | CEng 路徑：認可榮譽學士＋認可 Masters/EngD 或 further learning |
| 20 | Engineering Council | Incorporated Engineer (IEng) | 未標示 | https://www.engc.org.uk/professional-registration/our-professional-titles/incorporated-engineer-ieng/ | IEng 路徑：認可榮譽學士學位、Integrated MEng 納入同一途徑 |
| 21 | Engineering Council | Washington Accord | 未標示 | https://www.engc.org.uk/international-recognition/international-accords/washington-accord/ | 公約目的、適用英國四地範圍、Masters level 銜接條款 |
| 22 | Engineering Council | Higher Education Providers | 未標示 | https://www.engc.org.uk/education-and-skills/higher-education-programmes/higher-education-providers/ | 開辦受認證課程須申請 accredited status |
| 23 | Imperial College London | Advanced Mechanical Engineering (MSc, taught) | 2027 入學 | https://www.imperial.ac.uk/study/courses/postgraduate-taught/2027/advanced-mechanical-engineering/ | taught MSc 課程存在（年限未取得） |
| 24 | Imperial College London | Mechanical Engineering (MEng, undergraduate integrated) | 2027 入學 | https://www.imperial.ac.uk/study/courses/undergraduate/2027/mechanical-engineering/ | integrated MEng 課程存在（年限未取得） |
| 25 | Imperial College London | PhD application — choose course | 未標示 | https://www.imperial.ac.uk/study/apply/postgraduate-doctoral/application-process/choose-course/phd/ | PhD 與 MPhil-to-PhD 銜接路徑說明頁 |

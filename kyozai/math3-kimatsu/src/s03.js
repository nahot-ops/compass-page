// 中3 第3回（11/6）相似（相似条件・証明・平行線と線分の比）
const L = require("./lib");
const { writeBox, d, P, space, imgP, ansBox, qgrid, bandTitle, qHead, frame, SYS, runs, CW } = L;
const OUT = require("path").join(__dirname, "..");

const NAME = "　氏名　　　　　　　　　　";
const sec = (label, children) => ({ properties: L.sectionProps, headers: { default: L.header() }, footers: { default: L.footer(label) }, children });
const cell = (w, children, margins) => new d.TableCell({ borders: L.NOB, width: { size: w, type: d.WidthType.DXA }, margins, children });
const row2 = (w1, left, right, m1, m2) => new d.Table({
  width: { size: CW, type: d.WidthType.DXA }, columnWidths: [w1, CW - w1], borders: d.TableBorders.NONE,
  rows: [new d.TableRow({ children: [cell(w1, left, m1), cell(CW - w1, right, m2)] })],
});


// ============ 授業プリント ============
const kihon = [
  bandTitle("第3回　授業プリント①　＜基本＞", NAME + "得点　　　／50点"),
  P("目安10分。解き終わったら提出しましょう。答えに√がふくまれるときは、√の中をもっとも小さい整数にしましょう。", { before: 80, size: 20 }),

  qHead(1, "次の計算をしなさい。", "（2点×5）"),
  qgrid([
    { q: [P("（1）$√18+√32−√50$")], work: 650, ans: "", ansW: 2600 },
    { q: [P("（2）$√3(√12−√6)$")], work: 650, ans: "", ansW: 2600 },
    { q: [P("（3）${20/√5}−√45$")], work: 650, ans: "", ansW: 2600 },
    { q: [P("（4）$(√5+√3)(√5−√3)$")], work: 650, ans: "", ansW: 2600 },
    { q: [P("（5）$(x+3)^2−(x+2)(x−2)$")], work: 650, ans: "", ansW: 2600 },
  ], 3),

  qHead(2, "次の式を因数分解しなさい。", "（2点×4）"),
  qgrid([
    { q: [P("（1）$x^2+14x+49$")], work: 650, ans: "", ansW: 2600 },
    { q: [P("（2）$3x^2−27$")], work: 650, ans: "", ansW: 2600 },
    { q: [P("（3）$x^2−2x−48$")], work: 650, ans: "", ansW: 2600 },
    { q: [P("（4）$ab+4a−b−4$")], work: 650, ans: "", ansW: 2600 },
  ], 4),

  qHead(3, "次の二次方程式を解きなさい。", "（2点×4）"),
  qgrid([
    { q: [P("（1）$(x−4)^2=3$")], work: 650, ans: "$x$＝", ansW: 2600 },
    { q: [P("（2）$x^2+x−20=0$")], work: 650, ans: "$x$＝", ansW: 2600 },
    { q: [P("（3）$x^2−3x−1=0$")], work: 650, ans: "$x$＝", ansW: 2600 },
    { q: [P("（4）$(x+2)(x−3)=x+3$")], work: 650, ans: "$x$＝", ansW: 2600 },
  ], 4),

  qHead(4, "関数$y=ax^2$について、次の問いに答えなさい。", "（3点×4）"),
  qgrid([
    { q: [P("（1）関数$y=ax^2$のグラフが点$(2,−12)$を通るとき、$a$の値を求めなさい。")], work: 700, ans: "$a$＝", ansW: 2600 },
    { q: [P("（2）関数$y=2x^2$で、$x$の変域が$−3≦x≦1$のときの$y$の変域を求めなさい。")], work: 700, ans: "", ansW: 2600 },
    { q: [P("（3）関数$y=−x^2$で、$x$の値が1から4まで増加するときの変化の割合を求めなさい。")], work: 700, ans: "", ansW: 2600 },
    { q: [P("（4）関数$y=ax^2$で、$x$の値が$−4$から$−2$まで増加するときの変化の割合が12です。$a$の値を求めなさい。")], work: 700, ans: "$a$＝", ansW: 2600 },
  ], 4),

  qHead(5, "相似について、次の問いに答えなさい。", "（3点×4）"),
  row2(CW - 5200, [
    P("右の図で、△ABC∽△DEFで、相似比は4：5です。"),
    qgrid([
      { q: [P("（1）DEの長さを求めなさい。")], work: 900, ans: "　　　cm", ansW: 2400 },
      { q: [P("（2）BCの長さを求めなさい。")], work: 900, ans: "　　　cm", ansW: 2400 },
      { q: [P("（3）∠Cの大きさを求めなさい。")], work: 900, ans: "∠C＝　　　°", ansW: 2400 },
    ], 3, { width: CW - 5200 }),
  ], [imgP("s3b_k5.png", 360)]),
  P("（4）△GHIと△JKLで、∠G＝∠J＝40°、∠H＝∠K＝65°のとき、2つの三角形が相似であることを示す相似条件を書きなさい。", { before: 60 }),
  ansBox("", 5200),
];

const ouyo = [
  bandTitle("第3回　授業プリント②　＜応用＞", NAME + "得点　　　／50点"),
  P("大問ごとに時間を区切って解き、解説を聞きます。＜3＞は100点をねらう問題です。", { before: 80, size: 20 }),

  qHead(1, "直角三角形の相似", "目安7分　（17点）"),
  row2(CW - 4000, [
    P("右の図のように、∠BAC＝90°の直角三角形ABCがあり、頂点Aから辺BCに垂線ADをひきます。AB＝6cm、BC＝10cmです。"),
    P("（1）△ABC∽△DBAであることを証明しなさい。（10点）", { before: 80 }),
  ], [imgP("s3b_o1.png", 240)], { right: 200 }),
  writeBox(2000, null, 0),
  P("（2）BDの長さを求めなさい。（7点）", { before: 80 }),
  space(450), ansBox("　　　cm", 2600),

  qHead(2, "放物線と面積", "目安7分　（17点）"),
  row2(CW - 3600, [
    P("右の図のように、関数$y=x^2$のグラフ上に2点A、Bがあり、点Aの$x$座標は$−1$、点Bの$x$座標は3です。"),
    qgrid([
      { q: [P("（1）△OABの面積を求めなさい。（5点）")], work: 900, ans: "", ansW: 2400 },
      { q: [P("（2）関数$y=x^2$のグラフ上で、OとBの間に点Pをとります。△PABの面積が△OABの面積と等しくなるとき、点Pの座標を求めなさい。（6点）")], work: 900, ans: "P（　　，　　）", ansW: 2800 },
    ], 2, { width: CW - 3600 }),
  ], [imgP("s3b_o2.png", 210)], { right: 200 }),
  P("（3）$y$軸上に点Qをとります。△QABの面積が△OABの面積と等しくなるとき、点Qの座標を求めなさい。ただし、点Qは原点Oと異なる点とします。（6点）", { before: 60 }),
  space(400), ansBox("Q（　　，　　）", 2800),

  qHead(3, "★平行四辺形と相似", "目安8分　（16点）"),
  row2(CW - 4000, [
    P("右の図のように、平行四辺形ABCDの辺AD上に、AE：ED＝2：1となる点Eをとり、線分BEと対角線ACの交点をFとします。"),
    P("（1）△AEF∽△CBFであることを証明しなさい。（8点）", { before: 80 }),
  ], [imgP("s3b_o3.png", 240)], { right: 200 }),
  writeBox(1700, null, 0),
  qgrid([
    { q: [P("（2）AC＝15cmのとき、AFの長さを求めなさい。（4点）")], work: 400, ans: "　　　cm", ansW: 2600 },
    { q: [P("（3）BE＝10cmのとき、BFの長さを求めなさい。（4点）")], work: 400, ans: "　　　cm", ansW: 2600 },
  ], 2),
];

// ============ 採点用の解答 ============
function keyTable(rows) {
  const w = [1800, CW - 1800 - 1400, 1400];
  const c = (t, i, head) => new d.TableCell({ borders: L.BOX, width: { size: w[i], type: d.WidthType.DXA }, margins: { left: 100, right: 100, top: 30, bottom: 30 },
    shading: head ? { type: d.ShadingType.CLEAR, fill: "D9D9D9", color: "auto" } : undefined,
    children: [P(t, { after: 0, font: head ? L.GOT : undefined, bold: head, align: i === 2 ? d.AlignmentType.CENTER : undefined })] });
  return new d.Table({ width: { size: CW, type: d.WidthType.DXA }, columnWidths: w,
    rows: [["番号", "答え", "配点"], ...rows].map((r, k) => new d.TableRow({ cantSplit: true, children: r.map((t, i) => c(t, i, k === 0)) })) });
}
const key = [
  bandTitle("第3回　採点用の解答", "先生用"),
  qHead("授業プリント①", "基本（50点）"),
  keyTable([
    ["1（1）", "$2√2$", "2"], ["1（2）", "$6−3√2$", "2"], ["1（3）", "$√5$", "2"], ["1（4）", "2", "2"], ["1（5）", "$6x+13$", "2"],
    ["2（1）", "$(x+7)^2$", "2"], ["2（2）", "$3(x+3)(x−3)$", "2"], ["2（3）", "$(x−8)(x+6)$", "2"], ["2（4）", "$(a−1)(b+4)$", "2"],
    ["3（1）", "$x=4±√3$", "2"], ["3（2）", "$x=−5$、4", "2"], ["3（3）", "$x={3±√13/2}$", "2"], ["3（4）", "$x=1±√10$", "2"],
    ["4（1）", "$a=−3$", "3"], ["4（2）", "$0≦y≦18$", "3"], ["4（3）", "$−5$", "3"], ["4（4）", "$a=−2$", "3"],
    ["5（1）", "10cm", "3"], ["5（2）", "12cm", "3"], ["5（3）", "60°", "3"], ["5（4）", "2組の角がそれぞれ等しい", "3"],
  ]),
  qHead("授業プリント②", "応用（50点）"),
  keyTable([
    ["1（1）", "証明（記述。部分点は下の表）", "10"], ["1（2）", "${18/5}$cm（3.6cmも正解）", "7"],
    ["2（1）", "6", "5"], ["2（2）", "P(2, 4)", "6"], ["2（3）", "Q(0, 6)", "6"],
    ["★3（1）", "証明（記述。部分点は下の表）", "8"], ["★3（2）", "6cm", "4"], ["★3（3）", "6cm", "4"],
  ]),
]

// 記述問題の部分点の表
function critTable(title, rows) {
  const w = [600, 3400, CW - 600 - 3400 - 1000, 1000];
  const c = (t, i, head) => new d.TableCell({ borders: L.BOX, width: { size: w[i], type: d.WidthType.DXA }, margins: { left: 80, right: 80, top: 20, bottom: 20 },
    shading: head ? { type: d.ShadingType.CLEAR, fill: "D9D9D9", color: "auto" } : undefined,
    children: [P(t, { after: 0, size: 20, font: head ? L.GOT : undefined, bold: head, align: (i === 0 || i === 3) ? d.AlignmentType.CENTER : undefined })] });
  return [P(title, { before: 120, after: 40, font: L.GOT, bold: true, size: 22, keepNext: true }),
    new d.Table({ width: { size: CW, type: d.WidthType.DXA }, columnWidths: w,
      rows: [["", "見るところ", "書いてあればよい式・ことば", "点"], ...rows].map((r, k) => new d.TableRow({ cantSplit: true, children: r.map((t, i) => c(t, i, k === 0)) })) })];
}
const crit = [
  new d.Paragraph({ children: [new d.PageBreak()] }),
  qHead("記述問題の部分点", "応用プリント"),
  P("・根拠（仮定より、共通な角だから、錯角は等しいから　など）がない式は、その式の点をあげない。　・相似条件のことばが正しくないときは、その段階の点をあげない。", { size: 20 }),
  ...critTable("＜1＞（1）　10点", [
    ["①", "比べる三角形を書く", "△ABCと△DBAで、", "1"],
    ["②", "直角の角", "仮定より、∠BAC＝∠BDA＝90°……①", "3"],
    ["③", "共通な角", "共通な角だから、∠ABC＝∠DBA……②", "3"],
    ["④", "相似条件", "①、②より、2組の角がそれぞれ等しいので", "2"],
    ["⑤", "結論", "△ABC∽△DBA（頂点の順番がちがうものは×）", "1"],
  ]),
  ...critTable("★＜3＞（1）　8点", [
    ["①", "比べる三角形を書く", "△AEFと△CBFで、", "1"],
    ["②", "錯角（平行線）", "AD//BCより、錯角は等しいから、∠EAF＝∠BCF……①（∠AEF＝∠CBFでも○）", "3"],
    ["③", "対頂角（または2つ目の錯角）", "対頂角は等しいから、∠AFE＝∠CFB……②", "2"],
    ["④", "相似条件と結論", "①、②より、2組の角がそれぞれ等しいので、△AEF∽△CBF", "2"],
  ]),
];

// ============ 宿題（翌日にも授業があるので少なめ） ============
const hw = [
  bandTitle("第3回　宿題", NAME + "提出日　　／　　"),
  P("11/7（土）までに解答解説で丸つけをして、直しノートを作りましょう。今日の復習の問題です。", { before: 80, size: 20 }),
  qHead(1, "相似の証明（穴うめ）"),
  row2(CW - 3400, [
    P("右の図のように、△ABCの辺AB上に点D、辺AC上に点Eがあり、∠ADE＝∠ACBです。△ADE∽△ACBであることを、次のように証明しました。ア〜エにあてはまることばや記号を書きなさい。"),
    frame("", [
      P("【証明】△ADEと△ACBで、"),
      P("仮定より、∠ADE＝∠（　ア　）……①"),
      P("（　イ　）な角だから、∠DAE＝∠（　ウ　）……②"),
      P("①、②より、（　エ　）がそれぞれ等しいので、△ADE∽△ACB", { after: 0 }),
    ]),
  ], [imgP("h3_anti.png", 190)], { right: 200 }),
  qgrid([
    { q: [P("ア")], work: 0, ans: "", ansW: 2600 }, { q: [P("イ")], work: 0, ans: "", ansW: 2600 },
    { q: [P("ウ")], work: 0, ans: "", ansW: 2600 }, { q: [P("エ")], work: 0, ans: "", ansW: 3000 },
  ], 4),
  qHead(2, "相似な三角形の辺の長さ"),
  P("＜1＞の図で、AD＝4cm、AE＝5cm、AB＝10cm、DE＝6cmです。"),
  qgrid([
    { q: [P("（1）ACの長さを求めなさい。")], work: 300, ans: "　　　cm", ansW: 2600 },
    { q: [P("（2）BCの長さを求めなさい。")], work: 900, ans: "　　　cm", ansW: 2600 },
  ], 2),
  qHead(3, "解から係数を求める（今日まちがいが多かった型）"),
  qgrid([
    { q: [P("（1）二次方程式$x^2+ax+b=0$の解が3と$−4$のとき、$a$、$b$の値を求めなさい。")], work: 500, ans: "$a$＝　　，$b$＝", ansW: 3200 },
    { q: [P("★（2）二次方程式$x^2+ax+3a=0$の解の1つが$−2$のとき、$a$の値ともう1つの解を求めなさい。")], work: 500, ans: "$a$＝　　，もう1つの解", ansW: 4000 },
  ], 2),
  qHead(4, "相似の証明（記述）"),
  row2(CW - 3400, [
    P("右の図のように、△ABCの辺AB上に点D、辺AC上に点Eがあり、AD＝4cm、AB＝12cm、AE＝6cm、AC＝8cmです。"),
    P("（1）△ADE∽△ACBであることを証明しなさい。", { before: 60 }),
  ], [imgP("h3_sas.png", 160)], { right: 200 }),
  writeBox(1400, null, 0),
  row2(CW - 3000, [P("（2）DE＝5cmのとき、BCの長さを求めなさい。", { before: 60 }), space(300)], [space(120), ansBox("　　　cm", 2600)]),
  qHead(5, "★直角三角形の中の相似"),
  row2(CW - 3800, [
    P("右の図のように、∠ACB＝90°の直角三角形ABCがあり、頂点Cから辺ABに垂線CHをひきます。AC＝6cm、AB＝9cmです。"),
    qgrid([
      { q: [P("（1）△ABCと相似な三角形を、2つ答えなさい。")], work: 200, ans: "", ansW: 3200 },
      { q: [P("（2）AHの長さを求めなさい。")], work: 500, ans: "　　　cm", ansW: 2600 },
    ], 2, { width: CW - 3800 }),
  ], [imgP("h3b_rt.png", 210)], { right: 200 }),
  qHead(6, "計算の復習"),
  qgrid([
    { q: [P("（1）$x^2−11x+24$を因数分解")], work: 500, ans: "", ansW: 2600 },
    { q: [P("（2）$4x^2−25$を因数分解")], work: 500, ans: "", ansW: 2600 },
    { q: [P("（3）$x^2−8x+9=0$")], work: 500, ans: "$x$＝", ansW: 2600 },
    { q: [P("（4）$(x−3)^2=2(x−3)$")], work: 500, ans: "$x$＝", ansW: 2600 },
  ], 4),
];

// ============ 宿題の解答解説 ============
const A = (no, ans, steps, o = {}) => [
  P(`${no}　**答え　${ans}**`, { before: 80, after: 20, keepNext: true, size: 28, mathSize: 28 }),
  ...steps.map(s => typeof s === "string" ? P(s, { indent: 500, after: 10, size: 24, mathSize: 28, keepNext: o.keepNext }) : s),
];
const AT = (no, ans, steps) => [
  P(`${no}　**答え　${ans}**`, { before: 80, after: 20, size: 28, mathSize: 28 }),
  ...steps.map(s => typeof s === "string" ? P(s, { indent: 500, after: 10, size: 24, mathSize: 28 }) : s),
];
const KH = { s1: 32, s2: 28 };
const sysLine = (lead, rows, tags, o = {}) => new d.Paragraph({ children: [...runs(lead, { size: 24 }), SYS(rows, tags)], indent: { left: o.indent || 500 }, spacing: { before: 20, after: 40 } });
const T = (t, o = {}) => P(t, { size: 24, mathSize: 28, ...o });
const kai = [
  bandTitle("第3回　宿題　解答解説", ""),
  P("**〇かどうかわからない場合は、適当に〇をつけずに必ず先生に確認しましょう**", { before: 120, after: 120, size: 24 }),
  qHead(1, "相似の証明（穴うめ）", "", KH),
  ...A("", "ア　ACB　　イ　共通　　ウ　CAB　　エ　2組の角", []),
  frame("証明の書き方のポイント", [
    T("・はじめに「△〇〇と△〇〇で、」と、比べる三角形を書く。"),
    T("・等しい角や辺には、必ず理由（仮定より、共通な角だから、対頂角は等しいから　など）を書く。"),
    T("・最後に相似条件を書いてから、「△ADE∽△ACB」と結論を書く。頂点は対応する順に書く。", { after: 0 }),
  ]),
  T("∠DAEと∠CABは、どちらも頂点Aの角で、同じ角（共通な角）。∠BACと書いても正解。", { before: 60 }),
  qHead(2, "相似な三角形の辺の長さ", "", KH),
  T("＜1＞で、△ADE∽△ACBを証明した。対応する辺は、ADとAC、AEとAB、DEとCB。"),
  ...A("（1）", "8cm", ["AE：AB＝5：10＝1：2なので、相似比は1：2。", "AD：AC＝1：2。4：AC＝1：2 → AC＝8"]),
  ...A("（2）", "12cm", ["DE：CB＝1：2。6：BC＝1：2 → BC＝12", "AD：ABではないことに注意。対応する辺は、相似の記号「∽」の順に頂点を読むとわかる。"]),
  qHead(3, "解から係数を求める", "", KH),
  ...A("（1）", "$a=1$、$b=−12$", ["【解を代入する】$x=3$を代入して$9+3a+b=0$……①、$x=−4$を代入して$16−4a+b=0$……②。", sysLine("", ["3a+b=−9", "−4a+b=−16"], ["①", "②"]), "①−②：$7a=7$、$a=1$。①に代入して$b=−12$。",
    "【因数分解の形から考える】解が3と$−4$の二次方程式は$(x−3)(x+4)=0$。展開すると$x^2+x−12=0$。$x^2+ax+b=0$とくらべて$a=1$、$b=−12$。"]),
  ...A("★（2）", "$a=−4$、もう1つの解は6", ["$x=−2$を代入する。$4−2a+3a=0$ → $a=−4$。", "もとの方程式は$x^2−4x−12=0$ → $(x−6)(x+2)=0$ → $x=6$、$−2$。もう1つの解は6。"]),
  new d.Paragraph({ children: [new d.PageBreak()] }),
  qHead(4, "相似の証明（記述）", "", KH),
  ...A("（1）", "下の証明", []),
  frame("【証明】", [
    T("△ADEと△ACBで、"),
    T("仮定より、AD：AC＝4：8＝1：2……①"),
    T("　　　　　AE：AB＝6：12＝1：2……②"),
    T("共通な角だから、∠DAE＝∠CAB……③"),
    T("①、②、③より、2組の辺の比とその間の角がそれぞれ等しいので、△ADE∽△ACB", { after: 0 }),
  ]),
  T("ADとAC、AEとABが対応する。AD：ABではないことに注意。頂点は対応する順（A→A、D→C、E→B）に書く。", { before: 60 }),
  ...A("（2）", "10cm", ["（1）より相似比は1：2なので、DE：CB＝1：2。5：BC＝1：2 → BC＝10"]),
  qHead(5, "★直角三角形の中の相似", "", KH),
  ...A("（1）", "△ACH、△CBH", ["△ABCと△ACHで、∠ACB＝∠AHC＝90°、∠Aは共通。2組の角がそれぞれ等しいので△ABC∽△ACH。", "△ABCと△CBHで、∠ACB＝∠CHB＝90°、∠Bは共通。同じように△ABC∽△CBH。", "直角三角形の直角の頂点から垂線をひくと、相似な三角形が3つできる。"]),
  ...A("（2）", "4cm", ["△ABC∽△ACHより、AB：AC＝AC：AH。9：6＝6：AH → $9×AH=36$ → AH＝4"]),
  qHead(6, "計算の復習", "", KH),
  ...A("（1）", "$(x−3)(x−8)$", ["かけて24、たして$−11$になる2数は$−3$と$−8$。"]),
  ...A("（2）", "$(2x+5)(2x−5)$", ["$(2x)^2−5^2$なので、$a^2−b^2=(a+b)(a−b)$の形。"]),
  ...A("（3）", "$x=4±√7$", ["解の公式で$x={8±√(64−36)/2}={8±2√7/2}=4±√7$"]),
  ...A("（4）", "$x=3$、5", ["$x−3$を$A$とおくと$A^2=2A$ → $A(A−2)=0$ → $A=0$、2。$x−3=0$、2より$x=3$、5。", "両辺を$x−3$でわると、$x=3$の解が消えてしまうので、わってはいけない。"]),
];

// ============ 書き出し ============
Promise.all([
  L.save(`${OUT}/第3回_授業プリント.docx`, [sec("中3 第3回 授業プリント", kihon), sec("中3 第3回 授業プリント", ouyo)]),
  L.save(`${OUT}/第3回_採点用解答.docx`, [sec("中3 第3回 採点用の解答", [...key, ...crit])]),
  L.save(`${OUT}/第3回_宿題.docx`, [sec("中3 第3回 宿題", hw)]),
  L.save(`${OUT}/第3回_宿題_解答解説.docx`, [sec("中3 第3回 宿題 解答解説", kai)]),
]).then(() => console.log("ok"));

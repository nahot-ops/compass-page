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
  new d.Table({
    width: { size: CW, type: d.WidthType.DXA }, columnWidths: [3300, 3300, 3300, CW - 9900], borders: d.TableBorders.NONE,
    rows: [new d.TableRow({ cantSplit: true, children: [
      cell(3300, [P("（1）下の図で、DE//BCです。$x$の値を求めなさい。"), imgP("s3_k5a.png", 175, d.AlignmentType.LEFT), ansBox("$x$＝", 2600)], { right: 120 }),
      cell(3300, [P("（2）△ABCで、辺AB、ACの中点をそれぞれM、Nとします。BC＝14cmのとき、MNの長さを求めなさい。"), space(1300), ansBox("　　　cm", 2600)], { right: 120 }),
      cell(3300, [P("（3）下の図で、ℓ//$m$//$n$です。$x$の値を求めなさい。"), imgP("s3_k5c.png", 185, d.AlignmentType.LEFT), ansBox("$x$＝", 2600)], { right: 120 }),
      cell(CW - 9900, [P("（4）△ABC∽△DEFで、∠A＝50°、∠E＝70°のとき、∠Cの大きさを求めなさい。"), space(1300), ansBox("∠C＝　　　°", 2600)]),
    ] })],
  }),
];

const ouyo = [
  bandTitle("第3回　授業プリント②　＜応用＞", NAME + "得点　　　／50点"),
  P("大問ごとに時間を区切って解き、解説を聞きます。＜3＞は100点をねらう問題です。", { before: 80, size: 20 }),

  qHead(1, "相似の証明", "目安7分　（17点）"),
  row2(CW - 3600, [
    P("右の図のように、△ABCの辺AC上に点Dがあり、∠ABD＝∠ACBです。"),
    P("（1）△ABD∽△ACBであることを証明しなさい。（10点）", { before: 80 }),
  ], [imgP("s3_o1.png", 230)], { right: 200 }),
  writeBox(2700, null, 0),
  P("（2）AB＝6cm、AC＝9cmのとき、ADの長さを求めなさい。（7点）", { before: 80 }),
  space(1100), ansBox("　　　cm", 2600),

  qHead(2, "台形と平行線", "目安6分　（17点）"),
  row2(CW - 4000, [
    P("右の図のように、AD//BCの台形ABCDがあり、AD＝4cm、BC＝6cmです。対角線ACとBDの交点をOとし、Oを通りBCに平行な直線と辺AB、DCとの交点をそれぞれE、Fとします。"),
    qgrid([
      { q: [P("（1）AO：OCを、もっとも簡単な整数の比で表しなさい。（5点）")], work: 1100, ans: "　　：", ansW: 2400 },
      { q: [P("（2）EOの長さを求めなさい。（6点）")], work: 1100, ans: "　　　cm", ansW: 2400 },
      { q: [P("（3）EFの長さを求めなさい。（6点）")], work: 1100, ans: "　　　cm", ansW: 2400 },
    ], 3, { width: CW - 4000 }),
  ], [imgP("s3_o2.png", 240)], { right: 200 }),

  qHead(3, "★平行四辺形と相似", "目安8分　（16点）"),
  row2(CW - 4600, [
    P("右の図のように、平行四辺形ABCDがあり、AB＝9cm、対角線AC＝15cmです。辺AD上に点EをAE：ED＝2：1となるようにとり、線分BEと対角線ACの交点をFとします。また、BEの延長と辺CDの延長との交点をGとします。"),
    qgrid([
      { q: [P("（1）AF：FCを、もっとも簡単な整数の比で表しなさい。（5点）")], work: 1200, ans: "　　：", ansW: 2400 },
      { q: [P("（2）AFの長さを求めなさい。（5点）")], work: 1200, ans: "　　　cm", ansW: 2400 },
      { q: [P("（3）DGの長さを求めなさい。（6点）")], work: 1200, ans: "　　　cm", ansW: 2400 },
    ], 3, { width: CW - 4600 }),
  ], [imgP("s3_o3.png", 280)], { right: 200 }),
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
    ["5（1）", "$x=2$", "3"], ["5（2）", "7cm", "3"], ["5（3）", "$x=9$", "3"], ["5（4）", "60°", "3"],
  ]),
  qHead("授業プリント②", "応用（50点）"),
  keyTable([
    ["1（1）", "証明（記述。部分点は下の表）", "10"], ["1（2）", "4cm", "7"],
    ["2（1）", "2：3", "5"], ["2（2）", "${12/5}$cm", "6"], ["2（3）", "${24/5}$cm", "6"],
    ["★3（1）", "2：3", "5"], ["★3（2）", "6cm", "5"], ["★3（3）", "${9/2}$cm", "6"],
  ]),
];

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
  P("・根拠（仮定より、共通な角だから　など）がない式は、その式の点をあげない。　・相似条件のことばが正しくないときは、③の点をあげない。", { size: 20 }),
  ...critTable("＜1＞（1）　10点", [
    ["①", "比べる三角形を書く", "△ABDと△ACBで、", "1"],
    ["②", "仮定から等しい角", "仮定より、∠ABD＝∠ACB……①", "3"],
    ["③", "共通な角", "共通な角だから、∠BAD＝∠CAB……②", "3"],
    ["④", "相似条件", "①、②より、2組の角がそれぞれ等しいので", "2"],
    ["⑤", "結論", "△ABD∽△ACB（頂点の順番がちがうものは×）", "1"],
  ]),
];

// ============ 宿題（翌日にも授業があるので少なめ） ============
const hw = [
  bandTitle("第3回　宿題", NAME + "提出日　　／　　"),
  P("11/7（土）までに解答解説で丸つけをして、直しノートを作りましょう。明日も授業があるので、今日の復習だけです。", { before: 80, size: 20 }),
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
  qHead(2, "平行線と線分の比"),
  row2(CW - 3800, [
    P("右の図で、DE//BCです。$x$、$y$の値を求めなさい。"),
    qgrid([
      { q: [P("（1）$x$の値")], work: 900, ans: "$x$＝", ansW: 2600 },
      { q: [P("（2）$y$の値")], work: 900, ans: "$y$＝", ansW: 2600 },
    ], 2, { width: CW - 3800 }),
  ], [imgP("h3_par.png", 220)]),
  qHead(3, "★中点連結定理"),
  P("四角形ABCDの辺AB、BC、CD、DAの中点を、それぞれP、Q、R、Sとします。対角線AC＝10cm、BD＝8cmのとき、四角形PQRSの周の長さを求めなさい。"),
  space(900), ansBox("　　　cm", 2600),
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
  qHead(2, "平行線と線分の比", "", KH),
  row2(CW - 4400, [
    ...AT("（1）", "$x={5/2}$", ["【比の式で解く】DE//BCなので、AD：DB＝AE：EC。4：2＝5：$x$ → $4x=10$ → $x={5/2}$", "【図で何倍か考える】AD：DB＝②：①なので、AE：EC＝□2：□1。□2が5cmなので、□1はその半分で${5/2}$。"]),
    ...AT("（2）", "$y=9$", ["【比の式で解く】DE：BC＝AD：AB。AB＝4＋2＝6なので、6：$y$＝4：6 → $4y=36$ → $y=9$", "【図で何倍か考える】AD：AB＝②：③なので、DE：BC＝△2：△3。△2が6cmなので3倍。$y=3×3=9$", "DE：BCを求めるときは、AD：DB（②：①）ではなく、AD：AB（②：③）を使う。"]),
  ], [imgP("h3_par_ans.png", 270)], { right: 200 }),
  qHead(3, "★中点連結定理", "", KH),
  ...A("", "18cm", ["△ABCで、P、Qは辺AB、BCの中点なので、中点連結定理より、PQ＝${1/2}$AC＝5cm。", "同じように、△ACDでSR＝${1/2}$AC＝5cm、△ABDでPS＝${1/2}$BD＝4cm、△BCDでQR＝${1/2}$BD＝4cm。", "周の長さは$5+5+4+4=18$（cm）。"]),
];

// ============ 書き出し ============
Promise.all([
  L.save(`${OUT}/第3回_授業プリント.docx`, [sec("中3 第3回 授業プリント", kihon), sec("中3 第3回 授業プリント", ouyo)]),
  L.save(`${OUT}/第3回_採点用解答.docx`, [sec("中3 第3回 採点用の解答", [...key, ...crit])]),
  L.save(`${OUT}/第3回_宿題.docx`, [sec("中3 第3回 宿題", hw)]),
  L.save(`${OUT}/第3回_宿題_解答解説.docx`, [sec("中3 第3回 宿題 解答解説", kai)]),
]).then(() => console.log("ok"));

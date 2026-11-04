// 中3 第3回　発展プリント（授業中に早く終わった人用）
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

// ============ 発展プリント（授業中に早く終わった人用） ============
const hatten = [
  bandTitle("第3回　発展プリント　＜100点をめざす＞", NAME),
  P("授業プリントが終わって、直しもすんだ人が取り組みます。解き終わったら解答解説で丸つけをして、直しノートを作りましょう。", { before: 80, size: 20 }),
  qHead(1, "放物線と回転体"),
  row2(CW - 3600, [
    P("右の図のように、関数$y=x^2$のグラフ上に2点A、Bがあり、点Aの$x$座標は$−1$、点Bの$x$座標は2です。直線ABと$x$軸との交点をCとします。"),
    qgrid([
      { q: [P("（1）直線ABの式を求めなさい。")], work: 700, ans: "$y$＝", ansW: 2600 },
      { q: [P("（2）△OBCの面積を求めなさい。")], work: 700, ans: "", ansW: 2400 },
    ], 2, { width: CW - 3600 }),
    P("（3）△OBCを、$x$軸を軸として1回転させてできる立体の体積を求めなさい。ただし、円周率は$π$とします。", { before: 60 }),
    space(900), ansBox("", 2800),
  ], [imgP("s3c_1.png", 210)], { right: 200 }),
  qHead(2, "動く点と二次方程式"),
  row2(CW - 3800, [
    P("右の図のような長方形ABCDで、点PはBを出発して、辺BC上をCまで毎秒2cmの速さで動きます。点QはPと同時にCを出発して、辺CD上をDに向かって毎秒1cmの速さで動きます。出発してから$x$秒後の△PCQの面積を$y$cm²とします。ただし、$0<x<6$とします。"),
    qgrid([
      { q: [P("（1）$x=1$のときの$y$の値")], work: 500, ans: "", ansW: 2400 },
      { q: [P("（2）$y$を$x$の式で表しなさい。")], work: 500, ans: "$y$＝", ansW: 2800 },
    ], 2, { width: CW - 3800 }),
  ], [imgP("s3c_2.png", 230)], { right: 200 }),
  P("（3）△PCQの面積が8cm²になるのは、出発してから何秒後ですか。すべて求めなさい。答えを求める過程も書くこと。", { before: 60 }),
  writeBox(1500, "　　秒後と　　秒後", 3600),
  qHead(3, "★正三角形の中の相似"),
  row2(CW - 3400, [
    P("右の図のように、正三角形ABCの辺BC上に点Dをとり、辺AC上に∠ADE＝60°となる点Eをとります。"),
    P("（1）△ABD∽△DCEであることを証明しなさい。", { before: 60 }),
  ], [imgP("s3c_3.png", 180)], { right: 200 }),
  writeBox(2300, null, 0),
  row2(CW - 3000, [P("（2）AB＝9cm、BD＝3cmのとき、CEの長さを求めなさい。", { before: 60 }), space(500)], [space(150), ansBox("　　　cm", 2600)]),
];

const hattenKai = [
  bandTitle("第3回　発展プリント　解答解説", ""),
  P("**〇かどうかわからない場合は、適当に〇をつけずに必ず先生に確認しましょう**", { before: 120, after: 120, size: 24 }),
  qHead(1, "放物線と回転体", "", KH),
  row2(CW - 4200, [
    ...AT("（1）", "$y=x+2$", ["A$(−1,1)$、B(2, 4)。傾き＝${4−1/2−(−1)}=1$。$y=x+b$にB(2, 4)を代入して$b=2$。"]),
    ...AT("（2）", "4", ["$y=0$を代入して、C$(−2,0)$。底辺OC＝2、高さはBの$y$座標で4。$2×4÷2=4$"]),
    ...AT("（3）", "${32/3}π$", ["Bから$x$軸に垂線BHをひく（H(2, 0)）。回転させると、△CBHでできる円錐から、△OBHでできる円錐を取りのぞいた立体になる（図の破線）。",
      "△CBHの円錐：底面の半径4、高さCH＝4。${1/3}×π×4^2×4={64/3}π$", "△OBHの円錐：底面の半径4、高さOH＝2。${1/3}×π×4^2×2={32/3}π$", "${64/3}π−{32/3}π={32/3}π$"]),
  ], [imgP("s3c_1_ans.png", 260)], { right: 200 }),
  qHead(2, "動く点と二次方程式", "", KH),
  ...A("（1）", "5", ["1秒後、BP＝2cmなので PC＝12−2＝10cm、CQ＝1cm。$10×1÷2=5$"]),
  ...A("（2）", "$y=−x^2+6x$", ["$x$秒後、PC＝$(12−2x)$cm、CQ＝$x$cm。$y=(12−2x)×x÷2=x(6−x)=−x^2+6x$"]),
  ...A("（3）", "2秒後と4秒後", ["$−x^2+6x=8$ → $x^2−6x+8=0$ → $(x−2)(x−4)=0$ → $x=2$、4", "【解の検討】$0<x<6$なので、どちらも問題にあっている。（Qは4秒後でCから4cmで、CD＝8cmより短いのでOK）", "【確かめ】2秒後は$8×2÷2=8$、4秒後は$4×4÷2=8$で、どちらも8cm²。"]),
  qHead(3, "★正三角形の中の相似", "", KH),
  row2(CW - 3600, [
    ...AT("（1）", "下の証明", []),
    frame("【証明】", [
      T("△ABDと△DCEで、"),
      T("正三角形の角なので、∠ABD＝∠DCE＝60°……①"),
      T("∠ADCは△ABDの外角なので、∠ADC＝∠ABD＋∠BAD＝60°＋∠BAD"),
      T("また、∠ADC＝∠ADE＋∠EDC＝60°＋∠EDC"),
      T("よって、∠BAD＝∠CDE……②"),
      T("①、②より、2組の角がそれぞれ等しいので、△ABD∽△DCE", { after: 0 }),
    ]),
  ], [imgP("s3c_3_ans.png", 200)], { right: 200 }),
  T("∠BADと∠CDEが等しいことを示すのがポイント。どちらも「60°をたすと∠ADCになる」角になっている。", { before: 60 }),
  ...A("（2）", "2cm", ["DC＝9−3＝6cm。△ABD∽△DCEより、AB：DC＝BD：CE。", "9：6＝3：CE → $9×CE=18$ → CE＝2"]),
];

Promise.all([
  L.save(`${OUT}/第3回_発展プリント.docx`, [sec("中3 第3回 発展プリント", hatten)]),
  L.save(`${OUT}/第3回_発展プリント_解答解説.docx`, [sec("中3 第3回 発展プリント 解答解説", hattenKai)]),
]).then(() => console.log("ok"));

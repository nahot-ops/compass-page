// 第2回（11/4）一次関数の後半だけ（ダイヤグラム・動点・利用）
const L = require("./lib");
const { d, P, space, imgP, ansBox, qgrid, bandTitle, qHead, frame, runs, CW } = L;
const OUT = require("path").join(__dirname, "..");

const NAME = "2年　　組　　番　氏名　　　　　　　　　　";
const sec = (label, children) => ({ properties: L.sectionProps, headers: { default: L.header() }, footers: { default: L.footer(label) }, children });
const cell = (w, children, margins) => new d.TableCell({ borders: L.NOB, width: { size: w, type: d.WidthType.DXA }, margins, children });
const row2 = (w1, left, right, m1, m2) => new d.Table({
  width: { size: CW, type: d.WidthType.DXA }, columnWidths: [w1, CW - w1], borders: d.TableBorders.NONE,
  rows: [new d.TableRow({ children: [cell(w1, left, m1), cell(CW - w1, right, m2)] })],
});
// 罫線つきの表（ばねの表など）
const grid = (rows, widths, o = {}) => new d.Table({
  width: { size: widths.reduce((a, b) => a + b), type: d.WidthType.DXA }, columnWidths: widths, indent: o.indent ? { size: o.indent, type: d.WidthType.DXA } : undefined,
  rows: rows.map((r, k) => new d.TableRow({ children: r.map((t, i) => new d.TableCell({
    borders: L.BOX, width: { size: widths[i], type: d.WidthType.DXA }, margins: { left: 60, right: 60 },
    shading: (i === 0 && o.headCol) ? { type: d.ShadingType.CLEAR, fill: "E7E6E6", color: "auto" } : undefined,
    children: [P(t, { after: 0, align: d.AlignmentType.CENTER, keepNext: true })] })) })),
});

// ============ 授業プリント ============
const kihon = [
  bandTitle("第2回　授業プリント①　＜基本＞", NAME + "得点　　　／50点"),
  P("目安10分。解き終わったら提出しましょう。答えは最も簡単な形で書きましょう。", { before: 80, size: 20 }),

  qHead(1, "ばねの長さ", "（4点×3）"),
  P("長さ10cmのばねがあります。このばねは、おもりの重さ1gにつき0.5cmずつのびます。$x$gのおもりをつるしたときの、ばねの長さを$y$cmとします。"),
  qgrid([
    { q: [P("（1）$y$を$x$の式で表しなさい。")], work: 500, ans: "$y$＝", ansW: 3200 },
    { q: [P("（2）12gのおもりをつるしたときの、ばねの長さを求めなさい。")], work: 500, ans: "　　　　cm", ansW: 2600 },
    { q: [P("（3）ばねの長さが25cmになるのは、何gのおもりをつるしたときですか。")], work: 500, ans: "　　　　g", ansW: 2600 },
  ], 3),

  qHead(2, "ダイヤグラム", "（3点×2、4点×2）"),
  row2(CW - 4500, [
    P("Aさんは9時に家を出発し、途中で休んでから駅に向かいました。右の図は、Aさんが家を出発してから$x$分後の、家からの道のりを$y$mとして、$x$と$y$の関係を表したグラフです。"),
    qgrid([
      { q: [P("（1）家を出発してから最初の10分間の速さは、分速何mですか。")], work: 300, ans: "分速　　　　m", ansW: 2700 },
      { q: [P("（2）Aさんが止まっていたのは何分間ですか。")], work: 300, ans: "　　　　分間", ansW: 2700 },
      { q: [P("（3）$20≦x≦30$のとき、$y$を$x$の式で表しなさい。")], work: 700, ans: "$y$＝", ansW: 2900 },
      { q: [P("（4）Aさんが家から1400mの地点を通ったのは、9時何分ですか。")], work: 700, ans: "9時　　　　分", ansW: 2700 },
    ], 2, { width: CW - 4500 }),
  ], [imgP("j2b_dia.png", 255)]),

  qHead(3, "動く点と面積", "（4点×3）"),
  row2(CW - 3300, [
    P("右の図のような長方形ABCDで、点PはBを出発して、辺BC上をCまで毎秒1cmの速さで動きます。点PがBを出発してから$x$秒後の△ABPの面積を$y$cm²とします。"),
    qgrid([
      { q: [P("（1）$x=4$のときの$y$の値")], work: 800, ans: "", ansW: 2400 },
      { q: [P("（2）$y$を$x$の式で表しなさい。")], work: 800, ans: "$y$＝", ansW: 2600 },
      { q: [P("（3）$y$の変域を求めなさい。")], work: 800, ans: "", ansW: 2600 },
    ], 3, { width: CW - 3300 }),
  ], [imgP("j2b_rect.png", 175)]),

  qHead(4, "2直線$y=x+2$と$y=−x+6$について、次の問いに答えなさい。", "（6点×2）"),
  qgrid([
    { q: [P("（1）2直線の交点の座標を求めなさい。")], work: 1600, ans: "（　　　，　　　）", ansW: 3200 },
    { q: [P("（2）2直線と$x$軸で囲まれた三角形の面積を求めなさい。")], work: 1600, ans: "", ansW: 2600 },
  ], 2),
];

const ouyo = [
  bandTitle("第2回　授業プリント②　＜応用＞", NAME + "得点　　　／50点"),
  P("大問ごとに時間を区切って解き、解説を聞きます。★は100点をねらう問題です。", { before: 80, size: 20 }),

  qHead(1, "ダイヤグラム（追いつく）", "目安6分　（17点）"),
  row2(CW - 4500, [
    P("弟は9時に家を出発し、分速60mで歩いて、家から2400m離れた駅に向かいました。兄は9時15分に家を出発し、自転車で分速180mで同じ道を駅に向かいました。"),
    P("右の図は、弟が家を出発してから$x$分後の家からの道のりを$y$mとして、弟のようすを表したものです。"),
    qgrid([
      { q: [P("（1）弟について、$y$を$x$の式で表しなさい。（5点）")], work: 300, ans: "$y$＝", ansW: 2800 },
      { q: [P("（2）兄について、$y$を$x$の式で表しなさい。（6点）")], work: 300, ans: "$y$＝", ansW: 2800 },
    ], 2, { width: CW - 4500 }),
  ], [imgP("o2b_dia.png", 255)]),
  P("★（3）兄が弟に追いついた時刻と、そこが家から何mの地点かを求めなさい。（完全正答6点）"),
  space(1400), ansBox("9時　　　分　　　秒、家から　　　　m", 5400),

  qHead(2, "動く点と面積", "目安6分　（17点）"),
  row2(CW - 3200, [
    P("右の図のような長方形ABCDで、点PはAを出発して、辺AB、BC、CD上をDまで毎秒1cmの速さで動きます。点PがAを出発してから$x$秒後の△APDの面積を$y$cm²とします。"),
    qgrid([
      { q: [P("（1）$x=3$のときの$y$の値を求めなさい。（5点）")], work: 400, ans: "", ansW: 2400 },
      { q: [P("（2）点Pが辺CD上を動くとき、$y$を$x$の式で表しなさい。また、$x$の変域も書きなさい。（完全正答6点）")], work: 900, ans: "$y$＝　　　　　（　　　　　）", ansW: 4300 },
    ], 2, { width: CW - 3200 }),
  ], [imgP("o2b_rect.png", 160)]),
  P("★（3）△APDの面積が6cm²になるのは、点PがAを出発してから何秒後ですか。すべて求めなさい。（完全正答6点）"),
  space(1300), ansBox("", 3600),

  qHead(3, "水そうの水の量", "目安5分　（16点）"),
  P("水そうAには40Lの水が入っていて、毎分2Lの割合で水をぬきます。空の水そうBには、毎分3Lの割合で水を入れます。A、Bの水の出し入れを同時に始めてから$x$分後の水の量を$y$Lとします。"),
  qgrid([
    { q: [P("（1）水そうAについて、$y$を$x$の式で表しなさい。（5点）")], work: 500, ans: "$y$＝", ansW: 2800 },
    { q: [P("（2）水そうBについて、$y$を$x$の式で表しなさい。（5点）")], work: 500, ans: "$y$＝", ansW: 2800 },
  ], 2),
  P("★（3）2つの水そうの水の量が等しくなるのは、何分後ですか。また、そのときの水の量を求めなさい。（完全正答6点）"),
  space(1300), ansBox("　　　　分後、　　　　L", 3800),
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
  bandTitle("第2回　採点用の解答", "先生用"),
  qHead("授業プリント①", "基本（50点）"),
  keyTable([
    ["1（1）", "$y={1/2}x+10$（$y=0.5x+10$も正解）", "4"], ["1（2）", "16cm", "4"], ["1（3）", "30g", "4"],
    ["2（1）", "分速80m", "3"], ["2（2）", "10分間", "3"], ["2（3）", "$y=120x−1600$", "4"], ["2（4）", "9時25分", "4"],
    ["3（1）", "12", "4"], ["3（2）", "$y=3x$", "4"], ["3（3）", "$0≦y≦24$", "4"],
    ["4（1）", "(2, 4)", "6"], ["4（2）", "16", "6"],
  ]),
  qHead("授業プリント②", "応用（50点）"),
  keyTable([
    ["1（1）", "$y=60x$", "5"], ["1（2）", "$y=180x−2700$", "6"],
    ["★1（3）", "9時22分30秒、家から1350m（完全正答）", "6"],
    ["2（1）", "9", "5"], ["2（2）", "$y=−3x+42$（$10≦x≦14$）（完全正答）", "6"],
    ["★2（3）", "2秒後と12秒後（完全正答）", "6"],
    ["3（1）", "$y=−2x+40$", "5"], ["3（2）", "$y=3x$", "5"],
    ["★3（3）", "8分後、24L（完全正答）", "6"],
  ]),
];

// ============ 宿題（B4×1） ============
const hw = [
  bandTitle("第2回　宿題", NAME + "提出日　　／　　"),
  P("11/6（金）の授業までに、解き終わったら解答解説で丸つけをして、まちがえた問題は直しノートを作りましょう。", { before: 80, size: 20 }),
  qHead(1, "ダイヤグラム（すれちがう）"),
  row2(CW - 4500, [
    P("家から1500m離れた公園があります。姉は家から公園へ、妹は公園から家へ向かって、同時に出発しました。右の図は、2人が出発してから$x$分後の、家からの道のりを$y$mとして表したものです。"),
    qgrid([
      { q: [P("（1）姉の速さは、分速何mですか。")], work: 400, ans: "分速　　　　m", ansW: 2700 },
      { q: [P("（2）妹について、$y$を$x$の式で表しなさい。")], work: 700, ans: "$y$＝", ansW: 2800 },
    ], 2, { width: CW - 4500 }),
    P("（3）2人がすれちがうのは、出発してから何分後ですか。また、それは家から何mの地点ですか。"),
    space(700), ansBox("　　　　分後、家から　　　　m", 4400),
  ], [imgP("h2b_dia.png", 255)]),
  qHead(2, "動く点と面積"),
  P("下の図のような長方形ABCDで、点PはBを出発して、辺BC、CD上をDまで毎秒1cmの速さで動きます。点PがBを出発してから$x$秒後の△ABPの面積を$y$cm²とします。"),
  row2(CW - 4800, [
    imgP("h2b_rect.png", 170, d.AlignmentType.LEFT),
    P("（1）$x=3$のときの$y$の値を求めなさい。", { before: 60 }), space(500), ansBox("", 2600),
    P("（2）点Pが辺CD上にあるとき、$y$の値を求めなさい。", { before: 60 }), space(500), ansBox("", 2600),
    P("（3）$0≦x≦10$のときの$x$と$y$の関係を表すグラフを、右の図にかきなさい。", { before: 60 }),
  ], [imgP("h2b_grid.png", 265)]),
  qHead(3, "ばねの長さ（表から式を求める）"),
  P("あるばねにおもりをつるして、ばねの長さを調べたら、下の表のようになりました。おもりの重さを$x$g、ばねの長さを$y$cmとすると、$y$は$x$の一次関数です。"),
  grid([["おもりの重さ（g）", "0", "10", "20", "30"], ["ばねの長さ（cm）", "8", "9.5", "11", "12.5"]], [2600, 1200, 1200, 1200, 1200], { headCol: true, indent: 300 }),
  qgrid([
    { q: [P("（1）$y$を$x$の式で表しなさい。")], work: 600, ans: "$y$＝", ansW: 3000 },
    { q: [P("（2）ばねの長さが17cmになるのは、何gのおもりをつるしたときですか。")], work: 600, ans: "　　　　g", ansW: 2600 },
  ], 2),
];

// ============ 宿題の解答解説 ============
const A = (no, ans, steps, o = {}) => [
  P(`${no}　**答え　${ans}**`, { before: 80, after: 20, keepNext: true }),
  ...steps.map(s => P(s, { indent: 500, after: 10, size: 21, keepNext: o.keepNext })),
];
const kai = [
  bandTitle("第2回　宿題　解答解説", ""),
  P("**〇かどうかわからない場合は、適当に〇をつけずに必ず先生に確認しましょう**", { before: 120, after: 120, size: 24 }),
  qHead(1, "ダイヤグラム（すれちがう）"),
  row2(CW - 4300, [
    ...A("（1）", "分速100m", ["姉は15分で1500m進んでいる。$1500÷15=100$（m）"]),
    ...A("（2）", "$y=−50x+1500$", ["妹は30分で1500m進むので、分速$1500÷30=50$（m）。", "家に近づくので、$y$は1分に50ずつ減る。傾きは$−50$、切片は出発地点の1500。"]),
    ...A("（3）", "10分後、家から1000m", ["すれちがう点は、2つのグラフの交点。2つの式を連立方程式として解く。", "姉の式は$y=100x$。$100x=−50x+1500$ → $150x=1500$ → $x=10$。$y=100×10=1000$。"]),
    P("【答えの確かめ】10分後、姉は$100×10=1000$（m）、妹は$1500−50×10=1000$（m）の地点にいる。同じ地点なので、問題にあっている。", { indent: 500, size: 21 }),
  ], [imgP("h2b_dia_ans.png", 245), P("交点（すれちがう点）から、$x$軸と$y$軸に破線をおろすと、時間と道のりが読める。", { size: 19 })], { right: 200 }),
  qHead(2, "動く点と面積"),
  row2(CW - 4300, [
    ...A("（1）", "6", ["3秒後、点PはBから3cm進んで辺BC上にある。BP＝3cm。", "△ABPは、底辺BP＝3、高さAB＝4。$3×4÷2=6$"]),
    ...A("（2）", "12", ["点Pが辺CD上にあるとき、△ABPの底辺をABとみると、高さはいつもBC＝6cm。", "$4×6÷2=12$。点Pが辺CD上のどこにあっても、面積は変わらない。"]),
    ...A("（3）", "右の図", ["点PがBC上（$0≦x≦6$）：底辺BP＝$x$、高さ4なので、$y=x×4÷2=2x$。", "点PがCD上（$6≦x≦10$）：（2）より$y=12$。$x$軸に平行な線になる。", "(0, 0)、(6, 12)、(10, 12)を順に結ぶ。"]),
  ], [imgP("h2b_graph_ans.png", 235)], { right: 200 }),
  qHead(3, "ばねの長さ（表から式を求める）"),
  ...A("（1）", "$y={3/20}x+8$（$y=0.15x+8$も正解）", ["おもりが10g増えると、ばねは1.5cmずつのびる。", "変化の割合＝${1.5/10}=0.15={3/20}$。これが傾き。$x=0$のとき$y=8$なので、切片は8。"]),
  ...A("（2）", "60g", ["$y=17$を代入する。$17=0.15x+8$ → $0.15x=9$ → $x=60$。", "【確かめ】$0.15×60+8=9+8=17$（cm）で、問題にあっている。"]),
];

// ============ 書き出し ============
Promise.all([
  L.save(`${OUT}/第2回_授業プリント.docx`, [sec("第2回 授業プリント", kihon), sec("第2回 授業プリント", ouyo)]),
  L.save(`${OUT}/第2回_採点用解答.docx`, [sec("第2回 採点用の解答", key)]),
  L.save(`${OUT}/第2回_宿題.docx`, [sec("第2回 宿題", hw)]),
  L.save(`${OUT}/第2回_宿題_解答解説.docx`, [sec("第2回 宿題 解答解説", kai)]),
]).then(() => console.log("ok"));

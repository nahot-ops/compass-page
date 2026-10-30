// 第1回（10/30）総ざらい①　連立方程式＋一次関数の前半
const L = require("./lib");
const { d, P, Gothic, space, imgP, ansBox, qgrid, bandTitle, qHead, frame, SYS, M, runs, CW } = L;
const OUT = require("path").join(__dirname, "..");

const NAME = "2年　　組　　番　氏名　　　　　　　　　　";
const XY = "$(x,y)$＝(　　　，　　　)";
const sec = (label, children) => ({ properties: L.sectionProps, headers: { default: L.header() }, footers: { default: L.footer(label) }, children });
const sysP = (no, rows) => new d.Paragraph({ children: [...runs(no + "　"), SYS(rows)], spacing: { after: 40 } });

// ============ 授業プリント ============
const kihon = [
  bandTitle("第1回　授業プリント①　＜基本＞", NAME + "得点　　　／50点"),
  P("目安10分。解き終わったら提出しましょう。答えは最も簡単な形で書きましょう。", { before: 80, size: 20 }),

  qHead(1, "次の連立方程式を解きなさい。", "（4点×5）"),
  qgrid([
    { q: [sysP("（1）", ["2x+y=7", "x−y=2"])], work: 1700, ans: XY },
    { q: [sysP("（2）", ["3x+2y=4", "5x+3y=7"])], work: 1700, ans: XY },
    { q: [sysP("（3）", ["y=2x−1", "3x+2y=12"])], work: 1700, ans: XY },
    { q: [sysP("（4）", ["3x−2(x−y)=7", "x+3y=11"])], work: 1900, ans: XY },
    { q: [sysP("（5）", ["{x/2}+{y/3}=1", "3x−y=15"])], work: 1900, ans: XY },
  ], 3),

  qHead(2, "次の問いに答えなさい。"),
  P("（1）次のア～エのうち、$y$が$x$の一次関数であるものをすべて選び、記号で答えなさい。（完全正答3点）"),
  P("ア　1本80円の鉛筆を$x$本と、100円のノートを1冊買ったときの代金$y$円", { indent: 500 }),
  P("イ　面積が20cm²の長方形の、縦の長さ$x$cmと横の長さ$y$cm", { indent: 500 }),
  P("ウ　1辺が$x$cmの正方形の、周りの長さ$y$cm", { indent: 500 }),
  P("エ　半径が$x$cmの円の面積$y$cm²", { indent: 500, after: 0 }),
  ansBox("", 2600),
  space(100),
  P("（2）一次関数$y=−3x+5$で、$x$の値が$−1$から3まで変わるとき、次の値を求めなさい。（3点×3）"),
  qgrid([
    { q: [P("①　$x$の増加量")], work: 500, ans: "", ansW: 2400 },
    { q: [P("②　$y$の増加量")], work: 500, ans: "", ansW: 2400 },
    { q: [P("③　変化の割合")], work: 500, ans: "", ansW: 2400 },
  ], 3),
  P("（3）次の一次関数の式を求めなさい。（3点×3）"),
  qgrid([
    { q: [P("①　傾きが2で、点(3, 1)を通る直線")], work: 1000, ans: "$y$＝" },
    { q: [P("②　2点$(−1,7)$、$(2,1)$を通る直線")], work: 1000, ans: "$y$＝" },
    { q: [P("③　直線$y=3x−4$に平行で、点$(2,−1)$を通る直線")], work: 1000, ans: "$y$＝" },
  ], 3),
];
// （4）（5）は図を入れるため3列で組む
kihon.push(new d.Table({
  width: { size: CW, type: d.WidthType.DXA }, columnWidths: [4400, 4400, CW - 8800], borders: d.TableBorders.NONE,
  rows: [new d.TableRow({ cantSplit: true, children: [
    new d.TableCell({ borders: L.NOB, width: { size: 4400, type: d.WidthType.DXA }, margins: { right: 160 }, children: [P("（4）一次関数$y=−2x+3$で、$x$の変域が$−1≦x≦2$のとき、$y$の変域を求めなさい。（3点）"), space(1000), ansBox("", 3600)] }),
    new d.TableCell({ borders: L.NOB, width: { size: 4400, type: d.WidthType.DXA }, margins: { right: 160 }, children: [P("（5）右の図の直線①、②の式を求めなさい。（3点×2）"), space(500), ansBox("①　$y$＝", 3600), space(300), ansBox("②　$y$＝", 3600)] }),
    new d.TableCell({ borders: L.NOB, width: { size: CW - 8800, type: d.WidthType.DXA }, children: [imgP("j1_read.png", 205)] }),
  ] })],
}));

const ouyo = [
  bandTitle("第1回　授業プリント②　＜応用＞", NAME + "得点　　　／50点"),
  P("大問ごとに時間を区切って解き、解説を聞きます。★は100点をねらう問題です。", { before: 80, size: 20 }),

  qHead(1, "2直線と三角形", "目安5分　（22点）"),
  new d.Table({
    width: { size: CW, type: d.WidthType.DXA }, columnWidths: [CW - 4300, 4300], borders: d.TableBorders.NONE,
    rows: [new d.TableRow({ children: [
      new d.TableCell({ borders: L.NOB, width: { size: CW - 4300, type: d.WidthType.DXA }, margins: { right: 200 }, children: [
        P("右の図で、直線ℓは$y=2x+4$、直線$m$は$y=−x+7$のグラフです。ℓと$m$の交点をA、ℓ、$m$と$x$軸との交点をそれぞれB、Cとします。"),
        P("（1）点Aの座標を求めなさい。（5点）", { before: 100 }), space(700), ansBox("A（　　　，　　　）", 3400),
        P("（2）△ABCの面積を求めなさい。（5点）", { before: 60 }), space(700), ansBox("", 2600),
      ] }),
      new d.TableCell({ borders: L.NOB, width: { size: 4300, type: d.WidthType.DXA }, children: [imgP("o1_tri.png", 240)] }),
    ] })],
  }),
  qgrid([
    { q: [P("（3）点Bを通り、△ABCの面積を2等分する直線の式を求めなさい。（6点）")], work: 1100, ans: "$y$＝" },
    { q: [P("★（4）点Aを通り、△ABCの面積を2等分する直線の式を求めなさい。（6点）")], work: 1100, ans: "$y$＝" },
  ], 2),

  qHead(2, "連立方程式の利用", "目安4分　（16点）"),
  P("（1）1個120円のりんごと1個80円のみかんを、あわせて15個買ったところ、代金の合計は1520円でした。"),
  qgrid([
    { q: [P("①　りんごを$x$個、みかんを$y$個買ったとして、連立方程式をつくりなさい。（完全正答5点）")], work: 200, ans: "", ansW: 4200, ansH: 1000 },
    { q: [P("②　りんごとみかんを、それぞれ何個買いましたか。（5点）")], work: 200, ans: "りんご　　　個、みかん　　　個", ansW: 4600 },
  ], 2),
  P("★（2）2けたの自然数があります。十の位の数と一の位の数の和は11です。また、十の位の数と一の位の数を入れかえてできる数は、もとの数より27大きくなります。もとの自然数を求めなさい。"),
  P("ただし、用いる文字が何を表すかを最初に書いてから連立方程式をつくり、解いて求めなさい。（6点）", { after: 0 }),
  space(1100), ansBox("", 2600),

  qHead(3, "一次関数の式", "目安9分　（12点）"),
  qgrid([
    { q: [P("（1）2つの直線$y=ax+6$と$y=3x−6$のグラフが、$x$軸上で交わるとき、$a$の値を求めなさい。（6点）")], work: 2600, ans: "$a$＝", ansW: 2800 },
    { q: [P("★（2）一次関数$y=ax+b$（$a<0$）で、$x$の変域が$−2≦x≦4$のとき、$y$の変域は$−1≦y≦5$です。$a$、$b$の値を求めなさい。（完全正答6点）")], work: 2600, ans: "$a$＝　　　　，$b$＝", ansW: 3800 },
  ], 2),
];

// ============ 採点用の解答 ============
function keyTable(rows) {
  const w = [1800, CW - 1800 - 1400, 1400];
  const cell = (t, i, head) => new d.TableCell({ borders: L.BOX, width: { size: w[i], type: d.WidthType.DXA }, margins: { left: 100, right: 100, top: 30, bottom: 30 },
    shading: head ? { type: d.ShadingType.CLEAR, fill: "D9D9D9", color: "auto" } : undefined,
    children: [P(t, { after: 0, font: head ? L.GOT : undefined, bold: head, align: i === 2 ? d.AlignmentType.CENTER : undefined })] });
  return new d.Table({ width: { size: CW, type: d.WidthType.DXA }, columnWidths: w,
    rows: [["番号", "答え", "配点"], ...rows].map((r, k) => new d.TableRow({ cantSplit: true, children: r.map((t, i) => cell(t, i, k === 0)) })) });
}
const key = [
  bandTitle("第1回　採点用の解答", "先生用"),
  qHead("授業プリント①", "基本（50点）"),
  keyTable([
    ["1（1）", "$(x,y)=(3,1)$", "4"], ["1（2）", "$(x,y)=(2,−1)$", "4"], ["1（3）", "$(x,y)=(2,3)$", "4"],
    ["1（4）", "$(x,y)=(−1,4)$", "4"], ["1（5）", "$(x,y)=(4,−3)$", "4"],
    ["2（1）", "ア、ウ（完全正答）", "3"],
    ["2（2）①", "4", "3"], ["2（2）②", "$−12$", "3"], ["2（2）③", "$−3$", "3"],
    ["2（3）①", "$y=2x−5$", "3"], ["2（3）②", "$y=−2x+5$", "3"], ["2（3）③", "$y=3x−7$", "3"],
    ["2（4）", "$−1≦y≦5$", "3"],
    ["2（5）", "①　$y=2x−3$　　②　$y=−{1/2}x+2$", "3×2"],
  ]),
  qHead("授業プリント②", "応用（50点）"),
  keyTable([
    ["1（1）", "A(1, 6)", "5"], ["1（2）", "27", "5"],
    ["1（3）", "$y={1/2}x+1$", "6"], ["★1（4）", "$y=−4x+10$", "6"],
    ["2（1）①", "$x+y=15$、$120x+80y=1520$（完全正答。2式とも正しいとき）", "5"],
    ["2（1）②", "りんご8個、みかん7個", "5"],
    ["★2（2）", "47（文字の説明・連立方程式・答えがそろって6点）", "6"],
    ["3（1）", "$a=−3$", "6"], ["★3（2）", "$a=−1$、$b=3$（完全正答）", "6"],
  ]),
];

// ============ 宿題 ============
const hw1 = [
  bandTitle("第1回　宿題①　＜基本＞", NAME + "提出日　　／　　"),
  P("11/4（水）の授業までに、解き終わったら解答解説で丸つけをして、まちがえた問題は直しノートを作りましょう。", { before: 80, size: 20 }),
  qHead(1, "次の連立方程式を解きなさい。"),
  qgrid([
    { q: [sysP("（1）", ["x+y=5", "3x−y=7"])], work: 1300, ans: XY },
    { q: [sysP("（2）", ["2x+3y=1", "3x+4y=2"])], work: 1300, ans: XY },
    { q: [sysP("（3）", ["x=3y+1", "2x−5y=4"])], work: 1300, ans: XY },
    { q: [sysP("（4）", ["2(x+y)−3y=7", "x+2y=1"])], work: 1300, ans: XY },
    { q: [sysP("（5）", ["0.2x+0.3y=1.3", "x−y=4"])], work: 1300, ans: XY },
    { q: [P("（6）$2x+y=x+3y=5$")], work: 1300, ans: XY },
  ], 3),
  qHead(2, "次の問いに答えなさい。"),
  P("（1）次のア～エのうち、$y$が$x$の一次関数であるものをすべて選び、記号で答えなさい。"),
  P("ア　底辺が$x$cm、高さが6cmの三角形の面積$y$cm²", { indent: 500 }),
  P("イ　100kmの道のりを時速$x$kmで進むときにかかる時間$y$時間", { indent: 500 }),
  P("ウ　20Lの水が入った水そうから、毎分2Lずつ水をぬくとき、ぬき始めてから$x$分後の水の量$y$L", { indent: 500 }),
  P("エ　1辺が$x$cmの立方体の体積$y$cm³", { indent: 500, after: 0 }),
  ansBox("", 2600), space(80),
  qgrid([
    { q: [P("（2）一次関数$y={2/3}x−1$で、$x$の増加量が6のときの$y$の増加量を求めなさい。")], work: 600, ans: "", ansW: 2400 },
    { q: [P("（3）一次関数$y=−2x+5$で、$x$の値が$a$から4まで増加したとき、$y$の増加量は$−10$です。$a$の値を求めなさい。")], work: 600, ans: "$a$＝", ansW: 2400 },
  ], 2),
  P("（4）次の一次関数の式を求めなさい。"),
  qgrid([
    { q: [P("①　傾きが$−3$で、点$(2,−1)$を通る直線")], work: 900, ans: "$y$＝" },
    { q: [P("②　2点(1, 3)、(4, 9)を通る直線")], work: 900, ans: "$y$＝" },
    { q: [P("③　直線$y=−{1/2}x+3$に平行で、点$(4,−1)$を通る直線")], work: 900, ans: "$y$＝" },
    { q: [P("④　$x=2$のとき$y=1$、$x=−2$のとき$y=9$")], work: 900, ans: "$y$＝" },
    { q: [P("（5）一次関数$y={1/2}x+1$で、$x$の変域が$−4≦x≦2$のときの$y$の変域を求めなさい。")], work: 900, ans: "" },
  ], 3),
];
const hw2 = [
  bandTitle("第1回　宿題②　＜応用＞", NAME),
  new d.Table({
    width: { size: CW, type: d.WidthType.DXA }, columnWidths: [CW / 2, CW / 2], borders: d.TableBorders.NONE,
    rows: [new d.TableRow({ children: [
      new d.TableCell({ borders: L.NOB, width: { size: CW / 2, type: d.WidthType.DXA }, margins: { right: 200 }, children: [
        qHead(3, "次の式のグラフをかきなさい。番号もかくこと。"),
        P("①　$y={3/4}x−2$　　②　$x+2y=4$　　③　$y=−3$"),
        imgP("grid_blank.png", 220),
      ] }),
      new d.TableCell({ borders: L.NOB, width: { size: CW / 2, type: d.WidthType.DXA }, margins: { left: 200 }, children: [
        qHead(4, "右下の図の直線①、②について答えなさい。"),
        P("（1）直線①、②の式を求めなさい。"),
        ansBox("①　$y$＝", 3400), space(100), ansBox("②　$y$＝", 3400),
        P("（2）直線①と②の交点の座標を、計算で求めなさい。", { before: 100 }),
        imgP("h_read.png", 170, d.AlignmentType.RIGHT),
        ansBox("（　　　，　　　）", 3000),
      ] }),
    ] })],
  }),
  qHead(5, "右の図で、直線ℓは$y=−x+6$、直線$m$は$y={1/2}x+3$のグラフです。ℓと$m$の交点をA、$m$、ℓと$x$軸との交点をそれぞれB、Cとします。"),
  new d.Table({
    width: { size: CW, type: d.WidthType.DXA }, columnWidths: [CW - 4400, 4400], borders: d.TableBorders.NONE,
    rows: [new d.TableRow({ children: [
      new d.TableCell({ borders: L.NOB, width: { size: CW - 4400, type: d.WidthType.DXA }, children: [
        qgrid([
          { q: [P("（1）点Aの座標")], work: 400, ans: "A（　　，　　）", ansW: 2800 },
          { q: [P("（2）△ABCの面積")], work: 500, ans: "", ansW: 2400 },
          { q: [P("（3）点Aを通り、△ABCの面積を2等分する直線の式")], work: 600, ans: "$y$＝", ansW: 3000 },
          { q: [P("★（4）点Cを通り、△ABCの面積を2等分する直線の式")], work: 600, ans: "$y$＝", ansW: 3000 },
        ], 2, { width: CW - 4400 }),
      ] }),
      new d.TableCell({ borders: L.NOB, width: { size: 4400, type: d.WidthType.DXA }, children: [imgP("h_tri.png", 240)] }),
    ] })],
  }),
  qHead(6, "連立方程式の利用"),
  qgrid([
    { q: [P("（1）1本60円の鉛筆と1冊150円のノートを、あわせて12個買ったところ、代金の合計は1080円でした。鉛筆とノートを、それぞれいくつ買いましたか。")], work: 1000, ans: "鉛筆　　　本、ノート　　　冊", ansW: 4400 },
    { q: [P("（2）ある中学校の昨年の生徒数は240人でした。今年は、昨年とくらべて男子が10％増え、女子が5％減ったので、全体で243人になりました。昨年の男子と女子の生徒数を、それぞれ求めなさい。")], work: 1000, ans: "男子　　　人、女子　　　人", ansW: 4400 },
  ], 2),
  P("★（3）家から14km離れた公園まで行くのに、はじめは自転車で時速12km、途中からは歩いて時速4kmで進んだところ、全体で1時間30分かかりました。自転車で進んだ道のりと歩いた道のりを、それぞれ求めなさい。", { before: 60 }),
  space(800), ansBox("自転車　　　km、歩き　　　km", 4400),
  qHead(7, "★チャレンジ"),
  qgrid([
    { q: [P("（1）一次関数$y=ax+b$（$a>0$）で、$x$の変域が$−1≦x≦3$のとき、$y$の変域は$1≦y≦9$です。$a$、$b$の値を求めなさい。")], work: 500, ans: "$a$＝　　　，$b$＝", ansW: 3600 },
    { q: [P("（2）2つの直線$y=2x+a$と$y=−x+3$のグラフが、$x$軸上で交わるとき、$a$の値を求めなさい。")], work: 500, ans: "$a$＝", ansW: 2400 },
  ], 2),
];

// ============ 宿題の解答解説 ============
const A = (no, ans, steps, o = {}) => [
  P(`${no}　**答え　${ans}**`, { before: 80, after: 20, keepNext: true }),
  ...steps.map(s => P(s, { indent: 500, after: 10, size: 21, keepNext: o.keepNext })),
];
const kai = [
  bandTitle("第1回　宿題　解答解説", ""),
  P("**〇かどうかわからない場合は、適当に〇をつけずに必ず先生に確認しましょう**", { before: 120, after: 120, size: 24 }),
  qHead(1, "連立方程式"),
  ...A("（1）", "$(x,y)=(3,2)$", ["①＋②で$y$を消す（加減法）。$4x=12$より$x=3$。①に代入して$3+y=5$、$y=2$。"]),
  ...A("（2）", "$(x,y)=(2,−1)$", ["$x$の係数をそろえる。①×3：$6x+9y=3$、②×2：$6x+8y=4$。", "上から下をひくと$y=−1$。①に代入して$2x−3=1$、$x=2$。"]),
  ...A("（3）", "$(x,y)=(7,2)$", ["①を②に代入する（代入法）。$2(3y+1)−5y=4$ → $6y+2−5y=4$ → $y=2$。", "①に代入して$x=3×2+1=7$。"]),
  ...A("（4）", "$(x,y)=(3,−1)$", ["まず①のかっこをはずして整理する。$2x+2y−3y=7$ → $2x−y=7$……①′", "①′×2＋②：$5x=15$、$x=3$。②に代入して$3+2y=1$、$y=−1$。"]),
  ...A("（5）", "$(x,y)=(5,1)$", ["①の両辺を10倍して、係数を整数にする。$2x+3y=13$……①′", "②より$x=y+4$。①′に代入して$2(y+4)+3y=13$ → $5y=5$ → $y=1$、$x=5$。"]),
  ...A("（6）", "$(x,y)=(2,1)$", ["A＝B＝Cの形は、A＝C、B＝Cの2つの式に分ける。", "$2x+y=5$……①、$x+3y=5$……②。②より$x=5−3y$を①に代入して$y=1$、$x=2$。"]),
  qHead(2, "一次関数の基本"),
  ...A("（1）", "ア、ウ", ["ア　$y=3x$（$b=0$の一次関数）　イ　$y={100/x}$（反比例）", "ウ　$y=−2x+20$（一次関数）　エ　$y=x³$（一次関数ではない）"]),
  ...A("（2）", "4", ["$y$の増加量＝変化の割合×$x$の増加量＝${2/3}×6=4$"]),
  ...A("（3）", "$a=−1$", ["$x$の増加量は$4−a$。$y$の増加量＝$−2×(4−a)=−10$", "$4−a=5$より$a=−1$。"]),
  ...A("（4）①", "$y=−3x+5$", ["$y=−3x+b$に$x=2$、$y=−1$を代入。$−1=−6+b$より$b=5$。"]),
  ...A("（4）②", "$y=2x+1$", ["傾き＝${9−3/4−1}={6/3}=2$。$y=2x+b$に(1, 3)を代入して$b=1$。"]),
  ...A("（4）③", "$y=−{1/2}x+1$", ["平行な直線は傾きが同じ。$y=−{1/2}x+b$に$(4,−1)$を代入。$−1=−2+b$、$b=1$。"]),
  ...A("（4）④", "$y=−2x+5$", ["2点$(2,1)$、$(−2,9)$を通る直線と考える。傾き＝${1−9/2−(−2)}={−8/4}=−2$。", "$y=−2x+b$に(2, 1)を代入して$b=5$。"]),
  ...A("（5）", "$−1≦y≦2$", ["$x=−4$のとき$y=−2+1=−1$、$x=2$のとき$y=1+1=2$。", "傾きが正なので、小さい方から$−1≦y≦2$。グラフをかいて確かめると安心です。"]),
];
const kai2 = [
  qHead(3, "グラフをかく"),
  new d.Table({
    width: { size: CW, type: d.WidthType.DXA }, columnWidths: [CW - 4200, 4200], borders: d.TableBorders.NONE,
    rows: [new d.TableRow({ children: [
      new d.TableCell({ borders: L.NOB, width: { size: CW - 4200, type: d.WidthType.DXA }, children: [
        frame("グラフのかき方の手順", [
          P("手順1　切片を見て、$y$軸上に点をとる。"),
          P("手順2　傾きを見て、「右へ○、上（下）へ△」進んだ点をとる。"),
          P("手順3　2点を通る直線をひく。", { after: 0 }),
        ]),
        ...A("①", "$y={3/4}x−2$", ["切片$−2$で(0, −2)。傾き${3/4}$なので、右へ4、上へ3進んで(4, 1)。図の点線を見よう。"]),
        ...A("②", "$y=−{1/2}x+2$", ["$x+2y=4$を$y$について解く。$2y=−x+4$ → $y=−{1/2}x+2$。", "(0, 2)と(4, 0)を通る直線。"]),
        ...A("③", "$y=−3$", ["$y=k$のグラフは、$x$軸に平行な直線。点(0, −3)を通る。"]),
      ] }),
      new d.TableCell({ borders: L.NOB, width: { size: 4200, type: d.WidthType.DXA }, children: [imgP("h_graph_ans.png", 260)] }),
    ] })],
  }),
  qHead(4, "グラフから式を読む"),
  ...A("（1）", "①　$y=−2x+3$　　②　$y={1/2}x−2$", ["①　切片3。(0, 3)から右へ1進むと下へ2なので傾き$−2$。", "②　切片$−2$。(0, −2)から右へ4進むと上へ2なので傾き${2/4}={1/2}$。"]),
  ...A("（2）", "(2, −1)", ["交点の座標は、2つの式を連立方程式として解いた解。", "$−2x+3={1/2}x−2$。両辺を2倍して$−4x+6=x−4$ → $−5x=−10$ → $x=2$、$y=−1$。"]),
  qHead(5, "2直線と三角形"),
  new d.Table({
    width: { size: CW, type: d.WidthType.DXA }, columnWidths: [CW - 4400, 4400], borders: d.TableBorders.NONE,
    rows: [new d.TableRow({ children: [
      new d.TableCell({ borders: L.NOB, width: { size: CW - 4400, type: d.WidthType.DXA }, children: [
        ...A("（1）", "A(2, 4)", ["$−x+6={1/2}x+3$を解く。両辺を2倍して$−2x+12=x+6$ → $x=2$、$y=4$。"]),
        ...A("（2）", "24", ["B、Cは$y=0$を代入して求める。B$(−6,0)$、C(6, 0)。", "底辺BC＝$6−(−6)=12$、高さはAの$y$座標で4。$12×4÷2=24$"]),
        ...A("（3）", "$y=2x$", ["頂点Aを通って面積を2等分する直線は、向かいの辺BCの中点を通る。", "中点の座標は、$x$座標どうし・$y$座標どうしをたして2でわる。BCの中点は$({−6+6/2},0)$＝(0, 0)。原点とA(2, 4)を通るので$y=2x$。図の一点鎖線。"]),
        ...A("★（4）", "$y=−{1/4}x+{3/2}$", ["頂点Cを通るので、向かいの辺ABの中点Nを通る。", "N＝$({−6+2/2},{0+4/2})$＝$(−2,2)$。C(6, 0)とNを通る直線の傾きは${0−2/6−(−2)}=−{1/4}$。", "$y=−{1/4}x+b$にC(6, 0)を代入。$0=−{3/2}+b$、$b={3/2}$。図の点線。"]),
      ] }),
      new d.TableCell({ borders: L.NOB, width: { size: 4400, type: d.WidthType.DXA }, children: [imgP("h_tri_ans.png", 280), P("中点を通る線で、三角形は「底辺が同じ・高さが同じ」2つに分かれます。", { size: 19 })] }),
    ] })],
  }),
  qHead(6, "連立方程式の利用"),
  ...A("（1）", "鉛筆8本、ノート4冊", ["鉛筆を$x$本、ノートを$y$冊とする。$x+y=12$……①、$60x+150y=1080$……②", "②÷30：$2x+5y=36$。①×2をひくと$3y=12$、$y=4$、$x=8$。問題にあっている。"]),
  ...A("（2）", "男子100人、女子140人", ["昨年の男子を$x$人、女子を$y$人とする。増えた人数と減った人数を表に整理する。"], { keepNext: true }),
  new d.Table({
    width: { size: 7600, type: d.WidthType.DXA }, columnWidths: [2200, 1800, 1800, 1800], indent: { size: 500, type: d.WidthType.DXA },
    rows: [["", "男子", "女子", "合計"], ["昨年（人）", "$x$", "$y$", "240"], ["増減（人）", "$+{10/100}x$", "$−{5/100}y$", "$+3$"]].map((r, k) => new d.TableRow({ children: r.map((t, i) => new d.TableCell({ borders: L.BOX, width: { size: [2200, 1800, 1800, 1800][i], type: d.WidthType.DXA }, shading: k === 0 ? { type: d.ShadingType.CLEAR, fill: "E7E6E6", color: "auto" } : undefined, children: [P(t, { after: 0, align: d.AlignmentType.CENTER, keepNext: true })] })) })),
  }),
  P("$x+y=240$……①、${10/100}x−{5/100}y=3$……②。②×100：$10x−5y=300$ → $2x−y=60$……②′", { indent: 500, before: 60, size: 21 }),
  P("①＋②′：$3x=300$、$x=100$。①に代入して$y=140$。", { indent: 500, size: 21 }),
  P("【答えの確かめ】求めた昨年の人数から、今年の人数を計算する。", { indent: 500, size: 21 }),
  P("今年の男子：昨年の100人から10％増えたので、$100+100×{10/100}=100+10=110$（人）", { indent: 700, size: 21 }),
  P("今年の女子：昨年の140人から5％減ったので、$140−140×{5/100}=140−7=133$（人）", { indent: 700, size: 21 }),
  P("合計は$110+133=243$（人）で、問題の「全体で243人」と同じなので、問題にあっている。", { indent: 700, size: 21 }),
  ...A("★（3）", "自転車12km、歩き2km", ["自転車の道のりを$x$km、歩いた道のりを$y$kmとして、線分図に整理する。"]),
  imgP("h_speed.png", 380),
  P("道のり：$x+y=14$……①　時間：${x/12}+{y/4}={3/2}$……②（1時間30分＝${3/2}$時間）", { indent: 500, size: 21 }),
  P("②×12：$x+3y=18$。①をひくと$2y=4$、$y=2$、$x=12$。時間は$1+{1/2}={3/2}$時間で、問題にあっている。", { indent: 500, size: 21 }),
  qHead(7, "★チャレンジ"),
  ...A("（1）", "$a=2$、$b=3$", ["$a>0$なので右上がり。$x$が最小のとき$y$も最小、$x$が最大のとき$y$も最大。", "$x=−1$のとき$y=1$、$x=3$のとき$y=9$。$−a+b=1$、$3a+b=9$を解いて$a=2$、$b=3$。"]),
  ...A("（2）", "$a=−6$", ["$y=−x+3$と$x$軸との交点は、$y=0$を代入して(3, 0)。", "$y=2x+a$も(3, 0)を通るので$0=6+a$、$a=−6$。"]),
];

// ============ 書き出し ============
Promise.all([
  L.save(`${OUT}/第1回_授業プリント.docx`, [sec("第1回 授業プリント", kihon), sec("第1回 授業プリント", ouyo)]),
  L.save(`${OUT}/第1回_採点用解答.docx`, [sec("第1回 採点用の解答", key)]),
  L.save(`${OUT}/第1回_宿題.docx`, [sec("第1回 宿題", hw1), sec("第1回 宿題", hw2)]),
  L.save(`${OUT}/第1回_宿題_解答解説.docx`, [sec("第1回 宿題 解答解説", [...kai, ...kai2])]),
]).then(() => console.log("ok"));

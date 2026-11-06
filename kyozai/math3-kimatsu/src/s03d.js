// 中3 第3回　授業プリント②＜応用＞の解答解説（授業中に解けなかった生徒用）
const L = require("./lib");
const { d, P, imgP, bandTitle, qHead, frame, CW } = L;
const OUT = require("path").join(__dirname, "..");

const NAME = "　氏名　　　　　　　　　　";
const sec = (label, children) => ({ properties: L.sectionProps, headers: { default: L.header() }, footers: { default: L.footer(label) }, children });
const cell = (w, children, margins) => new d.TableCell({ borders: L.NOB, width: { size: w, type: d.WidthType.DXA }, margins, children });
const row2 = (w1, left, right, m1, m2) => new d.Table({
  width: { size: CW, type: d.WidthType.DXA }, columnWidths: [w1, CW - w1], borders: d.TableBorders.NONE,
  rows: [new d.TableRow({ children: [cell(w1, left, m1), cell(CW - w1, right, m2)] })],
});
const KH = { s1: 32, s2: 28 };
const T = (t, o = {}) => P(t, { size: 24, mathSize: 28, ...o });
// 表の中で使う（次の段落と同じページを使わない）
const AT = (no, ans, steps) => [
  P(`${no}　**答え　${ans}**`, { before: 80, after: 20, size: 28, mathSize: 28 }),
  ...steps.map(s => typeof s === "string" ? P(s, { indent: 500, after: 10, size: 24, mathSize: 28 }) : s),
];

const kai = [
  bandTitle("第3回　授業プリント②　解答解説", NAME),
  P("**〇かどうかわからない場合は、適当に〇をつけずに必ず先生に確認しましょう**", { before: 120, after: 120, size: 24 }),

  qHead(1, "直角三角形の相似", "", KH),
  ...AT("（1）", "下の証明", []),
  frame("【証明】", [
    T("△ABCと△DBAで、"),
    T("仮定より、∠BAC＝∠BDA＝90°……①"),
    T("共通な角だから、∠ABC＝∠DBA……②"),
    T("①、②より、2組の角がそれぞれ等しいので、△ABC∽△DBA", { after: 0 }),
  ]),
  T("・直角どうし（∠BACと∠BDA）と、頂点Bの角（共通な角）の2組を使う。", { before: 60 }),
  T("・頂点は対応する順に書く。A↔D（直角）、B↔B、C↔Aなので「△DBA」。"),
  row2(CW - 5600, [
    ...AT("（2）", "${18/5}$cm（3.6cm）", [
      "右の図のように、2つの三角形を同じ向きにならべると、対応する辺がわかりやすい。",
      "対応する辺は、ABとDB、BCとBA。",
      "【比の式で解く】AB：DB＝BC：BA",
      "$6:BD=10:6$ → $10×BD=36$ → $BD={18/5}$",
      "【図で何倍か考える】△ABCのBC（10cm）は、△DBAではBA（6cm）になる。",
      "10cmを6cmにするには$×{3/5}$。",
      "AB（6cm）も$×{3/5}$すると、BDになる。$6×{3/5}={18/5}$",
    ]),
  ], [imgP("s3k_o1_ans.png", 360)], { right: 200 }),
  T("BDとBCを対応させてしまうミスが多い。必ず「∽」の頂点の順で、対応する辺を確かめよう。", { before: 60 }),

  new d.Paragraph({ children: [new d.PageBreak()] }),
  qHead(2, "放物線と面積", "", KH),
  row2(CW - 3800, [
    ...AT("（1）", "6", [
      "A$(−1,1)$、B(3, 9)。直線ABの傾きは${9−1/3−(−1)}={8/4}=2$。",
      "$y=2x+b$にA$(−1,1)$を代入して$1=−2+b$、$b=3$。直線ABは$y=2x+3$。",
      "直線ABと$y$軸の交点をC(0, 3)とし、△OABを$y$軸で左右2つに分ける。",
      "△OAC：底辺OC＝3、高さ1（Aの$x$座標−1の絶対値）。$3×1÷2={3/2}$",
      "△OBC：底辺OC＝3、高さ3（Bの$x$座標）。$3×3÷2={9/2}$",
      "合わせて${3/2}+{9/2}=6$",
    ]),
    ...AT("（2）", "P(2, 4)", [
      "【等積変形】△PABと△OABは、底辺ABが共通。高さが等しければ面積も等しい。",
      "だから、Oを通りABに平行な直線の上にPがあればよい。",
      "ABの傾きは2なので、Oを通る平行な直線は$y=2x$（図の点線）。",
      "Pは$y=x^2$と$y=2x$の交点。$x^2=2x$ → $x^2−2x=0$ → $x(x−2)=0$ → $x=0$、2",
      "$x=0$は点Oなので、$x=2$。$y=2^2=4$。",
    ]),
  ], [imgP("s3k_o2_ans.png", 260)], { right: 200 }),
  ...AT("（3）", "Q(0, 6)", [
    "△QABも、$y$軸で△QACと△QBCに分けると、底辺はCQ、高さは1と3。",
    "△QAB＝$CQ×(1+3)÷2=CQ×2$。これが6になればよいので、CQ＝3。",
    "C(0, 3)から上へ3進むと(0, 6)、下へ3進むと(0, 0)。(0, 0)は原点Oなので、Q(0, 6)。",
    "【別の考え方】OC＝3なので、Cをはさんで反対側に同じ長さだけとる、と考えてもよい。",
  ]),

  new d.Paragraph({ children: [new d.PageBreak()] }),
  qHead(3, "★平行四辺形と相似", "", KH),
  row2(CW - 4600, [
    ...AT("（1）", "下の証明", []),
    frame("【証明】", [
      T("△AEFと△CBFで、"),
      T("AD//BCより、錯角は等しいから、"),
      T("∠EAF＝∠BCF……①"),
      T("∠AEF＝∠CBF……②"),
      T("①、②より、2組の角がそれぞれ等しいので、△AEF∽△CBF", { after: 0 }),
    ]),
    T("・②のかわりに「対頂角は等しいから、∠AFE＝∠CFB」を使ってもよい。", { before: 60 }),
    T("・平行四辺形なので、向かいあう辺ADとBCは平行。「AD//BCより」を必ず書く。"),
    T("・この形はチョウチョ型。"),
  ], [imgP("s3k_o3_ans.png", 300)], { right: 200 }),
  T("【相似比を求める】AE：ED＝2：1なので、AEを②、EDを①とすると、ADは③。", { before: 80 }),
  T("平行四辺形なので、BC＝AD＝③。だから、AE：CB＝②：③で、相似比は2：3。"),
  ...AT("（2）", "6cm", [
    "AFとCFが対応するので、AF：CF＝2：3。",
    "【比の式で解く】AF：AC＝2：(2＋3)＝2：5。$AF:15=2:5$ → $5×AF=30$ → AF＝6",
    "【図で何倍か考える】ACは⑤で15cm。⑤を15cmにするには×3。AFは②なので、$2×3=6$",
  ]),
  ...AT("（3）", "6cm", [
    "EFとBFが対応するので、EF：BF＝2：3。",
    "【比の式で解く】BF：BE＝3：(2＋3)＝3：5。$BF:10=3:5$ → $5×BF=30$ → BF＝6",
    "【図で何倍か考える】BEは⑤で10cm。⑤を10cmにするには×2。BFは③なので、$3×2=6$",
  ]),
  T("ACやBEは「2＋3＝5」に分かれている。全体を⑤と考えるのがポイント。", { before: 60 }),
];

L.save(`${OUT}/第3回_授業プリント②_解答解説.docx`, [sec("中3 第3回 授業プリント② 解答解説", kai)]).then(() => console.log("ok"));

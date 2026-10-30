// 表紙（7回分まとめて1枚）
const L = require("./lib");
const { d, P, space, imgP, CW } = L;
const OUT = require("path").join(__dirname, "..");
const rows = [
  ["回", "日付", "内容", "宿題"],
  ["第1回", "10/30（金）", "総ざらい①　連立方程式＋一次関数の前半", "多め（B4×2）"],
  ["第2回", "11/4（水）", "総ざらい②　第1回と同じ範囲の総合問題", "ふつう（B4×1）"],
  ["第3回", "11/6（金）", "一次関数の後半だけ（ダイヤグラム・動点・利用）", "ふつう（B4×1）"],
  ["第4回", "11/9（月）", "総ざらい③　角と平行線・多角形の角を追加", "多め（B4×2）"],
  ["第5回", "11/13（金）", "本番形式①　範囲全部", "ほぼなし"],
  ["第6回", "11/14（土）", "本番形式②　範囲全部", "ふつう（B4×1）"],
  ["第7回", "11/17（火）", "直前　本番形式③＋ミスの総点検", "なし（直しの見直し）"],
];
const W = [1500, 2200, CW - 1500 - 2200 - 3300, 3300];
const table = new d.Table({
  width: { size: CW, type: d.WidthType.DXA }, columnWidths: W,
  rows: rows.map((r, k) => new d.TableRow({ height: { value: 620, rule: d.HeightRule.ATLEAST }, children: r.map((t, i) => new d.TableCell({
    borders: L.BOX, width: { size: W[i], type: d.WidthType.DXA }, verticalAlign: d.VerticalAlign.CENTER, margins: { left: 120, right: 120 },
    shading: k === 0 ? { type: d.ShadingType.CLEAR, fill: "D9D9D9", color: "auto" } : undefined,
    children: [P(t, { after: 0, size: 24, font: k === 0 ? L.GOT : undefined, bold: k === 0, align: i === 2 ? undefined : d.AlignmentType.CENTER })],
  })) })),
});
const box = L.frame("＜この対策プリントの使い方＞", [
  P("1　授業プリント①＜基本＞は、解き終わったら提出。先生が採点して返します。", { size: 24 }),
  P("2　授業プリント②＜応用＞は、大問ごとに時間を区切って解き、前で解説を聞きます。", { size: 24 }),
  P("3　まちがえた問題は、直しノートを作って提出しましょう。", { size: 24 }),
  P("4　宿題は、解答解説で丸つけをしてから、直しノートを作りましょう。", { size: 24 }),
  P("5　★は100点をねらう問題です。できたら自信を持ってOK！", { size: 24, after: 0 }),
]);
const children = [
  space(1400),
  imgP("logo_gray.png", 560),
  space(900),
  P("中学2年　数学", { align: d.AlignmentType.CENTER, font: L.GOT, bold: true, size: 44 }),
  P("2学期期末テスト対策", { align: d.AlignmentType.CENTER, font: L.GOT, bold: true, size: 64, before: 120 }),
  P("★ 定期テストそっくり問題　全7回 ★", { align: d.AlignmentType.CENTER, font: L.GOT, bold: true, size: 40, before: 200 }),
  P("テスト本番　11月18日（水）", { align: d.AlignmentType.CENTER, size: 32, before: 300, after: 600 }),
  table,
  space(500),
  box,
  space(900),
  P("2年　　　組　　　番　　氏名", { align: d.AlignmentType.CENTER, size: 32, border: undefined }),
];
L.save(`${OUT}/00_表紙.docx`, [{ properties: L.sectionProps, children }]).then(() => console.log("ok"));

// 数学型の表紙（2回分まとめて1枚）
const L = require("./lib");
const { d, P, space, imgP, CW } = L;
const OUT = require("path").join(__dirname, "..");
const V = process.argv[2] || "_1030修正2版";

const rows = [
  ["回", "日付", "内容（学校ワーク p.22～47）", "宿題"],
  ["第1回", "　月　日（　）", "第1章　物質の性質（金属・密度・ガスバーナー・有機物）\n第2章　気体の性質（発生方法・性質・集め方）", "B4両面"],
  ["第2回", "　月　日（　）", "第3章　水溶液の性質\n（水溶液・ろ過・濃度・純粋な物質と混合物・溶解度・再結晶）", "B4両面"],
];
const W = [1300, 2200, CW - 1300 - 2200 - 1700, 1700];
const table = new d.Table({
  width: { size: CW, type: d.WidthType.DXA }, columnWidths: W,
  rows: rows.map((r, k) => new d.TableRow({ height: { value: 700, rule: d.HeightRule.ATLEAST }, children: r.map((t, i) => new d.TableCell({
    borders: L.BOX, width: { size: W[i], type: d.WidthType.DXA }, verticalAlign: d.VerticalAlign.CENTER, margins: { left: 120, right: 120, top: 40, bottom: 40 },
    shading: k === 0 ? { type: d.ShadingType.CLEAR, fill: "D9D9D9", color: "auto" } : undefined,
    children: t.split("\n").map(s => P(s, { after: 0, size: 24, font: k === 0 ? L.GOT : undefined, bold: k === 0, align: i === 2 && k > 0 ? undefined : d.AlignmentType.CENTER })),
  })) })),
});
const box = L.frame("＜この対策プリントの使い方＞", [
  P("1　授業プリント①＜基本＞は、解き終わったら提出。先生が採点して返します。", { size: 24 }),
  P("2　授業プリント②＜応用＞は、大問ごとに時間を区切って解き、前で解説を聞きます。", { size: 24 }),
  P("3　まちがえた問題は、直しノートを作って提出しましょう。", { size: 24 }),
  P("4　宿題は、解答解説で丸つけをしてから、直しノートを作りましょう。", { size: 24 }),
  P("5　計算は式も書き、答えには単位も書きます。記述は「～から。」「～ため。」で終わらせます。", { size: 24 }),
  P("6　★は100点をねらう問題です。できたら自信を持ってOK！", { size: 24, after: 0 }),
]);
const children = [
  space(1400),
  imgP("logo_gray.png", 560),
  space(900),
  P("中学1年　理科", { align: d.AlignmentType.CENTER, font: L.GOT, bold: true, size: 44 }),
  P("2学期期末テスト対策", { align: d.AlignmentType.CENTER, font: L.GOT, bold: true, size: 64, before: 120 }),
  P("★ 単元2　身のまわりの物質　全2回 ★", { align: d.AlignmentType.CENTER, font: L.GOT, bold: true, size: 40, before: 200 }),
  P("テスト本番　　月　　日（　）", { align: d.AlignmentType.CENTER, size: 32, before: 300, after: 600 }),
  table,
  space(500),
  box,
  space(900),
  P("1年　　　組　　　番　　氏名", { align: d.AlignmentType.CENTER, size: 32 }),
];
L.save(`${OUT}/数学型_00_表紙${V}.docx`, [{ properties: L.sectionProps, children }]).then(() => console.log("ok"));

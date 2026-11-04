// 授業プリント①の点数を控える表（A4縦）。氏名は先生が手書きで記入する
const d = require("docx");
const fs = require("fs");
const path = require("path");
const MIN = "MS P明朝", GOT = "MS Pゴシック";
const LOGO = fs.readFileSync(path.join(__dirname, "../math3-kimatsu/src/img/logo_gray.png"));

const LINE = { style: d.BorderStyle.SINGLE, size: 6, color: "000000" };
const THICK = { style: d.BorderStyle.SINGLE, size: 12, color: "000000" };
const B = { top: LINE, bottom: LINE, left: LINE, right: LINE };
const txt = (t, o = {}) => new d.Paragraph({ alignment: o.align ?? d.AlignmentType.CENTER, spacing: { before: 0, after: 0 },
  children: [new d.TextRun({ text: t, font: o.font || MIN, size: o.size || 20, bold: o.bold })] });

function sheet(title, sessions, n) {
  const W = 11906 - 1000 * 2;                // A4 の本文の幅
  const wNo = 450, wName = 1900, wGoal = 650, wNote = 900;
  const wS = Math.floor((W - wNo - wName - wGoal - wNote) / sessions.length);
  const widths = [wNo, wName, wGoal, ...sessions.map(() => wS), W - wNo - wName - wGoal - wS * sessions.length];
  const gray = { type: d.ShadingType.CLEAR, fill: "D9D9D9", color: "auto" };
  const c = (kids, w, o = {}) => new d.TableCell({ width: { size: w, type: d.WidthType.DXA }, borders: o.borders || B, shading: o.shade ? gray : undefined,
    verticalAlign: d.VerticalAlign.CENTER, margins: { left: 30, right: 30 }, children: kids });
  const head = new d.TableRow({ tableHeader: true, height: { value: 820, rule: d.HeightRule.ATLEAST }, children: [
    c([txt("No.", { font: GOT, bold: true })], widths[0], { shade: true }),
    c([txt("氏名", { font: GOT, bold: true })], widths[1], { shade: true }),
    c([txt("目標", { font: GOT, bold: true, size: 18 }), txt("（点）", { size: 14 })], widths[2], { shade: true }),
    ...sessions.map(([no, day, what], i) => c([txt(no, { font: GOT, bold: true, size: 18 }), txt(day, { size: 14 }), txt(what, { size: 12 })], widths[3 + i], { shade: true })),
    c([txt("メモ", { font: GOT, bold: true })], widths[widths.length - 1], { shade: true }),
  ] });
  const rows = [];
  for (let i = 1; i <= n; i++) {
    rows.push(new d.TableRow({ height: { value: 650, rule: d.HeightRule.EXACT }, children: [
      c([txt(String(i))], widths[0]), c([txt("")], widths[1]), c([txt("")], widths[2]),
      ...sessions.map((_, k) => c([txt("／50", { size: 14, align: d.AlignmentType.RIGHT })], widths[3 + k])),
      c([txt("")], widths[widths.length - 1]),
    ] }));
  }
  const sumRow = (label) => new d.TableRow({ height: { value: 650, rule: d.HeightRule.EXACT }, children: [
    c([txt(label, { font: GOT, bold: true })], widths[0] + widths[1] + widths[2], { shade: true }),
    ...sessions.map((_, k) => c([txt("")], widths[3 + k])), c([txt("")], widths[widths.length - 1]),
  ] });
  const mk = (label) => { const r = sumRow(label); return r; };
  const table = new d.Table({ width: { size: W, type: d.WidthType.DXA }, columnWidths: widths, rows: [head, ...rows,
    new d.TableRow({ height: { value: 650, rule: d.HeightRule.EXACT }, children: [
      new d.TableCell({ columnSpan: 3, width: { size: widths[0] + widths[1] + widths[2], type: d.WidthType.DXA }, borders: { ...B, top: THICK }, shading: gray, verticalAlign: d.VerticalAlign.CENTER, children: [txt("平均点", { font: GOT, bold: true })] }),
      ...sessions.map((_, k) => c([txt("")], widths[3 + k], { borders: { ...B, top: THICK } })), c([txt("")], widths[widths.length - 1], { borders: { ...B, top: THICK } }),
    ] }),
    new d.TableRow({ height: { value: 650, rule: d.HeightRule.EXACT }, children: [
      new d.TableCell({ columnSpan: 3, width: { size: widths[0] + widths[1] + widths[2], type: d.WidthType.DXA }, borders: B, shading: gray, verticalAlign: d.VerticalAlign.CENTER, children: [txt("40点未満の人数", { font: GOT, bold: true, size: 18 })] }),
      ...sessions.map((_, k) => c([txt("")], widths[3 + k])), c([txt("")], widths[widths.length - 1]),
    ] }),
  ] });
  return [
    new d.Paragraph({ alignment: d.AlignmentType.RIGHT, spacing: { after: 0 }, children: [new d.ImageRun({ type: "png", data: LOGO, transformation: { width: 110, height: 38 } })] }),
    new d.Paragraph({ spacing: { before: 0, after: 80 }, border: { bottom: { style: d.BorderStyle.SINGLE, size: 18, color: "000000", space: 2 } },
      children: [new d.TextRun({ text: title, font: GOT, bold: true, size: 30 })] }),
    new d.Paragraph({ spacing: { after: 120 }, children: [new d.TextRun({ text: "授業プリント①＜基本＞（50点）の点数を記入します。欠席は「欠」と書きます。", font: MIN, size: 18 })] }),
    table,
  ];
}

const M2 = [["第1回", "10/30（金）", "総ざらい①"], ["第2回", "11/4（水）", "総ざらい②"], ["第3回", "11/6（金）", "一次関数"], ["第4回", "11/9（月）", "総ざらい③"], ["第5回", "11/13（金）", "本番形式①"], ["第6回", "11/14（土）", "本番形式②"], ["第7回", "11/17（火）", "本番形式③"]];
const M3 = [["第1回", "11/2（月）", "総ざらい①"], ["第2回", "11/4（水）", "関数"], ["第3回", "11/6（金）", "相似"], ["第4回", "11/7（土）", "大問特訓"], ["第5回", "11/12（木）", "本番形式①"], ["第6回", "11/14（土）", "本番形式②"], ["第7回", "11/18（水）", "本番形式③"]];
const props = { page: { size: { width: 11906, height: 16838 }, margin: { top: 800, bottom: 800, left: 1000, right: 1000 } } };
const save = (file, kids) => d.Packer.toBuffer(new d.Document({ styles: { default: { document: { run: { font: MIN, size: 20 } } } }, sections: [{ properties: props, children: kids }] })).then(b => fs.writeFileSync(path.join(__dirname, file), b));
Promise.all([
  save("中2_授業プリント①_点数記録表.docx", sheet("中2　2学期期末対策　授業プリント①　点数記録表", M2, 17)),
  save("中3_授業プリント①_点数記録表.docx", sheet("中3　2学期期末対策　授業プリント①　点数記録表", M3, 17)),
]).then(() => console.log("ok"));

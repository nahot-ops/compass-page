// 数学 定期テスト対策プリント（B4・モノトーン）共通部品
const d = require("docx");
const fs = require("fs");
const path = require("path");

const MIN = "MS P明朝";
const GOT = "MS Pゴシック";
const IMG = path.join(__dirname, "img");

// B4 portrait（DXA）
const PAGE_W = 14570, PAGE_H = 20636;
const MARGIN = { top: 850, bottom: 750, left: 950, right: 950, header: 450, footer: 400 };
const CW = PAGE_W - MARGIN.left - MARGIN.right; // 本文の幅

const NONE = { style: d.BorderStyle.NONE, size: 0, color: "FFFFFF" };
const NOB = { top: NONE, bottom: NONE, left: NONE, right: NONE };
const LINE = { style: d.BorderStyle.SINGLE, size: 8, color: "000000" };
const BOX = { top: LINE, bottom: LINE, left: LINE, right: LINE };

// ---------- 数式（OMML） ----------
const NS = 'xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"';
const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const mr = t => `<m:r><m:t xml:space="preserve">${esc(t)}</m:t></m:r>`;
const mrp = t => `<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t xml:space="preserve">${esc(t)}</m:t></m:r>`;
// 数式の中身：{分子/分母} を分数に、[…] は立体（ふつうの文字）
function mbody(s) {
  let out = "", i = 0;
  while (i < s.length) {
    const c = s[i];
    if (c === "{") {
      let depth = 1, j = i + 1;
      while (depth) { if (s[j] === "{") depth++; if (s[j] === "}") depth--; j++; }
      const inner = s.slice(i + 1, j - 1);
      const k = inner.indexOf("/");
      out += `<m:f><m:num>${mbody(inner.slice(0, k))}</m:num><m:den>${mbody(inner.slice(k + 1))}</m:den></m:f>`;
      i = j;
    } else if (c === "[") {
      const j = s.indexOf("]", i);
      out += mrp(s.slice(i + 1, j)); i = j + 1;
    } else {
      let j = i;
      while (j < s.length && !"{[".includes(s[j])) j++;
      out += mr(s.slice(i, j)); i = j;
    }
  }
  return out;
}
const omath = inner => d.ImportedXmlComponent.fromXmlString(`<m:oMath ${NS}>${inner}</m:oMath>`).root[0];
const M = s => omath(mbody(s));
// 連立方程式 ｛ 2行
const SYS = (rows, tags = true) => omath(
  `<m:d><m:dPr><m:begChr m:val="{"/><m:endChr m:val=""/></m:dPr><m:e><m:eqArr>` +
  rows.map((r, i) => `<m:e>${mbody(r)}${tags ? mrp("　……" + "①②③"[i]) : ""}</m:e>`).join("") +
  `</m:eqArr></m:e></m:d>`);

// ---------- 文字 ----------
// 文字列中の $…$ を数式に。**…** を太字に。
function runs(str, o = {}) {
  const out = [];
  const font = o.font || MIN;
  const size = o.size || 22;
  str.split(/(\*\*[^*]*\*\*)/).forEach(part => {
    if (!part) return;
    const bold = part.startsWith("**") ? true : o.bold;
    if (part.startsWith("**")) part = part.slice(2, -2);
    part.split(/(\$[^$]*\$)/).forEach(seg => {
      if (!seg) return;
      if (seg.startsWith("$")) out.push(M(seg.slice(1, -1)));
      else out.push(new d.TextRun({ text: seg, font, size, bold }));
    });
  });
  return out;
}
function P(str, o = {}) {
  const kids = typeof str === "string" ? runs(str, o) : str;
  return new d.Paragraph({
    children: kids,
    alignment: o.align,
    indent: o.indent ? { left: o.indent, hanging: o.hanging || 0 } : undefined,
    spacing: { before: o.before || 0, after: o.after ?? 40, line: o.line || 300, lineRule: d.LineRuleType.AT_LEAST },
    keepNext: o.keepNext,
    pageBreakBefore: o.pageBreakBefore,
  });
}
const Gothic = (str, o = {}) => P(str, { ...o, font: GOT, bold: true, size: o.size || 26 });
const space = h => new d.Paragraph({ children: [], spacing: { before: 0, after: 0, line: h, lineRule: d.LineRuleType.EXACT } });

function img(file, w) {
  const buf = fs.readFileSync(path.join(IMG, file));
  const sz = require("child_process").execSync(`python3 -c "from PIL import Image;i=Image.open('${path.join(IMG, file)}');print(i.size[0],i.size[1])"`).toString().trim().split(" ").map(Number);
  return new d.ImageRun({ type: "png", data: buf, transformation: { width: w, height: Math.round(w * sz[1] / sz[0]) } });
}
const imgP = (file, w, align = d.AlignmentType.CENTER) => new d.Paragraph({ children: [img(file, w)], alignment: align, spacing: { before: 0, after: 0 } });

// ---------- 枠 ----------
// 解答の枠（右寄せ）
function ansBox(text, w = 3400, h = 560) {
  return new d.Table({
    alignment: d.AlignmentType.RIGHT,
    width: { size: w, type: d.WidthType.DXA }, columnWidths: [w],
    rows: [new d.TableRow({
      height: { value: h, rule: d.HeightRule.EXACT },
      children: [new d.TableCell({
        borders: BOX, width: { size: w, type: d.WidthType.DXA }, verticalAlign: d.VerticalAlign.CENTER,
        margins: { left: 100, right: 100 },
        children: [P(text, { after: 0 })],
      })],
    })],
  });
}
// 問題のマス目（cols 列）。cell = {q:[段落…], work:高さ, ans:"…", ansW}
function qgrid(cells, cols, o = {}) {
  const w = Math.floor((o.width || CW) / cols);
  const rows = [];
  for (let i = 0; i < cells.length; i += cols) {
    const rowCells = [];
    for (let j = 0; j < cols; j++) {
      const c = cells[i + j];
      const kids = c ? [...c.q, ...(c.work ? [space(c.work)] : []), ...(c.ans !== undefined ? [ansBox(c.ans, c.ansW || Math.min(w - 300, 3600), c.ansH)] : []), space(120)] : [P("")];
      rowCells.push(new d.TableCell({ borders: NOB, width: { size: w, type: d.WidthType.DXA }, margins: { left: 60, right: 120 }, children: kids }));
    }
    rows.push(new d.TableRow({ children: rowCells, cantSplit: true }));
  }
  return new d.Table({ width: { size: w * cols, type: d.WidthType.DXA }, columnWidths: Array(cols).fill(w), rows, borders: d.TableBorders.NONE });
}
// 見出し帯（黒線で囲む）
function bandTitle(left, right) {
  return new d.Table({
    width: { size: CW, type: d.WidthType.DXA }, columnWidths: [CW],
    rows: [new d.TableRow({ children: [new d.TableCell({
      borders: { top: { style: d.BorderStyle.SINGLE, size: 18, color: "000000" }, bottom: { style: d.BorderStyle.SINGLE, size: 18, color: "000000" }, left: NONE, right: NONE },
      width: { size: CW, type: d.WidthType.DXA }, margins: { top: 60, bottom: 60, left: 80, right: 80 },
      children: [new d.Paragraph({ children: [...runs(left, { font: GOT, bold: true, size: 30 }), new d.TextRun({ children: [new d.PositionalTab({ alignment: d.PositionalTabAlignment.RIGHT, relativeTo: d.PositionalTabRelativeTo.MARGIN, leader: d.PositionalTabLeader.NONE })] }), ...runs(right, { size: 22 })], spacing: { after: 0 } })],
    })] })],
  });
}
// 大問の見出し ＜1＞ …（目安〇分）
const qHead = (no, text, note = "") => new d.Paragraph({
  children: [...runs(`＜${no}＞`, { font: GOT, bold: true, size: 26 }), ...runs("　" + text, { font: GOT, size: 23, bold: true }),
    ...(note ? [new d.TextRun({ children: [new d.PositionalTab({ alignment: d.PositionalTabAlignment.RIGHT, relativeTo: d.PositionalTabRelativeTo.MARGIN, leader: d.PositionalTabLeader.NONE })] }), ...runs(note, { size: 20 })] : [])],
  spacing: { before: 120, after: 60 }, keepNext: true,
  border: { bottom: { style: d.BorderStyle.SINGLE, size: 6, color: "000000", space: 2 } },
});
// 囲み（黒枠・グレー見出し）
function frame(title, kids, o = {}) {
  return new d.Table({
    width: { size: o.w || CW, type: d.WidthType.DXA }, columnWidths: [o.w || CW],
    rows: [
      ...(title ? [new d.TableRow({ children: [new d.TableCell({ borders: BOX, shading: { type: d.ShadingType.CLEAR, fill: "D9D9D9", color: "auto" }, width: { size: o.w || CW, type: d.WidthType.DXA }, margins: { left: 120, top: 40, bottom: 40 }, children: [P(title, { font: GOT, bold: true, size: 22, after: 0 })] })] })] : []),
      new d.TableRow({ children: [new d.TableCell({ borders: BOX, width: { size: o.w || CW, type: d.WidthType.DXA }, margins: { left: 160, right: 160, top: 80, bottom: 80 }, children: kids })] }),
    ],
  });
}

// ---------- ページ設定 ----------
function header() {
  return new d.Header({ children: [new d.Paragraph({ children: [img("logo_gray.png", 120)], alignment: d.AlignmentType.RIGHT, spacing: { after: 0 } })] });
}
function footer(label) {
  return new d.Footer({ children: [new d.Paragraph({
    alignment: d.AlignmentType.CENTER, spacing: { after: 0 },
    children: [new d.TextRun({ text: label + "　", font: MIN, size: 18 }), new d.TextRun({ children: [d.PageNumber.CURRENT], font: MIN, size: 18 }), new d.TextRun({ text: "／", font: MIN, size: 18 }), new d.TextRun({ children: [d.PageNumber.TOTAL_PAGES], font: MIN, size: 18 })],
  })] });
}
const sectionProps = { page: { size: { width: PAGE_W, height: PAGE_H }, margin: MARGIN } };

function save(file, sections) {
  const doc = new d.Document({
    styles: { default: { document: { run: { font: MIN, size: 22 } } } },
    sections,
  });
  return d.Packer.toBuffer(doc).then(b => fs.writeFileSync(file, b));
}

module.exports = { d, MIN, GOT, CW, NOB, BOX, LINE, NONE, M, SYS, runs, P, Gothic, space, img, imgP, ansBox, qgrid, bandTitle, qHead, frame, header, footer, sectionProps, save };

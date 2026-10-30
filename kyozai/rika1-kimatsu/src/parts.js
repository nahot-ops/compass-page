// 理科の教材で使う部品（lib.js の上に積む）
const L = require("./lib");
const { d, P, space, ansBox, CW } = L;

const NAME = "1年　　組　　番　氏名　　　　　　　　　　";
const KAKUNIN = "〇かどうかわからない場合は、適当に〇をつけずに必ず先生に確認しましょう";

// 表が2つ続くとWordで1つにくっつくので、間に細い空き段落を入れる
function sep(kids) {
  const out = [];
  kids.forEach((k, i) => {
    if (i > 0 && k instanceof d.Table && kids[i - 1] instanceof d.Table) out.push(space(20));
    out.push(k);
  });
  return out;
}

// 数学型の1区切り（ヘッダーにグレーのロゴ、フッターに「第1回 授業プリント 1／2」）
const sec = (label, children) => ({ properties: L.sectionProps, headers: { default: L.header() }, footers: { default: L.footer(label) }, children: sep(children) });

// 一問一答の表：左に問題、右に解答の枠。cols=2 なら左右に2列並べる
function termTable(items, o = {}) {
  const W = o.width || CW, cols = o.cols || 1;
  const aw = o.ansW || 2600, gap = 200;
  const qw = Math.floor(W / cols) - aw - gap;
  const widths = [];
  for (let c = 0; c < cols; c++) widths.push(qw, aw, gap);
  widths.pop();
  const rows = [];
  for (let i = 0; i < items.length; i += cols) {
    const cells = [];
    for (let c = 0; c < cols; c++) {
      const it = items[i + c];
      cells.push(new d.TableCell({ borders: L.NOB, width: { size: qw, type: d.WidthType.DXA }, verticalAlign: d.VerticalAlign.CENTER, margins: { right: 80 },
        children: [P(it ? it[0] : "", { after: 0, size: o.size })] }));
      cells.push(new d.TableCell({ borders: it ? L.BOX : L.NOB, width: { size: aw, type: d.WidthType.DXA }, verticalAlign: d.VerticalAlign.CENTER, margins: { left: 80, right: 80 },
        children: [P(it && it[1] ? it[1] : "", { after: 0, size: o.size, align: d.AlignmentType.RIGHT })] }));
      if (c < cols - 1) cells.push(new d.TableCell({ borders: L.NOB, width: { size: gap, type: d.WidthType.DXA }, children: [P("")] }));
    }
    rows.push(new d.TableRow({ height: { value: o.h || 520, rule: d.HeightRule.ATLEAST }, cantSplit: true, children: cells }));
  }
  return new d.Table({ width: { size: W, type: d.WidthType.DXA }, columnWidths: widths, rows, borders: d.TableBorders.NONE });
}

// 採点用の解答（答えと配点だけ）
function keyTable(rows, W = CW) {
  const w = [1700, W - 1700 - 1300, 1300];
  const cell = (t, i, head) => new d.TableCell({ borders: L.BOX, width: { size: w[i], type: d.WidthType.DXA }, margins: { left: 100, right: 100, top: 30, bottom: 30 },
    shading: head ? { type: d.ShadingType.CLEAR, fill: "D9D9D9", color: "auto" } : undefined,
    children: [P(t, { after: 0, font: head ? L.GOT : undefined, bold: head, align: i === 2 ? d.AlignmentType.CENTER : undefined })] });
  return new d.Table({ width: { size: W, type: d.WidthType.DXA }, columnWidths: w,
    rows: [["番号", "答え", "配点"], ...rows].map((r, k) => new d.TableRow({ cantSplit: true, children: r.map((t, i) => cell(t, i, k === 0)) })) });
}

// 資料の表（見出し行はグレー）
function dataTable(rows, widths, o = {}) {
  const W = widths.reduce((a, b) => a + b, 0);
  return new d.Table({
    alignment: o.align, width: { size: W, type: d.WidthType.DXA }, columnWidths: widths,
    rows: rows.map((r, k) => new d.TableRow({ cantSplit: true, children: r.map((t, i) => new d.TableCell({
      borders: L.BOX, width: { size: widths[i], type: d.WidthType.DXA }, verticalAlign: d.VerticalAlign.CENTER, margins: { left: 70, right: 70, top: 20, bottom: 20 },
      shading: (k === 0 && !o.noHead) || (o.headCol && i === 0) ? { type: d.ShadingType.CLEAR, fill: "D9D9D9", color: "auto" } : undefined,
      children: (Array.isArray(t) ? t : [t]).map(s => P(s, { after: 0, size: o.size, align: o.allLeft || (o.left && i > 0) ? undefined : d.AlignmentType.CENTER })),
    })) })),
  });
}

// 左に文、右に図（または表）
function side(leftKids, rightKids, rightW, W = CW, split = false) {
  return new d.Table({
    width: { size: W, type: d.WidthType.DXA }, columnWidths: [W - rightW, rightW], borders: d.TableBorders.NONE,
    rows: [new d.TableRow({ cantSplit: !split, children: [
      new d.TableCell({ borders: L.NOB, width: { size: W - rightW, type: d.WidthType.DXA }, margins: { right: 200 }, children: sep(leftKids) }),
      new d.TableCell({ borders: L.NOB, width: { size: rightW, type: d.WidthType.DXA }, children: sep(rightKids) }),
    ] })],
  });
}

// 解答解説の1問分：「（1）答え」＋解説の行
function ex(no, ans, lines = [], o = {}) {
  return [
    P(`${no}　**${ans}**`, { before: 60, after: 20, size: o.size }),
    ...lines.map(t => P(t, { indent: o.indent || 400, after: 20, size: o.size })),
  ];
}

// 横に並んだ解答の枠。cells = [[ラベル, 幅], …]（ラベルは枠の左上に小さく）
function ansRow(cells, h = 640) {
  const W = cells.reduce((a, c) => a + c[1], 0) + 160 * (cells.length - 1);
  const widths = []; cells.forEach((c, i) => { widths.push(c[1]); if (i < cells.length - 1) widths.push(160); });
  const kids = []; cells.forEach((c, i) => {
    kids.push(new d.TableCell({ borders: L.BOX, width: { size: c[1], type: d.WidthType.DXA }, margins: { left: 80, right: 80 }, verticalAlign: d.VerticalAlign.CENTER,
      children: [P(c[0], { after: 0, size: 18, align: /^(g|cm³|g\/cm³|％|℃)$/.test(c[0]) ? d.AlignmentType.RIGHT : undefined })] }));
    if (i < cells.length - 1) kids.push(new d.TableCell({ borders: L.NOB, width: { size: 160, type: d.WidthType.DXA }, children: [P("")] }));
  });
  return new d.Table({ width: { size: W, type: d.WidthType.DXA }, columnWidths: widths, borders: d.TableBorders.NONE,
    rows: [new d.TableRow({ height: { value: h, rule: d.HeightRule.EXACT }, cantSplit: true, children: kids })] });
}

const caution = (size) => P(`**${KAKUNIN}**`, { after: 120, size, font: L.GOT });

module.exports = { NAME, KAKUNIN, sep, sec, ansRow, termTable, keyTable, dataTable, side, ex, caution };

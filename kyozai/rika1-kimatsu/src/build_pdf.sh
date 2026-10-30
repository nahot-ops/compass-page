#!/bin/bash
# 確認用PDFとPNGを作る：./build_pdf.sh 出力先 docx...
OUTD=$1; shift
mkdir -p "$OUTD"
for f in "$@"; do
  soffice --headless --convert-to pdf --outdir "$OUTD" "$f" >/dev/null 2>&1
  b=$(basename "$f" .docx)
  pdftoppm -r 45 -png "$OUTD/$b.pdf" "$OUTD/$b"
  echo "$b: $(pdfinfo "$OUTD/$b.pdf" | grep Pages)"
done

#!/usr/bin/env bash
# Render the report to PDF (via Typst) and DOCX. Run from anywhere.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p dist

inputs=(metadata.yaml sections/*.md)

# PNG copies of the SVG figures for the DOCX (pandoc cannot embed SVG without rsvg-convert).
for svg in figures/*.svg; do
  name=$(basename "$svg" .svg)
  printf '#set page(width: auto, height: auto, margin: 0pt)\n#image("/%s")\n' "$svg" > .fig.typ
  typst compile --root . --ppi 200 .fig.typ "figures/$name.png"
done
rm -f .fig.typ

pandoc "${inputs[@]}" \
  --from markdown --columns=10000 \
  --to typst --standalone \
  -V template=/style/conf.typ \
  --default-image-extension=svg \
  --resource-path=.:figures \
  -o .build.typ

typst compile --root . .build.typ dist/helm-report.pdf

pandoc "${inputs[@]}" \
  --from markdown --columns=10000 \
  --resource-path=.:figures \
  --default-image-extension=png \
  --toc --toc-depth=2 \
  -o dist/helm-report.docx

echo "Built dist/helm-report.pdf and dist/helm-report.docx"

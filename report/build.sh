#!/usr/bin/env bash
# Render the report to PDF (via Typst) and DOCX. Run from anywhere.
#   ./build.sh        English  -> dist/helm-report.{pdf,docx}
#   ./build.sh vi     Vietnamese -> dist/helm-report-vi.{pdf,docx}
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p dist

lang="${1:-en}"
case "$lang" in
  en) src=.; out=helm-report ;;
  vi) src=vi; out=helm-report-vi ;;
  *) echo "unknown language: $lang" >&2; exit 1 ;;
esac

inputs=("$src/metadata.yaml" "$src"/sections/*.md)

# PNG copies of the SVG figures for the DOCX (pandoc cannot embed SVG without rsvg-convert).
for svg in figures/*.svg figures/vi/*.svg; do
  [ -e "$svg" ] || continue
  printf '#set page(width: auto, height: auto, margin: 0pt)\n#image("/%s")\n' "$svg" > .fig.typ
  typst compile --root . --ppi 200 .fig.typ "${svg%.svg}.png"
done
rm -f .fig.typ

pandoc "${inputs[@]}" \
  --from markdown --columns=10000 \
  --to typst --standalone \
  --lua-filter=style/colwidths.lua \
  -V template=/style/conf.typ \
  --default-image-extension=svg \
  --resource-path=. \
  -o .build.typ

typst compile --root . .build.typ "dist/$out.pdf"

pandoc "${inputs[@]}" \
  --from markdown --columns=10000 \
  --resource-path=. \
  --default-image-extension=png \
  --lua-filter=style/colwidths.lua \
  --toc --toc-depth=2 \
  -o "dist/$out.docx"

echo "Built dist/$out.pdf and dist/$out.docx"

#!/usr/bin/env bash
# Render the report to PDF (via Typst) and DOCX. Run from anywhere.
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p dist

pandoc helm-report.md \
  --from markdown \
  --to typst --standalone \
  -V template=/style/conf.typ \
  --resource-path=.:figures \
  -o dist/helm-report.typ

typst compile --root . dist/helm-report.typ dist/helm-report.pdf

pandoc helm-report.md \
  --from markdown \
  --resource-path=.:figures \
  --toc --toc-depth=2 \
  -o dist/helm-report.docx

echo "Built dist/helm-report.pdf and dist/helm-report.docx"

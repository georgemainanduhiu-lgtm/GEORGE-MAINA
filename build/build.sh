#!/usr/bin/env bash
# Build Kindle-ready files from the Markdown manuscript.
#   dist/soccer-heroes-who-never-gave-up.epub  -> upload to KDP (recommended)
#   dist/soccer-heroes-who-never-gave-up.docx  -> editable Word version (also accepted by KDP)
# Requires: pandoc (3.x), python3 with Pillow and python-docx.
set -euo pipefail
cd "$(dirname "$0")/.."

NAME="soccer-heroes-who-never-gave-up"
mkdir -p dist

python3 build/make_cover.py dist/cover.jpg

# Reference DOCX: start each chapter (Heading 1) on a new page.
pandoc -o build/reference.docx --print-default-data-file reference.docx
python3 - <<'EOF'
from docx import Document
doc = Document("build/reference.docx")
next(s for s in doc.styles if s.name == "Heading 1").paragraph_format.page_break_before = True
doc.save("build/reference.docx")
EOF

pandoc build/metadata.yaml manuscript/*.md \
  -t epub3 -o "dist/$NAME.epub" \
  --toc --toc-depth=1 --split-level=1 \
  --css build/epub.css \
  --epub-cover-image dist/cover.jpg

pandoc build/metadata.yaml manuscript/*.md \
  -o "dist/$NAME.docx" \
  --toc --toc-depth=1 \
  --reference-doc build/reference.docx

echo "Word count (manuscript):"
cat manuscript/*.md | wc -w
ls -la dist

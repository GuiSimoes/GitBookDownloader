from pathlib import Path

# Pasta raiz do projeto
ROOT = Path(__file__).resolve().parent.parent

# Entradas
PDF_UNICO = ROOT / "Atendi Docs.pdf"
PASTA_PDFS = ROOT / "PDFs"
MAPA_PAGINAS = ROOT / "python" / "mapa_paginas.json"

# Saídas
OUTPUT = ROOT / "python" / "output"

OUTPUT.mkdir(exist_ok=True)

PDF_FINAL = OUTPUT / "Atendi Docs Final.pdf"
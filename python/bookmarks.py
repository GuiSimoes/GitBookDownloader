import json
import fitz

from config import ROOT, PDF_UNICO, PDF_FINAL

# Abre o PDF original
pdf = fitz.open(PDF_UNICO)

# Carrega o índice
with open(ROOT / "python" / "indice.json", "r", encoding="utf-8") as f:
    indice = json.load(f)

toc = []

nivel_anterior = 1

for item in indice:

    nivel = item["nivel"]

    # O PyMuPDF não permite pular níveis
    if nivel > nivel_anterior + 1:
        nivel = nivel_anterior + 1

    toc.append([
        nivel,
        item["titulo"],
        item["pagina"]
    ])

    nivel_anterior = nivel

print(f"Bookmarks encontrados: {len(toc)}")

# Aplica os bookmarks
pdf.set_toc(toc)

# Salva o novo PDF
print(f"Entrada : {PDF_UNICO}")
print(f"Saída   : {PDF_FINAL}")

pdf.save(PDF_FINAL)

pdf.close()

print(f"PDF criado com {len(toc)} bookmarks!")
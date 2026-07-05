from pathlib import Path
from pypdf import PdfReader
import json

PDFS = Path("../PDFs")

arquivos = sorted(PDFS.glob("*.pdf"))

mapa = []

pagina = 1

for arquivo in arquivos:

    reader = PdfReader(str(arquivo))
    paginas = len(reader.pages)

    titulo = arquivo.stem

    if " - " in titulo:
        titulo = titulo.split(" - ", 1)[1]

    mapa.append({
        "titulo": titulo,
        "pagina": pagina,
        "paginas": paginas
    })

    pagina += paginas

with open("mapa_paginas.json", "w", encoding="utf8") as f:
    json.dump(mapa, f, ensure_ascii=False, indent=4)

print(f"{len(mapa)} itens gravados.")
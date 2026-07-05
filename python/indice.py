import json
from pathlib import Path

# Caminho da raiz do projeto
BASE = Path(__file__).resolve().parent.parent

# Arquivos
menu_path = BASE / "menu.json"
mapa_path = BASE / "python" / "mapa_paginas.json"
saida_path = BASE / "python" / "indice.json"

# Carrega os arquivos
with open(menu_path, "r", encoding="utf-8") as f:
    menu = json.load(f)

with open(mapa_path, "r", encoding="utf-8") as f:
    mapa = json.load(f)

# Cria um índice pelo título
menu_por_titulo = {}

for item in menu:
    titulo = item["titulo"].strip()
    menu_por_titulo[titulo] = item

indice = []
nao_encontrados = []

for pagina in mapa:

    titulo = pagina["titulo"].strip()

    if titulo not in menu_por_titulo:
        nao_encontrados.append(titulo)
        continue

    indice.append({
        "titulo": titulo,
        "pagina": pagina["pagina"],
        "nivel": menu_por_titulo[titulo]["nivel"]
    })

# Salva indice.json
with open(saida_path, "w", encoding="utf-8") as f:
    json.dump(indice, f, indent=4, ensure_ascii=False)

print(f"\n✅ {len(indice)} itens gravados em indice.json")

if nao_encontrados:
    print(f"\n⚠ {len(nao_encontrados)} itens não encontrados:\n")

    for item in nao_encontrados:
        print("-", item)
else:
    print("\n✅ Todos os títulos foram encontrados.")
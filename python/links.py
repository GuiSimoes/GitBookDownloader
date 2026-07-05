import fitz

from config import PDF_FINAL

pdf = fitz.open(PDF_FINAL)

total = 0

for numero_pagina, pagina in enumerate(pdf, start=1):

    links = pagina.get_links()

    if not links:
        continue

    for link in links:

        if "uri" not in link:
            continue

        total += 1

        print(f"\n=== Link {total} ===")
        print(f"Página : {numero_pagina}")
        print(f"URI    : {repr(link['uri'])}")
        print(f"Dados  : {link}")

        if total >= 10:
            pdf.close()
            print(f"\nTotal parcial: {total}")
            exit()

pdf.close()

print(f"\nTotal de links: {total}")
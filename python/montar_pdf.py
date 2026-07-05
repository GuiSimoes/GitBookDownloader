import fitz

doc = fitz.open("../Atendi Docs.pdf")

print(f"PDF aberto com sucesso!")
print(f"Total de páginas: {doc.page_count}")

toc = doc.get_toc()

print(f"Bookmarks encontrados: {len(toc)}")

if toc:
    print(toc[:10])

doc.close()
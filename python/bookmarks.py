import fitz

from config import PDF_UNICO, PDF_FINAL

pdf = fitz.open(PDF_UNICO)

toc = [
    [1, "Atendi Docs", 1],
    [2, "Summary", 3],
    [2, "01. Empresa", 5],
    [3, "Cultura da Atendi", 6],
    [3, "FAQ Institucional da Atendi", 10],
]

pdf.set_toc(toc)

pdf.save(PDF_FINAL)

pdf.close()

print("PDF criado com bookmarks!")
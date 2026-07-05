const fs = require("fs");
const path = require("path");
const { PDFDocument } = require("pdf-lib");

(async () => {

    const pastaPDFs = path.join(__dirname, "PDFs");

    const arquivos = fs.readdirSync(pastaPDFs)
        .filter(a => a.endsWith(".pdf"))
        .sort();

    console.log(`${arquivos.length} PDFs encontrados.`);

    const pdfFinal = await PDFDocument.create();

    let contador = 1;

    for (const arquivo of arquivos) {

        console.log(`[${contador}/${arquivos.length}] ${arquivo}`);

        const bytes = fs.readFileSync(
            path.join(pastaPDFs, arquivo)
        );

        const pdf = await PDFDocument.load(bytes);

        const paginas = await pdfFinal.copyPages(
            pdf,
            pdf.getPageIndices()
        );

        paginas.forEach(p =>
            pdfFinal.addPage(p)
        );

        contador++;
    }

    const resultado = await pdfFinal.save();

    fs.writeFileSync(
        path.join(__dirname, "Atendi Docs.pdf"),
        resultado
    );

    console.log("");

    console.log("PDF final criado com sucesso!");

})();
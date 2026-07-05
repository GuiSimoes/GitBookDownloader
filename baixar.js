const { obterPaginas } = require("./src/sitemap");
const { gerarPDFs } = require("./src/pdf");

(async () => {

    const sitemap =
        "https://jose-eduardo-barbieri.gitbook.io/atendi-docs/sitemap-pages.xml";

    const paginas =
        await obterPaginas(sitemap);

    console.log(`${paginas.length} páginas encontradas.\n`);

    await gerarPDFs(paginas);

    console.log("\nConcluído!");

})();
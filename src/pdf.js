const path = require("path");
const { chromium } = require("playwright");
const {
    criarPasta,
    limparNome,
    numero
} = require("../utils");

async function gerarPDFs(paginas) {

    const pasta = path.join(__dirname, "PDFs");

    criarPasta(pasta);

    const browser = await chromium.launch({
        headless: true
    });

    const page = await browser.newPage({
        viewport: {
            width: 1440,
            height: 1800
        }
    });

    let contador = 1;

    for (const url of paginas) {

        console.log(`[${contador}/${paginas.length}]`);

        await page.goto(url, {
            waitUntil: "networkidle",
            timeout: 60000
        });

        await page.waitForTimeout(1000);

        const titulo = await page.locator("h1").textContent();

        const nome = `${numero(contador)} - ${limparNome(titulo)}.pdf`;

        console.log(nome);

        await page.pdf({
            path: path.join(pasta, nome),
            format: "A4",
            printBackground: true,
            margin: {
                top: "10mm",
                bottom: "10mm",
                left: "10mm",
                right: "10mm"
            }
        });

        contador++;
    }

    await browser.close();

}

module.exports = {
    gerarPDFs
};
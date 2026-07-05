const { parseStringPromise } = require("xml2js");

async function obterPaginas(urlSitemap) {

    console.log("Lendo sitemap...");

    const xml =
        await fetch(urlSitemap).then(r => r.text());

    const dados =
        await parseStringPromise(xml);

    return dados.urlset.url.map(x => x.loc[0]);

}

module.exports = {
    obterPaginas
};
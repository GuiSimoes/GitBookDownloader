const fs = require("fs");
const path = require("path");

function gerarMenu() {

    const siteIndex = JSON.parse(
        fs.readFileSync(
            path.join(__dirname, "..", "site-index.json"),
            "utf8"
        )
    );

    const menu = siteIndex.pages.map(pagina => ({

        titulo: pagina.title,

        url: pagina.pathname,

        nivel: (pagina.breadcrumbs?.length || 0) + 1

    }));

    fs.writeFileSync(

        path.join(__dirname, "..", "menu.json"),

        JSON.stringify(menu, null, 2),

        "utf8"

    );

    console.log(`${menu.length} itens salvos em menu.json`);

}

module.exports = {
    gerarMenu
};
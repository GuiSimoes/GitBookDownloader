const fs = require("fs");

function criarPasta(caminho) {
    if (!fs.existsSync(caminho)) {
        fs.mkdirSync(caminho, { recursive: true });
    }
}

function limparNome(nome) {
    return nome
        .replace(/[\\/:*?"<>|]/g, "")
        .replace(/\s+/g, " ")
        .trim();
}

function numero(valor, tamanho = 3) {
    return String(valor).padStart(tamanho, "0");
}

module.exports = {
    criarPasta,
    limparNome,
    numero
};
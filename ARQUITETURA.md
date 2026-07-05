# GitBookPDF - Arquitetura

## Objetivo

Baixar uma documentação GitBook e gerar um PDF profissional com navegação.

---

## Fluxo

GitBook URL
    ↓
Downloader (Node.js)
    ↓
PDFs individuais
    ↓
PDF único
    ↓
Mapa de páginas (JSON)
    ↓
Processamento (Python)
    ↓
PDF Final

---

## Estrutura do projeto

GitBookPDF
│
├── baixar.js
├── juntar.js
├── PDFs/
├── python/
│   ├── main.py
│   ├── config.py
│   ├── bookmarks.py
│   ├── indice.py
│   ├── mapa_paginas.py
│   └── montar_pdf.py
├── src/
└── README.md

---

## Responsabilidade dos módulos

### baixar.js
Baixa todas as páginas do GitBook e gera os PDFs individuais.

### juntar.js
Une todos os PDFs em um único arquivo.

### mapa_paginas.py
Gera o mapa de páginas utilizado pelas demais etapas.

### bookmarks.py
Cria a árvore de bookmarks do PDF.

### indice.py
Cria um índice clicável.

### montar_pdf.py
Executa a montagem final do PDF.

### main.py
Orquestra todo o processo.

### config.py
Centraliza configurações e caminhos do projeto.

---

## Roadmap

### V1.0 ✅
- Download do GitBook
- PDFs individuais
- PDF único

### V2.0 🚧
- Bookmarks
- Índice clicável
- Melhor navegação

### Futuro
- Interface gráfica
- Configuração por arquivo
- Suporte a qualquer GitBook
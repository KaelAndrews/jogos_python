# Jogos em Python

Uma coleção de jogos desenvolvidos em Python e executados diretamente no navegador usando Pyodide.

## Como Executar

1. Certifique-se de que o XAMPP (ou outro servidor web) está rodando
2. Abra `index.html` no navegador
3. Clique em "Jogar" no jogo desejado
4. Use o botão "Jogar Novamente" para executar novamente

## Primeiro Jogo: Jogo do Dado

- **Arquivo**: `jogos_python/dado.py`
- **Descrição**: Simula o lançamento de um dado de 6 faces
- **Funcionalidades**: Gera número aleatório entre 1 e 6

## Estrutura do Projeto

- `index.html`: Página principal com lista de jogos
- `css/styles.css`: Estilos para design responsivo e moderno
- `js/script.js`: JavaScript para interatividade e execução de Python via Pyodide
- `jogos_python/`: Pasta para armazenar os códigos Python dos jogos

## Como Adicionar um Novo Jogo

1. Crie um arquivo Python na pasta `jogos_python/` (ex: `jogo_novo.py`)
2. Escreva o código do jogo usando bibliotecas compatíveis com Pyodide
3. Adicione um card na seção `#jogos` do `index.html`
4. O sistema automaticamente carregará o arquivo baseado no nome passado para `carregarJogo()`

## Tecnologias Utilizadas

- HTML5
- CSS3 (com Flexbox e Grid)
- JavaScript (ES6+)
- Pyodide para execução de Python no navegador
- Google Fonts para tipografia

## Limitações e Considerações

- Jogos gráficos complexos podem não funcionar devido a limitações do Pyodide
- Input interativo é limitado; foque em jogos que usam output baseado em lógica
- Para jogos mais avançados, considere usar JavaScript para UI e Python para lógica via APIs

## Boas Práticas de UX

- Design responsivo para dispositivos móveis e desktop
- Transições suaves e feedback visual
- Carregamento assíncrono para melhor performance
- Acessibilidade com semântica HTML adequada
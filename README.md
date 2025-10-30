# Jogos em Python

Uma coleção de jogos desenvolvidos em Python e executados diretamente no navegador usando Pyodide.

## Estrutura do Projeto

- `index.html`: Página principal com lista de jogos
- `css/styles.css`: Estilos para design responsivo e moderno
- `js/script.js`: JavaScript para interatividade e execução de Python via Pyodide
- `jogos/`: Pasta para armazenar os códigos Python dos jogos

## Como Adicionar um Novo Jogo

1. Crie um arquivo Python na pasta `jogos/` (ex: `jogo_novo.py`)
2. Escreva o código do jogo usando bibliotecas compatíveis com Pyodide (como pygame, se disponível)
3. Adicione um card na seção `#jogos` do `index.html`
4. Modifique a função `carregarJogo` no `script.js` para carregar o arquivo Python específico

## Exemplo de Código Python

```python
# jogo_exemplo.py
import pygame
# Código do jogo aqui
```

## Tecnologias Utilizadas

- HTML5
- CSS3 (com Flexbox e Grid)
- JavaScript (ES6+)
- Pyodide para execução de Python no navegador
- Google Fonts para tipografia

## Boas Práticas de UX

- Design responsivo para dispositivos móveis e desktop
- Transições suaves e feedback visual
- Carregamento assíncrono para melhor performance
- Acessibilidade com semântica HTML adequada

## Como Executar

Abra o `index.html` em um navegador web moderno. Certifique-se de que o servidor web (como XAMPP) esteja rodando para evitar problemas de CORS.
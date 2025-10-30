// script.js - Interatividade para Jogos em Python

let pyodide = null;

// Inicializar Pyodide
async function initPyodide() {
    if (!pyodide) {
        pyodide = await loadPyodide({
            indexURL: "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/"
        });
    }
    return pyodide;
}

// Função para carregar um jogo
async function carregarJogo(nomeJogo) {
    const listaJogos = document.getElementById('jogos');
    const containerJogo = document.getElementById('jogo-container');
    const tituloJogo = document.getElementById('titulo-jogo');
    const canvasContainer = document.getElementById('canvas-container');

    // Esconder lista e mostrar container do jogo
    listaJogos.style.display = 'none';
    containerJogo.style.display = 'block';

    tituloJogo.textContent = `Jogo: ${nomeJogo.charAt(0).toUpperCase() + nomeJogo.slice(1)}`;

    // Limpar container anterior
    canvasContainer.innerHTML = '<p>Carregando jogo...</p>';

    try {
        // Inicializar Pyodide se necessário
        const py = await initPyodide();

        // Aqui você pode carregar o código Python do jogo
        // Por exemplo, de um arquivo na pasta jogos/
        // Para demonstração, vamos executar um código simples
        const codigoPython = `
import sys
print("Olá! Este é um jogo em Python executado no navegador.")
print("Nome do jogo:", "${nomeJogo}")
`;

        // Executar o código Python
        py.runPython(codigoPython);

        // Para jogos mais complexos, você pode usar bibliotecas como pygame via pyodide
        // Exemplo: py.runPython(await fetch('jogos/${nomeJogo}.py').then(r => r.text()));

        canvasContainer.innerHTML = '<pre>' + py.runPython('sys.stdout.getvalue()') + '</pre>';

    } catch (error) {
        canvasContainer.innerHTML = '<p>Erro ao carregar o jogo: ' + error.message + '</p>';
    }
}

// Função para voltar à lista de jogos
function voltarParaLista() {
    const listaJogos = document.getElementById('jogos');
    const containerJogo = document.getElementById('jogo-container');

    containerJogo.style.display = 'none';
    listaJogos.style.display = 'block';
}

// Inicializar quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
    console.log('Página de Jogos em Python carregada.');
});
// script.js - Interatividade para Jogos em Python

let pyodide = null;
let codigoPythonAtual = '';

// Inicializar Pyodide
async function initPyodide() {
    if (!pyodide) {
        pyodide = await loadPyodide({
            indexURL: "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/"
        });
        // Instalar micropip se necessário para pacotes adicionais
        await pyodide.loadPackage("micropip");
    }
    return pyodide;
}

// Função para carregar código Python de um arquivo
async function carregarCodigoPython(caminho) {
    const response = await fetch(caminho);
    if (!response.ok) {
        throw new Error(`Erro ao carregar ${caminho}: ${response.statusText}`);
    }
    return await response.text();
}

// Função para executar código Python
async function executarCodigoPython(codigo) {
    const py = await initPyodide();

    // Preparar captura de output
    py.runPython('import sys; sys.stdout = __import__("io").StringIO()');

    // Executar o código
    py.runPython(codigo);

    // Capturar output
    return py.runPython('sys.stdout.getvalue()');
}

// Função para carregar um jogo
async function carregarJogo(nomeJogo) {
    const listaJogos = document.getElementById('jogos');
    const containerJogo = document.getElementById('jogo-container');
    const tituloJogo = document.getElementById('titulo-jogo');
    const canvasContainer = document.getElementById('canvas-container');
    const controlesJogo = document.getElementById('controles-jogo');

    // Esconder lista e mostrar container do jogo
    listaJogos.style.display = 'none';
    containerJogo.style.display = 'block';

    tituloJogo.textContent = `Jogo: ${nomeJogo.charAt(0).toUpperCase() + nomeJogo.slice(1)}`;

    // Limpar container anterior
    canvasContainer.innerHTML = '<p>Carregando jogo...</p>';
    controlesJogo.style.display = 'none';

    try {
        // Carregar o código Python do arquivo
        const caminhoArquivo = `jogos_python/${nomeJogo}.py`;
        codigoPythonAtual = await carregarCodigoPython(caminhoArquivo);

        // Executar o jogo pela primeira vez
        await executarJogo();

        // Mostrar controles
        controlesJogo.style.display = 'block';

    } catch (error) {
        canvasContainer.innerHTML = '<p>Erro ao carregar o jogo: ' + error.message + '</p>';
    }
}

// Função para executar o jogo atual
async function executarJogo() {
    const canvasContainer = document.getElementById('canvas-container');

    try {
        const output = await executarCodigoPython(codigoPythonAtual);
        canvasContainer.innerHTML = '<pre>' + output + '</pre>';
    } catch (error) {
        canvasContainer.innerHTML = '<p>Erro ao executar o jogo: ' + error.message + '</p>';
    }
}

// Função para voltar à lista de jogos
function voltarParaLista() {
    const listaJogos = document.getElementById('jogos');
    const containerJogo = document.getElementById('jogo-container');

    containerJogo.style.display = 'none';
    listaJogos.style.display = 'block';
    codigoPythonAtual = '';
}

// Inicializar quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
    console.log('Página de Jogos em Python carregada.');

    // Adicionar evento ao botão jogar novamente
    const btnJogarNovamente = document.getElementById('btn-jogar-novamente');
    if (btnJogarNovamente) {
        btnJogarNovamente.addEventListener('click', executarJogo);
    }
});
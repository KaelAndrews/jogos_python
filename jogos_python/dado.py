import random

def jogar_dado():
    print("Bem-vindo ao Jogo do Dado!")
    print("Lançando o dado...")
    resultado = random.randint(1, 6)
    print(f"Você tirou: {resultado}")
    return resultado

# Executar o jogo
jogar_dado()
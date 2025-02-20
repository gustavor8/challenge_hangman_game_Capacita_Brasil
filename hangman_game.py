import random

# Lista com os estágios da forca
FORCA_ESTAGIOS = [
    """
       ------
       |    |
       |    
       |   
       |   
       |   
    """,
    """
       ------
       |    |
       |    O
       |   
       |   
       |   
    """,
    """
       ------
       |    |
       |    O
       |    |
       |   
       |   
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |   
       |   
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   
       |   
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |   
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |   
    """
]

# Dicionário de temas com listas de palavras
TEMAS = {
    "frutas": ["banana", "siriguela", "jabuticaba", "melancia", "morango"],
    "animais": ["ornitorrinco", "golfinho", "gato", "tamandua", "girafa"],
    "países": ["brasil", "canada", "tajiquistao", "mexico", "singapura"],
    "computação": ["python", "desenvolvimento", "computador", "programacao", "teclado"]
}

def escolher_tema():
    """Exibe os temas disponíveis e permite ao usuário escolher um."""
    print("Escolha um tema:")
    temas_lista = list(TEMAS.keys())
    for i, tema in enumerate(temas_lista, 1):
        print(f"{i}. {tema.capitalize()}")
    
    while True:
        try:
            escolha = int(input("Digite o número do tema: ")) - 1
            if 0 <= escolha < len(temas_lista):
                return temas_lista[escolha]
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def escolher_palavra(tema):
    """Escolhe uma palavra aleatória dentro do tema fornecido."""
    return random.choice(TEMAS[tema])

def exibir_status(palavra_oculta, letras_erradas, tentativas_restantes):
    """Exibe o estado atual do jogo, incluindo a forca, palavra oculta e tentativas restantes."""
    print(FORCA_ESTAGIOS[len(FORCA_ESTAGIOS) - 1 - tentativas_restantes])
    print("Palavra:", " ".join(palavra_oculta))
    print(f"Tentativas restantes: {tentativas_restantes}")
    print(f"Letras erradas: {', '.join(letras_erradas)}\n")
    
def continueGame():
    """Pergunta ao jogador se deseja jogar novamente e reinicia o jogo caso positivo."""
    while True:
        resposta = input("Deseja jogar novamente? (y/n): ").strip().lower()
        if resposta == "y":
            jogo_da_forca()
            break  # Evita chamadas recursivas infinitas
        elif resposta == "n":
            print("Obrigado por jogar! 🎮")
            exit()  # Encerra o programa corretamente
        else:
            print("Opção inválida. Digite 'y' para continuar ou 'n' para sair.")


def jogo_da_forca():
    """Função principal que executa o jogo da forca."""
    print("🎯 Bem-vindo ao Jogo da Forca! 🎯\n")
    
    tema_escolhido = escolher_tema()
    palavra_escolhida = escolher_palavra(tema_escolhido).lower()
    palavra_oculta = ["_"] * len(palavra_escolhida)
    letras_erradas = []
    tentativas_restantes = len(FORCA_ESTAGIOS) - 1
    
    while tentativas_restantes > 0 and "_" in palavra_oculta:
        exibir_status(palavra_oculta, letras_erradas, tentativas_restantes)
        tentativa = input("Digite uma letra: ").lower()
        
        if tentativa in palavra_escolhida:
            for i, letra in enumerate(palavra_escolhida):
                if letra == tentativa:
                    palavra_oculta[i] = tentativa
        else:
            if tentativa not in letras_erradas:
                letras_erradas.append(tentativa)
                tentativas_restantes -= 1
        
        print("\n" + "=" * 50 + "\n")
    
    if "_" not in palavra_oculta:
        print("🎉 Parabéns! Você acertou a palavra:", palavra_escolhida)
        continueGame()
    else:
        print(FORCA_ESTAGIOS[-1])
        print("💀 Você perdeu! A palavra era:", palavra_escolhida)
        continueGame()


if __name__ == "__main__":
    jogo_da_forca()

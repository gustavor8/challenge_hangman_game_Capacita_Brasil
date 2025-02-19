import random

# Lista com os estágios da forca
forca_estagios = [
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
temas = {
    "frutas": ["banana", "siriguela", "jabuticaba", "melancia", "morango"],
    "animais": ["ornitorrinco", "golfinho", "gato", "tamandua", "girafa"],
    "países": ["brasil", "canada", "tajiquistao", "mexico", "singapura"],
    "computação": ["python", "desenvolvimento", "computador", "programacao", "teclado"]
}

# Função para escolher uma palavra aleatória de um tema
def escolher_palavra(tema):
    return random.choice(temas[tema])

print("🎯 Bem-vindo ao Jogo da Forca! 🎯\n")

# Exibir temas disponíveis
print("Escolha um tema:")
for i, tema in enumerate(temas.keys(), 1):
    print(f"{i}. {tema.capitalize()}")

# Solicitar escolha do tema
escolha = int(input("Digite o número do tema: ")) - 1
tema_escolhido = list(temas.keys())[escolha]

# Escolher uma palavra aleatória do tema selecionado
palavra_escolhida = escolher_palavra(tema_escolhido).lower()
palavra_oculta = ["_"] * len(palavra_escolhida)
letras_erradas = []
tentativas_restantes = len(forca_estagios) - 1  # Número de chances


while tentativas_restantes > 0 and "_" in palavra_oculta:
    print(forca_estagios[len(forca_estagios) - 1 - tentativas_restantes])  # Exibe o estágio atual da forca
    print("Palavra: ", " ".join(palavra_oculta))
    print(f"Tentativas restantes: {tentativas_restantes}")
    print(f"Letras erradas: {', '.join(letras_erradas)}\n")

    tentativa = input("Digite uma letra: ").lower()

    # Veirfica se a letra tem na palavra oculta
    if tentativa in palavra_escolhida:
        # Atualiza a palavra oculta com a letra correta
        for i, letra in enumerate(palavra_escolhida):
            if letra == tentativa:
                palavra_oculta[i] = tentativa
    else:
        if tentativa not in letras_erradas:
            letras_erradas.append(tentativa)
            tentativas_restantes -= 1

    print("\n" + "=" * 50 + "\n")  # Separador visual

# Resultado final
if "_" not in palavra_oculta:
    print("🎉 Parabéns! Você acertou a palavra:", palavra_escolhida)
else:
    print(forca_estagios[-1])  # Exibe a forca completa
    print("💀 Você perdeu! A palavra era:", palavra_escolhida)

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

import random

# Lista de palavras
palavras = ["python", "desenvolvimento", "computador", "programacao", "teclado"]

# Escolhe uma palavra aleatória
palavra_escolhida = random.choice(palavras).lower()
palavra_oculta = ["_"] * len(palavra_escolhida)
letras_erradas = []
tentativas_restantes = len(forca_estagios) - 1  # Número de chances

print("🎯 Bem-vindo ao Jogo da Forca!\n")

while tentativas_restantes > 0 and "_" in palavra_oculta:
    print(forca_estagios[len(forca_estagios) - 1 - tentativas_restantes])  # Exibe o estágio atual da forca
    print("Palavra: ", " ".join(palavra_oculta))
    print(f"Tentativas restantes: {tentativas_restantes}")
    print(f"Letras erradas: {', '.join(letras_erradas)}\n")

    tentativa = input("Digite uma letra: ").lower()

    if tentativa in palavra_escolhida:
        # Atualiza a palavra oculta com a letra correta
        for i, letra in enumerate(palavra_escolhida):
            if letra == tentativa:
                palavra_oculta[i] = tentativa
    else:
        if tentativa not in letras_erradas:
            letras_erradas.append(tentativa)
            tentativas_restantes -= 1

    print("\n" + "=" * 30 + "\n")  # Separador visual

# Resultado final
if "_" not in palavra_oculta:
    print("🎉 Parabéns! Você acertou a palavra:", palavra_escolhida)
else:
    print(forca_estagios[-1])  # Exibe a forca completa
    print("💀 Você perdeu! A palavra era:", palavra_escolhida)

import random

# Função para carregar palavras do arquivo
def carregar_palavras(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        return [linha.strip().lower() for linha in f.readlines()]

# Função para carregar estágios do enforcado
def carregar_enforcado(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        return f.read().split("\n\n")  # Separa os estágios pelo espaço entre eles

# Função para imprimir o enforcado
def imprime_enforcado(erros, estagios):
    print(estagios[erros])  # Mostra o estágio do enforcado correspondente ao erro

# Carregar palavras e estágios do enforcado
palavras = carregar_palavras("gabarito_forca.txt")
estagios = carregar_enforcado("gabarito_enforcado.txt")

# Escolher palavra aleatória
palavra_secreta = random.choice(palavras)
palavra_oculta = ["_"] * len(palavra_secreta)  # Exibir "_" no lugar das letras
tentativas = 6
erros = 0
letras_tentadas = set()

print("Bem-vindo ao Jogo da Forca!\n")
print(" ".join(palavra_oculta))  # Exibir "_" para cada letra

# Loop principal do jogo
while erros < tentativas and "_" in palavra_oculta:
    letra = input("\nDigite uma letra: ").lower()

    # Verifica se a letra já foi tentada
    if letra in letras_tentadas:
        print("Você já tentou essa letra. Tente outra!")
        continue

    letras_tentadas.add(letra)

    if letra in palavra_secreta:
        # Substituir os "_" pelas letras corretas
        for i, l in enumerate(palavra_secreta):
            if l == letra:
                palavra_oculta[i] = letra
    else:
        erros += 1
        print("\nLetra errada! Você tem mais", tentativas - erros, "tentativas.")
        imprime_enforcado(erros, estagios)

    print("\n" + " ".join(palavra_oculta))  # Atualizar a palavra oculta

# Verifica se o jogador ganhou ou perdeu
if "_" not in palavra_oculta:
    print("\n🎉 Parabéns! Você acertou a palavra:", palavra_secreta)
else:
    print("\n💀 Você perdeu! A palavra era:", palavra_secreta)

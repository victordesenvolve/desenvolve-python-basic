from collections import Counter

def encontrar_anagramas(string, palavra_objetivo):
    # Tamanho da palavra objetivo
    tamanho_palavra = len(palavra_objetivo)
    
    # Contagem de caracteres da palavra objetivo
    contador_objetivo = Counter(palavra_objetivo)
    
    # Lista para armazenar os índices dos anagramas encontrados
    anagramas = []
    
    # Janela deslizante, começando no índice 0
    for i in range(len(string) - tamanho_palavra + 1):
        # Substring atual da janela
        janela = string[i:i + tamanho_palavra]
        
        # Contagem de caracteres da janela
        contador_janela = Counter(janela)
        
        # Se a contagem da janela for igual à da palavra objetivo, é um anagrama
        if contador_janela == contador_objetivo:
            anagramas.append(janela)
    
    return anagramas

# Exemplo de uso:
string = "cbaebabacd"
palavra_objetivo = "abc"
resultados = encontrar_anagramas(string, palavra_objetivo)
print(resultados)

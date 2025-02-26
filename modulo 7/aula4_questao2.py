import os
import re  

# Nome dos arquivos
arquivo_origem = "frase.txt"
arquivo_destino = "palavras.txt"

# Verifica se o arquivo original existe
if not os.path.exists(arquivo_origem):
    print(f"Erro: O arquivo '{arquivo_origem}' não foi encontrado.")
else:
    # Lê o conteúdo do arquivo original
    with open(arquivo_origem, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    # Remove caracteres não alfabéticos e divide em palavras
    palavras = re.findall(r'\b[A-Za-zÀ-ÿ]+\b', conteudo)  # Mantém palavras com acentos

    # Salva as palavras no novo arquivo, uma por linha
    with open(arquivo_destino, "w", encoding="utf-8") as arquivo:
        for palavra in palavras:
            arquivo.write(palavra + "\n")

    # Lê e imprime o conteúdo do novo arquivo
    with open(arquivo_destino, "r", encoding="utf-8") as arquivo:
        print("Conteúdo do arquivo 'palavras.txt':\n")
        print(arquivo.read())

frase = input("Digite uma frase para contarmos as vogais: ")

vogais = "aeiouAEIOU"

contador_vogais = 0

for char in frase:
    if char in vogais:
        contador_vogais += 1  


print(f"A frase contém {contador_vogais} vogais.")
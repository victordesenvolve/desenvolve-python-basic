
frase = input("Digite uma frase: ")


vogais = "aeiouAEIOU"


frase_modificada = "".join(["*" if char in vogais else char for char in frase])


print("Frase modificada:", frase_modificada)

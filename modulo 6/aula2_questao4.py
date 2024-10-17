
def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    min_len = min(len(lista1), len(lista2))

   
    for i in range(min_len):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])

   
    lista_intercalada.extend(lista1[min_len:])
    lista_intercalada.extend(lista2[min_len:])
    
    return lista_intercalada

qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []


print(f"Digite os {qtd1} elementos da lista 1:")
for _ in range(qtd1):
    elemento = int(input())
    lista1.append(elemento)


qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []


print(f"Digite os {qtd2} elementos da lista 2:")
for _ in range(qtd2):
    elemento = int(input())
    lista2.append(elemento)


lista_intercalada = intercalar_listas(lista1, lista2)

print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))

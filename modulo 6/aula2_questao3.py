import random
from collections import Counter


lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]


interseccao = list(set(lista1) & set(lista2))


interseccao.sort()


contador1 = Counter(lista1)
contador2 = Counter(lista2)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção ordenada:", interseccao)
print("\nContagem de elementos:")
print("Elemento : Lista 1 | Lista 2")
for elemento in sorted(set(lista1) | set(lista2)):
    print(f"{elemento:8} : {contador1[elemento]:8} | {contador2[elemento]:8}")

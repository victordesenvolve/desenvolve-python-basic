import random


original = [random.randint(-10, 10) for _ in range(20)]


print("Original:", original)

max_negativos = 0
inicio_intervalo = 0
fim_intervalo = 0

for i in range(len(original)):
    for j in range(i, len(original)):
      
        cont_negativos = sum(1 for k in original[i:j + 1] if k < 0)
        
       
        if cont_negativos > max_negativos:
            max_negativos = cont_negativos
            inicio_intervalo = i
            fim_intervalo = j


del original[inicio_intervalo:fim_intervalo + 1]


print("Editada:", original)

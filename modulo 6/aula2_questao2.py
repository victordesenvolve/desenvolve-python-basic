#Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos.
#Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, 
#e armazene em uma lista chamada elementos. 

import random

num_elementos = random.randint(5, 20)

print(num_elementos)

elementos = [random.randint(1, 10) for _ in range(num_elementos)]

print(elementos)

soma_elementos = sum(elementos)

print(soma_elementos)

media = soma_elementos/num_elementos
print(media)
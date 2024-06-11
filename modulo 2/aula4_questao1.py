#1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro
#quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.

#O terreno possui 250m2 e custa R$512,490.50

#Comente na linha acima de cada instrução uma breve descrição da instrução.

#Fórmulas:
#area_m2 = comprimento * largura
#preco_total = preco_m2 * area_m2]

terreno_comprimento = int(input('Qual o comprimento do terreno?'))
terreno_largura = int(input('Qual a largura do terreno?'))

preco_m2 = 1000
area_m2 = terreno_comprimento * terreno_largura
preco_total = preco_m2 * area_m2
print (f"O terreno possui {area_m2}m2 e custa R${preco_total}")

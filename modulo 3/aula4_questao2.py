#Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. 
#Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5.
#O programa deve imprimir uma mensagem correspondente à classificação do filme:
#Se a avaliação for 5, imprima "Excelente!"
#Se a avaliação for 4, imprima "Muito Bom!"
#Se a avaliação for 3, imprima "Bom!"
#Se a avaliação for 2, imprima "Regular."
#Se a avaliação for 1, imprima "Ruim."

nota = int(input('Qual sua nota para o filme? De 0 até 5.'))
if nota > 5 or nota < 0:
    print("Eu pedi nota de 0 até 5.")
else:
    if nota == 0:
        print("Horrivel")
    if nota == 1:
        print("Ruim")
    if nota == 2:
        print("Regular")
    if nota == 3:
        print("Bom") 
    if nota == 4:
        print("Ótimo")
    if nota == 5:
        print("Excelente")     
                  
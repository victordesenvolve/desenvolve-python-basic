#Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores),
# os armazena em uma lista e, usando fatiamento de listas, imprima:
#A lista original
#Os 3 primeiros elementos
#Os 2 últimos elementos
#A lista invertida (do fim para o começo)
#Os elementos de índice par (0, 2, 4 … )
#Os elementos de índice ímpar (1, 3, 5, … )

numeros = []

while True:
    valor = input("Informe 4 ou mais números, ou digite 'fim' para parar: ")

    if valor == "fim":
        if len(numeros) < 4:
            print("Informe pelo menos 4 números.")
            numeros.clear() 
        else:
            print("Números informados:", numeros)
            break  
    else:
        numeros.append(valor)

      ###################

print(numeros[0:3])

print(numeros[-3:-1])






   
    
            

          
             
        
       



